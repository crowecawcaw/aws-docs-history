# Output types for delivery to an AWS

service

This table describes options that you can use to send output from
Elemental Live to a downstream system that is an AWS service. Each row
describes a different use case.

The rows are sorted by downstream system (destination AWS
service). The _Released_ column
identifies the version of Elemental Live that introduced the output
group type.

| Downstream system                                                   | Type of output           | Description                                                                                                                                                                                               | Type of output group | Output option (if any)                                | Supported protocol                   | Live output supported | VOD output supported | Released      |
| ------------------------------------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | ----------------------------------------------------- | ------------------------------------ | --------------------- | -------------------- | ------------- |
| Amazon S3                                                           | DASH                     | Send DASH content to Amazon S3 .                                                                                                                                                                          | DASH                 |                                                       | Custom protocol: s3:// or s3ssl://   | Yes                   | Yes                  | 2.14.3        |
| Amazon S3                                                           | HLS                      | Send HLS content to an Amazon S3 bucket.                                                                                                                                                                  | HLS                  | A TS container or an fMP4 container                   | Custom protocol: s3:// or s3ssl://   | Yes                   | Yes                  | Before 2.14.0 |
| Amazon S3                                                           | JPEG frame capture files | Send JPEG files to an Amazon S3 bucket.                                                                                                                                                                   | Archive              | Raw (no container)                                    | Custom protocol: s3:// or s3ssl://   | No                    | Yes                  | Before 2.14.0 |
| Amazon S3                                                           | VOD files                | Send compressed VOD output to an Amazon S3 bucket.                                                                                                                                                        | Archive              | Various containers are supported. See the list below. | Custom protocol: s3:// or s3ssl://   | No                    | Yes                  | Before 2.14.0 |
| AWS Elemental MediaConnect                                          | Transport stream         | Send a redundant transport stream (TS) to a Zixi push<br>flow on MediaConnect                                                                                                                             | Reliable TS          | AWS Elemental MediaConnect option. See Note A.        | Not applicable                       | Yes                   | No                   | 2.14.3        |
| AWS Elemental MediaConnect                                          | Transport stream         | Send a redundant transport stream (TS) to an SRT<br>listener flow on MediaConnect.                                                                                                                        | Reliable TS          | AWS Elemental MediaConnect option. See Note B         | Not applicable                       | Yes                   | No                   | 2.14.3        |
| AWS Elemental MediaConnect, via Direct Connect to your own AWS VPC. | SMPTE 2110 stream        | Send a JPEG XS SMPTE 2110 stream to MediaConnect. SMPTE 2110<br>requires redundant inputs when sending to MediaConnect. Note<br>that you can't send an uncompressed SMPTE 2110 stream to<br>MediaConnect. | SMPTE 2110           |                                                       | rtp://                               | Yes                   | No                   | 2.22.0        |
| AWS Elemental MediaStore                                            | DASH                     | Send DASH content to MediaStore.                                                                                                                                                                          | DASH                 |                                                       | Custom protocol: ems:// or emsssl:// | Yes                   | Yes                  | 2.14.3        |
| AWS Elemental MediaStore                                            | HLS                      | Send HLS content to a container on MediaStore.                                                                                                                                                            | HLS                  | A TS container or an fMP4 container                   | Custom protocol: ems:// or emsssl:// | Yes                   | Yes                  | 2.14.3        |
| AWS Elemental MediaPackage                                          | HLS                      | Send HLS content to a MediaPackage channel using the HTTPS<br>protocol. The MediaPackage channel must be on your own AWS<br>account.                                                                      | HLS                  | A TS container                                        | https://                             | Yes                   | No                   | Before 2.14.0 |
| AWS Elemental MediaPackage<br>v2                                    | HLS                      | Send HLS content to a channel in MediaPackage v2 using the HTTPS protocol. The<br>output is typically (but not necessarily) part of a glass-to-glass low<br>latency workflow.                             | HLS                  | A TS container                                        | https://                             | Yes                   | No                   | 2.25.0        |

Note A. You could send to a MediaConnect Zixi flow using the Zixi option,
but the AWS Elemental MediaConnect option provides a seamless
integration with MediaConnect. The Zixi option is designed for destinations
other than MediaConnect.

Note B. You could send to a MediaConnect SRT flow using the SRT option, but
the AWS Elemental MediaConnect option provides a seamless integration
with MediaConnect. The SRT option is designed for destinations other than
MediaConnect.
