{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "76ba6b88-f162-4922-8a35-43828460a08f",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4e0d4afc-0c90-4a69-a5ee-03c6c8f12b53",
   "metadata": {},
   "outputs": [],
   "source": [
    "def load_and_process(\"weatherstats_kelowna_daily.csv\"):\n",
    "   \n",
    "    ## Loading data, dropping unwanted columns, handle Nan values, replacing index\n",
    "\n",
    "df1 = (pd.read_csv(\"weatherstats_kelowna_daily.csv\")\n",
    "       .drop(columns=['max_humidex', 'min_windchill','max_relative_humidity','avg_hourly_relative_humidity','avg_relative_humidity','avg_cloud_cover_4',\n",
    "                       'min_cloud_cover_4','max_cloud_cover_8','avg_hourly_cloud_cover_8','avg_cloud_cover_8','min_cloud_cover_8','max_cloud_cover_10',\n",
    "                       'avg_hourly_cloud_cover_10','max_wind_speed','avg_hourly_wind_speed','avg_wind_speed','min_wind_speed','max_wind_gust','daylight','sunrise_f','sunset_f'\n",
    "                        ,'avg_cloud_cover_10','avg_cloud_cover_10','min_cloud_cover_10','min_relative_humidity',\n",
    "                       'max_dew_point','avg_hourly_dew_point','avg_dew_point','min_dew_point','max_cloud_cover_4','avg_hourly_cloud_cover_4',\n",
    "                      'wind_gust_dir_10s','max_pressure_sea','avg_hourly_pressure_sea','avg_pressure_sea','min_pressure_sea',\n",
    "                      'max_pressure_station','avg_hourly_pressure_station','avg_pressure_station','min_pressure_station',\n",
    "                       'max_visibility','avg_hourly_visibility','avg_visibility','min_visibility','max_health_index',\n",
    "                      'avg_hourly_health_index','avg_health_index','min_health_index','heatdegdays','cooldegdays','growdegdays_5','growdegdays_7','growdegdays_10',\n",
    "                      'min_uv_forecast','max_uv_forecast','min_high_temperature_forecast','max_high_temperature_forecast','min_low_temperature_forecast','max_low_temperature_forecast'])\n",
    "        .dropna()\n",
    "        .reset_index()\n",
    "      )\n",
    "return df1"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
