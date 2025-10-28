# Using Quick Launch with SaaS and container products

Quick Launch is a deployment option that the seller can choose when configuring SaaS and container products on AWS Marketplace. Quick Launch provides buyers with guided, step-by-step instructions and resource deployment using AWS CloudFormation templates. Buyers use the CloudFormation templates to configure and launch products.

###### Topics

- [Launching SaaS products with Quick Launch](#saas-quick-launch "#saas-quick-launch")
- [Launching container products with Quick Launch](#buyer-launch-container-quicklaunch "#buyer-launch-container-quicklaunch")

## Launching SaaS products with Quick Launch

Quick Launch is an AWS Marketplace deployment option that's available for SaaS products that have
Quick Launch enabled. It reduces the time, resources, and steps required to configure, deploy,
and launch your software. For products that offer this feature, you can either choose to use
Quick Launch or manually configure your resources.

###### To find, subscribe, and launch a SaaS product using the Quick Launch experience

1. Navigate to the [AWS Marketplace search
   page](https://aws.amazon.com/marketplace/search/? "https://aws.amazon.com/marketplace/search/?").
2. Browse AWS Marketplace, and find the product that contains the software that you want to launch.
   Products that provide the Quick Launch experience have a **Quick Launch**
   badge in their product description.

###### Tip

To find products with the Quick Launch experience enabled, use the
**SaaS** and **CloudFormation template** filters in
the **Refine results** pane. 3. After you subscribe to the product, navigate to the **Configure and
launch** page by choosing the **Set Up Your Account**
button. 4. On the **Configure and launch** page in **Step 1: Make sure
you have required AWS permissions**, make sure that you have the permissions
necessary to use the Quick Launch experience. To request the permissions, contact your
AWS administrator.

To use the full Quick Launch experience, you must have the following
permissions:

    * `CreateServiceLinkedRole` — Allows AWS Marketplace to create the
     `AWSServiceRoleForMarketplaceDeployment` service-linked role. This
     service-linked role allows AWS Marketplace to manage deployment-related parameters, which are
     stored as secrets in AWS Secrets Manager, on your behalf.
    * `DescribeSecrets` — Allows AWS Marketplace to obtain information about
     deployment parameters passed by sellers.
    * `GetRole` — Allows AWS Marketplace to determine if the service-linked role
     has been created in the account.
    * `ListSecrets` — Allows AWS Marketplace to obtain the status of the
     deployment parameters.
    * `ListRegions` — Allows AWS Marketplace to obtain AWS Regions that are
     opted in for the current account.
    * `ReplicateSecrets` — Allows AWS Marketplace to start the replication of
     secrets to the selected Region where you will deploy the software.

5. For **Step 2: Log into an existing or new vendor account**, choose
   the **Log in or create an account** button. The seller's site opens in a
   new tab, where you can either log in or create a new account. When you're done, return to
   the **Configure and launch** page.
6. For **Step 3: Configure your software and AWS integration**, choose
   how you want to configure the product:
   - Quick Launch — You can choose this streamlined experience to configure your
     product quickly.
   - Manual — Use the instructions provided by the seller to configure your
     software.

7. For **Step 4: Launch your software**, choose the **Launch
   software** button to launch your software.

## Launching container products with Quick Launch

If the seller has enabled Quick Launch on a fulfillment option, you can use it to create an Amazon EKS
cluster and deploy a container application to it. With Quick Launch, you will use AWS CloudFormation to configure
and create an Amazon EKS cluster and launch a container application on it. With Quick Launch, you can
launch a container application for testing purposes. To use Quick Launch, follow the steps in [Launching with a Helm fulfillment
option](buyer-launch-container-helm.md "buyer-launch-container-helm.md").

To create an Amazon EKS cluster that the application can be deployed on, create a CloudFormation
stack. A _stack_ is a collection of AWS resources that you
can manage as a single unit. All the resources in a stack are defined by the stack's
CloudFormation template. In Quick Launch, the stack's resources include the information required to create
the Amazon EKS cluster and launch the application. For more information about stacks in AWS CloudFormation, see
[Working
with stacks](../../../AWSCloudFormation/latest/UserGuide/stacks.md "../../../AWSCloudFormation/latest/UserGuide/stacks.md") in the _AWS CloudFormation User Guide_.

After the cluster is created, Quick Launch launches the application on it by installing the
seller-provided Helm chart onto the cluster. Quick Launch handles this for you as part of the stack
creation that also creates the Amazon EKS cluster.
