<img src="https://github.com/appvoid/vosper/raw/main/logo.png" width="100%" height="auto">

# vosper
🕑 Real-Time Whisper Voice Recognition with vosk model feedback 🎙
### Features
- Minimal approach
- Easy installation
- Fast feedback thanks to vosk
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
Buy me a coffee! Creating this kind of things is tedious sometimes and enjoyable also. When you support a developer, you really make it to work a lot happier 😄
### [ 👉 **Donate using PayPal** ](https://www.paypal.com/donate/?hosted_button_id=CDZH8GJET9SNU)
### [ 👉 **Become a Patreon!** ](https://www.patreon.com/bePatron?u=52880328)
### Roadmap
- [x] Vosk Real-Time inference and Whisper VAD support
- [ ] Class-Based implementation
- [ ] Easier way to choose a whisper model

### Disclaimer
Real-Time usage scenarios (like a voice assistant for example) requires a GPU with at least 2-4~ gb of vram. The more the vram, the largest the model you can load, the better the transcription and the slower it gets.
