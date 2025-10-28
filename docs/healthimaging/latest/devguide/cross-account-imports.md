# Cross-account import for AWS HealthImaging

With cross-account/cross-region import, you can import data into your HealthImaging [data store](getting-started-concepts.md#concept-data-store "getting-started-concepts.md#concept-data-store") from Amazon S3 buckets located in other [supported Regions](endpoints-quotas.md#endpoints "endpoints-quotas.md#endpoints"). You can import data across AWS accounts,
accounts owned by other [AWS
Organizations](../../../glossary/latest/reference/glos-chap.md#awsorganizations "../../../glossary/latest/reference/glos-chap.md#awsorganizations"), and from open data sources like [Imaging Data Commons
(IDC)](https://registry.opendata.aws/nci-imaging-data-commons/ "https://registry.opendata.aws/nci-imaging-data-commons/") located in the [Registry of
Open Data on AWS](https://registry.opendata.aws/ "https://registry.opendata.aws/").

HealthImaging cross-account/cross-region import use cases include:

- Medical imaging SaaS products importing DICOM data from customer accounts
- Large organizations populating one HealthImaging data store from many Amazon S3 input
  buckets
- Researchers securely sharing data across multi-institution clinical studies

###### To use cross-account import

1. The Amazon S3 input (source) bucket owner must grant the HealthImaging data store owner
   `s3:ListBucket` and `s3:GetObject` permissions.
2. The HealthImaging data store owner must add the Amazon S3 bucket to their IAM
   `ImportJobDataAccessRole`. See [Create an IAM role for
   import](getting-started-setting-up.md#setting-up-create-iam-role-import "getting-started-setting-up.md#setting-up-create-iam-role-import").
3. The HealthImaging data store owner must provide the [`inputOwnerAccountId`](../APIReference/API_StartDICOMImportJob.md#healthimaging-StartDICOMImportJob-request-inputOwnerAccountId "../APIReference/API_StartDICOMImportJob.md#healthimaging-StartDICOMImportJob-request-inputOwnerAccountId") for the Amazon S3 input bucket when starting
   the import job.

###### Note

By providing the `inputOwnerAccountId`, the data store owner
validates the input Amazon S3 bucket belongs to the specified account to maintain
compliance with industry standards and mitigate potential security risks.

The following `startDICOMImportJob` code example includes the optional
`inputOwnerAccountId` parameter, which can be applied to all AWS CLI
and SDK code examples in the [Starting an import job](start-dicom-import-job.md "start-dicom-import-job.md") section.

Java

```
public static String startDicomImportJob(MedicalImagingClient medicalImagingClient,
        String jobName,
        String datastoreId,
        String dataAccessRoleArn,
        String inputS3Uri,
        String outputS3Uri,
        String inputOwnerAccountId) {

    try {
        StartDicomImportJobRequest startDicomImportJobRequest = StartDicomImportJobRequest.builder()
                .jobName(`jobName`)
                .datastoreId(`datastoreId`)
                .dataAccessRoleArn(`dataAccessRoleArn`)
                .inputS3Uri(`inputS3Uri`)
                .outputS3Uri(`outputS3Uri`)
                .inputOwnerAccountId(`inputOwnerAccountId`)
                .build();
        StartDicomImportJobResponse response = medicalImagingClient.startDICOMImportJob(startDicomImportJobRequest);
        return response.jobId();
    } catch (MedicalImagingException e) {
        System.err.println(e.awsErrorDetails().errorMessage());
        System.exit(1);
    }

    return "";
}

```
