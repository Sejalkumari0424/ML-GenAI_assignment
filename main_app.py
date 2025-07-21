# main_app.py

import streamlit as st
from utils.ai_services import (
    generate_story,
    extract_key_storyboard_prompts,
    generate_storyboard_image,
)
import os

# --- Page Setup ---
st.set_page_config(layout="wide", page_title="AI Story Generator", page_icon="🎬")

# --- UI Elements ---
st.title("🎬 AI Story & Storyboard Generator")
st.markdown("From a simple idea to a structured story and a cinematic 5-scene storyboard with narrative captions.")
st.markdown("---")

# --- Folder Setup ---
if not os.path.exists("generated_media"):
    os.makedirs("generated_media")

# --- User Input ---
user_topic = st.text_input(
    label="Enter a topic, character, or scenario for your story:",
    value="A lonely astronaut on Mars discovers a mysterious, pulsating alien artifact."
)

# --- Main Application Logic ---
if st.button("Generate Enhanced Story & Storyboard", type="primary", use_container_width=True):

    if 'story_text' not in st.session_state or st.session_state.get('topic') != user_topic:
        st.session_state.clear()
        st.session_state.topic = user_topic

        with st.spinner("Step 1: Gemini is writing a structured story..."):
            st.session_state.story_text = generate_story(user_topic)

        with st.spinner("Step 2: Gemini is crafting 5 scenes (prompts & captions)..."):
            # This now returns a list of dictionaries
            st.session_state.scene_data = extract_key_storyboard_prompts(st.session_state.story_text)
            st.session_state.image_paths = [None] * len(st.session_state.scene_data)

# --- Display Results ---
if 'story_text' in st.session_state and st.session_state.story_text:
    st.header("📜 Your Generated Story")
    st.write(st.session_state.story_text)
    st.divider()

    st.header("🎨 Your 5-Scene AI-Generated Storyboard")
    if 'scene_data' in st.session_state:
        scenes = st.session_state.scene_data
        num_scenes = len(scenes)
        
        cols = st.columns(num_scenes)

        for i, scene in enumerate(scenes):
            with cols[i]:
                # Extract the prompt and caption for the current scene
                prompt = scene.get("prompt", "")
                caption = scene.get("caption", "...")

                if st.session_state.image_paths[i]:
                    st.image(st.session_state.image_paths[i])
                    st.caption(f"_{caption}_") # Display the caption below the image
                elif prompt and "failed" not in prompt.lower() and "error" not in prompt.lower():
                    with st.spinner(f"Generating Scene {i+1}..."):
                        safe_topic = "".join(x for x in st.session_state.topic[:15] if x.isalnum() or x in " _-").rstrip()
                        image_filename = os.path.join("generated_media", f"scene_{i+1}_{safe_topic}.png")

                        success, result = generate_storyboard_image(prompt, image_filename)

                        if success:
                            st.session_state.image_paths[i] = result
                            st.image(result)
                            st.caption(f"_{caption}_") # Display the caption below the new image
                        else:
                            st.error(f"Image {i+1} failed.")
                            st.caption(f"Error: {result}", unsafe_allow_html=True)
                else:
                    st.warning(f"Skipping Scene {i+1} due to an invalid prompt.")
    
    st.divider()

    # --- Video Generation Placeholder Section ---
    st.header("🎥 Video Generation (Paused)")
    st.warning(
        """
        **The video generation model will be integrated here.**

        This feature is temporarily disabled as the free credits for the third-party video API service have been exhausted. 
        It will be re-enabled once a new API key is provided or a local model is configured.
        """,
        icon="⚠️"
    )

# Show this message only on the initial run
if 'story_text' not in st.session_state:
    st.info("Click the 'Generate Enhanced Story & Storyboard' button to begin.")