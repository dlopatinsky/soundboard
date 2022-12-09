# Soundboard

---

## Feature list

- Can play multiple .wav files at the same time
- Can instantly kill all active sounds
- Synthesizes audio files from text locally on your computer
- Configurable TTS profiles, for different models, languages etc
- Auto-generated example configs
- Graphical user interface
- No automatic sink setup yet, you'll have to redirect the audio yourself

## Requirements:

- torch
- omegaconf
- pyopenal
- kivy
- pytest (for tests only)

---

## Set up

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

The application is run from src/main.py.

---

## Custom TTS profiles

To create a custom TTS profiles add a similar structure to config/tts.ini:

```ini
# Name of the profile to select in the GUI
[English]
# Description of the model from PyTorch hub
repository = snakers4/silero-models
model = silero_tts
language = en
model_id = v3_en
speaker = en_1
# Applies locally, set this to a lower value
# for better performance and worse audio quality
sample_rate = 24000
```

The models are cached locally on your computer.
It takes time to download them from the hub when you first use a model,
but the later uses are much faster.

---

## Implementation progress:
- [x] basic soundboard functionality
- [x] GUI
- [ ] automatic sink setup
- [ ] keybindings
- [ ] configuration through GUI

---

## Authors:
- Dmitry Lopatinsky
