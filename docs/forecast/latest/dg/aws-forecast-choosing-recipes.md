

 Amazon Forecast is no longer available to new customers. Existing customers of Amazon Forecast can continue to use the service as normal. [Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/)

# Amazon Forecast Algorithms
<a name="aws-forecast-choosing-recipes"></a>

An Amazon Forecast predictor uses an algorithm to train a model with your time series datasets. The trained model is then used to generate metrics and predictions. 

 If you are unsure of which algorithm to use to train your model, choose AutoML when creating a predictor and let Forecast train the optimal model for your datasets. Otherwise, you can manually select one of the Amazon Forecast algorithms. 

**Python notebooks**  
For a step-by-step guide on using AutoML, see [Getting Started with AutoML](https://github.com/aws-samples/amazon-forecast-samples/blob/master/notebooks/advanced/Getting_started_with_AutoML/Getting_started_with_AutoML.ipynb).

## Built-in Forecast Algorithms
<a name="forecast-algos"></a>

 Amazon Forecast provides six built-in algorithms for you to choose from. These range from commonly used statistical algorithms like Autoregressive Integrated Moving Average (ARIMA), to complex neural network algorithms like CNN-QR and DeepAR\+. 

### [CNN-QR](aws-forecast-algo-cnnqr.md)
<a name="cnnqr"></a>

 `arn:aws:forecast:::algorithm/CNN-QR` 

 Amazon Forecast CNN-QR, Convolutional Neural Network - Quantile Regression, is a proprietary machine learning algorithm for forecasting time series using causal convolutional neural networks (CNNs). CNN-QR works best with large datasets containing hundreds of time series. It accepts item metadata, and is the only Forecast algorithm that accepts related time series data without future values. 

### [DeepAR\+](aws-forecast-recipe-deeparplus.md)
<a name="deeparplus"></a>

`arn:aws:forecast:::algorithm/Deep_AR_Plus`

 Amazon Forecast DeepAR\+ is a proprietary machine learning algorithm for forecasting time series using recurrent neural networks (RNNs). DeepAR\+ works best with large datasets containing hundreds of feature time series. The algorithm accepts forward-looking related time series and item metadata. 

### [Prophet](aws-forecast-recipe-prophet.md)
<a name="prophet"></a>

`arn:aws:forecast:::algorithm/Prophet`

 Prophet is a time series forecasting algorithm based on an additive model where non-linear trends are fit with yearly, weekly, and daily seasonality. It works best with time series with strong seasonal effects and several seasons of historical data. 

### [NPTS](aws-forecast-recipe-npts.md)
<a name="npts"></a>

`arn:aws:forecast:::algorithm/NPTS`

 The Amazon Forecast Non-Parametric Time Series (NPTS) proprietary algorithm is a scalable, probabilistic baseline forecaster. NPTS is especially useful when working with sparse or intermittent time series. Forecast provides four algorithm variants: Standard NPTS, Seasonal NPTS, Climatological Forecaster, and Seasonal Climatological Forecaster. 

### [ARIMA](aws-forecast-recipe-arima.md)
<a name="arima"></a>

`arn:aws:forecast:::algorithm/ARIMA`

 Autoregressive Integrated Moving Average (ARIMA) is a commonly used statistical algorithm for time-series forecasting. The algorithm is especially useful for simple datasets with under 100 time series. 

### [ETS](aws-forecast-recipe-ets.md)
<a name="ets"></a>

`arn:aws:forecast:::algorithm/ETS`

 Exponential Smoothing (ETS) is a commonly used statistical algorithm for time-series forecasting. The algorithm is especially useful for simple datasets with under 100 time series, and datasets with seasonality patterns. ETS computes a weighted average over all observations in the time series dataset as its prediction, with exponentially decreasing weights over time. 

## Comparing Forecast Algorithms
<a name="comparing-algos"></a>

 Use the following table to find the best option for your time series datasets. 


<table>
<thead>
  <tr><th></th><th colspan="2">Neural Networks</th><th>Flexible Local Algorithms</th><th colspan="3">Baseline Algorithms</th></tr>
  <tr><th></th><th>CNN-QR</th><th>DeepAR+</th><th>Prophet</th><th>NPTS</th><th>ARIMA</th><th>ETS</th></tr>
</thead>
<tbody>
  <tr><td>Computationally intensive training process</td><td>High</td><td>High</td><td>Medium</td><td>Low</td><td>Low</td><td>Low</td></tr>
  <tr><td>Accepts historical related time series*</td><td><img src="http://docs.aws.amazon.com/forecast/latest/dg/images/icon-yes.png" alt="" /> </td><td><img src="http://docs.aws.amazon.com/forecast/latest/dg/images/icon-no.png" alt="" /> </td><td><img src="http://docs.aws.amazon.com/forecast/latest/dg/images/icon-no.png" alt="" /> </td><td><img src="http://docs.aws.amazon.com/forecast/latest/dg/images/icon-no.png" alt="" /> </td><td><img src="http://docs.aws.amazon.com/forecast/latest/dg/images/icon-no.png" alt="" /> </td><td><img src="http://docs.aws.amazon.com/forecast/latest/dg/images/icon-no.png" alt="" /> </td></tr>
  <tr><td>Accepts forward-looking related time series*</td><td><img src="http://docs.aws.amazon.com/forecast/latest/dg/images/icon-yes.png" alt="" /> </td><td><img src="http://docs.aws.amazon.com/forecast/latest/dg/images/icon-yes.png" alt="" /> </td><td><img src="http://docs.aws.amazon.com/forecast/latest/dg/images/icon-yes.png" alt="" /> </td><td><img src="http://docs.aws.amazon.com/forecast/latest/dg/images/icon-no.png" alt="" /> </td><td><img src="http://docs.aws.amazon.com/forecast/latest/dg/images/icon-no.png" alt="" /> </td><td><img src="http://docs.aws.amazon.com/forecast/latest/dg/images/icon-no.png" alt="" /> </td></tr>
  <tr><td>Accepts item metadata (product color, brand, etc)</td><td><img src="http://docs.aws.amazon.com/forecast/latest/dg/images/icon-yes.png" alt="" /> </td><td><img src="http://docs.aws.amazon.com/forecast/latest/dg/images/icon-yes.png" alt="" /> </td><td><img src="http://docs.aws.amazon.com/forecast/latest/dg/images/icon-no.png" alt="" /> </td><td><img src="http://docs.aws.amazon.com/forecast/latest/dg/images/icon-no.png" alt="" /> </td><td><img src="http://docs.aws.amazon.com/forecast/latest/dg/images/icon-no.png" alt="" /> </td><td><img src="http://docs.aws.amazon.com/forecast/latest/dg/images/icon-no.png" alt="" /> </td></tr>
  <tr><td>Accepts the Weather Index built-in featurization</td><td><img src="http://docs.aws.amazon.com/forecast/latest/dg/images/icon-yes.png" alt="" /> </td><td><img src="http://docs.aws.amazon.com/forecast/latest/dg/images/icon-yes.png" alt="" /> </td><td><img src="http://docs.aws.amazon.com/forecast/latest/dg/images/icon-yes.png" alt="" /> </td><td><img src="http://docs.aws.amazon.com/forecast/latest/dg/images/icon-no.png" alt="" /> </td><td><img src="http://docs.aws.amazon.com/forecast/latest/dg/images/icon-no.png" alt="" /> </td><td><img src="http://docs.aws.amazon.com/forecast/latest/dg/images/icon-no.png" alt="" /> </td></tr>
  <tr><td>Suitable for sparse datasets</td><td><img src="http://docs.aws.amazon.com/forecast/latest/dg/images/icon-yes.png" alt="" /> </td><td><img src="http://docs.aws.amazon.com/forecast/latest/dg/images/icon-yes.png" alt="" /> </td><td><img src="http://docs.aws.amazon.com/forecast/latest/dg/images/icon-no.png" alt="" /> </td><td><img src="http://docs.aws.amazon.com/forecast/latest/dg/images/icon-yes.png" alt="" /> </td><td><img src="http://docs.aws.amazon.com/forecast/latest/dg/images/icon-no.png" alt="" /> </td><td><img src="http://docs.aws.amazon.com/forecast/latest/dg/images/icon-no.png" alt="" /> </td></tr>
  <tr><td>Performs Hyperparameter Optimization (HPO)</td><td><img src="http://docs.aws.amazon.com/forecast/latest/dg/images/icon-yes.png" alt="" /> </td><td><img src="http://docs.aws.amazon.com/forecast/latest/dg/images/icon-yes.png" alt="" /> </td><td><img src="http://docs.aws.amazon.com/forecast/latest/dg/images/icon-no.png" alt="" /> </td><td><img src="http://docs.aws.amazon.com/forecast/latest/dg/images/icon-no.png" alt="" /> </td><td><img src="http://docs.aws.amazon.com/forecast/latest/dg/images/icon-no.png" alt="" /> </td><td><img src="http://docs.aws.amazon.com/forecast/latest/dg/images/icon-no.png" alt="" /> </td></tr>
  <tr><td>Allows overriding default hyperparameter values </td><td><img src="http://docs.aws.amazon.com/forecast/latest/dg/images/icon-yes.png" alt="" /> </td><td><img src="http://docs.aws.amazon.com/forecast/latest/dg/images/icon-yes.png" alt="" /> </td><td><img src="http://docs.aws.amazon.com/forecast/latest/dg/images/icon-no.png" alt="" /> </td><td><img src="http://docs.aws.amazon.com/forecast/latest/dg/images/icon-yes.png" alt="" /> </td><td><img src="http://docs.aws.amazon.com/forecast/latest/dg/images/icon-no.png" alt="" /> </td><td><img src="http://docs.aws.amazon.com/forecast/latest/dg/images/icon-no.png" alt="" /> </td></tr>
</tbody>
</table>


\*For more information on related time series, see [Related Time Series](related-time-series-datasets.md). 