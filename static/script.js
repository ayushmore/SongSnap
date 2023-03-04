function lengthButtonClick(button) {
    // remove the "selected" class from all buttons
    const buttons = document.querySelectorAll(".length-button");
    buttons.forEach(btn => btn.classList.remove("selected"));
  
    // add the "selected" class to the clicked button
    button.classList.add("selected");
    
    // set the value of the hidden input
    const lengthInput = document.querySelector("#length");
    lengthInput.value = button.value;
  
    // add a console.log statement to see if this function is being called
    console.log("Button clicked");
  }
  
const form = document.querySelector("form");
form.addEventListener("submit", function() {
  console.log("Submit and in the JS function");
  const selectedButton = document.querySelector(".length-button.selected");
  if (selectedButton) {
    console.log("Checking to see if there even is a selected button");
    console.log(selectedButton);
    selectedButton.classList.add("selected");
  }
  console.log("Ending the JS function");
});

  