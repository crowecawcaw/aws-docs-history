# AWS Service Catalog API Overview

**Benefits of Using the Service Catalog API**

The AWS Service Catalog API provides programmatic control over all end-user actions as an
alternative to using the AWS Management Console. When you use the API, you can do the following:

- Write your own custom interfaces and apps
- Obtain fine-grained control of end user product provisioning operations
- Integrate resource provisioning into your orchestration pipelines
- Access a central location that hosts your applications with their resources
  **Access Service Catalog**

To build applications using language-specific APIs, use the libraries, sample code, tutorials,
and other resources for software developers. These libraries provide basic functions that
automate tasks such as cryptographically signing your requests, retrying requests, and
handling error responses, making it is easier for you to get started. To get started,
open the [Tools for Amazon Web Services](https://aws.amazon.com/tools "https://aws.amazon.com/tools") and locate the SDK of your choice under **SDKs**.

If you prefer to use a command line interface, you have the following options:

**AWS Command Line Interface (CLI)**

To get started, see the [AWS Command Line Interface User Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md"). For more information about the commands for Service Catalog,
see [servicecatalog](../../../cli/latest/reference/servicecatalog/index.md "../../../cli/latest/reference/servicecatalog/index.md") in the
_AWS CLI Command Reference_.

**AWS Tools for Windows PowerShell**

To get started, see the [AWS Tools for PowerShell User Guide](../../../powershell/latest/userguide.md "../../../powershell/latest/userguide.md"). For more information about the cmdlets for Service Catalog,
open the [AWS Tools for PowerShell Cmdlet Reference](../../../powershell/latest/reference.md "../../../powershell/latest/reference.md") and expand **AWS Service Catalog**.

The AWS Service Catalog API can be logically divided into the following categories.

###### Topics

- [Product Discovery](#product-discovery "#product-discovery")
- [Provisioning Requests](#provisioning-requests "#provisioning-requests")
- [Provisioned Products](#provisioned-info "#provisioned-info")
- [Provisioned Product Plans](#provisioned-product-plans "#provisioned-product-plans")
- [Portfolios](#portfolio-management "#portfolio-management")
- [Principal Association](#principal-association "#principal-association")
- [Products](#product-management "#product-management")
- [Provisioning Artifacts](#provisioning-artifact-management "#provisioning-artifact-management")
- [Constraints](#constraint-management "#constraint-management")
- [Service Actions](#service-action "#service-action")
- [TagOptions](#tagoption-management "#tagoption-management")
- [AppRegistry](#app-registry "#app-registry")
- [Example Workflow](#service-catalog-example-workflow "#service-catalog-example-workflow")

## Product Discovery

Use these operations to discover or get information about products and the launch
requirements for them. These operations do not create or modify resources.

[SearchProducts](../APIReference/API_SearchProducts.md "../APIReference/API_SearchProducts.md")

Lists all products to which the caller has access.

[DescribeProduct](../APIReference/API_DescribeProduct.md "../APIReference/API_DescribeProduct.md")

Get detailed information about a product.

[DescribeProductView](../APIReference/API_DescribeProductView.md "../APIReference/API_DescribeProductView.md")

Functionally identical to `DescribeProduct`, except that it
takes the ID of a product view instead of the ID of a product.

[ListLaunchPaths](../APIReference/API_ListLaunchPaths.md "../APIReference/API_ListLaunchPaths.md")

Lists all of the ways the user has access to a specified product, referred
to as _paths_ to the product. A user must select a
path in order to provision the product.

[DescribeProvisioningParameters](../APIReference/API_DescribeProvisioningParameters.md "../APIReference/API_DescribeProvisioningParameters.md")

Gets the parameters needed to provision a specified product, and
provides additional metadata about what will happen when the product is
provisioned.

Each `ProvisioningArtifactParameter` is something the user must
specify in order to successfully provision the product (for example, the
size of an EC2 instance). The `ConstraintSummary` objects contain
the list of allowable values and additional metadata about the
`ProvisioningArtifactParameter` objects.

## Provisioning Requests

Use these operations to request, update, or terminate provisioning for a product.

[ProvisionProduct](../APIReference/API_ProvisionProduct.md "../APIReference/API_ProvisionProduct.md")

Requests provisioning for a product. To provision a product is to
launch the resources needed to bring that product online for actual use.
For example, provisioning a product backed by an CloudFormation template means
launching an CloudFormation stack and all its underlying resources.

[UpdateProvisionedProduct](../APIReference/API_UpdateProvisionedProduct.md "../APIReference/API_UpdateProvisionedProduct.md")

Updates the configuration of a provisioned product. For example,
a product backed by CloudFormation gets its underlying CloudFormation stack updated. The
requester must have sufficient access permissions to the specified
ProvisionedProduct.

[TerminateProvisionedProduct](../APIReference/API_TerminateProvisionedProduct.md "../APIReference/API_TerminateProvisionedProduct.md")

Requests termination of a provisioned product. For example, for
a product backed by CloudFormation, this deletes the underlying CloudFormation stack. The
requester must have sufficient access permissions to the specified
provisioned product.

## Provisioned Products

Use these operations to get information about provisioned products. These operations do not create or modify resources.

[ListRecordHistory](../APIReference/API_ListRecordHistory.md "../APIReference/API_ListRecordHistory.md")

Lists all requests performed, even for terminated provisioned products.

[DescribeRecord](../APIReference/API_DescribeRecord.md "../APIReference/API_DescribeRecord.md")

Gets information about a request. Use this operation after the request operation
to obtain current `RecordDetail` information.

[SearchProvisionedProducts](../APIReference/API_SearchProvisionedProducts.md "../APIReference/API_SearchProvisionedProducts.md")

Gets information about the provisioned products that meet specified criteria.

[ScanProvisionedProducts](../APIReference/API_ScanProvisionedProducts.md "../APIReference/API_ScanProvisionedProducts.md")

Lists the provisioned products that are not terminated.

[DescribeProvisionedProduct](../APIReference/API_DescribeProvisionedProduct.md "../APIReference/API_DescribeProvisionedProduct.md")

Gets information about a provisioned product.

[ImportAsProvisionedProduct](../APIReference/API_ImportAsProvisionedProduct.md "../APIReference/API_ImportAsProvisionedProduct.md")

Requests the import of a resource as a Service Catalog provisioned product that is associated to a Service Catalog product and provisioning artifact. Once imported, all supported Service Catalog governance actions are supported on the provisioned product.

[UpdateProvisionedProductProperties](../APIReference/API_UpdateProvisionedProductProperties.md "../APIReference/API_UpdateProvisionedProductProperties.md")

Requests updates to the properties of the specified provisioned product.

## Provisioned Product Plans

Use these operations to manage your provisioned product plans. A plan includes the
list of resources to create or modify when you execute the plan.

[CreateProvisionedProductPlan](../APIReference/API_CreateProvisionedProductPlan.md "../APIReference/API_CreateProvisionedProductPlan.md")
Creates a plan.

[DescribeProvisionedProductPlan](../APIReference/API_DescribeProvisionedProductPlan.md "../APIReference/API_DescribeProvisionedProductPlan.md")
Gets information about the resource changes for a plan.

[ExecuteProvisionedProductPlan](../APIReference/API_ExecuteProvisionedProductPlan.md "../APIReference/API_ExecuteProvisionedProductPlan.md")
Provisions or modifies a product based on a plan.

[ListProvisionedProductPlans](../APIReference/API_ListProvisionedProductPlans.md "../APIReference/API_ListProvisionedProductPlans.md")
Lists the plans for a provisioned product.

[DeleteProvisionedProductPlan](../APIReference/API_DeleteProvisionedProductPlan.md "../APIReference/API_DeleteProvisionedProductPlan.md")
Deletes a plan.

## Portfolios

Catalog administrators use these operations provide all necessary operations for
portfolio management.

[CreatePortfolio](../APIReference/API_CreatePortfolio.md "../APIReference/API_CreatePortfolio.md")
Creates a portfolio.

[DeletePortfolio](../APIReference/API_DeletePortfolio.md "../APIReference/API_DeletePortfolio.md")
Deletes a portfolio.

[DescribePortfolio](../APIReference/API_DescribePortfolio.md "../APIReference/API_DescribePortfolio.md")
Gets detailed information about a portfolio.

[DescribePortfolioShares](../APIReference/API_DescribePortfolioShares.md "../APIReference/API_DescribePortfolioShares.md")
Returns a summary of each of the portfolio shares that were created for the specified portfolio.

[ListPortfolios](../APIReference/API_ListPortfolios.md "../APIReference/API_ListPortfolios.md")
Lists all portfolios in the catalog.

[ListPortfoliosForProduct](../APIReference/API_ListPortfoliosForProduct.md "../APIReference/API_ListPortfoliosForProduct.md")
Lists all portfolios that a product is associated with.

[UpdatePortfolio](../APIReference/API_UpdatePortfolio.md "../APIReference/API_UpdatePortfolio.md")
Updates a portfolio.

[UpdatePortfolioShare](../APIReference/API_UpdatePortfolioShare.md "../APIReference/API_UpdatePortfolioShare.md")
Updates a portfolio share.

[CreatePortfolioShare](../APIReference/API_CreatePortfolioShare.md "../APIReference/API_CreatePortfolioShare.md")
Shares a portfolio with an AWS account.

[DeletePortfolioShare](../APIReference/API_DeletePortfolioShare.md "../APIReference/API_DeletePortfolioShare.md")
Stops sharing a portfolio.

[AcceptPortfolioShare](../APIReference/API_AcceptPortfolioShare.md "../APIReference/API_AcceptPortfolioShare.md")
Accepts an offer to share a portfolio.

[RejectPortfolioShare](../APIReference/API_RejectPortfolioShare.md "../APIReference/API_RejectPortfolioShare.md")
Rejects an offer to share a portfolio.

[ListAcceptedPortfolioShares](../APIReference/API_ListAcceptedPortfolioShares.md "../APIReference/API_ListAcceptedPortfolioShares.md")
Lists details of all portfolios for which sharing was accepted by this account.

[ListPortfolioAccess](../APIReference/API_ListPortfolioAccess.md "../APIReference/API_ListPortfolioAccess.md")
Lists the account IDs that have access to a portfolio.

## Principal Association

Catalog administrators use these operations provide all necessary operations for
principal association.

[AssociatePrincipalWithPortfolio](../APIReference/API_AssociatePrincipalWithPortfolio.md "../APIReference/API_AssociatePrincipalWithPortfolio.md")
Associates a principal ARN with a portfolio.

[DisassociatePrincipalFromPortfolio](../APIReference/API_DisassociatePrincipalFromPortfolio.md "../APIReference/API_DisassociatePrincipalFromPortfolio.md")
Disassociates a principal ARN from a portfolio.

[ListPrincipalsForPortfolio](../APIReference/API_ListPrincipalsForPortfolio.md "../APIReference/API_ListPrincipalsForPortfolio.md")
Lists all principal ARNs associated with a portfolio.

## Products

Catalog administrators use these operations provide all necessary operations for
product management.

[SearchProductsAsAdmin](../APIReference/API_SearchProductsAsAdmin.md "../APIReference/API_SearchProductsAsAdmin.md")
Gets summary and status information for products.

[DescribeProductAsAdmin](../APIReference/API_DescribeProductAsAdmin.md "../APIReference/API_DescribeProductAsAdmin.md")
Gets information about a product.

[CreateProduct](../APIReference/API_CreateProduct.md "../APIReference/API_CreateProduct.md")
Creates a product.

[CopyProduct](../APIReference/API_CopyProduct.md "../APIReference/API_CopyProduct.md")
Copies a product.

[DescribeCopyProductStatus](../APIReference/API_DescribeCopyProductStatus.md "../APIReference/API_DescribeCopyProductStatus.md")
Gets the status of a copy product operation.

[UpdateProduct](../APIReference/API_UpdateProduct.md "../APIReference/API_UpdateProduct.md")
Updates a product.

[DeleteProduct](../APIReference/API_DeleteProduct.md "../APIReference/API_DeleteProduct.md")
Deletes a product.

[AssociateProductWithPortfolio](../APIReference/API_AssociateProductWithPortfolio.md "../APIReference/API_AssociateProductWithPortfolio.md")
Associates a product with a portfolio.

[DisassociateProductFromPortfolio](../APIReference/API_DisassociateProductFromPortfolio.md "../APIReference/API_DisassociateProductFromPortfolio.md")
Disassociates a product from a portfolio.

## Provisioning Artifacts

Catalog administrators use these operations to manage provisioning artifacts (also known
as product versions).

[DescribeProvisioningArtifact](../APIReference/API_DescribeProvisioningArtifact.md "../APIReference/API_DescribeProvisioningArtifact.md")
Gets information about a provisioning artifact.

[CreateProvisioningArtifact](../APIReference/API_CreateProvisioningArtifact.md "../APIReference/API_CreateProvisioningArtifact.md")
Creates a provisioning artifact for a product.

[DeleteProvisioningArtifact](../APIReference/API_DeleteProvisioningArtifact.md "../APIReference/API_DeleteProvisioningArtifact.md")
Deletes a provisioning artifact.

[ListProvisioningArtifacts](../APIReference/API_ListProvisioningArtifacts.md "../APIReference/API_ListProvisioningArtifacts.md")
Lists all provisioning artifacts associated with a product.

[UpdateProvisioningArtifact](../APIReference/API_UpdateProvisioningArtifact.md "../APIReference/API_UpdateProvisioningArtifact.md")
Updates a provisioning artifact.

## Constraints

Catalog administrator use these operations manage constraints.

[CreateConstraint](../APIReference/API_CreateConstraint.md "../APIReference/API_CreateConstraint.md")
Creates a constraint.

[DeleteConstraint](../APIReference/API_DeleteConstraint.md "../APIReference/API_DeleteConstraint.md")
Deletes a constraint.

[DescribeConstraint](../APIReference/API_DescribeConstraint.md "../APIReference/API_DescribeConstraint.md")
Gets information about a constraint.

[UpdateConstraint](../APIReference/API_UpdateConstraint.md "../APIReference/API_UpdateConstraint.md")
Updates a constraint.

[ListConstraintsForPortfolio](../APIReference/API_ListConstraintsForPortfolio.md "../APIReference/API_ListConstraintsForPortfolio.md")
Gets constraint information for the a portfolio and product.

## Service Actions

Catalog administrators use these operations to manage service actions.

[AssociateServiceActionWithProvisioningArtifact](../APIReference/API_AssociateServiceActionWithProvisioningArtifact.md "../APIReference/API_AssociateServiceActionWithProvisioningArtifact.md")
Associates a self-service action with a provisioning artifact.

[CreateServiceAction](../APIReference/API_CreateServiceAction.md "../APIReference/API_CreateServiceAction.md")
Creates a self-service action.

[DeleteServiceAction](../APIReference/API_DeleteServiceAction.md "../APIReference/API_DeleteServiceAction.md")
Deletes a self-service action.

[DescribeServiceAction](../APIReference/API_DescribeServiceAction.md "../APIReference/API_DescribeServiceAction.md")
Describes a self-service action.

[DescribeServiceActionExecutionParameters](../APIReference/API_DescribeServiceActionExecutionParameters.md "../APIReference/API_DescribeServiceActionExecutionParameters.md")
Finds the default parameters for a specific self-service action on a specific provisioned product and returns a map of the results to the user.

[ExecuteProvisionedProductServiceAction](../APIReference/API_ExecuteProvisionedProductServiceAction.md "../APIReference/API_ExecuteProvisionedProductServiceAction.md")
Executes a self-service action against a provisioned product.

[UpdateServiceAction](../APIReference/API_UpdateServiceAction.md "../APIReference/API_UpdateServiceAction.md")
Updates a self-service action.

## TagOptions

Catalog administrators use these operations to manage TagOptions.

[CreateTagOption](../APIReference/API_CreateTagOption.md "../APIReference/API_CreateTagOption.md")
Creates a TagOption.

[ListTagOptions](../APIReference/API_ListTagOptions.md "../APIReference/API_ListTagOptions.md")
Lists your TagOptions.

[DescribeTagOption](../APIReference/API_DescribeTagOption.md "../APIReference/API_DescribeTagOption.md")
Describes a TagOption.

[UpdateTagOption](../APIReference/API_UpdateTagOption.md "../APIReference/API_UpdateTagOption.md")
Updates a TagOption.

[AssociateTagOptionWithResource](../APIReference/API_AssociateTagOptionWithResource.md "../APIReference/API_AssociateTagOptionWithResource.md")
Associates a TagOption with a resource.

[DisassociateTagOptionFromResource](../APIReference/API_DisassociateTagOptionFromResource.md "../APIReference/API_DisassociateTagOptionFromResource.md")
Disassociates a TagOption from a resource.

[ListResourcesForTagOption](../APIReference/API_ListResourcesForTagOption.md "../APIReference/API_ListResourcesForTagOption.md")
Lists the resources for a TagOption.

[DeleteTagOption](../APIReference/API_DeleteTagOption.md "../APIReference/API_DeleteTagOption.md")
Deletes a TagOption.

## AppRegistry

Serves as a repository for your applications, their resources, and the application
metadata that you use in your enterprise.

[AssociateAttributeGroup](../APIReference/API_app-registry_AssociateAttributeGroup.md "../APIReference/API_app-registry_AssociateAttributeGroup.md")
Associates an attribute group with an application to augment the application's metadata with the group's attributes.

[AssociateResource](../APIReference/API_app-registry_AssociateResource.md "../APIReference/API_app-registry_AssociateResource.md")
Associates a resource with an application.

[CreateApplication](../APIReference/API_app-registry_CreateApplication.md "../APIReference/API_app-registry_CreateApplication.md")
Creates a new application that is the top-level node in a hierarchy of related cloud resource abstractions.

[CreateAttributeGroup](../APIReference/API_app-registry_CreateAttributeGroup.md "../APIReference/API_app-registry_CreateAttributeGroup.md")
Creates a new attribute group as a container for user-defined attributes.

[DeleteApplication](../APIReference/API_app-registry_DeleteApplication.md "../APIReference/API_app-registry_DeleteApplication.md")
Deletes an application that is specified either by its application ID or name.

[DeleteAttributeGroup](../APIReference/API_app-registry_DeleteAttributeGroup.md "../APIReference/API_app-registry_DeleteAttributeGroup.md")
Deletes an attribute group, specified either by its attribute group ID or name.

[DisassociateAttributeGroup](../APIReference/API_app-registry_DisassociateAttributeGroup.md "../APIReference/API_app-registry_DisassociateAttributeGroup.md")
Disassociates an attribute group from an application to remove the extra attributes contained in the attribute group from the application's metadata.

[DisassociateResource](../APIReference/API_app-registry_DisassociateResource.md "../APIReference/API_app-registry_DisassociateResource.md")
Disassociates a resource from application.

[GetApplication](../APIReference/API_app-registry_GetApplication.md "../APIReference/API_app-registry_GetApplication.md")
Retrieves metadata information about one of your applications.

[GetAssociatedResource](../APIReference/API_app-registry_GetAssociatedResource.md "../APIReference/API_app-registry_GetAssociatedResource.md")
Gets the resource associated with the application.

[GetAttributeGroup](../APIReference/API_app-registry_GetAttributeGroup.md "../APIReference/API_app-registry_GetAttributeGroup.md")
Retrieves an attribute group, either by its name or its ID.

[ListApplications](../APIReference/API_app-registry_ListApplications.md "../APIReference/API_app-registry_ListApplications.md")
Lists all attribute groups that are associated with specified application.

[ListAssociatedAttributeGroups](../APIReference/API_app-registry_ListAssociatedAttributeGroups.md "../APIReference/API_app-registry_ListAssociatedAttributeGroups.md")
Lists all attribute groups that are associated with specified application.

[ListAssociatedResources](../APIReference/API_app-registry_ListAssociatedResources.md "../APIReference/API_app-registry_ListAssociatedResources.md")
Lists all resources that are associated with specified application.

[ListAttributeGroups](../APIReference/API_app-registry_ListAttributeGroups.md "../APIReference/API_app-registry_ListAttributeGroups.md")
Lists all attribute groups of which you have access.

[ListAttributeGroupsForApplication](../APIReference/API_app-registry_ListAttributeGroupsForApplication.md "../APIReference/API_app-registry_ListAttributeGroupsForApplication.md")
Lists the details of all attribute groups associated with a specific application.

[ListTagsForResource](../APIReference/API_app-registry_ListTagsForResource.md "../APIReference/API_app-registry_ListTagsForResource.md")
Lists all of the tags on the resource.

[TagResource](../APIReference/API_app-registry_TagResource.md "../APIReference/API_app-registry_TagResource.md")
Assigns one or more tags (key-value pairs) to the specified resource.

[SyncResource](../APIReference/API_app-registry_SyncResource.md "../APIReference/API_app-registry_SyncResource.md")
Syncs the resource with what is currently recorded in AppRegistry.

[UntagResource](../APIReference/API_app-registry_UntagResource.md "../APIReference/API_app-registry_UntagResource.md")
Removes tags from a resource.

[UpdateApplication](../APIReference/API_app-registry_UpdateApplication.md "../APIReference/API_app-registry_UpdateApplication.md")
Updates an existing application with new attributes.

[UpdateAttributeGroup](../APIReference/API_app-registry_UpdateAttributeGroup.md "../APIReference/API_app-registry_UpdateAttributeGroup.md")
Updates an existing attribute group with new details.

## Example Workflow

In this scenario, the administrator creates resources using AWS Service Catalog and an end user
finds what products are available and provisions the product.
This is an example workflow; this is not the only way to use the AWS Service Catalog API.

###### Administrator Tasks

- Create portfolios, product views, products, product versions, and constraints.
- Assign IAM users to products, which gives them access.

###### End User Tasks

1. The user calls [SearchProducts](../APIReference/API_SearchProducts.md "../APIReference/API_SearchProducts.md") with no arguments.
   This returns the list of products the user has access to, as well as a "SearchDomain" that can be used
   to scope the results.
2. The user continues to call [SearchProducts](../APIReference/API_SearchProducts.md "../APIReference/API_SearchProducts.md")
   with additional search filters until the desired product is found.
3. The user calls [DescribeProductView](../APIReference/API_DescribeProductView.md "../APIReference/API_DescribeProductView.md")
   to find the list of provisioning artifacts (also known as versions) for this product. This determines
   what the user actually provisions.
4. The user calls [ListLaunchPaths](../APIReference/API_ListLaunchPaths.md "../APIReference/API_ListLaunchPaths.md") to find
   the list of paths for this product, along with the constraints for each path. This determines what
   set of constraints is applied on the provisioned product.
5. After choosing a provisioning artifact and a path, the user calls [DescribeProvisioningParameters](../APIReference/API_DescribeProvisioningParameters.md "../APIReference/API_DescribeProvisioningParameters.md"). This returns the list of parameters the user must
   provide before provisioning a product using the provisioning artifact and path, along with whatever
   additional usage instructions the administrator decided to provide.
6. The user calls [ProvisionProduct](../APIReference/API_ProvisionProduct.md "../APIReference/API_ProvisionProduct.md"), specifying
   the product, provisioning artifact, path, and input parameters. The input parameters are a
   list of key-value pairs, where the keys are obtained using [DescribeProvisioningParameters](../APIReference/API_DescribeProvisioningParameters.md "../APIReference/API_DescribeProvisioningParameters.md") and the values are user-provided (for example,
   `{ParameterKey:"dbpassword", ParameterValue:"mycoolpassword"}`). This starts a workflow to create
   the specified AWS resources. It also creates a record detail that tracks the provisioning request, and
   a provisioned product object that represents the underlying AWS resources.
7. The user polls [DescribeRecord](../APIReference/API_DescribeRecord.md "../APIReference/API_DescribeRecord.md") to see when the
   status of the record detail changes from the `IN_PROGRESS` state to a completed state (either
   `SUCCEEDED` or `ERROR`).
8. When the record detail for the request is in a completed state, the user calls [DescribeRecord](../APIReference/API_DescribeRecord.md "../APIReference/API_DescribeRecord.md") once more. The outputs identifies the created resources.
9. The user calls [UpdateProvisionedProduct](../APIReference/API_UpdateProvisionedProduct.md "../APIReference/API_UpdateProvisionedProduct.md")
   to update the underlying resources in place. Depending on the specific updates requested, this operation
   can update with no interruption, with some interruption, or replace the provisioned product entirely.
10. Finally, the user calls [TerminateProvisionedProduct](../APIReference/API_TerminateProvisionedProduct.md "../APIReference/API_TerminateProvisionedProduct.md")
    to terminate the provisioned product.
