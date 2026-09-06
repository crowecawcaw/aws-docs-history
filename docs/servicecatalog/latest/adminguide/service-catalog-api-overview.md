

# AWS Service Catalog API Overview
<a name="service-catalog-api-overview"></a>

**Benefits of Using the Service Catalog API**

The AWS Service Catalog API provides programmatic control over all end-user actions as an alternative to using the AWS Management Console. When you use the API, you can do the following:
+ Write your own custom interfaces and apps
+ Obtain fine-grained control of end user product provisioning operations
+ Integrate resource provisioning into your orchestration pipelines
+ Access a central location that hosts your applications with their resources

**Access Service Catalog**

To build applications using language-specific APIs, use the libraries, sample code, tutorials, and other resources for software developers. These libraries provide basic functions that automate tasks such as cryptographically signing your requests, retrying requests, and handling error responses, making it is easier for you to get started. To get started, open the [Tools for Amazon Web Services](https://aws.amazon.com/tools) and locate the SDK of your choice under **SDKs**.

If you prefer to use a command line interface, you have the following options:

**AWS Command Line Interface (CLI)**  
To get started, see the [AWS Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/). For more information about the commands for Service Catalog, see [servicecatalog](https://docs.aws.amazon.com/cli/latest/reference/servicecatalog/index.html) in the *AWS CLI Command Reference*.

**AWS Tools for Windows PowerShell**  
To get started, see the [AWS Tools for PowerShell User Guide](https://docs.aws.amazon.com/powershell/latest/userguide/). For more information about the cmdlets for Service Catalog, open the [AWS Tools for PowerShell Cmdlet Reference](https://docs.aws.amazon.com/powershell/latest/reference/) and expand **AWS Service Catalog**.

The AWS Service Catalog API can be logically divided into the following categories.

**Topics**
+ [Product Discovery](#product-discovery)
+ [Provisioning Requests](#provisioning-requests)
+ [Provisioned Products](#provisioned-info)
+ [Provisioned Product Plans](#provisioned-product-plans)
+ [Portfolios](#portfolio-management)
+ [Principal Association](#principal-association)
+ [Products](#product-management)
+ [Provisioning Artifacts](#provisioning-artifact-management)
+ [Constraints](#constraint-management)
+ [Service Actions](#service-action)
+ [TagOptions](#tagoption-management)
+ [AppRegistry](#app-registry)
+ [Example Workflow](#service-catalog-example-workflow)

## Product Discovery
<a name="product-discovery"></a>

Use these operations to discover or get information about products and the launch requirements for them. These operations do not create or modify resources.

[SearchProducts](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_SearchProducts.html)  
Lists all products to which the caller has access.

[DescribeProduct](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_DescribeProduct.html)  
Get detailed information about a product.

[DescribeProductView](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_DescribeProductView.html)  
Functionally identical to `DescribeProduct`, except that it takes the ID of a product view instead of the ID of a product.

[ListLaunchPaths](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ListLaunchPaths.html)  
Lists all of the ways the user has access to a specified product, referred to as *paths* to the product. A user must select a path in order to provision the product.

[DescribeProvisioningParameters](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_DescribeProvisioningParameters.html)  
Gets the parameters needed to provision a specified product, and provides additional metadata about what will happen when the product is provisioned.  
Each `ProvisioningArtifactParameter` is something the user must specify in order to successfully provision the product (for example, the size of an EC2 instance). The `ConstraintSummary` objects contain the list of allowable values and additional metadata about the `ProvisioningArtifactParameter` objects.

## Provisioning Requests
<a name="provisioning-requests"></a>

Use these operations to request, update, or terminate provisioning for a product.

[ProvisionProduct](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ProvisionProduct.html)  
Requests provisioning for a product. To provision a product is to launch the resources needed to bring that product online for actual use. For example, provisioning a product backed by an CloudFormation template means launching an CloudFormation stack and all its underlying resources.

[UpdateProvisionedProduct](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_UpdateProvisionedProduct.html)  
Updates the configuration of a provisioned product. For example, a product backed by CloudFormation gets its underlying CloudFormation stack updated. The requester must have sufficient access permissions to the specified ProvisionedProduct.

[TerminateProvisionedProduct](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_TerminateProvisionedProduct.html)  
Requests termination of a provisioned product. For example, for a product backed by CloudFormation, this deletes the underlying CloudFormation stack. The requester must have sufficient access permissions to the specified provisioned product.

## Provisioned Products
<a name="provisioned-info"></a>

Use these operations to get information about provisioned products. These operations do not create or modify resources.

[ListRecordHistory](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ListRecordHistory.html)  
Lists all requests performed, even for terminated provisioned products.

[DescribeRecord](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_DescribeRecord.html)  
Gets information about a request. Use this operation after the request operation to obtain current `RecordDetail` information.

[SearchProvisionedProducts](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_SearchProvisionedProducts.html)  
Gets information about the provisioned products that meet specified criteria.

[ScanProvisionedProducts](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ScanProvisionedProducts.html)  
Lists the provisioned products that are not terminated.

[DescribeProvisionedProduct](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_DescribeProvisionedProduct.html)  
Gets information about a provisioned product.

[ImportAsProvisionedProduct](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ImportAsProvisionedProduct.html)  
Requests the import of a resource as a Service Catalog provisioned product that is associated to a Service Catalog product and provisioning artifact. Once imported, all supported Service Catalog governance actions are supported on the provisioned product.

[UpdateProvisionedProductProperties](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_UpdateProvisionedProductProperties.html)  
Requests updates to the properties of the specified provisioned product.

## Provisioned Product Plans
<a name="provisioned-product-plans"></a>

Use these operations to manage your provisioned product plans. A plan includes the list of resources to create or modify when you execute the plan.

[CreateProvisionedProductPlan](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_CreateProvisionedProductPlan.html)  
Creates a plan.

[DescribeProvisionedProductPlan](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_DescribeProvisionedProductPlan.html)  
Gets information about the resource changes for a plan.

[ExecuteProvisionedProductPlan](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ExecuteProvisionedProductPlan.html)  
Provisions or modifies a product based on a plan.

[ListProvisionedProductPlans](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ListProvisionedProductPlans.html)  
Lists the plans for a provisioned product.

[DeleteProvisionedProductPlan](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_DeleteProvisionedProductPlan.html)  
Deletes a plan.

## Portfolios
<a name="portfolio-management"></a>

Catalog administrators use these operations provide all necessary operations for portfolio management.

[CreatePortfolio](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_CreatePortfolio.html)  
Creates a portfolio.

[DeletePortfolio](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_DeletePortfolio.html)  
Deletes a portfolio.

[DescribePortfolio](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_DescribePortfolio.html)  
Gets detailed information about a portfolio.

[DescribePortfolioShares](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_DescribePortfolioShares.html)  
Returns a summary of each of the portfolio shares that were created for the specified portfolio.

[ListPortfolios](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ListPortfolios.html)  
Lists all portfolios in the catalog.

[ListPortfoliosForProduct](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ListPortfoliosForProduct.html)  
Lists all portfolios that a product is associated with.

[UpdatePortfolio](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_UpdatePortfolio.html)  
Updates a portfolio.

[UpdatePortfolioShare](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_UpdatePortfolioShare.html)  
Updates a portfolio share.

[CreatePortfolioShare](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_CreatePortfolioShare.html)  
Shares a portfolio with an AWS account.

[DeletePortfolioShare](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_DeletePortfolioShare.html)  
Stops sharing a portfolio.

[AcceptPortfolioShare](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_AcceptPortfolioShare.html)  
Accepts an offer to share a portfolio.

[RejectPortfolioShare](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_RejectPortfolioShare.html)  
Rejects an offer to share a portfolio.

[ListAcceptedPortfolioShares](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ListAcceptedPortfolioShares.html)  
Lists details of all portfolios for which sharing was accepted by this account.

[ListPortfolioAccess](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ListPortfolioAccess.html)  
Lists the account IDs that have access to a portfolio.

## Principal Association
<a name="principal-association"></a>

Catalog administrators use these operations provide all necessary operations for principal association.

[AssociatePrincipalWithPortfolio](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_AssociatePrincipalWithPortfolio.html)  
Associates a principal ARN with a portfolio.

[DisassociatePrincipalFromPortfolio](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_DisassociatePrincipalFromPortfolio.html)  
Disassociates a principal ARN from a portfolio.

[ListPrincipalsForPortfolio](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ListPrincipalsForPortfolio.html)  
Lists all principal ARNs associated with a portfolio.

## Products
<a name="product-management"></a>

Catalog administrators use these operations provide all necessary operations for product management.

[SearchProductsAsAdmin](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_SearchProductsAsAdmin.html)  
Gets summary and status information for products.

[DescribeProductAsAdmin](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_DescribeProductAsAdmin.html)  
Gets information about a product.

[CreateProduct](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_CreateProduct.html)  
Creates a product.

[CopyProduct](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_CopyProduct.html)  
Copies a product.

[DescribeCopyProductStatus](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_DescribeCopyProductStatus.html)  
Gets the status of a copy product operation.

[UpdateProduct](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_UpdateProduct.html)  
Updates a product.

[DeleteProduct](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_DeleteProduct.html)  
Deletes a product.

[AssociateProductWithPortfolio](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_AssociateProductWithPortfolio.html)  
Associates a product with a portfolio.

[DisassociateProductFromPortfolio](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_DisassociateProductFromPortfolio.html)  
Disassociates a product from a portfolio.

## Provisioning Artifacts
<a name="provisioning-artifact-management"></a>

Catalog administrators use these operations to manage provisioning artifacts (also known as product versions).

[DescribeProvisioningArtifact](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_DescribeProvisioningArtifact.html)  
Gets information about a provisioning artifact.

[CreateProvisioningArtifact](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_CreateProvisioningArtifact.html)  
Creates a provisioning artifact for a product.

[DeleteProvisioningArtifact](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_DeleteProvisioningArtifact.html)  
Deletes a provisioning artifact.

[ListProvisioningArtifacts](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ListProvisioningArtifacts.html)  
Lists all provisioning artifacts associated with a product.

[UpdateProvisioningArtifact](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_UpdateProvisioningArtifact.html)  
Updates a provisioning artifact.

## Constraints
<a name="constraint-management"></a>

Catalog administrator use these operations manage constraints.

[CreateConstraint](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_CreateConstraint.html)  
Creates a constraint.

[DeleteConstraint](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_DeleteConstraint.html)  
Deletes a constraint.

[DescribeConstraint](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_DescribeConstraint.html)  
Gets information about a constraint.

[UpdateConstraint](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_UpdateConstraint.html)  
Updates a constraint.

[ListConstraintsForPortfolio](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ListConstraintsForPortfolio.html)  
Gets constraint information for the a portfolio and product.

## Service Actions
<a name="service-action"></a>

Catalog administrators use these operations to manage service actions.

[AssociateServiceActionWithProvisioningArtifact](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_AssociateServiceActionWithProvisioningArtifact.html)  
Associates a self-service action with a provisioning artifact.

[CreateServiceAction](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_CreateServiceAction.html)  
Creates a self-service action.

[DeleteServiceAction](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_DeleteServiceAction.html)  
Deletes a self-service action.

[DescribeServiceAction](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_DescribeServiceAction.html)  
Describes a self-service action.

[DescribeServiceActionExecutionParameters](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_DescribeServiceActionExecutionParameters.html)  
Finds the default parameters for a specific self-service action on a specific provisioned product and returns a map of the results to the user.

[ExecuteProvisionedProductServiceAction](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ExecuteProvisionedProductServiceAction.html)  
Executes a self-service action against a provisioned product.

[UpdateServiceAction](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_UpdateServiceAction.html)  
Updates a self-service action.

## TagOptions
<a name="tagoption-management"></a>

Catalog administrators use these operations to manage TagOptions.

[CreateTagOption](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_CreateTagOption.html)  
Creates a TagOption.

[ListTagOptions](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ListTagOptions.html)  
Lists your TagOptions.

[DescribeTagOption](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_DescribeTagOption.html)  
Describes a TagOption.

[UpdateTagOption](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_UpdateTagOption.html)  
Updates a TagOption.

[AssociateTagOptionWithResource](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_AssociateTagOptionWithResource.html)  
Associates a TagOption with a resource.

[DisassociateTagOptionFromResource](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_DisassociateTagOptionFromResource.html)  
Disassociates a TagOption from a resource.

[ListResourcesForTagOption](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ListResourcesForTagOption.html)  
Lists the resources for a TagOption.

[DeleteTagOption](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_DeleteTagOption.html)  
Deletes a TagOption.

## AppRegistry
<a name="app-registry"></a>

Serves as a repository for your applications, their resources, and the application metadata that you use in your enterprise.

[AssociateAttributeGroup](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_app-registry_AssociateAttributeGroup.html)  
Associates an attribute group with an application to augment the application's metadata with the group's attributes.

[AssociateResource](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_app-registry_AssociateResource.html)  
Associates a resource with an application.

[CreateApplication](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_app-registry_CreateApplication.html)  
Creates a new application that is the top-level node in a hierarchy of related cloud resource abstractions.

[CreateAttributeGroup](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_app-registry_CreateAttributeGroup.html)  
Creates a new attribute group as a container for user-defined attributes.

[DeleteApplication](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_app-registry_DeleteApplication.html)  
Deletes an application that is specified either by its application ID or name.

[DeleteAttributeGroup](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_app-registry_DeleteAttributeGroup.html)  
Deletes an attribute group, specified either by its attribute group ID or name.

[DisassociateAttributeGroup](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_app-registry_DisassociateAttributeGroup.html)  
Disassociates an attribute group from an application to remove the extra attributes contained in the attribute group from the application's metadata.

[DisassociateResource](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_app-registry_DisassociateResource.html)  
Disassociates a resource from application.

[GetApplication](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_app-registry_GetApplication.html)  
Retrieves metadata information about one of your applications.

[GetAssociatedResource](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_app-registry_GetAssociatedResource.html)  
Gets the resource associated with the application.

[GetAttributeGroup](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_app-registry_GetAttributeGroup.html)  
Retrieves an attribute group, either by its name or its ID.

[ListApplications](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_app-registry_ListApplications.html)  
Lists all attribute groups that are associated with specified application.

[ListAssociatedAttributeGroups](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_app-registry_ListAssociatedAttributeGroups.html)  
Lists all attribute groups that are associated with specified application.

[ListAssociatedResources](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_app-registry_ListAssociatedResources.html)  
Lists all resources that are associated with specified application.

[ListAttributeGroups](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_app-registry_ListAttributeGroups.html)  
Lists all attribute groups of which you have access.

[ListAttributeGroupsForApplication](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_app-registry_ListAttributeGroupsForApplication.html)  
Lists the details of all attribute groups associated with a specific application.

[ListTagsForResource](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_app-registry_ListTagsForResource.html)  
Lists all of the tags on the resource.

[TagResource](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_app-registry_TagResource.html)  
Assigns one or more tags (key-value pairs) to the specified resource.

[SyncResource](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_app-registry_SyncResource.html)  
Syncs the resource with what is currently recorded in AppRegistry.

[UntagResource](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_app-registry_UntagResource.html)  
Removes tags from a resource.

[UpdateApplication](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_app-registry_UpdateApplication.html)  
Updates an existing application with new attributes.

[UpdateAttributeGroup](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_app-registry_UpdateAttributeGroup.html)  
Updates an existing attribute group with new details.

## Example Workflow
<a name="service-catalog-example-workflow"></a>

In this scenario, the administrator creates resources using AWS Service Catalog and an end user finds what products are available and provisions the product. This is an example workflow; this is not the only way to use the AWS Service Catalog API.

**Administrator Tasks**
+ Create portfolios, product views, products, product versions, and constraints.
+ Assign IAM users to products, which gives them access.

**End User Tasks**

1. The user calls [SearchProducts](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_SearchProducts.html) with no arguments. This returns the list of products the user has access to, as well as a "SearchDomain" that can be used to scope the results.

1. The user continues to call [SearchProducts](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_SearchProducts.html) with additional search filters until the desired product is found.

1. The user calls [DescribeProductView](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_DescribeProductView.html) to find the list of provisioning artifacts (also known as versions) for this product. This determines what the user actually provisions.

1. The user calls [ListLaunchPaths](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ListLaunchPaths.html) to find the list of paths for this product, along with the constraints for each path. This determines what set of constraints is applied on the provisioned product.

1. After choosing a provisioning artifact and a path, the user calls [DescribeProvisioningParameters](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_DescribeProvisioningParameters.html). This returns the list of parameters the user must provide before provisioning a product using the provisioning artifact and path, along with whatever additional usage instructions the administrator decided to provide.

1. The user calls [ProvisionProduct](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ProvisionProduct.html), specifying the product, provisioning artifact, path, and input parameters. The input parameters are a list of key-value pairs, where the keys are obtained using [DescribeProvisioningParameters](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_DescribeProvisioningParameters.html) and the values are user-provided (for example, `{ParameterKey:"dbpassword", ParameterValue:"mycoolpassword"}`). This starts a workflow to create the specified AWS resources. It also creates a record detail that tracks the provisioning request, and a provisioned product object that represents the underlying AWS resources.

1. The user polls [DescribeRecord](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_DescribeRecord.html) to see when the status of the record detail changes from the `IN_PROGRESS` state to a completed state (either `SUCCEEDED` or `ERROR`).

1. When the record detail for the request is in a completed state, the user calls [DescribeRecord](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_DescribeRecord.html) once more. The outputs identifies the created resources.

1. The user calls [UpdateProvisionedProduct](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_UpdateProvisionedProduct.html) to update the underlying resources in place. Depending on the specific updates requested, this operation can update with no interruption, with some interruption, or replace the provisioned product entirely.

1. Finally, the user calls [TerminateProvisionedProduct](https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_TerminateProvisionedProduct.html) to terminate the provisioned product.