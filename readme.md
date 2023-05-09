<img src="https://github.com/appvoid/vosper/raw/main/logo.png" width="100%" height="auto">

# vosper
🕑 Real-Time Whisper Voice Recognition with vosk model feedback 🎙

### 🌏 News
> New logo: Hopefully everyone likes it.<br>
> vosper 2.0: The codebase was rewritten and more customization was added!<br>
> Pip is coming: A proper, easier installation and update alternative will be launched soon.
> vosper 2.1: The codebase is being refactorized for highly-optimized implementation.

### 📑 Features
- Minimal approach
- Easy installation
- Easy modification
- Fast text feedback thanks to vosk
- Detects human voices (It records audio for Whisper only when needed)
### ⭐ Installation
```
git clone https://github.com/appvoid/vosper.git && 
cd vosper && 
chmod +x install.sh &&
./install.sh
```
### ▶ Usage
```python3 main.py # It's pretty minimal...```
### ☕ **Donations and Support** 
[**paypal donation** ](https://www.paypal.com/donate/?hosted_button_id=CDZH8GJET9SNU) or [ **patreon support** ](https://www.patreon.com/bePatron?u=52880328)
### 🔭 Full Roadmap
- [x] Vosk Real-Time inference and Whisper VAD support
- [x] Class-Based implementation
- [x] Easier way to choose a whisper model
- [x] Improved code quality, comments, readability, etc...
- [x] Verbosity switch
- [x] Customizable settings
- [ ] Custom VAD model support
- [ ] Python's pip installation method
- [ ] Keyboard support
- [ ] Documentation

### 🔴 Disclaimer
Real-Time usage scenarios (like a voice assistant for example) requires a GPU with at least 2-4~ gb of vram. The more the vram, the largest the model you can load, the better the transcription and the slower it gets.
