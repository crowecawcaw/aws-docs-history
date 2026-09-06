

# Creating an ID mapping workflow (provider services)
<a name="create-id-mapping-workflow-provider-services"></a>

After completing the [prerequisites](create-idmw-two-accounts-prerequisite.md), you can create one or more ID mapping workflows using the LiveRamp provider service. LiveRamp translates a set of source RampIDs to another set using either maintained or derived RampIDs.

**To create an ID mapping workflow using the provider service**

1. Sign in to the AWS Management Console and open the AWS Entity Resolution console at [https://console.aws.amazon.com/entityresolution/](https://console.aws.amazon.com/entityresolution/).

1. In the left navigation pane, under **Workflows**, choose **ID mapping**.

1. On the **ID mapping workflows** page, in the upper right corner, choose **Create ID mapping workflow**.

1. For **Step 1: Specify ID mapping workflow details**, do the following.

   1. Enter an **ID mapping workflow name** and an optional **Description**.

      ![The Name and Description fields on the Specify ID mapping workflow details page](http://docs.aws.amazon.com/entityresolution/latest/userguide/images/specify-ID-mapping-details-name.png)

   1. For the **ID mapping method**, choose **Provider services**.

      AWS Entity Resolution currently offers the LiveRamp provider service as an ID mapping method. If you have a subscription to LiveRamp, then the status appears as **Subscribed**. For more information about how to subscribe to LiveRamp, see [Step 1: Subscribe to a provider service on AWS Data Exchange](prepare-third-party-input-data.md#subscribe-provider-service).

      ![The Subscribed status for the LiveRamp ID mapping method on the Specify ID mapping workflow page](http://docs.aws.amazon.com/entityresolution/latest/userguide/images/id-mapping-method.PNG)
**Note**  
Ensure that your data input file format aligns with the provider service's guidelines. For more information about LiveRamp's input file formatting guidelines, see [Perform Translation Through ADX](https://docs.liveramp.com/identity/en/perform-transcoding-through-adx.html) on the LiveRamp documentation website.

   1. For **LiveRamp configuration**, enter the following values that LiveRamp provides:
      + **Client ID manager ARN** 
      + **Client secret manager ARN**

      ![The LiveRamp configuration fields on the Specify ID mapping workflow page](http://docs.aws.amazon.com/entityresolution/latest/userguide/images/liveramp-configuration.PNG)

   1. (Optional) To enable **Tags** for the resource, choose **Add new tag**, and then enter the **Key** and **Value** pair.

   1. Choose **Next**.

1. For **Step 2: Specify source and target**, do the following.

   1. Turn on **Advanced options**.

   1. For **Source**, choose **ID namespace**.

      ![The Source fields on the Specify source and target page](http://docs.aws.amazon.com/entityresolution/latest/userguide/images/specify-source-id-namespace.PNG)

   1. For ID namespace, identify where the ID namespace is located, and then take the recommended action.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/entityresolution/latest/userguide/create-id-mapping-workflow-provider-services.html)

   1. For **Target**, choose **ID namespace**.

      ![The Target field on the Specify source and target page](http://docs.aws.amazon.com/entityresolution/latest/userguide/images/specify-target-id-namespace.PNG)

   1. To specify the **Service access** permissions, choose an option and take the recommended action.

      ![The Service access options on the Specify source and target page](http://docs.aws.amazon.com/entityresolution/latest/userguide/images/specify-source-target-service-access.PNG)    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/entityresolution/latest/userguide/create-id-mapping-workflow-provider-services.html)

1. Choose **Next**.

1. For **Step 3: Specify data output location – *optional***, do the following.

   1. For **Data output destination**, do the following.

      1. Choose the **Amazon S3 location** for the data output.

      1. For **Encryption**, if you choose to **Customize encryption settings**, then enter the **AWS KMS key** ARN or choose **Create an AWS KMS key**.

   1. View the **LiveRamp generated output**.

   1. Choose **Next**.

      ![The Data output destination fields on the Specify data output location page](http://docs.aws.amazon.com/entityresolution/latest/userguide/images/specify-data-ouput-IDM.PNG)

1. For **Step 4: Review and create**, do the following.

   1. Review the selections that you made for the previous steps and edit them if necessary.

   1. Choose **Create**.

      A message appears, indicating that the ID mapping workflow has been created.

After you create the ID mapping workflow, you're ready to [run an ID mapping workflow](run-id-mapping-workflow.md).