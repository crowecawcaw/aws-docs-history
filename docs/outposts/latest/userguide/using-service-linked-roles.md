# Service-linked roles for AWS Outposts

AWS Outposts uses AWS Identity and Access Management (IAM) service-linked roles. A service-linked role is a type of
service role that is linked directly to AWS Outposts. AWS Outposts defines service-linked roles and includes
all the permissions that it requires to call other AWS services on your behalf.

A service-linked role makes setting up your AWS Outposts more efficient because you don’t have to
manually add the necessary permissions. AWS Outposts defines the permissions of its service-linked
roles, and unless defined otherwise, only AWS Outposts can assume its roles. The defined permissions
include the trust policy and the permissions policy, and that permissions policy can't be
attached to any other IAM entity.

You can delete a service-linked role only after first deleting the related resources. This
protects your AWS Outposts resources because you can't inadvertently remove permission to access the
resources.

## Service-linked role permissions for AWS Outposts

AWS Outposts uses the service-linked role named **AWSServiceRoleForOutposts\_`OutpostID`**. This role grants
Outposts permissions to manage networking resources to enable private connectivity on your
behalf. This role also allows Outposts to create and configure network interfaces, manage
security groups, and attach interfaces to service link endpoint instances. These permissions
are necessary for establishing and maintaining the secure, private connection between your
on-premises Outpost and AWS services, ensuring reliable operation of your Outpost
deployment.

The AWSServiceRoleForOutposts\_`OutpostID` service-linked role trusts the following services to assume the
role:

- `outposts.amazonaws.com`

### Service-linked role policies

The AWSServiceRoleForOutposts\_`OutpostID` service-linked role includes the following policies:

- [AWSOutpostsServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSOutpostsServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSOutpostsServiceRolePolicy.md")
- AWSOutpostsPrivateConnectivityPolicy\_`OutpostID`

#### AWSOutpostsServiceRolePolicy

The `AWSOutpostsServiceRolePolicy` policy enables access to AWS resources
managed by AWS Outposts.

This policy allows AWS Outposts to complete the following actions on the specified
resources:

- Action: `ec2:DescribeNetworkInterfaces` on all AWS resources
- Action: `ec2:DescribeSecurityGroups` on all AWS resources
- Action: `ec2:DescribeSubnets` on all AWS resources
- Action: `ec2:DescribeVpcEndpoints` on all AWS resources
- Action: `ec2:CreateNetworkInterface` on the following AWS resources:

```
"arn:*:ec2:*:*:vpc/*",
"arn:*:ec2:*:*:subnet/*",
"arn:*:ec2:*:*:security-group/*"
```

- Action: `ec2:CreateNetworkInterface` on the AWS resource `"arn:*:ec2:*:*:network-interface/*"` that match the following condition:

```
"ForAnyValue:StringEquals" : { "aws:TagKeys": [ "outposts:private-connectivity-`resourceId`" ] }
```

- Action: `ec2:CreateSecurityGroup` on the following AWS resources:

```
"arn:*:ec2:*:*:vpc/*"
```

- Action: `ec2:CreateSecurityGroup` on the AWS resource `"arn:*:ec2:*:*:security-group/*"` that match the following condition:

```
"ForAnyValue:StringEquals": { "aws:TagKeys": [ "outposts:private-connectivity-`resourceId`" ] }
```

#### AWSOutpostsPrivateConnectivityPolicy_OutpostID

The
`AWSOutpostsPrivateConnectivityPolicy_`OutpostID``
policy allows AWS Outposts to complete the following actions on the specified resources:

- Action: `ec2:AuthorizeSecurityGroupIngress` on all AWS resources that match the following condition:

```
{ "StringLike" : { "ec2:ResourceTag/outposts:private-connectivity-`resourceId`" : "`OutpostID`" }} and { "StringEquals" : { "ec2:Vpc" : "`vpcArn`" }}
```

- Action: `ec2:AuthorizeSecurityGroupEgress` on all AWS resources that match the following condition:

```
{ "StringLike" : { "ec2:ResourceTag/outposts:private-connectivity-`resourceId`" : "`OutpostID`" }} and { "StringEquals" : { "ec2:Vpc" : "`vpcArn`" }}
```

- Action: `ec2:CreateNetworkInterfacePermission` on all AWS resources that match the following condition:

```
{ "StringLike" : { "ec2:ResourceTag/outposts:private-connectivity-`resourceId`" : "`OutpostID`" }} and { "StringEquals" : { "ec2:Vpc" : "`vpcArn`" }}
```

- Action: `ec2:CreateTags` on all AWS resources that match the following condition:

```
{ "StringLike" : { "aws:RequestTag/outposts:private-connectivity-`resourceId`" : "{{`OutpostId`}}*"}},
"StringEquals": {"ec2:CreateAction" : ["CreateSecurityGroup", "CreateNetworkInterface"]}
```

- Action: `ec2:RevokeSecurityGroupIngress` on all AWS resources that match the following condition:

```
{ "StringLike" : { "ec2:ResourceTag/outposts:private-connectivity-`resourceId`" : "`OutpostID`" }} and { "StringEquals" : { "ec2:Vpc" : "`vpcArn`" }}
```

- Action: `ec2:RevokeSecurityGroupEgress` on all AWS resources that match the following condition:

```
{ "StringLike" : { "ec2:ResourceTag/outposts:private-connectivity-`resourceId`" : "`OutpostID`" }} and { "StringEquals" : { "ec2:Vpc" : "`vpcArn`" }}
```

- Action: `ec2:DeleteNetworkInterface` on all AWS resources that match the following condition:

```
{ "StringLike" : { "ec2:ResourceTag/outposts:private-connectivity-`resourceId`" : "`OutpostID`" }} and { "StringEquals" : { "ec2:Vpc" : "`vpcArn`" }}
```

- Action: `ec2:DeleteSecurityGroup` on all AWS resources that match the following condition:

```
{ "StringLike" : { "ec2:ResourceTag/outposts:private-connectivity-`resourceId`" : "`OutpostID`" }} and { "StringEquals" : { "ec2:Vpc" : "`vpcArn`" }}
```

You must configure permissions to allow an IAM entity (such as a user, group, or role)
to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Create a service-linked role for AWS Outposts

You don't need to manually create a service-linked role. When you
configure private connectivity for your Outpost in the AWS Management Console, AWS Outposts creates the service-linked role for
you.

For more information, see [Service link private connectivity options](private-connectivity.md "private-connectivity.md").

## Edit a service-linked role for AWS Outposts

AWS Outposts does not allow you to edit the AWSServiceRoleForOutposts\_`OutpostID` service-linked role. After you create a
service-linked role, you can't change the name of the role because various entities might
reference the role. However, you can edit the description of the role using IAM. For more
information, see [Update a service-linked
role](../../../IAM/latest/UserGuide/id_roles_update-service-linked-role.md "../../../IAM/latest/UserGuide/id_roles_update-service-linked-role.md") in the _IAM User Guide_.

## Delete a service-linked role for AWS Outposts

If you no longer require a feature or service that requires a service-linked role, we
recommend that you delete that role. That way you avoid having an unused entity that is not
actively monitored or maintained. However, you must clean up the resources for your
service-linked role before you can manually delete it.

If the AWS Outposts service is using the role when you try to delete the resources, then the
deletion might fail. If that happens, wait for a few minutes and try the operation
again.

You must delete your Outpost before you can delete the AWSServiceRoleForOutposts\_`OutpostID` service-linked
role.

Before you begin, make sure that your Outpost is not being shared
using AWS Resource Access Manager (AWS RAM). For more information, see [Unsharing a shared
Outpost resource](../network-userguide/sharing-outposts.md#sharing-unshare "../network-userguide/sharing-outposts.md#sharing-unshare").

###### To delete AWS Outposts resources used by the AWSServiceRoleForOutposts\_`OutpostID`

Contact AWS Enterprise Support to delete your Outpost.

###### To manually delete the service-linked role using IAM

For more information, see [Delete a
service-linked role](../../../IAM/latest/UserGuide/id_roles_manage_delete.md#id_roles_manage_delete_slr "../../../IAM/latest/UserGuide/id_roles_manage_delete.md#id_roles_manage_delete_slr") in the _IAM User Guide_.

## Supported Regions for AWS Outposts service-linked roles

AWS Outposts supports using service-linked roles in all of the Regions where the service is
available. For more information, see the FAQs for [Outposts racks](https://aws.amazon.com/outposts/rack/faqs/ "https://aws.amazon.com/outposts/rack/faqs/").
