

# How Amazon Managed Service for Apache Flink works with IAM
<a name="security_iam_service-with-iam"></a>





In Amazon MSF, you use IAM in the following different contexts:
+ [Application permissions](#security_iam_application_permissions): Control access by the application to external resources, such as Amazon S3, Amazon Kinesis Data Streams, or Amazon DynamoDB, that use IAM authentication.
+ [Application management and lifecycle control permissions](#security_iam_application_management): Control use of Amazon MSF API actions, such as [CreateApplication](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_CreateApplication.html), [StartApplication](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_StartApplication.html), and [UpdateApplication](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_UpdateApplication.html), which control the application lifecycle. For a complete list of all Amazon MSF API actions that you can specify in the `Action` element of an IAM policy statement, see [Actions defined by Amazon Kinesis Analytics V2](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonkinesisanalyticsv2.html#amazonkinesisanalyticsv2-actions-as-permissions) in the *Service Authorization Reference*.

**Topics**
+ [Application permissions](#security_iam_application_permissions)
+ [Application management and lifecycle control permissions](#security_iam_application_management)
+ [Identity-based policies for Managed Service for Apache Flink](#security_iam_service-with-iam-id-based-policies)
+ [Resource-based policies within Managed Service for Apache Flink](#security_iam_service-with-iam-resource-based-policies)
+ [Access control lists (ACLs) in Managed Service for Apache Flink](#security_iam_service-with-iam-acls)
+ [Service roles for Managed Service for Apache Flink](#security_iam_service-with-iam-roles-service)
+ [Service-linked roles for Managed Service for Apache Flink](#security_iam_service-with-iam-roles-service-linked)

## Application permissions
<a name="security_iam_application_permissions"></a>

You control IAM permissions of an Amazon MSF application with the IAM role assigned to the application, as part of the application configuration. This IAM role determines application’s permissions to access other services, such as Amazon S3, Kinesis Data Streams, or DynamoDB, which use IAM for authorization.

**Warning**  
Changing the permissions for a service role might break Amazon MSF functionality. Make sure you don't remove permissions for the application to download the application code from the Amazon S3 bucket, and send logs to Amazon CloudWatch.

Assigning permissions to the application using [resource-based policies](#security_iam_service-with-iam-resource-based-policies) isn't supported. You can't specify an Amazon MSF application as principal in a policy attached to the resource to be accessed.

**Topics**
+ [Permissions to access the application code and application logs](#security_iam_permissions_access_application_code)
+ [Cross-service confused deputy prevention](#security_iam_cross_service_confused_deputy)

### Permissions to access the application code and application logs
<a name="security_iam_permissions_access_application_code"></a>

Amazon MSF also uses the application IAM role to access the application code uploaded in an Amazon S3 bucket, and to write the application logs to Amazon CloudWatch Logs.

When you create or update the application using the AWS Management Console, choose **Create / update IAM role <role-name> with required policies** in the Application configuration, Amazon MSF automatically creates and modifies the IAM role assigning the required permissions to Amazon S3 and CloudWatch Logs.

If you create the IAM role manually or if you create and manage the application using automation tools, you must add the following permissions to the application IAM role.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "ReadCode",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:GetObjectVersion"
            ],
            "Resource": [
                "arn:aws:s3:::{{amzn-s3-demo-bucket}}/{{path-to-application-code}}"
            ]
        },
        {
            "Sid": "ListCloudwatchLogGroups",
            "Effect": "Allow",
            "Action": [
                "logs:DescribeLogGroups"
            ],
            "Resource": [
                "arn:aws:logs:{{us-east-1}}:{{123456789012}}:log-group:*"
            ]
        },
        {
            "Sid": "ListCloudwatchLogStreams",
            "Effect": "Allow",
            "Action": [
                "logs:DescribeLogStreams"
            ],
            "Resource": [
                "arn:aws:logs:{{us-east-1}}:{{123456789012}}:log-group:/aws/kinesis-analytics/{{application-name}}:log-stream:*"
            ]
        },
        {
            "Sid": "PutCloudwatchLogs",
            "Effect": "Allow",
            "Action": [
                "logs:PutLogEvents"
            ],
            "Resource": [
                "arn:aws:logs:{{us-east-1}}:{{123456789012}}:log-group:/aws/kinesis-analytics/{{application-name}}:log-stream:kinesis-analytics-log-stream"
            ]
        }
    ]
}
```

------

### Cross-service confused deputy prevention
<a name="security_iam_cross_service_confused_deputy"></a>

When an Amazon MSF application calls a different AWS service, you can provide more granular access permissions. For example, if an IAM role is reused across multiple applications, an application may get access to a resource it should not be have access to. This is known as the [confused deputy problem](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html). For information about how the accessed resource can restrict access to a specific Amazon MSF application, see [Cross-service confused deputy prevention](iam-cross-service-confused-deputy-prevention.md).

## Application management and lifecycle control permissions
<a name="security_iam_application_management"></a>

Actions to manage the application and its lifecycle, such as [CreateApplication](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_CreateApplication.html), [StartApplication](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_StartApplication.html), and [UpdateApplication](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_UpdateApplication.html), are controlled through identity-based policies associated to the resource performing the action, such as an IAM user, IAM group, or a resource such as AWS Lambda calling the Amazon MSF API.

**Note**  
The API and SDK controlling Amazon MSF application lifecycle is called Amazon Kinesis Analytics V2, for backward compatibility reasons.

Assigning permissions for application lifecycle actions using resource-based policies attached to the Amazon MSF application isn't supported. The application IAM role isn't used to control access to the application lifecycle actions. You should not add application lifecycle permissions to the application role.

The following table lists the IAM features you can use with Amazon MSF application lifecycle actions.


| IAM feature | Managed Service for Apache Flink support | 
| --- | --- | 
| [Identity-based policies](#security_iam_service-with-iam-id-based-policies) |  Yes | 
| [Resource-based policies](#security_iam_service-with-iam-resource-based-policies) | No | 
| [Policy actions](#security_iam_service-with-iam-id-based-policies-actions) |  Yes | 
| [Policy resources](#security_iam_service-with-iam-id-based-policies-resources) |  Yes | 
| [Policy condition keys](#security_iam_service-with-iam-id-based-policies-conditionkeys) | Yes | 
| [ACLs](#security_iam_service-with-iam-acls) | No | 
| [ABAC (tags in policies)](#security_iam_service-with-iam-tags) |  Yes | 
| [Temporary credentials](#security_iam_service-with-iam-roles-tempcreds) |  Yes | 
| [Cross-service principal permissions](#security_iam_service-with-iam-principal-permissions) |  Yes | 
| [Service roles](#security_iam_service-with-iam-roles-service) | No | 
| [Service-linked roles](#security_iam_service-with-iam-roles-service-linked) | No | 
+ For a high-level view of how Managed Service for Apache Flink and other AWS services work with most IAM features, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.
+ For information about the service-specific resources, actions, and condition context keys that you can use in IAM permission policies, see [Actions, resources, and condition keys for Amazon Kinesis Analytics V2](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonkinesisanalyticsv2.html) in the *Service Authorization Reference*.

**Topics**
+ [Policy actions](#security_iam_service-with-iam-id-based-policies-actions)
+ [Policy resources](#security_iam_service-with-iam-id-based-policies-resources)
+ [Policy condition keys](#security_iam_service-with-iam-id-based-policies-conditionkeys)
+ [ABAC](#security_iam_service-with-iam-tags)
+ [Temporary credentials](#security_iam_service-with-iam-roles-tempcreds)
+ [Principal permissions](#security_iam_service-with-iam-principal-permissions)

### Application lifecycle policy actions
<a name="security_iam_service-with-iam-id-based-policies-actions"></a>

**Supports policy actions:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Policy actions in Amazon MSF use the `kinesisanalytics` prefix before the action. Amazon MSF APIs and SDKs use the `Amazon Kinesis Analytics V2` prefix.

To specify multiple actions in a single statement, separate them with commas. The following example shows the syntax for specifying Amazon MSF policy actions.

```
"Action" : [
   "kinesisanalytics:{{action1}}",
   "kinesisanalytics:{{action2}}"
]
```

You can also specify multiple actions using wildcards (\*). For example, to specify all actions that begin with the word `Describe`, include the following action.

```
"Action": "kinesisanalytics:Describe*"
```

To see a complete list of all Amazon MSF API actions that you can specify in the `Action` element of an IAM policy statement, see [Actions defined by Amazon Kinesis Analytics V2](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonkinesisanalyticsv2.html#amazonkinesisanalyticsv2-actions-as-permissions).

To view examples of Amazon MSF identity-based policies, see [Identity-based policy examples](security_iam_id-based-policy-examples.md).

### Application lifecycle policy resources
<a name="security_iam_service-with-iam-id-based-policies-resources"></a>

**Supports policy resources:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

Permissions for Amazon MSF application lifecycle actions are defined for **each application**. The `Resource` JSON element in an IAM policy defines the Amazon MSF application to which the permissions apply.

You can assign permission to a single application by specifying the application ARN, or a group of application by using wildcards. The following example shows the syntax of the `Resource` element.

```
"Resouce" : "arn:{{partition}}:kinesisanalytics:{{Region}}:{{account}}:application/{{application-name}}
```

You can also assign permissions to control a subset of applications using wildcards. For example, you can assign permissions to control all applications whose name starts with a specific prefix.

```
"Resouce" : "arn:{{partition}}:kinesisanalytics:{{Region}}:{{account}}:application/{{application-name-prefix*}}
```

### Application lifecycle policy condition keys
<a name="security_iam_service-with-iam-id-based-policies-conditionkeys"></a>

**Supports service-specific policy condition keys:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html), such as equals or less than, to match the condition in the policy with values in the request. To see all AWS global condition keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

You can use condition keys to control permissions to Amazon MSF application lifecycle actions. To see a list of Managed Service for Apache Flink condition keys, see [Condition Keys for Amazon Managed Service for Apache Flink](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awskinesisanalytics.html#awskinesisanalytics-policy-keys) in the *Service Authorization Reference*. To learn with which actions and resources you can use a condition key, see [Actions Defined by Amazon Managed Service for Apache Flink](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awskinesisanalytics.html#awskinesisanalytics-actions-as-permissions).

### Attribute-based access control (ABAC) with Managed Service for Apache Flink
<a name="security_iam_service-with-iam-tags"></a>

**Supports ABAC (tags in policies):** Yes

Using condition keys, you can implement attribute-based access control (ABAC), which is an authorization strategy that defines permissions based on attributes. In AWS, these attributes are called *tags*. You can attach tags to IAM entities (users or roles) and to many AWS resources. Tagging entities and resources is the first step of ABAC. Then, you design ABAC policies to allow operations when the principal's tag matches the tag on the resource that they are trying to access.

ABAC is helpful in environments that are growing rapidly and helps with situations where policy management becomes cumbersome.

To control access based on tags, you provide tag information in the [condition element](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) of a policy using the `aws:ResourceTag/key-name`, `aws:RequestTag/key-name`, or `aws:TagKeys` condition keys. If a service supports all three condition keys for every resource type, then the value is **Yes** for the service. If a service supports all three condition keys for only some resource types, then the value is **Partial**. 
+ For more information about ABAC, see [Define permissions based on attributes with ABAC authorization](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html).
+ To view a tutorial with the steps for setting up ABAC, see [IAM tutorial: Define permissions to access AWS resources based on tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html).

### Using temporary credentials
<a name="security_iam_service-with-iam-roles-tempcreds"></a>

**Supports temporary credentials:** Yes

Amazon MSF application lifecycle actions support temporary credentials.

You're using temporary credentials if you sign in to the AWS Management Console using any method except a user name and password. For example, when you access AWS using your company's single sign-on (SSO) link, that process automatically creates temporary credentials. You also automatically create temporary credentials when you sign in to the console as a user and then switch roles. For more information about switching roles, see [Switch from a user to an IAM role (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-console.html).

You can manually create temporary credentials using the AWS CLI or AWS API. You can then use those temporary credentials to access AWS. We recommend that you dynamically generate temporary credentials instead of using long-term access keys. For more information, see [Temporary security credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html).

### Cross-service principal permissions
<a name="security_iam_service-with-iam-principal-permissions"></a>

**Supports forward access sessions (FAS):** Yes

Amazon MSF application lifecycle actions support cross-service principal permissions.

When you use an IAM user or role to perform actions in AWS, you're considered a principal. When you use some services, you might perform an action that then initiates another action in a different service. Forward access sessions (FAS) uses the permissions of the principal calling an AWS service, combined with the requesting AWS service to make requests to downstream services. FAS requests are only made when a service receives a request that requires interactions with other AWS services or resources to complete. In this case, you must have permissions to perform both actions. For policy details when making FAS requests, see [Forward access sessions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_forward_access_sessions.html).

## Identity-based policies for Managed Service for Apache Flink
<a name="security_iam_service-with-iam-id-based-policies"></a>

**Supports identity-based policies:** Yes

Identity-based policies are JSON permissions policy documents that you can attach to an identity, such as an IAM user, group of users, or role. These policies control what actions users and roles can perform, on which resources, and under what conditions. To learn how to create an identity-based policy, see [Define custom IAM permissions with customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) in the *IAM User Guide*.

With IAM identity-based policies, you can specify allowed or denied actions and resources as well as the conditions under which actions are allowed or denied. To learn about all of the elements that you can use in a JSON policy, see [IAM JSON policy elements reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html) in the *IAM User Guide*.

### Identity-based policy examples for Managed Service for Apache Flink
<a name="security_iam_service-with-iam-id-based-policies-examples"></a>



To view examples of Managed Service for Apache Flink identity-based policies, see [Identity-based policy examples for Amazon Managed Service for Apache Flink](security_iam_id-based-policy-examples.md).

## Resource-based policies within Managed Service for Apache Flink
<a name="security_iam_service-with-iam-resource-based-policies"></a>

Amazon Managed Service for Apache Flink currently does not support resource-based access control.

## Access control lists (ACLs) in Managed Service for Apache Flink
<a name="security_iam_service-with-iam-acls"></a>

**Supports ACLs:** No 

Access control lists (ACLs) control which principals (account members, users, or roles) have permissions to access a resource. ACLs are similar to resource-based policies, although they do not use the JSON policy document format.

## Service roles for Managed Service for Apache Flink
<a name="security_iam_service-with-iam-roles-service"></a>

**Supports service roles:** Yes

 A service role is an [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) that a service assumes to perform actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For more information, see [Create a role to delegate permissions to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html) in the *IAM User Guide*. 

**Warning**  
Changing the permissions for a service role might break Managed Service for Apache Flink functionality. Edit service roles only when Managed Service for Apache Flink provides guidance to do so.

## Service-linked roles for Managed Service for Apache Flink
<a name="security_iam_service-with-iam-roles-service-linked"></a>

**Supports service-linked roles:** Yes

 A service-linked role is a type of service role that is linked to an AWS service. The service can assume the role to perform an action on your behalf. Service-linked roles appear in your AWS account and are owned by the service. An IAM administrator can view, but not edit the permissions for service-linked roles. 

For details about creating or managing service-linked roles, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html). Find a service in the table that includes a `Yes` in the **Service-linked role** column. Choose the **Yes** link to view the service-linked role documentation for that service.