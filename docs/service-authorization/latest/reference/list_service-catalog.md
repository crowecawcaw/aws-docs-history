

# Actions, resources, and condition keys for AWS Service Catalog
<a name="list_service-catalog"></a>

AWS Service Catalog (service prefix: `servicecatalog`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_Reference.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/permissions.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/servicecatalog/servicecatalog.json) for this service.

**Topics**
+ [API operations defined by AWS Service Catalog](#list_service-catalog-operations)
+ [Actions defined by AWS Service Catalog](#list_service-catalog-actions-as-permissions)
+ [Permission-only actions for AWS Service Catalog](#list_service-catalog-permission-only-actions)
+ [Resource types defined by AWS Service Catalog](#list_service-catalog-resources-for-iam-policies)
+ [Condition keys for AWS Service Catalog](#list_service-catalog-policy-keys)

## API operations defined by AWS Service Catalog
<a name="list_service-catalog-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_service-catalog-actions-as-permissions).




- **   AcceptPortfolioShare  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:AcceptPortfolioShare](#list_service-catalog-action-AcceptPortfolioShare) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateBudgetWithResource  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:AssociateBudgetWithResource](#list_service-catalog-action-AssociateBudgetWithResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociatePrincipalWithPortfolio  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:AssociatePrincipalWithPortfolio](#list_service-catalog-action-AssociatePrincipalWithPortfolio) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateProductWithPortfolio  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:AssociateProductWithPortfolio](#list_service-catalog-action-AssociateProductWithPortfolio) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateServiceActionWithProvisioningArtifact  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:AssociateServiceActionWithProvisioningArtifact](#list_service-catalog-action-AssociateServiceActionWithProvisioningArtifact) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateTagOptionWithResource  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:AssociateTagOptionWithResource](#list_service-catalog-action-AssociateTagOptionWithResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchAssociateServiceActionWithProvisioningArtifact  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:BatchAssociateServiceActionWithProvisioningArtifact](#list_service-catalog-action-BatchAssociateServiceActionWithProvisioningArtifact) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchDisassociateServiceActionFromProvisioningArtifact  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:BatchDisassociateServiceActionFromProvisioningArtifact](#list_service-catalog-action-BatchDisassociateServiceActionFromProvisioningArtifact) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CopyProduct  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:CopyProduct](#list_service-catalog-action-CopyProduct) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateConstraint  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:CreateConstraint](#list_service-catalog-action-CreateConstraint)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** servicecatalog.amazonaws.com / **Access level:** Write

- **   CreatePortfolio  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:CreatePortfolio](#list_service-catalog-action-CreatePortfolio)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [servicecatalog:TagResource](#list_service-catalog-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreatePortfolioShare  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:CreatePortfolioShare](#list_service-catalog-action-CreatePortfolioShare) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   CreateProduct  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:CreateProduct](#list_service-catalog-action-CreateProduct)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [servicecatalog:TagResource](#list_service-catalog-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [codestar-connections:PassConnection](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-passconnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   CreateProvisionedProductPlan  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:CreateProvisionedProductPlan](#list_service-catalog-action-CreateProvisionedProductPlan) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateProvisioningArtifact  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:CreateProvisioningArtifact](#list_service-catalog-action-CreateProvisioningArtifact) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateServiceAction  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:CreateServiceAction](#list_service-catalog-action-CreateServiceAction)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** servicecatalog.amazonaws.com / **Access level:** Write

- **   CreateTagOption  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:CreateTagOption](#list_service-catalog-action-CreateTagOption) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConstraint  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:DeleteConstraint](#list_service-catalog-action-DeleteConstraint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePortfolio  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:DeletePortfolio](#list_service-catalog-action-DeletePortfolio) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePortfolioShare  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:DeletePortfolioShare](#list_service-catalog-action-DeletePortfolioShare) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteProduct  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:DeleteProduct](#list_service-catalog-action-DeleteProduct) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteProvisionedProductPlan  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:DeleteProvisionedProductPlan](#list_service-catalog-action-DeleteProvisionedProductPlan) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteProvisioningArtifact  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:DeleteProvisioningArtifact](#list_service-catalog-action-DeleteProvisioningArtifact) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteServiceAction  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:DeleteServiceAction](#list_service-catalog-action-DeleteServiceAction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTagOption  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:DeleteTagOption](#list_service-catalog-action-DeleteTagOption) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeConstraint  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:DescribeConstraint](#list_service-catalog-action-DescribeConstraint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeCopyProductStatus  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:DescribeCopyProductStatus](#list_service-catalog-action-DescribeCopyProductStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribePortfolio  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:DescribePortfolio](#list_service-catalog-action-DescribePortfolio) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribePortfolioShareStatus  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:DescribePortfolioShareStatus](#list_service-catalog-action-DescribePortfolioShareStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribePortfolioShares  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:DescribePortfolioShares](#list_service-catalog-action-DescribePortfolioShares) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeProduct  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:DescribeProduct](#list_service-catalog-action-DescribeProduct) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeProductAsAdmin  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:DescribeProductAsAdmin](#list_service-catalog-action-DescribeProductAsAdmin) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeProductView  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:DescribeProductView](#list_service-catalog-action-DescribeProductView) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeProvisionedProduct  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:DescribeProvisionedProduct](#list_service-catalog-action-DescribeProvisionedProduct) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeProvisionedProductPlan  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:DescribeProvisionedProductPlan](#list_service-catalog-action-DescribeProvisionedProductPlan) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeProvisioningArtifact  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:DescribeProvisioningArtifact](#list_service-catalog-action-DescribeProvisioningArtifact) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeProvisioningParameters  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:DescribeProvisioningParameters](#list_service-catalog-action-DescribeProvisioningParameters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeRecord  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:DescribeRecord](#list_service-catalog-action-DescribeRecord) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeServiceAction  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:DescribeServiceAction](#list_service-catalog-action-DescribeServiceAction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeServiceActionExecutionParameters  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:DescribeServiceActionExecutionParameters](#list_service-catalog-action-DescribeServiceActionExecutionParameters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTagOption  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:DescribeTagOption](#list_service-catalog-action-DescribeTagOption) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DisableAWSOrganizationsAccess  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:DisableAWSOrganizationsAccess](#list_service-catalog-action-DisableAWSOrganizationsAccess) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateBudgetFromResource  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:DisassociateBudgetFromResource](#list_service-catalog-action-DisassociateBudgetFromResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociatePrincipalFromPortfolio  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:DisassociatePrincipalFromPortfolio](#list_service-catalog-action-DisassociatePrincipalFromPortfolio) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateProductFromPortfolio  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:DisassociateProductFromPortfolio](#list_service-catalog-action-DisassociateProductFromPortfolio) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateServiceActionFromProvisioningArtifact  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:DisassociateServiceActionFromProvisioningArtifact](#list_service-catalog-action-DisassociateServiceActionFromProvisioningArtifact) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateTagOptionFromResource  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:DisassociateTagOptionFromResource](#list_service-catalog-action-DisassociateTagOptionFromResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnableAWSOrganizationsAccess  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:EnableAWSOrganizationsAccess](#list_service-catalog-action-EnableAWSOrganizationsAccess) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ExecuteProvisionedProductPlan  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:ExecuteProvisionedProductPlan](#list_service-catalog-action-ExecuteProvisionedProductPlan) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ExecuteProvisionedProductServiceAction  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:ExecuteProvisionedProductServiceAction](#list_service-catalog-action-ExecuteProvisionedProductServiceAction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAWSOrganizationsAccessStatus  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:GetAWSOrganizationsAccessStatus](#list_service-catalog-action-GetAWSOrganizationsAccessStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetProvisionedProductOutputs  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:GetProvisionedProductOutputs](#list_service-catalog-action-GetProvisionedProductOutputs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ImportAsProvisionedProduct  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:ImportAsProvisionedProduct](#list_service-catalog-action-ImportAsProvisionedProduct) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListAcceptedPortfolioShares  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:ListAcceptedPortfolioShares](#list_service-catalog-action-ListAcceptedPortfolioShares) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListBudgetsForResource  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:ListBudgetsForResource](#list_service-catalog-action-ListBudgetsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListConstraintsForPortfolio  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:ListConstraintsForPortfolio](#list_service-catalog-action-ListConstraintsForPortfolio) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListLaunchPaths  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:ListLaunchPaths](#list_service-catalog-action-ListLaunchPaths) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListOrganizationPortfolioAccess  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:ListOrganizationPortfolioAccess](#list_service-catalog-action-ListOrganizationPortfolioAccess) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPortfolioAccess  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:ListPortfolioAccess](#list_service-catalog-action-ListPortfolioAccess) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPortfolios  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:ListPortfolios](#list_service-catalog-action-ListPortfolios) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPortfoliosForProduct  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:ListPortfoliosForProduct](#list_service-catalog-action-ListPortfoliosForProduct) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPrincipalsForPortfolio  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:ListPrincipalsForPortfolio](#list_service-catalog-action-ListPrincipalsForPortfolio) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListProvisionedProductPlans  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:ListProvisionedProductPlans](#list_service-catalog-action-ListProvisionedProductPlans) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListProvisioningArtifacts  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:ListProvisioningArtifacts](#list_service-catalog-action-ListProvisioningArtifacts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListProvisioningArtifactsForServiceAction  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:ListProvisioningArtifactsForServiceAction](#list_service-catalog-action-ListProvisioningArtifactsForServiceAction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRecordHistory  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:ListRecordHistory](#list_service-catalog-action-ListRecordHistory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListResourcesForTagOption  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:ListResourcesForTagOption](#list_service-catalog-action-ListResourcesForTagOption) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListServiceActions  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:ListServiceActions](#list_service-catalog-action-ListServiceActions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListServiceActionsForProvisioningArtifact  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:ListServiceActionsForProvisioningArtifact](#list_service-catalog-action-ListServiceActionsForProvisioningArtifact) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListStackInstancesForProvisionedProduct  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:ListStackInstancesForProvisionedProduct](#list_service-catalog-action-ListStackInstancesForProvisionedProduct) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagOptions  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:ListTagOptions](#list_service-catalog-action-ListTagOptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   NotifyProvisionProductEngineWorkflowResult  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:NotifyProvisionProductEngineWorkflowResult](#list_service-catalog-action-NotifyProvisionProductEngineWorkflowResult) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   NotifyTerminateProvisionedProductEngineWorkflowResult  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:NotifyTerminateProvisionedProductEngineWorkflowResult](#list_service-catalog-action-NotifyTerminateProvisionedProductEngineWorkflowResult) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   NotifyUpdateProvisionedProductEngineWorkflowResult  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:NotifyUpdateProvisionedProductEngineWorkflowResult](#list_service-catalog-action-NotifyUpdateProvisionedProductEngineWorkflowResult) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ProvisionProduct  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:ProvisionProduct](#list_service-catalog-action-ProvisionProduct) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RejectPortfolioShare  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:RejectPortfolioShare](#list_service-catalog-action-RejectPortfolioShare) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ScanProvisionedProducts  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:ScanProvisionedProducts](#list_service-catalog-action-ScanProvisionedProducts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   SearchProducts  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:SearchProducts](#list_service-catalog-action-SearchProducts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   SearchProductsAsAdmin  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:SearchProductsAsAdmin](#list_service-catalog-action-SearchProductsAsAdmin) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   SearchProvisionedProducts  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:SearchProvisionedProducts](#list_service-catalog-action-SearchProvisionedProducts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   TerminateProvisionedProduct  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:TerminateProvisionedProduct](#list_service-catalog-action-TerminateProvisionedProduct) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateConstraint  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:UpdateConstraint](#list_service-catalog-action-UpdateConstraint)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** servicecatalog.amazonaws.com / **Access level:** Write

- **   UpdatePortfolio  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:TagResource](#list_service-catalog-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [servicecatalog:UntagResource](#list_service-catalog-action-UntagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [servicecatalog:UpdatePortfolio](#list_service-catalog-action-UpdatePortfolio)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdatePortfolioShare  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:UpdatePortfolioShare](#list_service-catalog-action-UpdatePortfolioShare) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   UpdateProduct  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:TagResource](#list_service-catalog-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [servicecatalog:UntagResource](#list_service-catalog-action-UntagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [servicecatalog:UpdateProduct](#list_service-catalog-action-UpdateProduct)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [codestar-connections:PassConnection](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-passconnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   UpdateProvisionedProduct  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:UpdateProvisionedProduct](#list_service-catalog-action-UpdateProvisionedProduct) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateProvisionedProductProperties  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:UpdateProvisionedProductProperties](#list_service-catalog-action-UpdateProvisionedProductProperties) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateProvisioningArtifact  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:UpdateProvisioningArtifact](#list_service-catalog-action-UpdateProvisioningArtifact) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateServiceAction  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:UpdateServiceAction](#list_service-catalog-action-UpdateServiceAction)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** servicecatalog.amazonaws.com / **Access level:** Write

- **   UpdateTagOption  **
  - **SDK client:** servicecatalog
  - **IAM action:**  [servicecatalog:UpdateTagOption](#list_service-catalog-action-UpdateTagOption) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateAttributeGroup  **
  - **SDK client:** servicecatalog-appregistry
  - **IAM action:**  [servicecatalog:AssociateAttributeGroup](#list_service-catalog-action-AssociateAttributeGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateResource  **
  - **SDK client:** servicecatalog-appregistry
  - **IAM action:**  [servicecatalog:AssociateResource](#list_service-catalog-action-AssociateResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateApplication  **
  - **SDK client:** servicecatalog-appregistry
  - **IAM action:**  [servicecatalog:CreateApplication](#list_service-catalog-action-CreateApplication)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [servicecatalog:TagResource](#list_service-catalog-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateAttributeGroup  **
  - **SDK client:** servicecatalog-appregistry
  - **IAM action:**  [servicecatalog:CreateAttributeGroup](#list_service-catalog-action-CreateAttributeGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [servicecatalog:TagResource](#list_service-catalog-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteApplication  **
  - **SDK client:** servicecatalog-appregistry
  - **IAM action:**  [servicecatalog:DeleteApplication](#list_service-catalog-action-DeleteApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAttributeGroup  **
  - **SDK client:** servicecatalog-appregistry
  - **IAM action:**  [servicecatalog:DeleteAttributeGroup](#list_service-catalog-action-DeleteAttributeGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateAttributeGroup  **
  - **SDK client:** servicecatalog-appregistry
  - **IAM action:**  [servicecatalog:DisassociateAttributeGroup](#list_service-catalog-action-DisassociateAttributeGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateResource  **
  - **SDK client:** servicecatalog-appregistry
  - **IAM action:**  [servicecatalog:DisassociateResource](#list_service-catalog-action-DisassociateResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetApplication  **
  - **SDK client:** servicecatalog-appregistry
  - **IAM action:**  [servicecatalog:GetApplication](#list_service-catalog-action-GetApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAssociatedResource  **
  - **SDK client:** servicecatalog-appregistry
  - **IAM action:**  [servicecatalog:GetAssociatedResource](#list_service-catalog-action-GetAssociatedResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAttributeGroup  **
  - **SDK client:** servicecatalog-appregistry
  - **IAM action:**  [servicecatalog:GetAttributeGroup](#list_service-catalog-action-GetAttributeGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConfiguration  **
  - **SDK client:** servicecatalog-appregistry
  - **IAM action:**  [servicecatalog:GetConfiguration](#list_service-catalog-action-GetConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListApplications  **
  - **SDK client:** servicecatalog-appregistry
  - **IAM action:**  [servicecatalog:ListApplications](#list_service-catalog-action-ListApplications) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAssociatedAttributeGroups  **
  - **SDK client:** servicecatalog-appregistry
  - **IAM action:**  [servicecatalog:ListAssociatedAttributeGroups](#list_service-catalog-action-ListAssociatedAttributeGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAssociatedResources  **
  - **SDK client:** servicecatalog-appregistry
  - **IAM action:**  [servicecatalog:ListAssociatedResources](#list_service-catalog-action-ListAssociatedResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAttributeGroups  **
  - **SDK client:** servicecatalog-appregistry
  - **IAM action:**  [servicecatalog:ListAttributeGroups](#list_service-catalog-action-ListAttributeGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAttributeGroupsForApplication  **
  - **SDK client:** servicecatalog-appregistry
  - **IAM action:**  [servicecatalog:ListAttributeGroupsForApplication](#list_service-catalog-action-ListAttributeGroupsForApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **SDK client:** servicecatalog-appregistry
  - **IAM action:**  [servicecatalog:ListTagsForResource](#list_service-catalog-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutConfiguration  **
  - **SDK client:** servicecatalog-appregistry
  - **IAM action:**  [servicecatalog:PutConfiguration](#list_service-catalog-action-PutConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SyncResource  **
  - **SDK client:** servicecatalog-appregistry
  - **IAM action:**  [servicecatalog:SyncResource](#list_service-catalog-action-SyncResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **SDK client:** servicecatalog-appregistry
  - **IAM action:**  [servicecatalog:TagResource](#list_service-catalog-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **SDK client:** servicecatalog-appregistry
  - **IAM action:**  [servicecatalog:UntagResource](#list_service-catalog-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateApplication  **
  - **SDK client:** servicecatalog-appregistry
  - **IAM action:**  [servicecatalog:UpdateApplication](#list_service-catalog-action-UpdateApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateAttributeGroup  **
  - **SDK client:** servicecatalog-appregistry
  - **IAM action:**  [servicecatalog:UpdateAttributeGroup](#list_service-catalog-action-UpdateAttributeGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Service Catalog
<a name="list_service-catalog-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AcceptPortfolioShare](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_AcceptPortfolioShare.html)  **
  - **Description:** Grants permission to accept a portfolio that has been shared with you
  - **Resource types (\*required):** [Portfolio\*](#list_service-catalog-resource-Portfolio)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateAttributeGroup](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_AssociateAttributeGroup.html)  **
  - **Description:** Grants permission to associate an attribute group with an application
  - **Resource types (\*required):** [Application\*](#list_service-catalog-resource-Application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [AttributeGroup\*](#list_service-catalog-resource-AttributeGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateBudgetWithResource](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_AssociateBudgetWithResource.html)  **
  - **Description:** Grants permission to associate a budget with a resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [AssociatePrincipalWithPortfolio](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_AssociatePrincipalWithPortfolio.html)  **
  - **Description:** Grants permission to associate an IAM principal with a portfolio, giving the specified principal access to any products associated with the specified portfolio
  - **Resource types (\*required):** [Portfolio\*](#list_service-catalog-resource-Portfolio)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateProductWithPortfolio](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_AssociateProductWithPortfolio.html)  **
  - **Description:** Grants permission to associate a product with a portfolio
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [AssociateResource](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_AssociateResource.html)  **
  - **Description:** Grants permission to associate a resource with an application
  - **Resource types (\*required):** [Application\*](#list_service-catalog-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)<br />[servicecatalog:Resource](#list_service-catalog-servicecatalog_Resource)<br />[servicecatalog:ResourceType](#list_service-catalog-servicecatalog_ResourceType)
  - **Access level:** Write

- **   [AssociateServiceActionWithProvisioningArtifact](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_AssociateServiceActionWithProvisioningArtifact.html)  **
  - **Description:** Grants permission to associate an action with a provisioning artifact
  - **Resource types (\*required):** [Product\*](#list_service-catalog-resource-Product)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateTagOptionWithResource](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_AssociateTagOptionWithResource.html)  **
  - **Description:** Grants permission to associate the specified TagOption with the specified portfolio or product
  - **Resource types (\*required):** [Portfolio](#list_service-catalog-resource-Portfolio) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Product](#list_service-catalog-resource-Product) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchAssociateServiceActionWithProvisioningArtifact](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_BatchAssociateServiceActionWithProvisioningArtifact.html)  **
  - **Description:** Grants permission to associate multiple self-service actions with provisioning artifacts
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [BatchDisassociateServiceActionFromProvisioningArtifact](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_BatchDisassociateServiceActionFromProvisioningArtifact.html)  **
  - **Description:** Grants permission to disassociate a batch of self-service actions from the specified provisioning artifact
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CopyProduct](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_CopyProduct.html)  **
  - **Description:** Grants permission to copy the specified source product to the specified target product or a new product
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateApplication](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_CreateApplication.html)  **
  - **Description:** Grants permission to create an application
  - **Resource types (\*required):** [Application\*](#list_service-catalog-resource-Application)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_service-catalog-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_service-catalog-aws_TagKeys)
  - **Access level:** Write

- **   [CreateAttributeGroup](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_CreateAttributeGroup.html)  **
  - **Description:** Grants permission to create an attribute group
  - **Resource types (\*required):** [AttributeGroup\*](#list_service-catalog-resource-AttributeGroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_service-catalog-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_service-catalog-aws_TagKeys)
  - **Access level:** Write

- **   [CreateConstraint](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_CreateConstraint.html)  **
  - **Description:** Grants permission to create a constraint on an associated product and portfolio
  - **Resource types (\*required):** [Product\*](#list_service-catalog-resource-Product)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreatePortfolio](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_CreatePortfolio.html)  **
  - **Description:** Grants permission to create a portfolio
  - **Resource types (\*required):** [Portfolio\*](#list_service-catalog-resource-Portfolio)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_service-catalog-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_service-catalog-aws_TagKeys)
  - **Access level:** Write

- **   [CreatePortfolioShare](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_CreatePortfolioShare.html)  **
  - **Description:** Grants permission to share a portfolio you own with another AWS account
  - **Resource types (\*required):** [Portfolio\*](#list_service-catalog-resource-Portfolio)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [CreateProduct](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_CreateProduct.html)  **
  - **Description:** Grants permission to create a product and that product's first provisioning artifact
  - **Resource types (\*required):** [Product\*](#list_service-catalog-resource-Product)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_service-catalog-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_service-catalog-aws_TagKeys)
  - **Access level:** Write

- **   [CreateProvisionedProductPlan](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_CreateProvisionedProductPlan.html)  **
  - **Description:** Grants permission to add a new provisioned product plan
  - **Resource types (\*required):** 
  - **Condition keys:** [servicecatalog:accountLevel](#list_service-catalog-servicecatalog_accountLevel)<br />[servicecatalog:roleLevel](#list_service-catalog-servicecatalog_roleLevel)<br />[servicecatalog:userLevel](#list_service-catalog-servicecatalog_userLevel)
  - **Access level:** Write

- **   [CreateProvisioningArtifact](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_CreateProvisioningArtifact.html)  **
  - **Description:** Grants permission to add a new provisioning artifact to an existing product
  - **Resource types (\*required):** [Product\*](#list_service-catalog-resource-Product)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateServiceAction](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_CreateServiceAction.html)  **
  - **Description:** Grants permission to create a self-service action
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateTagOption](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_CreateTagOption.html)  **
  - **Description:** Grants permission to create a TagOption
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteApplication](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_DeleteApplication.html)  **
  - **Description:** Grants permission to delete an application if all associations have been removed from the application
  - **Resource types (\*required):** [Application\*](#list_service-catalog-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAttributeGroup](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_DeleteAttributeGroup.html)  **
  - **Description:** Grants permission to delete an attribute group if all associations have been removed from the attribute group
  - **Resource types (\*required):** [AttributeGroup\*](#list_service-catalog-resource-AttributeGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteConstraint](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DeleteConstraint.html)  **
  - **Description:** Grants permission to remove and delete an existing constraint from an associated product and portfolio
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeletePortfolio](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DeletePortfolio.html)  **
  - **Description:** Grants permission to delete a portfolio if all associations and shares have been removed from the portfolio
  - **Resource types (\*required):** [Portfolio\*](#list_service-catalog-resource-Portfolio)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePortfolioShare](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DeletePortfolioShare.html)  **
  - **Description:** Grants permission to unshare a portfolio you own from an AWS account you previously shared the portfolio with
  - **Resource types (\*required):** [Portfolio\*](#list_service-catalog-resource-Portfolio)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [DeleteProduct](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DeleteProduct.html)  **
  - **Description:** Grants permission to delete a product if all associations have been removed from the product
  - **Resource types (\*required):** [Product\*](#list_service-catalog-resource-Product)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteProvisionedProductPlan](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DeleteProvisionedProductPlan.html)  **
  - **Description:** Grants permission to delete a provisioned product plan
  - **Resource types (\*required):** 
  - **Condition keys:** [servicecatalog:accountLevel](#list_service-catalog-servicecatalog_accountLevel)<br />[servicecatalog:roleLevel](#list_service-catalog-servicecatalog_roleLevel)<br />[servicecatalog:userLevel](#list_service-catalog-servicecatalog_userLevel)
  - **Access level:** Write

- **   [DeleteProvisioningArtifact](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DeleteProvisioningArtifact.html)  **
  - **Description:** Grants permission to delete a provisioning artifact from a product
  - **Resource types (\*required):** [Product\*](#list_service-catalog-resource-Product)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteServiceAction](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DeleteServiceAction.html)  **
  - **Description:** Grants permission to delete a self-service action
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteTagOption](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DeleteTagOption.html)  **
  - **Description:** Grants permission to delete the specified TagOption
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DescribeConstraint](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DescribeConstraint.html)  **
  - **Description:** Grants permission to describe a constraint
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeCopyProductStatus](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DescribeCopyProductStatus.html)  **
  - **Description:** Grants permission to get the status of the specified copy product operation
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribePortfolio](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DescribePortfolio.html)  **
  - **Description:** Grants permission to describe a portfolio
  - **Resource types (\*required):** [Portfolio\*](#list_service-catalog-resource-Portfolio)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribePortfolioShareStatus](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DescribePortfolioShareStatus.html)  **
  - **Description:** Grants permission to get the status of the specified portfolio share operation
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribePortfolioShares](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DescribePortfolioShares.html)  **
  - **Description:** Grants permission to view a summary of each of the portfolio shares that were created for the specified portfolio
  - **Resource types (\*required):** [Portfolio\*](#list_service-catalog-resource-Portfolio)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [DescribeProduct](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DescribeProduct.html)  **
  - **Description:** Grants permission to describe a product as an end-user
  - **Resource types (\*required):** [Product\*](#list_service-catalog-resource-Product)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeProductAsAdmin](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DescribeProductAsAdmin.html)  **
  - **Description:** Grants permission to describe a product as an admin
  - **Resource types (\*required):** [Product\*](#list_service-catalog-resource-Product)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeProductView](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DescribeProductView.html)  **
  - **Description:** Grants permission to describe a product as an end-user
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeProvisionedProduct](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DescribeProvisionedProduct.html)  **
  - **Description:** Grants permission to describe a provisioned product
  - **Resource types (\*required):** 
  - **Condition keys:** [servicecatalog:accountLevel](#list_service-catalog-servicecatalog_accountLevel)<br />[servicecatalog:roleLevel](#list_service-catalog-servicecatalog_roleLevel)<br />[servicecatalog:userLevel](#list_service-catalog-servicecatalog_userLevel)
  - **Access level:** Read

- **   [DescribeProvisionedProductPlan](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DescribeProvisionedProductPlan.html)  **
  - **Description:** Grants permission to describe a provisioned product plan
  - **Resource types (\*required):** 
  - **Condition keys:** [servicecatalog:accountLevel](#list_service-catalog-servicecatalog_accountLevel)<br />[servicecatalog:roleLevel](#list_service-catalog-servicecatalog_roleLevel)<br />[servicecatalog:userLevel](#list_service-catalog-servicecatalog_userLevel)
  - **Access level:** Read

- **   [DescribeProvisioningArtifact](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DescribeProvisioningArtifact.html)  **
  - **Description:** Grants permission to describe a provisioning artifact
  - **Resource types (\*required):** [Product\*](#list_service-catalog-resource-Product)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeProvisioningParameters](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DescribeProvisioningParameters.html)  **
  - **Description:** Grants permission to describe the parameters that you need to specify to successfully provision a specified provisioning artifact
  - **Resource types (\*required):** [Product\*](#list_service-catalog-resource-Product)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeRecord](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DescribeRecord.html)  **
  - **Description:** Grants permission to describe a record and lists any outputs
  - **Resource types (\*required):** 
  - **Condition keys:** [servicecatalog:accountLevel](#list_service-catalog-servicecatalog_accountLevel)<br />[servicecatalog:roleLevel](#list_service-catalog-servicecatalog_roleLevel)<br />[servicecatalog:userLevel](#list_service-catalog-servicecatalog_userLevel)
  - **Access level:** Read

- **   [DescribeServiceAction](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DescribeServiceAction.html)  **
  - **Description:** Grants permission to describe a self-service action
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeServiceActionExecutionParameters](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DescribeServiceActionExecutionParameters.html)  **
  - **Description:** Grants permission to get the default parameters if you executed the specified Service Action on the specified Provisioned Product
  - **Resource types (\*required):** 
  - **Condition keys:** [servicecatalog:accountLevel](#list_service-catalog-servicecatalog_accountLevel)<br />[servicecatalog:roleLevel](#list_service-catalog-servicecatalog_roleLevel)<br />[servicecatalog:userLevel](#list_service-catalog-servicecatalog_userLevel)
  - **Access level:** Read

- **   [DescribeTagOption](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DescribeTagOption.html)  **
  - **Description:** Grants permission to get information about the specified TagOption
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DisableAWSOrganizationsAccess](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DisableAWSOrganizationsAccess.html)  **
  - **Description:** Grants permission to disable portfolio sharing through AWS Organizations feature
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DisassociateAttributeGroup](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_DisassociateAttributeGroup.html)  **
  - **Description:** Grants permission to disassociate an attribute group from an application
  - **Resource types (\*required):** [Application\*](#list_service-catalog-resource-Application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [AttributeGroup\*](#list_service-catalog-resource-AttributeGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateBudgetFromResource](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DisassociateBudgetFromResource.html)  **
  - **Description:** Grants permission to disassociate a budget from a resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DisassociatePrincipalFromPortfolio](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DisassociatePrincipalFromPortfolio.html)  **
  - **Description:** Grants permission to disassociate an IAM principal from a portfolio
  - **Resource types (\*required):** [Portfolio\*](#list_service-catalog-resource-Portfolio)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateProductFromPortfolio](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DisassociateProductFromPortfolio.html)  **
  - **Description:** Grants permission to disassociate a product from a portfolio
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DisassociateResource](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_DisassociateResource.html)  **
  - **Description:** Grants permission to disassociate a resource from an application
  - **Resource types (\*required):** [Application\*](#list_service-catalog-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)<br />[servicecatalog:Resource](#list_service-catalog-servicecatalog_Resource)<br />[servicecatalog:ResourceType](#list_service-catalog-servicecatalog_ResourceType)
  - **Access level:** Write

- **   [DisassociateServiceActionFromProvisioningArtifact](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DisassociateServiceActionFromProvisioningArtifact.html)  **
  - **Description:** Grants permission to disassociate the specified self-service action association from the specified provisioning artifact
  - **Resource types (\*required):** [Product\*](#list_service-catalog-resource-Product)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateTagOptionFromResource](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DisassociateTagOptionFromResource.html)  **
  - **Description:** Grants permission to disassociate the specified TagOption from the specified resource
  - **Resource types (\*required):** [Portfolio](#list_service-catalog-resource-Portfolio) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Product](#list_service-catalog-resource-Product) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [EnableAWSOrganizationsAccess](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_EnableAWSOrganizationsAccess.html)  **
  - **Description:** Grants permission to enable portfolio sharing feature through AWS Organizations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ExecuteProvisionedProductPlan](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ExecuteProvisionedProductPlan.html)  **
  - **Description:** Grants permission to execute a provisioned product plan
  - **Resource types (\*required):** 
  - **Condition keys:** [servicecatalog:accountLevel](#list_service-catalog-servicecatalog_accountLevel)<br />[servicecatalog:roleLevel](#list_service-catalog-servicecatalog_roleLevel)<br />[servicecatalog:userLevel](#list_service-catalog-servicecatalog_userLevel)
  - **Access level:** Write

- **   [ExecuteProvisionedProductServiceAction](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ExecuteProvisionedProductServiceAction.html)  **
  - **Description:** Grants permission to executes a provisioned product plan
  - **Resource types (\*required):** 
  - **Condition keys:** [servicecatalog:accountLevel](#list_service-catalog-servicecatalog_accountLevel)<br />[servicecatalog:roleLevel](#list_service-catalog-servicecatalog_roleLevel)<br />[servicecatalog:userLevel](#list_service-catalog-servicecatalog_userLevel)
  - **Access level:** Write

- **   [GetAWSOrganizationsAccessStatus](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_GetAWSOrganizationsAccessStatus.html)  **
  - **Description:** Grants permission to get the access status of AWS Organization portfolio share feature
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetApplication](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_GetApplication.html)  **
  - **Description:** Grants permission to get an application
  - **Resource types (\*required):** [Application\*](#list_service-catalog-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAssociatedResource](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_GetAssociatedResource.html)  **
  - **Description:** Grants permission to get information about a resource associated to an application
  - **Resource types (\*required):** [Application\*](#list_service-catalog-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)<br />[servicecatalog:Resource](#list_service-catalog-servicecatalog_Resource)<br />[servicecatalog:ResourceType](#list_service-catalog-servicecatalog_ResourceType)
  - **Access level:** Read

- **   [GetAttributeGroup](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_GetAttributeGroup.html)  **
  - **Description:** Grants permission to get an attribute group
  - **Resource types (\*required):** [AttributeGroup\*](#list_service-catalog-resource-AttributeGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetConfiguration](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_GetConfiguration.html)  **
  - **Description:** Grants permission to read AppRegistry configurations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetProvisionedProductOutputs](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_GetProvisionedProductOutputs.html)  **
  - **Description:** Grants permission to get the provisioned product output with either provisioned product id or name
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ImportAsProvisionedProduct](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ImportAsProvisionedProduct.html)  **
  - **Description:** Grants permission to import a resource into a provisioned product
  - **Resource types (\*required):** [Product\*](#list_service-catalog-resource-Product)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ListAcceptedPortfolioShares](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ListAcceptedPortfolioShares.html)  **
  - **Description:** Grants permission to list the portfolios that have been shared with you and you have accepted
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListApplications](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_ListApplications.html)  **
  - **Description:** Grants permission to list your applications
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAssociatedAttributeGroups](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_ListAssociatedAttributeGroups.html)  **
  - **Description:** Grants permission to list the attribute groups associated with an application
  - **Resource types (\*required):** [Application\*](#list_service-catalog-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAssociatedResources](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_ListAssociatedResources.html)  **
  - **Description:** Grants permission to list the resources associated with an application
  - **Resource types (\*required):** [Application\*](#list_service-catalog-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAttributeGroups](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_ListAttributeGroups.html)  **
  - **Description:** Grants permission to list your attribute groups
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAttributeGroupsForApplication](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_ListAttributeGroupsForApplication.html)  **
  - **Description:** Grants permission to list the associated attribute groups for a given application
  - **Resource types (\*required):** [Application\*](#list_service-catalog-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListBudgetsForResource](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ListBudgetsForResource.html)  **
  - **Description:** Grants permission to list all the budgets associated to a resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListConstraintsForPortfolio](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ListConstraintsForPortfolio.html)  **
  - **Description:** Grants permission to list constraints associated with a given portfolio
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListLaunchPaths](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ListLaunchPaths.html)  **
  - **Description:** Grants permission to list the different ways to launch a given product as an end-user
  - **Resource types (\*required):** [Product\*](#list_service-catalog-resource-Product)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListOrganizationPortfolioAccess](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ListOrganizationPortfolioAccess.html)  **
  - **Description:** Grants permission to list the organization nodes that have access to the specified portfolio
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPortfolioAccess](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ListPortfolioAccess.html)  **
  - **Description:** Grants permission to list the AWS accounts you have shared a given portfolio with
  - **Resource types (\*required):** [Portfolio\*](#list_service-catalog-resource-Portfolio)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListPortfolios](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ListPortfolios.html)  **
  - **Description:** Grants permission to list the portfolios in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPortfoliosForProduct](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ListPortfoliosForProduct.html)  **
  - **Description:** Grants permission to list the portfolios associated with a given product
  - **Resource types (\*required):** [Product\*](#list_service-catalog-resource-Product)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListPrincipalsForPortfolio](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ListPrincipalsForPortfolio.html)  **
  - **Description:** Grants permission to list the IAM principals associated with a given portfolio
  - **Resource types (\*required):** [Portfolio\*](#list_service-catalog-resource-Portfolio)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListProvisionedProductPlans](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ListProvisionedProductPlans.html)  **
  - **Description:** Grants permission to list the provisioned product plans
  - **Resource types (\*required):** 
  - **Condition keys:** [servicecatalog:accountLevel](#list_service-catalog-servicecatalog_accountLevel)<br />[servicecatalog:roleLevel](#list_service-catalog-servicecatalog_roleLevel)<br />[servicecatalog:userLevel](#list_service-catalog-servicecatalog_userLevel)
  - **Access level:** List

- **   [ListProvisioningArtifacts](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ListProvisioningArtifacts.html)  **
  - **Description:** Grants permission to list the provisioning artifacts associated with a given product
  - **Resource types (\*required):** [Product\*](#list_service-catalog-resource-Product)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListProvisioningArtifactsForServiceAction](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ListProvisioningArtifactsForServiceAction.html)  **
  - **Description:** Grants permission to list all provisioning artifacts for the specified self-service action
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRecordHistory](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ListRecordHistory.html)  **
  - **Description:** Grants permission to list all the records in your account or all the records related to a given provisioned product
  - **Resource types (\*required):** 
  - **Condition keys:** [servicecatalog:accountLevel](#list_service-catalog-servicecatalog_accountLevel)<br />[servicecatalog:roleLevel](#list_service-catalog-servicecatalog_roleLevel)<br />[servicecatalog:userLevel](#list_service-catalog-servicecatalog_userLevel)
  - **Access level:** List

- **   [ListResourcesForTagOption](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ListResourcesForTagOption.html)  **
  - **Description:** Grants permission to list the resources associated with the specified TagOption
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListServiceActions](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ListServiceActions.html)  **
  - **Description:** Grants permission to list all self-service actions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListServiceActionsForProvisioningArtifact](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ListServiceActionsForProvisioningArtifact.html)  **
  - **Description:** Grants permission to list all the service actions associated with the specified provisioning artifact in your account
  - **Resource types (\*required):** [Product\*](#list_service-catalog-resource-Product)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)<br />[servicecatalog:accountLevel](#list_service-catalog-servicecatalog_accountLevel)<br />[servicecatalog:roleLevel](#list_service-catalog-servicecatalog_roleLevel)<br />[servicecatalog:userLevel](#list_service-catalog-servicecatalog_userLevel)
  - **Access level:** List

- **   [ListStackInstancesForProvisionedProduct](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ListStackInstancesForProvisionedProduct.html)  **
  - **Description:** Grants permission to list account, region and status of each stack instances that are associated with a CFN\_STACKSET type provisioned product
  - **Resource types (\*required):** 
  - **Condition keys:** [servicecatalog:accountLevel](#list_service-catalog-servicecatalog_accountLevel)<br />[servicecatalog:roleLevel](#list_service-catalog-servicecatalog_roleLevel)<br />[servicecatalog:userLevel](#list_service-catalog-servicecatalog_userLevel)
  - **Access level:** List

- **   [ListTagOptions](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ListTagOptions.html)  **
  - **Description:** Grants permission to list the specified TagOptions or all TagOptions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the tags for a service catalog appregistry resource
  - **Resource types (\*required):** [Application](#list_service-catalog-resource-Application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [AttributeGroup](#list_service-catalog-resource-AttributeGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [NotifyProvisionProductEngineWorkflowResult](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_NotifyProvisionProductEngineWorkflowResult.html)  **
  - **Description:** Grants permission to notify the result of the provisioning engine execution
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [NotifyTerminateProvisionedProductEngineWorkflowResult](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_NotifyTerminateProvisionedProductEngineWorkflowResult.html)  **
  - **Description:** Grants permission to notify the result of the terminate engine execution
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [NotifyUpdateProvisionedProductEngineWorkflowResult](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_NotifyUpdateProvisionedProductEngineWorkflowResult.html)  **
  - **Description:** Grants permission to notify the result of the update engine execution
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ProvisionProduct](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ProvisionProduct.html)  **
  - **Description:** Grants permission to provision a product with a specified provisioning artifact and launch parameters
  - **Resource types (\*required):** [Product\*](#list_service-catalog-resource-Product)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutConfiguration](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_PutConfiguration.html)  **
  - **Description:** Grants permission to assign AppRegistry configurations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [RejectPortfolioShare](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_RejectPortfolioShare.html)  **
  - **Description:** Grants permission to reject a portfolio that has been shared with you that you previously accepted
  - **Resource types (\*required):** [Portfolio\*](#list_service-catalog-resource-Portfolio)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ScanProvisionedProducts](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ScanProvisionedProducts.html)  **
  - **Description:** Grants permission to list all the provisioned products in your account
  - **Resource types (\*required):** 
  - **Condition keys:** [servicecatalog:accountLevel](#list_service-catalog-servicecatalog_accountLevel)<br />[servicecatalog:roleLevel](#list_service-catalog-servicecatalog_roleLevel)<br />[servicecatalog:userLevel](#list_service-catalog-servicecatalog_userLevel)
  - **Access level:** List

- **   [SearchProducts](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_SearchProducts.html)  **
  - **Description:** Grants permission to list the products available to you as an end-user
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [SearchProductsAsAdmin](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_SearchProductsAsAdmin.html)  **
  - **Description:** Grants permission to list all the products in your account or all the products associated with a given portfolio
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [SearchProvisionedProducts](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_SearchProvisionedProducts.html)  **
  - **Description:** Grants permission to list all the provisioned products in your account
  - **Resource types (\*required):** 
  - **Condition keys:** [servicecatalog:accountLevel](#list_service-catalog-servicecatalog_accountLevel)<br />[servicecatalog:roleLevel](#list_service-catalog-servicecatalog_roleLevel)<br />[servicecatalog:userLevel](#list_service-catalog-servicecatalog_userLevel)
  - **Access level:** List

- **   [SyncResource](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_SyncResource.html)  **
  - **Description:** Grants permission to sync a resource with its current state in AppRegistry
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_TagResource.html)  **
  - **Description:** Grants permission to tag a service catalog appregistry resource
  - **Resource types (\*required):** [Application](#list_service-catalog-resource-Application) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_service-catalog-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_service-catalog-aws_TagKeys)
  - **Resource types (\*required):** [AttributeGroup](#list_service-catalog-resource-AttributeGroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_service-catalog-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_service-catalog-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [TerminateProvisionedProduct](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_TerminateProvisionedProduct.html)  **
  - **Description:** Grants permission to terminate an existing provisioned product
  - **Resource types (\*required):** 
  - **Condition keys:** [servicecatalog:accountLevel](#list_service-catalog-servicecatalog_accountLevel)<br />[servicecatalog:roleLevel](#list_service-catalog-servicecatalog_roleLevel)<br />[servicecatalog:userLevel](#list_service-catalog-servicecatalog_userLevel)
  - **Access level:** Write

- **   [UntagResource](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_UntagResource.html)  **
  - **Description:** Grants permission to remove a tag from a service catalog appregistry resource
  - **Resource types (\*required):** [Application](#list_service-catalog-resource-Application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_service-catalog-aws_TagKeys)
  - **Resource types (\*required):** [AttributeGroup](#list_service-catalog-resource-AttributeGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_service-catalog-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateApplication](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_UpdateApplication.html)  **
  - **Description:** Grants permission to update the attributes of an existing application
  - **Resource types (\*required):** [Application\*](#list_service-catalog-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAttributeGroup](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_UpdateAttributeGroup.html)  **
  - **Description:** Grants permission to update the attributes of an existing attribute group
  - **Resource types (\*required):** [AttributeGroup\*](#list_service-catalog-resource-AttributeGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateConstraint](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_UpdateConstraint.html)  **
  - **Description:** Grants permission to update the metadata fields of an existing constraint
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdatePortfolio](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_UpdatePortfolio.html)  **
  - **Description:** Grants permission to update the metadata fields and/or tags of an existing portfolio
  - **Resource types (\*required):** [Portfolio\*](#list_service-catalog-resource-Portfolio)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_service-catalog-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_service-catalog-aws_TagKeys)
  - **Access level:** Write

- **   [UpdatePortfolioShare](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_UpdatePortfolioShare.html)  **
  - **Description:** Grants permission to enable or disable resource sharing for an existing portfolio share
  - **Resource types (\*required):** [Portfolio\*](#list_service-catalog-resource-Portfolio)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [UpdateProduct](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_UpdateProduct.html)  **
  - **Description:** Grants permission to update the metadata fields and/or tags of an existing product
  - **Resource types (\*required):** [Product\*](#list_service-catalog-resource-Product)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_service-catalog-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_service-catalog-aws_TagKeys)
  - **Access level:** Write

- **   [UpdateProvisionedProduct](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_UpdateProvisionedProduct.html)  **
  - **Description:** Grants permission to update an existing provisioned product
  - **Resource types (\*required):** 
  - **Condition keys:** [servicecatalog:accountLevel](#list_service-catalog-servicecatalog_accountLevel)<br />[servicecatalog:roleLevel](#list_service-catalog-servicecatalog_roleLevel)<br />[servicecatalog:userLevel](#list_service-catalog-servicecatalog_userLevel)
  - **Access level:** Write

- **   [UpdateProvisionedProductProperties](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_UpdateProvisionedProductProperties.html)  **
  - **Description:** Grants permission to update the properties of an existing provisioned product
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateProvisioningArtifact](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_UpdateProvisioningArtifact.html)  **
  - **Description:** Grants permission to update the metadata fields of an existing provisioning artifact
  - **Resource types (\*required):** [Product\*](#list_service-catalog-resource-Product)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateServiceAction](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_UpdateServiceAction.html)  **
  - **Description:** Grants permission to update a self-service action
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateTagOption](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_UpdateTagOption.html)  **
  - **Description:** Grants permission to update the specified TagOption
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write



## Permission-only actions for AWS Service Catalog
<a name="list_service-catalog-permission-only-actions"></a>

The following actions are defined by AWS Service Catalog but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [DeleteResourcePolicy](https://docs.aws.amazon.com/servicecatalog/latest/arguide/sharing-definitions.html)  **
  - **Description:** Grants permission to delete a resource-based policy for the specified resource
  - **Resource types (\*required):** [Application](#list_service-catalog-resource-Application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [AttributeGroup](#list_service-catalog-resource-AttributeGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetResourcePolicy](https://docs.aws.amazon.com/servicecatalog/latest/arguide/sharing-definitions.html)  **
  - **Description:** Grants permission to get a resource-based policy for the specified resource
  - **Resource types (\*required):** [Application](#list_service-catalog-resource-Application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [AttributeGroup](#list_service-catalog-resource-AttributeGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PutResourcePolicy](https://docs.aws.amazon.com/servicecatalog/latest/arguide/sharing-definitions.html)  **
  - **Description:** Grants permission to add a resource-based policy for the specified resource
  - **Resource types (\*required):** [Application](#list_service-catalog-resource-Application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [AttributeGroup](#list_service-catalog-resource-AttributeGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS Service Catalog
<a name="list_service-catalog-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [Application](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_CreateApplication.html)  | arn:${Partition}:servicecatalog:${Region}:${Account}:/applications/${ApplicationId} | [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_) | 
|  [AttributeGroup](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_CreateAttributeGroup.html)  | arn:${Partition}:servicecatalog:${Region}:${Account}:/attribute-groups/${AttributeGroupId} | [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_) | 
|  [Portfolio](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_PortfolioDetail.html)  | arn:${Partition}:catalog:${Region}:${Account}:portfolio/${PortfolioId} | [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_) | 
|  [Product](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ProductViewDetail.html)  | arn:${Partition}:catalog:${Region}:${Account}:product/${ProductId} | [aws:ResourceTag/${TagKey}](#list_service-catalog-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Service Catalog
<a name="list_service-catalog-policy-keys"></a>

AWS Service Catalog defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of tag keys in the request | ArrayOfString | 
|   [servicecatalog:Resource](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/permissions-examples.html)  | Filters access by controlling what value can be specified as the Resource parameter in an AppRegistry associate resource API | String | 
|   [servicecatalog:ResourceType](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/permissions-examples.html)  | Filters access by controlling what value can be specified as the ResourceType parameter in an AppRegistry associate resource API | String | 
|   [servicecatalog:accountLevel](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/permissions-examples.html)  | Filters access by user to see and perform actions on resources created by anyone in the account | String | 
|   [servicecatalog:roleLevel](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/permissions-examples.html)  | Filters access by user to see and perform actions on resources created either by them or by anyone federating into the same role as them | String | 
|   [servicecatalog:userLevel](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/permissions-examples.html)  | Filters access by user to see and perform actions on only resources that they created | String | 