# ML-GenAI_assignment
This repository contains my assignment submission, including code, documentation, and required files as per the given guidelines.


# AI Story, Storyboard & Video Scene Generator

An end-to-end creative pipeline that transforms a simple text idea into a professionally structured short story, a cinematic 5-scene visual storyboard, and a short, animated video scene.

## 📖 Table of Contents

- [Project Description](#-project-description)
- [Features](#-features)
- [How It Works](#-how-it-works)
- [Tech Stack](#-tech-stack)
- [Prerequisites](#-prerequisites)
- [Setup and Installation](#-setup-and-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Challenges Faced and Solutions](#-challenges-faced-and-solutions)
- [Future Work](#-future-work)
- [License](#-license)

---

## 📜 Project Description

This application leverages a sophisticated multi-modal AI architecture to automate the creative process from concept to a final visual narrative. A user provides a high-level topic (e.g., "a detective discovering a clue in a rainy city"), and the system generates a complete creative package: a well-plotted story following a three-act structure, a corresponding 5-panel storyboard with high-quality images and emotive captions, and finally, a short video clip that animates the opening scene of the story.

The project is designed to be a powerful tool for writers, artists, and filmmakers to quickly visualize their ideas, prototype narrative concepts, and see their stories come to life in motion.

**_Current Status:_**
> Due to the high computational cost and lack of free-tier availability for state-of-the-art video models, the final video generation feature is **temporarily disabled** in the current version of the application. The full pipeline is designed and ready for integration as soon as a suitable service is available.

## ✨ Features

-   **Structured Story Generation:** Utilizes Gemini 1.5 Flash to write stories with a classic three-act plot structure (Setup, Confrontation, Resolution).
-   **Advanced Prompt Engineering:** Intelligently analyzes the generated story to extract 5 key cinematic moments, creating bespoke, high-fidelity prompts for each scene.
-   **Narrative Captions:** Generates short, emotive captions for each storyboard image to guide the viewer and enhance the storytelling.
-   **Hybrid AI Model Integration:** Seamlessly combines the strengths of Google's Gemini for text and logic with Hugging Face's Stable Diffusion XL for state-of-the-art image generation.
-   **Planned Video Synthesis:** The architecture is designed to feed the generated storyboard images into an Image-to-Video model to create a final, animated scene.
-   **Interactive Web Interface:** Built with Streamlit for a clean, responsive, and user-friendly experience.

## 🚀 How It Works

The application follows a sequential, multi-stage pipeline to process the user's request:

1.  **User Input:** The user provides a story topic via the Streamlit web interface.
2.  **Story Generation (Gemini):** The topic is sent to a `generate_story` function. A detailed "meta-prompt" instructs Gemini 1.5 Flash to act as a screenwriter and produce a short story following the three-act structure.
3.  **Scene Extraction (Gemini):** The generated story is then passed to an `extract_key_storyboard_prompts` function. A second, highly-specific meta-prompt instructs Gemini to act as a creative director, analyzing the story and creating a list of 5 Python dictionaries. Each dictionary contains:
    -   A `prompt` for the image generator, detailing camera angles, lighting, and style.
    -   A `caption` to be displayed under the image in the UI.
4.  **Image Generation (Hugging Face):** The Streamlit UI iterates through the 5 scenes. For each scene, it calls the `generate_storyboard_image` function with the corresponding `prompt`. This function sends an API request to the free Hugging Face Inference API, which runs the Stable Diffusion XL model.
5.  **Display Storyboard:** As each image is generated, it is saved locally and displayed in the UI within its own column, along with its narrative caption, creating the final 5-panel storyboard.
6.  **Video Generation (Temporarily Disabled):** The final, intended step is to take the first image from the generated storyboard and pass it to an Image-to-Video model (like Stable Video Diffusion). This would produce a short, 3-5 second animated clip, bringing the opening scene to life.

> **Note:** As described above, the video generation feature (Step 6) is temporarily disabled in the user interface due to the non-availability of a suitable free service at this time. The codebase is designed for its future integration.

## 🛠️ Tech Stack

### Frontend
-   **[Streamlit](https://streamlit.io/):** For building the interactive web application interface.

### Backend & AI Services
-   **[Google AI Studio API](https://aistudio.google.com/):** Provides access to the `Gemini 1.5 Flash` model for all text generation and analysis tasks.
-   **[Hugging Face Inference API](https://huggingface.co/inference-api):** Provides free, public access to the `Stable Diffusion XL` model for image generation.
-   **Planned Video Service:** The architecture is ready to integrate an Image-to-Video service like **Stable Video Diffusion** via an API provider (e.g., Replicate) or a local `diffusers` implementation.

### Core Python Libraries
-   `google-generativeai`: The official Python SDK for the Google AI Studio API.
-   `requests`: For making HTTP requests to the Hugging Face API.
-   `python-dotenv`: To manage environment variables and API keys securely.
-   `Pillow`: For processing and saving image data.
-   `streamlit`: The core web framework library.

## ✅ Prerequisites

Before you begin, ensure you have the following installed and configured:

1.  **Python 3.8 or higher:** [Download Python](https://www.python.org/downloads/)
2.  **Git:** For cloning the repository. [Download Git](https://git-scm.com/downloads)
3.  **API Keys:**
    -   **Google AI Studio API Key:** Get one for free from [Google AI Studio](https://aistudio.google.com/).
    -   **Hugging Face User Access Token:** Get one for free from your [Hugging Face account settings](https://huggingface.co/settings/tokens).

## ⚙️ Setup and Installation

Follow these steps to get the project running on your local machine.

**1. Clone the Repository:**
```bash
git clone https://github.com/your-username/ai-story-generator.git
cd ai-story-generator
```
*(Note: Replace `your-username` with your actual GitHub username)*

**2. Create and Activate a Virtual Environment:**
It's highly recommended to use a virtual environment to manage project dependencies.

-   **On macOS/Linux:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
-   **On Windows:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

**3. Create a `requirements.txt` file:**
Create a file named `requirements.txt` in the root of your project and paste the following content into it:
```
streamlit
google-generativeai
requests
python-dotenv
Pillow
```

**4. Install Dependencies:**
Install all the required Python libraries from the `requirements.txt` file.
```bash
pip install -r requirements.txt
```

**5. Set Up Environment Variables:**
Create a file named `.env` in the root of your project directory. This file will securely store your API keys. **This file is ignored by Git and should never be committed.**

Paste the following into your `.env` file and replace the placeholders with your actual keys:
```
# .env file

GOOGLE_API_KEY="your_new_key_from_ai_studio_here"
HUGGINGFACE_API_TOKEN="hf_YourSecretTokenFromHuggingFace"
```

**6. Run the Application:**
You are now ready to launch the Streamlit app!
```bash
streamlit run main_app.py
```
Your web browser should automatically open to the application's interface.

## 🚀 Usage

1.  Once the application is running, you will see the main interface.
2.  The text input box will be pre-filled with an example topic. You can use this or enter your own.
3.  Click the **"Generate Enhanced Story & Storyboard"** button.
4.  Watch the spinners as the AI completes each step:
    -   First, the story will be generated and displayed.
    -   Then, the 5 storyboard panels will be generated one by one.
5.  Once complete, you can view the full story and the 5-scene visual storyboard with captions. The video section will display a message indicating its current status.

## 🗂️ Project Structure

```
ai-story-generator/
│
├── .env                  # Stores your secret API keys (must be created manually)
├── generated_media/      # Directory where generated images are saved
├── main_app.py           # The main Streamlit application file (UI)
├── README.md             # This documentation file
├── requirements.txt      # Lists the Python dependencies for the project
│
└── utils/
    └── ai_services.py    # The "brains" of the app; contains all AI model logic
```

## 🧠 Challenges Faced and Solutions

Developing this multi-modal pipeline presented several interesting technical and strategic challenges:

1.  **Challenge: Finding a Free, High-Quality Video Generation Service.**
    -   **Problem:** State-of-the-art video models like Google's Veo are in private preview, and most public video generation APIs require a paid subscription or have very limited free credits that were exhausted quickly.
    -   **Solution:** The project was strategically pivoted to perfect the Story and Image generation stages first. The UI was updated to clearly communicate that video generation is a planned future step, managing user expectations while still delivering a complete and valuable creative tool.

2.  **Challenge: Ensuring Reliable and Structured AI Output.**
    -   **Problem:** Large Language Models (LLMs) can be creatively unpredictable. Early versions sometimes returned prompts or stories in the wrong format, breaking the application's parsing logic.
    -   **Solution:** Implemented **Advanced Prompt Engineering**. Instead of simple requests, the meta-prompts were enhanced to give the AI a "persona" (like a screenwriter or creative director) and provided strict, explicit instructions on the desired output format (e.g., "CRITICAL: Respond ONLY with a Python list of 5 dictionaries"). This drastically increased the reliability and quality of the AI's responses.

3.  **Challenge: Handling Asynchronous AI Model Loading Times.**
    -   **Problem:** The free Hugging Face Inference API uses a "serverless" model. If a model hasn't been used recently, it can take 20-30 seconds to load, causing the initial API request to time out or return a `503 Service Unavailable` error.
    -   **Solution:** A robust retry mechanism was built into the `ai_services.py` module. The code now catches the `503` error, reads the `estimated_time` from the API response, waits for that duration, and then automatically retries the request. This makes the user experience seamless, with the "cold start" delay simply appearing as a slightly longer spinner in the UI.

4.  **Challenge: Choosing the Right API and Authentication Method.**
    -   **Problem:** The Google AI ecosystem offers multiple entry points (Vertex AI, Google AI Studio) with different authentication methods (`gcloud auth` vs. simple API keys). The initial path using Vertex AI was powerful but added significant setup complexity for new users.
    -   **Solution:** The project was migrated to use the **Google AI Studio API (`google-generativeai` library)**. This simplified the setup process to just requiring a single API key in the `.env` file, dramatically lowering the barrier to entry for other developers wanting to run the project.

## 🔮 Future Work

The current application provides a robust foundation. The next logical step is to re-enable video generation.

-   **Re-integrate Video Generation:** Implement the final step of the pipeline to turn the generated storyboard images into short, animated video clips. This could be achieved by:
    -   **API-based Service:** Using a service with a free tier like [Replicate](https://replicate.com/) to access an Image-to-Video model (e.g., Stable Video Diffusion).
    -   **Local Model:** Integrating the `diffusers` library to run Stable Video Diffusion locally, for users with powerful NVIDIA GPUs who prefer privacy and unlimited usage.

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

*(Note: You should create a `LICENSE` file and add the MIT license text if you intend to make this project public.)*
