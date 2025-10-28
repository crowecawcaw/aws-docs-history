# Cost Optimization

HealthImaging is designed to optimize storage costs by automatically moving data to the most cost-effective access tier when access patterns change. As usage patterns change over time, intelligent tiering provides automatic lifecycle management for DICOM data without any operational overhead. HealthImaging has two storage tiers:

- **Frequent Access tier** storage for newly imported or regularly accessed DICOM data.
- **Archive Instant Access tier** storage for DICOM data that has not been accessed recently. Provides reduced storage costs for long-term archival while maintaining millisecond access latencies.
  You are billed for the aggregate storage size of all image sets in a data store. Both storage tiers are billed per GB per month, and there is no per image set fee. There are also no retrieval charges for moving data between storage tiers.

###### Note

Image sets are billed at a minimum size of 5 MB. HealthImaging accepts image sets smaller than 5 MB, but these smaller objects are charged at a 5 MB rate.

## How Intelligent Tiering Works

Your data is stored in the Frequent Access tier when new image sets are created. Image sets can be created by importing new data (through Import Jobs or DICOMweb STOW-RS) or by invoking CopyImageSet. HealthImaging automatically moves image sets that have not been accessed for 30 consecutive days to the Archive Instant Access tier, and image sets remain in Archive Instant Access tier until they are accessed again.

The following are actions that constitute access to DICOM data that automatically move image sets from the Archive Instant Access tier back to the Frequent Access tier:

- Invoking [GetImageSetMetadata](../APIReference/API_GetImageSetMetadata.md "../APIReference/API_GetImageSetMetadata.md"), [GetImageFrame](../APIReference/API_GetImageFrame.md "../APIReference/API_GetImageFrame.md"), or any [DICOMweb WADO-RS](dicomweb-retrieve.md "dicomweb-retrieve.md") action.
- Invoking [CopyImageSet](../APIReference/API_CopyImageSet.md "../APIReference/API_CopyImageSet.md") or [UpdateImageSetMetadata](../APIReference/API_UpdateImageSetMetadata.md "../APIReference/API_UpdateImageSetMetadata.md"). In the case of Copy operations, only the replicated image sets are tiered up to Frequent Access. In the case of Copy with destination, the destination image set is tiered up.
- Viewing and downloading image set data through the AWS HealthImaging management console.

The above actions both promote image sets to Frequent Access tier and prevent image sets in Frequent Access tier from tiering down to the Archive Instant Access tier for another 30 days. Access to image sets can occur via the AWS Management Console or through programmatic interfaces such as the AWS CLI or AWS SDKs. Other actions **do not** constitute access and therefore will not automatically move objects from the Archive Instant Access tier back to the Frequent Access tier. The following is a sample, not a definitive list, of such actions:

- Actions on data stores ([CreateDatastore](../APIReference/API_CreateDatastore.md "../APIReference/API_CreateDatastore.md") and [GetDatastore](../APIReference/API_GetDatastore.md "../APIReference/API_GetDatastore.md"))
- List actions ([ListDICOMImportJobs](../APIReference/API_ListDICOMImportJobs.md "../APIReference/API_ListDICOMImportJobs.md"), [ListImageSetVersions](../APIReference/API_ListImageSetVersions.md "../APIReference/API_ListImageSetVersions.md"), and [ListTagsForResource](../APIReference/API_ListTagsForResource.md "../APIReference/API_ListTagsForResource.md"))
- Search actions ([SearchImageSets](../APIReference/API_SearchImageSets.md "../APIReference/API_SearchImageSets.md") and [DICOMweb QIDO-RS](dicomweb-search.md "dicomweb-search.md") queries)
- Invoking [GetImageSet](../APIReference/API_GetImageSet.md "../APIReference/API_GetImageSet.md"), [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md"), or [UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md")
- Delete operations

Data imported to HealthImaging is charged for a minimum storage duration of 30 days. You can delete your data anytime, but each image deleted prior to 30 days after import will be charged for the remainder of the minimum duration.

## Estimating Structured Data Storage

HealthImaging stores some DICOM header information in indexed storage. You are charged for this structured storage consumption independent of the image set storage tier, and these charges are additive. You can estimate structured storage consumption by multiplying the number of DICOM resources in your data stores by the indexed record sizes per resource. The following values are approximate.

| DICOM Resource | Indexed Sizes (bytes) |
| -------------- | --------------------- |
| Study          | 1024                  |
| Series         | 830                   |
| Instance       | 680                   |
