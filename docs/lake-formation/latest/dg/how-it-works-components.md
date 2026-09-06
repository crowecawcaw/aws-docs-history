

# Lake Formation components
<a name="how-it-works-components"></a>

AWS Lake Formation relies on the interaction of several components to create and manage your data lake.

## Lake Formation console
<a name="components-console"></a>

You use the Lake Formation console to define and manage your data lake and grant and revoke Lake Formation permissions. You can use blueprints on the console to discover, cleanse, transform, and ingest data. You can also enable or disable access to the console for individual Lake Formation users.

## Lake Formation API and Command Line Interface
<a name="components-cli"></a>

Lake Formation provides API operations through several language-specific SDKs and the AWS Command Line Interface (AWS CLI). The Lake Formation API works in conjunction with the AWS Glue API. The Lake Formation API focuses primarily on managing Lake Formation permissions, while the AWS Glue API provides a data catalog API and a managed infrastructure for defining, scheduling, and running ETL operations on your data. 

For information about the AWS Glue API, see the [AWS Glue Developer Guide](https://docs.aws.amazon.com/glue/latest/dg/). For information about using the AWS CLI, see the [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/).

## Other AWS services
<a name="components-other-services"></a>

Lake Formation uses the following services:
+ [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/) to orchestrate jobs and crawlers to transform data using the AWS Glue transforms.
+ [IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/) to grant permissions policies to Lake Formation principals. The Lake Formation permission model augments the IAM permission model to secure your data lake.