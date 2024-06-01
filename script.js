const loginForm = document.getElementById('login-form');

function redirectToIndex1() {
    window.location.href = 'index1.html';
}

function redirectToIndex2() {
  window.location.href = 'index2.html';
}

loginForm.addEventListener('submit', (event) => {
    event.preventDefault(); // Prevent default form submission

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    // Check if email or password is empty
    if (!email || !password) {
        alert('Please enter both email and password.');
    } else {
        // Simulate login by logging the information to the console (replace with your actual logic)
        console.log(`Email: ${email}, Password: ${password}`);

        // If login is successful, redirect to index2.html
        redirectToIndex2();
    }
});



