const chatLog = document.getElementById('chat-log');
const form = document.getElementById('chat-form');
const textarea = document.getElementById('message');

function addMessage(role, text) {
  const wrapper = document.createElement('div');
  wrapper.className = `message ${role}`;

  const label = document.createElement('span');
  label.className = 'label';
  label.textContent = role === 'user' ? 'You' : 'Ai-coder';

  const bubble = document.createElement('p');
  bubble.textContent = text;

  wrapper.appendChild(label);
  wrapper.appendChild(bubble);
  chatLog.appendChild(wrapper);
  chatLog.scrollTop = chatLog.scrollHeight;
}

form.addEventListener('submit', async (event) => {
  event.preventDefault();

  const message = textarea.value.trim();
  if (!message) {
    return;
  }

  addMessage('user', message);
  textarea.value = '';
  textarea.focus();

  try {
    const response = await fetch('/api/chat', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ message })
    });

    const data = await response.json();
    if (!response.ok) {
      throw new Error(data.reply || 'Something went wrong');
    }

    addMessage('bot', data.reply);
  } catch (error) {
    addMessage('bot', error.message);
  }
});
