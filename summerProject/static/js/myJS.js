// // Dropdown Menu
// var dropdown = document.querySelectorAll('.dropdown');
// var dropdownArray = Array.prototype.slice.call(dropdown,0);
// dropdownArray.forEach(function(el){
// 	var button = el.querySelector('a[data-toggle="dropdown"]'),
// 			menu = el.querySelector('.dropdown-menu'),
// 			arrow = button.querySelector('i.icon-arrow');
//
// 	button.onclick = function(event) {
// 		if(!menu.hasClass('show')) {
// 			menu.classList.add('show');
// 			menu.classList.remove('hide');
// 			arrow.classList.add('open');
// 			arrow.classList.remove('close');
// 			event.preventDefault();
// 		}
// 		else {
// 			menu.classList.remove('show');
// 			menu.classList.add('hide');
// 			arrow.classList.remove('open');
// 			arrow.classList.add('close');
// 			event.preventDefault();
// 		}
// 	};
// })
//
// Element.prototype.hasClass = function(className) {
//     return this.className && new RegExp("(^|\\s)" + className + "(\\s|$)").test(this.className);
// };
//
// $('#myNavbar').onclick = function(event){
// 	if(!menu.hasClass('show')) {
// 		menu.classList.add('show');
// 		menu.classList.remove('hide');
// 		arrow.classList.add('open');
// 		arrow.classList.remove('close');
// 		event.preventDefault();
// 	}
// 	else {
// 		menu.classList.remove('show');
// 		menu.classList.add('hide');
// 		arrow.classList.remove('open');
// 		arrow.classList.add('close');
// 		event.preventDefault();
// 	}
// }


//movie api

var movies = ['Harry Potter', "Power Rangers","Star Wars: Rogue One"];
var start = true;
var SImage;
var curr;
var currMovie;
var RandomThing;
var RandomThing2;
function MovieCall(){

	// var RandomThing = movies[Math.floor(Math.random() * movies.length)];
	// var RandomThing2 = movies[Math.floor(Math.random() * movies.length)];

if(start === true){
		RandomThing = movies[Math.floor(Math.random() * movies.length)];
		RandomThing2 = movies[Math.floor(Math.random() * movies.length)];
		$.getJSON("https://api.themoviedb.org/3/search/movie?api_key=1fbd48e9fd1b23d25b35bce4481f52a0&query=" + encodeURI(RandomThing) + "&page=1").then(function(response){
		var image = response.results[0].poster_path;

		if(image !== "N/A"){
			$('#curr').attr('src',"https://image.tmdb.org/t/p/w500/" + image);
		}

		console.log(response.results[0]);
		start = false;
		console.log(curr);
	});
	currMovie = RandomThing;

}
else{
	currMovie = RandomThing2;
	 $('#curr').attr('src', curr[0].currentSrc);
}

RandomThing2 = movies[Math.floor(Math.random() * movies.length)];
	$.getJSON("https://api.themoviedb.org/3/search/movie?api_key=1fbd48e9fd1b23d25b35bce4481f52a0&query=" + encodeURI(RandomThing2) + "&page=1").then(function(response){
		var image2 = response.results[0].poster_path;

		if(image2 !== "N/A"){
			$('#next').attr('src',"https://image.tmdb.org/t/p/w500/" + image2);
		}
		currMovie = RandomThing2;

		curr = ($('#next'));
	});

		$('h3').text(currMovie)
}

$('button').click(function(){
	MovieCall();
});
