

AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform).

# Step 1: Download the Strategy Recommendations collector
<a name="getting-started-dowmload-collector"></a>

Migration Hub Strategy Recommendations application data collector is a virtual appliance that you can install in your on-premises VMware environment. The Strategy Recommendations application data collector is also available as an Amazon Machine Image (AMI). If you want to use the AMI version of the collector to assess AWS applications or for some other reason, you don't need to download the collector. You can skip this section and go to [Deploy the Strategy Recommendations collector in an Amazon EC2 instance](getting-started-deploy.md#getting-started-deploy-ec2).

This section describes how to download the collector Open Virtualization Archive (OVA) file that you use to deploy the collector as a virtual machine (VM) in your VMware environment.

**To download the collector OVA file**

1. Using the AWS account that you created in [Setting up Strategy Recommendations](setting-up.md), sign in to the AWS Management Console and open the Migration Hub console at [https://console.aws.amazon.com/migrationhub/](https://console.aws.amazon.com/migrationhub/).

1. In the Migration Hub console navigation pane, choose **Strategy**.

1. On the **Migration Hub Strategy Recommendations** page, choose **Download data collector**.

1. Optionally, you can choose **Download the import template** if you want to import application data. For more information about importing data, see [Importing data into Strategy Recommendations](importing-data.md). 

1. Click on **Get recommendations** button and choose **Agree** to allow Migration Hub to create a service-linked role (SLR) in your account. When setting up Strategy Recommendations for the first time, you must create the SLR. For more information, see [Using service-linked roles for Strategy Recommendations](using-service-linked-roles.md).

## Next step
<a name="getting-started-dowmload-collector-next"></a>

 [Step 2: Deploy the Strategy Recommendations collector](getting-started-deploy.md) 