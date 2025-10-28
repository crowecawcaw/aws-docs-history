# How to connect with other AWS

services with trusted identity propagation enabled

When trusted identity propagation is enabled for your Amazon SageMaker AI domain, the domain users
can connect to other trusted identity propagation enabled AWS services. When trusted
identity propagation is enabled, your identity context is automatically propagated to
compatible services, allowing for fine-grained access control and improved auditing across
your machine learning workflows. This integration eliminates the need for complex IAM role
switching and provides a unified identity experience across AWS services. The following
pages provide information on how to connect Amazon SageMaker Studio to other AWS services when
trusted identity propagation is enabled.

###### Topics

- [Connect Studio
  JupyterLab notebooks to Amazon S3 Access Grants with trusted identity propagation
  enabled](trustedidentitypropagation-s3-access-grants.md "trustedidentitypropagation-s3-access-grants.md")
- [Connect Studio JupyterLab
  notebooks to Amazon EMR with trusted identity propagation enabled](trustedidentitypropagation-emr-ec2.md "trustedidentitypropagation-emr-ec2.md")
- [Connect your Studio
  JupyterLab notebooks to EMR Serverless with trusted identity propagation
  enabled](trustedidentitypropagation-emr-serverless.md "trustedidentitypropagation-emr-serverless.md")
- [Connect Studio
  JupyterLab notebooks to Redshift Data API with trusted identity propagation enabled](trustedidentitypropagation-redshift-data-apis.md "trustedidentitypropagation-redshift-data-apis.md")
- [Connect Studio
  JupyterLab notebooks to Lake Formation and Athena with trusted identity propagation
  enabled](trustedidentitypropagation-lake-formation-athena.md "trustedidentitypropagation-lake-formation-athena.md")
