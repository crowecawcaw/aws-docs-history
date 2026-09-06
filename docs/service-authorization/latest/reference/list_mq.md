

# Actions, resources, and condition keys for Amazon MQ
<a name="list_mq"></a>

Amazon MQ (service prefix: `mq`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/welcome.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/security-api-authentication-authorization.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/mq/mq.json) for this service.

**Topics**
+ [API operations defined by Amazon MQ](#list_mq-operations)
+ [Actions defined by Amazon MQ](#list_mq-actions-as-permissions)
+ [Permission-only actions for Amazon MQ](#list_mq-permission-only-actions)
+ [Resource types defined by Amazon MQ](#list_mq-resources-for-iam-policies)
+ [Condition keys for Amazon MQ](#list_mq-policy-keys)

## API operations defined by Amazon MQ
<a name="list_mq-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_mq-actions-as-permissions).




- **   CreateBroker  **
  - **IAM action:**  [mq:CreateBroker](#list_mq-action-CreateBroker)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mq:CreateTags](#list_mq-action-CreateTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** mq.amazonaws.com / **Access level:** Write

- **   CreateConfiguration  **
  - **IAM action:**  [mq:CreateConfiguration](#list_mq-action-CreateConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mq:CreateTags](#list_mq-action-CreateTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateTags  **
  - **IAM action:**  [mq:CreateTags](#list_mq-action-CreateTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   CreateUser  **
  - **IAM action:**  [mq:CreateUser](#list_mq-action-CreateUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteBroker  **
  - **IAM action:**  [mq:DeleteBroker](#list_mq-action-DeleteBroker) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConfiguration  **
  - **IAM action:**  [mq:DeleteConfiguration](#list_mq-action-DeleteConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTags  **
  - **IAM action:**  [mq:DeleteTags](#list_mq-action-DeleteTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   DeleteUser  **
  - **IAM action:**  [mq:DeleteUser](#list_mq-action-DeleteUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeBroker  **
  - **IAM action:**  [mq:DescribeBroker](#list_mq-action-DescribeBroker) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeBrokerEngineTypes  **
  - **IAM action:**  [mq:DescribeBrokerEngineTypes](#list_mq-action-DescribeBrokerEngineTypes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeBrokerInstanceOptions  **
  - **IAM action:**  [mq:DescribeBrokerInstanceOptions](#list_mq-action-DescribeBrokerInstanceOptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeConfiguration  **
  - **IAM action:**  [mq:DescribeConfiguration](#list_mq-action-DescribeConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeConfigurationRevision  **
  - **IAM action:**  [mq:DescribeConfigurationRevision](#list_mq-action-DescribeConfigurationRevision) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSharedResources  **
  - **IAM action:**  [mq:DescribeSharedResources](#list_mq-action-DescribeSharedResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeUser  **
  - **IAM action:**  [mq:DescribeUser](#list_mq-action-DescribeUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListBrokers  **
  - **IAM action:**  [mq:ListBrokers](#list_mq-action-ListBrokers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListConfigurationRevisions  **
  - **IAM action:**  [mq:ListConfigurationRevisions](#list_mq-action-ListConfigurationRevisions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListConfigurations  **
  - **IAM action:**  [mq:ListConfigurations](#list_mq-action-ListConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTags  **
  - **IAM action:**  [mq:ListTags](#list_mq-action-ListTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListUsers  **
  - **IAM action:**  [mq:ListUsers](#list_mq-action-ListUsers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   Promote  **
  - **IAM action:**  [mq:Promote](#list_mq-action-Promote) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RebootBroker  **
  - **IAM action:**  [mq:RebootBroker](#list_mq-action-RebootBroker) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateBroker  **
  - **IAM action:**  [mq:UpdateBroker](#list_mq-action-UpdateBroker)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mq:UpdateBrokerAccessConfiguration](#list_mq-action-UpdateBrokerAccessConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** mq.amazonaws.com / **Access level:** Write

- **   UpdateConfiguration  **
  - **IAM action:**  [mq:UpdateConfiguration](#list_mq-action-UpdateConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateUser  **
  - **IAM action:**  [mq:UpdateUser](#list_mq-action-UpdateUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon MQ
<a name="list_mq-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateBroker](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/rest-api-brokers.html#rest-api-brokers-methods-post)  **
  - **Description:** Grants permission to create a broker
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_mq-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_mq-aws_TagKeys)
  - **Access level:** Write

- **   [CreateConfiguration](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/rest-api-configurations.html#rest-api-configurations-methods-post)  **
  - **Description:** Grants permission to create a new configuration for the specified configuration name. Amazon MQ uses the default configuration (the engine type and engine version)
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_mq-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_mq-aws_TagKeys)
  - **Access level:** Write

- **   [CreateTags](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/rest-api-tags.html#rest-api-tags-methods-post)  **
  - **Description:** Grants permission to create tags
  - **Resource types (\*required):** [brokers](#list_mq-resource-brokers) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mq-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mq-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mq-aws_TagKeys)
  - **Resource types (\*required):** [configurations](#list_mq-resource-configurations) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mq-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mq-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mq-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [CreateUser](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/rest-api-username.html#rest-api-username-methods-post)  **
  - **Description:** Grants permission to create an ActiveMQ user
  - **Resource types (\*required):** [brokers\*](#list_mq-resource-brokers)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mq-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteBroker](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/rest-api-broker.html#rest-api-broker-methods-delete)  **
  - **Description:** Grants permission to delete a broker
  - **Resource types (\*required):** [brokers\*](#list_mq-resource-brokers)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mq-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteConfiguration](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/rest-api-configurations.html#rest-api-configurations-methods-delete)  **
  - **Description:** Grants permission to delete a configuration
  - **Resource types (\*required):** [configurations\*](#list_mq-resource-configurations)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mq-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTags](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/rest-api-tags.html#rest-api-tags-methods-delete)  **
  - **Description:** Grants permission to delete tags
  - **Resource types (\*required):** [brokers](#list_mq-resource-brokers) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mq-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mq-aws_TagKeys)
  - **Resource types (\*required):** [configurations](#list_mq-resource-configurations) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mq-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mq-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [DeleteUser](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/rest-api-username.html#rest-api-username-methods-delete)  **
  - **Description:** Grants permission to delete an ActiveMQ user
  - **Resource types (\*required):** [brokers\*](#list_mq-resource-brokers)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mq-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeBroker](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/rest-api-broker.html#rest-api-broker-methods-get)  **
  - **Description:** Grants permission to return information about the specified broker
  - **Resource types (\*required):** [brokers\*](#list_mq-resource-brokers)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mq-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeBrokerEngineTypes](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/broker-engine-types.html#broker-engine-types-http-methods)  **
  - **Description:** Grants permission to return information about broker engines
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeBrokerInstanceOptions](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/broker-instance-options.html#broker-engine-types-http-methods)  **
  - **Description:** Grants permission to return information about the broker instance options
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeConfiguration](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/rest-api-configuration.html#rest-api-configuration-methods-get)  **
  - **Description:** Grants permission to return information about the specified configuration
  - **Resource types (\*required):** [configurations\*](#list_mq-resource-configurations)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mq-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeConfigurationRevision](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/rest-api-configuration-revision.html#rest-api-configuration-revision-methods-get)  **
  - **Description:** Grants permission to return the specified configuration revision for the specified configuration
  - **Resource types (\*required):** [configurations\*](#list_mq-resource-configurations)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mq-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeSharedResources](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/brokers-broker-id-shared-resources.html)  **
  - **Description:** Grants permission to return the resources shared to a broker
  - **Resource types (\*required):** [brokers\*](#list_mq-resource-brokers)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mq-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeUser](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/rest-api-username.html#rest-api-username-methods-get)  **
  - **Description:** Grants permission to return information about an ActiveMQ user
  - **Resource types (\*required):** [brokers\*](#list_mq-resource-brokers)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mq-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListBrokers](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/rest-api-brokers.html#rest-api-brokers-methods-get)  **
  - **Description:** Grants permission to return a list of all brokers
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListConfigurationRevisions](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/rest-api-revisions.html#rest-api-revisions-methods-get)  **
  - **Description:** Grants permission to return a list of all existing revisions for the specified configuration
  - **Resource types (\*required):** [configurations\*](#list_mq-resource-configurations)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mq-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListConfigurations](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/rest-api-configurations.html#rest-api-configurations-methods-get)  **
  - **Description:** Grants permission to return a list of all configurations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTags](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/rest-api-tags.html#rest-api-tags-methods-get)  **
  - **Description:** Grants permission to return a list of tags
  - **Resource types (\*required):** [brokers](#list_mq-resource-brokers) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mq-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [configurations](#list_mq-resource-configurations) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mq-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListUsers](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/rest-api-users.html#rest-api-users-methods-get)  **
  - **Description:** Grants permission to return a list of all ActiveMQ users
  - **Resource types (\*required):** [brokers\*](#list_mq-resource-brokers)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mq-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [Promote](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/rest-api-promote.html#rest-api-promote-methods-post)  **
  - **Description:** Grants permission to promote a broker
  - **Resource types (\*required):** [brokers\*](#list_mq-resource-brokers)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mq-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RebootBroker](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/rest-api-restart.html#rest-api-reboot-methods-post)  **
  - **Description:** Grants permission to reboot a broker
  - **Resource types (\*required):** [brokers\*](#list_mq-resource-brokers)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mq-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateBroker](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/rest-api-broker.html#rest-api-broker-methods-get)  **
  - **Description:** Grants permission to add a pending configuration change to a broker
  - **Resource types (\*required):** [brokers\*](#list_mq-resource-brokers)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mq-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateConfiguration](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/rest-api-configuration.html#rest-api-configuration-methods-put)  **
  - **Description:** Grants permission to update the specified configuration
  - **Resource types (\*required):** [configurations\*](#list_mq-resource-configurations)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mq-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateUser](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/rest-api-username.html#rest-api-username-methods-put)  **
  - **Description:** Grants permission to update the information for an ActiveMQ user
  - **Resource types (\*required):** [brokers\*](#list_mq-resource-brokers)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mq-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for Amazon MQ
<a name="list_mq-permission-only-actions"></a>

The following actions are defined by Amazon MQ but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [CreateReplicaBroker](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/rest-api-brokers.html#rest-api-brokers-methods-post)  **
  - **Description:** Grants permission to create a replica broker
  - **Resource types (\*required):** [brokers\*](#list_mq-resource-brokers)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mq-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateBrokerAccessConfiguration](${AuthZDocPage}#security-api-permissions-reference)  **
  - **Description:** Grants permission to update RabbitMQ broker authentication and authorization configuration
  - **Resource types (\*required):** [brokers\*](#list_mq-resource-brokers)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mq-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon MQ
<a name="list_mq-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [brokers](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-how-it-works.html)  | arn:${Partition}:mq:${Region}:${Account}:broker:${BrokerName}:${BrokerId} | [aws:ResourceTag/${TagKey}](#list_mq-aws_ResourceTag___TagKey_) | 
|  [configurations](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-how-it-works.html)  | arn:${Partition}:mq:${Region}:${Account}:configuration:${ConfigurationId} | [aws:ResourceTag/${TagKey}](#list_mq-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon MQ
<a name="list_mq-policy-keys"></a>

Amazon MQ defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/security_iam_service-with-iam.html#security_iam_service-with-iam-tags)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/security_iam_service-with-iam.html#security_iam_service-with-iam-tags)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/security_iam_service-with-iam.html#security_iam_service-with-iam-tags)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 