

# How Amazon VPC Lattice works with IAM
<a name="security_iam_service-with-iam"></a>

Before you use IAM to manage access to VPC Lattice, learn what IAM features are available to use with VPC Lattice.




| IAM feature | VPC Lattice support | 
| --- | --- | 
| [Identity-based policies](#security_iam_service-with-iam-id-based-policies) |  Yes | 
| [Resource-based policies](#security_iam_service-with-iam-resource-based-policies) |  Yes | 
| [Policy actions](#security_iam_service-with-iam-id-based-policies-actions) |  Yes | 
| [Policy resources](#security_iam_service-with-iam-id-based-policies-resources) |  Yes | 
| [Policy condition keys](#security_iam_service-with-iam-id-based-policies-conditionkeys) |  Yes | 
| [ACLs](#security_iam_service-with-iam-acls) |  No  | 
| [ABAC (tags in policies)](#security_iam_service-with-iam-tags) |  Yes | 
| [Temporary credentials](#security_iam_service-with-iam-roles-tempcreds) |  Yes | 
| [Service roles](#security_iam_service-with-iam-roles-service) |  No  | 
| [Service-linked roles](#security_iam_service-with-iam-roles-service-linked) |  Yes | 

For a high-level view of how VPC Lattice and other AWS services work with most IAM features, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

## Identity-based policies for VPC Lattice
<a name="security_iam_service-with-iam-id-based-policies"></a>

**Supports identity-based policies:** Yes

Identity-based policies are JSON permissions policy documents that you can attach to an identity, such as an IAM user, group of users, or role. These policies control what actions users and roles can perform, on which resources, and under what conditions. To learn how to create an identity-based policy, see [Define custom IAM permissions with customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) in the *IAM User Guide*.

With IAM identity-based policies, you can specify allowed or denied actions and resources as well as the conditions under which actions are allowed or denied. To learn about all of the elements that you can use in a JSON policy, see [IAM JSON policy elements reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html) in the *IAM User Guide*.

## Resource-based policies within VPC Lattice
<a name="security_iam_service-with-iam-resource-based-policies"></a>

**Supports resource-based policies:** Yes

Resource-based policies are JSON policy documents that you attach to a resource in AWS. In AWS services that support resource-based policies, service administrators can use them to control access to a specific resource of that AWS service. For the resource where the policy is attached, the policy defines what actions a specified principal can perform on that resource and under what conditions. You must specify a principal in a resource-based policy.

VPC Lattice supports *auth policies*, a resource-based policy that lets you control access to services in your service network. For more information, see [Control access to VPC Lattice services using auth policies](auth-policies.md).

VPC Lattice also supports resource-based permissions policies for integration with AWS Resource Access Manager. You can use these resource-based policies to grant permission to manage connectivity to other AWS accounts or organizations for services, resource configurations, and service networks. For more information, see [Share your VPC Lattice entities](sharing.md).

## Policy actions for VPC Lattice
<a name="security_iam_service-with-iam-id-based-policies-actions"></a>

**Supports policy actions:** Yes

In an IAM policy statement, you can specify any API action from any service that supports IAM. For VPC Lattice, use the following prefix with the name of the API action: `vpc-lattice:`. For example: `vpc-lattice:CreateService`, `vpc-lattice:CreateTargetGroup`, and `vpc-lattice:PutAuthPolicy`.

To specify multiple actions in a single statement, separate them with commas, as follows:

```
"Action": [ "vpc-lattice:{{action1}}", "vpc-lattice:{{action2}}" ]
```

You can also specify multiple actions using wildcards. For example, you can specify all actions whose names begin with the word `Get`, as follows:

```
"Action": "vpc-lattice:Get*"
```

For a complete list of VPC Lattice API actions, see [Actions defined by Amazon VPC Lattice ](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonvpclattice.html#amazonvpclattice-actions-as-permissions) in the *Service Authorization Reference*.

## Policy resources for VPC Lattice
<a name="security_iam_service-with-iam-id-based-policies-resources"></a>

**Supports policy resources:** Yes

In an IAM policy statement, the `Resource` element specifies the object or objects that the statement covers. For VPC Lattice, each IAM policy statement applies to the resources that you specify using their ARNs.

The specific Amazon Resource Name (ARN) format depends on the resource. When you provide an ARN, replace the {{italicized}} text with your resource-specific information. 
+ **Access log subscriptions:**

  ```
  "Resource": "arn:aws:vpc-lattice:{{region}}:{{account-id}}:accesslogsubscription/{{access-log-subscription-id}}"
  ```
+ **Listeners:**

  ```
  "Resource": "arn:aws:vpc-lattice:{{region}}:{{account-id}}:service/{{service-id}}/listener/{{listener-id}}"
  ```
+ **Resource gateways**

  ```
  "Resource": "arn:aws:vpc-lattice:{{region}}:{{account-id}}:resourcegateway/{{resource-gateway-id}}"
  ```
+ **Resource configuration**

  ```
  "Resource": "arn:aws:vpc-lattice:{{region}}:{{account-id}}:resourceconfiguration/{{resource-configuration-id}}"
  ```
+ **Rules:**

  ```
  "Resource": "arn:aws:vpc-lattice:{{region}}:{{account-id}}:service/{{service-id}}/listener/{{listener-id}}/rule/{{rule-id}}"
  ```
+ **Services:**

  ```
  "Resource": "arn:aws:vpc-lattice:{{region}}:{{account-id}}:service/{{service-id}}"
  ```
+ **Service networks:**

  ```
  "Resource": "arn:aws:vpc-lattice:{{region}}:{{account-id}}:servicenetwork/{{service-network-id}}"
  ```
+ **Service network service associations:**

  ```
  "Resource": "arn:aws:vpc-lattice:{{region}}:{{account-id}}:servicenetworkserviceassociation/{{service-network-service-association-id}}"
  ```
+ **Service network resource configuration associations**

  ```
  "Resource": "arn:aws:vpc-lattice:{{region}}:{{account-id}}:servicenetworkresourceassociation/{{service-network-resource-association-id}}"
  ```
+ **Service network VPC associations:**

  ```
  "Resource": "arn:aws:vpc-lattice:{{region}}:{{account-id}}:servicenetworkvpcassociation/{{service-network-vpc-association-id}}"
  ```
+ **Target groups:**

  ```
  "Resource": "arn:aws:vpc-lattice:{{region}}:{{account-id}}:targetgroup/{{target-group-id}}"
  ```

## Policy condition keys for VPC Lattice
<a name="security_iam_service-with-iam-id-based-policies-conditionkeys"></a>

**Supports service-specific policy condition keys:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html), such as equals or less than, to match the condition in the policy with values in the request. To see all AWS global condition keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

To see a list of the VPC Lattice condition keys, see [Condition keys for Amazon VPC Lattice](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonvpclattice.html#amazonvpclattice-policy-keys) in the *Service Authorization Reference*.

AWS supports global condition keys and service-specific condition keys. For information about AWS global condition keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

## Access control lists (ACLs) in VPC Lattice
<a name="security_iam_service-with-iam-acls"></a>

**Supports ACLs:** No 

Access control lists (ACLs) control which principals (account members, users, or roles) have permissions to access a resource. ACLs are similar to resource-based policies, although they do not use the JSON policy document format.

## Attribute-based access control (ABAC) with VPC Lattice
<a name="security_iam_service-with-iam-tags"></a>

**Supports ABAC (tags in policies):** Yes

Attribute-based access control (ABAC) is an authorization strategy that defines permissions based on attributes called tags. You can attach tags to IAM entities and AWS resources, then design ABAC policies to allow operations when the principal's tag matches the tag on the resource.

To control access based on tags, you provide tag information in the [condition element](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) of a policy using the `aws:ResourceTag/{{key-name}}`, `aws:RequestTag/{{key-name}}`, or `aws:TagKeys` condition keys.

If a service supports all three condition keys for every resource type, then the value is **Yes** for the service. If a service supports all three condition keys for only some resource types, then the value is **Partial**.

For more information about ABAC, see [Define permissions with ABAC authorization](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*. To view a tutorial with steps for setting up ABAC, see [Use attribute-based access control (ABAC)](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html) in the *IAM User Guide*.

## Using temporary credentials with VPC Lattice
<a name="security_iam_service-with-iam-roles-tempcreds"></a>

**Supports temporary credentials:** Yes

Temporary credentials provide short-term access to AWS resources and are automatically created when you use federation or switch roles. AWS recommends that you dynamically generate temporary credentials instead of using long-term access keys. For more information, see [Temporary security credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) and [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

## Service roles for VPC Lattice
<a name="security_iam_service-with-iam-roles-service"></a>

**Supports service roles:** No 

 A service role is an [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) that a service assumes to perform actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For more information, see [Create a role to delegate permissions to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html) in the *IAM User Guide*. 

**Warning**  
Changing the permissions for a service role might break VPC Lattice functionality. Edit service roles only when VPC Lattice provides guidance to do so.

## Service-linked roles for VPC Lattice
<a name="security_iam_service-with-iam-roles-service-linked"></a>

**Supports service-linked roles:** Yes

 A service-linked role is a type of service role that is linked to an AWS service. The service can assume the role to perform an action on your behalf. Service-linked roles appear in your AWS account and are owned by the service. An IAM administrator can view, but not edit the permissions for service-linked roles. 

For information about creating or managing VPC Lattice service-linked roles, see [Using service-linked roles for Amazon VPC Lattice](using-service-linked-roles.md).