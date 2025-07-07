#!/bin/bash
echo 'DICare Setup Script'
apt update && apt install -y python3-pip git
pip3 install -r requirements.txt
echo 'Установка завершена. Запустите бота с python3 bot.py'
