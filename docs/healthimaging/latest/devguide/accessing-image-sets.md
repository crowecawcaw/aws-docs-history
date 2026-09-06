

# Accessing image sets with AWS HealthImaging
<a name="accessing-image-sets"></a>

Accessing medical imaging data in AWS HealthImaging typically involves searching for an [image set](getting-started-concepts.md#concept-image-set) with a unique key and getting the associated [metadata](getting-started-concepts.md#concept-metadata) and [image frames](getting-started-concepts.md#concept-image-frame) (pixel data).

**Important**  
During import, HealthImaging processes DICOM instance binaries (`.dcm` files) and transforms them into image sets. Use HealthImaging [cloud native actions](https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_Operations.html) (APIs) to manage data stores and image sets. Use HealthImaging's [representation of DICOMweb services](dicomweb-retrieve.md) to return DICOMweb responses.

The following topics explain how to use HealthImaging cloud native actions in the AWS Management Console, AWS CLI, and AWS SDKs to search image sets and get their associated properties, metadata, and image frames.

**Topics**
+ [Understanding image sets](understanding-image-sets.md)
+ [Searching image sets](search-image-sets.md)
+ [Getting image set properties](get-image-set-properties.md)
+ [Getting image set metadata](get-image-set-metadata.md)
+ [Getting image set pixel data](get-image-frame.md)