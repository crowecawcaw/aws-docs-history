# Use security configurations to set up Amazon EMR cluster security

You can use Amazon EMR security configurations to configure data encryption, Kerberos
authentication, and Amazon S3 authorization for EMRFS on your clusters. First, you create a
security configuration. Then, the security configuration is available to use and re-use when
you create clusters.

You can use the AWS Management Console, the AWS Command Line Interface (AWS CLI), or the AWS SDKs to create security
configurations. You can also use an AWS CloudFormation template to create a security configuration.
For more information, see [AWS CloudFormation User Guide](../../../AWSCloudFormation/latest/UserGuide.md "../../../AWSCloudFormation/latest/UserGuide.md") and the template reference for [AWS::EMR::SecurityConfiguration](../../../AWSCloudFormation/latest/UserGuide/aws-resource-emr-securityconfiguration.md#cfn-emr-securityconfiguration-securityconfiguration "../../../AWSCloudFormation/latest/UserGuide/aws-resource-emr-securityconfiguration.md#cfn-emr-securityconfiguration-securityconfiguration").

###### Topics

- [Create a security
  configuration with the Amazon EMR console or with the AWS CLI](emr-create-security-configuration.md "emr-create-security-configuration.md")
- [Specify a security configuration
  for an Amazon EMR cluster](emr-specify-security-configuration.md "emr-specify-security-configuration.md")
