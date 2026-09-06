

# Actions, resources, and condition keys for AWS HealthImaging
<a name="list_medical-imaging"></a>

AWS HealthImaging (service prefix: `medical-imaging`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/healthimaging/latest/devguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/healthimaging/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/healthimaging/latest/devguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/medical-imaging/medical-imaging.json) for this service.

**Topics**
+ [API operations defined by AWS HealthImaging](#list_medical-imaging-operations)
+ [Actions defined by AWS HealthImaging](#list_medical-imaging-actions-as-permissions)
+ [Resource types defined by AWS HealthImaging](#list_medical-imaging-resources-for-iam-policies)
+ [Condition keys for AWS HealthImaging](#list_medical-imaging-policy-keys)

## API operations defined by AWS HealthImaging
<a name="list_medical-imaging-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_medical-imaging-actions-as-permissions).




- **   CopyImageSet  **
  - **IAM action:**  [medical-imaging:CopyImageSet](#list_medical-imaging-action-CopyImageSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateDatastore  **
  - **IAM action:**  [medical-imaging:CreateDatastore](#list_medical-imaging-action-CreateDatastore)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [medical-imaging:TagResource](#list_medical-imaging-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteDatastore  **
  - **IAM action:**  [medical-imaging:DeleteDatastore](#list_medical-imaging-action-DeleteDatastore) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteImageSet  **
  - **IAM action:**  [medical-imaging:DeleteImageSet](#list_medical-imaging-action-DeleteImageSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetDICOMImportJob  **
  - **IAM action:**  [medical-imaging:GetDICOMImportJob](#list_medical-imaging-action-GetDICOMImportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDatastore  **
  - **IAM action:**  [medical-imaging:GetDatastore](#list_medical-imaging-action-GetDatastore) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetImageFrame  **
  - **IAM action:**  [medical-imaging:GetImageFrame](#list_medical-imaging-action-GetImageFrame) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetImageSet  **
  - **IAM action:**  [medical-imaging:GetImageSet](#list_medical-imaging-action-GetImageSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetImageSetMetadata  **
  - **IAM action:**  [medical-imaging:GetImageSetMetadata](#list_medical-imaging-action-GetImageSetMetadata) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListDICOMImportJobs  **
  - **IAM action:**  [medical-imaging:ListDICOMImportJobs](#list_medical-imaging-action-ListDICOMImportJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDatastores  **
  - **IAM action:**  [medical-imaging:ListDatastores](#list_medical-imaging-action-ListDatastores) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListImageSetVersions  **
  - **IAM action:**  [medical-imaging:ListImageSetVersions](#list_medical-imaging-action-ListImageSetVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [medical-imaging:ListTagsForResource](#list_medical-imaging-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   SearchImageSets  **
  - **IAM action:**  [medical-imaging:SearchImageSets](#list_medical-imaging-action-SearchImageSets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   StartDICOMImportJob  **
  - **IAM action:**  [medical-imaging:StartDICOMImportJob](#list_medical-imaging-action-StartDICOMImportJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** medical-imaging.amazonaws.com / **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [medical-imaging:TagResource](#list_medical-imaging-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [medical-imaging:UntagResource](#list_medical-imaging-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateImageSetMetadata  **
  - **IAM action:**  [medical-imaging:UpdateImageSetMetadata](#list_medical-imaging-action-UpdateImageSetMetadata) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS HealthImaging
<a name="list_medical-imaging-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CopyImageSet](https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_dataplane_CopyImageSet.html)  **
  - **Description:** Grants permission to copy an image set
  - **Resource types (\*required):** [datastore\*](#list_medical-imaging-resource-datastore) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medical-imaging-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [imageset\*](#list_medical-imaging-resource-imageset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medical-imaging-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateDatastore](https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_CreateDatastore.html)  **
  - **Description:** Grants permission to create a data store to ingest imaging data
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_medical-imaging-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_medical-imaging-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteDatastore](https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_DeleteDatastore.html)  **
  - **Description:** Grants permission to delete a data store
  - **Resource types (\*required):** [datastore\*](#list_medical-imaging-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medical-imaging-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteImageSet](https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_dataplane_DeleteImageSet.html)  **
  - **Description:** Grants permission to delete an image set
  - **Resource types (\*required):** [datastore\*](#list_medical-imaging-resource-datastore) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medical-imaging-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [imageset\*](#list_medical-imaging-resource-imageset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medical-imaging-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetDICOMBulkdata](https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_dicom_GetDICOMBulkdata.html)  **
  - **Description:** Grants permission to get dicom bulkdata in binary format
  - **Resource types (\*required):** [datastore\*](#list_medical-imaging-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medical-imaging-aws_ResourceTag___TagKey_)<br />[medical-imaging:SeriesInstanceUID](#list_medical-imaging-medical-imaging_SeriesInstanceUID)<br />[medical-imaging:StudyInstanceUID](#list_medical-imaging-medical-imaging_StudyInstanceUID)
  - **Access level:** Read

- **   [GetDICOMImportJob](https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_GetDICOMImportJob.html)  **
  - **Description:** Grants permission to get an import job's properties
  - **Resource types (\*required):** [datastore\*](#list_medical-imaging-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medical-imaging-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDICOMInstance](https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_dicom_GetDICOMInstance.html)  **
  - **Description:** Grants permission to get dicom instance in dcm format
  - **Resource types (\*required):** [datastore\*](#list_medical-imaging-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medical-imaging-aws_ResourceTag___TagKey_)<br />[medical-imaging:SeriesInstanceUID](#list_medical-imaging-medical-imaging_SeriesInstanceUID)<br />[medical-imaging:StudyInstanceUID](#list_medical-imaging-medical-imaging_StudyInstanceUID)
  - **Access level:** Read

- **   [GetDICOMInstanceFrames](https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_dicom_GetDICOMInstanceFrames.html)  **
  - **Description:** Grants permission to get dicom instance frames in format requested by the customer
  - **Resource types (\*required):** [datastore\*](#list_medical-imaging-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medical-imaging-aws_ResourceTag___TagKey_)<br />[medical-imaging:SeriesInstanceUID](#list_medical-imaging-medical-imaging_SeriesInstanceUID)<br />[medical-imaging:StudyInstanceUID](#list_medical-imaging-medical-imaging_StudyInstanceUID)
  - **Access level:** Read

- **   [GetDICOMInstanceMetadata](https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_dicom_GetDICOMInstanceMetadata.html)  **
  - **Description:** Grants permission to get dicom instance metadata in DICOM JSON format
  - **Resource types (\*required):** [datastore\*](#list_medical-imaging-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medical-imaging-aws_ResourceTag___TagKey_)<br />[medical-imaging:SeriesInstanceUID](#list_medical-imaging-medical-imaging_SeriesInstanceUID)<br />[medical-imaging:StudyInstanceUID](#list_medical-imaging-medical-imaging_StudyInstanceUID)
  - **Access level:** Read

- **   [GetDICOMSeriesMetadata](https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_dicom_GetDICOMSeriesMetadata.html)  **
  - **Description:** Grants permission to retrieve metadata for all DICOM instances belonging to a given DICOM series in DICOM JSON format
  - **Resource types (\*required):** [datastore\*](#list_medical-imaging-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medical-imaging-aws_ResourceTag___TagKey_)<br />[medical-imaging:SeriesInstanceUID](#list_medical-imaging-medical-imaging_SeriesInstanceUID)<br />[medical-imaging:StudyInstanceUID](#list_medical-imaging-medical-imaging_StudyInstanceUID)
  - **Access level:** Read

- **   [GetDatastore](https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_GetDatastore.html)  **
  - **Description:** Grants permission to get data store properties
  - **Resource types (\*required):** [datastore\*](#list_medical-imaging-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medical-imaging-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetImageFrame](https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_dataplane_GetImageFrame.html)  **
  - **Description:** Grants permission to get image frame properties
  - **Resource types (\*required):** [datastore\*](#list_medical-imaging-resource-datastore) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medical-imaging-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [imageset\*](#list_medical-imaging-resource-imageset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medical-imaging-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetImageSet](https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_dataplane_GetImageSet.html)  **
  - **Description:** Grants permission to get image set properties
  - **Resource types (\*required):** [datastore\*](#list_medical-imaging-resource-datastore) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medical-imaging-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [imageset\*](#list_medical-imaging-resource-imageset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medical-imaging-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetImageSetMetadata](https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_dataplane_GetImageSetMetadata.html)  **
  - **Description:** Grants permission to get image set metadata properties
  - **Resource types (\*required):** [datastore\*](#list_medical-imaging-resource-datastore) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medical-imaging-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [imageset\*](#list_medical-imaging-resource-imageset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medical-imaging-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListDICOMImportJobs](https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_ListDICOMImportJobs.html)  **
  - **Description:** Grants permission to list import jobs for a data store
  - **Resource types (\*required):** [datastore\*](#list_medical-imaging-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medical-imaging-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDatastores](https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_ListDatastores.html)  **
  - **Description:** Grants permission to list data stores
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListImageSetVersions](https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_dataplane_ListImageSetVersions.html)  **
  - **Description:** Grants permission to list versions of an image set
  - **Resource types (\*required):** [datastore\*](#list_medical-imaging-resource-datastore) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medical-imaging-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [imageset\*](#list_medical-imaging-resource-imageset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medical-imaging-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a medical imaging resource
  - **Resource types (\*required):** [datastore](#list_medical-imaging-resource-datastore) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medical-imaging-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [imageset](#list_medical-imaging-resource-imageset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medical-imaging-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [SearchDICOMInstances](https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_dicom_SearchDICOMInstances.html)  **
  - **Description:** Grants permission to search dicom instances that returns data in DICOM JSON format
  - **Resource types (\*required):** [datastore\*](#list_medical-imaging-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medical-imaging-aws_ResourceTag___TagKey_)<br />[medical-imaging:SeriesInstanceUID](#list_medical-imaging-medical-imaging_SeriesInstanceUID)<br />[medical-imaging:StudyInstanceUID](#list_medical-imaging-medical-imaging_StudyInstanceUID)
  - **Access level:** Read

- **   [SearchDICOMSeries](https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_dicom_SearchDICOMSeries.html)  **
  - **Description:** Grants permission to search dicom series that returns data in DICOM JSON format
  - **Resource types (\*required):** [datastore\*](#list_medical-imaging-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medical-imaging-aws_ResourceTag___TagKey_)<br />[medical-imaging:StudyInstanceUID](#list_medical-imaging-medical-imaging_StudyInstanceUID)
  - **Access level:** Read

- **   [SearchDICOMStudies](https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_dicom_SearchDICOMStudies.html)  **
  - **Description:** Grants permission to search dicom studies that returns data in DICOM JSON format
  - **Resource types (\*required):** [datastore\*](#list_medical-imaging-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medical-imaging-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [SearchImageSets](https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_dataplane_SearchImageSets.html)  **
  - **Description:** Grants permission to search image sets
  - **Resource types (\*required):** [datastore\*](#list_medical-imaging-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medical-imaging-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [StartDICOMImportJob](https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_StartDICOMImportJob.html)  **
  - **Description:** Grants permission to start a DICOM import job
  - **Resource types (\*required):** [datastore\*](#list_medical-imaging-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medical-imaging-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StoreDICOM](https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_dicom_StoreDICOM.html)  **
  - **Description:** Grants permission to store dicom instances that returns result in DICOM JSON format
  - **Resource types (\*required):** [datastore\*](#list_medical-imaging-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medical-imaging-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StoreDICOMStudy](https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_dicom_StoreDICOMStudy.html)  **
  - **Description:** Grants permission to store a dicom study that returns result in DICOM JSON format
  - **Resource types (\*required):** [datastore\*](#list_medical-imaging-resource-datastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medical-imaging-aws_ResourceTag___TagKey_)<br />[medical-imaging:StudyInstanceUID](#list_medical-imaging-medical-imaging_StudyInstanceUID)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add tags to a medical imaging resource
  - **Resource types (\*required):** [datastore](#list_medical-imaging-resource-datastore) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_medical-imaging-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_medical-imaging-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medical-imaging-aws_TagKeys)
  - **Resource types (\*required):** [imageset](#list_medical-imaging-resource-imageset) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_medical-imaging-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_medical-imaging-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medical-imaging-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from a medical imaging resource
  - **Resource types (\*required):** [datastore](#list_medical-imaging-resource-datastore) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medical-imaging-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medical-imaging-aws_TagKeys)
  - **Resource types (\*required):** [imageset](#list_medical-imaging-resource-imageset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medical-imaging-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_medical-imaging-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateImageSetMetadata](https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_dataplane_UpdateImageSetMetadata.html)  **
  - **Description:** Grants permission to update image set metadata properties
  - **Resource types (\*required):** [datastore\*](#list_medical-imaging-resource-datastore) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medical-imaging-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [imageset\*](#list_medical-imaging-resource-imageset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_medical-imaging-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS HealthImaging
<a name="list_medical-imaging-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [datastore](https://docs.aws.amazon.com/healthimaging/latest/devguide/API_DatastoreProperties.html)  | arn:${Partition}:medical-imaging:${Region}:${Account}:datastore/${DatastoreId} | [aws:ResourceTag/${TagKey}](#list_medical-imaging-aws_ResourceTag___TagKey_) | 
|  [imageset](https://docs.aws.amazon.com/healthimaging/latest/devguide/API_ImageSetProperties.html)  | arn:${Partition}:medical-imaging:${Region}:${Account}:datastore/${DatastoreId}/imageset/${ImageSetId} | [aws:ResourceTag/${TagKey}](#list_medical-imaging-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS HealthImaging
<a name="list_medical-imaging-policy-keys"></a>

AWS HealthImaging defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by a tag key and value pair that is allowed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by a tag key and value pair of a resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by a list of tag keys that are allowed in the request | ArrayOfString | 
|   [medical-imaging:SeriesInstanceUID](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awshealthimaging.html#awshealthimaging-policy-keys)  | Filters access by the SeriesInstanceUID parameter in the request | String | 
|   [medical-imaging:StudyInstanceUID](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awshealthimaging.html#awshealthimaging-policy-keys)  | Filters access by the StudyInstanceUID parameter in the request | String | 