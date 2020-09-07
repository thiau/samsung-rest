# Samsung REST

Expose REST APIs for [samsungctl](https://github.com/Ape/samsungctl)

## How to run this project
1 - Run `pip install -r requirements.txt`

2 - Create `.env` file and add these variables:
| Variable Name | Value          |
|---------------|----------------|
| TV_HOSTNAME   | TV IP Address  |
| TV_PORT       | TV Port number |

3 - Run the app using `python app.py`

## Available endpoints

| Endpoint | Action              |
|----------|---------------------|
| /power   | Switch TV to on/off |

Endpoints can be declared in `server/routes/tv_routes.py` and implemented in `tv/samsung_tv.py`. All available actions can be found [here](https://github.com/Ape/samsungctl#key-codes).

## Reference 
https://github.com/Ape/samsungctl