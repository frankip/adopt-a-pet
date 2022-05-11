import os

class Config:
    PET_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    PET_API_KEY = 'key'


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}