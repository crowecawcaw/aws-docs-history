

# Using Quick Launch with SaaS products
<a name="quick-launch"></a>

Quick Launch is a deployment option that the seller can choose when configuring SaaS products on AWS Marketplace. Quick Launch provides buyers with guided, step-by-step instructions and resource deployment using AWS CloudFormation templates. Buyers use the CloudFormation templates to configure and launch products.

**Topics**
+ [Launching SaaS products with Quick Launch](#saas-quick-launch)

## Launching SaaS products with Quick Launch
<a name="saas-quick-launch"></a>

Quick Launch is an AWS Marketplace deployment option that's available for SaaS products that have Quick Launch enabled. It reduces the time, resources, and steps required to configure, deploy, and launch your software. For products that offer this feature, you can either choose to use Quick Launch or manually configure your resources.

**To find, subscribe, and launch a SaaS product using the Quick Launch experience**

1. Navigate to the [AWS Marketplace search page](https://aws.amazon.com/marketplace/search/?).

1. Browse AWS Marketplace, and find the product that contains the software that you want to launch. Products that provide the Quick Launch experience have a **Quick Launch** badge in their product description.
**Tip**  
To find products with the Quick Launch experience enabled, use the **SaaS** and **CloudFormation template** filters in the **Refine results** pane.

1. After you subscribe to the product, navigate to the **Configure and launch** page by choosing the **Set Up Your Account** button.

1. On the **Configure and launch** page in **Step 1: Make sure you have required AWS permissions**, make sure that you have the permissions necessary to use the Quick Launch experience. To request the permissions, contact your AWS administrator.

   To use the full Quick Launch experience, you must have the following permissions:
   + `CreateServiceLinkedRole` — Allows AWS Marketplace to create the `AWSServiceRoleForMarketplaceDeployment` service-linked role. This service-linked role allows AWS Marketplace to manage deployment-related parameters, which are stored as secrets in AWS Secrets Manager, on your behalf.
   + `DescribeSecrets` — Allows AWS Marketplace to obtain information about deployment parameters passed by sellers.
   + `GetRole` — Allows AWS Marketplace to determine if the service-linked role has been created in the account.
   + `ListSecrets` — Allows AWS Marketplace to obtain the status of the deployment parameters.
   + `ListRegions` — Allows AWS Marketplace to obtain AWS Regions that are opted in for the current account.
   + `ReplicateSecrets` — Allows AWS Marketplace to start the replication of secrets to the selected Region where you will deploy the software.

1. For **Step 2: Log into an existing or new vendor account**, choose the **Log in or create an account** button. The seller's site opens in a new tab, where you can either log in or create a new account. When you're done, return to the **Configure and launch** page.

1. For **Step 3: Configure your software and AWS integration**, choose how you want to configure the product:
   + Quick Launch — You can choose this streamlined experience to configure your product quickly. 
   + Manual — Use the instructions provided by the seller to configure your software.

1. For **Step 4: Launch your software**, choose the **Launch software** button to launch your software.