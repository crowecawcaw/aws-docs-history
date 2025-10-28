# Advanced model building configurations

Amazon SageMaker Canvas supports various advanced settings that you can configure when building a model.
The following page lists all of the advanced settings along with additional information
about their options and configurations.

###### Note

The following advanced settings are currently only supported for numeric, categorical,
and time series forecasting model types.

## Advanced numeric and categorical

prediction model settings

Canvas supports the following advanced settings for numeric and categorical
prediction model types.

### Objective

metric

The objective metric is the metric that you want Canvas to optimize while
building your model. If you don’t select a metric, Canvas chooses one for you by
default. For descriptions of the available metrics, see the [Metrics reference](canvas-metrics.md "canvas-metrics.md").

### Training method

Canvas can automatically select the training method based on the dataset size,
or you can select it manually. The following training methods are available for you
to choose from:

- **Ensembling** – SageMaker AI leverages the
  AutoGluon library to train several base models. To find the best combination
  for your dataset, ensemble mode runs 5–10 trials with different model and meta
  parameter settings. Then, these models are combined using a stacking
  ensemble method to create an optimal predictive model. For a list of
  algorithms supported by ensemble mode for tabular data, see the following
  [Algorithms](#canvas-advanced-settings-predictive-algos "#canvas-advanced-settings-predictive-algos")
  section.
- **Hyperparameter optimization (HPO)**
  – SageMaker AI finds the best version of a model by tuning hyperparameters
  using Bayesian optimization or multi-fidelity optimization while running
  training jobs on your dataset. HPO mode selects the algorithms that are most
  relevant to your dataset and selects the best range of hyperparameters to
  tune your models. To tune your models, HPO mode runs up to 100 trials
  (default) to find the optimal hyperparameters settings within the selected
  range. If your dataset size is less than 100 MB, SageMaker AI uses Bayesian
  optimization. SageMaker AI chooses multi-fidelity optimization if your dataset is
  larger than 100 MB.

For a list of algorithms supported by HPO mode for tabular data, see the
following [Algorithms](#canvas-advanced-settings-predictive-algos "#canvas-advanced-settings-predictive-algos")
section.

- **Auto** – SageMaker AI automatically chooses
  either ensembling mode or HPO mode based on your dataset size. If your
  dataset is larger than 100 MB, SageMaker AI chooses HPO mode. Otherwise, it chooses
  ensembling mode.

### Algorithms

In **Ensembling** mode, Canvas supports the following machine
learning algorithms:

- [LightGBM](lightgbm.md "lightgbm.md") – An optimized framework that uses tree-based
  algorithms with gradient boosting. This algorithm uses trees that grow in
  breadth, rather than depth, and is highly optimized for speed.
- [CatBoost](catboost.md "catboost.md") – A framework that uses tree-based algorithms
  with gradient boosting. Optimized for handling categorical variables.
- [XGBoost](xgboost.md "xgboost.md") – A framework that uses tree-based algorithms
  with gradient boosting that grows in depth, rather than breadth.
- [Random Forest](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html "https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html") – A tree-based algorithm that uses several
  decision trees on random sub-samples of the data with replacement. The trees
  are split into optimal nodes at each level. The decisions of each tree are
  averaged together to prevent overfitting and improve predictions.
- [Extra Trees](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html#sklearn.ensemble.ExtraTreesClassifier "https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html#sklearn.ensemble.ExtraTreesClassifier") – A tree-based algorithm that uses several
  decision trees on the entire dataset. The trees are split randomly at each
  level. The decisions of each tree are averaged to prevent overfitting and to
  improve predictions. Extra trees add a degree of randomization in comparison
  to the random forest algorithm.
- [Linear Models](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.linear_model "https://scikit-learn.org/stable/modules/classes.html#module-sklearn.linear_model") – A framework that uses a linear equation
  to model the relationship between two variables in observed data.
- Neural network torch – A neural network model that's implemented
  using [Pytorch](https://pytorch.org/ "https://pytorch.org/").
- Neural network fast.ai – A neural network model that's implemented
  using [fast.ai](https://www.fast.ai/ "https://www.fast.ai/").

In **HPO mode**, Canvas supports the following machine
learning algorithms:

- [XGBoost](xgboost.md "xgboost.md") – A supervised learning algorithm that attempts
  to accurately predict a target variable by combining an ensemble of
  estimates from a set of simpler and weaker models.
- Deep learning algorithm – A multilayer perceptron (MLP) and
  feedforward artificial neural network. This algorithm can handle data that
  is not linearly separable.

### Data split

You have the option to specify how you want to split your dataset between the
training set (the portion of your dataset used for building the model) and the
validation set, (the portion of your dataset used for verifying the model’s
accuracy). For example, a common split ratio is 80% training and 20% validation,
where 80% of your data is used to build the model while 20% is saved for measuring
model performance. If you don’t specify a custom ratio, then Canvas splits your
dataset automatically.

### Max

candidates

###### Note

This feature is only available in the HPO training mode.

You can specify the maximum number of model candidates that Canvas generates
while building your model. We recommend that you use the default number of
candidates, which is 100, to build the most accurate models. The maximum number you
can specify is 250. Decreasing the number of model candidates may impact your
model’s accuracy.

### Max job

runtime

You can specify the maximum job runtime, or the maximum amount of time that
Canvas spends building your model. After the time limit, Canvas stops
building and selects the best model candidate.

The maximum time that you can specify is 720 hours. We highly recommend that you
keep the maximum job runtime greater than 30 minutes to ensure that Canvas has
enough time to generate model candidates and finish building your model.

## Advanced time series forecasting

model settings

For time series forecasting models, Canvas supports the Objective metric,
which is listed in the previous section.

Time series forecasting models also support the following advanced setting:

### Algorithm selection

When you build a time series forecasting model, Canvas uses an
_ensemble_ (or a combination) of statistical and machine learning
algorithms to deliver highly accurate time series forecasts. By default, Canvas selects the optimal combination
of all the available algorithms based on the time series in your dataset. However, you have the option to specify
one or more algorithms to use for your forecasting model. In this case, Canvas determines the best blend
using only your selected algorithms. If you're uncertain about which algorithm to select for training your model,
we recommend that you choose all of the available algorithms.

###### Note

Algorithm selection is only supported for standard builds. If you don’t select any algorithms in
the advanced settings, then by default SageMaker AI runs a quick build and trains model candidates using a single
tree-based learning algorithm. For more information about the difference between quick builds and standard builds, see
[How custom models work](canvas-build-model.md "canvas-build-model.md").

Canvas supports the following time series forecasting algorithms:

- [Autoregressive Integrated Moving Average (ARIMA)](https://en.wikipedia.org/wiki/Autoregressive_integrated_moving_average "https://en.wikipedia.org/wiki/Autoregressive_integrated_moving_average") – A simple stochastic time series model
  that uses statistical analysis to interpret the data and make future predictions. This algorithm is useful for simple
  datasets with fewer than 100 time series.
- [Convolutional Neural Network - Quantile Regression (CNN-QR)](../../../forecast/latest/dg/aws-forecast-algo-cnnqr.md "../../../forecast/latest/dg/aws-forecast-algo-cnnqr.md") – A proprietary, supervised
  learning algorithm that trains one global model from a large collection of time series and uses a quantile decoder
  to make predictions. CNN-QR works best with large datasets containing hundreds of time series.
- [DeepAR+](../../../forecast/latest/dg/aws-forecast-recipe-deeparplus.md "../../../forecast/latest/dg/aws-forecast-recipe-deeparplus.md") – A proprietary, supervised learning algorithm for forecasting scalar time series using
  recurrent neural networks (RNNs) to train a single model jointly over all of the time series. DeepAR+ works best
  with large datasets containing hundreds of feature time series.
- [Non-Parametric Time Series (NPTS)](../../../forecast/latest/dg/aws-forecast-recipe-npts.md "../../../forecast/latest/dg/aws-forecast-recipe-npts.md") – A scalable, probabilistic baseline forecaster that predicts
  the future value distribution of a given time series by sampling from past observations. NPTS is useful when working
  with sparse or intermittent time series (for example, forecasting demand for individual items where the time series
  has many 0s or low counts).
- [Exponential Smoothing (ETS)](https://en.wikipedia.org/wiki/Exponential_smoothing "https://en.wikipedia.org/wiki/Exponential_smoothing")
  – A forecasting method that produces forecasts which are weighted averages of past observations where the
  weights of older observations exponentially decrease. The algorithm is useful for simple datasets with fewer than 100
  time series and datasets with seasonality patterns.
- [Prophet](https://facebook.github.io/prophet/ "https://facebook.github.io/prophet/") – An additive regression
  model that works best with time series that have strong seasonal effects and several seasons of historical data.
  The algorithm is useful for datasets with non-linear growth trends that approach a limit.

### Forecast

quantiles

For time series forecasting, SageMaker AI trains 6 model candidates with your target time
series. Then, SageMaker AI combines these models using a stacking ensemble method to create
an optimal forecasting model for a given objective metric. Each forecasting model
generates a probabilistic forecast by producing forecasts at quantiles between P1
and P99. These quantiles are used to account for forecast uncertainty. By default,
forecasts are generated for 0.1 (`p10`), 0.5 (`p50`), and 0.9
(`p90`). You can choose to specify up to five of your own quantiles
from 0.01 (`p1`) to 0.99 (`p99`), by increments of 0.01 or
higher.
