function lengthButtonClick(button) {
    // remove the "selected" class from all buttons
    const buttons = document.querySelectorAll(".length-button");
    buttons.forEach(btn => btn.classList.remove("selected"));
  
    button.classList.add("selected");
    
    const lengthInput = document.querySelector("#length");
    lengthInput.value = button.value;
  
    console.log("Button clicked");
  }

  
const form = document.querySelector("form");
const summary = document.querySelector(".summary");
const error = document.querySelector(".error");
form.addEventListener("submit", function() {

  if (summary && summary.parentElement) {
    summary.parentElement.removeChild(summary);
    console.log("summary removed");
  }

  if (error && error.parentElement) {
    error.parentElement.removeChild(error);
    console.log("error removed");
  }
  
  const selectedButton = document.querySelector(".length-button.selected");
  if (selectedButton) {
    selectedButton.classList.add("selected");
    console.log("we here!")
  }

  // const selectedButton = document.querySelector(".length-button.selected");
  if (selectedButton) {
    console.log("we here! part 2!")
    const selectedValue = selectedButton.value;
    const lengthInput = document.querySelector("#length");
    lengthInput.value = selectedValue;
  }

  const loadingComponent = document.getElementById('loading-component');
  loadingComponent.style.display = 'block';
  console.log("Ending the JS function");
});

  