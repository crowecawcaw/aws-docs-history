# AWS HealthImaging endpoints and quotas

The following topics contain information about AWS HealthImaging service endpoints and
quotas.

###### Topics

- [Service endpoints](#endpoints "#endpoints")
- [Service quotas](#quotas "#quotas")

## Service endpoints

A service endpoint is a URL that identifies a host and port as the entry point for a
web service. Every web service request contains an endpoint. Most AWS services provide
endpoints for specific Regions to enable faster connectivity. The following table lists
the service endpoints for AWS HealthImaging.

| Region Name           | Region         | Endpoint                                     | Protocol |
| --------------------- | -------------- | -------------------------------------------- | -------- |
| US East (N. Virginia) | us-east-1      | medical-imaging.us-east-1.amazonaws.com      | HTTPS    |
| US West (Oregon)      | us-west-2      | medical-imaging.us-west-2.amazonaws.com      | HTTPS    |
| Asia Pacific (Sydney) | ap-southeast-2 | medical-imaging.ap-southeast-2.amazonaws.com | HTTPS    |
| Europe (Ireland)      | eu-west-1      | medical-imaging.eu-west-1.amazonaws.com      | HTTPS    |

If you are using HTTP requests to call AWS HealthImaging actions, you must use different
endpoints depending on the actions being called. The following menu lists the available
service endpoints for HTTP requests and the actions they support.

data store, import, tagging
The following _data store_,
_import_, and _tagging_
actions are accessible via endpoint:

`https://medical-imaging.`region`.amazonaws.com`

- CreateDatastore

- GetDatastore

- ListDatastores

- DeleteDatastore

- StartDICOMImportJob

- GetDICOMImportJob

- ListDICOMImportJobs

- TagResource

- ListTagsForResource

- UntagResource

image set
The following _image set_ actions are
accessible via endpoint:

```
https://runtime-medical-imaging.`region`.amazonaws.com

```

- SearchImageSets

- GetImageSet

- GetImageSetMetadata

- GetImageFrame

- ListImageSetVersions

- UpdateImageSetMetadata

- CopyImageSet

- DeleteImageSet

DICOMweb
HealthImaging offers a representations of DICOMweb Retrieve
WADO-RS services. For more information, see [Retrieving DICOM data from HealthImaging](dicomweb-retrieve.md "dicomweb-retrieve.md").

The following DICOMweb services are accessible via
endpoint:

```
https://dicom-medical-imaging.`region`.amazonaws.com

```

- `GetDICOMInstance`
- `GetDICOMInstanceMetadata`
- `GetDICOMInstanceFrames`

## Service quotas

Service quotas are defined as the maximum value for your resources, actions, and items
in your AWS account.

###### Note

For adjustable quotas, you can request a quota increase using the [Service Quotas console](https://console.aws.amazon.com/servicequotas/ "https://console.aws.amazon.com/servicequotas/"). For more
information, see [Requesting a
quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _Service Quotas User Guide_.

The following table lists the default quotas for AWS HealthImaging.

| Name                                                                                | Default                                                        | Adjustable                                                                                                                                                                                         | Description                                                                                                       |
| ----------------------------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Maximum concurrent CopyImageSet requests per data store                             | Each supported Region: 100                                     | [Yes](https://console.aws.amazon.com/servicequotas/home/services/medical-imaging/quotas/L-0D1B2633 "https://console.aws.amazon.com/servicequotas/home/services/medical-imaging/quotas/L-0D1B2633") | The maximum concurrent CopyImageSet requests per data store in the current AWS Region                             |
| Maximum concurrent DeleteImageSet requests per data store                           | Each supported Region: 100                                     | [Yes](https://console.aws.amazon.com/servicequotas/home/services/medical-imaging/quotas/L-2020885D "https://console.aws.amazon.com/servicequotas/home/services/medical-imaging/quotas/L-2020885D") | The maximum concurrent DeleteImageSet requests per data store in the current AWS Region                           |
| Maximum concurrent UpdateImageSetMetadata requests per data store                   | Each supported Region: 100                                     | [Yes](https://console.aws.amazon.com/servicequotas/home/services/medical-imaging/quotas/L-8588E9BF "https://console.aws.amazon.com/servicequotas/home/services/medical-imaging/quotas/L-8588E9BF") | The maximum concurrent UpdateImageSetMetadata requests per data store in the current AWS Region                   |
| Maximum concurrent import jobs per data store                                       | ap-southeast-2: 20<br>Each of the other supported Regions: 100 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/medical-imaging/quotas/L-23763099 "https://console.aws.amazon.com/servicequotas/home/services/medical-imaging/quotas/L-23763099") | The maximum number of concurrent import jobs per data store in the current AWS Region                             |
| Maximum data stores                                                                 | Each supported Region: 10                                      | [Yes](https://console.aws.amazon.com/servicequotas/home/services/medical-imaging/quotas/L-8829B870 "https://console.aws.amazon.com/servicequotas/home/services/medical-imaging/quotas/L-8829B870") | The maximum number of active data stores in the current AWS Region                                                |
| Maximum number of ImageFrames allowed to be copied per CopyImageSet request         | Each supported Region: 1,000                                   | [Yes](https://console.aws.amazon.com/servicequotas/home/services/medical-imaging/quotas/L-164416ED "https://console.aws.amazon.com/servicequotas/home/services/medical-imaging/quotas/L-164416ED") | The maximum number of ImageFrames allowed to be copied per CopyImageSet request in the current AWS Region         |
| Maximum number of files in a DICOM import job                                       | Each supported Region: 5,000                                   | [Yes](https://console.aws.amazon.com/servicequotas/home/services/medical-imaging/quotas/L-685AAB3A "https://console.aws.amazon.com/servicequotas/home/services/medical-imaging/quotas/L-685AAB3A") | The maximum number of files in a DICOM import job in the current AWS Region                                       |
| Maximum number of nested folders in a DICOM import job                              | Each supported Region: 10,000                                  | No                                                                                                                                                                                                 | The maximum number of nested folders in a DICOM import job in the current AWS Region                              |
| Maximum payload size limit (in KB) accepted by UpdateImageSetMetadata               | Each supported Region: 10 Kilobytes                            | [Yes](https://console.aws.amazon.com/servicequotas/home/services/medical-imaging/quotas/L-A880A4C2 "https://console.aws.amazon.com/servicequotas/home/services/medical-imaging/quotas/L-A880A4C2") | The maximum payload size limit (in KB) accepted by UpdateImageSetMetadata in the current AWS Region               |
| Maximum size (in GB) of all files in a DICOM import job                             | Each supported Region: 10 Gigabytes                            | No                                                                                                                                                                                                 | The maximum size (in GB) of all files in a DICOM import job in the current AWS Region                             |
| Maximum size (in GB) of each DICOM P10 file in a DICOM import job                   | Each supported Region: 4 Gigabytes                             | No                                                                                                                                                                                                 | The maximum size (in GB) of each DICOM P10 file in the DICOM import job in the current AWS Region                 |
| Maximum size limit (in MB) on ImageSetMetadata per Import, Copy, and UpdateImageSet | Each supported Region: 50 Megabytes                            | [Yes](https://console.aws.amazon.com/servicequotas/home/services/medical-imaging/quotas/L-AD2C6765 "https://console.aws.amazon.com/servicequotas/home/services/medical-imaging/quotas/L-AD2C6765") | The maximum size limit (in MB) on ImageSetMetadata per Import, Copy, and UpdateImageSet in the current AWS Region |
