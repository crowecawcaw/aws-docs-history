Amazon Monitron is no longer open to new customers. Existing customers can
continue to use the service as normal. For capabilities similar to Amazon
Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron "https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron").

# Understanding sensor measurements

When a sensor is initially paired to an asset, Amazon Monitron will learn from the
vibration and temperature data collected from the equipment, establishing a baseline to
determine what is "normal" for that asset. It will use this learning to detect potential
failures in the future.

Depending on the situation, operational scenario, use case, and various parameters
like the asset’s duty cycle, Amazon Monitron will take between 14 and 21 days to
establish this baseline. During this initial learning and training phase, the asset is
assumed to be healthy.

After establishing a baseline for the asset, Amazon Monitron monitors the data it
collects, looking for an event or trend that indicates a potential failure. It
specifically watches for increases in temperature, or vibration levels, or both.
Increases in temperature and vibrations are two of the main indicators of a
malfunctioning machine. Machine abnormalities often indicate that an asset is starting
to fail.

Amazon Monitron uses vibration thresholds established by the International
Organization of Standardization (ISO) for your class of machinery. It applies the ISO
thresholds in combination with its self-training model to assess actual thresholds to
fit your equipment. For example, if your machine runs a little hot or a little cold, or
if it vibrates a little bit more than standard, Amazon Monitron adjusts the
thresholds slightly so that it can more accurately identify when the machine is acting
abnormally.

The only alarms you will recieve during the initial learning and training period will
be from the ISO model (which does not require any learning period). You should treat ISO
alarms during the training period as you would any alarm—acknowledge the alarm,
perform any necessary review of the machine, and then close out the alarm with the
suitable action taken code. After that time, Amazon Monitron continues to fine-tune
the baseline, building a better picture of "normal" as the sensor collects more
data.

If temperature or vibration levels inconsistently rise above the modified threshold, a
failure might be possible, but is probably not imminent. In that case, Amazon Monitron sends a `Warning` notification. If the increase is consistently above the
threshold, the conditions are clearly abnormal and a failure is much more likely. Under
those circumstances, Amazon Monitron sends an `Alarm` notification to the
mobile or web app.

|                                                                                                                                       |                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Notifications screen showing alarms and warnings for various positions with vibration and temperature data. a mobile app notification | Notifications panel showing alarms and warnings for various positions with detected vibration and temperature issues. a web app notification | In this example, the Position 3 sensor has detected a persistent increase in temperature and vibration, indicating that a potential failure needs to be investigated. |
|                                                                                                                                       |                                                                                                                                              |
| ---                                                                                                                                   | ---                                                                                                                                          |
| Pump monitoring interface showing vibration and temperature alarms with graphical data.                                               | Dashboard showing vibration and temperature data for a pump main asset with alarm notifications.                                             |
