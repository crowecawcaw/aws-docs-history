# Ec2Config

The subnet and security groups that AWS DataSync uses to connect to one of your
Amazon EFS file system's [mount targets](../../../efs/latest/ug/accessing-fs.md "../../../efs/latest/ug/accessing-fs.md").

## Contents

**SecurityGroupArns**

Specifies the Amazon Resource Names (ARNs) of the security groups associated with an
Amazon EFS file system's mount target.

Type: Array of strings

Array Members: Minimum number of 1 item. Maximum number of 5 items.

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):ec2:[a-z\-0-9]*:[0-9]{12}:security-group/sg-[a-f0-9]+$`

Required: Yes

**SubnetArn**

Specifies the ARN of a subnet where DataSync creates the [network interfaces](datasync-network.md#required-network-interfaces "datasync-network.md#required-network-interfaces") for managing traffic during your transfer.

The subnet must be located:

- In the same virtual private cloud (VPC) as the Amazon EFS file system.
- In the same Availability Zone as at least one mount target for the Amazon EFS
  file system.

###### Note

You don't need to specify a subnet that includes a file system mount target.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):ec2:[a-z\-0-9]*:[0-9]{12}:subnet/.*$`

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/Ec2Config.md "../../../goto/SdkForCpp/datasync-2018-11-09/Ec2Config.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/Ec2Config.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/Ec2Config.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/Ec2Config.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/Ec2Config.md")
