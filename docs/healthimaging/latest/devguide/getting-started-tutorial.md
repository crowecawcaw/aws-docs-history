# AWS HealthImaging tutorial

###### Objective

The objective of this tutorial is to import DICOM P10 binaries (`.dcm` files)
into an AWS HealthImaging [data store](getting-started-concepts.md#concept-data-store "getting-started-concepts.md#concept-data-store") and transform them into
[image sets](getting-started-concepts.md#concept-image-set "getting-started-concepts.md#concept-image-set") comprised of [metadata](getting-started-concepts.md#concept-metadata "getting-started-concepts.md#concept-metadata") and [image
frames](getting-started-concepts.md#concept-image-frame "getting-started-concepts.md#concept-image-frame") (pixel data). After importing the DICOM data, you use HealthImaging cloud native actions
to access the image sets, metadata, and image frames based on your [access preference](what-is.md#what-is-accessing "what-is.md#what-is-accessing").

###### Prerequisites

All procedures listed in [Setting up](getting-started-setting-up.md "getting-started-setting-up.md") are required to complete this
tutorial.

###### Tutorial steps

1. [Start import job](start-dicom-import-job.md "start-dicom-import-job.md")
2. [Get import job properties](get-dicom-import-job.md "get-dicom-import-job.md")
3. [Search image sets](search-image-sets.md "search-image-sets.md")
4. [Get image set properties](get-image-set-properties.md "get-image-set-properties.md")
5. [Get image set metadata](get-image-set-metadata.md "get-image-set-metadata.md")
6. [Get image set pixel data](get-image-frame.md "get-image-frame.md")
7. [Delete data store](delete-data-store.md "delete-data-store.md")
