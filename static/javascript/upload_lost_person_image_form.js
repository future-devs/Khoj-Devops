$(document).ready(function(){

	$("#search_button").click(function() {
		let images_list = $('#loster_image')[0].files;
		console.log(images_list)
		console.log(images_list.length);
		if(images_list.length > 10) {
			alert("Sorry, you can upload only 5 images.");
		}
	});

});