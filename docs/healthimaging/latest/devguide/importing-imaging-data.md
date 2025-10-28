# Importing imaging data with AWS HealthImaging

Importing is the process of moving your medical imaging data from an Amazon S3 input bucket to an
AWS HealthImaging [data store](getting-started-concepts.md#concept-data-store "getting-started-concepts.md#concept-data-store"). During import, AWS HealthImaging
performs a [pixel data verification check](pixel-data-verification.md "pixel-data-verification.md") before
transforming your DICOM P10 files into [image sets](getting-started-concepts.md#concept-image-set "getting-started-concepts.md#concept-image-set")
comprised of [metadata](getting-started-concepts.md#concept-metadata "getting-started-concepts.md#concept-metadata") and [image frames](getting-started-concepts.md#concept-image-frame "getting-started-concepts.md#concept-image-frame") (pixel data).

###### Important

HealthImaging import jobs process DICOM instance binaries (`.dcm` files) and transform
them into image sets. Use HealthImaging [cloud native actions](../APIReference/API_Operations.md "../APIReference/API_Operations.md")
(APIs) to manage data stores and image sets. Use HealthImaging's [representation of DICOMweb services](using-dicomweb.md "using-dicomweb.md") to return DICOMweb responses.

The following topics describe how to import your medical imaging data into an HealthImaging data
store using the AWS Management Console, AWS CLI, and AWS SDKs.

###### Topics

- [Understanding import jobs](understanding-import-jobs.md "understanding-import-jobs.md")
- [Starting an import job](start-dicom-import-job.md "start-dicom-import-job.md")
- [Getting import job properties](get-dicom-import-job.md "get-dicom-import-job.md")
- [Listing import jobs](list-dicom-import-jobs.md "list-dicom-import-jobs.md")
