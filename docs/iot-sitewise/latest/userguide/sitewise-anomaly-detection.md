# Native anomaly detection

AWS IoT SiteWise native anomaly detection is a machine learning (ML) feature for monitoring
industrial equipment that detects abnormal equipment behavior and identifies potential failures.
With native anomaly detection, you can implement predictive maintenance programs and identify
suboptimal equipment processes.

AWS IoT SiteWise native anomaly detection doesn’t require extensive ML knowledge or experience. You simply select the
properties to train a custom ML model that finds potential failures for you. AWS IoT SiteWise native anomaly detection
automatically creates the best model to learn your equipment’s normal operating conditions. The
model is optimized to find abnormal equipment behavior that occurred in the historical data.
Using either the AWS IoT SiteWise console or the SDK, you run the model to process new time-series data
according to your desired schedule.

To use AWS IoT SiteWise native anomaly detection, you do the following:

- Select the properties and the time period that you would like to train against.
- Add the periods of historical failures shown in the data (label data), if it
  exists.
- Train your ML model using AWS IoT SiteWise native anomaly detection. Optionally you can configure automatic
  retraining to keep your model updated over time.
- Setup your inference schedule to test your live data streams against your trained
  model.
  Native anomaly detection monitors fixed and stationary industrial equipment that operates with limited
  variability in operating conditions. Supported equipment includes rotating machinery such as
  pumps, compressors, motors, computer numerical control (CNC) machines, and turbines. Process
  industry applications include heat exchangers, boilers, and inverters. Native anomaly detection is a back-end
  analytics service integrated into AWS IoT SiteWise and supplements existing maintenance systems.

###### Topics

- [Native anomaly detection features](sitewise-anomaly-detection-features.md "sitewise-anomaly-detection-features.md")
- [Prerequisites](anomaly-prerequisites.md "anomaly-prerequisites.md")
- [Enable anomaly detection on sensors of an asset](anom-detection-sensors-asset.md "anom-detection-sensors-asset.md")
- [Enable anomaly detection on sensors across
  assets](anom-detection-sensors-across-asset.md "anom-detection-sensors-across-asset.md")
- [Advanced training configurations](adv-training-configs.md "adv-training-configs.md")
- [Advanced inference configurations](advanced-inference-configurations.md "advanced-inference-configurations.md")
- [Review inference results](reviewing-inference-results.md "reviewing-inference-results.md")
- [Trigger custom actions on
  anomalous behavior (AWS Management Console)](trigger-custom-actions-anomalous-behavior.md "trigger-custom-actions-anomalous-behavior.md")
- [Best practices](ano-best-practices.md "ano-best-practices.md")
