function refreshPage() {
    // Get the form fields and summary section
    var titleField = document.getElementById("title");
    var artistField = document.getElementById("artist");
    var lengthField = document.getElementById("length");
    var summaryElement = document.querySelector(".summary");
    
    // Clear the form fields
    titleField.value = "";
    artistField.value = "";
    lengthField.selectedIndex = ""; // Reset the select field
    
    // Hide the summary section if it exists
    if (summaryElement) {
      summaryElement.style.display = "none";
    }
  }