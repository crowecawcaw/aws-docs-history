

# Amazon Lookout for Metrics
<a name="lookout"></a>

The following are the requirements and connection instructions for using Amazon Lookout for Metrics with Amazon AppFlow.

**Note**  
You can use Amazon Lookout for Metrics as a destination only.

**Topics**
+ [Requirements](#lookout-requirements)
+ [Setup instructions](#lookout-setup)
+ [Notes](#lookout-notes)
+ [Related resources](#lookout-resources)

## Requirements
<a name="lookout-requirements"></a>
+ To get access to Amazon Lookout for Metrics, you must first be added to the allow list. To request access, see [Amazon Lookout for Metrics Preview](https://pages.awscloud.com/AmazonLookout-for-MetricsPreview.html). For more information about the service, see [Amazon Lookout for Metrics](https://aws.amazon.com/lookout-for-metrics/).

## Setup instructions
<a name="lookout-setup"></a>

**To create a flow with Amazon Lookout for Metrics as the destination**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. Choose **Create flow** and enter a name for your flow.

1. Under **Data encryption**, choose **Customize encryption settings (advanced)** then select an existing customer managed key (CMK) or create a new one. The default AWS managed CMK is not supported when using Amazon Lookout for Metrics as a destination.

1. (Optional) To add a tag, choose **Tags**, **Add tag** and then enter the key name and value.

1. Choose **Next**.

1. For **Source details**, choose a supported source and provide the requested information.

1. For **Destination details**, choose Amazon Lookout for Metrics as the destination for your time-series data.

1. When using Amazon Lookout for Metrics as a destination, only the **Run flow on schedule** option is available. Specify the appropriate schedule settings, such as the frequency, start date, and start time. You can also enter an end date (optional).

   Amazon Lookout for Metrics currently supports the following scheduling options:
   + If the source supports minutes: you can run the flow every 5 or 10 minutes by selecting **5** or **10** from the **Every** dropdown list.
   + If the source supports hours: you can run the flow once an hour by selecting **1** from the **Every** dropdown list.
   + If the source supports days: you can run the flow once a day by selecting **1** from the **Every** dropdown list.

1. Choose **Next**.

1. Under **Source to destination field mapping**, go to the **Source field name** dropdown list and choose **Map all fields directly**. Alternatively, you can manually select the fields that you want to use from the list.
**Note**  
A timestamp field is not required in your data. However, in order to use the anomaly detection feature of Amazon Lookout for Metrics, you need at least one measure or numeric column with values changing over time.

1. (Optional) Under **Validations - optional**, add validations to check whether a field has bad data. For each field, choose the condition that indicates bad data and what action Amazon AppFlow should take when a field in a record is bad.

1. Choose **Next**.

1. (Optional) Specify a filter to determine which records to transfer. To add a filter, choose **Add filter**, select the field name, select a condition, and then specify the criteria.

1. Choose **Next**.

1. Review the settings and then choose **Create flow**.

## Notes
<a name="lookout-notes"></a>
+ The default AWS managed CMK is not supported when using Amazon Lookout for Metrics as a destination.
+ The following sources are supported when using Amazon Lookout for Metrics as a destination:
  + Amplitude
  + Dynatrace
  + Google Analytics
  + Infor Nexus
  + Marketo
  + Salesforce
  + ServiceNow
  + Singular
  + Trend Micro
  + Veeva
  + Zendesk
+ Amazon Lookout for Metrics currently supports the following scheduling options:
  + If the source supports minutes: you can run the flow every 5 or 10 minutes 
  + If the source supports hours: you can run the flow once an hour
  + If the source supports days: you can run the flow once a day 

## Related resources
<a name="lookout-resources"></a>
+ [Amazon Lookout for Metrics](https://aws.amazon.com/lookout-for-metrics/) service page
+ [Amazon Lookout for Metrics Preview](https://pages.awscloud.com/AmazonLookout-for-MetricsPreview.html) 