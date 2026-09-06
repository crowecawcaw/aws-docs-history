

# Upsolver
<a name="upsolver"></a>

The following are the requirements and connection instructions for using Upsolver with Amazon AppFlow.

**Note**  
You can use Upsolver as a destination only.

**Topics**
+ [Requirements](#upsolver-requirements)
+ [Setup instructions](#upsolver-setup)
+ [Notes](#upsolver-notes)
+ [Related resources](#upsolver-resources)

## Requirements
<a name="upsolver-requirements"></a>
+ You must create an Amazon AppFlow data source in the Upsolver user interface. This will create an S3 bucket in your AWS account where Amazon AppFlow will send data.
+ Alternatively, you can create an Amazon S3 bucket through the Amazon S3 console. The bucket name must begin with `upsolver-appflow`.

## Setup instructions
<a name="upsolver-setup"></a>

**To connect to Upsolver while creating a flow**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. Choose **Create flow**.

1. For **Flow details**, enter a name and description for the flow.

1. (Optional) To use a customer managed CMK instead of the default AWS managed CMK, choose **Data encryption**, **Customize encryption settings** and then choose an existing CMK or create a new one.

1. (Optional) To add a tag, choose **Tags**, **Add tag** and then enter the key name and value.

1. Choose **Next**.

1. Choose **Upsolver** from the **Destination name** dropdown list.

1. Under **Bucket details**, select the S3 bucket in which you will place your data. You can specify a prefix, which is equivalent to specifying a folder within the S3 bucket where your source files are located or records are to be written to the destination.  
![Destination name field showing Upsolver selected, and Bucket details section with S3 bucket dropdown and prefix input field.](http://docs.aws.amazon.com/appflow/latest/userguide/images/connection_setup-upsolver-console.png)

Now that you are connected to your Amazon S3 bucket, you can continue with the flow creation steps as described in [Creating flows in Amazon AppFlow](create-flow.md).

**Tip**  
If you aren’t connected successfully, ensure that you have followed the instructions in the [Requirements](#upsolver-requirements).

## Notes
<a name="upsolver-notes"></a>
+ You can configure Amazon AppFlow flows with Upsolver as the destination, and send data from any supported source to the integrated Upsolver Amazon S3 bucket. The data is then available for downstream processing in Upsolver.

## Related resources
<a name="upsolver-resources"></a>
+  [Amazon AppFlow data source](https://docs.upsolver.com/upsolver-1/connecting-data-sources/amazon-aws-data-sources/amazon-appflow-data-source) from the Upsolver documentation