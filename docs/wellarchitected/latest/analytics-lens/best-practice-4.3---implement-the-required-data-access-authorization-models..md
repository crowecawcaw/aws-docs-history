# Best practice 4.3 – Implement the required data access authorization models

User authorization determines what actions that a user is
permitted to take on the data or resource. The data owners
should be able to use the authorization methods to protect
their data as needed. For example, if the data owners must
control which users are allowed to view certain columns of
data, the analytics workload should provide column-wise data
access authorization along with user group management for an
effective control.

## Suggestion 4.3.1 – Implement IAM policy-based data access controls

Limit access to sensitive data stores with IAM policies
where possible. Provide systems and people with rotating
short-term credentials via role-based access control
(RBAC).

For more details, see AWS Big Data Blog: [Restrict access to your AWS Glue Data Catalog with resource-level IAM permissions and resource-based policies](https://aws.amazon.com/blogs/big-data/restrict-access-to-your-aws-glue-data-catalog-with-resource-level-iam-permissions-and-resource-based-policies/ "https://aws.amazon.com/blogs/big-data/restrict-access-to-your-aws-glue-data-catalog-with-resource-level-iam-permissions-and-resource-based-policies/")

## Suggestion 4.3.2 – Implement dataset-level data access controls

As dataset owners require independent rules of granting
data access, you should build the analytics workloads to
have the dataset owners control the data access per each
dataset level. For example, if the analytics workload
hosts a shared Amazon Redshift cluster, the owners of the
individual table should be able to authorize the table
read and write independently.

For more details, refer to the following information:

- AWS Big Data Blog:
  [Validate,
  evolve, and control schemas in Amazon MSK and Amazon Kinesis Data](https://aws.amazon.com/blogs/big-data/validate-evolve-and-control-schemas-in-amazon-msk-and-amazon-kinesis-data-streams-with-aws-glue-schema-registry/ "https://aws.amazon.com/blogs/big-data/validate-evolve-and-control-schemas-in-amazon-msk-and-amazon-kinesis-data-streams-with-aws-glue-schema-registry/")
  [Streams
  with AWS Glue Schema Registry](https://aws.amazon.com/blogs/big-data/validate-evolve-and-control-schemas-in-amazon-msk-and-amazon-kinesis-data-streams-with-aws-glue-schema-registry/ "https://aws.amazon.com/blogs/big-data/validate-evolve-and-control-schemas-in-amazon-msk-and-amazon-kinesis-data-streams-with-aws-glue-schema-registry/").
- Amazon Redshift:
  [Amazon Redshift announces support for Row-Level Security
  (RLS)](https://aws.amazon.com/about-aws/whats-new/2022/07/amazon-redshift-row-level-security/ "https://aws.amazon.com/about-aws/whats-new/2022/07/amazon-redshift-row-level-security/")
  [Streams
  with AWS Glue Schema Registry](https://aws.amazon.com/blogs/big-data/validate-evolve-and-control-schemas-in-amazon-msk-and-amazon-kinesis-data-streams-with-aws-glue-schema-registry/ "https://aws.amazon.com/blogs/big-data/validate-evolve-and-control-schemas-in-amazon-msk-and-amazon-kinesis-data-streams-with-aws-glue-schema-registry/").

## Suggestion 4.3.3 – Implement column-level data access controls

Care should be taken that end users of analytics
applications are not exposed to sensitive data. Downstream
consumers of data should only access the limited view of
data necessary for that analytics purpose. Enforce that
sensitive data is not exposed using column-level
restrictions, for example, mask the sensitive columns to
downstream systems so an accidental exposure is avoided.

For more details, refer to the following information:

- AWS Big Data Blog:
  [Allow
  fine-grained permissions for Quick Suite authors in
  AWS Lake](https://aws.amazon.com/blogs/big-data/enable-fine-grained-permissions-for-amazon-quicksight-authors-in-aws-lake-formation/ "https://aws.amazon.com/blogs/big-data/enable-fine-grained-permissions-for-amazon-quicksight-authors-in-aws-lake-formation/")
  [Formation](https://aws.amazon.com/blogs/big-data/enable-fine-grained-permissions-for-amazon-quicksight-authors-in-aws-lake-formation/ "https://aws.amazon.com/blogs/big-data/enable-fine-grained-permissions-for-amazon-quicksight-authors-in-aws-lake-formation/")
- Amazon Redshift: [Role-based access controls](../../../redshift/latest/dg/t_Roles.md "../../../redshift/latest/dg/t_Roles.md")
- AWS Partner Network (APN) Blog:
  [Implementing
  SAML AuthN for Amazon EMR Using Okta and](https://aws.amazon.com/blogs/apn/implementing-saml-authn-for-amazon-emr-using-okta-and-column-level-authz-with-aws-lake-formation/ "https://aws.amazon.com/blogs/apn/implementing-saml-authn-for-amazon-emr-using-okta-and-column-level-authz-with-aws-lake-formation/")
  [Column-Level
  AuthZ with AWS Lake Formation](https://aws.amazon.com/blogs/apn/implementing-saml-authn-for-amazon-emr-using-okta-and-column-level-authz-with-aws-lake-formation/ "https://aws.amazon.com/blogs/apn/implementing-saml-authn-for-amazon-emr-using-okta-and-column-level-authz-with-aws-lake-formation/")
- AWS Big Data Blog:
  [Implementing
  Authorization and Auditing using Apache Ranger on Amazon EMR](https://aws.amazon.com/blogs/big-data/implementing-authorization-and-auditing-using-apache-ranger-on-amazon-emr/ "https://aws.amazon.com/blogs/big-data/implementing-authorization-and-auditing-using-apache-ranger-on-amazon-emr/")
