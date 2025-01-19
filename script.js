import { GoogleGenerativeAI, HarmCategory, HarmBlockThreshold } from "@google/generative-ai";
  
  const apiKey = process.env.GEMINI_API_KEY;
  const genAI = new GoogleGenerativeAI(apiKey);
  
  const model = genAI.getGenerativeModel({
    model: "gemini-2.0-flash-exp",
    systemInstruction: "build backend of the given problem statement \"Job seekers often struggle to create professional, tailored, and visually appealing resumes due to time constraints, lack of expertise, and difficulty customizing for specific roles. The solution is an AI-powered resume builder using the Gemini API to generate personalized content and streamline the creation process with support and easy download options.\"",
  });
  
  const generationConfig = {
    temperature: 1,
    topP: 0.95,
    topK: 40,
    maxOutputTokens: 8192,
    responseMimeType: "text/plain",
  };
  
  async function run() {
    const chatSession = model.startChat({
      generationConfig,
      history: [
      ],
    });
  
    const result = await chatSession.sendMessage("INSERT_INPUT_HERE");
    console.log(result.response.text());
  }
  
  run();

  document.getElementById('resume-form').addEventListener('submit', async function (e) {
    e.preventDefault();

    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const skills = document.getElementById('skills').value;
    const experience = document.getElementById('experience').value;

    const resumePreview = document.getElementById('resume-preview');
    const previewContent = document.getElementById('preview-content');

    // Placeholder for API call to Gemini API
    const resumeData = {
      name,
      email,
      skills,
      experience
    };

    // Mockup for response (replace this with API call result)
    const response = {
      resume: `Name: ${name}\nEmail: ${email}\nSkills: ${skills}\nExperience: ${experience}`
    };

    // Display the generated resume
    previewContent.textContent = response.resume;
    resumePreview.style.display = 'block';
  });
    // Function to send data to the backend using Fetch API
    function submitData() {
        const name = document.getElementById('name').value;
        
        // Send the name to the Flask backend using fetch
        fetch('http://127.0.0.1:5000/api/submit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name: name })
        })
        .then(response => response.json())
        .then(data => {
            // Handle the response from the backend
            document.getElementById('response').innerText = data.message;
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }