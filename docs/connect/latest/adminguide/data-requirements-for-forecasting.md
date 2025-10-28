# Data requirements for

forecasting in Amazon Connect

Amazon Connect generates forecasts using a machine-learning model tailored for contact
center operations. The following are the historical input data requirements for both
short-term and long-term forecasts.

- **Historical data minimum requirement**: At least 1
  forecast group should have a minimum of 1,000 contacts per month in the last
  6 months.
- **Historical data maximum duration**: Forecasting models
  use a maximum of 156 weeks of historical data.
- For a queue channel to have non-zero forecasts, it needs at least 1 record
  in last 4 weeks or 28 days.
