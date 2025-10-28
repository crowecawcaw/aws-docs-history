# Detecting unusual spend with AWS Cost Anomaly Detection

AWS Cost Anomaly Detection is a feature that uses machine learning models to detect and alert on anomalous
spend patterns in your deployed AWS services.

Using AWS Cost Anomaly Detection includes the following benefits:

- You receive alerts individually in aggregated reports either in an email message
  or an Amazon SNS topic.

For Amazon SNS topics, create an Amazon Q Developer in chat applications configuration that maps the SNS
topic to a Slack channel or an Amazon Chime chat room. For more information, see [Receiving anomaly alerts in chat applications](cad-alert-chime.md "cad-alert-chime.md").

- You can evaluate your spend patterns using machine learning methods to minimize
  false positive alerts. For example, you can evaluate weekly or monthly seasonality
  and natural growth.
- You can investigate the root causes of the anomaly, ranked by their dollar impact
  and split across four dimensions: AWS service, AWS account, Region, or usage
  type.
- You can configure how to evaluate your costs. Choose whether you want to analyze
  all of your AWS services independently or analyze specific member accounts, cost
  allocation tags, or cost categories.
  After your billing data is processed, AWS Cost Anomaly Detection runs approximately three times a day in
  order to monitor for anomalies in your net unblended cost data (that is, net costs after all
  applicable discounts are calculated). You might experience a slight delay in receiving
  alerts. Cost Anomaly Detection uses data from Cost Explorer, which has a delay of up to 24 hours. As a
  result, it can take up to 24 hours to detect an anomaly after a usage occurs. If you create
  a new monitor, it can take 24 hours to begin detecting new anomalies. For a new service
  subscription, 10 days of historical service usage data is needed before anomalies can be
  detected for that service.

###### Note

You can opt out of Cost Anomaly Detection at any time. For more information, see [Opting out of Cost Anomaly Detection](opting-out-cad.md "opting-out-cad.md").

###### Topics

- [Setting up your anomaly detection](settingup-ad.md "settingup-ad.md")
- [Controlling access for Cost Anomaly Detection](accesscontrol-ad.md "accesscontrol-ad.md")
- [Getting started with AWS Cost Anomaly Detection](getting-started-ad.md "getting-started-ad.md")
- [Editing your alert preferences](edit-alert-pref.md "edit-alert-pref.md")
- [Creating an Amazon SNS topic for anomaly notifications](ad-SNS.md "ad-SNS.md")
- [Receiving anomaly alerts in chat applications](cad-alert-chime.md "cad-alert-chime.md")
- [Using EventBridge with Cost Anomaly Detection](cad-eventbridge.md "cad-eventbridge.md")
- [Using AWS User Notifications with
  Cost Anomaly Detection](cad-user-notifications.md "cad-user-notifications.md")
- [Opting out of Cost Anomaly Detection](opting-out-cad.md "opting-out-cad.md")
