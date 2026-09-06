

# AWS HealthImaging endpoints and quotas
<a name="healthimaging"></a>

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints. Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md).

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account. For more information, see [AWS service quotas](aws_service_limits.md).

The following are the service endpoints and service quotas for this service.

## Service endpoints
<a name="healthimaging-region"></a>


| Region Name | Region | Endpoint | Protocol | 
| --- | --- | --- | --- | 
| US East (N. Virginia) | us-east-1 |  medical-imaging.us-east-1.amazonaws.com <br /> medical-imaging-fips.us-east-1.amazonaws.com  | HTTPS<br />HTTPS | 
| US West (Oregon) | us-west-2 |  medical-imaging.us-west-2.amazonaws.com <br /> medical-imaging-fips.us-west-2.amazonaws.com  | HTTPS<br />HTTPS | 
| Asia Pacific (Sydney) | ap-southeast-2 |  medical-imaging.ap-southeast-2.amazonaws.com  | HTTPS | 
| Europe (Ireland) | eu-west-1 |  medical-imaging.eu-west-1.amazonaws.com  | HTTPS | 
| Europe (London) | eu-west-2 |  medical-imaging.eu-west-2.amazonaws.com  | HTTPS | 

If you are using HTTP requests to call AWS HealthImaging API actions, you must use two different endpoints depending on the actions being called. The following menu lists the available service endpoints for HTTP requests and the actions they support.

### Supported API actions for HTTP requests
<a name="supported-runtime-apis"></a>

Using HTTP requests, the following *data store*, *import*, and *tagging* actions are accessible via endpoint:

`https://medical-imaging.{{region}}.amazonaws.com`
+ CreateDatastore
+ GetDatastore
+ ListDatastores
+ DeleteDatastore
+ StartDICOMImportJob
+ GetDICOMImportJob
+ ListDICOMImportJobs
+ TagResource
+ ListTagsForResource
+ UntagResource

Using HTTP requests, the following *runtime* actions are accessible via endpoint:

`https://runtime-medical-imaging.{{region}}.amazonaws.com`
+ SearchImageSets
+ GetImageSet
+ GetImageSetMetadata
+ GetImageFrame
+ ListImageSetVersions
+ UpdateImageSetMetadata
+ CopyImageSet
+ DeleteImageSet

## Service quotas
<a name="health-imaging-quotas"></a>


| Name | Default | Adjustable | Description | 
| --- | --- | --- | --- | 
| Maximum concurrent CopyImageSet requests per data store | Each supported Region: 100 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/medical-imaging/quotas/L-0D1B2633)  | The maximum concurrent CopyImageSet requests per data store in the current AWS Region | 
| Maximum concurrent DeleteImageSet requests per data store | Each supported Region: 100 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/medical-imaging/quotas/L-2020885D)  | The maximum concurrent DeleteImageSet requests per data store in the current AWS Region | 
| Maximum concurrent UpdateImageSetMetadata requests per data store | Each supported Region: 100 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/medical-imaging/quotas/L-8588E9BF)  | The maximum concurrent UpdateImageSetMetadata requests per data store in the current AWS Region | 
| Maximum concurrent import jobs per data store | ap-southeast-2: 20<br />Each of the other supported Regions: 100 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/medical-imaging/quotas/L-23763099)  | The maximum number of concurrent import jobs per data store in the current AWS Region | 
| Maximum data stores | Each supported Region: 100 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/medical-imaging/quotas/L-8829B870)  | The maximum number of active data stores in the current AWS Region | 
| Maximum number of ImageFrames allowed to be copied per CopyImageSet request | Each supported Region: 1,000 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/medical-imaging/quotas/L-164416ED)  | The maximum number of ImageFrames allowed to be copied per CopyImageSet request in the current AWS Region | 
| Maximum number of files in a DICOM import job | Each supported Region: 5,000 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/medical-imaging/quotas/L-685AAB3A)  | The maximum number of files in a DICOM import job in the current AWS Region | 
| Maximum number of nested folders in a DICOM import job | Each supported Region: 10,000 | No | The maximum number of nested folders in a DICOM import job in the current AWS Region | 
| Maximum payload size limit (in KB) accepted by UpdateImageSetMetadata | Each supported Region: 10 Kilobytes |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/medical-imaging/quotas/L-A880A4C2)  | The maximum payload size limit (in KB) accepted by UpdateImageSetMetadata in the current AWS Region | 
| Maximum size (in GB) of all files in a DICOM import job | Each supported Region: 10 Gigabytes | No | The maximum size (in GB) of all files in a DICOM import job in the current AWS Region | 
| Maximum size (in GB) of each DICOM P10 file in a DICOM import job | Each supported Region: 10 Gigabytes | No | The maximum size (in GB) of each DICOM P10 file in the DICOM import job in the current AWS Region | 
| Maximum size limit (in MB) on ImageSetMetadata per Import, Copy, and UpdateImageSet | Each supported Region: 50 Megabytes |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/medical-imaging/quotas/L-AD2C6765)  | The maximum size limit (in MB) on ImageSetMetadata per Import, Copy, and UpdateImageSet in the current AWS Region | 