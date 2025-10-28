# Considerations and limitations for Amazon EMR with

the Identity Center integration

Consider the following points when you use IAM Identity Center with Amazon EMR:

- Trusted Identity Propagation through Identity Center is supported on Amazon EMR 6.15.0 and higher, and only with Apache Spark. Also, Trusted Identity Propagation through Identity Center using EMR Runtime Roles feature
  is supported on Amazon EMR 7.8.0 and higher, and only with Apache Spark.
- To enable EMR clusters with trusted identity propagation, you must use the AWS CLI to create a
  security configuration that has trusted identity propagation enabled, and use that security
  configuration when you launch your cluster. For more information, see [Create an Identity Center enabled security
  configuration](emr-idc-start.md#emr-idc-start-securityconfig "emr-idc-start.md#emr-idc-start-securityconfig").
- Fine-grained access controls using AWS Lake Formation that use Trusted Identity Propagation are available for
  Amazon EMR clusters on EMR version 7.2.0 and higher. Between EMR versions 6.15.0 and 7.1.0, only table-level access control, based on AWS Lake Formation, is available.
- With Amazon EMR clusters that use Trusted Identity Propagation, operations that support access control based on Lake Formation with Apache Spark
  include SELECT, ALTER TABLE, INSERT INTO, and DROP TABLE.
- Fine-grained access controls using AWS Lake Formation that use Trusted Identity Propagation will need to update Lake Formation Identity Center configuration
  by adding EMR managed IAM Identity application arn as authorized target. You can find Amazon EMR managed IAM Identity application ARN
  by calling EMR `describe-security-configure` API and look for
  field `IdCApplicationARN`. More details: [Updating IAM Identity Center integration](../../../lake-formation/latest/dg/update-lf-identity-center-connection.md "../../../lake-formation/latest/dg/update-lf-identity-center-connection.md") on how
  to setup Lake Formation with IAM Identity Center configuration.
- To use Fine-grained access controls using AWS Lake Formation that use Trusted Identity Propagation, IAM Identity users should be
  granted Lake Formation permissions on default database. More
  details: [Configure Lake Formation for an IAM Identity Center enabled EMR cluster](emr-idc-lf.md "emr-idc-lf.md").
- Trusted Identity Propagation with Amazon EMR is supported in the following AWS Regions:
  - `af-south-1` – Africa (Cape Town)
  - `ap-east-1` – Asia Pacific (Hong Kong)
  - `ap-northeast-1` – Asia Pacific (Tokyo)
  - `ap-northeast-2` – Asia Pacific (Seoul)
  - `ap-northeast-3` – Asia Pacific (Osaka)
  - `ap-south-1` – Asia Pacific (Mumbai)
  - `ap-south-2` – Asia Pacific (Hyderabad)
  - `ap-southeast-1` – Asia Pacific (Singapore)
  - `ap-southeast-2` – Asia Pacific (Sydney)
  - `ap-southeast-3` – Asia Pacific (Jakarta)
  - `ap-southeast-4` – Asia Pacific (Melbourne)
  - `ca-central-1` – Canada (Central)
  - `eu-central-1` – Europe (Frankfurt)
  - `eu-central-2` – Europe (Zurich)
  - `eu-north-1` – Europe (Stockholm)
  - `eu-south-1` – Europe (Milan)
  - `eu-south-2` – Europe (Spain)
  - `eu-west-1` – Europe (Ireland)
  - `eu-west-2` – Europe (London)
  - `eu-west-3` – Europe (Paris)
  - `il-central-1` – Israel (Tel Aviv)
  - `me-central-1` – Middle East (UAE)
  - `me-south-1` – Middle East (Bahrain)
  - `sa-east-1` – South America (São Paulo)
  - `us-east-1` – US East (N. Virginia)
  - `us-east-2` – US East (Ohio)
  - `us-west-1` – US West (N. California)
  - `us-west-2` – US West (Oregon)
