# Retrieving DICOM data from HealthImaging

AWS HealthImaging offers representations of [`DICOMweb WADO-RS`](https://www.dicomstandard.org/using/dicomweb/retrieve-wado-rs-and-wado-uri "https://www.dicomstandard.org/using/dicomweb/retrieve-wado-rs-and-wado-uri") APIs
to retrieve data at the series and instance levels. With these APIs, it is possible to retrieve
all metadata for a DICOM series from a HealthImaging [data store](getting-started-concepts.md#concept-data-store "getting-started-concepts.md#concept-data-store").
It is also possible to retrieve a DICOM instance, DICOM instance metadata, and DICOM instance
frames (pixel data). HealthImaging's `DICOMweb WADO-RS` APIs offer flexibility in how you
retrieve data stored in HealthImaging and provide interoperability with legacy applications.

###### Important

HealthImaging stores DICOM data as [image sets](getting-started-concepts.md#concept-image-set "getting-started-concepts.md#concept-image-set"). Use HealthImaging
[cloud
native actions](../APIReference/API_Operations.md "../APIReference/API_Operations.md") to manage and retrieve image sets. HealthImaging's DICOMweb APIs can be used to
return image set information with DICOMweb-conformant responses.

The APIs listed in this section are built in conformance to the DICOMweb (WADO-RS) standard
for web-based medical imaging. Because they are representations of DICOMweb APIs, they are not
offered through AWS CLI and AWS SDKs.

The following table describes all HealthImaging representations of DICOMweb WADO-RS APIs available
for retrieving data from HealthImaging.

| HealthImaging representations of DICOMweb WADO-RS APIs | Name                                                                                                                                                                                                                                                                                                                            | Description |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `GetDICOMSeriesMetadata`                               | Retrieve DICOM instance metadata (`.json` file) for a DICOM series in a HealthImaging data store by specifying<br>the Study and Series UIDs associated with a resource. See [Retrieve series metadata](dicomweb-retrieve-series-metadata.md "dicomweb-retrieve-series-metadata.md").                                            |
| `GetDICOMInstance`                                     | Retrieve a DICOM instance (`.dcm` file) from a HealthImaging data store by specifying<br>the Series, Study, and Instance UIDs associated with a resource. See [Retrieve an instance](dicomweb-retrieve-instance.md "dicomweb-retrieve-instance.md").                                                                            |
| `GetDICOMInstanceMetadata`                             | Retrieve DICOM instance metadata (`.json` file) from a DICOM instance in a<br>HealthImaging data store by specifying the Series, Study, and Instance UIDs associated with a<br>resource. See [Retrieve instance metadata](dicomweb-retrieve-instance-metadata.md "dicomweb-retrieve-instance-metadata.md").                     |
| `GetDICOMInstanceFrames`                               | Retrieve single or batch image frames (`multipart` request) from a DICOM<br>instance in a HealthImaging data store by specifying the Series UID, Study UID, Instance UIDs, and<br>frame numbers associated with a resource. See [Retrieve frames](dicomweb-retrieve-instance-frames.md "dicomweb-retrieve-instance-frames.md"). |

###### Topics

- [Getting a DICOM instance from HealthImaging](dicomweb-retrieve-instance.md "dicomweb-retrieve-instance.md")
- [Getting DICOM instance metadata from
  HealthImaging](dicomweb-retrieve-instance-metadata.md "dicomweb-retrieve-instance-metadata.md")
- [Getting DICOM series metadata from
  HealthImaging](dicomweb-retrieve-series-metadata.md "dicomweb-retrieve-series-metadata.md")
- [Getting DICOM instance frames from
  HealthImaging](dicomweb-retrieve-instance-frames.md "dicomweb-retrieve-instance-frames.md")
- [Getting DICOM bulkdata from HealthImaging](dicom-retrieve-bulkdata.md "dicom-retrieve-bulkdata.md")
