

**AWS Mainframe Modernization self-managed experience** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization self-managed experience, explore capabilities from vendor-direct offerings and from AWS Transform. Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

**AWS Mainframe Modernization Service (Managed Runtime Environment experience)** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

# AWS Mainframe Modernization replatforming with NTT DATA
<a name="unikix"></a>

AWS Mainframe Modernization offers a variety of Amazon Machine Images (AMIs). These AMIs facilitate the rapid provisioning of Amazon EC2 instances, creating a tailored environment for rehosting and replatforming mainframe applications in AWS by using NTT Data. This guide provides the steps required to access and use these AMIs. 

## Prerequisites
<a name="prereqs-unikix"></a>
+ Ensure that you have administrator access to an AWS account where you can create Amazon EC2 instances.
+ Verify that the AWS Mainframe Modernization service is available in the Region where you plan to create the Amazon EC2 instances. See [List of AWS Services Available by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).
+ Identify the Amazon VPC where you want to create the Amazon EC2 instances.

## Subscribe to the Amazon Machine Image
<a name="subscribe-to-images-unikix"></a>

When you subscribe to an AWS Marketplace product, you can launch an instance from the product's AMI.

1. Sign in to the AWS Management Console and open the AWS Marketplace console at [https://console.aws.amazon.com/marketplace](https://console.aws.amazon.com/marketplace).

1. Choose **Manage subscriptions**.

1. Copy and paste the following link into the browser address bar: [https://aws.amazon.com/marketplace/pp/prodview-eg227ymldsnx2](https://aws.amazon.com/marketplace/pp/prodview-eg227ymldsnx2)

1. Choose **Continue to Subscribe**.

1. If the terms and conditions are acceptable, choose **Accept Terms**. The subscription might take a few minutes to process.

1. Wait for a thank-you message to appear. This message confirms that you have successfully subscribed to the product.

1. In the left navigate pane, choose **Manage subscriptions**. This view shows you all of your subscriptions.

## Launch AWS Mainframe Modernization replatform with NTT DATA instance
<a name="launch-data-replatform-unikix"></a>

1. Open the AWS Marketplace console at [https://console.aws.amazon.com/marketplace](https://console.aws.amazon.com/marketplace).

1. In the left navigation pane, choose **Manage subscriptions**.

1. Find the AMI that you want to launch, and choose **Launch new instance**.

1. Under **Region**, select the allow-listed Region.

1. Choose **Continue to launch through EC2**. This action takes you to the Amazon EC2 console.

1. Enter a name for the server.

1. Select an instance type that matches your project performance and cost requirements. The suggested starting point for instance size is `c5.2xLarge`.

1. Choose an existing key pair or create and save a new one. For information about key pairs, see [Amazon EC2 key pairs and Linux instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html) in the Amazon EC2 User Guide.

1. Edit the network settings and choose the allow-listed VPC and appropriate subnet.

1. Choose an existing security group or create a new one. If this is an Enterprise Server Amazon EC2 instance it is typical to allow TCP traffic to ports 86 and 10086 to administer the Rocket Software (formerly Micro Focus) configuration.

1. Configure the storage for the Amazon EC2 instance.

1. Review the summary and choose **Launch instance**. For the launch to success, the instance type must be valid. If the launch fails, choose **Edit instance configuration** and choose a different instance type.

1. After you see the success message, choose **Connect to instance**.

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the left navigation pane, under the **Instances** menu, choose **Instances**.

1. In the main pane, check the status of your instance.

## Getting started with NTT Data
<a name="unikix-getting-started"></a>

After you provision the Amazon EC2 instance, SSH into it with the user name `ec2-user`. The screen will look like the following image.

![SSH screen with provided Amazon EC2 instance and user name.](http://docs.aws.amazon.com/m2/latest/userguide/images/unikix-start-screen.png)


Under the `/opt/software/` folder, there is a folder named `UniKix_Product_Guides`, as shown in the following image.

![SSH screen with details of /opt/software/ folder. Spot the folder UniKix_Product_Guides.](http://docs.aws.amazon.com/m2/latest/userguide/images/unikix-product-guides.png)


The `UniKix_Product_Guides` folder includes the documentation for the following components that are installed on this Amazon EC2 instance:
+ NTT DATA TPE
+ NTT DATA BPE
+ NTT DATA Enterprise COBOL
+ NTT DATA UniKix Secure
+ NTT DATA UniKix Central Manager

The `software` folder that appears in the previous image has the binaries for the components that are listed above.

After you successfully validate the Amazon EC2 instance, get started using AWS Mainframe Modernization Replatform with NTT DATA by following the NTT Data documentation.