# Trusted Identity Propagation with AWS Glue ETL

With IAM Identity Center, you can connect to identity providers (IdPs) and centrally manage access for users and groups across AWS
analytics services. You can integrate identity providers such as Okta, Ping, and Microsoft Entra ID (formerly Azure Active Directory) with IAM
Identity Center for users in your organization to access data using a single-sign on experience. IAM Identity Center also supports connecting
additional third-party identity providers.

With AWS Glue 5.0 and higher, you can propagate user-identities from IAM Identity Center to AWS Glue interactive sessions. AWS Glue Interactive Sessions
will further propagate supplied identity to downstream services such as Amazon S3 Access Grants, AWS Lake Formation, and Amazon Redshift, enabling secure data access
via user identity in these downstream services.

## Overview

[Identity Center](../../../singlesignon/latest/userguide/what-is.md "../../../singlesignon/latest/userguide/what-is.md") is the recommended approach for
workforce authentication and authorization on AWS for organizations of any size and type.
With Identity Center, you can create and manage user identities in AWS, or connect your existing identity source, including Microsoft Active
Directory, Okta, Ping Identity, JumpCloud, Google Workspace, and Microsoft Entra ID (formerly Azure AD).

[Trusted identity propagation](../../../singlesignon/latest/userguide/trustedidentitypropagation-overview.md "../../../singlesignon/latest/userguide/trustedidentitypropagation-overview.md") is an IAM Identity Center feature that administrators of connected AWS services can use to
grant and audit access to service data. Access to this data is based on user attributes such as group associations. Setting up trusted identity
propagation requires collaboration between the administrators of connected AWS services and the IAM Identity Center administrators.

## Features and benefits

The AWS Glue interactive sessions integration with IAM Identity Center
[Trusted identity propagation](../../../singlesignon/latest/userguide/trustedidentitypropagation-overview.md "../../../singlesignon/latest/userguide/trustedidentitypropagation-overview.md")  
 provides the following benefits:

- The ability to enforce table-level authorization and fine grained access control with Identity Center identities on Lake Formation managed
  AWS Glue data catalog tables.
- The ability to enforce authorization with Identity Center identities on Amazon Redshift clusters.
- Enables end to end tracking of user actions for auditing.
- The ability to enforce Amazon S3 prefix-level authorization with Identity Center identities on Amazon S3 Access Grants-managed Amazon S3
  prefixes.

## Use cases

###### Interactive Data Exploration and Analysis

Data engineers use their corporate identities to seamlessly access and analyze data across multiple AWS accounts. Through SageMaker Studio,
they launch interactive Spark sessions via AWS Glue ETL, connecting to various data sources including Amazon S3 and the AWS Glue Data Catalog.
As engineers explore datasets, Spark enforces fine-grained access controls defined in Lake Formation based on their identities,
ensuring they can only view authorized data. All queries and data transformations are logged with the user's identity, creating a clear audit
trail. This streamlined approach enables rapid prototyping of new analytics products while maintaining strict data governance across client
environments.

###### Data Preparation and Feature Engineering

Data scientists from multiple research teams collaborate on complex projects using a unified data platform. They log into SageMaker Studio
with their corporate credentials, immediately accessing a vast, shared data lake that spans multiple AWS accounts. As they begin feature
engineering for new machine learning models, Spark sessions launched through AWS Glue ETL enforce Lake Formation's column and row-level security
policies based on their propagated identities. Scientists can efficiently prepare data and engineer features using familiar tools, while
compliance teams have assurance that every data interaction is automatically tracked and audited. This secure, collaborative environment
accelerates research pipelines while maintaining the strict data protection standards required in regulated industries.

## How it works

![Architecture diagram showing AWS Glue Interactive Sessions workflow. A user logs into client-facing applications (SageMaker Unified Studio, or custom applications) through IAM Identity Center. The user's identity is propagated to AWS Glue Interactive Sessions, which connects to access control services including IAM Identity Center, AWS Lake Formation, AWS Glue Data Catalog, and Amazon S3 Access Grant, before finally accessing S3 Storage.](images/GlueISSMAI.png)

A user logs into client-facing applications (SageMaker AI, or custom applications) using their corporate identity
through IAM Identity Center. This identity is then propagated through the entire data access pipeline.

The authenticated user launches AWS AWS Glue Interactive Sessions, which serve as the compute engine for data processing.
These sessions maintain the user's identity context throughout the workflow.

AWS Lake Formation and the AWS Glue Data Catalog work together to enforce fine-grained access controls.
Lake Formation applies security policies based on the user's propagated identity, while Amazon S3 Access Grant provides additional permission layers,
ensuring users can only access data they're authorized to view.

Finally, the system connects to Amazon S3 Storage where the actual data resides. All access is governed by the combined security policies,
maintaining data governance while enabling interactive data exploration and analysis. This architecture enables secure, identity-based data
access across multiple AWS services while maintaining a seamless user experience for data scientists and engineers working with large datasets.

## Integrations

### AWS managed development environment

The following AWS managed client-facing applications support trusted identity propagation with AWS Glue interactive sessions:

- [Sagemaker Unified Studio](https://aws.amazon.com/sagemaker/unified-studio/ "https://aws.amazon.com/sagemaker/unified-studio/")
- [Amazon SageMaker AI](https://aws.amazon.com/sagemaker-ai/ "https://aws.amazon.com/sagemaker-ai/")

###### Sagemaker Unified Studio

To use trusted identity propagation with Sagemaker Unified Studio:

1. Set up Sagemaker Unified Studio project with trusted identity propagation enabled as the client-facing development environment.
2. Set up [Lake Formation](../../../en_us/singlesignon/latest/userguide/tip-tutorial-lf.md "../../../en_us/singlesignon/latest/userguide/tip-tutorial-lf.md")
   to enable fine-grained access control for AWS Glue tables based on the user or group in IAM Identity Center.
3. [Set up Amazon S3 Access Grants](../../../en_us/singlesignon/latest/userguide/tip-tutorial-s3.md "../../../en_us/singlesignon/latest/userguide/tip-tutorial-s3.md") to enable temporary access to the underlying data locations in Amazon S3.
4. Open Sagemaker Unified Studio JupyterLab IDE space and select AWS Glue as compute for notebook execution.

### Customer managed self-hosted Notebook environment

To enable trusted identity propagation for users of custom-developed applications, see
[Access AWS services programmatically using trusted identity propagation](https://aws.amazon.com/blogs/security/access-aws-services-programmatically-using-trusted-identity-propagation/ "https://aws.amazon.com/blogs/security/access-aws-services-programmatically-using-trusted-identity-propagation/") in the AWS Security Blog.
