# Configuring Service Catalog

Integration

After you create two IAM users with baseline permissions in each
account, you can now configure Service Catalog. This section describes how to
configure Service Catalog to have a portfolio that includes an Amazon S3 bucket product.
Use the Amazon S3 template in [Creating an Amazon S3 Bucket for Website Hosting](../../../AWSCloudFormation/latest/UserGuide/quickref-s3.md#scenario-s3-bucket-website "../../../AWSCloudFormation/latest/UserGuide/quickref-s3.md#scenario-s3-bucket-website") for your
preliminary product. Copy and save the Amazon S3 template to your
device.

###### To configure Service Catalog

1. Follow the steps in [Step 3: Create an AWS Service Catalog Portfolio](../../../servicecatalog/latest/adminguide/getstarted-portfolio.md "../../../servicecatalog/latest/adminguide/getstarted-portfolio.md") to create a
   portfolio.
2. To add the Amazon S3 bucket product to the portfolio you just created,
   enter the product details in the Service Catalog console on the **Upload
   new product** page.
3. For **Select template**, choose the Amazon S3 bucket
   CloudFormation template you saved to your device.
4. Set **Constraint type** to
   **Launch** for the product that you just created
   with the **SCConnectLaunch** role in the
   baseline permissions. For additional launch constraint instructions,
   see [AWS Service Catalog Launch Constraints](../../../servicecatalog/latest/adminguide/constraints-launch.md "../../../servicecatalog/latest/adminguide/constraints-launch.md").

###### Note

The AWS configuration design requires each Service Catalog product to have
either a launch or StackSet constraint. Failure to follow this step can
result in an _Unable to Retrieve Parameter_ message
within Jira Service Management Service Catalog.

## Video: Integrate AWS products in your Jira Service Management

portal

This video (11:22) describes how to integrate AWS products into
your Jira Service Management portal. Jira Service Management enables end
users to provision, manage, and operate AWS resources natively with
Jira Service Management from Atlassian.
