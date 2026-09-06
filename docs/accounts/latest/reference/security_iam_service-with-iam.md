

# How AWS Account Management works with IAM
<a name="security_iam_service-with-iam"></a>

This information is most relevant for AWS accounts that you create when you use our advanced AWS experience. To learn about how access control works for our new AWS experience, see [Compare access management](sign-up-for-aws.md#compare-access-management).

Before you use IAM to manage access to Account Management, learn what IAM features are available to use with Account Management.






**IAM features you can use with AWS Account Management**  

| IAM feature | Account Management support | 
| --- | --- | 
| [Identity-based policies](#security_iam_service-with-iam-id-based-policies) |  Yes | 
| [Resource-based policies](#security_iam_service-with-iam-resource-based-policies) |  No  | 
| [Policy actions](#security_iam_service-with-iam-id-based-policies-actions) |  Yes | 
| [Policy resources](#security_iam_service-with-iam-id-based-policies-resources) |  Yes | 
| [Policy condition keys](#security_iam_service-with-iam-id-based-policies-conditionkeys) |  Yes | 
| [ACLs](#security_iam_service-with-iam-acls) |  No  | 
| [ABAC (tags in policies)](#security_iam_service-with-iam-tags) |  No  | 
| [Temporary credentials](#security_iam_service-with-iam-roles-tempcreds) |  Yes | 
| [Principal permissions](#security_iam_service-with-iam-principal-permissions) |  Yes | 
| [Service roles](#security_iam_service-with-iam-roles-service) |  No  | 
| [Service-linked roles](#security_iam_service-with-iam-roles-service-linked) |  No  | 

To get a high-level view of how Account Management and other AWS services work with most IAM features, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

## Identity-based policies for Account Management
<a name="security_iam_service-with-iam-id-based-policies"></a>

**Supports identity-based policies:** Yes

Identity-based policies are JSON permissions policy documents that you can attach to an identity, such as an IAM user, group of users, or role. These policies control what actions users and roles can perform, on which resources, and under what conditions. To learn how to create an identity-based policy, see [Define custom IAM permissions with customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) in the *IAM User Guide*.

With IAM identity-based policies, you can specify allowed or denied actions and resources as well as the conditions under which actions are allowed or denied. To learn about all of the elements that you can use in a JSON policy, see [IAM JSON policy elements reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html) in the *IAM User Guide*.

### Identity-based policy examples for Account Management
<a name="security_iam_service-with-iam-id-based-policies-examples"></a>



To view examples of Account Management identity-based policies, see [Identity-based policy examples for AWS Account Management](security_iam_id-based-policy-examples.md).

## Resource-based policies within Account Management
<a name="security_iam_service-with-iam-resource-based-policies"></a>

**Supports resource-based policies:** No 

Resource-based policies are JSON policy documents that you attach to a resource. Examples of resource-based policies are IAM *role trust policies* and Amazon S3 *bucket policies*. In services that support resource-based policies, service administrators can use them to control access to a specific resource. For the resource where the policy is attached, the policy defines what actions a specified principal can perform on that resource and under what conditions. You must [specify a principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html) in a resource-based policy. Principals can include accounts, users, roles, federated users, or AWS services.

To enable cross-account access, you can specify an entire account or IAM entities in another account as the principal in a resource-based policy. For more information, see [Cross account resource access in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-cross-account-resource-access.html) in the *IAM User Guide*.

## Policy actions for Account Management
<a name="security_iam_service-with-iam-id-based-policies-actions"></a>

**Supports policy actions:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.



To see a list of Account Management actions, see [Actions defined by AWS Account Management](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsaccountmanagement.html#awsaccountmanagement-actions-as-permissions) in the *Service Authorization Reference*.

Policy actions in Account Management use the following prefix before the action.

```
account
```

To specify multiple actions in a single statement, separate them with commas.

```
"Action": [
      "account:{{action1}}",
      "account:{{action2}}"
         ]
```





You can specify multiple actions using wildcards (\*). For example, to specify all actions that work with an AWS account's alternate contacts, include the following action.

```
"Action": "account:*AlternateContact"
```

To view examples of Account Management identity-based policies, see [Identity-based policy examples for AWS Account Management](security_iam_id-based-policy-examples.md).

## Policy resources for Account Management
<a name="security_iam_service-with-iam-id-based-policies-resources"></a>

**Supports policy resources:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

The Account Management service supports the following specific resource types in an IAM policy's `Resource` element to help you filter the policy and distinguish between these types of AWS accounts:
+ **account**

  This `resource` type matches only standalone AWS accounts that are not member accounts in an organization managed by the AWS Organizations service.
+ **accountInOrganization**

  This `resource` type matches only AWS accounts that are member accounts in an organization managed by the AWS Organizations service.

To see a list of Account Management resource types and their ARNs, see [Resources defined by AWS Account Management](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsaccountmanagement.html#awsaccountmanagement-resources-for-iam-policies) in the *Service Authorization Reference*. To learn with which actions you can specify the ARN of each resource, see [Actions defined by AWS Account Management](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsaccountmanagement.html#awsaccountmanagement-actions-as-permissions).

To view examples of Account Management identity-based policies, see [Identity-based policy examples for AWS Account Management](security_iam_id-based-policy-examples.md).

## Policy condition keys for Account Management
<a name="security_iam_service-with-iam-id-based-policies-conditionkeys"></a>

**Supports service-specific policy condition keys:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html), such as equals or less than, to match the condition in the policy with values in the request. To see all AWS global condition keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

The Account Management service supports the following condition keys that you can use to provide fine-grained filtering for your IAM policies:
+  **account:TargetRegion**

  This condition key takes an argument that consists of a list of [AWS Region codes](https://docs.aws.amazon.com/general/latest/gr/rande.html#regional-endpoints). It lets you filter the policy to affect only those actions that apply to the specified Regions.
+ **account:AlternateContactTypes**

  This condition key takes a list of alternate contact types:
  + BILLING
  + OPERATIONS
  + SECURITY

  Using this key lets you filter the request to only those actions that target the specified alternate contact types.
+ **account:AccountResourceOrgPaths**

  This condition key takes an argument that consists of a list of paths through your organization's hierarchy to specific organizational units (OU). It lets you filter the policy to affect only target accounts in a matching OU.

  ```
  {{o-aa111bb222}}/{{r-a1b2}}/{{ou-a1b2-f6g7h111}}/*
  ```
+ **account:AccountResourceOrgTags**

  This condition key takes an argument that consists of a list of tag keys and values. It lets you filter the policy to affect only those accounts that are members of an organization and that are tagged with the specified tag keys and values.
+ **account:EmailTargetDomain**

  This condition key takes an argument that consists of a list of email domains. It lets you filter the policy to affect only those actions that match the specified email domains. This condition key is case-sensitive. You should use `StringEqualsIgnoreCase` instead of `StringEquals` in the condition block of the policy to control the action based on the target email address domain. Here is a sample policy allowing the `account:StartPrimaryEmailUpdate` action to complete when the email domain contains `example.com`, `company.org`, or any combination of case, such as `EXAMPLE.COM`.

  ```
  {
      "Version": "2012-10-17",		 	 	 
      "Statement": [
          {
              "Sid": "AllowConditionKey",
              "Effect": "Allow",
              "Action": [
                  "account:StartPrimaryEmailUpdate"
              ],
              "Resource": "*",
              "Condition": {
                  "StringEqualsIgnoreCase": {
                      "account:EmailTargetDomain": [
                          "example.com",
                          "company.org"
                      ]
                  }
              }
          }
      ]
  }
  ```

To see a list of Account Management condition keys, see [Condition keys for AWS Account Management](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsaccountmanagement.html#awsaccountmanagement-policy-keys) in the *Service Authorization Reference*. To learn with which actions and resources you can use a condition key, see [Actions defined by AWS Account Management](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsaccountmanagement.html#awsaccountmanagement-actions-as-permissions).

To view examples of Account Management identity-based policies, see [Identity-based policy examples for AWS Account Management](security_iam_id-based-policy-examples.md).

## Access control lists in Account Management
<a name="security_iam_service-with-iam-acls"></a>

**Supports ACLs:** No 

Access control lists (ACLs) control which principals (account members, users, or roles) have permissions to access a resource. ACLs are similar to resource-based policies, although they do not use the JSON policy document format.

## Attribute-based access control with Account Management
<a name="security_iam_service-with-iam-tags"></a>

**Supports ABAC (tags in policies):** No 

Attribute-based access control (ABAC) is an authorization strategy that defines permissions based on attributes. In AWS, these attributes are called *tags*. You can attach tags to IAM entities (users or roles) and to many AWS resources. Tagging entities and resources is the first step of ABAC. Then you design ABAC policies to allow operations when the principal's tag matches the tag on the resource that they are trying to access.

ABAC is helpful in environments that are growing rapidly and helps with situations where policy management becomes cumbersome.

For AWS Account Management, tag-based access control is supported only through the `account:AccountResourceOrgTags/key-name` condition key. The standard `aws:ResourceTag/key-name` condition key is not supported for APIs in the account namespace.

**Example JSON policy using the supported condition key**

The following example policy allows access to view contact information for accounts tagged with the key "CostCenter" and either value "12345" or "67890" in your organization.

------
#### [ JSON ]

****  

```
{
   "Version":"2012-10-17",		 	 	 
   "Statement":[
      {
         "Effect":"Allow",
         "Action":[
            "account:GetContactInformation",
            "account:GetAlternateContact"
         ],
         "Resource":"*",
         "Condition":{
            "ForAnyValue:StringEquals":{
               "account:AccountResourceOrgTags/CostCenter":[
                  "12345",
                  "67890"
               ]
            }
         }
      }
   ]
}
```

------

For more information about ABAC, see [Define permissions based on attributes with ABAC authorization](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) and [IAM tutorial: Define permissions to access AWS resources based on tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html) in the *IAM User Guide*.

## Using temporary credentials with Account Management
<a name="security_iam_service-with-iam-roles-tempcreds"></a>

**Supports temporary credentials:** Yes

Temporary credentials provide short-term access to AWS resources and are automatically created when you use federation or switch roles. AWS recommends that you dynamically generate temporary credentials instead of using long-term access keys. For more information, see [Temporary security credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) and [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

## Cross-service principal permissions for Account Management
<a name="security_iam_service-with-iam-principal-permissions"></a>

**Supports forward access sessions (FAS):** Yes

 Forward access sessions (FAS) use the permissions of the principal calling an AWS service, combined with the requesting AWS service to make requests to downstream services. For policy details when making FAS requests, see [Forward access sessions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_forward_access_sessions.html). 

## Service roles for Account Management
<a name="security_iam_service-with-iam-roles-service"></a>

**Supports service roles:** No 

 A service role is an [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) that a service assumes to perform actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For more information, see [Create a role to delegate permissions to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html) in the *IAM User Guide*. 

## Service-linked roles for Account Management
<a name="security_iam_service-with-iam-roles-service-linked"></a>

**Supports service-linked roles:** No 

 A service-linked role is a type of service role that is linked to an AWS service. The service can assume the role to perform an action on your behalf. Service-linked roles appear in your AWS account and are owned by the service. An IAM administrator can view, but not edit the permissions for service-linked roles. 

For details about creating or managing service-linked roles, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html). Find a service in the table that includes a `Yes` in the **Service-linked role** column. Choose the **Yes** link to view the service-linked role documentation for that service.