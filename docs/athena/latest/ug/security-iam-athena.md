# Identity and access management in Athena

Amazon Athena uses [AWS Identity and Access Management (IAM)](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md") policies to restrict access to Athena operations. For a full
list of permissions for Athena, see [Actions, resources,
and condition keys for Amazon Athena](../../../service-authorization/latest/reference/list_amazonathena.md "../../../service-authorization/latest/reference/list_amazonathena.md") in the _Service Authorization Reference_.

Whenever you use IAM policies, make sure that you follow IAM best practices. For more information, see [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User Guide_.

The permissions required to run Athena queries include the following:

- Amazon S3 locations where the underlying data to query is stored. For more information,
  see [Identity and access management in Amazon S3](../../../AmazonS3/latest/dev/s3-access-control.md "../../../AmazonS3/latest/dev/s3-access-control.md") in the
  _Amazon Simple Storage Service User Guide_.
- Metadata and resources that you store in the AWS Glue Data Catalog, such as databases and
  tables, including additional actions for encrypted metadata. For more information,
  see [Setting up IAM permissions for AWS Glue](../../../glue/latest/dg/getting-started-access.md "../../../glue/latest/dg/getting-started-access.md") and [Setting up encryption in
  AWS Glue](../../../glue/latest/dg/set-up-encryption.md "../../../glue/latest/dg/set-up-encryption.md") in the _AWS Glue Developer Guide_.
- Athena API actions. For a list of API actions in Athena, see [Actions](../APIReference/API_Operations.md "../APIReference/API_Operations.md") in the _Amazon Athena API Reference_.
  The following topics provide more information about permissions for specific areas of
  Athena.

###### Topics

- [AWS managed policies](managed-policies.md "managed-policies.md")
- [Data perimeters](data-perimeters.md "data-perimeters.md")
- [Access through JDBC and ODBC connections](policy-actions.md "policy-actions.md")
- [Control access to Amazon S3 from Athena](s3-permissions.md "s3-permissions.md")
- [Cross-account access to S3 buckets](cross-account-permissions.md "cross-account-permissions.md")
- [Access to databases and tables in AWS Glue](fine-grained-access-to-glue-resources.md "fine-grained-access-to-glue-resources.md")
- [Cross-account access to AWS Glue data catalogs](security-iam-cross-account-glue-catalog-access.md "security-iam-cross-account-glue-catalog-access.md")
- [Access to encrypted metadata in the Data Catalog](access-encrypted-data-glue-data-catalog.md "access-encrypted-data-glue-data-catalog.md")
- [Access to workgroups and tags](workgroups-access.md "workgroups-access.md")
- [Use IAM policies to control workgroup access](workgroups-iam-policy.md "workgroups-iam-policy.md")
- [IAM Identity Center enabled workgroups](workgroups-identity-center.md "workgroups-identity-center.md")
- [Configure minimum encryption](workgroups-minimum-encryption.md "workgroups-minimum-encryption.md")
- [Configure access to prepared statements](security-iam-athena-prepared-statements.md "security-iam-athena-prepared-statements.md")
- [Use CalledVia context keys](security-iam-athena-calledvia.md "security-iam-athena-calledvia.md")
- [Allow access to the Athena Data Connector for External Hive Metastore](hive-metastore-iam-access.md "hive-metastore-iam-access.md")
- [Allow Lambda function access to external Hive metastores](hive-metastore-iam-access-lambda.md "hive-metastore-iam-access-lambda.md")
- [Permissions required to create connector and Athena catalog](athena-catalog-access.md "athena-catalog-access.md")
- [Allow access to Athena Federated Query](federated-query-iam-access.md "federated-query-iam-access.md")
- [Allow access to UDFs](udf-iam-access.md "udf-iam-access.md")
- [Allow access for ML with Athena](machine-learning-iam-access.md "machine-learning-iam-access.md")
- [Enable federated access to the Athena API](access-federation-saml.md "access-federation-saml.md")
