function goToWebsite () {
  var dropdown = document.getElementById ("websiteDropdown");
  var selectedOption = dropdown.options[dropdown.selectedIndex].value; // Dropdown refers to the dropdown element on the webpage.
  // dropdown.selectedIndex gets the index of the currently selected option in the dropdown.
  // dropdown.options gets an array-like object that represents the available options in the dropdown. That basically means that it's an array of all the options in the dropdown.
  // By accessing .value at the end of the line, we are able to get the value of the selected option from the dropdown, and that is what the variable will be equal to.
  if (selectedOption) {
    window.location = selectedOption;
  }
}