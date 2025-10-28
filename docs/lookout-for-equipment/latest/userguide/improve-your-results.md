On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# Improving your results

To improve the results, consider the following:

- Did unrecorded maintenance events, system inefficiencies, or a new normal
  operating mode happen during the time of flagged anomalies in the test set? If
  so, the results indicate those situations. Change your train-evaluation splits
  so that each normal mode is captured during model training.
- Are the sensor inputs relevant to the failure labels? In other words, is it
  possible that the labels are related to one component of the equipment but the
  sensors are monitoring a different component? If so, consider building a new
  model where the sensor inputs and labels are relevant to each other and drop any
  irrelevant sensors. Alternatively, drop the labels you're using and train the
  model only on the sensor data.
- Is the label time zone the same as the sensor data time zone? If not, consider
  adjusting the time zone of your label data to align with sensor data time zone.
- Is the failure label range inadequate? In other words, could there be
  anomalous behavior outside of the label range? This can happen for a variety of
  reasons, such as when the anomalous behavior was observed much earlier than the
  actual repair work. If so, consider adjusting the range accordingly.
- Are there data integrity issues with your sensor data? For example, do some of
  the sensors become nonfunctional during the training or evaluation data? In that
  case, consider dropping those sensors when you run the model. Alternatively, use
  a training-evaluation split that filters out the non-functional part of the
  sensor data.
- Does the sensor data include uninteresting normal-operating modes, such as
  off-periods or ramp-up or ramp-down periods? Consider filtering those out of the
  sensor data.
- We recommend that you avoid using data that contains monotonically increasing
  values, such as operating hours or mileage.
