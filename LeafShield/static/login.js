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
                  document.getElementById('password').value = '';
              }
          });
      }, 100);  // Adjust delay if necessary
  }
});

document.getElementById('loginForm').addEventListener('submit', function(event) {
  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;

  // Basic validation to prevent submission if fields are empty
  if (!username || !password) {
      event.preventDefault();
      document.getElementById('message').textContent = 'Please fill out all fields!';
  } 
});


