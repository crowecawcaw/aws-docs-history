

# Actions, resources, and condition keys for Amazon SageMaker geospatial capabilities
<a name="list_sagemaker-geospatial"></a>

Amazon SageMaker geospatial capabilities (service prefix: `sagemaker-geospatial`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/sagemaker/latest/dg/geospatial.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Operations_Amazon_SageMaker_geospatial_capabilities.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/sagemaker/latest/dg/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/sagemaker-geospatial/sagemaker-geospatial.json) for this service.

**Topics**
+ [API operations defined by Amazon SageMaker geospatial capabilities](#list_sagemaker-geospatial-operations)
+ [Actions defined by Amazon SageMaker geospatial capabilities](#list_sagemaker-geospatial-actions-as-permissions)
+ [Resource types defined by Amazon SageMaker geospatial capabilities](#list_sagemaker-geospatial-resources-for-iam-policies)
+ [Condition keys for Amazon SageMaker geospatial capabilities](#list_sagemaker-geospatial-policy-keys)

## API operations defined by Amazon SageMaker geospatial capabilities
<a name="list_sagemaker-geospatial-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_sagemaker-geospatial-actions-as-permissions).




- **   DeleteEarthObservationJob  **
  - **IAM action:**  [sagemaker-geospatial:DeleteEarthObservationJob](#list_sagemaker-geospatial-action-DeleteEarthObservationJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteVectorEnrichmentJob  **
  - **IAM action:**  [sagemaker-geospatial:DeleteVectorEnrichmentJob](#list_sagemaker-geospatial-action-DeleteVectorEnrichmentJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ExportEarthObservationJob  **
  - **IAM action:**  [sagemaker-geospatial:ExportEarthObservationJob](#list_sagemaker-geospatial-action-ExportEarthObservationJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sagemaker-geospatial.amazonaws.com / **Access level:** Write

- **   ExportVectorEnrichmentJob  **
  - **IAM action:**  [sagemaker-geospatial:ExportVectorEnrichmentJob](#list_sagemaker-geospatial-action-ExportVectorEnrichmentJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sagemaker-geospatial.amazonaws.com / **Access level:** Write

- **   GetEarthObservationJob  **
  - **IAM action:**  [sagemaker-geospatial:GetEarthObservationJob](#list_sagemaker-geospatial-action-GetEarthObservationJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRasterDataCollection  **
  - **IAM action:**  [sagemaker-geospatial:GetRasterDataCollection](#list_sagemaker-geospatial-action-GetRasterDataCollection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTile  **
  - **IAM action:**  [sagemaker-geospatial:GetTile](#list_sagemaker-geospatial-action-GetTile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sagemaker-geospatial.amazonaws.com / **Access level:** Write

- **   GetVectorEnrichmentJob  **
  - **IAM action:**  [sagemaker-geospatial:GetVectorEnrichmentJob](#list_sagemaker-geospatial-action-GetVectorEnrichmentJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListEarthObservationJobs  **
  - **IAM action:**  [sagemaker-geospatial:ListEarthObservationJobs](#list_sagemaker-geospatial-action-ListEarthObservationJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRasterDataCollections  **
  - **IAM action:**  [sagemaker-geospatial:ListRasterDataCollections](#list_sagemaker-geospatial-action-ListRasterDataCollections) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [sagemaker-geospatial:ListTagsForResource](#list_sagemaker-geospatial-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListVectorEnrichmentJobs  **
  - **IAM action:**  [sagemaker-geospatial:ListVectorEnrichmentJobs](#list_sagemaker-geospatial-action-ListVectorEnrichmentJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   SearchRasterDataCollection  **
  - **IAM action:**  [sagemaker-geospatial:SearchRasterDataCollection](#list_sagemaker-geospatial-action-SearchRasterDataCollection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   StartEarthObservationJob  **
  - **IAM action:**  [sagemaker-geospatial:StartEarthObservationJob](#list_sagemaker-geospatial-action-StartEarthObservationJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sagemaker-geospatial:TagResource](#list_sagemaker-geospatial-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sagemaker-geospatial.amazonaws.com / **Access level:** Write

- **   StartVectorEnrichmentJob  **
  - **IAM action:**  [sagemaker-geospatial:StartVectorEnrichmentJob](#list_sagemaker-geospatial-action-StartVectorEnrichmentJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sagemaker-geospatial:TagResource](#list_sagemaker-geospatial-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sagemaker-geospatial.amazonaws.com / **Access level:** Write

- **   StopEarthObservationJob  **
  - **IAM action:**  [sagemaker-geospatial:StopEarthObservationJob](#list_sagemaker-geospatial-action-StopEarthObservationJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopVectorEnrichmentJob  **
  - **IAM action:**  [sagemaker-geospatial:StopVectorEnrichmentJob](#list_sagemaker-geospatial-action-StopVectorEnrichmentJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [sagemaker-geospatial:TagResource](#list_sagemaker-geospatial-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [sagemaker-geospatial:UntagResource](#list_sagemaker-geospatial-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write



## Actions defined by Amazon SageMaker geospatial capabilities
<a name="list_sagemaker-geospatial-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [DeleteEarthObservationJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_DeleteEarthObservationJob.html)  **
  - **Description:** Grants permission to the DeleteEarthObservationJob operation which deletes an existing earth observation job
  - **Resource types (\*required):** [EarthObservationJob\*](#list_sagemaker-geospatial-resource-EarthObservationJob)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-geospatial-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteVectorEnrichmentJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_DeleteVectorEnrichmentJob.html)  **
  - **Description:** Grants permission to the DeleteVectorEnrichmentJob operation which deletes an existing vector enrichment job
  - **Resource types (\*required):** [VectorEnrichmentJob\*](#list_sagemaker-geospatial-resource-VectorEnrichmentJob)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-geospatial-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ExportEarthObservationJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_ExportEarthObservationJob.html)  **
  - **Description:** Grants permission to copy results of an earth observation job to an S3 location
  - **Resource types (\*required):** [EarthObservationJob\*](#list_sagemaker-geospatial-resource-EarthObservationJob)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-geospatial-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ExportVectorEnrichmentJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_ExportVectorEnrichmentJob.html)  **
  - **Description:** Grants permission to copy results of an VectorEnrichmentJob to an S3 location
  - **Resource types (\*required):** [VectorEnrichmentJob\*](#list_sagemaker-geospatial-resource-VectorEnrichmentJob)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-geospatial-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetEarthObservationJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_GetEarthObservationJob.html)  **
  - **Description:** Grants permission to return details about the earth observation job
  - **Resource types (\*required):** [EarthObservationJob\*](#list_sagemaker-geospatial-resource-EarthObservationJob)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-geospatial-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRasterDataCollection](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_GetRasterDataCollection.html)  **
  - **Description:** Grants permission to return details about the raster data collection
  - **Resource types (\*required):** [RasterDataCollection\*](#list_sagemaker-geospatial-resource-RasterDataCollection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-geospatial-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTile](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_GetTile.html)  **
  - **Description:** Grants permission to get the tile of an earth observation job
  - **Resource types (\*required):** [EarthObservationJob\*](#list_sagemaker-geospatial-resource-EarthObservationJob)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-geospatial-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetVectorEnrichmentJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_GetVectorEnrichmentJob.html)  **
  - **Description:** Grants permission to return details about the vector enrichment job
  - **Resource types (\*required):** [VectorEnrichmentJob\*](#list_sagemaker-geospatial-resource-VectorEnrichmentJob)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-geospatial-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListEarthObservationJobs](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_ListEarthObservationJobs.html)  **
  - **Description:** Grants permission to return an array of earth observation jobs associated with the current account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRasterDataCollections](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_ListRasterDataCollections.html)  **
  - **Description:** Grants permission to return an array of aster data collections associated with the given model name
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_ListTagsForResource.html)  **
  - **Description:** Grants permission to lists tag for an SageMaker Geospatial resource
  - **Resource types (\*required):** [EarthObservationJob](#list_sagemaker-geospatial-resource-EarthObservationJob) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-geospatial-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [RasterDataCollection](#list_sagemaker-geospatial-resource-RasterDataCollection) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-geospatial-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [VectorEnrichmentJob](#list_sagemaker-geospatial-resource-VectorEnrichmentJob) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-geospatial-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListVectorEnrichmentJobs](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_ListVectorEnrichmentJobs.html)  **
  - **Description:** Grants permission to return an array of vector enrichment jobs associated with the current account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [SearchRasterDataCollection](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_SearchRasterDataCollection.html)  **
  - **Description:** Grants permission to query raster data collections
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [StartEarthObservationJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_StartEarthObservationJob.html)  **
  - **Description:** Grants permission to the StartEarthObservationJob operation which starts a new earth observation job to your account
  - **Resource types (\*required):** [EarthObservationJob\*](#list_sagemaker-geospatial-resource-EarthObservationJob)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-geospatial-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-geospatial-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-geospatial-aws_TagKeys)
  - **Access level:** Write

- **   [StartVectorEnrichmentJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_StartVectorEnrichmentJob.html)  **
  - **Description:** Grants permission to the StartVectorEnrichmentJob operation which starts a new vector enrichment job to your account
  - **Resource types (\*required):** [VectorEnrichmentJob\*](#list_sagemaker-geospatial-resource-VectorEnrichmentJob)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-geospatial-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-geospatial-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-geospatial-aws_TagKeys)
  - **Access level:** Write

- **   [StopEarthObservationJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_StopEarthObservationJob.html)  **
  - **Description:** Grants permission to the StopEarthObservationJob operation which stops an existing earth observation job
  - **Resource types (\*required):** [EarthObservationJob\*](#list_sagemaker-geospatial-resource-EarthObservationJob)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-geospatial-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopVectorEnrichmentJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_StopVectorEnrichmentJob.html)  **
  - **Description:** Grants permission to the StopVectorEnrichmentJob operation which stops an existing vector enrichment job
  - **Resource types (\*required):** [VectorEnrichmentJob\*](#list_sagemaker-geospatial-resource-VectorEnrichmentJob)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-geospatial-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_TagResource.html)  **
  - **Description:** Grants permission to tag an SageMaker Geospatial resource
  - **Resource types (\*required):** [EarthObservationJob](#list_sagemaker-geospatial-resource-EarthObservationJob) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-geospatial-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-geospatial-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-geospatial-aws_TagKeys)
  - **Resource types (\*required):** [RasterDataCollection](#list_sagemaker-geospatial-resource-RasterDataCollection) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-geospatial-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-geospatial-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-geospatial-aws_TagKeys)
  - **Resource types (\*required):** [VectorEnrichmentJob](#list_sagemaker-geospatial-resource-VectorEnrichmentJob) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-geospatial-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-geospatial-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-geospatial-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_UntagResource.html)  **
  - **Description:** Grants permission to untag an SageMaker Geospatial resource
  - **Resource types (\*required):** [EarthObservationJob](#list_sagemaker-geospatial-resource-EarthObservationJob) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-geospatial-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-geospatial-aws_TagKeys)
  - **Resource types (\*required):** [RasterDataCollection](#list_sagemaker-geospatial-resource-RasterDataCollection) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-geospatial-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-geospatial-aws_TagKeys)
  - **Resource types (\*required):** [VectorEnrichmentJob](#list_sagemaker-geospatial-resource-VectorEnrichmentJob) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-geospatial-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-geospatial-aws_TagKeys)
  - **Access level:** Tagging, Write



## Resource types defined by Amazon SageMaker geospatial capabilities
<a name="list_sagemaker-geospatial-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [EarthObservationJob](https://docs.aws.amazon.com/sagemaker/latest/dg/geospatial-eoj.html)  | arn:${Partition}:sagemaker-geospatial:${Region}:${Account}:earth-observation-job/${JobID} | [aws:ResourceTag/${TagKey}](#list_sagemaker-geospatial-aws_ResourceTag___TagKey_) | 
|  [RasterDataCollection](https://docs.aws.amazon.com/sagemaker/latest/dg/geospatial-data-collections.html)  | arn:${Partition}:sagemaker-geospatial:${Region}:${Account}:raster-data-collection/${CollectionID} | [aws:ResourceTag/${TagKey}](#list_sagemaker-geospatial-aws_ResourceTag___TagKey_) | 
|  [VectorEnrichmentJob](https://docs.aws.amazon.com/sagemaker/latest/dg/geospatial-vej.html)  | arn:${Partition}:sagemaker-geospatial:${Region}:${Account}:vector-enrichment-job/${JobID} | [aws:ResourceTag/${TagKey}](#list_sagemaker-geospatial-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon SageMaker geospatial capabilities
<a name="list_sagemaker-geospatial-policy-keys"></a>

Amazon SageMaker geospatial capabilities defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of tag keys in the request | ArrayOfString | 