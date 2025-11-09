# How Amazon VPC Lattice works with IAM

Before you use IAM to manage access to VPC Lattice, learn what IAM features are
available to use with VPC Lattice.

| IAM feature                                                                                                                                              | VPC Lattice support |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| [Identity-based policies](#security_iam_service-with-iam-id-based-policies "#security_iam_service-with-iam-id-based-policies")                           | Yes                 |
| [Resource-based policies](#security_iam_service-with-iam-resource-based-policies "#security_iam_service-with-iam-resource-based-policies")               | Yes                 |
| [Policy actions](#security_iam_service-with-iam-id-based-policies-actions "#security_iam_service-with-iam-id-based-policies-actions")                    | Yes                 |
| [Policy resources](#security_iam_service-with-iam-id-based-policies-resources "#security_iam_service-with-iam-id-based-policies-resources")              | Yes                 |
| [Policy condition keys](#security_iam_service-with-iam-id-based-policies-conditionkeys "#security_iam_service-with-iam-id-based-policies-conditionkeys") | Yes                 |
| [ACLs](#security_iam_service-with-iam-acls "#security_iam_service-with-iam-acls")                                                                        | No                  |
| [ABAC (tags in<br>policies)](#security_iam_service-with-iam-tags "#security_iam_service-with-iam-tags")                                                  | Yes                 |
| [Temporary<br>credentials](#security_iam_service-with-iam-roles-tempcreds "#security_iam_service-with-iam-roles-tempcreds")                              | Yes                 |
| [Service<br>roles](#security_iam_service-with-iam-roles-service "#security_iam_service-with-iam-roles-service")                                          | No                  |
| [Service-linked roles](#security_iam_service-with-iam-roles-service-linked "#security_iam_service-with-iam-roles-service-linked")                        | Yes                 |

For a high-level view of how VPC Lattice and other AWS services work with most IAM
features, see [AWS
services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

## Identity-based policies

for VPC Lattice

**Supports identity-based policies:**

Yes

Identity-based policies are JSON permissions policy documents that you can attach to an identity, such as an IAM user, group of users, or role. These
policies control what actions users and roles can perform, on which resources, and under what conditions. To learn how to create an identity-based
policy, see [Define custom IAM permissions with customer managed policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the
_IAM User Guide_.

With IAM identity-based policies, you can specify allowed or denied actions and
resources as well as the conditions under which actions are allowed or denied. To learn about all of the elements that you can use in a
JSON policy, see [IAM JSON
policy elements reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the
_IAM User Guide_.

## Resource-based

policies within VPC Lattice

**Supports resource-based policies:**

Yes

Resource-based policies are JSON policy documents that you attach to a resource in
AWS. In AWS services that support resource-based policies, service administrators can
use them to control access to a specific resource of that AWS service. For the resource where the policy is
attached, the policy defines what actions a specified principal can perform on that
resource and under what conditions. You must specify a principal in a resource-based
policy.

VPC Lattice supports _auth policies_, a resource-based
policy that lets you control access to services in your service network. For more
information, see [Control access to VPC Lattice services using auth policies](auth-policies.md "auth-policies.md").

VPC Lattice also supports resource-based permissions policies for integration with
AWS Resource Access Manager. You can use these resource-based policies to grant permission to manage connectivity to other
AWS accounts or organizations for services, resource configurations, and service networks. For more information, see [Share your VPC Lattice entities](sharing.md "sharing.md").

## Policy actions

for VPC Lattice

**Supports policy actions:**

Yes

In an IAM policy statement, you can specify any API action from any service that
supports IAM. For VPC Lattice, use the following prefix with the name of the API action:
`vpc-lattice:`. For example: `vpc-lattice:CreateService`,
`vpc-lattice:CreateTargetGroup`, and
`vpc-lattice:PutAuthPolicy`.

To specify multiple actions in a single statement, separate them with commas, as
follows:

```
"Action": [ "vpc-lattice:`action1`", "vpc-lattice:`action2`" ]
```

You can also specify multiple actions using wildcards. For example, you can specify all
actions whose names begin with the word `Get`, as follows:

```
"Action": "vpc-lattice:Get*"
```

For a complete list of VPC Lattice API actions, see [Actions defined by Amazon VPC Lattice](../../../service-authorization/latest/reference/list_amazonvpclattice.md#amazonvpclattice-actions-as-permissions "../../../service-authorization/latest/reference/list_amazonvpclattice.md#amazonvpclattice-actions-as-permissions") in the
_Service Authorization Reference_.

## Policy

resources for VPC Lattice

**Supports policy resources:**

Yes

In an IAM policy statement, the `Resource` element specifies the object or
objects that the statement covers. For VPC Lattice, each IAM policy statement applies to the
resources that you specify using their ARNs.

The specific Amazon Resource Name (ARN) format depends on the resource. When you provide
an ARN, replace the `italicized` text with your resource-specific
information.

- **Access log subscriptions:**

```
"Resource": "arn:aws:vpc-lattice:`region`:`account-id`:accesslogsubscription/`access-log-subscription-id`"
```

- **Listeners:**

```
"Resource": "arn:aws:vpc-lattice:`region`:`account-id`:service/`service-id`/listener/`listener-id`"
```

- **Resource gateways**

```
"Resource": "arn:aws:vpc-lattice:`region`:`account-id`:resourcegateway/`resource-gateway-id`"
```

- **Resource configuration**

```
"Resource": "arn:aws:vpc-lattice:`region`:`account-id`:resourceconfiguration/`resource-configuration-id`"
```

- **Rules:**

```
"Resource": "arn:aws:vpc-lattice:`region`:`account-id`:service/`service-id`/listener/`listener-id`/rule/`rule-id`"
```

- **Services:**

```
"Resource": "arn:aws:vpc-lattice:`region`:`account-id`:service/`service-id`"
```

- **Service networks:**

```
"Resource": "arn:aws:vpc-lattice:`region`:`account-id`:servicenetwork/`service-network-id`"
```

- **Service network service associations:**

```
"Resource": "arn:aws:vpc-lattice:`region`:`account-id`:servicenetworkserviceassociation/`service-network-service-association-id`"
```

- **Service network resource configuration associations**

```
"Resource": "arn:aws:vpc-lattice:`region`:`account-id`:servicenetworkresourceassociation/`service-network-resource-association-id`"
```

- **Service network VPC associations:**

```
"Resource": "arn:aws:vpc-lattice:`region`:`account-id`:servicenetworkvpcassociation/`service-network-vpc-association-id`"
```

- **Target groups:**

```
"Resource": "arn:aws:vpc-lattice:`region`:`account-id`:targetgroup/`target-group-id`"
```

## Policy

condition keys for VPC Lattice

**Supports service-specific policy condition keys:**

Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition
operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the condition in the
policy with values in the request. To see all AWS global
condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

To see a list of the VPC Lattice condition keys, see [Condition keys for Amazon VPC Lattice](../../../service-authorization/latest/reference/list_amazonvpclattice.md#amazonvpclattice-policy-keys "../../../service-authorization/latest/reference/list_amazonvpclattice.md#amazonvpclattice-policy-keys") in the
_Service Authorization Reference_.

AWS supports global condition keys and service-specific condition keys. For
information about AWS global condition keys, see [AWS global condition
context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the _IAM User Guide_.

## Access control lists (ACLs) in

VPC Lattice

**Supports ACLs:**

No

Access control lists (ACLs) control which principals (account members, users, or roles) have permissions to access a resource. ACLs are
similar to resource-based policies, although they do not use the JSON policy document format.

## Attribute-based access control (ABAC)

with VPC Lattice

**Supports ABAC (tags in policies):**

Yes

Attribute-based access control (ABAC) is an authorization strategy that defines permissions
based on attributes called tags. You can attach tags to IAM entities and AWS resources, then design ABAC policies to allow operations when the principal's tag matches the tag on the resource.

To control access based on tags, you provide tag information in the [condition element](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") of a policy using the `aws:ResourceTag/`key-name``, 
 `aws:RequestTag/`key-name``, or `aws:TagKeys` condition keys.

If a service supports all three condition keys for every resource type, then the value is **Yes** for the service. If a service supports all three condition keys for only some resource types, then the value is **Partial**.

For more information about ABAC, see [Define permissions with ABAC authorization](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in the _IAM User Guide_. To view a tutorial with steps for setting up ABAC, see
[Use attribute-based access control (ABAC)](../../../IAM/latest/UserGuide/tutorial_attribute-based-access-control.md "../../../IAM/latest/UserGuide/tutorial_attribute-based-access-control.md") in the _IAM User Guide_.

## Using temporary credentials

with VPC Lattice

**Supports temporary credentials:**

Yes

Temporary credentials provide short-term access to AWS resources and are automatically created when you use federation or switch roles. AWS recommends that you
dynamically generate temporary credentials instead of using long-term access keys. For
more information, see [Temporary
security credentials in IAM](../../../IAM/latest/UserGuide/id_credentials_temp.md "../../../IAM/latest/UserGuide/id_credentials_temp.md") and [AWS services
that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

## Service roles for

VPC Lattice

**Supports service roles:**

No

A service role is an [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") that a service assumes to perform
actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For
more information, see [Create a role to delegate permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the _IAM User Guide_.

###### Warning

Changing the permissions for a service role might break VPC Lattice functionality. Edit
service roles only when VPC Lattice provides guidance to do so.

## Service-linked roles

for VPC Lattice

**Supports service-linked roles:**

Yes

A service-linked role is a type of service role that is linked to an AWS service. The service can assume the role to perform an action on your behalf.
Service-linked roles appear in your AWS account and are owned by the service. An IAM administrator can view,
but not edit the permissions for service-linked roles.

For information about creating or managing VPC Lattice service-linked roles, see [Using service-linked roles for Amazon VPC Lattice](using-service-linked-roles.md "using-service-linked-roles.md").
