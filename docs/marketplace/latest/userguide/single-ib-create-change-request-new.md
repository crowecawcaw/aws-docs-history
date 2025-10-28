# Creating a change

request for an EC2 Image Builder product in AWS Marketplace

To make changes to a product or version in AWS Marketplace, you submit a **change request** through the AWS Marketplace Management Portal. Change requests are added
to a queue and can take from minutes to days to resolve, depending on the type of request.
You can see the status of requests in the AWS Marketplace Management Portal. This topic provides the procedures that
you can use to create a change request for a single product in AWS Marketplace, including the
option to use the self-service experience.

You can create a change request for the following situations:

- You saved your in-progress steps, but didn't complete the entire process, while
  using the self-service experience to create a single product listing. To
  complete the remaining steps, you create a change request.
- You want to make modifications to the product information for your product that is
  in either a **Limited** or **Public** state. To
  update the information, you create a change request. For more information about the
  types of changes that you can request for EC2 Image Builder products, see [Create a change request](#single-ib-creating-change-request "#single-ib-creating-change-request").

###### Note

In addition to the AWS Marketplace Management Portal, you can also create change requests by using the [AWS Marketplace Catalog
API](../../../marketplace-catalog/latest/api-reference/seller-products.md "../../../marketplace-catalog/latest/api-reference/seller-products.md").

###### Topics

- [Create a change request by using
  self-service](#ib-self-service-change-req "#ib-self-service-change-req")
- [Create a change request](#single-ib-creating-change-request "#single-ib-creating-change-request")
- [Get the status of a change
  request](#single-ib-getting-change-request-status "#single-ib-getting-change-request-status")
- [Additional resources](#ib-single-change-req-resources "#ib-single-change-req-resources")

## Create a change request by using

self-service

To make modifications to versions or the product information, you create a _change request_ in the AWS Marketplace Management Portal. Change requests are the
building blocks of a self-service listing that you use to make changes to your product.
Each time you select **Save and exit** from the steps or select
**Submit** for any update, you are making a change request. You can
find your requests on the AWS Marketplace Management Portal [Request](https://aws.amazon.com/marketplace/management/requests "https://aws.amazon.com/marketplace/management/requests") tab.

###### To create a change request using self-service

1. Open the AWS Marketplace Management Portal at [https://aws.amazon.com/marketplace/management/tour/](https://aws.amazon.com/marketplace/management/tour/ "https://aws.amazon.com/marketplace/management/tour/"), and sign in to
   your seller account, then go to the [**Server products**](https://aws.amazon.com/marketplace/management/products/server "https://aws.amazon.com/marketplace/management/products/server") page.
2. On the **Server products** tab, select the product that you
   want to modify.
3. Choose an option from the **Request changes**
   dropdown.
4. After you make a change request, there is a wait time for the system to
   process your request, reflected **Under Review**. When the
   request completes, it will result in either **Succeeded** or
   **Failed**.
   - After the request is submitted, it begins processing through these
     statuses: **Under review**, **Preparing
     changes**, and **Applying
     changes**.
   - **Succeeded** means that the requested change has
     been processed and changes reflect in the system.
   - **Failed** means that something went wrong with the
     request, so the changes were not processed. If the status is
     **Failed**, you can select the request to find
     error codes that provide recommendations on how to correct the error. At
     this point, you can troubleshoot the errors and create a new request for
     the change. To make the process faster, you can choose **Copy to
     new request** to copy the details of the failed request.
     Then, you can make the adjustment and resubmit the request.

## Create a change request

###### Important

On June 15, 2023, AWS Marketplace will discontinue the following procedure. After June 15,
2023, use the [Create a change request by using
self-service](#ib-self-service-change-req "#ib-self-service-change-req") procedure.

To make modifications to versions or the product information, you create a _change request_ in the AWS Marketplace Management Portal.

###### To create a change request

1. Open the AWS Marketplace Management Portal at [https://aws.amazon.com/marketplace/management/tour/](https://aws.amazon.com/marketplace/management/tour/ "https://aws.amazon.com/marketplace/management/tour/"), and sign in to
   your seller account, then go to the [**Server products**](https://aws.amazon.com/marketplace/management/products/server "https://aws.amazon.com/marketplace/management/products/server") page.
2. On the **Server products** tab, select the product that you
   want to modify.
3. Choose an option from the **Request changes** dropdown
   list.

For most change requests, fill out the form in the user interface
and submit it.

For more information about the status of a change request, see [Get the status of a change
request](#single-ib-getting-change-request-status "#single-ib-getting-change-request-status"). For insight into potential
issues with change requests, see [Troubleshooting common errors for change
requests on AWS Marketplace](request-errors-and-issues.md "request-errors-and-issues.md").

## Get the status of a change

request

###### Important

On June 15, 2023, AWS Marketplace will discontinue the following procedure. This procedure
is no longer needed for the self-service experience.

After you submit a change request, you can see the status of your request from the
**Requests** tab of the [**Server
products**](https://aws.amazon.com/marketplace/management/products/server "https://aws.amazon.com/marketplace/management/products/server") page of the AWS Marketplace Management Portal. The status could be any of
the following:

- **Under review** means that your request is being reviewed.
  Some requests require manual review by the AWS Marketplace team but most are reviewed
  automatically in the system.
- **Succeeded** means that your request is complete. Your
  product or version has been updated as you requested.
- **Action required** means that you need to update your
  request to fix an issue or answer a question about the request. Select the
  request to see the details, including any issues.
- **Failed** means that something went wrong with the request,
  and you should create a new request for the change, with the same data.

## Additional resources

For more details about change requests for specific types of updates, see the
following resources:

- [Updating EC2 Image Builder product information on
  AWS Marketplace](single-ib-updating-product.md "single-ib-updating-product.md")
