# Modifying image sets with AWS HealthImaging

DICOM import jobs typically require you to modify your [image sets](getting-started-concepts.md#concept-image-set "getting-started-concepts.md#concept-image-set") for the following reasons:

- Patient safety
- Data consistency
- Reduce storage costs

###### Important

During import, HealthImaging processes DICOM instance binaries (`.dcm` files) and
transforms them into image sets. Use HealthImaging [cloud native actions](../APIReference/API_Operations.md "../APIReference/API_Operations.md")
(APIs) to manage data stores and image sets. Use HealthImaging's [representation of DICOMweb services](using-dicomweb.md "using-dicomweb.md") to return DICOMweb responses.

HealthImaging provides several cloud native APIs to simplify the image set modification process. The
following topics describe how to modify image sets using AWS CLI and AWS SDKs.

###### Topics

- [Listing image set versions](list-image-set-versions.md "list-image-set-versions.md")
- [Updating image set metadata](update-image-set-metadata.md "update-image-set-metadata.md")
- [Copying an image set](copy-image-set.md "copy-image-set.md")
- [Deleting an image set](delete-image-set.md "delete-image-set.md")
