function validateForm() {
    let form = document.forms[0]; // Get the first form on the page

    let fullname = form["fullname"].value.trim();
    let studentid = form["studentid"].value.trim();
    let email = form["email"].value.trim();
    let phone = form["phone"].value.trim();
    let address = form["address"].value.trim();
    let gender = form["gender"].value;
    let dob = form["dob"].value;
    let accommodation = document.querySelector('input[name="accommodation"]:checked');

    // Simple required fields check
    if (fullname === "" || studentid === "" || email === "" || phone === "" || address === "" || gender === "Select gender" || dob === "" || !accommodation) {
        alert("All fields are required!");
        return false;
    }

    // Email validation
    let emailPattern = /^\S+@\S+\.\S+$/;
    if (!emailPattern.test(email)) {
        alert("Please enter a valid email address!");
        return false;
    }

    // Phone number validation (must be 10 digits)
    let phonePattern = /^\d{10}$/;
    if (!phonePattern.test(phone)) {
        alert("Phone number must be exactly 10 digits!");
        return false;
    }

    // Date of Birth validation (should be a past date)
    let today = new Date();
    let dobDate = new Date(dob);
    if (dobDate >= today) {
        alert("Date of Birth must be a valid past date!");
        return false;
    }

    alert("Form submitted successfully!");
    return true;
}
