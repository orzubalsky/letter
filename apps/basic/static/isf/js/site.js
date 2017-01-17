;(function($){
var site = window.site = new function()
{
    this.init = function()
    {
        this.sticky_navigation();
    };

    this.sticky_navigation = function()
    {
    	var $navbar = $('.navbar');
	    var elem_top_initial = $navbar.offset().top;
	    var subheader = $('.intro-text .name').text();

    	$(window).on('scroll', function(e)
        {
        	var doc_top = $(window).scrollTop();
	        var elem_top = $navbar.offset().top;

	        if (doc_top >= elem_top_initial)
	        {
				$navbar.addClass('navbar-fixed-top');
				$('body').addClass('with-navbar-fixed-top');
				$('.isf').text('')
				$('.subheader').text('#J20 ART STRIKE');
	        }
	        else
	        {
	        	$navbar.removeClass('navbar-fixed-top');
	        	$('body').removeClass('with-navbar-fixed-top');
				$('.isf').text('#J20 ART STRIKE')
	        	$('.subheader').text('');
	        }
	    });
    };
};
})(jQuery);

$(document).ready(function()
{
	site.init();
});