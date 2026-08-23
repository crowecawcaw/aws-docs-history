# Monitoring Forecast Performance

Amazon Connect Decisions tracks five standard statistical metrics to measure forecast accuracy
for the user specified prediction lead time in the plan configuration:

- **MAPE (Mean Absolute Percentage Error)**: (1/n) ×
  Σ |Actual - Forecast| / |Actual| × 100%

  - Measures the average percentage error across all forecasts.

###### Note

Forecast references the forecast that was generated at your specified prediction
lead time before the actual demand period occurred. Based on your plan
configuration, the system measures accuracy by comparing the forecast created a
specific number of time buckets in advance to the actual demand—for example,
if your time bucket is weeks and your prediction lead time is 3 weeks, the
“Forecast” value in accuracy formulas (MAPE, WAPE, RMSE, Bias, and
MAE) references the forecast that was created 3 weeks prior to each demand
period.

- **WAPE (Weighted Absolute Percentage Error)**: Σ
  |Actual - Forecast| / Σ |Actual| × 100%

  - Gives more weight to high-volume products.

- **RMSE (Root Mean Square Error)**:
  √[(1/n) × Σ (Actual - Forecast)²]

  - Emphasizes larger forecast errors.

- **Bias (Forecast Bias)**: Σ (Forecast - Actual) /
  Σ |Actual| × 100%

  - Indicates whether forecasts systematically over-predict or
    under-predict.

- **MAE (Mean Absolute Error)**: (1/n) × Σ
  |Actual - Forecast|

  - Provides the average error in the same units as your demand.
