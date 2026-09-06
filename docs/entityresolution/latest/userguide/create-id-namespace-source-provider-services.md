

# Creating an ID namespace source (provider services)
<a name="create-id-namespace-source-provider-services"></a>

This topic describes the process of creating an ID namespace source using the **Provider services** method. This method uses a provider service called LiveRamp. LiveRamp translates third-party encoded data from a source to a target during an ID mapping workflow. 

**Note**  
If the input data is the source, then it must have a schema mapping and an associated AWS Glue database.

**To create an ID namespace source (provider services)**

1. Sign in to the AWS Management Console and open the AWS Entity Resolution console at [https://console.aws.amazon.com/entityresolution/](https://console.aws.amazon.com/entityresolution/).

1. In the left navigation pane, under **Data preparation**, choose **ID namespaces**.

1. On the **ID namespaces** page, in the upper right corner, choose **Create ID namespace**.

1. For **Details**, do the following:

   1. For **ID namespace name**, enter a unique name.

   1. (Optional) For **Description**, enter an optional description.

   1. For **ID namespace type**, choose **Source**.

1. For the **ID namespace method**, choose **Provider services**.
**Note**  
AWS Entity Resolution currently offers the LiveRamp provider service as an ID namespace method. If you have a subscription to LiveRamp, then the status appears as **Subscribed**. For more information about how to subscribe to LiveRamp, see [Step 1: Subscribe to a provider service on AWS Data Exchange](prepare-third-party-input-data.md#subscribe-provider-service).

1. For **Data input**, choose the **AWS Region**, **AWS Glue database**, the **AWS Glue table**, and the **Schema mapping** from the dropdown list.

   You can add up to 20 data inputs.

1. To specify the **Service access** permissions, choose an option and take the recommended action.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/entityresolution/latest/userguide/create-id-namespace-source-provider-services.html)

1. (Optional) To enable **Tags** for the resource, choose **Add new tag**, and then enter the **Key** and **Value** pair.

1. Choose **Create ID namespace**.

 The ID namespace source is created. You are now ready to [create an ID namespace target](create-id-namespace-target.md).