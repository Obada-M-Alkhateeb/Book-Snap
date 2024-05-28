// Account creation form handling
const signupForm = document.getElementById('signup-form');
const errorMessageElement = document.getElementById('error-message');

signupForm.addEventListener('submit', (event) => {
    event.preventDefault(); // Prevent default form submission

    const firstName = document.getElementById('first-name').value;
    const lastName = document.getElementById('last-name').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirm-password').value;

    // Check if any field is empty
    if (!firstName || !lastName || !email || !password || !confirmPassword) {
        errorMessageElement.textContent = 'All fields are required.';
        return;
    }

    // Check if password and confirm password match
    if (password !== confirmPassword) {
        errorMessageElement.textContent = 'Passwords do not match. Please try again.';
        return false; // Prevent form submission
    }

    // Clear any previous error messages
    errorMessageElement.textContent = '';

    // Simulate account creation by logging the information to the console (replace with your actual logic)
    console.log(`First Name: ${firstName}, Last Name: ${lastName}, Email: ${email}, Password: ${password}`);

    // If account creation is successful, redirect to index2.html
    window.location.href = 'index2.html';
});
