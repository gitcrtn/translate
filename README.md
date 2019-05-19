# translate
Simple translation commands
- en-ja (英和辞書)
- ja-en (和英辞書)

## Support APIs
- Google Translate
- Weblio (default)

## Usage
    en-ja <text> [--api google|weblio]
    ja-en <text> [--api google|weblio]

    en-ja translate
    ja-en 翻訳する

    en-ja "Simple translation commands" --api google
    ja-en "シンプルな翻訳コマンド" --api google

## Requirement
Python 3.7

## Installation
    git clone https://github.com/gitcrtn/translate.git
    cd translate
    
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    deactivate
    
    chmod +x bin/*

    echo "export PATH=$PWD/bin:$PATH" >> ~/.bashrc

## Settings
Put service account file of Google Cloud Platform (GCP) into cred directory.  
This file is used by Google Translate API.  
  
Rename as below (**** is any numbers):  
cred/google-translate-****.json  
  
And also, enable Google Translate API from your GCP console.

## License
[MIT](https://github.com/gitcrtn/translate/blob/master/LICENSE)

## Author
[Carotene](https://github.com/gitcrtn)
