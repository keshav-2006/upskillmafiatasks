let generatedOTP = '';
let timerInterval;

document.getElementById('generate-otp-btn').addEventListener('click', () => {
  generatedOTP = generateOTP(6);
  document.getElementById('generated-otp').textContent = `Your OTP: ${generatedOTP}`;
  document.getElementById('verification-result').textContent = '';
  document.getElementById('generate-otp-btn').disabled = true;
  startTimer(30);
});

document.getElementById('verify-otp-btn').addEventListener('click', () => {
  const userInput = document.getElementById('otp-input').value;
  const resultElement = document.getElementById('verification-result');
  if (userInput == generatedOTP) {
    resultElement.textContent = 'OTP Verified Successfully!';
    resultElement.style.color = 'green';
    stopTimer();
  } else {
    resultElement.textContent = 'Incorrect OTP or OTP Expired! Please Try Again.';
    resultElement.style.color = 'red';
  }
});

function generateOTP(length) {
  let otp = '';
  for (let i = 0; i < length; i++) {
    otp += Math.floor(Math.random() * 10);
  }
  return otp;
}

function startTimer(duration) {
  const timerElement = document.getElementById('timer');
  let timeRemaining = duration;
  timerElement.textContent = `Time remaining: ${timeRemaining} seconds`;
  timerInterval = setInterval(() => {
    timeRemaining -= 1;
    timerElement.textContent = `Time remaining: ${timeRemaining} seconds`;
    if (timeRemaining <= 0) {
      clearInterval(timerInterval); 
      generatedOTP = ''; 
      timerElement.textContent = 'OTP expired. Please generate a new one.';
      document.getElementById('generate-otp-btn').disabled = false;
    }
  }, 1000);
}
function stopTimer() {
  clearInterval(timerInterval); 
  document.getElementById('timer').textContent = ''; 
  document.getElementById('generate-otp-btn').disabled = false; 
  generatedOTP = ''; 
}