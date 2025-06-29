const fetchJobs = async () => {
    try {
        const response = await fetch('http://localhost:5501/api/v1/job/getjobs');
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const jobs = await response.json();

        // Shuffle the job array to get a random selection of jobs
        const shuffledJobs = jobs.sort(() => Math.random() - 0.5);

        // Limit to 3 jobs
        const selectedJobs = shuffledJobs.slice(0, 3);

        const jobCardsContainer = document.getElementById('job-cards');
        jobCardsContainer.innerHTML = ''; // Clear previous job cards

        // Loop through the selected jobs and create job cards
        selectedJobs.forEach((job) => {
            const jobCard = document.createElement('div');
            jobCard.classList.add('job-card');
            jobCard.innerHTML = `
                <h3>${job.title}</h3>
                <p><strong>Company:</strong> ${job.company}</p>
                <p><strong>Location:</strong> ${job.location}</p>
                <p>${job.description}</p>
            `;
            jobCard.onclick = () => {
                window.location.href = `job-details.html?id=${job.id}`; // Redirect to job details page
            };
            jobCardsContainer.appendChild(jobCard);
        });
    } catch (error) {
        console.error('Error fetching jobs:', error);
    }
};

// Call fetchJobs to load the job data when the page loads
window.onload = fetchJobs;





// Get the volume button
const volumeButton = document.querySelector('.volume-btn');

// Flag to track whether the speech is currently being read
let isReading = false;

// Function to read all text on the page
function readText() {
  // If text is already being read, stop it
  if (isReading) {
    window.speechSynthesis.cancel(); // Stop the speech
    volumeButton.textContent = "🔊 Read All Text"; // Change button text to indicate it can start reading again
    isReading = false;
  } else {
    // Grab all the text content from the page
    const pageText = document.body.innerText;

    // Initialize a SpeechSynthesisUtterance object with the page's text
    const speech = new SpeechSynthesisUtterance(pageText);

    // Optionally, set the language and voice of the speech
    speech.lang = 'en-US';  // You can change this to a different language if needed
    speech.volume = 1; // Volume range is from 0 (silent) to 1 (loudest)
    speech.rate = 1;   // Speech rate (1 is normal speed)
    speech.pitch = 1;  // Pitch level (1 is the default pitch)

    // Start the speech
    window.speechSynthesis.speak(speech);

    // Update the flag and button text
    isReading = true;
    volumeButton.textContent = "⏸️ Stop Reading"; // Change button text to indicate it can be stopped
  }
}

// Add event listener to the volume button to trigger reading or stopping
volumeButton.addEventListener('click', readText);












