var flashSuccess = ".flash-success";
var flashError = ".flash-error";

toastr.options.timeOut = 3000
toastr.options.extendedTimeout = 6000
toastr.options.newestOnTop = false
toastr.options.positionClass = "toast-bottom-right"

if ($(flashSuccess).length ) {
	toastr.success($(flashSuccess).text() )
};

if ($(flashError).length ) {
	toastr.error($(flashError).text() )
};

function imgError(image) {
	image.onerror = "";
	alert("Error retrieving image.");
	image.src = "/static/images/default-team-img.svg";
	return true;
}