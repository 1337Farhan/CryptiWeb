[![Django CI](https://github.com/1337Farhan/CryptiWeb/actions/workflows/django.yml/badge.svg)](https://github.com/1337Farhan/CryptiWeb/actions/workflows/django.yml)

# CryptiWeb
The webapp and enhanced version of the [Crypti](https://github.com/1337Farhan/Crypti) project.
<br/><br/>

## 1. Introduction 👋
Developed by a team consisting of Me, [@Anas-Elhounsri](https://github.com/Anas-Elhounsri/), and [@mosman4](https://github.com/mosman4/), CryptiWeb is an online version of my previous project [Crypti](https://github.com/1337Farhan/Crypti).
<br/><br/>

## 2. Setup
*Note: you need to have our AWS setup ready before doing this, refer to [Crypti-LSTM](https://github.com/Anas-Elhounsri/Crypti-LSTM)*

There are four steps to host CryptiWeb on your local machine.
- Create a conda environment with requirements.txt *(ipython is recommended)*
  
    `conda env create -f environment.yml python=3.11 ipython`

- Create a secret key from [djecrety](https://djecrety.ir/) and replace the secret key in `settings.py`

- Setup environment variables in your terminal
      
    `export AWS_S3_ACCESS_KEY_ID="<your_s3_access_key_id>";`

    `export AWS_SECRET_ACCESS_KEY="<your_s3_secret_key>";`

    `export AWS_DEFAULT_REGION="your_aws_region";`

- Run `update_coins()` from `tasks.py` in your shell to fetch prediction from aws
    
    `$ python3.11 manage.py shell`
    
    `>>> from coin_prediction.tasks import update_coins()`

    `>>> update_coins()`

Finally you can run `python3.11 manage.py runserver`.
<br/><br/>

## 3. Differences from - the OG - Crpyti 📈
CryptiWeb is a webapp (This repo) developed using The Django Framwork to allow more users to get to know and try the project. It realizes a Long Shot Term Memory (LSTM) model [Crypti-LSTM](https://github.com/Anas-Elhounsri/Crypti-LSTM) to perform time series prediction instead of linear regression, and hosted on Amazon Web Services (AWS) with an architecture designed by [@Anas-Elhounsri](https://github.com/Anas-Elhounsri/). And finally the project is availabe as a mobile app [CryptiMobile](https://github.com/mosman4/cryptimobile) designed by [@mosman4](https://github.com/mosman4/).
<br/><br/>

## 4. Known issues 🐛
Although we have moved from using linear regression to using LSTM, we are aware that our model is not accurate because it only consumes one variable (Price). In the near future, we are planning on updating our model to a Multivariate LSTM including more variables for more accurate forcasting results.

Read more: 
- [What are LSTMs](https://machinelearningmastery.com/gentle-introduction-long-short-term-memory-networks-experts/)
- [Multivariate LSTM](https://www.researchgate.net/figure/The-framework-of-the-multivariate-long-short-term-memory-M-LSTM-model-for-CBM-daily_fig2_347587318)
<br/><br/>

## 5. Roadmap 🚀
We are planning to achieve the following by the end of '23
- Update the model to a Multivariate LSTM
- Add more information to the website
- Enhance the look and feel of the app
- Conduct testing and re-adjustments on the model
<br></br>

## 6. Disclaimer ❗
This project is for educational, entertainment, and testing reasons only, it is by no means a financial advice/tool, and it should not be relied on for any finanial decisions.
<br/><br/>

Finally, we will be more than happy to see your contribution.
