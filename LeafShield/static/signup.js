document.addEventListener('DOMContentLoaded', function() {
    // Find the hidden Django messages
    const messagesDiv = document.getElementById('django-messages');
    if (messagesDiv) {
        const messages = messagesDiv.querySelectorAll('.message');
  
        // Delay the alert slightly to ensure the page is fully rendered
        setTimeout(() => {
            messages.forEach((message) => {
                alert(message.textContent);  // Display alert for each message
  
                // Clear input fields if it's an error message
                if (message.classList.contains('error')) {
                    document.getElementById('username').value = '';
                    document.getElementById('first_name').value = '';
                    document.getElementById('last_name').value = '';
                    document.getElementById('email').value = '';
                    document.getElementById('password').value = '';
                    document.getElementById('confirmPassword').value = '';
                }
            });
        }, 100);  // Adjust delay if necessary
    }
  });
  
  // Handle form submission
  document.getElementById('registrationForm').addEventListener('submit', function(event) {
      const username = document.getElementById('username').value;
      const first_name = document.getElementById('first_name').value;
      const last_name = document.getElementById('last_name').value;
      const email = document.getElementById('email').value;
      const password = document.getElementById('password').value;
      const confirmPassword = document.getElementById('confirmPassword').value;
  
      // Basic validation: Check if all fields are filled
      if (!username || !first_name || !last_name || !email || !password || !confirmPassword) {
          event.preventDefault();
          alert('Please fill out all fields!');
          return;
      }
  
      // Check if password and confirm password match
      if (password !== confirmPassword) {
          event.preventDefault();
          alert('Password and Confirm Password do not match!');
          return;
      }
  
      // If all validations pass, you can proceed with form submission
  });
  