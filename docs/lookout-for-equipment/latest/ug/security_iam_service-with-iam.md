

 On October 7, 2026, AWS will discontinue support for Amazon Lookout for Equipment. After October 7, 2026, you will no longer be able to access the Lookout for Equipment console or resources. For more information, [see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/). 

# AWS Identity and Access Management for Amazon Lookout for Equipment
<a name="security_iam_service-with-iam"></a>

Before you use IAM to manage access to Amazon Lookout for Equipment, learn what IAM features are available to use with Amazon Lookout for Equipment.

To get a high-level view of how Lookout for Equipment and other AWS services work with most IAM features, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

## Lookout for Equipment identity-based policies
<a name="security_iam_service-with-iam-id-based-policies"></a>

Identity-based policies are JSON permissions policy documents that you can attach to an identity, such as an IAM user, group of users, or role. These policies control what actions users and roles can perform, on which resources, and under what conditions. To learn how to create an identity-based policy, see [Define custom IAM permissions with customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) in the *IAM User Guide*.

With IAM identity-based policies, you can specify allowed or denied actions and resources as well as the conditions under which actions are allowed or denied. To learn about all of the elements that you can use in a JSON policy, see [IAM JSON policy elements reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html) in the *IAM User Guide*.

## Actions
<a name="security_iam_service-with-iam-id-based-policies-actions"></a>

Administrators can use Amazon Web Services JSON policies to specify who has access to what. That is, which *principal* can perform *actions* on what *resources*, and under what *conditions*. 

The `Action` element of a JSON policy describes the actions that you can use to allow or deny access in a policy. Policy actions usually have the same name as the associated AWS API operation. There are some exceptions, such as *permission-only actions* that don't have a matching API operation. There are also some operations that require multiple actions in a policy. These additional actions are called *dependent actions*. 

Include actions in a policy to grant permissions to perform the associated operation.

Policy actions in Lookout for Equipment use the following prefix before the action: `lookoutequipment:`. For example, to grant someone permission to list Lookout for Equipment datasets with the `ListDatasets` API operation, you include the `lookoutequipment:ListDatasets` action in their policy. Policy statements must include either an `Action` or `NotAction` element. Lookout for Equipment defines its own set of actions that describe tasks that you can perform with this service. 

To specify multiple actions in a single statement, separate them with commas as follows.

```
"Action": [
      "lookoutequipment:{{action1}}",
      "lookoutequipment:{{action2}}"
         ]
```

You can specify multiple actions using wildcards (\*). For example, to specify all actions that begin with the word `Describe`, include the following action.

```
"Action": "lookoutequipment:Describe*"
```

## Resources
<a name="security_iam_service-with-iam-id-based-policies-resources"></a>

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

The Lookout for Equipment dataset resource has the following Amazon Resource Name (ARN).

```
arn:${Partition}:lookoutequipment:${Region}:${Account}:dataset/${datasetName}/${GUID}
```

For example, to specify a dataset in your statement, use the full ARN: 

```
"Resource": "arn:aws:lookoutequipment:${Region}:${Account}:dataset/${datasetName}/${GUID}"
```

Some Lookout for Equipment actions, such as those for creating resources, cannot be performed on a specific resource. In those cases, you must use the wildcard (\*). 

```
"Resource": "*"
```

To see a list of Lookout for Equipment resource types and their ARNs, see [Resources Defined by Amazon Lookout for Equipment](https://docs.aws.amazon.com/service-authorization/latest/reference/reference.html) in the *Service Authorization Reference*. To learn with which actions you can specify the ARN of each resource, see [Actions defined by Amazon Lookout for Equipment](https://docs.aws.amazon.com/service-authorization/latest/reference/reference.html). For more information about the format of ARNs, see [Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html). 

## Condition keys
<a name="security_iam_service-with-iam-id-based-policies-conditionkeys"></a>

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html), such as equals or less than, to match the condition in the policy with values in the request. To see all AWS global condition keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

To view examples of Amazon Lookout for Equipment identity-based policies, see [Identity-based policy examples for Amazon Lookout for Equipment](security_iam_id-based-policy-examples.md).

## Access control lists (ACLs) in Lookout for Equipment
<a name="security_iam_service-with-iam-acls"></a>

Access control lists (ACLs) control which principals (account members, users, or roles) have permissions to access a resource. ACLs are similar to resource-based policies, although they do not use the JSON policy document format.

Access control lists (ACLs) are lists of grantees that you can attach to resources. They grant accounts permissions to access the resource to which they are attached. You can attach ACLs to an Amazon S3 {{bucket}} resource. 

With Amazon S3 access control lists (ACLs), you can manage access to {{bucket}} resources. Each {{bucket}} has an ACL attached to it as a subresource. It defines which AWS accounts, IAM users or groups of users, or IAM roles are granted access and the type of access. When a request is received for a resource, AWS checks the corresponding ACL to verify that the requester has the necessary access permissions.

When you create a {{bucket}} resource, Amazon S3 creates a default ACL that grants the resource owner full control over the resource. In the following example {{bucket}} ACL, John Doe is listed as the owner of the {{bucket}} and is granted full control over that {{bucket}}. An ACL can have up to 100 grantees.

```
<?xml version="1.0" encoding="UTF-8"?>
<AccessControlPolicy xmlns="http://lookoutequipment.amazonaws.com/doc/2006-03-01/">
  <Owner>
    <ID>{{c1daexampleaaf850ea79cf0430f33d72579fd1611c97f7ded193374c0b163b6}}</ID>
    <DisplayName>{{john-doe}}</DisplayName>
  </Owner>
  <AccessControlList>
    <Grant>
      <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
               xsi:type="Canonical User">
        <ID>{{c1daexampleaaf850ea79cf0430f33d72579fd1611c97f7ded193374c0b163b6}}</ID>
        <DisplayName>{{john-doe}}</DisplayName>
      </Grantee>
      <Permission>FULL_CONTROL</Permission>
    </Grant>
  </AccessControlList>
</AccessControlPolicy>
```

The ID field in the ACL is the AWS account canonical user ID. To learn how to view this ID in an account that you own, see [Finding an AWS account canonical user ID](https://docs.aws.amazon.com/general/latest/gr/acct-identifiers.html#FindingCanonicalId). 

## Attribute-based access control (ABAC) with Lookout for Equipment
<a name="security_iam_service-with-iam-tags"></a>

Attribute-based access control (ABAC) is an authorization strategy that defines permissions based on attributes called tags. You can attach tags to IAM entities and AWS resources, then design ABAC policies to allow operations when the principal's tag matches the tag on the resource.

To control access based on tags, you provide tag information in the [condition element](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) of a policy using the `aws:ResourceTag/{{key-name}}`, `aws:RequestTag/{{key-name}}`, or `aws:TagKeys` condition keys.

If a service supports all three condition keys for every resource type, then the value is **Yes** for the service. If a service supports all three condition keys for only some resource types, then the value is **Partial**.

For more information about ABAC, see [Define permissions with ABAC authorization](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*. To view a tutorial with steps for setting up ABAC, see [Use attribute-based access control (ABAC)](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html) in the *IAM User Guide*.

## Using Temporary credentials with Lookout for Equipment
<a name="security_iam_service-with-iam-roles-tempcreds"></a>

Temporary credentials provide short-term access to AWS resources and are automatically created when you use federation or switch roles. AWS recommends that you dynamically generate temporary credentials instead of using long-term access keys. For more information, see [Temporary security credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) and [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

## Cross-service principal permissions for Lookout for Equipment
<a name="security_iam_service-with-iam-principal-permissions"></a>

 Forward access sessions (FAS) use the permissions of the principal calling an AWS service, combined with the requesting AWS service to make requests to downstream services. For policy details when making FAS requests, see [Forward access sessions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_forward_access_sessions.html). 

## Service roles for Lookout for Equipment
<a name="security_iam_service-with-iam-roles-service"></a>

 A service role is an [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) that a service assumes to perform actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For more information, see [Create a role to delegate permissions to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html) in the *IAM User Guide*. 

**Warning**  
Changing the permissions for a service role might break Lookout for Equipment functionality. Edit service roles only when Lookout for Equipment provides guidance to do so.

### Choosing an IAM role in Lookout for Equipment
<a name="security_iam_service-with-iam-roles-choose"></a>

When you create a resource in Lookout for Equipment, you must choose a role to allow Lookout for Equipment to access Amazon S3 on your behalf. If you have previously created a service role or service-linked role, then Lookout for Equipment provides you with a list of roles to choose from. It's important to choose a role that allows access to read and write to your Amazon S3 bucket. instances