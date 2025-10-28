# What Is AWS Service Catalog?

[AWS Service Catalog](https://aws.amazon.com/servicecatalog "https://aws.amazon.com/servicecatalog") enables organizations
to create and manage catalogs of products that are approved for use in AWS.

If you are new to AWS Service Catalog, see the following guides: [Service Catalog Administrator Guide](../adminguide.md "../adminguide.md") and [Service Catalog User Guide](../userguide.md "../userguide.md").

## Benefits of Using the Service Catalog API

The AWS Service Catalog API provides programmatic control over all end-user actions as an
alternative to using the AWS Management Console. When you use the API, you can do the following:

- Write your own custom interfaces and apps
- Obtain fine-grained control of end user product provisioning operations
- Integrate resource provisioning into your orchestration pipelines
- Access a central location that hosts your applications with their
  resources

## Access Service Catalog

To build applications using language-specific APIs, use the libraries, sample code, tutorials,
and other resources for software developers. These libraries provide basic functions that
automate tasks such as cryptographically signing your requests, retrying requests, and
handling error responses, making it is easier for you to get started. To get started,
open [Tools for Amazon Web Services](https://aws.amazon.com/tools/ "https://aws.amazon.com/tools/") and locate the SDK of your choice under **SDKs**.

If you prefer to use a command line interface, you have the following options:

**AWS Command Line Interface (CLI)**

To get started, see the [AWS Command Line Interface User Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md"). For more information about the commands for Service Catalog,
see [servicecatalog](../../../cli/latest/reference/servicecatalog/index.md "../../../cli/latest/reference/servicecatalog/index.md") in the
_AWS CLI Command Reference_.

**AWS Tools for Windows PowerShell**

To get started, see the [AWS Tools for PowerShell User Guide](../../../powershell/latest/userguide.md "../../../powershell/latest/userguide.md"). For more information about the cmdlets for Service Catalog,
open the [AWS Tools for PowerShell Cmdlet Reference](../../../powershell/latest/reference.md "../../../powershell/latest/reference.md") and expand **AWS Service Catalog**.

## Example Workflow

In this scenario, the administrator creates resources using Service Catalog and an end user
finds what products are available and provisions the product.
This is an example workflow; this is not the only way to use the Service Catalog API.

###### Administrator Tasks

- Create portfolios, product views, products, product versions, and constraints.
- Assign IAM users to products, which gives them access.

###### End User Tasks

1. The user calls [SearchProducts](API_SearchProducts.md "API_SearchProducts.md") with no arguments.
   This returns the list of products the user has access to, as well as a "SearchDomain" that can be used
   to scope the results.
2. The user continues to call [SearchProducts](API_SearchProducts.md "API_SearchProducts.md")
   with additional search filters until the desired product is found.
3. The user calls [DescribeProductView](API_DescribeProductView.md "API_DescribeProductView.md")
   to find the list of provisioning artifacts (also known as versions) for this product. This determines
   what the user actually provisions.
4. The user calls [ListLaunchPaths](API_ListLaunchPaths.md "API_ListLaunchPaths.md") to find
   the list of paths for this product, along with the constraints for each path. This determines what
   set of constraints is applied on the provisioned product.
5. After choosing a provisioning artifact and a path, the user calls [DescribeProvisioningParameters](API_DescribeProvisioningParameters.md "API_DescribeProvisioningParameters.md"). This returns the list of parameters the user must
   provide before provisioning a product using the provisioning artifact and path, along with whatever
   additional usage instructions the administrator decided to provide.
6. The user calls [ProvisionProduct](API_ProvisionProduct.md "API_ProvisionProduct.md"), specifying
   the product, provisioning artifact, path, and input parameters. The input parameters are a
   list of key-value pairs, where the keys are obtained using [DescribeProvisioningParameters](API_DescribeProvisioningParameters.md "API_DescribeProvisioningParameters.md") and the values are user-provided (for example,
   `{ParameterKey:"dbpassword", ParameterValue:"mycoolpassword"}`). This starts a workflow to create
   the specified AWS resources. It also creates a record detail that tracks the provisioning request, and
   a provisioned product object that represents the underlying AWS resources.
7. The user polls [DescribeRecord](API_DescribeRecord.md "API_DescribeRecord.md") to see when the
   status of the record detail changes from the `IN_PROGRESS` state to a completed state (either
   `SUCCEEDED` or `ERROR`).
8. When the record detail for the request is in a completed state, the user calls [DescribeRecord](API_DescribeRecord.md "API_DescribeRecord.md") once more. The outputs identifies the created resources.
9. The user calls [UpdateProvisionedProduct](API_UpdateProvisionedProduct.md "API_UpdateProvisionedProduct.md")
   to update the underlying resources in place. Depending on the specific updates requested, this operation
   can update with no interruption, with some interruption, or replace the provisioned product entirely.
10. Finally, the user calls [TerminateProvisionedProduct](API_TerminateProvisionedProduct.md "API_TerminateProvisionedProduct.md")
    to terminate the provisioned product.
