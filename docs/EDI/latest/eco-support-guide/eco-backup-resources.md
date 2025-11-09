# Resources that EDI Cloud Operations back up

The following table lists the AWS resources that ECO backs up for EDI with the default backup up plan.

| AWS resource                              | Purpose                                                                                                                                                                                                                                                          |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Data Platform**                         |
| DynamoDB                                  | Persistent storage for OSDU management data, reference data, and metadata                                                                                                                                                                                        |
| Aurora PostgreSQL                         | Reservoir Domain Data Management Service (DDMS)                                                                                                                                                                                                                  |
| Amazon S3 (optional)                      | Persistent storage for all data records                                                                                                                                                                                                                          |
| Amazon EBS                                | Volume storage that Amazon EKS persistent volume claims use. Applications that run in Amazon EKS, such as MongoDB to store data entitlements for<br>authorization, and Amazon OpenSearch Service to store indexes and saved searches, require persistent storage |
| **EDI IQ**                                |
| DynamoDB                                  | Table that contains the EDI IQ Terraform state files                                                                                                                                                                                                             |
| RDS for MySQL                             | Persistent storage for EDI IQ job scans and ingestion statuses                                                                                                                                                                                                   |
| Amazon S3 \*_delta_lake_<br>• folder only | The \*_delta_lake_<br>• folder containing the metadata of scanned data. Backed using an Amazon S3 replication rule                                                                                                                                               |

###### Note

By default, ECO doesn't back up the Amazon S3 data from your Data Platform account that contains OSDU data records. ECO uses the default backup plan to back up
the **delta_lake** folder that contains ingestion metadata from the Amazon S3 source bucket for the EDI IQ console.

If you require changes to the default backup plan, work with your E-SDM during onboarding. Or submit a service request from your account.
