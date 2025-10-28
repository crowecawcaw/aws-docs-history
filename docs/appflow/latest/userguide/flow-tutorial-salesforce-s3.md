# Step 4: Transfer data from a SaaS source to Amazon S3

Suppose you now want to transfer your data from Salesforce to Amazon S3. With Amazon S3, you can
synchronize and replicate customer relationship management (CRM) data into data lakes to
analyze or use to drive machine learning. To keep this information up to date, you can
create an event-triggered flow from Salesforce to Amazon S3. An event-triggered flow runs when
Amazon AppFlow detects a change to the target data in the CRM storage service.

After you create an S3 bucket, you can set up and run a flow with Amazon AppFlow to transfer
data from a supported source to the S3 bucket. You can use one S3 bucket as both a source
and destination, so you don't need to create a new S3 bucket if you already created one for
this tutorial. In this step, you use the AWS Management Console to create and run a flow from Salesforce
or another software as a service (SaaS) application to Amazon S3.

###### Topics

- [Prerequisites](#flow-tutorial-salesforce-s3-prerequisites "#flow-tutorial-salesforce-s3-prerequisites")
- [Change data capture in Salesforce](#change-data-capture-salesforce "#change-data-capture-salesforce")
- [Create a flow](#flow-tutorial-create-salesforce-s3-flow "#flow-tutorial-create-salesforce-s3-flow")
- [Run a flow (event-triggered or on-demand)](#flow-tutorial-run-salesforce-s3-flow "#flow-tutorial-run-salesforce-s3-flow")
- [View transferred data](#get-transferred-data "#get-transferred-data")

## Prerequisites

Before you begin, you need an S3 bucket to receive the data if you don't already have
one. You can use the same S3 bucket as both a source and destination for different
flows. This tutorial uses Salesforce for a SaaS account, but you can use another
supported source application if you want. Some flow options that this tutorial uses
don't work for a SaaS application other than Salesforce.

- Amazon S3 setup — If you don't already have an
  S3 bucket, [Create an S3 bucket](flow-tutorial-set-up-source.md#tutorial-create-bucket "flow-tutorial-set-up-source.md#tutorial-create-bucket") to
  prepare Amazon S3 to receive your data.
- Salesforce setup (Optional) — If you
  already have a Salesforce account, or you want to complete this tutorial with a
  different SaaS application, you can skip this step. Sign up for a free
  Salesforce developer account [here](https://developer.salesforce.com/signup "https://developer.salesforce.com/signup").
- Transfer data to Salesforce (Optional) —
  If you use Salesforce for this tutorial, we recommend that you complete [Step 3: Transfer data from Amazon S3](flow-tutorial-s3-salesforce.md "flow-tutorial-s3-salesforce.md")
  before you continue.

## Change data capture in Salesforce

To run an event-triggered flow, Amazon AppFlow needs to receive a notification when a record
changes. When you use the change data capture feature in Salesforce, you can generate
change event notifications for selected entities. If you don't have administrator-level
credentials, you might not be able to select entities to generate change notifications.
However, the free developer account has administrator privileges.

###### To enable change data capture

1. Open Salesforce at [www.salesforce.com](https://www.salesforce.com/ "https://www.salesforce.com/") and log in to your account.
2. Navigate to the **Change Data Capture**
   page.
3. If you use the sample data, select **Account
   (Account)** to generate change event notifications. Otherwise,
   select the appropriate entity for your data.

For more information about Salesforce change data capture, see [Change Data Capture](https://developer.salesforce.com/docs/atlas.en-us.change_data_capture.meta/change_data_capture/cdc_intro.htm "https://developer.salesforce.com/docs/atlas.en-us.change_data_capture.meta/change_data_capture/cdc_intro.htm").

## Create a flow

The following procedures detail how
to create a flow from Salesforce to Amazon S3, but you can follow the steps with any
supported source. Some flow options that this tutorial uses don't work for a SaaS
application other than Salesforce, but alternate steps appear.

###### To complete Step 1: Specify flow details

1. Open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. Choose **Create flow**.
3. For **Flow name**, enter ``SaaS`-to-s3`.
For example, if your source is Salesforce, enter `salesforce-to-s3`.
4. Under **Data encryption**, you have the option to
   activate custom encryption settings. By default, Amazon AppFlow encrypts your data with
   a key in AWS Key Management Service (AWS KMS). AWS creates, uses, and manages this key for you.
   Amazon AppFlow always encrypts your data during transit and at rest. The default
   encryption is adequate for this tutorial, so don't select custom encryption
   settings. For more information, see [Data protection](data-protection.md "data-protection.md")
   in the _Amazon AppFlow User Guide_.
5. Under **Tags**, you have the option to add tags
   to your flow. Tags are key-value pairs that assign metadata to resources that
   you create. Tags aren't necessary for this tutorial. For more information, see
   [Tagging
   AWS resources](../../../general/latest/gr/aws_tagging.md "../../../general/latest/gr/aws_tagging.md") in the _AWS General Reference_.
6. To continue to Step 2: Configure flow, choose **Next**.

###### To complete Step 2: Configure flow

1. Configure the **Source details**. These details
   vary based on the source that you want to transfer data from.
   - If you want to transfer data from Salesforce, do the following:
     1. For **Source name**, choose **Salesforce**.
     2. For **Choose Salesforce connection**, select your
        connection. For example, select `my-salesforce-connection`, the
        connection that you created in a previous step.

     ###### Tip

     If you don't have a connection, you can choose
     **Connect** to create one now. 3. Select **Salesforce events**. 4. If you use the sample data, for **Choose
     Salesforce event**, select **Account Change Event**. Otherwise, select the
     event that matches your data.

   - If you want to transfer data from another supported application
     besides Salesforce, do the following:
     1. For **Source name**, select the
        source that you want for your data.
     2. For **Choose connection**, select the
        connection that you created, or create one.
     3. Select **object** and specify the correct
        object type for your data.
     4. If there are any other source details, configure the required
        fields.

2. For **Destination name**, choose **Amazon S3**.
3. In **Bucket details**, for _Choose an S3
   bucket_, select your S3 bucket. Use the same S3 bucket that
   contains the `source` folder from the previous step.
4. For _Enter bucket prefix_, enter `destination`. Bucket prefixes are folders.

###### Tip

If you don't have a folder that matches the name that you entered, the flow
automatically creates one when it runs. 5. Configure the **Flow trigger**. This varies
based on the source where you want to transfer data from.

    * If you want to transfer data from Salesforce, leave the default
     selection **Run flow on event**.
    * If you want to transfer data from another supported application
     besides Salesforce, leave the default selection **Run on demand**. This option allows you to run the flow
     with the selection of one button in the console.


    ###### Tip

    You can also run flows on a schedule. Amazon AppFlow bases the time zone for this schedule on your web browser.
     For more information, see [Schedule-triggered flows](flow-triggers.md "flow-triggers.md") in the *Amazon AppFlow User Guide*.

6. To continue to Step 3: Map data fields, choose **Next**.

###### To complete Step 3: Map data fields

1. Under **Mapping method**, leave the default selection **Manually map
   fields**.
2. In the **Source to destination field
   mapping** section, select the _Choose source
   fields_ dropdown and select **Map all fields
   directly**.
3. Under **Validations**, specify what happens to invalid data
   within the flow. For this step, you don't need any validations.
4. To continue to Step 4: Add filters, choose **Next**.

###### To complete Step 4: Add filters

1. Under **Filters**, specify what data the flow transfers. With
   this setting, you can ensure the flow transfers data only when it meets certain
   criteria. For this tutorial, you don't need any filters.
2. To continue to Step 5: Review and create, choose **Next**.

###### To complete Step 5: Review and create

- Review the flow settings, then choose **Create flow**.

## Run a flow

You now have a flow. The source that you use determines how you run this flow.

Your event-triggered flow runs when a change occurs to a record that you've
set up to generate change event notifications. Here, you change a record within
your Salesforce account to activate a flow run.

###### To run an event-triggered flow with Salesforce

1. Open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. In **Flows**, select the `salesforce-to-s3` flow.
3. Choose **Activate flow**.
4. Open Salesforce at [www.salesforce.com](https://www.salesforce.com/ "https://www.salesforce.com/") and log in to your account.
5. Navigate to the page where Salesforce stores your records. For the
   sample data, this is the **Accounts**
   page.
6. Edit one of the records. For example, in the sample data, change the
   **Rating** in
   `Example3` from **cold** to
   **hot**.
   After about a minute, refresh your flow page in Amazon AppFlow. When the flow
   successfully runs, a timestamp from the last flow run appears.

![Timestamp showing last event-triggered flow run.](images/flow-timestamp.png)
Your on-demand flow runs when you choose the **Run flow**
button in the console.

###### To run an on-demand flow

1. In **Flows**, select your flow from the list.
2. Choose **Run flow**.
   When the flow successfully runs, a banner appears.

![Success message for flow run.](images/flow-success2.png)

## View transferred data

The data from your source now resides in your S3 bucket. From the S3 bucket, you can,
for example, consume the data from multiple AWS services for analysis. In this step,
you download and view the data on your computer.

###### To retrieve the transferred data

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In **Buckets**, choose your S3 bucket from the list.
3. In your S3 bucket, choose the `destination` folder. Then
   choose the flow folder, for example,
   `salesforce-to-s3`.
4. The folder contains one file. Select this file and choose **Download**.
5. Navigate to the file in your `Downloads` folder and rename
   it with a descriptive name.
6. Open the file to view the updated record.

You've now transferred data from Salesforce or the SaaS that you chose to Amazon S3. If
you used Salesforce, you set up an event-triggered flow to keep up-to-date with changing
data.
