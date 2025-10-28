# Best practice 4.2 – Build user identity solutions that uniquely identify people and systems

To control data access effectively, the analytics workload
should be able to uniquely identify the people or systems.
For example, the workload should be able to tell who
accessed to the data by looking at the user identifiers (such
as user names, tags, or IAM role names) with confidence that
the identifier represents only one person or system.

For more details, refer to the following information:

- AWS Big Data Blog:
  [Amazon Redshift identity federation with multi-factor
  authentication](https://aws.amazon.com/blogs/big-data/amazon-redshift-identity-federation-with-multi-factor-authentication/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-identity-federation-with-multi-factor-authentication/")
- AWS Big Data Blog:
  [Federating
  single sign-on access to your Amazon Redshift cluster with
  PingIdentity](https://aws.amazon.com/blogs/big-data/federating-single-sign-on-access-to-your-amazon-redshift-cluster-with-pingidentity/ "https://aws.amazon.com/blogs/big-data/federating-single-sign-on-access-to-your-amazon-redshift-cluster-with-pingidentity/")
- AWS Database Blog:
  [Get
  started with Amazon OpenSearch Service: Use Amazon Cognito for Kibana](https://aws.amazon.com/blogs/database/get-started-with-amazon-elasticsearch-service-use-amazon-cognito-for-kibana-access-control/ "https://aws.amazon.com/blogs/database/get-started-with-amazon-elasticsearch-service-use-amazon-cognito-for-kibana-access-control/")
  [access
  control](https://aws.amazon.com/blogs/database/get-started-with-amazon-elasticsearch-service-use-amazon-cognito-for-kibana-access-control/ "https://aws.amazon.com/blogs/database/get-started-with-amazon-elasticsearch-service-use-amazon-cognito-for-kibana-access-control/")
- AWS Partner Network (APN) Blog:
  [Implementing
  SAML AuthN for Amazon EMR Using Okta and](https://aws.amazon.com/blogs/apn/implementing-saml-authn-for-amazon-emr-using-okta-and-column-level-authz-with-aws-lake-formation/ "https://aws.amazon.com/blogs/apn/implementing-saml-authn-for-amazon-emr-using-okta-and-column-level-authz-with-aws-lake-formation/")
  [Column-Level
  AuthZ with AWS Lake Formation](https://aws.amazon.com/blogs/apn/implementing-saml-authn-for-amazon-emr-using-okta-and-column-level-authz-with-aws-lake-formation/ "https://aws.amazon.com/blogs/apn/implementing-saml-authn-for-amazon-emr-using-okta-and-column-level-authz-with-aws-lake-formation/")
- AWS CloudTrail User Guide:
  [How
  AWS CloudTrail works with IAM](../../../awscloudtrail/latest/userguide/security_iam_service-with-iam.md "../../../awscloudtrail/latest/userguide/security_iam_service-with-iam.md")

## Suggestion 4.2.1 – Centralize workforce identities

It’s a best practice to centralize your workforce
identities, which allows you to federate with AWS Identity and Access Management (IAM) using AWS IAM Identity Center
or another federation
provider. In Amazon Redshift, IAM roles can be mapped to
Amazon Redshift database groups. In Amazon EMR, IAM roles
can be mapped to an Amazon EMR security configuration or an
Apache Ranger Microsoft Active Directory group-based
policy. In AWS Glue, IAM roles can be mapped to AWS AWS Glue Data Catalog resource policies.

AWS analytics services – such as Amazon OpenSearch Service
and Amazon DynamoDB – allow integration with Amazon Cognito for authentication. Amazon Cognito lets you add
user sign-up, sign- in, and access control to your web and
mobile apps. Amazon Cognito scales to millions of users
and supports sign-in with social identity providers, such
as Apple, Facebook, Google, and Amazon, and enterprise
identity providers via SAML 2.0 and OpenID Connect.

For more details, refer to the following information:

- AWS Big Data Blog:
  [Federate
  Database User Authentication Easily with IAM and Amazon Redshift](https://aws.amazon.com/blogs/big-data/federate-database-user-authentication-easily-with-iam-and-amazon-redshift/ "https://aws.amazon.com/blogs/big-data/federate-database-user-authentication-easily-with-iam-and-amazon-redshift/")
- WS Big Data Blog:
  [Federating
  single sign-on access to your Amazon Redshift cluster
  with PingIdentity](https://aws.amazon.com/blogs/big-data/federating-single-sign-on-access-to-your-amazon-redshift-cluster-with-pingidentity/ "https://aws.amazon.com/blogs/big-data/federating-single-sign-on-access-to-your-amazon-redshift-cluster-with-pingidentity/")
- Amazon EMR Management Guide:
  [Allow
  AWS IAM Identity Center for Amazon EMR Studio](../../../emr/latest/ManagementGuide/emr-studio-enable-sso.md "../../../emr/latest/ManagementGuide/emr-studio-enable-sso.md")
