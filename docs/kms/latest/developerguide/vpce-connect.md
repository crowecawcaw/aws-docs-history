

# Connect to an AWS KMS VPC endpoint
<a name="vpce-connect"></a>

You can connect to AWS KMS through the VPC endpoint by using an AWS SDK, the AWS CLI, or AWS Tools for PowerShell. To specify the VPC endpoint, use its DNS name. 

For example, this [list-keys](https://docs.aws.amazon.com/cli/latest/reference/kms/list-keys.html) command uses the `endpoint-url` parameter to specify the VPC endpoint. To use a command like this, replace the example VPC endpoint ID with one in your account.

```
$ aws kms list-keys --endpoint-url {{https://vpce-1234abcdf5678c90a-09p7654s-us-east-1a.ec2.us-east-1.vpce.amazonaws.com}}
```

**Required permissions**  
For an AWS KMS request that uses a VPC endpoint to be successful, the principal requires permissions from two sources:  
+ A [key policy](key-policies.md), [IAM policy](iam-policies.md), or [grant](grants.md) must give principal permission to call the operation on the resource (KMS key or alias).
+ A VPC endpoint policy must give the principal permission to use the endpoint to make the request.
For example, a key policy might give a principal permission to call [Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) on a particular KMS key. However, the VPC endpoint policy might not allow that principal to call `Decrypt` on that KMS key by using the endpoint.  
Or a VPC endpoint policy might allow a principal to use the endpoint to call [DisableKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_DisableKey.html) on certain KMS keys. But if the principal doesn't have those permissions from a key policy, IAM policy, or grant, the request fails.  
You can create a VPC endpoint policy when you create your endpoint, and you can change the VPC endpoint policy at any time. Use the VPC management console, or the [CreateVpcEndpoint](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVpcEndpoint.html) or [ModifyVpcEndpoint](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpcEndpoint.html) operations. You can also create and change a VPC endpoint policy by [using an AWS CloudFormation template](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.html). For help using the VPC management console, see [Create an interface endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-interface.html#create-interface-endpoint) and [Modifying an interface endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-interface.html#modify-interface-endpoint) in the *AWS PrivateLink Guide*.

**Private hostnames**  
If you enabled private hostnames when you created your VPC endpoint, you do not need to specify the VPC endpoint URL in your CLI commands or application configuration. The standard AWS KMS DNS hostname resolves to your VPC endpoint. The AWS CLI and SDKs use this hostname by default, so you can begin using the VPC endpoint to connect to an AWS KMS regional endpoint without changing anything in your scripts and applications.   
To use private hostnames, the `enableDnsHostnames` and `enableDnsSupport` attributes of your VPC must be set to `true`. To set these attributes, use the [ModifyVpcAttribute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpcAttribute.html) operation. For details, see [View and update DNS attributes for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html#vpc-dns-updating) in the *Amazon VPC User Guide*.