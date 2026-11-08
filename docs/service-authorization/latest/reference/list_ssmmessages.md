

# Actions, resources, and condition keys for Amazon Message Gateway Service
<a name="list_ssmmessages"></a>

Amazon Message Gateway Service (service prefix: `ssmmessages`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-setting-up-messageAPIs.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/systems-manager/latest/userguide/setup-instance-permissions.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/ssmmessages/ssmmessages.json) for this service.

**Topics**
+ [Actions defined by Amazon Message Gateway Service](#list_ssmmessages-actions-as-permissions)
+ [Resource types defined by Amazon Message Gateway Service](#list_ssmmessages-resources-for-iam-policies)
+ [Condition keys for Amazon Message Gateway Service](#list_ssmmessages-policy-keys)

## Actions defined by Amazon Message Gateway Service
<a name="list_ssmmessages-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. For each action, the table lists the resource types and condition keys supported by that action. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateControlChannel](https://docs.aws.amazon.com/systems-manager/latest/userguide/getting-started-create-iam-instance-profile.html)  **
  - **Description:** Grants permission to register a control channel for an instance to send control messages to Systems Manager service
  - **Resource types (\*required):** 
  - **Condition keys:** [ec2:SourceInstanceARN](#list_ssmmessages-ec2_SourceInstanceARN)<br />[ssm:SourceInstanceARN](#list_ssmmessages-ssm_SourceInstanceARN)
  - **Access level:** Write

- **   [CreateDataChannel](https://docs.aws.amazon.com/systems-manager/latest/userguide/getting-started-create-iam-instance-profile.html)  **
  - **Description:** Grants permission to register a data channel for an instance to send data messages to Systems Manager service
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [OpenControlChannel](https://docs.aws.amazon.com/systems-manager/latest/userguide/getting-started-create-iam-instance-profile.html)  **
  - **Description:** Grants permission to open a websocket connection for a registered control channel stream from an instance to Systems Manager service
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [OpenDataChannel](https://docs.aws.amazon.com/systems-manager/latest/userguide/getting-started-create-iam-instance-profile.html)  **
  - **Description:** Grants permission to open a websocket connection for a registered data channel stream from an instance to Systems Manager service
  - **Resource types (\*required):** [session\*](#list_ssmmessages-resource-session)
  - **Condition keys:** [ssm:resourceTag/aws:ssmmessages:session-id](#list_ssmmessages-ssm_resourceTag_aws_ssmmessages_session-id)<br />[ssm:resourceTag/aws:ssmmessages:target-id](#list_ssmmessages-ssm_resourceTag_aws_ssmmessages_target-id)
  - **Access level:** Write



## Resource types defined by Amazon Message Gateway Service
<a name="list_ssmmessages-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [session](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html)  | arn:${Partition}:ssm:${Region}:${Account}:session/${SessionId} | [ssm:resourceTag/aws:ssmmessages:session-id](#list_ssmmessages-ssm_resourceTag_aws_ssmmessages_session-id)<br />[ssm:resourceTag/aws:ssmmessages:target-id](#list_ssmmessages-ssm_resourceTag_aws_ssmmessages_target-id) | 

## Condition keys for Amazon Message Gateway Service
<a name="list_ssmmessages-policy-keys"></a>

Amazon Message Gateway Service defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [ec2:SourceInstanceARN](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys)  | Filters access by the ARN of the instance from which the request originated | ARN | 
|   [ssm:SourceInstanceARN](https://docs.aws.amazon.com/systems-manager/latest/userguide/security_iam_service-with-iam.html#policy-conditions)  | Filters access by verifying the Amazon Resource Name (ARN) of the AWS Systems Manager's managed instance from which the request is made. This key is not present when the request comes from the managed instance authenticated with an IAM role associated with EC2 instance profile | ARN | 
|   [ssm:resourceTag/aws:ssmmessages:session-id](https://docs.aws.amazon.com/systems-manager/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#policy-conditions)  | Filters access by the user ID of the principal that started the session, as recorded in the AWS-supplied aws:ssmmessages:session-id tag | String | 
|   [ssm:resourceTag/aws:ssmmessages:target-id](https://docs.aws.amazon.com/systems-manager/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#policy-conditions)  | Filters access by the ID of the managed node that the session connects to, as recorded in the AWS-supplied aws:ssmmessages:target-id tag | String | 