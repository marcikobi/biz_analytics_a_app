import streamlit as st

st.title("Prediction of annual alcohol consumption per capita in the EU and chosen countries")

from scipy.stats import linregress

st.subheader("Prediction")

years = [2000, 2005, 2010, 2015, 2018]
consumption_per_year_GER = [14.16, 13.28, 12.64, 13.06, 12.91]
consumption_per_year_AT = [13.12, 12.79, 12.2, 12.07, 11.96]
consumption_per_year_PL = [9.17, 10.6, 11.21, 11.63, 11.71]
consumption_per_year_EU = [12.64, 12.30, 11.21, 11.38, 11.44]
consumption_per_year_NL = [11.08, 10.71, 10.21, 9.55, 9.61]
consumption_per_year_FR = [14.08, 13.09, 12.4, 12.64, 12.33]
consumption_per_year_DEN = [12.67, 12.29, 11, 10.36, 10.26]
consumption_per_year_CZ = [15, 14.76, 14.06, 14.25, 14.45]
consumption_per_year_CH = [12.49,11.64,11.41,11.58,11.53]
consumption_per_year_BEL = [12.49, 13.13, 11.4, 11.82, 11.08]
consumption_per_year_LUX = [14.32,13.58,12.98,13.18,12.94]

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

regression_result_NL = linregress(years, consumption_per_year_NL)
scipy_slope_NL = regression_result_NL.slope
scipy_intercept_NL = regression_result_NL.intercept

regression_result_FR = linregress(years, consumption_per_year_FR)
scipy_slope_FR = regression_result_FR.slope
scipy_intercept_FR = regression_result_FR.intercept

regression_result_DEN = linregress(years, consumption_per_year_DEN)
scipy_slope_DEN = regression_result_DEN.slope
scipy_intercept_DEN = regression_result_DEN.intercept

regression_result_CZ = linregress(years, consumption_per_year_CZ)
scipy_slope_CZ = regression_result_CZ.slope
scipy_intercept_CZ = regression_result_CZ.intercept

regression_result_CH = linregress(years, consumption_per_year_CH)
scipy_slope_CH = regression_result_CH.slope
scipy_intercept_CH = regression_result_CH.intercept

regression_result_BEL = linregress(years, consumption_per_year_BEL)
scipy_slope_BEL = regression_result_BEL.slope
scipy_intercept_BEL = regression_result_BEL.intercept

regression_result_LUX = linregress(years, consumption_per_year_LUX)
scipy_slope_LUX = regression_result_LUX.slope
scipy_intercept_LUX = regression_result_LUX.intercept


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

def scipy_model_NL(desired_year):
    model_result = scipy_slope_NL * desired_year + scipy_intercept_NL
    return model_result

def scipy_model_FR(desired_year):
    model_result = scipy_slope_FR * desired_year + scipy_intercept_FR
    return model_result

def scipy_model_DEN(desired_year):
    model_result = scipy_slope_DEN * desired_year + scipy_intercept_DEN
    return model_result

def scipy_model_CZ(desired_year):
    model_result = scipy_slope_CZ * desired_year + scipy_intercept_CZ
    return model_result

def scipy_model_CH(desired_year):
    model_result = scipy_slope_CH * desired_year + scipy_intercept_CH
    return model_result

def scipy_model_BEL(desired_year):
    model_result = scipy_slope_BEL * desired_year + scipy_intercept_BEL
    return model_result

def scipy_model_LUX(desired_year):
    model_result = scipy_slope_LUX * desired_year + scipy_intercept_LUX
    return model_result





auswahl = st.selectbox('Choose a country:', ('Austria', 'Belgium', 'Czech Republic', 'Denmark', 'France', 'Germany', 'Luxembourg', 'Netherlands', 'Poland', 'Switzerland', 'European Union'))
desired_year= st.number_input('Year', value=2022)

prediction_GER = scipy_model_GER(desired_year)
prediction_rounded_GER = round(prediction_GER, 2)

prediction_AT = scipy_model_AT(desired_year)
prediction_rounded_AT = round(prediction_AT, 2)

prediction_PL = scipy_model_PL(desired_year)
prediction_rounded_PL = round(prediction_PL, 2)

prediction_EU = scipy_model_EU(desired_year)
prediction_rounded_EU = round(prediction_EU, 2)

prediction_NL = scipy_model_NL(desired_year)
prediction_rounded_NL = round(prediction_NL, 2)

prediction_FR = scipy_model_FR(desired_year)
prediction_rounded_FR = round(prediction_FR, 2)

prediction_DEN = scipy_model_DEN(desired_year)
prediction_rounded_DEN = round(prediction_DEN, 2)

prediction_CZ = scipy_model_CZ(desired_year)
prediction_rounded_CZ = round(prediction_CZ, 2)

prediction_CH = scipy_model_CH(desired_year)
prediction_rounded_CH = round(prediction_CH, 2)

prediction_BEL = scipy_model_BEL(desired_year)
prediction_rounded_BEL = round(prediction_BEL, 2)

prediction_LUX = scipy_model_LUX(desired_year)
prediction_rounded_LUX = round(prediction_LUX, 2)

difference_GER = prediction_rounded_GER - prediction_rounded_EU
difference_rounded_GER = round(difference_GER, 2)

difference_AT = prediction_rounded_AT - prediction_rounded_EU
difference_rounded_AT = round(difference_AT, 2)

difference_PL = prediction_rounded_PL - prediction_rounded_EU
difference_rounded_PL = round(difference_PL, 2)

difference_EU = prediction_rounded_EU - prediction_rounded_EU
difference_rounded_EU = round(difference_EU, 2)

difference_NL = prediction_rounded_NL - prediction_rounded_EU
difference_rounded_NL = round(difference_NL, 2)

difference_FR = prediction_rounded_FR - prediction_rounded_EU
difference_rounded_FR = round(difference_FR, 2)

difference_DEN = prediction_rounded_DEN - prediction_rounded_EU
difference_rounded_DEN = round(difference_DEN, 2)

difference_CZ = prediction_rounded_CZ - prediction_rounded_EU
difference_rounded_CZ = round(difference_CZ, 2)

difference_CH = prediction_rounded_CH - prediction_rounded_EU
difference_rounded_CH = round(difference_CH, 2)

difference_BEL = prediction_rounded_BEL - prediction_rounded_EU
difference_rounded_BEL = round(difference_BEL, 2)

difference_LUX = prediction_rounded_LUX - prediction_rounded_EU
difference_rounded_LUX = round(difference_LUX, 2)

if auswahl == "Austria":
    "The prediction of alcohol consuption for "
    st.write(auswahl)
    "for the year"
    st.write(desired_year)
    "amounts to"
    st.write(prediction_rounded_AT)
    "liter per capita"

    "The difference to the EU average in the selected year is"
    st.write(difference_rounded_AT)


elif auswahl == "Poland":
    "The prediction of alcohol consumption for "
    st.write(auswahl)
    "for the year"
    st.write(desired_year)
    "amounts to"
    st.write(prediction_rounded_PL)
    "liter per capita"

    "The difference to the EU average in the selected year is"
    st.write(difference_rounded_PL)

elif auswahl == "Germany":
    "The prediction of alcohol consumption for "
    st.write(auswahl)
    "for the year"
    st.write(desired_year)
    "amounts to"
    st.write(prediction_rounded_GER)
    "liter per capita"

    "The difference to the EU average in the selected year is"
    st.write(difference_rounded_GER)

elif auswahl == "European Union":
    "The prediction of alcohol consumption for "
    st.write(auswahl)
    "for the year"
    st.write(desired_year)
    "amounts to"
    st.write(prediction_rounded_EU)
    "liter per capita"

elif auswahl == "Netherlands":
    "The prediction of alcohol consumption for "
    st.write(auswahl)
    "for the year"
    st.write(desired_year)
    "amounts to"
    st.write(prediction_rounded_NL)
    "liter per capita"

    "The difference to the EU average in the selected year is"
    st.write(difference_rounded_NL)

elif auswahl == "France":
    "The prediction of alcohol consumption for "
    st.write(auswahl)
    "for the year"
    st.write(desired_year)
    "amounts to"
    st.write(prediction_rounded_FR)
    "liter per capita"

    "The difference to the EU average in the selected year is"
    st.write(difference_rounded_FR)

elif auswahl == "Denmark":
    "The prediction of alcohol consumption for "
    st.write(auswahl)
    "for the year"
    st.write(desired_year)
    "amounts to"
    st.write(prediction_rounded_DEN)
    "liter per capita"

    "The difference to the EU average in the selected year is"
    st.write(difference_rounded_DEN)

elif auswahl == "Czech Republic":
    "The prediction of alcohol consumption for "
    st.write(auswahl)
    "for the year"
    st.write(desired_year)
    "amounts to"
    st.write(prediction_rounded_CZ)
    "liter per capita"

    "The difference to the EU average in the selected year is"
    st.write(difference_rounded_CZ)

elif auswahl == "Switzerland":
    "The prediction of alcohol consumption for "
    st.write(auswahl)
    "for the year"
    st.write(desired_year)
    "amounts to"
    st.write(prediction_rounded_CH)
    "liter per capita"

    "The difference to the EU average in the selected year is"
    st.write(difference_rounded_CH)

elif auswahl == "Belgium":
    "The prediction of alcohol consumption for "
    st.write(auswahl)
    "for the year"
    st.write(desired_year)
    "amounts to"
    st.write(prediction_rounded_BEL)
    "liter per capita"

    "The difference to the EU average in the selected year is"
    st.write(difference_rounded_BEL)

elif auswahl == "Luxembourg":
    "The prediction of alcohol consumption for "
    st.write(auswahl)
    "for the year"
    st.write(desired_year)
    "amounts to"
    st.write(prediction_rounded_LUX)
    "liter per capita"

    "The difference to the EU average in the selected year is"
    st.write(difference_rounded_LUX)


else:
    "please select data"

"" \
"" \
"" \
"" \
""


"The model is a linear regression model based on data from 2000 to 2018."
"Data points are available for each of the years 2000, 2005, 2010, 2015, and 2018"

"The data is from the following source:"
"http://data.worldbank.org/data-catalog/world-development-indicators"













#%%

#%%
