# Lake Formation components

AWS Lake Formation relies on the interaction of several components to create and manage your
data lake.

## Lake Formation console

You use the Lake Formation console to define and manage your data lake and grant and revoke Lake Formation
permissions. You can use blueprints on the console to discover, cleanse, transform,
and ingest data. You can also enable or disable access to the console for individual
Lake Formation users.

## Lake Formation API and Command Line Interface

Lake Formation provides API operations through several language-specific SDKs and the
AWS Command Line Interface (AWS CLI). The Lake Formation API works in conjunction with the AWS Glue API. The Lake Formation
API focuses primarily on managing Lake Formation permissions, while the AWS Glue API provides a
data catalog API and a managed infrastructure for defining, scheduling, and running
ETL operations on your data.

For information about the AWS Glue API, see the [AWS Glue Developer Guide](../../../glue/latest/dg.md "../../../glue/latest/dg.md"). For information about using the AWS CLI, see the [AWS CLI Command Reference](../../../cli/latest/reference.md "../../../cli/latest/reference.md").

## Other AWS services

Lake Formation uses the following services:

- [AWS Glue](../../../glue/latest/dg.md "../../../glue/latest/dg.md") to orchestrate jobs and crawlers
  to transform data using the AWS Glue transforms.
- [IAM](../../../IAM/latest/UserGuide.md "../../../IAM/latest/UserGuide.md") to grant permissions policies to
  Lake Formation principals. The Lake Formation permission model augments the IAM permission
  model to secure your data lake.
