// The Foundation
let particles = []
let score = 0;
let maxScore = 10;
let binX, binY, binW, binH;

// The Setup Function
function setup() {
  createCanvas(600, 400);
  
  binW = 100; // Sets bin width
  binH = 150; // Sets bin height
  binX = width / 2 - binW / 2; // Centers the bin
  binY = height - binH - 40; // Positions bin 40 pixels from the bottom
}

function draw() {
  background(20, 30, 50); //Fills canvas dark blue color
  
  fill(80, 150, 100); // Fills bin color to green
  noStroke();
  rect(binX, binY, binW, binH, 10); // 10 is rounded corners
  
  fill(255); // Text color to white
  textSize(16);
  textAlign(CENTER);
  text("Trash Bin", width / 2, binY - 10); // 200-10=200. 10 pixels above the bin
  
  for (let i = particles.length - 1; i >= 0; i--) {
    let p = particles[i]; // Creates a shorthand variable called p
    
    p.x += p.vx; // Moves the particles horizontally by its velocity
    p.y += p.vy; // Moves particles vertically
    p.alpha -+ 5; // Makes particle fade out
    
    fill(p.r, p.g, p.b, p.alpha); // Set color
    noStroke();
    circle(p.x, p.y, p.size); // Draw circle at particle's position with its size
    
    if (p.alpha <= 0) { // If particle is invisible
      particle.splice(i, 1); //Remove it from the array
    }
  }
  
  // Score display
  fill(255);
  noStroke();
  textSize(18);
  textAlign(CENTER);
  text("Cleanliness Score: " + score + " / " + maxScore, width / 2, 30); // maxscore variable is 10. 30 pixels from the top
  
  textSize(14);
  text("Click inside the bin to throw waste!", width / 2, height - 20);
  
  textSize(14);
  text("Click inside the bin to throw waste!", width / 2, height - 20);
}

function mousePressed() {
  if (mouseX > binX && mouseX < binX + binW && 
      mouseY > binY && mouseY < binY + binH) {
    // Mouse must be inside the bin left, right, top, bottom borders. All 4 must be true for the code inside to run.
    for (let i = 0; i < 20; i++) { // This loop runs 20 times, each time through it creates one particle.
      let angle = random(TWO_PI); // Random angle between 0 and 2π full circle. Particles shoot in all directions.
      let speed = random(2, 5); // Random speed between 2 and 5.
      
      particles.push({ // Add a new particle to the array
        x: mouseX, // Start at mouse X position
        y: mouseY, // Start at mouse Y position
        vx: cos(angle) * speed, // Horizontal velocity converts the angle to X direction, multiply by speed to control how fast.
        vy: sin(angle) * speed, // Verticle velocity converts the angel to Y direction
        size: random(4, 8), // Random diameter between 4 and 8 pixels
        r: random(150, 255), // Random red value
        g: random(150, 255), // Random green value
        b: random(150, 255), //Random blue value
        alpha: 255 // Fully visible, will fade in draw.
      });
    }
    
    if (score < maxScore) { // Only if score is less than 10.
      score++; // Increase score by 1. Same as score = score + 1 which prevents the score from going above 10.
    } // Closes the 'if' statement checking if click is inside bin.
  } // Closes the entire 'mousePressed()' function
}