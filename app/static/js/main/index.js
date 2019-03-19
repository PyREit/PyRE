// Link al repo github
$(window).scroll(function() {
	if ($(window).scrollTop() >= (($(document).height() - $(window).height()) - $('.call-to-action').innerHeight()) && location.pathname == '/') {
		toastr.options = {
			"closeButton": true,
		    "positionClass": "toast-bottom-right", // toast-top-right / toast-top-left / toast-bottom-right / toast-bottom-left
			"preventDuplicates": true,
		    "showDuration": "7000", // in milliseconds
		    "hideDuration": "1000", // in milliseconds
		    "timeOut": "5000", // in milliseconds
		    "extendedTimeOut": "1000", // in milliseconds
		    "showEasing": "swing",
		    "hideEasing": "linear",
		    "showMethod": "fadeIn",
		    "hideMethod": "fadeOut"
		};
		toastr.options.onclick = function() { window.location.assign("https://github.com/pyreit/PyRE"); };
		toastr.success('Scopri come abbiamo sviluppato questo sito!', 'How it is made');
	  }
});

//setTimeout(function showModal() {$('#provvisorio').modal('show');}, 2500);