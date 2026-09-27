

# Access control
<a name="iot-create-role"></a>

## Granting an AWS IoT rule the access it requires
<a name="iot-create-role-iam"></a>

Use IAM roles to control the AWS resources to which each rule has access. Before you create a rule, you must create an IAM role with a policy that allows access to the required AWS resources. AWS IoT assumes this role when implementing a rule.

**Complete the following steps to create the IAM role and AWS IoT policy that grant an AWS IoT rule the access it requires (AWS CLI).**

1. Save the following trust policy document, which grants AWS IoT permission to assume the role, to a file named `iot-role-trust.json`.  
****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Principal": {
                   "Service": "iot.amazonaws.com"
           },
               "Action": "sts:AssumeRole",
               "Condition": {
                   "StringEquals": {
                       "aws:SourceAccount": "{{123456789012}}"
               },
                   "ArnLike": {
                       "aws:SourceArn": "arn:aws:iot:{{us-east-1:123456789012}}:{{rule/rulename}}"
               }
           }
           }
       ]
   }
   ```

   Use the [create-role](https://docs.aws.amazon.com/cli/latest/reference/iam/create-role.html) command to create an IAM role specifying the `iot-role-trust.json` file:

   ```
   aws iam create-role --role-name {{my-iot-role}} --assume-role-policy-document file://{{iot-role-trust.json}}
   ```

   The output of this command looks like the following:

   ```
   {
   	"Role": {
   		"AssumeRolePolicyDocument": "url-encoded-json",
   		"RoleId": "AKIAIOSFODNN7EXAMPLE",
   		"CreateDate": "2015-09-30T18:43:32.821Z",
   		"RoleName": "my-iot-role",
   		"Path": "/",
   		"Arn": "{{arn:aws:iam::123456789012:role/my-iot-role}}"
   	}
   }
   ```

1. Save the following JSON into a file named `my-iot-policy.json`.  
****  

   ```
   {
   	"Version":"2012-10-17",		 	 	 
   	"Statement": [
   		{
   			"Effect": "Allow",
   			"Action": "dynamodb:*",
   			"Resource": "*"
   		}
   	]
   }
   ```

   This JSON is an example policy document that grants AWS IoT administrator access to DynamoDB.

   Use the [create-policy](https://docs.aws.amazon.com/cli/latest/reference/iam/create-policy.html) command to grant AWS IoT access to your AWS resources upon assuming the role, passing in the `my-iot-policy.json` file:

   ```
   aws iam create-policy --policy-name {{my-iot-policy}} --policy-document file://{{my-iot-policy.json}}
   ```

   For more information about how to grant access to AWS services in policies for AWS IoT, see [Creating an AWS IoT rule](iot-create-rule.md).

   The output of the [create-policy](https://docs.aws.amazon.com/cli/latest/reference/iam/create-policy.html) command contains the ARN of the policy. Attach the policy to a role.

   ```
   {
   	"Policy": {
   		"PolicyName": "my-iot-policy",
   		"CreateDate": "2015-09-30T19:31:18.620Z",
   		"AttachmentCount": 0,
   		"IsAttachable": true,
   		"PolicyId": "ZXR6A36LTYANPAI7NJ5UV",
   		"DefaultVersionId": "v1",
   		"Path": "/",
   		"Arn": "{{arn:aws:iam::123456789012:policy/my-iot-policy}}",
   		"UpdateDate": "2015-09-30T19:31:18.620Z"
   	}
   }
   ```

1. Use the [attach-role-policy](https://docs.aws.amazon.com/cli/latest/reference/iam/attach-role-policy.html) command to attach your policy to your role:

   ```
   aws iam attach-role-policy --role-name {{my-iot-role}} --policy-arn "{{arn:aws:iam::123456789012:policy/my-iot-policy}}"
   ```

## Revoking rule engine access
<a name="iot-revoke-rule-engine-access"></a>

To immediately revoke rule engine access, do the following:

1. Remove iot.amazonaws.com from the [trust policy](https://docs.aws.amazon.com/iot/latest/developerguide/iot-create-role.html#iot-create-role-iam)

1. Follow the steps to [revoke IAM role sessions](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_revoke-sessions.html)

## Restricting HTTP action traffic to the rules engine IPv6 ranges
<a name="rules-engine-ip-ranges"></a>

Endpoints that restrict inbound traffic by source address must allow the range for your Region from the following table. This applies to HTTP action endpoints, which are the only destinations you can configure to be reachable over IPv6 only. For other actions, the rules engine connects to dual-stack destinations over IPv4, so there is no range to allow.

These ranges apply only when the rules engine connects to your endpoint over IPv6, which happens when your endpoint publishes AAAA records and no A records. There is no equivalent IPv4 range, so restricting rules engine traffic by source address requires an endpoint that's reachable only over IPv6.

Each range is used only for rules engine actions and doesn't change. Ranges for additional Regions are added to this table as they become available. For the steps to receive data over IPv6, see [Network access](http-action-destination.md#http-action-destination-network-access).

**Note**  
Regions not listed in this table don't have a rules engine IPv6 range.


| Region | IPv6 address range | 
| --- | --- | 
| us-east-1 | 2600:1f33:8000::/48 | 
| us-east-2 | 2600:1f33:6000::/48 | 
| us-west-1 | 2600:1f33:c000::/48 | 
| us-west-2 | 2600:1f33:4000::/48 | 
| ap-east-1 | 2406:da33:e000::/48 | 
| ap-northeast-1 | 2406:da33:4000::/48 | 
| ap-northeast-2 | 2406:da33:2000::/48 | 
| ap-south-1 | 2406:da33:a000::/48 | 
| ap-southeast-1 | 2406:da33:8000::/48 | 
| ap-southeast-2 | 2406:da33:c000::/48 | 
| ap-southeast-5 | 2406:da33:800::/48 | 
| ca-central-1 | 2600:1f33:1000::/48 | 
| eu-central-1 | 2a05:d033:4000::/48 | 
| eu-north-1 | 2a05:d033:6000::/48 | 
| eu-south-1 | 2a05:d033:a000::/48 | 
| eu-south-2 | 2a05:d033:1000::/48 | 
| eu-west-1 | 2a05:d033:8000::/48 | 
| eu-west-2 | 2a05:d033:c000::/48 | 
| eu-west-3 | 2a05:d033:2000::/48 | 
| il-central-1 | 2a05:d033:5000::/48 | 
| sa-east-1 | 2600:1f33:e000::/48 | 
| us-gov-east-1 | 2600:1f33:5000::/48 | 
| us-gov-west-1 | 2600:1f33:2000::/48 | 

The following examples restrict inbound traffic to the `us-east-1` range. Replace it with the range for your Region.

An API Gateway resource policy that allows the rules engine and denies everything else:

```
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Effect": "Allow",
			"Principal": "*",
			"Action": "execute-api:Invoke",
			"Resource": "execute-api:/*"
		},
		{
			"Effect": "Deny",
			"Principal": "*",
			"Action": "execute-api:Invoke",
			"Resource": "execute-api:/*",
			"Condition": {
				"NotIpAddress": {
					"aws:SourceIp": ["2600:1f33:8000::/48"]
				}
			}
		}
	]
}
```

For an endpoint behind a load balancer or on Amazon EC2, add an inbound rule to the security group that allows TCP traffic on port 443 from the range for your Region.