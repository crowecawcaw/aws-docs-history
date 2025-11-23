# Creating AMI-based products

The Amazon Machine Image (AMI) self-service experience guides you as you create your product listing and make
change requests. By using the self-service experience, you can update your product listing
directly with less time needed for processing by the AWS Marketplace Seller Operations team. Many steps of the
self-service experience align with the catalog system in AWS Marketplace, which facilitates direct
validation instead of waiting for processing and validation from the AWS Marketplace Seller Operations team. This topic
explains how to use the AMI self-service experience to create a product listing
for a single AMI. Customers use AMIs to create Amazon EC2 instances with
your product already installed and configured.

###### Topics

- [Prerequisites](#single-ami-prerequisites "#single-ami-prerequisites")
- [Understand the self-service
  experience](#understand-ami-self-service-exp "#understand-ami-self-service-exp")
- [Create the listing](#ami-create-product "#ami-create-product")
- [Additional resources](#ami-single-create-resources "#ami-single-create-resources")

## Prerequisites

Before you create an AMI product listing, you must complete the following
prerequisites:

1. Have access to the AWS Marketplace Management Portal. This is the tool that you use to register as a
   seller and manage the products that you sell on AWS Marketplace. To learn more about
   getting access to the AWS Marketplace Management Portal, see [Policies and permissions for AWS Marketplace
   sellers](detailed-management-portal-permissions.md "detailed-management-portal-permissions.md").
2. Register as a seller and, if you want to charge for your products, submit your
   tax and banking information. To learn more about becoming a seller, see [Getting started as an AWS Marketplace seller](user-guide-for-sellers.md "user-guide-for-sellers.md").
3. Have a product that you want to sell. For AMI-based products, this typically
   means you have created or modified your server software, and created an AMI for
   your customers to use. To learn more about preparing an AMI for use in AWS Marketplace,
   see [Best practices for building AMIs for use with AWS Marketplace](best-practices-for-building-your-amis.md "best-practices-for-building-your-amis.md").

## Understand the self-service

experience

The self-service experience guides you through creating your product on AWS Marketplace. As you
proceed through the steps, you specify product information and AMI deployment settings,
such as AWS Region, instance types, and AMI details. You also configure transaction
details including the pricing, country availability, EULA, and refund policy. As an
option, you can specify an allowlist of AWS account IDs to access and test the product
while it is in the **Limited** status.

Before you start, review the following key aspects of the self-service experience:

- You can only go to the next step after you complete the required fields in the
  current step. This requirement is because there is page-level validation at the
  end of each step. You can't save or submit an incomplete step.
- If you need to end your session before completing all the steps in the
  process, you can choose **Save and exit** to submit the steps
  that you completed to the staging area.
- A step that is incomplete and doesn't pass validation isn't submitted to the
  system. A partially completed step isn't valid and can't be saved.
- When you choose **Save and exit**, the **Save and
  exit** dialog box shows the steps that passed validation checks.
  You can review and choose to save up to the last completed and validated steps.
  If there is a validation error or missing details, you can choose **Fix
  it** to go back to that step.
- After you **Save and exit**, the request is under review
  while it's processing. It could take a few minutes or hours to finish
  processing. You can't continue the steps or make changes until the request has
  succeeded. For the first **Save and exit**, the request is
  creating the product in parallel with the steps that you have completed.
  - After the request has **Succeeded**, you
    have completed the save. To resume changes on the **Product
    overview** page, choose **Resume product
    creation** or use **Request changes** to
    update the details you have previously submitted in the last session.
    When you resume, notice that the steps you have completed are marked
    with a green **Succeeded** label. To update a
    previously submitted step, use **Request changes**. The
    previous **Save and exit** request must be completed
    before you can continue this step.

- When you’ve completed all the steps, you can choose **Next**
  to see a review. Choose **Submit** which requests that the
  system perform a final validation. After you receive a **Succeeded** response, the product moves to a
  **Limited** status. You can see on the detail page that the
  product is now available to anyone on the allowlist. If the request fails, the
  product remains in the **Staging** status and requires you to
  make corrections before resubmitting.

## Create the listing

The steps in this section explain how to create a listing for a
single-AMI product.

###### Note

You can only go to the next step when you complete the required fields in the
current step. You can't save or submit an incomplete step. If you need to end your
session before completing all the steps in the process, choose **Save and
exit** to submit the steps that you completed to the staging area. For
more information, see [Understand the self-service
experience](#understand-ami-self-service-exp "#understand-ami-self-service-exp").

###### To create a single-AMI product

1. Open the AWS Marketplace Management Portal at [https://aws.amazon.com/marketplace/management/tour/](https://aws.amazon.com/marketplace/management/tour/ "https://aws.amazon.com/marketplace/management/tour/"), and then
   sign in to your seller account.
2. From the **Products** menu, choose
   **Server**. Or, you can go directly to the [**Server Products**](https://aws.amazon.com/marketplace/management/products/server "https://aws.amazon.com/marketplace/management/products/server") page.
3. From the **Server products** tab, select **Create
   server product**, select **Amazon Machine Image
   (AMI)**, and then select one of the licensing types for
   single-AMI products:
   - **Bring your own license (BYOL)** – A
     product that the user gets a license from you outside of AWS Marketplace. It
     can be either a paid or free license.
   - **Free** – A product that is free for your
     subscribers to use. (They will still pay charges for any associated
     Amazon Elastic Compute Cloud (Amazon EC2) instance, or other AWS resources.)
   - **Paid hourly or hourly-annual** – A
     product that the buyer pays for either on an hourly basis or hourly
     with an annual contract. AWS does the metering based on the
     product code on the AMI.
   - **Paid monthly** – A product that the
     buyer is billed for monthly by AWS.
   - **Paid usage** – Software is directly
     charged for the value you provide, along with one of four usage
     categories: users, data, bandwidth, or hosts. You can define up to
     24 dimensions for the product. All charges are still incurred by the
     customer.
   - **AMI with contract pricing** – A
     Single-AMI product or Single-AMI with an CloudFormation stack that the buyer
     pays an upfront fee for.

4. The self-service experience guides you through the steps to create an
   AWS Marketplace listing. You must enter product information (metadata), product
   deployment details (AWS Region, instances, and AMI details), and public
   offer details (price, EULA, availability by country, EULA, refund). As an
   option, you can add accounts to the allowlist to test the product. Complete
   each step to move to the next step in the process.

###### Note

If you need to end your session before completing all steps in the
process, you can use the **Save and exit** function to
submit the steps you completed to the staging area. This creates a
request for the information you provided to be validated. While the
request is processing, you can't edit the product. After the request
succeeds, you can continue creating your product by choosing
**Resume product creation**.

A failed request means no update was made to the product because of a
validation error. This will be visible on the request log for your
product. You can select the request to view the error, use
**Copy to new** under **Actions**
to correct the error, and resubmit the request. When you resume the
steps, you can continue from the step after the step that you saved in
the last session. To update previous steps, go to the product overview
page and submit a change request to update steps that you submitted
previously. 5. After entering required information for all of the change request steps,
choose **Submit**. This submittal creates a request to the
AWS Marketplace catalog system to validate the information and release the product to
a **Limited** state, if the validation passes. While the
request is processing, you can't continue to edit the product. After the
request succeeds, the product is moved to a **Limited**
state.

    * When your product is initially published, it's only accessible to
     your AWS account (the one you used to create the product) and the
     AWS Marketplace Seller Operations team's test account. If you view the product from the
     **Server products** page, you can choose
     **View on AWS Marketplace** to view the product details
     as they will appear in AWS Marketplace for buyers. This detail listing isn't
     visible to other AWS Marketplace users.
    * This capability allows you to test your product (and even publish
     multiple versions for testing) before releasing it publicly.

6. Test your product in the **Limited** state and make sure
   that it follows AWS Marketplace [AMI-based product requirements](product-and-ami-policies.md "product-and-ami-policies.md") and the [product checklist](aws-marketplace-listing-checklist.md "aws-marketplace-listing-checklist.md"). Then, to request that your product be
   published to **Public**, choose **Update visibility**. The AWS Marketplace Seller Operations team must review your product
   before approving it to go **Public**.

###### Note

Product verification and publication is a manual process, which is
handled by the AWS Marketplace Seller Operations team. It can take 7–10 business days to
publish your initial product version, if there are no errors. For more
details about timing, see [Timing and expectations](product-submission.md#timing-and-expectations "product-submission.md#timing-and-expectations").

For more information about preparing and submitting both your single-AMI product
and your product information, see [Additional resources](#ami-single-create-resources "#ami-single-create-resources").

## Additional resources

For more information about preparing your product information and submitting it
for publication, see the following resources:

- [Preparing your product for AWS Marketplace](product-preparation.md "product-preparation.md")
- [Submitting your product for publication on AWS Marketplace](product-submission.md "product-submission.md")

For more information about preparing your single-AMI product for submission to
AWS Marketplace, see the following resources:

- [Best practices for building AMIs for use with AWS Marketplace](best-practices-for-building-your-amis.md "best-practices-for-building-your-amis.md")
- [AMI product checklist for AWS Marketplace](aws-marketplace-listing-checklist.md "aws-marketplace-listing-checklist.md")
- [AMI-based product requirements for AWS Marketplace](product-and-ami-policies.md "product-and-ami-policies.md")
