# Configuring SaaS product settings in AWS Marketplace

After you [create a software as a service (SaaS)
product](saas-create-product.md "saas-create-product.md") in AWS Marketplace, you can modify many of the product settings.
The following sections show you how to submit change requests and modify product settings, such as
updating pricing details, product visibility, and other settings.

###### Topics

- [Manage change requests](#create-change-request "#create-change-request")
- [Update product information](#update-product-information "#update-product-information")
- [Update architecture details](#updating-architecture-details "#updating-architecture-details")
- [Update the allowlist of AWS account IDs](#update-allowlist "#update-allowlist")
- [Update product visibility](#saas-update-visibility "#saas-update-visibility")
- [Update pricing terms](#saas-update-pricing-terms "#saas-update-pricing-terms")
- [Add pricing dimensions](#saas-add-pricing-dimensions "#saas-add-pricing-dimensions")
- [Update pricing dimensions](#saas-update-dimension "#saas-update-dimension")
- [Restrict pricing dimensions](#restrict-pricing-dimensions "#restrict-pricing-dimensions")
- [Determine how buyers will access your
  product](#configure-product-access "#configure-product-access")
- [Update availability by country](#saas-availability-by-country "#saas-availability-by-country")
- [Update the refund policy of a product](#update-refund-policy "#update-refund-policy")
- [Update the end user license agreement (EULA)](#saas-update-eula "#saas-update-eula")

## Manage change requests

In a [self-service listing](saas-create-product.md#saas-creating-self-service "saas-create-product.md#saas-creating-self-service"), you use a
_change request_ to make changes to your product.
Your current requests can be found on the AWS Marketplace Management Portal on the [**Requests** tab](https://aws.amazon.com/marketplace/management/requests "https://aws.amazon.com/marketplace/management/requests"). You can make new requests through
the **Request changes** dropdown list that is located under the
navigation bar.

###### To create a change request for a SaaS product

1. Open the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management "https://aws.amazon.com/marketplace/management"), and sign in to your seller account.
2. From the **Products** tab, select **SaaS**
   from the dropdown list.
3. After the request is submitted, it begins processing. The change request goes
   through the following statuses: **Under review**,
   **Preparing changes**, and **Applying
   changes**.
4. When the request's processing is completed, its status changes to one of the
   following values:
   - **Succeeded** – This status indicates that
     your requested change was processed and changes are reflected in the
     system.
   - **Failed** – This status indicates that
     something went wrong with the request and the changes were not
     processed. If the status is **Failed**, you can select
     the request to find **Error Codes** that provide
     recommendations on how to correct the issue. You can troubleshoot the
     errors and create a new request for the change. To make the process
     faster, you can use a **Copy to new request** function
     which copies the details of the **Failed** request. You
     can make needed changes and resubmit the request.

Change requests that start with an update will load the current details of the project.
Then, you can make updates, which overwrite the existing details. Add and restrict request
pairs are specifically for updates that are provisioned after each request succeeds (after
you choose **Save and exit** and **Submit** actions in the
self-service experience). This means existing subscribers can continue to use the product
until their subscription or contract ends. However, no new subscribers can be added to a
product that is in a **Restricted** status.

## Update product information

After you create your product, you might want to change the information associated
with it in AWS Marketplace.

1. Open the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management "https://aws.amazon.com/marketplace/management"), and sign in to your seller account.
2. From the [SaaS
   Products](https://aws.amazon.com/marketplace/management/products/saas "https://aws.amazon.com/marketplace/management/products/saas") page, on the **SaaS
   products** tab, select the product that you want to modify.
3. From the **Request changes** dropdown list, choose
   **Update product information**.
4. Update any of the following fields that you want to change:
   - **Product title**
   - **SKU**
   - **Short description**
   - **Long description**
   - **Product logo URL**
   - **Highlights**
   - **Product categories**
   - **Keywords**
   - **Product video URL**
   - **Resources**
   - **Support information**

   ###### Note

   For details about the logo format, see [Company and product logo requirements](product-submission.md#seller-and-product-logos "product-submission.md#seller-and-product-logos").

5. To update the product information, choose **Submit**.
6. Verify that the request appears on the **Requests** tab with
   the **Under review** status. You might need to refresh the page
   to see your new request.

## Update architecture details

To receive the special designation that your product is deployed on AWS,
update your product's architecture details in the AWS Marketplace Management Portal (AMMP)
by selecting a hosting pattern and uploading an architecture diagram.
For list of hosting patterns that AWS considers deployed on AWS, see [Guidelines](saas-guidelines.md#march-saas-guidelines "saas-guidelines.md#march-saas-guidelines").

###### To update architecture details

1. Sign into the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management "https://aws.amazon.com/marketplace/management").
2. On the **Products** menu, choose **SaaS**.
3. In the **SaaS products** table, choose your product.
4. For **Request changes**, choose **Update architecture details**.
5. Choose a hosting pattern. If you select a hosting pattern that AWS Marketplace considers deployed on AWS, complete the following two additional steps. For more information about patterns considered deployed on AWS, see [Guidelines](saas-guidelines.md#march-saas-guidelines "saas-guidelines.md#march-saas-guidelines"), previously in this guide.
   1. If prompted, in the **Architecture diagram** section, choose **Choose file** to upload your architecture diagram in PNG or JPG format. For more information about diagrams, see [Creating architecture diagrams](saas-guidelines.md#arch-diagram "saas-guidelines.md#arch-diagram").
   2. If prompted, in the **Application plane**, choose where your application runs. For more information, see [Control plane vs. application plane](../../../whitepapers/latest/saas-architecture-fundamentals/control-plane-vs.md "../../../whitepapers/latest/saas-architecture-fundamentals/control-plane-vs.md").

6. Choose **Update architecuture details**.

Once the request completes, **Request status** changes to **Succeeded**. To check request status, choose your product in the **SaaS products** table and choose the **Request log** tab.

To view your assessment results, choose your product in the **SaaS products** table and choose the **Architecture details** tab.

## Update the allowlist of AWS account IDs

You can change the list of AWS account IDs that can view your product in a limited
state.

1. Open the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management "https://aws.amazon.com/marketplace/management"), and sign in to your seller account.
2. From the [SaaS
   products](https://aws.amazon.com/marketplace/management/products/saas "https://aws.amazon.com/marketplace/management/products/saas") page, on the **SaaS
   products** tab, select the product that you want to modify.
3. From the **Request changes** dropdown list, select
   **Update allowlist**. A list shows the AWS account IDs
   that are currently allowlisted.
4. In the **Allowlisted AWS accounts** field, enter the
   AWS account IDs and separate them using a comma.
5. To update the allowlist of AWS account IDs, choose
   **Submit**.

## Update product visibility

To change which buyers can view your Quick Launch experience in AWS Marketplace, you can use
**Update visibility**.

1. Open the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management "https://aws.amazon.com/marketplace/management"), and sign in to your seller account.
2. From the [SaaS
   products](https://console.aws.amazon.com/marketplace/latest/userguide/saas-guidelines.html "https://console.aws.amazon.com/marketplace/latest/userguide/saas-guidelines.html") page, select the product that you want to
   modify.
3. From the **Request changes** dropdown, choose
   **Update visibility**.

###### Note

You can request that the product be moved from a
**Limited** status to a **Public**
status by using this change request. However, the change request must go
through an AWS Marketplace Seller Operations team approval process to be moved to
**Public**. 4. When you publish to public, you'll provide the actual price for your product.
This price will be applied after your listing is approved for public
visibility. 5. To submit your request for review, choose **Submit**. 6. Verify that the **Requests** tab shows the **Request
status** as **Under review**. When the request
completes, the status becomes **Succeeded**.

## Update pricing terms

To change the pricing per dimension on your SaaS product, use **Update pricing
terms**.

###### Note

A pricing increase for any dimension results in the pricing update option being
unavailable for at least the next 90 days. If updating both a price decrease and an
increase, update the price decrease first.

1. Open the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management "https://aws.amazon.com/marketplace/management")
   and sign in to your seller account.
2. From the [SaaS
   Products](https://aws.amazon.com/marketplace/management/products/saas "https://aws.amazon.com/marketplace/management/products/saas") page, on the **SaaS
   products** tab, select the product that you want to modify.
3. From the **Request changes** dropdown list, select
   **Update public offers**, and then select **Update
   pricing terms**.
4. Current pricing is pre-filled in the fields. You can delete the current price,
   and then add your new price.
5. To submit your request for review, choose **Submit**.
6. Verify that the **Requests** tab shows the **Request
   status** as **Under review**. When the request
   completes, the status will update to **Succeeded** or
   **Failed**.

## Add pricing dimensions

You can add a dimension that you want to use to charge your product. A dimension is
the foundational unit of measure that your buyer is charged for when using your
product.

###### Note

To update the name or description of an existing pricing dimension, see [Update pricing dimensions](#saas-update-dimension "#saas-update-dimension").

1. Open the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management "https://aws.amazon.com/marketplace/management"), and sign in to your seller account.
2. From the [SaaS
   Products](https://aws.amazon.com/marketplace/management/products/saas "https://aws.amazon.com/marketplace/management/products/saas") tab, select the product that you want to
   modify.
3. From the **Request changes** dropdown, choose
   **Update pricing dimensions** and then **Add
   pricing dimensions**.
4. Provide a dimension API identifier, display name, and description to add a new
   dimension to your product, and then choose **Next**.

###### Note

The API identifier and name must be unique across all dimensions. You
can't change the API identifier and unit after the dimension is
created. 5. Define the prices for each dimension you've added, and then choose
**Next** to review your changes.

###### Note

You can only add dimensions for the pricing model selected for your
product (for example, contract, usage, or contract with consumption). For
limited products, the prices for the newly added dimensions are set to
$0.01. You can update the prices when the product is ready for public
visibility. 6. Choose **Submit** to submit your request for review. 7. In the **Requests** tab, verify that the request status is
**Under review**. When the request is complete, the status
changes to **Succeeded**.

## Update pricing dimensions

You can update a dimension that you want to use to charge your product. A dimension is
the foundational unit of measure that your buyer is charged for when using your
product.

1. Open the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management "https://aws.amazon.com/marketplace/management"), and sign in to your seller account.
2. From the [SaaS
   Products](https://aws.amazon.com/marketplace/management/products/saas "https://aws.amazon.com/marketplace/management/products/saas") tab, select the product that you want to
   modify.
3. From the **Request changes** dropdown, choose
   **Update pricing dimensions** and then **Update
   dimension information**.
4. Find the dimension you want to update, and then choose the name or
   description.
5. Provide the new name or description, and then choose the
   **checkmark** to confirm your update. The dimension name must be unique.
6. Choose **Submit** to submit your request for review.
7. In the **Requests** tab, verify that the request status is
   **Under review**. When the request is complete, the status
   will change to **Succeeded**.

## Restrict pricing dimensions

You can restrict a dimension that is currently listed in the product. This request
removes the selected dimension from the product.

1. Open the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management "https://aws.amazon.com/marketplace/management"), and sign in to your seller account.
2. From the [SaaS
   Products](https://aws.amazon.com/marketplace/management/products/saas "https://aws.amazon.com/marketplace/management/products/saas") tab, select the product that you want to
   modify.
3. From the **Request changes** dropdown, choose
   **Update pricing dimensions** and then **Restrict
   pricing dimensions**.
4. For limited and public products, you'll be prompted to contact the AWS Marketplace
   Seller Operations team using the **[Contact
   Us](https://aws.amazon.com/marketplace/management/contact-us/ "https://aws.amazon.com/marketplace/management/contact-us/")** button. Using the form, provide details for the
   dimensions you want to remove from your product listing.

###### Note

Operations may not always be able to restrict pricing dimensions.

## Determine how buyers will access your

product

You can choose one of the following options for how customers can access your
product:

- [Update the SaaS URL fulfillment
  option](#update-fulfillment-options "#update-fulfillment-options") – Customers use a URL for
  the site that they are redirected to after subscribing to your product in
  AWS Marketplace.
- [Configure Quick Launch](#saas-quick-launch "#saas-quick-launch") – Customers use a simplified
  process to configure and launch your product. You can complete this
  configuration for existing products with either Limited or Public
  visibility.

### Update the SaaS URL fulfillment

option

To update the URL that is used to fulfill your SaaS product, use the
**Update fulfillment options** tab.

1. Open the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management "https://aws.amazon.com/marketplace/management"), and sign in to your seller account.
2. From the [SaaS Products](https://aws.amazon.com/marketplace/management/products/saas "https://aws.amazon.com/marketplace/management/products/saas") page, on the **SaaS
   products** tab, choose the product that you want to
   modify.
3. From the **Request changes** dropdown list, choose
   **Update fulfillment options**, and then choose
   **Edit default fulfillment URL**.
4. In the **Fulfillment URL** field, enter the new URL for
   the SaaS product fulfillment option.
5. To submit your request for review, choose
   **Submit**.
6. Verify that the **Requests** tab shows the
   **Request status** as **Under
   review**. When the request completes, the status will update to
   **Succeeded** or **Failed**.

### Configure Quick Launch

SaaS products listed in AWS Marketplace often require AWS resources to be deployed in the
subscribing buyer's account (for example, IAM roles). Quick Launch allows you to
provide your buyers with guided, step-by-step instructions and resource deployment
using AWS CloudFormation templates. Buyers use the CloudFormation templates to configure and launch
products. To learn more about the Quick Launch configuration process, see the [Enable SaaS Quick Launch](https://catalog.workshops.aws/mpseller/en-US/saas/quick-launch-integration "https://catalog.workshops.aws/mpseller/en-US/saas/quick-launch-integration") lab.

To configure a Quick Launch experience that customers can use to launch your SaaS
product, use the **Fulfillment options** tab.

1. From the [SaaS Products](https://aws.amazon.com/marketplace/management/products/saas "https://aws.amazon.com/marketplace/management/products/saas") page, on the **SaaS
   products** tab, select the product that you want to
   modify.

###### Note

To configure the Quick Launch experience, the product must have either
Limited or Public visibility. 2. On the product detail page, choose the **Fulfillment
options** tab. 3. For **Quick Launch**, choose the **Activate and
configure** button. 4. For **Account login details**, provide a URL for your
site where the buyer can log in or create an account. This URL opens a new
tab in the buyer experience. Buyers then sign in or create an account and
return to AWS Marketplace to launch the template. 5. Create an AWS CloudFormation template.

###### Tip

Follow the AWS Well-Architected Framework when creating your AWS
CloudFormation template that deploys resources into the buyer's AWS
account. For more information and resources, [AWS
Well-Architected](https://aws.amazon.com/architecture/well-architected/ "https://aws.amazon.com/architecture/well-architected/") and read the [AWS
Well-Architected Framework](../../../wellarchitected/latest/framework/welcome.md "../../../wellarchitected/latest/framework/welcome.md").

For **AWS CloudFormation template**, choose the **Add AWS CloudFormation
template** button and provide the following information:

    * **Title**
     – Enter the name of your CloudFormation deployment.
    * **Description** – Enter a description of
     the template.
    * **Stack name** – Enter a name for the
     stack. This name is the stack name for the buyer in
     CloudFormation.
    * **CloudFormation template URL** – Provide the
     Amazon Simple Storage Service (Amazon S3) URL for the template. AWS will review this
     template.


    ###### Note

    To simplify the launch process for your customers, we suggest
     minimizing the number of templates that are associated with your
     configuration process. Ideally, you want one template that
     deploys the resources needed to use the product. For questions
     related to your CloudFormation template, contact your AWS Marketplace business
     development partner or the [AWS Marketplace Seller Operations](https://aws.amazon.com/marketplace/management/contact-us/ "https://aws.amazon.com/marketplace/management/contact-us/") team.
    * **Required IAM permissions** – Provide
     the permissions that are required to deploy the CloudFormation template.
     If you want to share deployment parameters, which are stored as
     secrets in [AWS Secrets Manager](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md") for the buyer, your policy must include the
     following actions:




    	+ `secretsManager:ListSecrets`
    	+ `secretsManager:DescribeSecret`
    	+ `secretsManager:ReplicateSecretToRegions`
    	+ `secretsManager:GetSecretValue`
    ###### Note

    If your product requires seller-provided CloudFormation deployment
     parameters, such as API keys and [external IDs](../../../IAM/latest/UserGuide/id_roles_create_for-user_externalid.md "../../../IAM/latest/UserGuide/id_roles_create_for-user_externalid.md"), use the
     `PutDeploymentParameter` operation to share the
     parameter with your customers. For more information, see [PutDeploymentParameter](../../../marketplace-deployment/latest/api-reference/API_PutDeploymentParameter.md "../../../marketplace-deployment/latest/api-reference/API_PutDeploymentParameter.md") in the
     *AWS Marketplace Deployment Service API
     Reference*.

6. (Optional) For **Manual configuration instructions**,
   provide instructions for buyers who want to configure your product manually.
   Consider including links to your product's onboarding guide and
   documentation.
7. For **Launch details**, provide the URL where buyers will
   access the product after the CloudFormation stack has been deployed.
8. (Optional) For **Allowlisted accounts for Quick Launch**,
   provide a comma-separated list of AWS accounts that can view the Quick
   Launch experience with **Limited** visibility.
9. Choose **Submit**. By default, the Quick Launch
   experience has **Limited** visibility. Only your account
   and any allowlisted accounts can view the page. You can use the
   **Configure and launch** page to test your
   configuration. To do that, you must first subscribe to your product and
   choose the **Set up your account** button.
10. When you're ready, you can publish the Quick Launch experience in the
    AWS Marketplace catalog. Use the **Update Quick Launch visibility**
    button on the **Fulfillment options** tab on the product
    detail page.

When you change the visibility to **Public**, the AWS Marketplace
Seller Operations team reviews the configuration, conducts buyer testing,
and publishes the experience.

###### Note

If you need support as you enable the Quick Launch experience, contact
the [AWS Marketplace Seller Operations](https://aws.amazon.com/marketplace/management/contact-us/ "https://aws.amazon.com/marketplace/management/contact-us/") team.

## Update availability by country

You can define the countries in which your product can be offered.

1. Open the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management "https://aws.amazon.com/marketplace/management"), and sign in to your seller account.
2. From the [SaaS
   Products](https://aws.amazon.com/marketplace/management/products/saas "https://aws.amazon.com/marketplace/management/products/saas") tab, select the product that you want to
   modify.
3. From the **Request changes** dropdown, select
   **Update public offer** and then choose **Update
   availability by country**.
4. Choose one of the following options:
   - All countries – Available in all supported countries.
   - All countries with exclusions – Available in all supported countries
     except in selected countries.
   - Allowlisted countries only – Specific list of countries where the
     product is available.

5. Choose **Submit** to submit your request for review.
6. In the **Requests** tab, verify that the request status is
   **Under review**. When the request is complete, the status
   will change to **Succeeded**.

## Update the refund policy of a product

You can update the refund policy for your product by using **Update refund
policy**.

1. Open the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management "https://aws.amazon.com/marketplace/management"), and sign in to your seller account.
2. From the [SaaS
   Products](https://aws.amazon.com/marketplace/management/products/saas "https://aws.amazon.com/marketplace/management/products/saas") page, on the **SaaS
   products** tab, select the product that you want to modify.
3. From the **Request changes** dropdown list, select
   **Update public offer**, and then select **Update
   refund policy**.
4. The current refund policy details are provided in the text box. Review and
   modify the details as you want. Submitting the request overwrites the current
   refund policy.
5. To submit your request for review, choose **Submit**.
6. Verify that the **Requests** tab shows the **Request
   status** as **Under review**. When the request
   completes, the status will update to **Succeeded** or
   **Failed**.

## Update the end user license agreement (EULA)

You can update your EULA for new users subscribing to your product.

1. Open the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management "https://aws.amazon.com/marketplace/management"), and sign in to your seller account.
2. From the [SaaS
   Products](https://aws.amazon.com/marketplace/management/products/saas "https://aws.amazon.com/marketplace/management/products/saas") tab, select the product that you want to
   modify.
3. From the **Request changes** dropdown, choose
   **Update public offer** and then **Update
   EULA**.
4. You can choose the [Standard
   Contract for AWS Marketplace (SCMP)](standardized-license-terms.md "standardized-license-terms.md") or submit a custom EULA. For a
   custom EULA, you must provide an Amazon Simple Storage Service (Amazon S3) URL for the
   contract. Your Amazon S3 bucket must be publicly accessible.
5. Choose **Submit** to submit your request for review.
6. In the **Requests** tab, verify that the request status is
   **Under review**. When the request is complete, the status
   will change to **Succeeded**.
