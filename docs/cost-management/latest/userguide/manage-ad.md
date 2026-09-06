

# Detecting unusual spend with AWS Cost Anomaly Detection
<a name="manage-ad"></a>

AWS Cost Anomaly Detection is a feature that uses machine learning models to detect and alert on anomalous spend patterns in your deployed AWS services.

Using AWS Cost Anomaly Detection includes the following benefits: 
+ You receive alerts individually in aggregated reports either in an email message or an Amazon SNS topic. 

  For Amazon SNS topics, create an Amazon Q Developer in chat applications configuration that maps the Amazon SNS topic to a Slack channel or an Amazon Chime chat room. For more information, see [Receiving anomaly alerts in chat applications](cad-alert-chime.md).
+ You can evaluate your spend patterns using machine learning methods to minimize false positive alerts. For example, you can evaluate weekly or monthly seasonality and natural growth.
+ You can investigate the root causes of the anomaly, ranked by their dollar impact and split across four dimensions: AWS service, AWS account, Region, or usage type.
+ You can configure how to evaluate your costs. Choose whether you want to analyze all of your AWS services independently or analyze specific member accounts, cost allocation tags, or cost categories.

After your billing data is processed, AWS Cost Anomaly Detection runs approximately three times a day in order to monitor for anomalies in your net unblended cost data (that is, net costs after all applicable discounts are calculated). You might experience a slight delay in receiving alerts. Cost Anomaly Detection uses data from Cost Explorer, which has a delay of up to 24 hours. As a result, it can take up to 24 hours to detect an anomaly after a usage occurs. If you create a new monitor, it can take 24 hours to begin detecting new anomalies. For a new service subscription, 10 days of historical service usage data is needed before anomalies can be detected for that service.

**Note**  
You can opt out of Cost Anomaly Detection at any time. For more information, see [Opting out of Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/opting-out-cad.html).  
Cost Anomaly Detection isn't available for bill source accounts that use billing transfer. Cost Anomaly Detection doesn't support billing transfer views.  
Cost Anomaly Detection does not monitor third-party products and services available through AWS Marketplace, except for third-party foundation models on Amazon Bedrock. These models appear in Cost Explorer and on your bill under the AWS Marketplace billing entity. To get alerts for other AWS Marketplace charges, use AWS Budgets. A cost budget tracks your total AWS costs, including AWS Marketplace. You can use the **Billing entity** filter to track AWS Marketplace charges specifically. For more information, see [Creating a budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create.html).

**Topics**
+ [Setting up your anomaly detection](settingup-ad.md)
+ [Controlling access for Cost Anomaly Detection](accesscontrol-ad.md)
+ [Getting started with AWS Cost Anomaly Detection](getting-started-ad.md)
+ [Transitioning from customer to AWS managed monitors](transition-monitors.md)
+ [Editing your alert preferences](edit-alert-pref.md)
+ [Creating an Amazon SNS topic for anomaly notifications](ad-SNS.md)
+ [Receiving anomaly alerts in chat applications](cad-alert-chime.md)
+ [Using EventBridge with Cost Anomaly Detection](cad-eventbridge.md)
+ [Using AWS User Notifications with Cost Anomaly Detection](cad-user-notifications.md)
+ [Opting out of Cost Anomaly Detection](opting-out-cad.md)
+ [Investigating anomaly root causes with Amazon Q Developer](investigating-ad.md)