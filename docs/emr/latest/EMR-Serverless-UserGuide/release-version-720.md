# EMR Serverless 7.2.0

The following table lists the application versions available with
EMR Serverless 7.2.0.

| Application  | Version |
| ------------ | ------- |
| Apache Spark | 3.5.1   |
| Apache Hive  | 3.1.3   |
| Apache Tez   | 0.10.2  |

###### EMR Serverless 7.2.0 release notes

- **Lake Formation with EMR Serverless** – you can now use AWS Lake Formation to apply
  fine-grained access controls on Data Catalog tables that are backed by S3. This capability lets you configure table, row, column, and
  cell level access controls for read queries within your EMR Serverless Spark jobs. For more information,
  refer to [Using EMR Serverless with AWS Lake Formation for fine-grained access control](emr-serverless-lf-enable.md "emr-serverless-lf-enable.md") and [Considerations and
  limitations](emr-serverless-lf-enable-considerations.md "emr-serverless-lf-enable-considerations.md").
