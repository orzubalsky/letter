import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.generic import ListView
from django.core import serializers
from django.core.urlresolvers import reverse_lazy
from django.db import IntegrityError
from letters.models import Letter, Signature
from letters.forms import SignatureForm
from basic.models import Person
from cms.models import ContentBlock
from basic.forms import PersonForm


class LetterList(ListView):
    """
    """
    queryset = Letter.objects.filter(is_active=True)
    context_object_name = 'letter_list'
    template_name = 'letter_list.html'


def home(request):
    """
    """
    letter = Letter.objects.get(pk=1)

    return HttpResponseRedirect(reverse_lazy(
        'letters:letter-detail',
        kwargs={
            'slug': letter.slug,
        },
        current_app='letters')
    )

def letter_detail(request, slug=None, data=None):
    """
    """
    letter = get_object_or_404(Letter, slug=slug)
    content_blocks = ContentBlock.objects.filter(is_active=True)

    if request.method == 'POST':
        data = request.POST

    if data is not None or request.method == 'POST':
        person_form = PersonForm(data=data, prefix="person")
        signature_form = SignatureForm(data=data, prefix="signature")

        if person_form.is_valid():
            # save person
            person = person_form.save(commit=False)
            person_data = person_form.cleaned_data

            person = Person.objects.filter(email=person_data['email'])

            if person.exists():
                person = person[0]

                # keep this object in case something goes wrong
                # when saving the registration
                original_person = person

                # update student data from form
                person.name = person_data['name']
            else:
                person = Person(**person_data)

            person.save()

            if signature_form.is_valid():

                # save signature
                signature_data = signature_form.cleaned_data

                signature = Signature(
                    person=person,
                    letter=letter,
                    comment=signature_data['comment']
                )

                # try saving the signature.
                # this may fail because of the unique_together db constraint
                # an IntegrityError will occur
                try:
                    signature.save()
                    return HttpResponse(
                        serializers.serialize('json', [person, ]))

                # in case saving the signature failed
                # (see comment above the try block),
                # add an error to the signature form
                except IntegrityError:

                    # restore data
                    person.name = original_person.name
                    person.save()

                    # display error
                    signature_form._errors['errors'] = \
                        signature_form.error_class(
                            ['Looks like you already signed this letter', ])

                    return HttpResponse(json.dumps(
                        signature_form.errors))

    else:
        signature_form = SignatureForm(prefix="signature")
        person_form = PersonForm(prefix="person")

    return render(request, 'letter_detail.html', {
        'letter': letter,
        'content_blocks': content_blocks,
        'person_form': person_form,
        'signature_form': signature_form,
    })
