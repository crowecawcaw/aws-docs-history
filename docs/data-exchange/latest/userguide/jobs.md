# Jobs in AWS Data Exchange

AWS Data Exchange jobs are asynchronous import or export operations.

As a provider of data products in AWS Data Exchange, you can create and manage your data sets that you
want to publish to a product. You can download (export) or copy your assets or revisions to
Amazon Simple Storage Service (Amazon S3) or a signed URL. In addition, providers can import assets from an Amazon API Gateway API
or import assets from an Amazon Redshift data set.

As a subscriber, you can view and access the data sets that you have an entitlement to
through a subscription. You can use the API operations to download (export) or copy your
entitled data sets to Amazon S3 for use with a variety of AWS analytics and machine learning
services.

To create or copy assets or copy revisions through jobs, you can use the AWS Management Console,
AWS Command Line Interface (AWS CLI), your own REST application, or one of the AWS SDKs.

Jobs are deleted 90 days after they are created.

###### Topics

- [Job properties](#job-properties "#job-properties")
- [AWS Regions and jobs](#jobs-regions "#jobs-regions")
- [Importing assets to AWS Data Exchange](importing-assets.md "importing-assets.md")
- [Exporting assets from AWS Data Exchange](exporting-assets.md "exporting-assets.md")
- [Exporting revisions from AWS Data Exchange](exporting-revisions.md "exporting-revisions.md")

## Job properties

Jobs have the following properties:

- **Job ID** – An ID generated when the job is
  created that uniquely identifies the job.
- **Job type** – The following job types are
  supported:
  - Import from Amazon S3
  - Import an AWS Lake Formation
    data
    permission (Preview)
  - Import from signed URL
  - Import from Amazon API Gateway API
  - Import from an AWS Data Exchange datashare for Amazon Redshift
  - Import an Amazon S3 data access
  - Export to Amazon S3
  - Export to signed URL

- **Amazon Resource Name (ARN)** – A unique
  identifier for AWS resources.
- **Job state** – The job states are
  `WAITING`, `IN_PROGRESS`, `COMPLETED`,
  `CANCELLED`, `ERROR`, or `TIMED_OUT`. When a job is
  created, it's in the `WAITING` state until the job is started.
- **Job details** – Details of the operation to be
  performed by the job, such as export destination details or import source details.

###### Example job resource

```
{
    "Arn": "arn:aws:dataexchange:us-east-1:`123456789012`:jobs/`6cEXAMPLE818f7c7a23b3d0EXAMPLE1c`",
    "Id": "`6cEXAMPLE818f7c7a23b3d0EXAMPLE1c`",
    "State": "COMPLETED",
    "Type": "IMPORT_ASSETS_FROM_S3",
    "CreatedAt": "2019-10-11T14:12:24.640Z",
    "UpdatedAt": "2019-10-11T14:13:00.804Z",
    "Details": {
        "ImportAssetsFromS3": {
            "AssetSources": [
                {
                    "Bucket": "amzn-s3-demo-bucket",
                    "Key": "`MyKey`"
                }
            ],
            "DataSetId": "14EXAMPLE4460dc9b005a0dEXAMPLE2f",
            "RevisionId": "e5EXAMPLE224f879066f999EXAMPLE42"
        }
    }
}
```

## AWS Regions and jobs

If you import or export an asset to or from an Amazon S3 bucket that is in an AWS Region that
is different than the data set's Region, your AWS account is charged for the data transfer
costs, according to Amazon S3 data transfer pricing policies.

If you export assets to a signed URL, your AWS account is charged for data transfer
costs from Amazon S3 to the internet according to [Amazon S3
pricing policies](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

When your subscription to an AWS Data Exchange for Files data set ends, you retain access to any files
that you already exported. Review your Data Subscription Agreement to verify if your agreement
requires that you delete exported data when ending a subscription.
