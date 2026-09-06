

# Step 3: Transfer data from Amazon S3 to a SaaS destination
<a name="flow-tutorial-s3-salesforce"></a>

Amazon S3 now hosts your data, but you still need to synchronize all your records in the destination. To transfer data to a supported destination, you must create and run a flow with Amazon AppFlow. In this step, you use the AWS Management Console to send data from Amazon S3 to either Salesforce or another software as a service (SaaS) application.

**Topics**
+ [Prerequisites](#flow-tutorial-s3-salesforce-prerequisites)
+ [Create a flow](#flow-tutorial-create-s3-salesforce-flow)
+ [Run a flow](#flow-tutorial-run-s3-salesforce-flow)
+ [View transferred data](#view-transferred-data)
+ [(Optional) Edit flow to add validations](#edit-add-validation)

## Prerequisites
<a name="flow-tutorial-s3-salesforce-prerequisites"></a>

Before you begin, complete [Step 1: Upload data to Amazon S3](flow-tutorial-set-up-source.md).

## Create a flow
<a name="flow-tutorial-create-s3-salesforce-flow"></a>

The following procedures detail how to create a flow from Amazon S3 to Salesforce, but you can follow the steps with any destination.

**To complete Step 1: Specify flow details**

1. Open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/). Ensure the AWS Region of your Amazon AppFlow console is the same one as your S3 bucket.

1. Choose **Create flow**.

1. For **Flow name**, enter **s3-to-{{SaaS}}**. For example, if your destination is Salesforce, enter **s3-to-salesforce**.

1. Under **Data encryption**, you have the option to activate custom encryption settings. By default, Amazon AppFlow encrypts your data with a key in AWS Key Management Service (AWS KMS). AWS creates, uses, and manages this key for you. Amazon AppFlow always encrypts your data during transit and at rest. The default encryption is adequate for this tutorial, so don't select custom encryption settings. For more information, see [Data protection](https://docs.aws.amazon.com/appflow/latest/userguide/data-protection.html) in the *Amazon AppFlow User Guide*.

1. Under **Tags**, you have the option to add tags to your flow. Tags are key-value pairs that assign metadata to resources that you create. Tags are not necessary for this tutorial. For more information, see [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the *AWS General Reference*.

1.  To continue to Step 2: Configure flow, choose **Next**.

**To complete Step 2: Configure flow**

1. For **Source name**, choose **Amazon S3**.

1. In **Bucket details**, for *Choose an S3 bucket*, select your S3 bucket.

1. For *Enter bucket prefix*, enter **source**. Bucket prefixes are folders.

1. Ensure **Data format preference** is **CSV format**.

1. Configure the **Destination details**. These details vary based on the destination that you want to transfer data to.
   + If you want to transfer data to Salesforce, do the following:

     1. For **Destination name**, select **Salesforce**.

     1. For **Choose Salesforce connection**, select your connection. For example, select `my-salesforce-connection`, the connection that you created in the previous step.
**Tip**  
If you don't have a connection, you can choose **Connect** to create one now.

     1. If you want to use the sample data that you downloaded, for **Choose Salesforce object**, select **Account**.
   + If you want to transfer data to another supported application besides Salesforce, do the following:

     1. For **Destination name**, select the destination that you want for your data.

     1. For **Choose connection**, select the connection that you created, or create one.

     1. Select **object** and specify the correct object type for your data.

     1. If there are any other destination details, configure the required fields.

1. In the **Error handling** section, you can specify how you want the flow to handle errors and where to put the data that causes errors. For this tutorial, you can leave the settings in this section at their default values.

1. For **Flow trigger**, leave the default selection **Run on demand**. When you select this value, you use a single button in the console to run the flow.
**Tip**  
You can also run flows on a schedule. Amazon AppFlow bases the time zone for this schedule on your web browser. For more information, see [Schedule-triggered flows](https://docs.aws.amazon.com/appflow/latest/userguide/flow-triggers.html) in the *Amazon AppFlow User Guide*.

1. To continue to Step 3: Map data fields, choose **Next**.

**To complete Step 3: Map data fields**

1. Map your data fields. These vary based on the destination for your data transfer.
   + If you're transferring to Salesforce, do the following:

     1. Under **Mapping method**, leave the default selection **Manually map fields**.

     1. Under **Destination record preference**, leave the default selection **Insert new records**.

     1. In the **Source to destination field mapping** section, select the *Choose source fields* dropdown and select **Map all fields directly**.
**Important**  
If you use the sample data, ensure Account Name maps to Account Name, Account Type maps to Account Type, Billing State/Province maps to Billing State/Province, Account Rating maps to Account Rating, and Industry maps to Industry.

     1. Choose **Map selected fields**.
   + If you want to transfer data to another supported application besides Salesforce, do the following:

     1. Select **Mapping method** and specify how you want to map your data. You can choose to map the source fields to the destination fields manually, or else upload a .csv file that includes these mappings.

     1. Map your fields from the source field name to the destination field name.

1. Under **Validations**, specify what happens to invalid data within the flow. For this step, you don't need any validations.

1. To continue to Step 4: Add filters, choose **Next**.

**To complete Step 4: Add filters**

1. Under **Filters**, specify what data the flow transfers. With this setting, you can ensure the flow transfers data only when it meets certain criteria. For this tutorial, you don't need any filters.

1. To continue to Step 5: Review and create, choose **Next**.

**To complete Step 5: Review and create**
+ Review the flow settings, and then choose **Create flow**.

## Run a flow
<a name="flow-tutorial-run-s3-salesforce-flow"></a>

You now have a run-on-demand flow. When you choose the **Run flow** button in the console, this flow transfers your data.

**To run a flow**

1. In **Flows**, select your flow from the list.

1. Choose **Run flow**.

When the flow successfully runs, a banner appears. If you use the provided data, the banner shows nine processed records.

![Success message for flow run.](http://docs.aws.amazon.com/appflow/latest/userguide/images/flow-success.png)


## View transferred data
<a name="view-transferred-data"></a>

After your flow runs, you can view the data in the destination.

**To view transferred data**
+ If you use the sample Salesforce account data, navigate to your Salesforce **Account tab** to view the imported account records. For more information on Salesforce accounts, see [Salesforce accounts](https://help.salesforce.com/s/articleView?id=sf.accounts).

You have now transferred data from Amazon S3 to Salesforce or the SaaS application that you chose. If you used Salesforce and the sample data, you have synchronized and expanded your Salesforce account data.

## (Optional) Edit flow to add validations
<a name="edit-add-validation"></a>

The flow that you ran transferred all the records in the data set. You can add validations to a flow so that you transfer only valid records. In this procedure, if you use the sample data, you edit your Amazon S3 to Salesforce flow to transfer only account records with ratings.

Before you edit and run the flow again, delete the records that you transferred from the original flow.

**To delete account records in Salesforce**
+ Follow the directions in [Mass Delete Records](https://help.salesforce.com/s/articleView?id=sf.admin_massdelete.htm).

For the sample data set, suppose you consider account records valid only if they have an account rating. Two of the account records don't have associated account ratings. You don't want these records to transfer from Amazon S3 so that you only have valid data in Salesforce.

**To edit a flow and add validations**

1. Open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. In **Flows**, choose your flow.

1. Choose **Actions**, then choose **Edit flow**.

1. Choose **Next** until you reach **Step 3: Edit data fields**.

1. In **Validations**, choose **Add validation**.

1. If you use the sample data, for **Field name**, select **Account rating**. For **Condition**, choose **Values missing or null**. For **Action**, choose **Ignore record**. This configuration will omit the transfer of account records with missing rating values.  
![Example4 and Example8 are missing account rating values.](http://docs.aws.amazon.com/appflow/latest/userguide/images/validate-data.png)

1. Choose **Save**.

**To run the edited flow and view transferred data**

1. In **Flows**, select your flow from the list.

1. Choose **Run flow**. When the flow successfully runs, a banner appears.  
![Success message for flow run.](http://docs.aws.amazon.com/appflow/latest/userguide/images/flow-success.png)

1. If you use the sample Salesforce account data, navigate to your Salesforce **Account** tab to view the imported account records. For more information on Salesforce accounts, see [Salesforce Accounts](https://help.salesforce.com/s/articleView?id=sf.accounts).

If you used the sample data, only seven of the nine records transferred. `Example4` and `Example8` do not appear because they have no account ratings associated with them.