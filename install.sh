#!/bin/bash
echo 'Setting up Python libraries...'
pip3 install -r requirements.txt
echo 'Installing ffmpeg for Whisper, type your password:'
sudo apt update && sudo apt install ffmpeg