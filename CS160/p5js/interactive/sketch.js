function setup() {
alert("Hello,\nChange colors with b,r,g,B,w\nChange brush size with up and down arrows\nChange shapes with left and right arrows\n\nIf you forget press 'h' for a console message with these commands.")
var boxlength = prompt("Enter drawing box length in px:")
var boxwidth = prompt("Enter drawing box width in px:")
createCanvas(boxlength,boxwidth)
ellipseMode(CENTER);
createDrawing();
brushSize = 10;
fillColor = 0;
shapeValue = ellipse
}

function draw() {
	shapeValue(mouseX,mouseY,brushSize,brushSize);

	if(mouseIsPressed) { fill(fillColor); }
	else { 
		stroke(255,255,255,0);
		fill(255,255,255,0);
	}

	if(keyIsPressed) {
		if (keyCode == UP_ARROW) { brushSize = brushSize + 2; }
		if (keyCode == DOWN_ARROW) { brushSize = brushSize - 2; }

		if (key == 'b') { fillColor = "#0000FF"; }
		if (key == 'r') { fillColor = "#FF0000"; }
		if (key == 'g') { fillColor = "#00FF00"; }
		if (key == 'B') { fillColor = "#000000"; }
		if (key == 'w') { fillColor = "#FFFFFF"; }

		if (keyCode == LEFT_ARROW) { shapeValue = rect; }
		if (keyCode == RIGHT_ARROW) { shapeValue = ellipse; }

		if (key == 'h') {
			print("Change colors with b,r,g,B,w\nChange brush size with up and down arrows\nChange shapes with left and right arrows");
		}

	}
}

function createDrawing() {
	background(204);
	fill(255,100,50,255);
	strokeWeight(1);
	ellipse(100,100,200);
	strokeWeight(2);
	fill(50,255,50,225);
	ellipse(200,200,200);
	strokeWeight(6);
	fill(50,50,255,205);
	ellipse(300,300,200);
	strokeWeight(12);
	fill(255,255,50,185);
	ellipse(400,400,200);
	strokeWeight(10);
	fill(50,255,255,165);
	rect(400,50,150,150);
	strokeWeight(75);
	fill(255,50,255,145);
	ellipse(0,480,400,400);
	strokeWeight(2);
	line(0,0,599,479);
	line(0,240,599,479);
	line(240,0,599,479);
}