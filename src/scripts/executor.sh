#!/bin/bash
echo Executando script no Windows...
python -m venv venv
source venv/Scripts/activate

pip install -r requirements.txt

python "./src/backend/app.py"
