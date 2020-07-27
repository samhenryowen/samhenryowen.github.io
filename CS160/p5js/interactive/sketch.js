function setup() {

createCanvas(600,480)
ellipseMode(CENTER);
}

function draw() {

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