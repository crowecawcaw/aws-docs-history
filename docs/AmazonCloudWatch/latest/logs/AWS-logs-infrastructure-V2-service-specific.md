

# Service-specific permissions
<a name="AWS-logs-infrastructure-V2-service-specific"></a>

In addition to the destination-specific permissions listed in the previous sections, some services require explicit authorization that customers are allowed to send logs from their resources, as an additional layer of security. This policy authorizes the `AllowVendedLogDeliveryForResource` action for resources that vend logs within that service. For these services, use the following policy and replace the service namespace ({{service}}), the Region ({{region}}), the AWS account ID ({{account-id}}), and the resource type ({{resource-type}}) with the appropriate values for your resource. Not every service that vends logs uses this action. Confirm the required permissions and values, including whether the `AllowVendedLogDeliveryForResource` action applies, in the vended logs documentation for the service that you are granting access to. The following example shows the policy for vending logs from Amazon SES.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "ServiceLevelAccessForLogDelivery",
            "Effect": "Allow",
            "Action": [
                "{{ses}}:AllowVendedLogDeliveryForResource"
            ],
            "Resource": "arn:aws:{{ses}}:{{us-east-1}}:{{123456789012}}:{{resource-type}}/*"
        }
    ]
}
```

------