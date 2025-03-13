function validateForm() {
    let form = document.forms[0]; // Get the first form on the page

    let course = form["course"].value.trim();
    let fromYear = form["from-year"].value;
    let toYear = form["to-year"].value;
    let department = form["department"].value.trim();
    let college = form["college"].value.trim();
    let university = form["university"].value.trim();
    let cgpa = form["cgpa"].value.trim();
    let declaration = form["declaration"].checked;

    // Check if required fields are filled
    if (course === "" || fromYear === "Select start year" || toYear === "Select end year" || department === "" || college === "" || university === "" || cgpa === "") {
        alert("All fields are required!");
        return false;
    }

    // Ensure 'From Year' is less than 'To Year'
    if (parseInt(fromYear) >= parseInt(toYear)) {
        alert("From Year must be earlier than To Year!");
        return false;
    }

    // Validate CGPA (should be between 0 and 10)
    let cgpaPattern = /^(10|[0-9](\.[0-9]{1,2})?)$/;
    if (!cgpaPattern.test(cgpa)) {
        alert("Please enter a valid CGPA between 0 and 10!");
        return false;
    }

    // Check if declaration checkbox is checked
    if (!declaration) {
        alert("You must agree to the declaration before submitting!");
        return false;
    }

    alert("Form submitted successfully!");
    return true;
}
