AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/ "https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/")

# Create a pipeline from Data Pipeline templates using the CLI

Data Pipeline provides several pre-configured pipeline definitions, known as templates. You can use templates to get started with AWS Data Pipeline quickly. These templates are available in a public bucket at the Amazon S3 location: `s3://datapipeline-us-east-1/templates/`. These predefined templates are created to achieve specific use cases and can be used to create pipelines. You can use `aws s3 ls --recursive "s3://datapipeline-us-east-1/templates/"` to list all the available templates.

## Create a pipeline from a template using the CLI

Assume you want to create a pipeline that exports a DynamoDB table to Amazon S3. The template to be used in this case can be found at: `s3://datapipeline-us-east-1/templates/DynamoDB Templates/Export DynamoDB table to S3.json`.

###### To download the template JSON and create a pipeline using the CLI

1. Download the template using the `aws s3 cp` CLI or curl. For example:

```
aws s3 cp "s3://datapipeline-us-east-1/templates/DynamoDB Templates/Export DynamoDB table to S3.json" <destination directory>
```

2. Make changes to the downloaded template as needed. For example, to use latest EMR release version, change the `releaseLabel` field in `EmrClusterForBackup` object, change the master and core instance types, and change the default values of parameters in the template.
3. Create a pipeline using the `create-pipeline` CLI. For example:

```
aws datapipeline create-pipeline --name my-ddb-backup-pipeline --unique-id my-ddb-backup-pipeline --region ap-northeast-1
```

4. Note the created pipeline ID.
5. Use `put-pipeline-definition` to upload the definition. Provide values of the parameters whose default values you want to override using the `--parameter-values` option.

For more information about templates, see [Choose a template](#dp-choose-templates "#dp-choose-templates").

## Choose a template

The following templates are available for download from the Amazon S3
bucket: `s3://datapipeline-us-east-1/templates/`.

###### Templates

- [Getting started using
  ShellCommandActivity](dp-template-gettingstartedshell.md "dp-template-gettingstartedshell.md")
- [Run AWS CLI command](dp-template-runawscli.md "dp-template-runawscli.md")
- [Export DynamoDB table to S3](dp-template-exportddbtos3.md "dp-template-exportddbtos3.md")
- [Import DynamoDB backup data from S3](dp-template-exports3toddb.md "dp-template-exports3toddb.md")
- [Run job on an Amazon EMR cluster](dp-template-emr.md "dp-template-emr.md")
- [Full copy of Amazon RDS MySQL Table to Amazon S3](dp-template-copyrdstos3.md "dp-template-copyrdstos3.md")
- [Incremental copy of Amazon RDS MySQL table to
  Amazon S3](dp-template-incrementalcopyrdstos3.md "dp-template-incrementalcopyrdstos3.md")
- [Load S3 data into Amazon RDS MySQL table](dp-template-copys3tords.md "dp-template-copys3tords.md")
- [Full copy of Amazon RDS MySQL table to Amazon Redshift](dp-template-redshiftrdsfull.md "dp-template-redshiftrdsfull.md")
- [Incremental copy of an Amazon RDS MySQL table to
  Amazon Redshift](dp-template-redshiftrdsincremental.md "dp-template-redshiftrdsincremental.md")
- [Load data from Amazon S3 into Amazon Redshift](dp-template-s3redshift.md "dp-template-s3redshift.md")
