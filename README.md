# Apple Products Price Comparison
This script was developed to compare the price of different Apple products in different places across the globe.


### Pre-requisites
1. Exchange Rates Data API Key (Create an account and copy key from here: https://apilayer.com/marketplace/exchangerates_data-api)


### Instructions
1. Clone the repository and change to project directory.
2. Copy the file `.env.template` to `.env` and then replace the API key with the one you copied from Exchange Rates Data API.
    ```sh
    cp .env.template .env
    ````
3. Create a virtual environment and install dependencies from `requirements.txt` file.
    ```sh
    python -m venv env
    source env/bin/activate
    pip install -r requirements.txt
    ```
3. Run `script.py`.
    ```sh
    python script.py
    ```

Run `python script.py --help` for a list of available options.


### Contributing
Contributors are heartily welcome. The following things are still to be done:
1. Automatic scraping of the product prices from the Apple website
2. Add options to list only certain products.
3. Add options to list only certain countries / places.


### Screenshots
![Screenshot](screenshots/screenshot_1.png "Screenshot")
