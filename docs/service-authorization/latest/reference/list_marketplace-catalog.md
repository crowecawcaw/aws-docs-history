

# Actions, resources, and condition keys for AWS Marketplace Catalog
<a name="list_marketplace-catalog"></a>

AWS Marketplace Catalog (service prefix: `aws-marketplace`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/api-access-control.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/aws-marketplace/aws-marketplace.json) for this service.

**Topics**
+ [API operations defined by AWS Marketplace Catalog](#list_marketplace-catalog-operations)
+ [Actions defined by AWS Marketplace Catalog](#list_marketplace-catalog-actions-as-permissions)
+ [Resource types defined by AWS Marketplace Catalog](#list_marketplace-catalog-resources-for-iam-policies)
+ [Condition keys for AWS Marketplace Catalog](#list_marketplace-catalog-policy-keys)

## API operations defined by AWS Marketplace Catalog
<a name="list_marketplace-catalog-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_marketplace-catalog-actions-as-permissions).




- **   BatchDescribeEntities  **
  - **IAM action:**  [aws-marketplace:DescribeEntity](#list_marketplace-catalog-action-DescribeEntity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   CancelChangeSet  **
  - **IAM action:**  [aws-marketplace:CancelChangeSet](#list_marketplace-catalog-action-CancelChangeSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteResourcePolicy  **
  - **IAM action:**  [aws-marketplace:DeleteResourcePolicy](#list_marketplace-catalog-action-DeleteResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DescribeAssessment  **
  - **IAM action:**  [aws-marketplace:DescribeAssessment](#list_marketplace-catalog-action-DescribeAssessment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeChangeSet  **
  - **IAM action:**  [aws-marketplace:DescribeChangeSet](#list_marketplace-catalog-action-DescribeChangeSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEntity  **
  - **IAM action:**  [aws-marketplace:DescribeEntity](#list_marketplace-catalog-action-DescribeEntity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourcePolicy  **
  - **IAM action:**  [aws-marketplace:GetResourcePolicy](#list_marketplace-catalog-action-GetResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAssessments  **
  - **IAM action:**  [aws-marketplace:ListAssessments](#list_marketplace-catalog-action-ListAssessments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListChangeSets  **
  - **IAM action:**  [aws-marketplace:ListChangeSets](#list_marketplace-catalog-action-ListChangeSets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEntities  **
  - **IAM action:**  [aws-marketplace:DescribeEntity](#list_marketplace-catalog-action-DescribeEntity)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [aws-marketplace:ListEntities](#list_marketplace-catalog-action-ListEntities)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [aws-marketplace:ListTagsForResource](#list_marketplace-catalog-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutResourcePolicy  **
  - **IAM action:**  [aws-marketplace:PutResourcePolicy](#list_marketplace-catalog-action-PutResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   StartChangeSet  **
  - **IAM action:**  [aws-marketplace:DescribeAgreement](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-iam-users-groups-policies.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [aws-marketplace:DescribeChangeSet](#list_marketplace-catalog-action-DescribeChangeSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [aws-marketplace:DescribeEntity](#list_marketplace-catalog-action-DescribeEntity)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [aws-marketplace:GetAgreementTerms](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-iam-users-groups-policies.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [aws-marketplace:StartChangeSet](#list_marketplace-catalog-action-StartChangeSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [aws-marketplace:TagResource](#list_marketplace-catalog-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [dataexchange:PublishDataSet](https://docs.aws.amazon.com/data-exchange/latest/userguide/api-permissions-ref.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** assets.marketplace.amazonaws.com / **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [aws-marketplace:TagResource](#list_marketplace-catalog-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [aws-marketplace:UntagResource](#list_marketplace-catalog-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write



## Actions defined by AWS Marketplace Catalog
<a name="list_marketplace-catalog-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CancelChangeSet](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_CancelChangeSet.html)  **
  - **Description:** Grants permission to cancel a running change set
  - **Resource types (\*required):** [ChangeSet\*](#list_marketplace-catalog-resource-ChangeSet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_marketplace-catalog-aws_ResourceTag___TagKey_)<br />[catalog:ChangeType](#list_marketplace-catalog-catalog_ChangeType)
  - **Access level:** Write

- **   [CreateVerificationEvidence](https://docs.aws.amazon.com/marketplace/latest/APIReference/compliance-api-access-control.html)  **
  - **Description:** Grants permission to create a new verification evidence resource for BusinessVerification
  - **Resource types (\*required):** [VerificationEvidence\*](#list_marketplace-catalog-resource-VerificationEvidence)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_marketplace-catalog-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_marketplace-catalog-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_marketplace-catalog-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteResourcePolicy](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_DeleteResourcePolicy.html)  **
  - **Description:** Grants permission to delete the resource policy of an existing entity
  - **Resource types (\*required):** [Entity\*](#list_marketplace-catalog-resource-Entity)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_marketplace-catalog-aws_ResourceTag___TagKey_)<br />[catalog:ChangeType](#list_marketplace-catalog-catalog_ChangeType)
  - **Access level:** Permissions management, Write

- **   [DescribeAssessment](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_DescribeAssessment.html)  **
  - **Description:** Grants permission to return the details of an existing assessment
  - **Resource types (\*required):** [Assessment](#list_marketplace-catalog-resource-Assessment)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeChangeSet](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_DescribeChangeSet.html)  **
  - **Description:** Grants permission to return the details of an existing change set
  - **Resource types (\*required):** [ChangeSet\*](#list_marketplace-catalog-resource-ChangeSet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_marketplace-catalog-aws_ResourceTag___TagKey_)<br />[catalog:ChangeType](#list_marketplace-catalog-catalog_ChangeType)
  - **Access level:** Read

- **   [DescribeEntity](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_DescribeEntity.html)  **
  - **Description:** Grants permission to return the details of an existing entity
  - **Resource types (\*required):** [Entity\*](#list_marketplace-catalog-resource-Entity)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_marketplace-catalog-aws_ResourceTag___TagKey_)<br />[catalog:ChangeType](#list_marketplace-catalog-catalog_ChangeType)
  - **Access level:** Read

- **   [GetInvoiceSubmissionTask](https://docs.aws.amazon.com/marketplace/latest/APIReference/compliance-api-access-control.html)  **
  - **Description:** Grants permission to retrieve details of an existing invoice submission task
  - **Resource types (\*required):** [InvoiceSubmissionTask\*](#list_marketplace-catalog-resource-InvoiceSubmissionTask)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_marketplace-catalog-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetIssuedTaxInvoice](https://docs.aws.amazon.com/marketplace/latest/APIReference/compliance-api-access-control.html)  **
  - **Description:** Grants permission to retrieve details of a specific tax invoice issued by AWS on behalf of a seller
  - **Resource types (\*required):** [IssuedTaxInvoice\*](#list_marketplace-catalog-resource-IssuedTaxInvoice)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_marketplace-catalog-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetResourcePolicy](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_GetResourcePolicy.html)  **
  - **Description:** Grants permission to get the resource policy of an existing entity
  - **Resource types (\*required):** [Entity\*](#list_marketplace-catalog-resource-Entity)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_marketplace-catalog-aws_ResourceTag___TagKey_)<br />[catalog:ChangeType](#list_marketplace-catalog-catalog_ChangeType)
  - **Access level:** Read

- **   [GetTaxComplianceProfile](https://docs.aws.amazon.com/marketplace/latest/APIReference/compliance-api-access-control.html)  **
  - **Description:** Grants permission to retrieve details of a tax compliance profile including artifacts with download URLs
  - **Resource types (\*required):** [TaxComplianceProfile\*](#list_marketplace-catalog-resource-TaxComplianceProfile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_marketplace-catalog-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetVerification](https://docs.aws.amazon.com/marketplace/latest/APIReference/compliance-api-access-control.html)  **
  - **Description:** Grants permission to retrieve the detailed status of a specific verification process, including PSP validation results
  - **Resource types (\*required):** 
  - **Condition keys:** [aws-marketplace:VerificationType](#list_marketplace-catalog-aws-marketplace_VerificationType)
  - **Access level:** Read

- **   [GetVerificationEvidence](https://docs.aws.amazon.com/marketplace/latest/APIReference/compliance-api-access-control.html)  **
  - **Description:** Grants permission to retrieve the complete content of a specific verification evidence resource
  - **Resource types (\*required):** [VerificationEvidence\*](#list_marketplace-catalog-resource-VerificationEvidence)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_marketplace-catalog-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListAssessments](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_ListAssessments.html)  **
  - **Description:** Grants permission to list existing assessments
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListChangeSets](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_ListChangeSets.html)  **
  - **Description:** Grants permission to list existing change sets
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListEntities](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_ListEntities.html)  **
  - **Description:** Grants permission to list existing entities
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListInvoiceSubmissionTasks](https://docs.aws.amazon.com/marketplace/latest/APIReference/compliance-api-access-control.html)  **
  - **Description:** Grants permission to list existing invoice submission tasks
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListIssuedTaxInvoices](https://docs.aws.amazon.com/marketplace/latest/APIReference/compliance-api-access-control.html)  **
  - **Description:** Grants permission to list tax invoices issued by AWS on behalf of a seller
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPayables](https://docs.aws.amazon.com/marketplace/latest/APIReference/compliance-api-access-control.html)  **
  - **Description:** Grants permission to list payables of the specified payable provenance
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags on an existing entity, change set, invoice submission task, issued tax invoice, VerificationEvidence, TaxComplianceProfile, or TaxComplianceProfileChangeTask
  - **Resource types (\*required):** [ChangeSet](#list_marketplace-catalog-resource-ChangeSet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_marketplace-catalog-aws_ResourceTag___TagKey_)<br />[catalog:ChangeType](#list_marketplace-catalog-catalog_ChangeType)
  - **Resource types (\*required):** [Entity](#list_marketplace-catalog-resource-Entity) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_marketplace-catalog-aws_ResourceTag___TagKey_)<br />[catalog:ChangeType](#list_marketplace-catalog-catalog_ChangeType)
  - **Resource types (\*required):** [InvoiceSubmissionTask](#list_marketplace-catalog-resource-InvoiceSubmissionTask) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_marketplace-catalog-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [IssuedTaxInvoice](#list_marketplace-catalog-resource-IssuedTaxInvoice) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_marketplace-catalog-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [TaxComplianceProfile](#list_marketplace-catalog-resource-TaxComplianceProfile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_marketplace-catalog-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [TaxComplianceProfileChangeTask](#list_marketplace-catalog-resource-TaxComplianceProfileChangeTask) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_marketplace-catalog-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [VerificationEvidence](#list_marketplace-catalog-resource-VerificationEvidence) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_marketplace-catalog-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTaxComplianceProfileChangeTasks](https://docs.aws.amazon.com/marketplace/latest/APIReference/compliance-api-access-control.html)  **
  - **Description:** Grants permission to list tax compliance profile change tasks with optional filters
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTaxComplianceProfiles](https://docs.aws.amazon.com/marketplace/latest/APIReference/compliance-api-access-control.html)  **
  - **Description:** Grants permission to list tax compliance profiles with optional filters
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListVerificationEvidence](https://docs.aws.amazon.com/marketplace/latest/APIReference/compliance-api-access-control.html)  **
  - **Description:** Grants permission to list verification evidence resources with summary metadata
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListVerifications](https://docs.aws.amazon.com/marketplace/latest/APIReference/compliance-api-access-control.html)  **
  - **Description:** Grants permission to list all verification statuses across jurisdictions and verification types
  - **Resource types (\*required):** 
  - **Condition keys:** [aws-marketplace:VerificationType](#list_marketplace-catalog-aws-marketplace_VerificationType)
  - **Access level:** List

- **   [PutResourcePolicy](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_PutResourcePolicy.html)  **
  - **Description:** Grants permission to attach a resource policy to an existing entity
  - **Resource types (\*required):** [Entity\*](#list_marketplace-catalog-resource-Entity)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_marketplace-catalog-aws_ResourceTag___TagKey_)<br />[catalog:ChangeType](#list_marketplace-catalog-catalog_ChangeType)
  - **Access level:** Permissions management, Write

- **   [StartChangeSet](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_StartChangeSet.html)  **
  - **Description:** Grants permission to request a new change set (Note: resource-level permissions for this action and condition context keys for this action are only supported when used with Catalog API and are not supported when used with AWS Marketplace Management Portal)
  - **Resource types (\*required):** [Entity\*](#list_marketplace-catalog-resource-Entity)
  - **Condition keys:** [aws-marketplace:Intent](#list_marketplace-catalog-aws-marketplace_Intent)<br />[aws:RequestTag/${TagKey}](#list_marketplace-catalog-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_marketplace-catalog-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_marketplace-catalog-aws_TagKeys)<br />[catalog:ChangeType](#list_marketplace-catalog-catalog_ChangeType)
  - **Access level:** Write

- **   [StartInvoiceSubmissionTask](https://docs.aws.amazon.com/marketplace/latest/APIReference/compliance-api-access-control.html)  **
  - **Description:** Grants permission to initiate tasks that submit invoices for processing in AWS Marketplace
  - **Resource types (\*required):** [InvoiceSubmissionTask\*](#list_marketplace-catalog-resource-InvoiceSubmissionTask)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_marketplace-catalog-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_marketplace-catalog-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_marketplace-catalog-aws_TagKeys)
  - **Access level:** Write

- **   [StartTaxComplianceProfileChangeTask](https://docs.aws.amazon.com/marketplace/latest/APIReference/compliance-api-access-control.html)  **
  - **Description:** Grants permission to initiate asynchronous processing of a tax compliance profile create or update with artifact validation
  - **Resource types (\*required):** [TaxComplianceProfileChangeTask\*](#list_marketplace-catalog-resource-TaxComplianceProfileChangeTask)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_marketplace-catalog-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_marketplace-catalog-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_marketplace-catalog-aws_TagKeys)
  - **Access level:** Write

- **   [StartVerification](https://docs.aws.amazon.com/marketplace/latest/APIReference/compliance-api-access-control.html)  **
  - **Description:** Grants permission to submit verification evidence to a Payment Service Provider and enable data sharing for a specified jurisdiction
  - **Resource types (\*required):** [VerificationEvidence\*](#list_marketplace-catalog-resource-VerificationEvidence)
  - **Condition keys:** [aws-marketplace:VerificationType](#list_marketplace-catalog-aws-marketplace_VerificationType)<br />[aws:ResourceTag/${TagKey}](#list_marketplace-catalog-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_TagResource.html)  **
  - **Description:** Grants permission to add new tags to a resource. Supported resources: Entity, ChangeSet, InvoiceSubmissionTask, IssuedTaxInvoice, VerificationEvidence, TaxComplianceProfile, and TaxComplianceProfileChangeTask
  - **Resource types (\*required):** [ChangeSet](#list_marketplace-catalog-resource-ChangeSet) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_marketplace-catalog-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_marketplace-catalog-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_marketplace-catalog-aws_TagKeys)<br />[catalog:ChangeType](#list_marketplace-catalog-catalog_ChangeType)
  - **Resource types (\*required):** [Entity](#list_marketplace-catalog-resource-Entity) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_marketplace-catalog-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_marketplace-catalog-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_marketplace-catalog-aws_TagKeys)<br />[catalog:ChangeType](#list_marketplace-catalog-catalog_ChangeType)
  - **Resource types (\*required):** [InvoiceSubmissionTask](#list_marketplace-catalog-resource-InvoiceSubmissionTask) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_marketplace-catalog-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_marketplace-catalog-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_marketplace-catalog-aws_TagKeys)
  - **Resource types (\*required):** [IssuedTaxInvoice](#list_marketplace-catalog-resource-IssuedTaxInvoice) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_marketplace-catalog-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_marketplace-catalog-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_marketplace-catalog-aws_TagKeys)
  - **Resource types (\*required):** [TaxComplianceProfile](#list_marketplace-catalog-resource-TaxComplianceProfile) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_marketplace-catalog-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_marketplace-catalog-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_marketplace-catalog-aws_TagKeys)
  - **Resource types (\*required):** [TaxComplianceProfileChangeTask](#list_marketplace-catalog-resource-TaxComplianceProfileChangeTask) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_marketplace-catalog-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_marketplace-catalog-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_marketplace-catalog-aws_TagKeys)
  - **Resource types (\*required):** [VerificationEvidence](#list_marketplace-catalog-resource-VerificationEvidence) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_marketplace-catalog-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_marketplace-catalog-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_marketplace-catalog-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from a resource. Supported resources: Entity, ChangeSet, InvoiceSubmissionTask, IssuedTaxInvoice, VerificationEvidence, TaxComplianceProfile, and TaxComplianceProfileChangeTask
  - **Resource types (\*required):** [ChangeSet](#list_marketplace-catalog-resource-ChangeSet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_marketplace-catalog-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_marketplace-catalog-aws_TagKeys)<br />[catalog:ChangeType](#list_marketplace-catalog-catalog_ChangeType)
  - **Resource types (\*required):** [Entity](#list_marketplace-catalog-resource-Entity) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_marketplace-catalog-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_marketplace-catalog-aws_TagKeys)<br />[catalog:ChangeType](#list_marketplace-catalog-catalog_ChangeType)
  - **Resource types (\*required):** [InvoiceSubmissionTask](#list_marketplace-catalog-resource-InvoiceSubmissionTask) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_marketplace-catalog-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_marketplace-catalog-aws_TagKeys)
  - **Resource types (\*required):** [IssuedTaxInvoice](#list_marketplace-catalog-resource-IssuedTaxInvoice) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_marketplace-catalog-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_marketplace-catalog-aws_TagKeys)
  - **Resource types (\*required):** [TaxComplianceProfile](#list_marketplace-catalog-resource-TaxComplianceProfile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_marketplace-catalog-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_marketplace-catalog-aws_TagKeys)
  - **Resource types (\*required):** [TaxComplianceProfileChangeTask](#list_marketplace-catalog-resource-TaxComplianceProfileChangeTask) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_marketplace-catalog-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_marketplace-catalog-aws_TagKeys)
  - **Resource types (\*required):** [VerificationEvidence](#list_marketplace-catalog-resource-VerificationEvidence) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_marketplace-catalog-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_marketplace-catalog-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateVerificationEvidence](https://docs.aws.amazon.com/marketplace/latest/APIReference/compliance-api-access-control.html)  **
  - **Description:** Grants permission to update an existing verification evidence resource using full replacement semantics
  - **Resource types (\*required):** [VerificationEvidence\*](#list_marketplace-catalog-resource-VerificationEvidence)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_marketplace-catalog-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS Marketplace Catalog
<a name="list_marketplace-catalog-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [Assessment](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_DescribeAssessment.html#API_DescribeAssessment_ResponseSyntax)  | arn:${Partition}:aws-marketplace:${Region}::${Catalog}/Assessment/${ResourceId} |   | 
|  [ChangeSet](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_StartChangeSet.html#API_StartChangeSet_ResponseSyntax)  | arn:${Partition}:aws-marketplace:${Region}:${Account}:${Catalog}/ChangeSet/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_marketplace-catalog-aws_ResourceTag___TagKey_)<br />[catalog:ChangeType](#list_marketplace-catalog-catalog_ChangeType) | 
|  [Entity](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_DescribeEntity.html#API_DescribeEntity_ResponseSyntax)  | arn:${Partition}:aws-marketplace:${Region}:${Account}:${Catalog}/${EntityType}/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_marketplace-catalog-aws_ResourceTag___TagKey_)<br />[catalog:ChangeType](#list_marketplace-catalog-catalog_ChangeType) | 
|  [InvoiceSubmissionTask](https://docs.aws.amazon.com/marketplace/latest/APIReference/compliance-api-access-control.html)  | arn:${Partition}:aws-marketplace:${Region}:${Account}:catalog/${Catalog}/invoice-submission-task/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_marketplace-catalog-aws_ResourceTag___TagKey_) | 
|  [IssuedTaxInvoice](https://docs.aws.amazon.com/marketplace/latest/APIReference/compliance-api-access-control.html)  | arn:${Partition}:aws-marketplace:${Region}:${Account}:catalog/${Catalog}/issued-tax-invoice/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_marketplace-catalog-aws_ResourceTag___TagKey_) | 
|  [TaxComplianceProfile](https://docs.aws.amazon.com/marketplace/latest/APIReference/compliance-api-access-control.html)  | arn:${Partition}:aws-marketplace:${Region}:${Account}:tax-compliance-profile/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_marketplace-catalog-aws_ResourceTag___TagKey_) | 
|  [TaxComplianceProfileChangeTask](https://docs.aws.amazon.com/marketplace/latest/APIReference/compliance-api-access-control.html)  | arn:${Partition}:aws-marketplace:${Region}:${Account}:tax-compliance-profile-change-task/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_marketplace-catalog-aws_ResourceTag___TagKey_) | 
|  [VerificationEvidence](https://docs.aws.amazon.com/marketplace/latest/APIReference/compliance-api-access-control.html)  | arn:${Partition}:aws-marketplace:${Region}:${Account}:verification-type/${VerificationType}/verification-evidence/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_marketplace-catalog-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Marketplace Catalog
<a name="list_marketplace-catalog-policy-keys"></a>

AWS Marketplace Catalog defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws-marketplace:Intent](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/api-access-control.html)  | Filters access by the Intent parameter in the StartChangeSet request | String | 
|   [aws-marketplace:VerificationType](https://docs.aws.amazon.com/marketplace/latest/APIReference/compliance-api-access-control.html)  | Filters access by the verification type for verification process operations (StartVerification, GetVerification, ListVerifications). Valid values: BusinessVerification | String | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 
|   [catalog:ChangeType](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/api-access-control.html)  | Filters access by the change type in the StartChangeSet request | String | 