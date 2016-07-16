function previewColor() {
	var red = document.getElementById("RED");
	var green = document.getElementById("GREEN");
	var blue = document.getElementById("BLUE");

	var rp = document.getElementById('red-color-preview');
	var gp = document.getElementById('green-color-preview');
	var bp = document.getElementById('blue-color-preview');
	rp.children[1].innerHTML = "RED: " + red.value
	gp.children[1].innerHTML = "GREEN: " + green.value
	bp.children[1].innerHTML = "BLUE: " + blue.value
	this.rgbString = "rgb(" + red.value + ", " +green.value + ", " + blue.value + ")"
//	console.log(this.rgbString)
	rp.style.backgroundColor = this.rgbString;
	gp.style.backgroundColor = this.rgbString;
	bp.style.backgroundColor = this.rgbString;
}
window.onload = function() { 
	var red = document.getElementById("RED");
	var green = document.getElementById("GREEN");
	var blue = document.getElementById("BLUE");
	blue.addEventListener("input", previewColor);
	green.addEventListener("input", previewColor);
	red.addEventListener("input", previewColor);
}
