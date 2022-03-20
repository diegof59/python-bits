# datetimes.py

from datetime import datetime
import pytz

my_datetime:datetime = datetime.now() # Local datetime if setted, else UTC datetime

my_dt_str:str = my_datetime.strftime('%d/%m/%Y') # day/month/year format

bogota_tz = pytz.timezone('America/Bogota') # Bogotá timezone
bogota_dt = datetime.now(bogota_tz) # Datetime in Bogotá