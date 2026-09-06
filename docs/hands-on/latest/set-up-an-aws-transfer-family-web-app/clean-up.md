

# Task 5: Clean up resources
<a name="clean-up"></a>


|  |  | 
| --- |--- |
| **Time to complete** | 5 minutes  | 

## Overview
<a name="overview"></a>

In this task, you will go through the steps to delete all the resources you created throughout this tutorial. It is a best practice to delete resources you are no longer using to avoid unwanted charges. 

## Implementation
<a name="implementation"></a>

### Clean up resources
<a name="primary-step"></a>

1. Delete the application

   Open the [AWS Transfer Family console](https://console.aws.amazon.com/transfer/home). In the left pane, choose **Web** **apps**. 

   Select **AWS Transfer Family web app demo** and choose **Actions.** 

   Choose **Delete**.   
![Interface element requiring manual review.](http://docs.aws.amazon.com/hands-on/latest/set-up-an-aws-transfer-family-web-app/images/transfer-family-clean-interface.png)

1. Confirm deletion

   Enter **delete** to confirm.   
![Interface element requiring manual review.](http://docs.aws.amazon.com/hands-on/latest/set-up-an-aws-transfer-family-web-app/images/transfer-family-clean-dab-interface.png)

1. Delete the S3 access grant

   Open the [Amazon S3 Access Grants console](https://console.aws.amazon.com/s3/access-grants). 

   Choose **View** **details** and choose **Delete**.   
![The navigation interface.](http://docs.aws.amazon.com/hands-on/latest/set-up-an-aws-transfer-family-web-app/images/transfer-family-clean-debf-ebbfb.png)

1. Deregister the S3 access grant

   In the **Locations** tab, choose the **location** and select **Deregister**.   
![The navigation interface.](http://docs.aws.amazon.com/hands-on/latest/set-up-an-aws-transfer-family-web-app/images/transfer-family-clean-navigation-interface.png)

1. Delete the S3 bucket

   If you choose to delete the S3 bucket: 
   + Open the [Amazon S3 console](Amazon%20S3). 
   + Search for your bucket name (for example, **transfer-family-web-app-demo-1** in this tutorial). **Note: It will be different in your account since bucket names are globally unique.** 
   + Select the **bucket** and choose **Delete**. 
   + Enter the name of the bucket to confirm deletion of the bucket.   
![The navigation bar showing search for your bucket name (for example, transfer-family-web-app-demo-1 in this ...](http://docs.aws.amazon.com/hands-on/latest/set-up-an-aws-transfer-family-web-app/images/transfer-family-clean-navigation-bar.png)

## Congratulations\!
<a name="congratulations"></a>

You have set up an AWS Transfer Family web app to enable a simple interface for transferring data to and from Amazon S3 via a web browser. 