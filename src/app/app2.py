import streamlit as st
import pandas as pd
import numpy as np
import csv

st.title("Alkoholkonsum")

from scipy.stats import linregress

st.subheader("Vorhersage")

years = [2000, 2005, 2010, 2015, 2018]
consumption_per_year_GER = [14.16, 13.28, 12.64, 13.06, 12.91]
consumption_per_year_AT = [13.12, 12.79, 12.2, 12.07, 11.96]
consumption_per_year_PL = [9.17, 10.6, 11.21, 11.63, 11.71]
consumption_per_year_EU = [12.64, 12.30, 11.21, 11.38, 11.44]

regression_result_GER = linregress(years, consumption_per_year_GER)
scipy_slope_GER = regression_result_GER.slope
scipy_intercept_GER = regression_result_GER.intercept

regression_result_AT = linregress(years, consumption_per_year_AT)
scipy_slope_AT = regression_result_AT.slope
scipy_intercept_AT = regression_result_AT.intercept

regression_result_PL = linregress(years, consumption_per_year_PL)
scipy_slope_PL = regression_result_PL.slope
scipy_intercept_PL = regression_result_PL.intercept

regression_result_EU = linregress(years, consumption_per_year_EU)
scipy_slope_EU = regression_result_EU.slope
scipy_intercept_EU = regression_result_EU.intercept


def scipy_model_GER(desired_year):
    model_result = scipy_slope_GER * desired_year + scipy_intercept_GER
    return model_result

def scipy_model_AT(desired_year):
    model_result = scipy_slope_AT * desired_year + scipy_intercept_AT
    return model_result

def scipy_model_PL(desired_year):
    model_result = scipy_slope_PL * desired_year + scipy_intercept_PL
    return model_result

def scipy_model_EU(desired_year):
    model_result = scipy_slope_EU * desired_year + scipy_intercept_EU
    return model_result

auswahl = st.selectbox('Wähle ein Land aus:', ('Germany', 'Austria', 'Poland', 'European Union'))
desired_year= st.number_input('Jahr', value=2022)

prediction_GER = scipy_model_GER(desired_year)
prediction_rounded_GER = round(prediction_GER, 2)

prediction_AT = scipy_model_AT(desired_year)
prediction_rounded_AT = round(prediction_AT, 2)

prediction_PL = scipy_model_PL(desired_year)
prediction_rounded_PL = round(prediction_PL, 2)

prediction_EU = scipy_model_EU(desired_year)
prediction_rounded_EU = round(prediction_EU, 2)

if auswahl == "Austria":
    st.write(prediction_rounded_AT)

elif auswahl == "Poland":
    st.write(prediction_rounded_PL)

elif auswahl == "Germany":
    st.write(prediction_rounded_GER)

elif auswahl == "European Union":
    st.write(prediction_rounded_EU)

else: st.write('Bitte Land auswählen')










#%%

#%%
