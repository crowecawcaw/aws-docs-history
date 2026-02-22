# Understanding the ML algorithm used by

Amazon Quick Sight

|                                                                                                                                                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| You don't need any technical experience in machine learning to use<br>the ML-powered features in Amazon Quick Sight. This section dives into the<br>technical aspects of the algorithm, for those who want the details<br>about how it works. This information isn't required reading to use<br>the features. |

Amazon Quick Sight uses a built-in version of the Random Cut Forest (RCF) algorithm. The
following sections explain what that means and how it is used in Amazon Quick Sight.

First, let's look at some of the terminology involved:

- Anomaly – Something that is characterized by its difference from the
  majority of the other things in the same sample. Also known as an outlier, an
  exception, a deviation, and so on.
- Data point – A discrete unit—or simply put, a row—in a
  dataset. However, a row can have multiple data points if you use a measure over
  different dimensions.
- Decision Tree – A way of visualizing the decision process of the
  algorithm that evaluates patterns in the data.
- Forecast – A prediction of future behavior based on current and past
  behavior.
- Model – A mathematical representation of the algorithm or what the
  algorithm learns.
- Seasonality – The repeating patterns of behavior that occur cyclically
  in time series data.
- Time series – An ordered set of date or time data in one field or
  column.

###### Topics

- [What's the
  difference between anomaly detection and forecasting?](difference-between-anomaly-detection-and-forecasting.md "difference-between-anomaly-detection-and-forecasting.md")
- [What is RCF?](what-is-random-cut-forest.md "what-is-random-cut-forest.md")
- [How RCF is applied to detect
  anomalies](how-does-rcf-detect-anomalies.md "how-does-rcf-detect-anomalies.md")
- [How RCF is applied to generate
  forecasts](how-does-rcf-generate-forecasts.md "how-does-rcf-generate-forecasts.md")
- [References for machine
  learning and RCF](learn-more-about-machine-learning-and-rcf.md "learn-more-about-machine-learning-and-rcf.md")
