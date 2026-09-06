

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Configuring Service Catalog Integration
<a name="jsd-integration-configure-sc"></a>

After you create two IAM users with baseline permissions in each account, you can now configure Service Catalog. This section describes how to configure Service Catalog to have a portfolio that includes an Amazon S3 bucket product. Use the Amazon S3 template in [Creating an Amazon S3 Bucket for Website Hosting](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-s3.html#scenario-s3-bucket-website ) for your preliminary product. Copy and save the Amazon S3 template to your device.

**To configure Service Catalog**

1. Follow the steps in [Step 3: Create an AWS Service Catalog Portfolio](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/getstarted-portfolio.html) to create a portfolio.

1. To add the Amazon S3 bucket product to the portfolio you just created, enter the product details in the Service Catalog console on the **Upload new product** page.

1. For **Select template**, choose the Amazon S3 bucket CloudFormation template you saved to your device.

1. Set **Constraint type** to **Launch** for the product that you just created with the **SCConnectLaunch** role in the baseline permissions. For additional launch constraint instructions, see [AWS Service Catalog Launch Constraints](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/constraints-launch.html).

**Note**  
The AWS configuration design requires each Service Catalog product to have either a launch or StackSet constraint. Failure to follow this step can result in an *Unable to Retrieve Parameter* message within Jira Service Management Service Catalog.

## Video: Integrate AWS products in your Jira Service Management portal
<a name="video-intro-jira"></a>

This video (11:22) describes how to integrate AWS products into your Jira Service Management portal. Jira Service Management enables end users to provision, manage, and operate AWS resources natively with Jira Service Management from Atlassian.

[![AWS Videos](http://img.youtube.com/vi/1AODGjhqufo/0.jpg)](http://www.youtube.com/watch?v=1AODGjhqufo)
