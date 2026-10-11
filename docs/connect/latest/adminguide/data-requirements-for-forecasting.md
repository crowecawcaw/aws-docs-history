

# Data requirements for forecasting in Connect Customer
<a name="data-requirements-for-forecasting"></a>

Connect Customer generates forecasts using a machine-learning model tailored for contact center operations. The following are the historical input data requirements for both short-term and long-term forecasts.
+ **Historical data minimum requirement**: A queue and channel combination must have at least 1 contact in the last 28 days and at least 1 contact older than 7 days.
+ **Historical data maximum duration**: Forecasting models use a maximum of 156 weeks of historical data.
+ **Recommended for forecast accuracy**: A forecast group should have a minimum of 1,000 contacts per month in the last 6 months.