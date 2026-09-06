

# Trusted Identity Propagation
<a name="security-iam-service-trusted-prop"></a>

With Amazon EMR releases 7.8.0 and higher, you can propagate user-identities from AWS IAM Identity Center to interactive workloads with EMR Serverless through Apache Livy Endpoint. Apache Livy interactive workloads will further propagate supplied identity to downstream services like Amazon S3, Lake Formation and Amazon Redshift, enabling secure data access via user identity in these downstream. The following sections provide a conceptual overview, prerequisites, and steps required to launch and propagate identity to interactive workloads with EMR Serverless through Apache Livy Endpoint.

## Overview
<a name="security-iam-service-trusted-prop-overview"></a>

[IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) is the recommended approach for workforce authentication and authorization on AWS for organizations of any size and type. With Identity Center, create and manage user identities in AWS, or connect your existing identity source, including Microsoft Active Directory, Okta, Ping Identity, JumpCloud, Google Workspace, and Microsoft Entra ID (formerly Azure AD).

[Trusted identity propagation](https://docs.aws.amazon.com/singlesignon/latest/userguide/trustedidentitypropagation-overview.html) is an AWS IAM Identity Center feature that administrators of connected AWS services can use to grant and audit access to service data. Access to this data is based on user attributes such as group associations. Setting up trusted identity propagation requires collaboration between the administrators of connected AWS services and the IAM Identity Center administrators. For more information, refer to [Prerequisites and considerations](https://docs.aws.amazon.com/singlesignon/latest/userguide/trustedidentitypropagation-overall-prerequisites.html) in the *IAM Identity Center User Guide*.

## Features and benefits
<a name="security-iam-service-trusted-prop-features"></a>

The EMR Serverless Apache Livy Endpoint integration with IAM Identity Center [Trusted identity propagation](https://docs.aws.amazon.com/singlesignon/latest/userguide/trustedidentitypropagation-overview.html) provides the following benefits:
+ The ability to enforce table-level authorization with Identity Center identities on AWS Lake Formation managed AWS Glue data catalog tables.
+ The ability to enforce authorization with Identity Center identities on Amazon Redshift clusters.
+ Enables end to end tracking of user actions for auditing.
+ The ability to enforce Amazon S3 prefix-level authorization with Identity Center identities on S3 Access Grants-managed S3 prefixes.

## How it works
<a name="security-iam-service-trusted-prop-features-works"></a>

![EMR Serverless flowchart.](http://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/images/PEZ-SMAI.png)


### Use case example
<a name="security-iam-service-trusted-prop-use-cases"></a>

#### Data Preparation and Feature Engineering
<a name="security-iam-service-trusted-prop-feature-eng"></a>

Data scientists from multiple research teams collaborate on complex projects using a unified data platform. They log into SageMaker AI using their corporate credentials, immediately gaining access to a vast, shared data lake spanning several AWS accounts. As they begin feature engineering for new machine learning models, the Spark sessions launched through EMR Serverless enforce Lake Formation's column and row-level security policies based on their propagated identities. Scientists can efficiently prepare data and engineer features using familiar tools, while compliance teams are assured that every data interaction is automatically tracked and audited. This secure, collaborative environment accelerates research pipelines while maintaining strict data protection standards required in regulated industries.