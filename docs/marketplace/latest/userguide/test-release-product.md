

# Testing and releasing your container product on AWS Marketplace

After you add a new version of your container product to AWS Marketplace, you can test your product and then release it to the public. This topic outlines the specific steps and process required for testing and releasing your product to public.

**Topics**
+ [Container image and Helm chart delivery options](#container-helm-delivery)
+ [Amazon EKS add-on delivery option](#eks-addon-delivery)

## Container image and Helm chart delivery options
<a name="container-helm-delivery"></a>

This section provides guidance on the releasing your Container image and Helm chart.

Your request for a new version is created and should complete within minutes. You can track the request on the **Change history** tab of your product, where it appears as **Add delivery options**. If you receive any errors when testing or releasing your add-on, see the Asynchronous Errors table in [Add a new version](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/container-products.html#container-add-version) in the *AWS Marketplace Catalog API Reference*.

**Note**  
If your product is currently set to limited availability, only the buyers that the product is available for can access the product version. If your product is currently set to public availability, all AWS Marketplace buyers can access the product version.

If this was your first version, your product is still in the **Draft** state. To move it to **Limited**, complete **Step 1: Product details** and **Step 2: Delivery configuration**, and then choose **Advance to procurement configuration**. In the **Transition to Limited** dialog box, choose **Confirm and continue**.

To publish your product, complete the remaining steps in **Complete your listing**, starting with **Step 3: Procurement configuration**, and then choose **Publish**. For more information, see [Update product visibility](container-product-getting-started.md#container-product-visibility).

## Amazon EKS add-on delivery option
<a name="eks-addon-delivery"></a>

This section provides guidance on testing and releasing your Amazon EKS add-on.

**Test your add-on**
+ After you submit your add-on, AWS Marketplace processes your request and publishes your add-on in a limited state for you to validate in the Amazon EKS add-on catalog. You can track the request on the **Change history** tab of your product. Ingestion times will vary from 5-10 business days depending on the volume of requests we are handling.

  While the AWS team publishes the add-on into the Amazon EKS add-on catalog, the request status is **Preparing** or **Applying**. When the add-on is published in the **Limited** state, the status changes to **Succeeded**. You can then start testing your add-on.
+ After your add-on is available, you can find it in the Asia Pacific (Seoul) Region for testing purposes. AWS Marketplace relies on your expertise to verify the functionality of your software. To test your add-on, you must create an Amazon EKS cluster in the Asia Pacific (Seoul) Region in your seller account where your add-on is allowlisted. To test your add-on, follow [ these detailed instructions](https://aws.amazon.com/blogs/awsmarketplace/deploy-third-party-software-add-ons-aws-marketplace-amazon-eks-clusters/). Make sure to test on each Kubernetes version that your software supports.
+ If you're offering a paid product, create a private offer to the following internal AWS accounts. These accounts help integrate your software into the Amazon EKS console in all commercial AWS Regions.

  ```
  288092140294, 288092140294, 408202761791
  ```
+ Keep your test cluster with the add-on active until AWS Marketplace approves and moves your add-on version to public.
**Note**  
AWS Marketplace will not bear the AWS infrastructure costs incurred during testing of your container product on your Amazon EKS clusters. You can follow right sizing mechanisms to tone down the nodes to a minimal operating cost while we verify the testing results.

**Release your add-on to public**

After you have validated your software via Amazon EKS cluster as an add-on, you can submit a request to release the version of your Amazon EKS add-on to public using AWS Partner Central or the AWS Marketplace Catalog API.

**To release an Amazon EKS add-on version**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose the **Delivery** tab.

1. In the **Versions** section, choose **Edit**, and then choose **Update version visibility**.

   This action appears when the product has Limited or Public visibility and has an Amazon EKS add-on delivery option with Limited visibility.

1. Under **Select versions to release**, select the versions whose add-on you want to release.

   The table lists only versions with an Amazon EKS add-on delivery option that has Limited visibility. One request can release up to 50 delivery options.

1. Choose **Save and submit**.

Your change request appears on the product's **Change history** tab as **Update version visibility**. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name. While a request is in progress, the actions on the **Delivery** tab are unavailable.

 For more information, see [Update the visibility for an Amazon EKS add-on](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/container-products.html#update-delivery-option-visibility) in the *AWS Marketplace Catalog API Reference*.