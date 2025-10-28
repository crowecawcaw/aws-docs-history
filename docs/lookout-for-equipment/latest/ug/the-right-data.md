On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# Choosing the right data

Your dataset should contain time-series data that's generated from an industrial asset
such as a pump, compressor, motor, and so on. Each asset should be generating data from
one or more sensors. The data that Lookout for Equipment uses for training should be representative of
the condition and operation of the asset. Making sure that you have the right data is
crucial. We recommend that you work with a SME. A SME can help you make sure that the
data is relevant to the aspect of the asset that you're trying to analyze. We recommend
that you remove unnecessary sensor data. With data from too few sensors, you might miss
critical information. With data from too many sensors, your model might overfit the data
and it might miss out on key patterns.

###### Important

Choosing the right input data is crucial to the success of using Lookout for Equipment. It might
take multiple iterations of trial and error to find the right inputs. We cannot
guarantee results. Success is highly dependent on the relevancy of your data to
equipment issues.

Use these guidelines to choose the right data:

- **Use only numerical data** – Remove
  nonnumerical data. Lookout for Equipment can't use non-numerical data for analysis.
- **Use only analog data** – Use only analog
  data (that is, many values that vary over time). Using digital values (also
  known as categorical values, or values that can be only one of a limited number
  of options), such as valve positions or set points, can lead to inconsistent or
  misleading results.
- **Remove continuously increasing data** –
  Remove data that is just an ever-increasing number, such as operating hours or
  mileage.
- **Use data for the relevant component or
  subcomponent** – You can use Lookout for Equipment to monitor an entire asset
  (such as a pump) or just a subcomponent (such as a pump motor). Determine where
  your downtime issues occur and choose the component or subcomponent that has the
  greater effect on that.
  When formatting a predictive maintenance problem, consider these guidelines:

- **Data size** – Although Lookout for Equipment can ingest
  more than 50 GB of data, it can use only 7 GB with a model. Factors such as the
  number of sensors used, how far back in history the dataset goes, and the sample
  rate of the sensors can all determine how many measurements this amount of data
  can include. This amount of data also includes the missing data imputed by
  Lookout for Equipment.
- **Missing data** – Lookout for Equipment automatically
  fills in missing data (known as imputing). It does this by forward filling
  previous sensor readings. However, if too much original data is missing, it
  might affect your results.
- **Sample rate** – _Sample rate_ is the interval at which the sensor readings are
  recorded. Use the highest frequency sample rate possible without exceeding the
  data size limit. The sample rate and data size might also increase your ML model
  training time. Lookout for Equipment handles any timestamp misalignment.
- **Number of sensors** – Lookout for Equipment can train a
  model with data from up to 300 sensors. However, having the right data is more
  important than the quantity of data. More is not necessarily better.
- **Vibration** – Although vibration data is
  usually important for identifying potential failure, Lookout for Equipment does not work with
  raw high-frequency data. When using high-frequency vibration data, first
  generate the key values from the vibration data, such as RMS and FFT.

## Filtering for normal data

Make sure that you use only data from normal (standard) operations. To do this,
identify a key operating metric that indicates that the equipment is operating in a
standard fashion. For example, when operating a compressor in a refinery, the key
metric is usually production flow rate. In this case, you would need to filter out
times when the production flow rate is below normal due to reduced production or any
reason other than abnormal behavior. Other examples of key metrics might be RPM,
fuel efficiency, "run" state, availability, and so on. Lookout for Equipment assumes that the data
is normal. Making sure that the data fits this assumption is very important.

## Using failure labels

To provide insight into past events, Lookout for Equipment uses labels that call out these events
for the ML model. Providing this data is optional, but if it's available, it can
help train your model more accurately and efficiently.

For information about using labels, see [Understanding labeling](understanding-labeling.md "understanding-labeling.md") and [Labeling your data](labeling-data.md "labeling-data.md").
