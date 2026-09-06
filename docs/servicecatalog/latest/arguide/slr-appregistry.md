

AWS Service Catalog AppRegistry is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Service Catalog AppRegistry availability change](https://docs.aws.amazon.com/servicecatalog/latest/arguide/app-registry-availability-change.html).

# Using service-linked roles for AWS Service Catalog AppRegistry
<a name="slr-appregistry"></a>

 This section describes how AWS Service Catalog AppRegistry uses the service-linked role `AWSServiceCatalogAppRegistryServiceRolePolicy` to create, update, and delete resource groups in your accounts. AWS Resource Groups allows you to manage your resources in groups instead individually. You can create resource groups that contain all of the resources in AWS CloudFormation stacks. For more information, see [What are resource groups?](https://docs.aws.amazon.com/ARG/latest/userguide/resource-groups.html) in the *AWS Resource Groups User Guide*. 

 AppRegistry uses service-linked roles. A service-linked role is a type of IAM identity that links directly to an AWS service. For more information, see [IAM identities (users, user groups, and roles)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html) in the *IAM User Guide*. AppRegistry uses the service-linked role `AWSServiceRoleForAWSServiceCatalogAppRegistry`, which includes all of the permissions that are required to call other AWS services on your behalf. 

 Using service-linked roles make setting up AWS services more efficient because you don’t have to add required permissions manually. AppRegistry defines its service-linked roles with the necessary permissions, The defined permissions include the trust policy and permissions policy. The permissions policy cannot be attached to any other entity (user, group, or role). For more information, see [IAM identities (users, user groups, and roles)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html) in the *IAM User Guide*. 

 You can delete a service-linked role only after deleting the related resources. This action protects your AppRegistry resources because you cannot inadvertently remove permission to access the resources. 

**Note**  
 AppRegistry creates new tags on the resource groups `EnableAWSServiceCatalogAppRegistry` and `true`. If you modify these tags, AppRegistry loses permissions to manage service-linked resource groups that are created for applications and associated stacks. 

## Service-linked role permissions for AppRegistry
<a name="permissions-slr"></a>

 AppRegistry can call APIs on your behalf using the service-linked role `AWSServiceRoleForAWSServiceCatalogAppRegistry`. This role trusts the service principal ***servicecatalog-appregistry.amazonaws.com*** to assume the role. 

 The following role permissions policy allows AppRegistry to complete the following actions on the specified resources: 

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "cloudformation:DescribeStacks",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "resource-groups:CreateGroup",
                "resource-groups:Tag"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:RequestTag/EnableAWSServiceCatalogAppRegistry": "true"
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": [
                "resource-groups:DeleteGroup",
                "resource-groups:UpdateGroup",
                "resource-groups:GetTags",
                "resource-groups:Tag",
                "resource-groups:Untag"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceTag/EnableAWSServiceCatalogAppRegistry": "true"
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": [
                "resource-groups:GetGroup",
                "resource-groups:GetGroupConfiguration"
            ],
            "Resource": [
                "arn:*:resource-groups:*:*:group/AWS_AppRegistry*",
                "arn:*:resource-groups:*:*:group/AWS_Cloudformation_Stack*"
            ]
        }
     ]
  }
```

------

 To allow an entity to create, edit, or delete a service-linked role, you must configure permissions. For more information, see [Service-linked role permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions) in the *IAM User Guide.* 

 You can allow an entity to create the service-linked role `AWSServiceRoleForAWSServiceCatalogAppRegistry` by adding this statement to the permissions policy for the IAM entity that creates the service-linked role. 

```
{
    "Effect": "Allow",
    "Action": [
        "iam:CreateServiceLinkedRole"
    ],
    "Resource": "arn:aws:iam::*:role/aws-service-role/servicecatalog-appregistry.amazonaws.com/AWSServiceRoleForAWSServiceCatalogAppRegistry*",
    "Condition": {"StringLike": {"iam:AWSServiceName": "servicecatalog-appregistry.amazonaws.com"}}
}
```

## Creating a service-linked role for AppRegistry
<a name="create-role"></a>

 AppRegistry automatically creates your service-linked role when you create an application or update an existing application in the AWS Management Console, AWS CLI, or AWS API. 

 When customers request specific operations, AppRegistry automatically creates roles for them. 

**Important**  
 If you completed an action with another AWS service that uses features that your service-linked role supports, the role can appear in your AWS account. 

 You can use the AWS Management Console to create a service-linked role with the use case `AWSServiceRoleForAWSServiceCatalogAppRegistry`. 

 You can use the AWS CLI or AWS API to create a service-linked role with the service name ***servicecatalog-appregistry.amazonaws.com***. 

 If you delete your service-linked role, you can create the role again in your account using the same process as before. For more information about creating and deleting service-linked roles, see [Creating a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html) in the *IAM User Guide.* 

## Editing a Service-Linked Role for AppRegistry
<a name="edit-slr"></a>

 After you create a service-linked role, you cannot change the name of the role because various entities might reference it. However, you can use the IAM console, AWS CLI, or AWS API to edit the role description. For more information, see [Editing a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role) in the *IAM User Guide*. 

## Deleting a Service-Linked Role for AppRegistry
<a name="delete-slr"></a>

 If you no longer need to use a feature or service that requires a service-linked role, we recommend that you delete the role. This way, you don't have an unused entity that's not actively monitored or maintained. 

 You must clean your service-linked role's resources before you can delete the role. You can use AppRegistry to clean the resources and then use the IAM console, AWS CLI, or AWS API to delete the role. For more information, see [Deleting roles or instance profiles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_delete.html) in the *IAM User Guide*. 

 To clean the resources that are associated with your service-linked role resources before you delete them, you must disassociate all resources from your applications. Then, you can disassociate all attribute groups from your applications. Finally, you can delete your applications. 

## Supported AWS Regions for AppRegistry service-linked roles
<a name="regions-slr"></a>

 AppRegistry supports using service-linked roles in all AWS Regions where AppRegistry is available. For more information, see [AWS service endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html) in the *AWS General Reference guide*. 