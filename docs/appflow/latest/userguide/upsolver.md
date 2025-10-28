# Upsolver

The following are the requirements and connection instructions for using Upsolver with
Amazon AppFlow.

###### Note

You can use Upsolver as a destination only.

###### Topics

- [Requirements](#upsolver-requirements "#upsolver-requirements")
- [Setup instructions](#upsolver-setup "#upsolver-setup")
- [Notes](#upsolver-notes "#upsolver-notes")
- [Related resources](#upsolver-resources "#upsolver-resources")

## Requirements

- You must create an Amazon AppFlow data source in the Upsolver user interface. This will create
  an S3 bucket in your AWS account where Amazon AppFlow will send data.
- Alternatively, you can create an Amazon S3 bucket through the Amazon S3 console. The bucket name
  must begin with `upsolver-appflow`.

## Setup instructions

###### To connect to Upsolver while creating a flow

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. Choose **Create flow**.
3. For **Flow details**, enter a name and description for the flow.
4. (Optional) To use a customer managed CMK instead of the default AWS managed CMK, choose
   **Data encryption**, **Customize encryption settings** and
   then choose an existing CMK or create a new one.
5. (Optional) To add a tag, choose **Tags**, **Add tag**
   and then enter the key name and value.
6. Choose **Next**.
7. Choose **Upsolver** from the **Destination name**
   dropdown list.
8. Under **Bucket details**, select the S3 bucket in which you will place
   your data. You can specify a prefix, which is equivalent to specifying a folder within the S3
   bucket where your source files are located or records are to be written to the
   destination.

![Destination name field showing Upsolver selected, with bucket details section below.](images/connection_setup-upsolver-console.png)

Now that you are connected to your Amazon S3 bucket, you can continue with the flow creation
steps as described in [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

###### Tip

If you aren’t connected successfully, ensure that you have followed the instructions in the
[Requirements](#upsolver-requirements "#upsolver-requirements").

## Notes

- You can configure Amazon AppFlow flows with Upsolver as the destination, and send data from
  any supported source to the integrated Upsolver Amazon S3 bucket. The data is then available for
  downstream processing in Upsolver.

## Related resources

- [Amazon AppFlow data source](https://docs.upsolver.com/upsolver-1/connecting-data-sources/amazon-aws-data-sources/amazon-appflow-data-source "https://docs.upsolver.com/upsolver-1/connecting-data-sources/amazon-aws-data-sources/amazon-appflow-data-source") from the Upsolver documentation
