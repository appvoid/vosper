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
- [x] Class-Based implementation
- [x] Easier way to choose a whisper model
- [x] Improved code quality, comments, readability, etc...
- [x] Verbosity switch
- [ ] Custom VAD

### Error Rate Reference
*- Lower is better -*
| model | librispeech | tedlium |
| ----- | ----------- | ------- |
|small-en-us-0-15|9.85|10.38|
|en-us-0-22-lgraph|7.82|8.20|
|en-us-0-22|5.69|6.05|
|whisper-tiny-en|5.6|6.0|
|whisper-tiny|7.6|7.0|
|whisper-base-en|4.2|4.9|
|whisper-base|5.0|5.5|
|whisper-small-en|3.1|4.0|
|whisper-small|3.4|4.3|
|whisper-medium-en|3.1|4.1|
|whisper-medium|2.9|3.8|
|whisper-large|2.7|4.0|

### Disclaimer
Real-Time usage scenarios (like a voice assistant for example) requires a GPU with at least 2-4~ gb of vram. The more the vram, the largest the model you can load, the better the transcription and the slower it gets.
