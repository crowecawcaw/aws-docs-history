# Trusted Identity Propagation for interactive workloads

The steps to propagate identity to interactive workloads through an Apache Livy endpoint depend on whether your users interact with AWS
managed development environment like Amazon SageMaker AI or your own self-hosted Notebook environment as client-facing application.

![EMR Serverless flowchart.](/images/emr/latest/EMR-Serverless-UserGuide/images/PEZ-SMAI.png)

## AWS managed development environment

The following AWS managed client-facing application supports trusted identity propagation
with EMR-Serverless Apache Livy endpoint:

- [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/ai/ "https://aws.amazon.com/sagemaker/ai/")

## Customer managed self-hosted Notebook environment

To enable trusted identity propagation for users of custom-developed applications, see to [Access AWS services programmatically using
trusted identity propagation](https://aws.amazon.com/blogs/security/access-aws-services-programmatically-using-trusted-identity-propagation/ "https://aws.amazon.com/blogs/security/access-aws-services-programmatically-using-trusted-identity-propagation/") in the _AWS Security Blog_.
