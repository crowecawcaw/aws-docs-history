

# Step 5: Clean up your resources
<a name="flow-tutorial-clean-up"></a>

After you've completed the tutorial, it's good practice to clean up any resources that you no longer want to use. This way, your account doesn't incur any further charges.

**Topics**
+ [Clean up in Amazon S3](#flow-tutorial-clean-s3)
+ [Clean up in Amazon AppFlow](#flow-tutorial-clean-appflow)
+ [Clean up in Salesforce](#flow-tutorial-clean-salesforce)

## Clean up in Amazon S3
<a name="flow-tutorial-clean-s3"></a>

Because you used an S3 bucket as both a source and a destination throughout this tutorial, Amazon S3 hosted multiple files. Unless you delete these files, their storage continues to incur charges on your AWS account. Before you delete an S3 bucket, ensure you have saved any important files to another location.

**To clean up your S3 bucket**

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the **Buckets** section, select your S3 bucket and choose **Empty**. Follow the prompts to delete the contents of the bucket.

1. In the **Buckets** section, select your S3 bucket and choose **Delete**. Follow the prompts to delete the S3 bucket.
**Warning**  
Because S3 bucket names are globally unique, when you delete your S3 bucket, someone else can use its name. If you want to reserve an S3 bucket name, don't delete the bucket.

Now you have deleted all of the Amazon S3 resources that you created for the tutorial.

For more information on how to empty and delete S3 buckets, see the following resources:
+ [Emptying a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/empty-bucket.html) in the *Amazon S3 User Guide*.
+ [Deleting a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/delete-bucket.html) in the *Amazon S3 User Guide*.

## Clean up in Amazon AppFlow
<a name="flow-tutorial-clean-appflow"></a>

Amazon AppFlow stores both your connection and flows. To clean up all resources that you created in this tutorial, delete the two flows and your connection to the SaaS application.

**To clean up your flows**

1. Open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. In the **Flows** section, select a flow and choose **Delete**. Follow the prompts to delete your flow.

1. Perform the above step for any flows that remain.

**To clean up your connection**

1. Open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. In the **Connections** section, under **Connectors**, open the *Choose a connector* box. Select the connector that you used in the tutorial.

1. Select the connection and choose **Delete**.

1. If you used more than one connector, repeat steps 2 and 3 for all connectors.

Now you have deleted all of the resources that you created within Amazon AppFlow for the tutorial.

## Clean up in Salesforce
<a name="flow-tutorial-clean-salesforce"></a>

If you used Salesforce for this tutorial and uploaded the sample data from an S3 bucket to Salesforce, you might want to delete the sample account records.

**To delete imported records in Salesforce**
+ Follow the directions in [Mass delete records](https://help.salesforce.com/s/articleView?id=sf.admin_massdelete.htm).

After you complete these steps, you have cleaned up all of the resources that you created in this tutorial. Deleted resources no longer incur charges on your AWS account.