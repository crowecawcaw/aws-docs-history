# Integrity of Data in AWS Backup

## AWS Backup data integrity goal

AWS Backup seeks to maintain integrity during transmission, storage, and processing of
your data. AWS Backup treats stored resource data as content-agnostic critical information,
in that we offer the same high level of security to customers, regardless of the type of
data you store. We are vigilant about our customers' security and have implemented
sophisticated technical and physical measures against unauthorized access. You retain
complete control over how your data is classified, the Regions in which you store your data,
and how you control, archive, and protect your data against disclosure.

## AWS Backup data integrity implementation

AWS Backup works in concert with other AWS and Amazon services to maintain integrity of
the data it stores and with which it interacts. The tools used may vary and can include (but
are not limited to):

- Continuous object validation against their checksum to prevent object corruption
- Internal checksums to confirm integrity of data in transit and at rest
- Checksums calculated on data in backups created from the primary store
- Checksums are always verified to be correct before using the corresponding data. If we find data that doesn't match its checksum, we replace it with a correct copy. If we fail to replace the correct copy, we will fail the corresponding jobs
- Automatic attempt to restore normal levels of object storage redundancy in the event
  of disk corruption or detection of device failure
- Redundant storage of data across multiple physical locations
- Object durability enhancement across multiple availability zones during the initial
  write, combined with further replication in the event of device unavailability or
  detected bit-rot
- Checksums on all network traffic to detect corruption of data packets when storing
  or retrieving data

AWS Backup natively stores data for Amazon DynamoDB with advanced features, Amazon EFS, Amazon S3,
Amazon Timestream, and virtual machines running with VMware connected through Backup gateway. AWS Backup
facilitates backups of data stored with other services, including Amazon Aurora, Amazon DocumentDB,
Amazon DynamoDB, Amazon EBS,
Amazon EC2, Amazon FSx for Windows File Server, Amazon FSx for Lustre, Amazon FSx for OpenZFS, Amazon FSx for NetApp ONTAP, Amazon Neptune,
Amazon RDS, and Amazon Redshift.

## Objective confirmation and audit of

AWS Backup data integrity

The data stored directly by AWS Backup and the data stored in partnership with fellow AWS
services with which AWS Backup interacts is subjected to the rigorous process of Amazon Simple Storage Service (Amazon S3)
underpinning this data integrity. This integrity is confirmed by an independent, third-party
auditor through an annual SOC audit report which is available through [AWS Artifact](https://aws.amazon.com/artifact/ "https://aws.amazon.com/artifact/").
