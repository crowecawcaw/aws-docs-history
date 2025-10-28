#

Managing provisioned products as the administrator

To manage all
of the provisioned products
for an account,
you must have `AWSServiceCatalogAdminFullAccess` or an equivalent IAM permission
to access provisioned-product write operations.
For more information,
see [Identity and Access Management in
AWS Service Catalog](controlling_access.md "controlling_access.md").

###### Tip

For static provisioned-product chaining,
you must reference provisioned-product outputs
in a product-artifact template
before the provisioned product is provisioned.
For more information,
including an example,
see the following:

- [AWS::ServiceCatalog::CloudFormationProvisionedProduct](https://amazonaws.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#aws-resource-servicecatalog-cloudformationprovisionedproduct--examples "https://amazonaws.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#aws-resource-servicecatalog-cloudformationprovisionedproduct--examples")
  in the _AWS CloudFormation User Guide_.
- [DescribeProvisioningParameters (ProvisioningArtifactOutputKeys)](https://amazonaws.com/servicecatalog/latest/dg/API_DescribeProvisioningParameters.html#API_DescribeProvisioningParameters_ResponseElements "https://amazonaws.com/servicecatalog/latest/dg/API_DescribeProvisioningParameters.html#API_DescribeProvisioningParameters_ResponseElements")
  in the _AWS Service Catalog Developer Guide_.

###### To view and manage all provisioned products

1. Open the AWS Service Catalog console at [https://console.aws.amazon.com/servicecatalog/](https://console.aws.amazon.com/servicecatalog/ "https://console.aws.amazon.com/servicecatalog/").

If you are already logged in to the AWS Service Catalog console, choose
**Service Catalog**, then **End user**. 2. If necessary, scroll down to the **Provisioned products** section. 3. In the **Provisioned products** section, choose the **View:** list
and select the level of access you want to see: **User**,
**Role**, or **Account**. This action displays all the
provisioned products in the catalog. 4. Choose a provisioned product to view, update, or terminate. For more
information about the information provided in this view, see [Viewing Provisioned Product
Information](../userguide/enduser-viewstack.md "../userguide/enduser-viewstack.md").
