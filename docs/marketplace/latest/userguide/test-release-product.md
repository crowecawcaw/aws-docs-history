# Testing and releasing your container product on AWS Marketplace

After you add a new version of your container product to AWS Marketplace, you can test your product
and then release it to the public. This topic outlines the specific steps and process required for testing and
releasing your product to public.

###### Topics

- [Container image and Helm chart
  delivery options](#container-helm-delivery "#container-helm-delivery")
- [Amazon EKS add-on delivery option](#eks-addon-delivery "#eks-addon-delivery")

## Container image and Helm chart

delivery options

This section provides guidance on the releasing your Container image and
Helm chart.

Your request for a new version is created and should complete within minutes. You can
track the request from the **Requests** tab of the **Server
products** page. If you receive any errors when testing or releasing your add-on,
see the Aynchronous Errors table in [Add a new version](../../../marketplace-catalog/latest/api-reference/container-products.md#container-add-version "../../../marketplace-catalog/latest/api-reference/container-products.md#container-add-version") in the _AWS Marketplace Catalog API Reference_.

###### Note

If your product is currently set to limited availability, only the buyers that the
product is available for can access the product version. If your product is currently set
to public availability, all AWS Marketplace buyers can access the product version.

If this was your first version set, your product is now ready to be published.

## Amazon EKS add-on delivery option

This section provides guidance on testing and releasing your Amazon EKS add-on.

**Test your add-on**

- After you submit your add-on, AWS Marketplace processes your request and publishes your add-on
  in a limited state for you to validate in the Amazon EKS add-on catalog. You can track the
  request from the **Requests** tab of the **Server
  products** page in the AWS Marketplace Management Portal. Ingestion times will vary from 5-10
  business days depending on the volume of requests we are handling.

When your request is in **Under review** status, the
add-on is still being published by AWS team from AWS Marketplace into Amazon EKS add-on catalog.
Request status changes to **Success** once the add-on is
published onto **Limited** state. You can start the testing
of your add-on after this.

- After your add-on is available, you can find it in the Asia Pacific (Seoul) Region for
  testing purposes. AWS Marketplace relies on your expertise to verify the functionality of your
  software. To test your add-on, you must create an Amazon EKS cluster in the
  Asia Pacific (Seoul) Region in your seller account where your add-on is allowlisted. To test
  your add-on, follow [these detailed instructions](https://aws.amazon.com/blogs/awsmarketplace/deploy-third-party-software-add-ons-aws-marketplace-amazon-eks-clusters/ "https://aws.amazon.com/blogs/awsmarketplace/deploy-third-party-software-add-ons-aws-marketplace-amazon-eks-clusters/"). Make sure to test on each
  Kubernetes version that your software supports.
- If you're offering a paid product, create a private offer to the following internal
  AWS accounts. These accounts help integrate your software into the Amazon EKS console in
  all commercial AWS Regions.

```
288092140294, 288092140294, 408202761791
```

- Keep your test cluster with the add-on active until AWS Marketplace approves and moves your
  add-on version to public.

###### Note

AWS Marketplace will not bear the AWS infrastructure costs incurred during testing of your
container product on your Amazon EKS clusters. You can follow right sizing mechanisms to
tone down the nodes to a minimal operating cost while we verify the testing
results.

**Release your add-on to public**

After you have validated your software via Amazon EKS cluster as an add-on, you can submit a
request to release the version of your Amazon EKS add-on to public using the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management/ "https://aws.amazon.com/marketplace/management/") or AWS Marketplace Catalog API.

For more information, see [Update the visibility for an Amazon EKS add-on](../../../marketplace-catalog/latest/api-reference/container-products.md#update-delivery-option-visibility "../../../marketplace-catalog/latest/api-reference/container-products.md#update-delivery-option-visibility") in the _AWS Marketplace Catalog API
Reference_.

You can track the request from the **Requests** tab of the
**Server products** page in the AWS Marketplace Management Portal. Ingestion times will
vary.
