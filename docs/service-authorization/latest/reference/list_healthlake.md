

# Actions, resources, and condition keys for AWS HealthLake
<a name="list_healthlake"></a>

AWS HealthLake (service prefix: `healthlake`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/healthlake/latest/devguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/healthlake/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/healthlake/latest/devguide/auth-and-access-control.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/healthlake/healthlake.json) for this service.

**Topics**
+ [API operations defined by AWS HealthLake](#list_healthlake-operations)
+ [Actions defined by AWS HealthLake](#list_healthlake-actions-as-permissions)
+ [Resource types defined by AWS HealthLake](#list_healthlake-resources-for-iam-policies)
+ [Condition keys for AWS HealthLake](#list_healthlake-policy-keys)

## API operations defined by AWS HealthLake
<a name="list_healthlake-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_healthlake-actions-as-permissions).




- **   CreateDataTransformationProfile  **
  - **IAM action:**  [healthlake:CreateDataTransformationProfile](#list_healthlake-action-CreateDataTransformationProfile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [healthlake:TagResource](#list_healthlake-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateFHIRDatastore  **
  - **IAM action:**  [healthlake:CreateFHIRDatastore](#list_healthlake-action-CreateFHIRDatastore)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [healthlake:TagResource](#list_healthlake-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteDataTransformationProfile  **
  - **IAM action:**  [healthlake:DeleteDataTransformationProfile](#list_healthlake-action-DeleteDataTransformationProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFHIRDatastore  **
  - **IAM action:**  [healthlake:DeleteFHIRDatastore](#list_healthlake-action-DeleteFHIRDatastore) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeDataTransformationJob  **
  - **IAM action:**  [healthlake:DescribeDataTransformationJob](#list_healthlake-action-DescribeDataTransformationJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFHIRDatastore  **
  - **IAM action:**  [healthlake:DescribeFHIRDatastore](#list_healthlake-action-DescribeFHIRDatastore) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFHIRExportJob  **
  - **IAM action:**  [healthlake:DescribeFHIRExportJob](#list_healthlake-action-DescribeFHIRExportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFHIRImportJob  **
  - **IAM action:**  [healthlake:DescribeFHIRImportJob](#list_healthlake-action-DescribeFHIRImportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDataTransformationProfile  **
  - **IAM action:**  [healthlake:GetDataTransformationProfile](#list_healthlake-action-GetDataTransformationProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListDataTransformationJobs  **
  - **IAM action:**  [healthlake:ListDataTransformationJobs](#list_healthlake-action-ListDataTransformationJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDataTransformationProfileVersions  **
  - **IAM action:**  [healthlake:ListDataTransformationProfileVersions](#list_healthlake-action-ListDataTransformationProfileVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDataTransformationProfiles  **
  - **IAM action:**  [healthlake:ListDataTransformationProfiles](#list_healthlake-action-ListDataTransformationProfiles) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFHIRDatastores  **
  - **IAM action:**  [healthlake:ListFHIRDatastores](#list_healthlake-action-ListFHIRDatastores) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFHIRExportJobs  **
  - **IAM action:**  [healthlake:ListFHIRExportJobs](#list_healthlake-action-ListFHIRExportJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFHIRImportJobs  **
  - **IAM action:**  [healthlake:ListFHIRImportJobs](#list_healthlake-action-ListFHIRImportJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [healthlake:ListTagsForResource](#list_healthlake-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PublishDataTransformationProfile  **
  - **IAM action:**  [healthlake:PublishDataTransformationProfile](#list_healthlake-action-PublishDataTransformationProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RestoreFHIRDatastore  **
  - **IAM action:**  [healthlake:RestoreFHIRDatastore](#list_healthlake-action-RestoreFHIRDatastore)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [healthlake:TagResource](#list_healthlake-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   StartDataTransformationJob  **
  - **IAM action:**  [healthlake:StartDataTransformationJob](#list_healthlake-action-StartDataTransformationJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** healthlake.amazonaws.com / **Access level:** Write

- **   StartFHIRExportJob  **
  - **IAM action:**  [healthlake:StartFHIRExportJob](#list_healthlake-action-StartFHIRExportJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** healthlake.amazonaws.com / **Access level:** Write

- **   StartFHIRImportJob  **
  - **IAM action:**  [healthlake:StartFHIRImportJob](#list_healthlake-action-StartFHIRImportJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** healthlake.amazonaws.com / **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [healthlake:TagResource](#list_healthlake-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [healthlake:UntagResource](#list_healthlake-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateDataTransformationProfile  **
  - **IAM action:**  [healthlake:UpdateDataTransformationProfile](#list_healthlake-action-UpdateDataTransformationProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateFHIRDatastore  **
  - **IAM action:**  [healthlake:UpdateFHIRDatastore](#list_healthlake-action-UpdateFHIRDatastore) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateProfileWithAgent  **
  - **IAM action:**  [healthlake:UpdateProfileWithAgent](#list_healthlake-action-UpdateProfileWithAgent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS HealthLake
<a name="list_healthlake-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CancelFHIRExportJobWithDelete](https://docs.aws.amazon.com/healthlake/latest/devguide/export-datastore-rest.html)  **
  - **Description:** Grants permission to cancel an on going FHIR Export job with Delete
  - **Resource types (\*required):** [datastore\*](#list_healthlake-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ConfirmAttributionList](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-operations-confirm-attribution-list.html)  **
  - **Description:** Grants permission to allow customers to indicate to a Producer that the Consumer does not have any more changes to be made to the Attribution List
  - **Resource types (\*required):** [datastore\*](#list_healthlake-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateDataTransformationProfile](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_CreateDataTransformationProfile.html)  **
  - **Description:** Grants permission to create a data transformation profile
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_healthlake-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_healthlake-aws_TagKeys)
  - **Access level:** Write

- **   [CreateFHIRDatastore](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_CreateFHIRDatastore.html)  **
  - **Description:** Grants permission to create a datastore that can ingest and export FHIR data
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_healthlake-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_healthlake-aws_TagKeys)
  - **Access level:** Write

- **   [CreateResource](https://docs.aws.amazon.com/healthlake/latest/devguide/crud-healthlake.html)  **
  - **Description:** Grants permission to create resource
  - **Resource types (\*required):** [datastore\*](#list_healthlake-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDataTransformationProfile](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_DeleteDataTransformationProfile.html)  **
  - **Description:** Grants permission to delete a data transformation profile and all its versions
  - **Resource types (\*required):** [dataTransformationProfile\*](#list_healthlake-resource-dataTransformationProfile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteFHIRDatastore](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_DeleteFHIRDatastore.html)  **
  - **Description:** Grants permission to delete a datastore
  - **Resource types (\*required):** [datastore\*](#list_healthlake-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteResource](https://docs.aws.amazon.com/healthlake/latest/devguide/crud-healthlake.html)  **
  - **Description:** Grants permission to delete resource
  - **Resource types (\*required):** [datastore\*](#list_healthlake-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeDataTransformationJob](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_DescribeDataTransformationJob.html)  **
  - **Description:** Grants permission to describe a data transformation job
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeFHIRBulkDeleteJob](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-operations-bulk-delete.html)  **
  - **Description:** Grants permission to describe a FHIR Bulk Delete Job
  - **Resource types (\*required):** [datastore\*](#list_healthlake-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeFHIRBulkMemberMatchJob](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-operations-bulk-member-match.html)  **
  - **Description:** Grants permission to describe a FHIR Bulk Member Match Job
  - **Resource types (\*required):** [datastore\*](#list_healthlake-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeFHIRDatastore](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_DescribeFHIRDatastore.html)  **
  - **Description:** Grants permission to get the properties associated with the FHIR datastore, including the datastore ID, datastore ARN, datastore name, datastore status, created at, datastore type version, and datastore endpoint
  - **Resource types (\*required):** [datastore\*](#list_healthlake-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeFHIRExportJob](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_DescribeFHIRExportJob.html)  **
  - **Description:** Grants permission to display the properties of a FHIR export job, including the ID, ARN, name, and the status of the datastore
  - **Resource types (\*required):** [datastore\*](#list_healthlake-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeFHIRExportJobWithGet](https://docs.aws.amazon.com/healthlake/latest/devguide/export-datastore-rest.html)  **
  - **Description:** Grants permission to display the properties of a FHIR export job, including the ID, ARN, name, and the status of the datastore with Get
  - **Resource types (\*required):** [datastore\*](#list_healthlake-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeFHIRImportJob](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_DescribeFHIRImportJob.html)  **
  - **Description:** Grants permission to display the properties of a FHIR import job, including the ID, ARN, name, and the status of the datastore
  - **Resource types (\*required):** [datastore\*](#list_healthlake-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ExpandValueSetWithGet](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-operations-expand.html)  **
  - **Description:** Grants permission to search and expand ValueSet resource
  - **Resource types (\*required):** [datastore\*](#list_healthlake-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ExpandValueSetWithPost](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-operations-expand.html)  **
  - **Description:** Grants permission to search and expand ValueSet resource
  - **Resource types (\*required):** [datastore\*](#list_healthlake-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GenerateDocumentWithGet](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-operations-document.html)  **
  - **Description:** Grants permission to generate a clinical document resource
  - **Resource types (\*required):** [datastore\*](#list_healthlake-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GenerateDocumentWithPost](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-operations-document.html)  **
  - **Description:** Grants permission to generate a clinical document resource
  - **Resource types (\*required):** [datastore\*](#list_healthlake-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetCapabilities](https://docs.aws.amazon.com/healthlake/latest/devguide/crud-healthlake.html)  **
  - **Description:** Grants permission to get the capabilities of a FHIR datastore
  - **Resource types (\*required):** [datastore\*](#list_healthlake-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDataTransformationProfile](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_GetDataTransformationProfile.html)  **
  - **Description:** Grants permission to retrieve a data transformation profile and its content
  - **Resource types (\*required):** [dataTransformationProfile\*](#list_healthlake-resource-dataTransformationProfile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetExportedFile](https://docs.aws.amazon.com/healthlake/latest/devguide/export-datastore-rest.html)  **
  - **Description:** Grants permission to access exported files from a FHIR Export job initiated with Get
  - **Resource types (\*required):** [datastore\*](#list_healthlake-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetHistoryByResourceId](https://docs.aws.amazon.com/healthlake/latest/devguide/crud-healthlake.html)  **
  - **Description:** Grants permission to read resource history
  - **Resource types (\*required):** [datastore\*](#list_healthlake-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [InquirePreAuthClaim](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-operations-inquire.html)  **
  - **Description:** Grants permission to inquire about the status of a prior authorization Claim
  - **Resource types (\*required):** [datastore\*](#list_healthlake-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListDataTransformationJobs](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_ListDataTransformationJobs.html)  **
  - **Description:** Grants permission to list data transformation jobs in the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDataTransformationProfileVersions](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_ListDataTransformationProfileVersions.html)  **
  - **Description:** Grants permission to list all versions of a data transformation profile
  - **Resource types (\*required):** [dataTransformationProfile\*](#list_healthlake-resource-dataTransformationProfile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDataTransformationProfiles](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_ListDataTransformationProfiles.html)  **
  - **Description:** Grants permission to list data transformation profiles in the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListFHIRDatastores](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_ListFHIRDatastores.html)  **
  - **Description:** Grants permission to list all FHIR datastores that are in the user's account, regardless of datastore status
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListFHIRExportJobs](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_ListFHIRExportJobs.html)  **
  - **Description:** Grants permission to get a list of export jobs for the specified datastore
  - **Resource types (\*required):** [datastore\*](#list_healthlake-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListFHIRImportJobs](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_ListFHIRImportJobs.html)  **
  - **Description:** Grants permission to get a list of import jobs for the specified datastore
  - **Resource types (\*required):** [datastore\*](#list_healthlake-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to get a list of tags for the specified datastore
  - **Resource types (\*required):** [dataTransformationProfile](#list_healthlake-resource-dataTransformationProfile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [datastore](#list_healthlake-resource-datastore) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [LookupCodeSystemWithGet](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-operations-lookup.html)  **
  - **Description:** Grants permission to retrieve Codes for a CodeSystem resource
  - **Resource types (\*required):** [datastore\*](#list_healthlake-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [LookupCodeSystemWithPost](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-operations-lookup.html)  **
  - **Description:** Grants permission to retrieve Codes for a CodeSystem resource
  - **Resource types (\*required):** [datastore\*](#list_healthlake-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [MemberAdd](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-operations-member-add.html)  **
  - **Description:** Grants permission to attribute a member with a specific provider group
  - **Resource types (\*required):** [datastore\*](#list_healthlake-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [MemberMatch](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-operations-member-match.html)  **
  - **Description:** Grants permission to enable cross-system patient matching
  - **Resource types (\*required):** [datastore\*](#list_healthlake-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [MemberRemove](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-operations-member-remove.html)  **
  - **Description:** Grants permission to remove a member from a group
  - **Resource types (\*required):** [datastore\*](#list_healthlake-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PatchResource](https://docs.aws.amazon.com/healthlake/latest/devguide/managing-fhir-resources-patch.html)  **
  - **Description:** Grants permission to patch a resource
  - **Resource types (\*required):** [datastore\*](#list_healthlake-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ProcessBundle](https://docs.aws.amazon.com/healthlake/latest/devguide/crud-healthlake.html)  **
  - **Description:** Grants permission to bundle multiple resource operations
  - **Resource types (\*required):** [datastore\*](#list_healthlake-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PublishDataTransformationProfile](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_PublishDataTransformationProfile.html)  **
  - **Description:** Grants permission to publish a new immutable version of a data transformation profile
  - **Resource types (\*required):** [dataTransformationProfile\*](#list_healthlake-resource-dataTransformationProfile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [QuestionnairePackage](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-operations-questionnaire-package.html)  **
  - **Description:** Grants permission to retrieve Questionnaire packages with dependency Library and ValueSet resources
  - **Resource types (\*required):** [datastore\*](#list_healthlake-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ReadResource](https://docs.aws.amazon.com/healthlake/latest/devguide/crud-healthlake.html)  **
  - **Description:** Grants permission to read resource
  - **Resource types (\*required):** [datastore\*](#list_healthlake-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [RestoreFHIRDatastore](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_RestoreFHIRDatastore.html)  **
  - **Description:** Grants permission to restore a backup-enabled datastore to a point in time, creating a new datastore from the backup
  - **Resource types (\*required):** [datastore\*](#list_healthlake-resource-datastore)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_healthlake-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_healthlake-aws_TagKeys)
  - **Access level:** Write

- **   [RetrieveAttributionStatus](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-operations-attribution-status.html)  **
  - **Description:** Grants permission to retrieve member attribution status
  - **Resource types (\*required):** [datastore\*](#list_healthlake-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SearchEverything](https://docs.aws.amazon.com/healthlake/latest/devguide/search-healthlake.html)  **
  - **Description:** Grants permission to search all resources related to a patient
  - **Resource types (\*required):** [datastore\*](#list_healthlake-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [SearchWithGet](https://docs.aws.amazon.com/healthlake/latest/devguide/search-healthlake.html)  **
  - **Description:** Grants permission to search resources with GET method
  - **Resource types (\*required):** [datastore\*](#list_healthlake-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [SearchWithPost](https://docs.aws.amazon.com/healthlake/latest/devguide/search-healthlake.html)  **
  - **Description:** Grants permission to search resources with POST method
  - **Resource types (\*required):** [datastore\*](#list_healthlake-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [StartDataTransformationJob](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_StartDataTransformationJob.html)  **
  - **Description:** Grants permission to start an asynchronous data transformation job
  - **Resource types (\*required):** [dataTransformationProfile\*](#list_healthlake-resource-dataTransformationProfile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartFHIRBulkDeleteJob](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-operations-bulk-delete.html)  **
  - **Description:** Grants permission to begin a FHIR Bulk Delete Job
  - **Resource types (\*required):** [datastore\*](#list_healthlake-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartFHIRBulkMemberMatchJob](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-operations-bulk-member-match.html)  **
  - **Description:** Grants permission to begin a FHIR Bulk Member Match Job
  - **Resource types (\*required):** [datastore\*](#list_healthlake-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartFHIRExportJob](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_StartFHIRExportJob.html)  **
  - **Description:** Grants permission to begin a FHIR Export job
  - **Resource types (\*required):** [datastore\*](#list_healthlake-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartFHIRExportJobWithGet](https://docs.aws.amazon.com/healthlake/latest/devguide/export-datastore-rest.html)  **
  - **Description:** Grants permission to begin a FHIR Export job with Get
  - **Resource types (\*required):** [datastore\*](#list_healthlake-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartFHIRExportJobWithPost](https://docs.aws.amazon.com/healthlake/latest/devguide/export-datastore-rest.html)  **
  - **Description:** Grants permission to begin a FHIR Export job with Post
  - **Resource types (\*required):** [datastore\*](#list_healthlake-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartFHIRImportJob](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_StartFHIRImportJob.html)  **
  - **Description:** Grants permission to begin a FHIR Import job
  - **Resource types (\*required):** [datastore\*](#list_healthlake-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SubmitPreAuthClaim](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-operations-submit.html)  **
  - **Description:** Grants permission to submit a prior authorization Claim request
  - **Resource types (\*required):** [datastore\*](#list_healthlake-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add tags to a datastore
  - **Resource types (\*required):** [dataTransformationProfile](#list_healthlake-resource-dataTransformationProfile) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_healthlake-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_healthlake-aws_TagKeys)
  - **Resource types (\*required):** [datastore](#list_healthlake-resource-datastore) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_healthlake-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_healthlake-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [TransformData](https://docs.aws.amazon.com/healthlake/latest/devguide/data-transformation-getting-started-sdk.html)  **
  - **Description:** Grants permission to perform a synchronous data transformation
  - **Resource types (\*required):** [dataTransformationProfile\*](#list_healthlake-resource-dataTransformationProfile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TranslateConceptMapWithGet](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-operations-translate.html)  **
  - **Description:** Grants permission to translate a code from one value set to another using a ConceptMap resource with GET method
  - **Resource types (\*required):** [datastore\*](#list_healthlake-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [TranslateConceptMapWithPost](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-operations-translate.html)  **
  - **Description:** Grants permission to translate a code from one value set to another using a ConceptMap resource with POST method
  - **Resource types (\*required):** [datastore\*](#list_healthlake-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [UntagResource](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags associated with a datastore
  - **Resource types (\*required):** [dataTransformationProfile](#list_healthlake-resource-dataTransformationProfile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_healthlake-aws_TagKeys)
  - **Resource types (\*required):** [datastore](#list_healthlake-resource-datastore) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_healthlake-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateDataTransformationProfile](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_UpdateDataTransformationProfile.html)  **
  - **Description:** Grants permission to update the draft version of a data transformation profile
  - **Resource types (\*required):** [dataTransformationProfile\*](#list_healthlake-resource-dataTransformationProfile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateFHIRDatastore](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_UpdateFHIRDatastore.html)  **
  - **Description:** Grants permission to update the configuration of a datastore
  - **Resource types (\*required):** [datastore\*](#list_healthlake-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateProfileWithAgent](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_UpdateProfileWithAgent.html)  **
  - **Description:** Grants permission to update a data transformation profile using the AI agent
  - **Resource types (\*required):** [dataTransformationProfile\*](#list_healthlake-resource-dataTransformationProfile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateResource](https://docs.aws.amazon.com/healthlake/latest/devguide/crud-healthlake.html)  **
  - **Description:** Grants permission to update resource
  - **Resource types (\*required):** [datastore\*](#list_healthlake-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ValidateResource](https://docs.aws.amazon.com/healthlake/latest/devguide/reference-fhir-operations-validate.html)  **
  - **Description:** Grants permission to validate a resource
  - **Resource types (\*required):** [datastore\*](#list_healthlake-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ValidateSource](https://docs.aws.amazon.com/healthlake/latest/devguide/data-transformation-features.html)  **
  - **Description:** Grants permission to validate source data against format specifications
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [VersionReadResource](https://docs.aws.amazon.com/healthlake/latest/devguide/crud-healthlake.html)  **
  - **Description:** Grants permission to read version of a resource
  - **Resource types (\*required):** [datastore\*](#list_healthlake-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_)
  - **Access level:** Read



## Resource types defined by AWS HealthLake
<a name="list_healthlake-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [dataTransformationProfile](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_DataTransformationProfileSummary.html)  | arn:${Partition}:healthlake:${Region}:${Account}:dataTransformationProfile/${ProfileId} | [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_) | 
|  [datastore](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_DatastoreProperties.html)  | arn:${Partition}:healthlake:${Region}:${Account}:datastore/fhir/${DatastoreId} | [aws:ResourceTag/${TagKey}](#list_healthlake-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS HealthLake
<a name="list_healthlake-policy-keys"></a>

AWS HealthLake defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the presence of tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of tag keys in the request | ArrayOfString | 