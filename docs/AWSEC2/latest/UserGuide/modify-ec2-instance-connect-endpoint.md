

# Modify an EC2 Instance Connect Endpoint
<a name="modify-ec2-instance-connect-endpoint"></a>

You can modify existing EC2 Instance Connect Endpoints using the console, AWS CLI, or an SDK.

Before you begin, you must have the required IAM permissions. For more information, see [Permissions to create, describe, modify, and delete EC2 Instance Connect Endpoints](permissions-for-ec2-instance-connect-endpoint.md#iam-CreateInstanceConnectEndpoint).

## Parameters you can modify
<a name="eice-modify-parameters"></a>

You can modify the following EC2 Instance Connect Endpoint parameters:

**Security groups**  
You can specify new security groups for the EC2 Instance Connect Endpoint. The new security groups replace the current security groups.  
When modifying the security groups, you must specify:  
+ At least one security group, even if it's just the default security group in the VPC.
+ The IDs of the security groups, not the names.

**IP address type**  
You can specify a new IP address type for the EC2 Instance Connect Endpoint.  
Valid values: `ipv4` \| `dualstack` \| `ipv6`

**Preserve client IP setting**  
You can specify whether to preserve the client IP address as the source.  
Preserving the client IP is only supported on IPv4 EC2 Instance Connect Endpoints. When enabling `PreserveClientIp`, either the endpoint's existing IP address type must be `ipv4`, or if modifying the IP address type in the same request, the new value must be `ipv4`.

------
#### [ Console ]

**To modify an EC2 Instance Connect Endpoint**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the left navigation pane, choose **Endpoints**.

1. Select the endpoint.

1. Choose **Actions**, **Modify endpoint settings**.

1. Change the endpoint settings.

1. Choose **Save changes**.

   The endpoint enters the **Pending** state. When modification completes, the endpoint returns to the **Available** state.

------
#### [ AWS CLI ]

**To modify an EC2 Instance Connect Endpoint**  
Use the [modify-instance-connect-endpoint](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-instance-connect-endpoint.html) command and specify the EC2 Instance Connect Endpoint and the parameters to modify. The following example modifies all the parameters in a single request.

```
aws ec2 modify-instance-connect-endpoint \
    --instance-connect-endpoint-id {{eice-0123456789example}} \
    --security-group-ids {{sg-0123456789example}} \
    --ip-address-type {{dualstack}} \
    --no-preserve-client-ip
```

The following is example output.

```
{
    "Return": true
}
```

**To monitor the update status**  
During modification, the EC2 Instance Connect Endpoint status changes to `update-in-progress`. The update process runs asynchronously and completes with either an `update-complete` or `update-failed` status. The endpoint uses its old configuration until the status changes to `update-complete`.

Use the [describe-instance-connect-endpoints](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instance-connect-endpoints.html) command to monitor the update status. The `--query` parameter filters the results to the `State` field.

```
aws ec2 describe-instance-connect-endpoints \
    --instance-connect-endpoint-ids {{eice-0123456789example}} \
    --query InstanceConnectEndpoints[*].State --output text
```

The following is example output.

```
update-complete
```

------
#### [ PowerShell ]

**To modify an EC2 Instance Connect Endpoint**  
Use the [Edit-EC2InstanceConnectEndpoint](https://docs.aws.amazon.com/powershell/latest/reference/items/Edit-EC2InstanceConnectEndpoint.html) cmdlet and specify the EC2 Instance Connect Endpoint and the parameters to modify. The following example modifies all the parameters in a single request.

```
Edit-EC2InstanceConnectEndpoint `
    -InstanceConnectEndpointId {{eice-0123456789example}} `
    -SecurityGroupIds {{sg-0123456789example}} `
    -IpAddressType {{dualstack}} `
    -PreserveClientIp {{$false}}
```

The following is example output.

```
True
```

**To monitor the update status**  
During modification, the EC2 Instance Connect Endpoint status changes to `update-in-progress`. The update process runs asynchronously and completes with either an `update-complete` or `update-failed` status. The endpoint uses its old configuration until the status changes to `update-complete`.

Use the [Get-EC2InstanceConnectEndpoint](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2InstanceConnectEndpoint.html) command to monitor the update status. `.State.Value` filters the results to the `State` field.

```
(Get-EC2InstanceConnectEndpoint -InstanceConnectEndpointId "{{eice-0123456789example}}").State.Value
```

The following is example output.

```
update-complete
```

------