

# Actions, resources, and condition keys for Amazon EC2 Instance Connect
<a name="list_ec2-instance-connect"></a>

Amazon EC2 Instance Connect (service prefix: `ec2-instance-connect`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/ec2-instance-connect/latest/APIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/ec2-instance-connect/ec2-instance-connect.json) for this service.

**Topics**
+ [API operations defined by Amazon EC2 Instance Connect](#list_ec2-instance-connect-operations)
+ [Actions defined by Amazon EC2 Instance Connect](#list_ec2-instance-connect-actions-as-permissions)
+ [Resource types defined by Amazon EC2 Instance Connect](#list_ec2-instance-connect-resources-for-iam-policies)
+ [Condition keys for Amazon EC2 Instance Connect](#list_ec2-instance-connect-policy-keys)

## API operations defined by Amazon EC2 Instance Connect
<a name="list_ec2-instance-connect-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_ec2-instance-connect-actions-as-permissions).




- **   SendSSHPublicKey  **
  - **IAM action:**  [ec2-instance-connect:SendSSHPublicKey](#list_ec2-instance-connect-action-SendSSHPublicKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SendSerialConsoleSSHPublicKey  **
  - **IAM action:**  [ec2-instance-connect:SendSerialConsoleSSHPublicKey](#list_ec2-instance-connect-action-SendSerialConsoleSSHPublicKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon EC2 Instance Connect
<a name="list_ec2-instance-connect-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [OpenTunnel](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/permissions-for-ec2-instance-connect-endpoint.html#iam-OpenTunnel)  **
  - **Description:** Grants permission to establish SSH connection to an EC2 instance using EC2 Instance Connect Endpoint
  - **Resource types (\*required):** [instance-connect-endpoint\*](#list_ec2-instance-connect-resource-instance-connect-endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ec2-instance-connect-aws_ResourceTag___TagKey_)<br />[ec2:ResourceTag/${TagKey}](#list_ec2-instance-connect-ec2_ResourceTag___TagKey_)
  - **Resource types (\*required):** [instance-connect-endpoint\*](#list_ec2-instance-connect-resource-instance-connect-endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ec2-instance-connect-aws_ResourceTag___TagKey_)<br />ec2-instance-connect:MaxTunnelDuration<br />[ec2-instance-connect:privateIpAddress](#list_ec2-instance-connect-ec2-instance-connect_privateIpAddress)<br />[ec2-instance-connect:remotePort](#list_ec2-instance-connect-ec2-instance-connect_remotePort)<br />[ec2:ResourceTag/${TagKey}](#list_ec2-instance-connect-ec2_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SendSSHPublicKey](https://docs.aws.amazon.com/ec2-instance-connect/latest/APIReference/API_SendSSHPublicKey.html)  **
  - **Description:** Grants permission to push an SSH public key to the specified EC2 instance to be used for standard SSH
  - **Resource types (\*required):** [instance\*](#list_ec2-instance-connect-resource-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ec2-instance-connect-aws_ResourceTag___TagKey_)<br />[ec2:osuser](#list_ec2-instance-connect-ec2_osuser)<br />[ec2:ResourceTag/${TagKey}](#list_ec2-instance-connect-ec2_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SendSerialConsoleSSHPublicKey](https://docs.aws.amazon.com/ec2-instance-connect/latest/APIReference/API_SendSerialConsoleSSHPublicKey.html)  **
  - **Description:** Grants permission to push an SSH public key to the specified EC2 instance to be used for serial console SSH
  - **Resource types (\*required):** [instance\*](#list_ec2-instance-connect-resource-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ec2-instance-connect-aws_ResourceTag___TagKey_)<br />[ec2:ResourceTag/${TagKey}](#list_ec2-instance-connect-ec2_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon EC2 Instance Connect
<a name="list_ec2-instance-connect-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format)  | arn:${Partition}:ec2:${Region}:${Account}:instance/${InstanceId} | [aws:ResourceTag/${TagKey}](#list_ec2-instance-connect-aws_ResourceTag___TagKey_)<br />[ec2:ResourceTag/${TagKey}](#list_ec2-instance-connect-ec2_ResourceTag___TagKey_) | 
|  [instance-connect-endpoint](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/permissions-for-ec2-instance-connect-endpoint.html#iam-CreateInstanceConnectEndpoint)  | arn:${Partition}:ec2:${Region}:${Account}:instance-connect-endpoint/${InstanceConnectEndpointId} | [aws:ResourceTag/${TagKey}](#list_ec2-instance-connect-aws_ResourceTag___TagKey_)<br />[ec2:ResourceTag/${TagKey}](#list_ec2-instance-connect-ec2_ResourceTag___TagKey_) | 

## Condition keys for Amazon EC2 Instance Connect
<a name="list_ec2-instance-connect-policy-keys"></a>

Amazon EC2 Instance Connect defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tags associated with the resource | String | 
|   [ec2-instance-connect:maxTunnelDuration](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/permissions-for-ec2-instance-connect-endpoint.html#iam-OpenTunnel)  | Filters access by maximum session duration associated with the instance | Numeric | 
|   [ec2-instance-connect:privateIpAddress](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/permissions-for-ec2-instance-connect-endpoint.html#iam-OpenTunnel)  | Filters access by private IP Address associated with the instance | IPAddress | 
|   [ec2-instance-connect:remotePort](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/permissions-for-ec2-instance-connect-endpoint.html#iam-OpenTunnel)  | Filters access by port number associated with the instance | Numeric | 
|   [ec2:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tags associated with the resource | String | 
|   [ec2:osuser](https://docs.aws.amazon.com/ec2-instance-connect/latest/APIReference/API_SendSSHPublicKey.html)  | Filters access by specifying the default user name for the AMI that you used to launch your instance | String | 