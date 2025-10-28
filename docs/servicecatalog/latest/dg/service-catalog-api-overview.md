# AWS Service Catalog API Overview

The AWS Service Catalog API can be logically divided into the following categories.

###### Operations by category

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

## Product Discovery

Use these operations to discover or get information about products and the launch
requirements for them. These operations do not create or modify resources.

[SearchProducts](API_SearchProducts.md "API_SearchProducts.md")

Lists all products to which the caller has access.

[DescribeProduct](API_DescribeProduct.md "API_DescribeProduct.md")

Get detailed information about a product.

[DescribeProductView](API_DescribeProductView.md "API_DescribeProductView.md")

Functionally identical to `DescribeProduct`, except that it
takes the ID of a product view instead of the ID of a product.

[ListLaunchPaths](API_ListLaunchPaths.md "API_ListLaunchPaths.md")

Lists all of the ways the user has access to a specified product, referred
to as _paths_ to the product. A user must select a
path in order to provision the product.

[DescribeProvisioningParameters](API_DescribeProvisioningParameters.md "API_DescribeProvisioningParameters.md")

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

[ProvisionProduct](API_ProvisionProduct.md "API_ProvisionProduct.md")

Requests provisioning for a product. To provision a product is to
launch the resources needed to bring that product online for actual use.
For example, provisioning a product backed by an AWS CloudFormation template means
launching an AWS CloudFormation stack and all its underlying resources.

[UpdateProvisionedProduct](API_UpdateProvisionedProduct.md "API_UpdateProvisionedProduct.md")

Updates the configuration of a provisioned product. For example,
a product backed by AWS CloudFormation gets its underlying AWS CloudFormation stack updated. The
requester must have sufficient access permissions to the specified
ProvisionedProduct.

[TerminateProvisionedProduct](API_TerminateProvisionedProduct.md "API_TerminateProvisionedProduct.md")

Requests termination of a provisioned product. For example, for
a product backed by AWS CloudFormation, this deletes the underlying AWS CloudFormation stack. The
requester must have sufficient access permissions to the specified
provisioned product.

## Provisioned Products

Use these operations to get information about provisioned products. These operations do not create or modify resources.

[ListRecordHistory](API_ListRecordHistory.md "API_ListRecordHistory.md")

Lists all requests performed, even for terminated provisioned products.

[DescribeRecord](API_DescribeRecord.md "API_DescribeRecord.md")

Gets information about a request. Use this operation after the request operation
to obtain current `RecordDetail` information.

[SearchProvisionedProducts](API_SearchProvisionedProducts.md "API_SearchProvisionedProducts.md")

Gets information about the provisioned products that meet specified criteria.

[ScanProvisionedProducts](API_ScanProvisionedProducts.md "API_ScanProvisionedProducts.md")

Lists the provisioned products that are not terminated.

[DescribeProvisionedProduct](API_DescribeProvisionedProduct.md "API_DescribeProvisionedProduct.md")

Gets information about a provisioned product.

[ImportAsProvisionedProduct](API_ImportAsProvisionedProduct.md "API_ImportAsProvisionedProduct.md")

Requests the import of a resource as a Service Catalog provisioned product that is associated to a Service Catalog product and provisioning artifact. Once imported, all supported Service Catalog governance actions are supported on the provisioned product.

[UpdateProvisionedProductProperties](API_UpdateProvisionedProductProperties.md "API_UpdateProvisionedProductProperties.md")

Requests updates to the properties of the specified provisioned product.

## Provisioned Product Plans

Use these operations to manage your provisioned product plans. A plan includes the
list of resources to create or modify when you execute the plan.

[CreateProvisionedProductPlan](API_CreateProvisionedProductPlan.md "API_CreateProvisionedProductPlan.md")

Creates a plan.

[DescribeProvisionedProductPlan](API_DescribeProvisionedProductPlan.md "API_DescribeProvisionedProductPlan.md")

Gets information about the resource changes for a plan.

[ExecuteProvisionedProductPlan](API_ExecuteProvisionedProductPlan.md "API_ExecuteProvisionedProductPlan.md")

Provisions or modifies a product based on a plan.

[ListProvisionedProductPlans](API_ListProvisionedProductPlans.md "API_ListProvisionedProductPlans.md")

Lists the plans for a provisioned product.

[DeleteProvisionedProductPlan](API_DeleteProvisionedProductPlan.md "API_DeleteProvisionedProductPlan.md")

Deletes a plan.

## Portfolios

Catalog administrators use these operations provide all necessary operations for
portfolio management.

[CreatePortfolio](API_CreatePortfolio.md "API_CreatePortfolio.md")

Creates a portfolio.

[DeletePortfolio](API_DeletePortfolio.md "API_DeletePortfolio.md")

Deletes a portfolio.

[DescribePortfolio](API_DescribePortfolio.md "API_DescribePortfolio.md")

Gets detailed information about a portfolio.

[DescribePortfolioShares](API_DescribePortfolioShares.md "API_DescribePortfolioShares.md")

Returns a summary of each of the portfolio shares that were created for the specified portfolio.

[ListPortfolios](API_ListPortfolios.md "API_ListPortfolios.md")

Lists all portfolios in the catalog.

[ListPortfoliosForProduct](API_ListPortfoliosForProduct.md "API_ListPortfoliosForProduct.md")

Lists all portfolios that a product is associated with.

[UpdatePortfolio](API_UpdatePortfolio.md "API_UpdatePortfolio.md")

Updates a portfolio.

[UpdatePortfolioShare](API_UpdatePortfolioShare.md "API_UpdatePortfolioShare.md")

Updates a portfolio share.

[CreatePortfolioShare](API_CreatePortfolioShare.md "API_CreatePortfolioShare.md")

Shares a portfolio with an AWS account.

[DeletePortfolioShare](API_DeletePortfolioShare.md "API_DeletePortfolioShare.md")

Stops sharing a portfolio.

[AcceptPortfolioShare](API_AcceptPortfolioShare.md "API_AcceptPortfolioShare.md")

Accepts an offer to share a portfolio.

[RejectPortfolioShare](API_RejectPortfolioShare.md "API_RejectPortfolioShare.md")

Rejects an offer to share a portfolio.

[ListAcceptedPortfolioShares](API_ListAcceptedPortfolioShares.md "API_ListAcceptedPortfolioShares.md")

Lists details of all portfolios for which sharing was accepted by this account.

[ListPortfolioAccess](API_ListPortfolioAccess.md "API_ListPortfolioAccess.md")

Lists the account IDs that have access to a portfolio.

## Principal Association

Catalog administrators use these operations provide all necessary operations for
principal association.

[AssociatePrincipalWithPortfolio](API_AssociatePrincipalWithPortfolio.md "API_AssociatePrincipalWithPortfolio.md")

Associates a principal ARN with a portfolio.

[DisassociatePrincipalFromPortfolio](API_DisassociatePrincipalFromPortfolio.md "API_DisassociatePrincipalFromPortfolio.md")

Disassociates a principal ARN from a portfolio.

[ListPrincipalsForPortfolio](API_ListPrincipalsForPortfolio.md "API_ListPrincipalsForPortfolio.md")

Lists all principal ARNs associated with a portfolio.

## Products

Catalog administrators use these operations provide all necessary operations for
product management.

[SearchProductsAsAdmin](API_SearchProductsAsAdmin.md "API_SearchProductsAsAdmin.md")

Gets summary and status information for products.

[DescribeProductAsAdmin](API_DescribeProductAsAdmin.md "API_DescribeProductAsAdmin.md")

Gets information about a product.

[CreateProduct](API_CreateProduct.md "API_CreateProduct.md")

Creates a product.

[CopyProduct](API_CopyProduct.md "API_CopyProduct.md")

Copies a product.

[DescribeCopyProductStatus](API_DescribeCopyProductStatus.md "API_DescribeCopyProductStatus.md")

Gets the status of a copy product operation.

[UpdateProduct](API_UpdateProduct.md "API_UpdateProduct.md")

Updates a product.

[DeleteProduct](API_DeleteProduct.md "API_DeleteProduct.md")

Deletes a product.

[AssociateProductWithPortfolio](API_AssociateProductWithPortfolio.md "API_AssociateProductWithPortfolio.md")

Associates a product with a portfolio.

[DisassociateProductFromPortfolio](API_DisassociateProductFromPortfolio.md "API_DisassociateProductFromPortfolio.md")

Disassociates a product from a portfolio.

## Provisioning Artifacts

Catalog administrators use these operations to manage provisioning artifacts (also known
as product versions).

[DescribeProvisioningArtifact](API_DescribeProvisioningArtifact.md "API_DescribeProvisioningArtifact.md")

Gets information about a provisioning artifact.

[CreateProvisioningArtifact](API_CreateProvisioningArtifact.md "API_CreateProvisioningArtifact.md")

Creates a provisioning artifact for a product.

[DeleteProvisioningArtifact](API_DeleteProvisioningArtifact.md "API_DeleteProvisioningArtifact.md")

Deletes a provisioning artifact.

[ListProvisioningArtifacts](API_ListProvisioningArtifacts.md "API_ListProvisioningArtifacts.md")

Lists all provisioning artifacts associated with a product.

[UpdateProvisioningArtifact](API_UpdateProvisioningArtifact.md "API_UpdateProvisioningArtifact.md")

Updates a provisioning artifact.

## Constraints

Catalog administrator use these operations manage constraints.

[CreateConstraint](API_CreateConstraint.md "API_CreateConstraint.md")

Creates a constraint.

[DeleteConstraint](API_DeleteConstraint.md "API_DeleteConstraint.md")

Deletes a constraint.

[DescribeConstraint](API_DescribeConstraint.md "API_DescribeConstraint.md")

Gets information about a constraint.

[UpdateConstraint](API_UpdateConstraint.md "API_UpdateConstraint.md")

Updates a constraint.

[ListConstraintsForPortfolio](API_ListConstraintsForPortfolio.md "API_ListConstraintsForPortfolio.md")

Gets constraint information for the a portfolio and product.

## Service Actions

Catalog administrators use these operations to manage service actions.

[AssociateServiceActionWithProvisioningArtifact](API_AssociateServiceActionWithProvisioningArtifact.md "API_AssociateServiceActionWithProvisioningArtifact.md")

Associates a self-service action with a provisioning artifact.

[CreateServiceAction](API_CreateServiceAction.md "API_CreateServiceAction.md")

Creates a self-service action.

[DeleteServiceAction](API_DeleteServiceAction.md "API_DeleteServiceAction.md")

Deletes a self-service action.

[DescribeServiceAction](API_DescribeServiceAction.md "API_DescribeServiceAction.md")

Describes a self-service action.

[DescribeServiceActionExecutionParameters](API_DescribeServiceActionExecutionParameters.md "API_DescribeServiceActionExecutionParameters.md")

Finds the default parameters for a specific self-service action on a specific provisioned product and returns a map of the results to the user.

[ExecuteProvisionedProductServiceAction](API_ExecuteProvisionedProductServiceAction.md "API_ExecuteProvisionedProductServiceAction.md")

Executes a self-service action against a provisioned product.

[UpdateServiceAction](API_UpdateServiceAction.md "API_UpdateServiceAction.md")

Updates a self-service action.

## TagOptions

Catalog administrators use these operations to manage TagOptions.

[CreateTagOption](API_CreateTagOption.md "API_CreateTagOption.md")

Creates a TagOption.

[ListTagOptions](API_ListTagOptions.md "API_ListTagOptions.md")

Lists your TagOptions.

[DescribeTagOption](API_DescribeTagOption.md "API_DescribeTagOption.md")

Describes a TagOption.

[UpdateTagOption](API_UpdateTagOption.md "API_UpdateTagOption.md")

Updates a TagOption.

[AssociateTagOptionWithResource](API_AssociateTagOptionWithResource.md "API_AssociateTagOptionWithResource.md")

Associates a TagOption with a resource.

[DisassociateTagOptionFromResource](API_DisassociateTagOptionFromResource.md "API_DisassociateTagOptionFromResource.md")

Disassociates a TagOption from a resource.

[ListResourcesForTagOption](API_ListResourcesForTagOption.md "API_ListResourcesForTagOption.md")

Lists the resources for a TagOption.

[DeleteTagOption](API_DeleteTagOption.md "API_DeleteTagOption.md")

Deletes a TagOption.

## AppRegistry

Serves as a repository for your applications, their resources, and the application
metadata that you use in your enterprise.

[AssociateAttributeGroup](API_app-registry_AssociateAttributeGroup.md "API_app-registry_AssociateAttributeGroup.md")

Associates an attribute group with an application to augment the
application's metadata with the group's attributes.

[AssociateResource](API_app-registry_AssociateResource.md "API_app-registry_AssociateResource.md")

Associates a resource with an application.

[CreateApplication](API_app-registry_CreateApplication.md "API_app-registry_CreateApplication.md")

Creates a new application that is the top-level node in a hierarchy of
related cloud resource abstractions.

[CreateAttributeGroup](API_app-registry_CreateAttributeGroup.md "API_app-registry_CreateAttributeGroup.md")

Creates a new attribute group as a container for user-defined attributes.

[DeleteApplication](API_app-registry_DeleteApplication.md "API_app-registry_DeleteApplication.md")

Deletes an application that is specified either by its application ID or
name.

[DeleteAttributeGroup](API_app-registry_DeleteAttributeGroup.md "API_app-registry_DeleteAttributeGroup.md")

Deletes an attribute group, specified either by its attribute group ID or
name.

[DisassociateAttributeGroup](API_app-registry_DisassociateAttributeGroup.md "API_app-registry_DisassociateAttributeGroup.md")

Disassociates an attribute group from an application to remove the extra
attributes contained in the attribute group from the application's metadata.

[DisassociateResource](API_app-registry_DisassociateResource.md "API_app-registry_DisassociateResource.md")

Disassociates a resource from application.

[GetApplication](API_app-registry_GetApplication.md "API_app-registry_GetApplication.md")

Retrieves metadata information about one of your applications.

[GetAssociatedResource](API_app-registry_GetAssociatedResource.md "API_app-registry_GetAssociatedResource.md")

Gets the resource associated with the application.

[GetAttributeGroup](API_app-registry_GetAttributeGroup.md "API_app-registry_GetAttributeGroup.md")

Retrieves an attribute group, either by its name or its ID.

[ListApplications](API_app-registry_ListApplications.md "API_app-registry_ListApplications.md")

Lists all attribute groups that are associated with specified application.

[ListAssociatedAttributeGroups](API_app-registry_ListAssociatedAttributeGroups.md "API_app-registry_ListAssociatedAttributeGroups.md")

Lists all attribute groups that are associated with specified application.

[ListAssociatedResources](API_app-registry_ListAssociatedResources.md "API_app-registry_ListAssociatedResources.md")

Lists all resources that are associated with specified application.

[ListAttributeGroups](API_app-registry_ListAttributeGroups.md "API_app-registry_ListAttributeGroups.md")

Lists all attribute groups of which you have access.

[ListAttributeGroupsForApplication](API_app-registry_ListAttributeGroupsForApplication.md "API_app-registry_ListAttributeGroupsForApplication.md")

Lists the details of all attribute groups associated with a specific application.

[ListTagsForResource](API_app-registry_ListTagsForResource.md "API_app-registry_ListTagsForResource.md")

Lists all of the tags on the resource.

[TagResource](API_app-registry_TagResource.md "API_app-registry_TagResource.md")

Assigns one or more tags (key-value pairs) to the specified resource.

[SyncResource](API_app-registry_SyncResource.md "API_app-registry_SyncResource.md")

Syncs the resource with what is currently recorded in AppRegistry.

[UntagResource](API_app-registry_UntagResource.md "API_app-registry_UntagResource.md")

Removes tags from a resource.

[UpdateApplication](API_app-registry_UpdateApplication.md "API_app-registry_UpdateApplication.md")

Updates an existing application with new attributes.

[UpdateAttributeGroup](API_app-registry_UpdateAttributeGroup.md "API_app-registry_UpdateAttributeGroup.md")

Updates an existing attribute group with new details.
