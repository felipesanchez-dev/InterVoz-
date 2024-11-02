
[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=FF3670&size=35&center=true&vCenter=true&width=1000&lines=Welcome+to+InterVoz;My+name+is+Felipe;I'm+Software+Engineering)](https://git.io/typing-svg)

# Voice Translator

## Description
This project uses artificial intelligence to transcribe an audio file in Spanish, translate it into several languages (English, Italian, French, and Japanese), and convert the translations into audio files. It is built using Gradio, Whisper, and the ElevenLabs API.

## Setup
Obtain your ElevenLabs API key and replace "Your ElevenLabs API key here" in the file with your generated key from <a href="https://elevenlabs.io/">ElevenLabs </a>. <br>
Ensure you have the <a href="https://elevenlabs.io/">Wisper </a> model and the necessary libraries installed.

## Functionality
The main workflow of the application is as follows:

* `Transcription:` The user records or uploads an audio file in Spanish.
* `Translation:` The transcribed text is translated into English, Italian, French, and Japanese.
* `Audio Conversion:` The translations are converted into audio files and returned to the user.

## Main Functions
* `translator(audio_file):` Main function that handles the transcription and translation of the audio.
* `text_to_speach(text, language):` Converts text to speech using the <a href="https://elevenlabs.io/">ElevenLabs </a> API.

## Virtualization Guide
If you want to virtualize your Python environment, follow the instructions for your operating system below.
### MacOS
1. **Open your terminal.**

2. **Navigate to your project directory:**
   ```bash
   $ cd /path/to/your/project
   ```
3. **Create a virtual environment:**
   ```bash
   $ python3 -m venv venv
   ```
4. **Activate the virtual environment:**
   ```bash
   $ source venv/bin/activate
   ```
5. **To deactivate the virtual environment, simply run:**
   ```bash
   $ deactivate
   ```
### Windows
1. **Open your terminal.**

2. **Navigate to your project directory:**
   ```bash
    $ cd C:\path\to\your\project
    ```
3. **Create a virtual environment:**
   ```bash
   $ python3 -m venv venv
   ```
4. **Activate the virtual environment:**
   ```bash
   $ venv\Scripts\activate
   ```
5. **To deactivate the virtual environment, simply run:**
   ```bash
   $ deactivate
   ```
### Linux
1. **Open your terminal.**

2. **Navigate to your project directory:**
   ```bash
    $ cd C:\path\to\your\project
    ```
3. **Create a virtual environment:**
   ```bash
   $ python3 -m venv venv
   ```
4. **Activate the virtual environment:**
   ```bash
   $ source venv/bin/activate
   ```
5. **To deactivate the virtual environment, simply run:**
   ```bash
   $ deactivate
   ```
## Requirements

Make sure you have the following Python packages installed:

- `gradio`
- `whisper`
- `translate`
- `elevenlabs`

#### Define ElevenLabs API Key

`ELEVENLABS_API_KEY = "Your ElevenLabs API key here"` <br>
<img src="https://github.com/felipesanchez-dev/InterVoz-/blob/main/img/API_KEY.png" alt="API key">

### You can install the dependencies using "pip":
   ```bash
   $ pip install gradio whisper translate elevenlab
   ```
## CONTRIBUTIONS
`Contributions are welcome. Feel free to open an issue or submit a pull request.`

## LICENSE
This project is licensed under the MIT License. See the LICENSE file for more details.

## CONTACT ME

[<img height="48px" width="48px" alt="Icone VS-Code" src="https://skillicons.dev/icons?i=instagram"/>](https://www.instagram.com/felipesanchez_dev/)
[<img height="48px" width="48px" alt="Icone VS-Code" src="https://skillicons.dev/icons?i=gmail"/>](mailto:jfelipe9.121@gmail.com)
[<img height="48px" width="48px" alt="Icone VS-Code" src="https://skillicons.dev/icons?i=linkedin"/>](https://www.linkedin.com/in/felipereyessa/)
