# Create dummy secrey key so we can use sessions
SECRET_KEY = '123456790'

# database connection
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://flask_admin_geo:flask_admin_geo@localhost/flask_admin_geo'
SQLALCHEMY_ECHO = True

# credentials for loading map tiles from mapbox
MAPBOX_MAP_ID = 'mapbox.streets'
MAPBOX_ACCESS_TOKEN = 'pk.eyJ1IjoidG9tZ29icmF2byIsImEiOiJjajZwZzVyZnYwdGZlMnFvMTZyaXR3bmU3In0.fM7v2OUbs3hsBgwgioVIaA'

# when the creating new shapes, use this default map center
DEFAULT_CENTER_LAT = -33.918861
DEFAULT_CENTER_LONG = 18.423300
