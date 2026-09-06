

# Use security configurations to set up Amazon EMR cluster security
<a name="emr-security-configurations"></a>

You can use Amazon EMR security configurations to configure data encryption, Kerberos authentication, and Amazon S3 authorization for EMRFS on your clusters. First, you create a security configuration. Then, the security configuration is available to use and re-use when you create clusters.

You can use the AWS Management Console, the AWS Command Line Interface (AWS CLI), or the AWS SDKs to create security configurations. You can also use an AWS CloudFormation template to create a security configuration. For more information, see [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/) and the template reference for [AWS::EMR::SecurityConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-securityconfiguration.html#cfn-emr-securityconfiguration-securityconfiguration).

**Topics**
+ [Create a security configuration with the Amazon EMR console or with the AWS CLI](emr-create-security-configuration.md)
+ [Specify a security configuration for an Amazon EMR cluster](emr-specify-security-configuration.md)