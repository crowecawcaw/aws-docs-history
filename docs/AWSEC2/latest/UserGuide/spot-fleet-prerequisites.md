# Spot Fleet permissions

If your users will create or manage a Spot Fleet, you need to grant them the required
permissions.

If you use the Amazon EC2 console to create a Spot Fleet, it creates two service-linked roles
named `AWSServiceRoleForEC2SpotFleet` and
`AWSServiceRoleForEC2Spot`, and a role named
`aws-ec2-spot-fleet-tagging-role` that grant the Spot Fleet the permissions to
request, launch, terminate, and tag resources on your behalf. If you use the AWS CLI or an
API, you must ensure that these roles exist.

Use the following instructions to grant the required permissions and create the
roles.

###### Permissions and roles

- [Grant permission to users for Spot Fleet](#spot-fleet-iam-users "#spot-fleet-iam-users")
- [Service-linked role for
  Spot Fleet](#service-linked-roles-spot-fleet-requests "#service-linked-roles-spot-fleet-requests")
- [Service-linked role for
  Spot Instances](#service-linked-roles-spot-instances "#service-linked-roles-spot-instances")
- [IAM role for tagging a
  Spot Fleet](#spot-fleet-service-linked-role "#spot-fleet-service-linked-role")

## Grant permission to users for Spot Fleet

If your users will create or manage a Spot Fleet, be sure to grant them the required
permissions.

###### To create a policy for Spot Fleet

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Policies**,
   **Create policy**.
3. On the **Create policy** page, choose
   **JSON**, and replace the text with the
   following.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:RunInstances",
 "ec2:CreateTags",
 "ec2:RequestSpotFleet",
 "ec2:ModifySpotFleetRequest",
 "ec2:CancelSpotFleetRequests",
 "ec2:DescribeSpotFleetRequests",
 "ec2:DescribeSpotFleetInstances",
 "ec2:DescribeSpotFleetRequestHistory"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "arn:aws:iam::*:role/aws-ec2-spot-fleet-tagging-role"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:CreateServiceLinkedRole",
 "iam:ListRoles",
 "iam:ListInstanceProfiles"
 ],
 "Resource": "*"
 }
 ]
}`

```

The preceding example policy grants a user the permissions required for
most Spot Fleet use cases. To limit the user to specific API actions, specify only
those API actions instead.

**Required EC2 and IAM APIs**

The following APIs must be included in the policy:

    * `ec2:RunInstances` – Required to launch instances
     in a Spot Fleet
    * `ec2:CreateTags` – Required to tag the Spot Fleet
     request, instances, or volumes
    * `iam:PassRole` – Required to specify the Spot Fleet
     role
    * `iam:CreateServiceLinkedRole` – Required to
     create the service-linked role
    * `iam:ListRoles` – Required to enumerate existing
     IAM roles
    * `iam:ListInstanceProfiles` – Required to
     enumerate existing instance profiles

###### Important

If you specify a role for the IAM instance profile in the launch
specification or launch template, you must grant the user the permission
to pass the role to the service. To do this, in the IAM policy include
`"arn:aws:iam::*:role/`IamInstanceProfile-role`"`
as a resource for the `iam:PassRole` action. For more
information, see [Granting a
user permissions to pass a role to an AWS service](../../../IAM/latest/UserGuide/id_roles_use_passrole.md "../../../IAM/latest/UserGuide/id_roles_use_passrole.md") in the
_IAM User Guide_.

**Spot Fleet APIs**

Add the following Spot Fleet API actions to your policy, as needed:

    * `ec2:RequestSpotFleet`
    * `ec2:ModifySpotFleetRequest`
    * `ec2:CancelSpotFleetRequests`
    * `ec2:DescribeSpotFleetRequests`
    * `ec2:DescribeSpotFleetInstances`
    * `ec2:DescribeSpotFleetRequestHistory`

**Optional IAM APIs**

(Optional) To enable a user to create roles or instance profiles using the
IAM console, you must add the following actions to the policy:

    * `iam:AddRoleToInstanceProfile`
    * `iam:AttachRolePolicy`
    * `iam:CreateInstanceProfile`
    * `iam:CreateRole`
    * `iam:GetRole`
    * `iam:ListPolicies`

4. Choose **Review policy**.
5. On the **Review policy** page, enter a policy name and
   description, and choose **Create policy**.
6. To provide access, add permissions to your users, groups, or roles:
   - Users and groups in AWS IAM Identity Center:

   Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_.
   - Users managed in IAM through an identity provider:

   Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
   in the _IAM User Guide_.
   - IAM users:
     - Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_.
     - (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the _IAM User Guide_.

## Service-linked role for

Spot Fleet

Amazon EC2 uses service-linked roles for the permissions that it requires to call other
AWS services on your behalf. A service-linked role is a unique type of IAM role
that is linked directly to an AWS service. Service-linked roles provide a secure
way to delegate permissions to AWS services because only the linked service can
assume a service-linked role. For more information, see [Service-linked
roles](../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md "../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md") in the _IAM User Guide_.

Amazon EC2 uses the service-linked role named
**AWSServiceRoleForEC2SpotFleet** to launch and manage
instances on your behalf.

###### Important

If you specify an [encrypted AMI](AMIEncryption.md "AMIEncryption.md") or an
encrypted Amazon EBS snapshot in your Spot Fleet, you must grant the **AWSServiceRoleForEC2SpotFleet** role permission to use the CMK so
that Amazon EC2 can launch instances on your behalf. For more information, see [Grant access to
CMKs for use with encrypted AMIs and EBS snapshots](#spot-fleet-service-linked-roles-access-to-cmks "#spot-fleet-service-linked-roles-access-to-cmks").

### Permissions granted by AWSServiceRoleForEC2SpotFleet

The **AWSServiceRoleForEC2SpotFleet** role grants the Spot Fleet
permission to request, launch, terminate, and tag instances on your behalf.
Amazon EC2 uses this service-linked role to complete the following actions:

- `ec2:RequestSpotInstances` - Request Spot Instances
- `ec2:RunInstances` - Launch instances
- `ec2:TerminateInstances` - Terminate instances
- `ec2:DescribeImages` - Describe Amazon Machine Images
  (AMIs) for the instances
- `ec2:DescribeInstanceStatus` - Describe the status of the
  instances
- `ec2:DescribeSubnets` - Describe the subnets for the
  instances
- `ec2:CreateTags` - Add tags to the Spot Fleet request, instances,
  and volumes
- `elasticloadbalancing:RegisterInstancesWithLoadBalancer` -
  Add the specified instances to the specified load balancer
- `elasticloadbalancing:RegisterTargets` - Register the
  specified targets with the specified target group

### Create the

service-linked role

Under most circumstances, you don't need to manually create a service-linked
role. Amazon EC2 creates the **AWSServiceRoleForEC2SpotFleet**
service-linked role the first time you create a Spot Fleet using the console.

If you had an active Spot Fleet request before October 2017, when Amazon EC2 began
supporting this service-linked role, Amazon EC2 created the
**AWSServiceRoleForEC2SpotFleet** role in your AWS
account. For more information, see [A new role appeared in my AWS account](../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared "../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared") in the
_IAM User Guide_.

If you use the AWS CLI or an API to create a Spot Fleet, you must first ensure that
this role exists.

###### To create the AWSServiceRoleForEC2SpotFleet role for Spot Fleet using the

console

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles**.
3. Choose **Create role**.
4. On the **Select trusted entity** page, do the
   following:
   1. For **Trusted entity type**, choose
      **AWS service**.
   2. Under **Use case**, for **Service or
      use case**, choose **EC2**.
   3. For **Use case**, choose **EC2 - Spot
      Fleet**.

   ###### Note

   The **EC2 - Spot Fleet** use case will
   automatically create a policy with the required IAM
   permissions and will suggest
   **AWSEC2SpotFleetServiceRolePolicy** as
   the role name. 4. Choose **Next**.

5. On the **Add permissions** page, choose
   **Next**.
6. On the **Name, review, and create** page, choose
   **Create role**.

###### To create the AWSServiceRoleForEC2SpotFleet role for Spot Fleet using the

AWS CLI

Use the [create-service-linked-role](../../../cli/latest/reference/iam/create-service-linked-role.md "../../../cli/latest/reference/iam/create-service-linked-role.md") command as follows.

```
aws iam create-service-linked-role --aws-service-name spotfleet.amazonaws.com
```

If you no longer need to use Spot Fleet, we recommend that you delete the
**AWSServiceRoleForEC2SpotFleet** role. After this role is
deleted from your account, Amazon EC2 will create the role again if you request a
Spot Fleet using the console. For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/id_roles_manage_delete.md#id_roles_manage_delete_slr "../../../IAM/latest/UserGuide/id_roles_manage_delete.md#id_roles_manage_delete_slr") in the
_IAM User Guide_.

### Grant access to

CMKs for use with encrypted AMIs and EBS snapshots

If you specify an [encrypted AMI](AMIEncryption.md "AMIEncryption.md") or an
encrypted Amazon EBS snapshot in your Spot Fleet request and you use a customer managed key for
encryption, you must grant the
**AWSServiceRoleForEC2SpotFleet** role permission to use
the CMK so that Amazon EC2 can launch instances on your behalf. To do this, you must
add a grant to the CMK, as shown in the following procedure.

When providing permissions, grants are an alternative to key policies. For
more information, see [Using Grants](../../../kms/latest/developerguide/grants.md "../../../kms/latest/developerguide/grants.md")
and [Using Key Policies in
AWS KMS](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md") in the _AWS Key Management Service Developer Guide_.

###### To grant the AWSServiceRoleForEC2SpotFleet role permissions to use the

CMK

- Use the [create-grant](../../../cli/latest/reference/kms/create-grant.md "../../../cli/latest/reference/kms/create-grant.md") command to add a grant to the CMK and to
  specify the principal (the
  **AWSServiceRoleForEC2SpotFleet** service-linked
  role) that is given permission to perform the operations that the grant
  permits. The CMK is specified by the `key-id` parameter and
  the ARN of the CMK. The principal is specified by the
  `grantee-principal` parameter and the ARN of the
  **AWSServiceRoleForEC2SpotFleet** service-linked
  role.

```
aws kms create-grant \
    --region `us-east-1` \
    --key-id arn:aws:kms:`us-east-1`:`444455556666`:key/`1234abcd-12ab-34cd-56ef-1234567890ab` \
    --grantee-principal arn:aws:iam::`111122223333`:role/aws-service-role/spotfleet.amazonaws.com/AWSServiceRoleForEC2SpotFleet \
    --operations "Decrypt" "Encrypt" "GenerateDataKey" "GenerateDataKeyWithoutPlaintext" "CreateGrant" "DescribeKey" "ReEncryptFrom" "ReEncryptTo"
```

## Service-linked role for

Spot Instances

Amazon EC2 uses the service-linked role named **AWSServiceRoleForEC2Spot** to launch and manage Spot Instances on your behalf.
For more information, see [Service-linked role for Spot Instance requests](service-linked-roles-spot-instance-requests.md "service-linked-roles-spot-instance-requests.md").

## IAM role for tagging a

Spot Fleet

The `aws-ec2-spot-fleet-tagging-role` IAM role grants the Spot Fleet
permission to tag the Spot Fleet request, instances, and volumes. For more information,
see [Tag a new or existing Spot Fleet request and the instances
and volumes it launches](tag-spot-fleet.md "tag-spot-fleet.md").

###### Important

If you choose to tag instances in the fleet and you also choose to maintain
target capacity (the Spot Fleet request is of type `maintain`), the
differences in the permissions that are set for the user and the
`IamFleetRole` might lead to inconsistent tagging behavior of
instances in the fleet. If the `IamFleetRole` does not include the
`CreateTags` permission, some of the instances launched by the
fleet might not be tagged. While we are working to fix this inconsistency, to
ensure that all instances launched by the fleet are tagged, we recommend that
you use the `aws-ec2-spot-fleet-tagging-role` role for the
`IamFleetRole`. Alternatively, to use an existing role, attach
the `AmazonEC2SpotFleetTaggingRole` AWS Managed Policy to the
existing role. Otherwise, you need to manually add the `CreateTags`
permission to your existing policy.

###### To create the IAM role for tagging a Spot Fleet

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles**.
3. Choose **Create role**.
4. On the **Select trusted entity** page, under
   **Trusted entity type**, choose **AWS
   service**.
5. Under **Use case**, from **Use cases for other
   AWS services**, choose **EC2**, and then
   choose **EC2 - Spot Fleet Tagging**.
6. Choose **Next**.
7. On the **Add permissions** page, choose
   **Next**.
8. On the **Name, review, and create** page, for
   **Role name**, enter a name for the role (for example,
   `aws-ec2-spot-fleet-tagging-role`).
9. Review the information on the page, and then choose **Create
   role**.

### Cross-service

confused deputy prevention

The [confused deputy
problem](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md") is a security issue where an entity that doesn't have
permission to perform an action can coerce a more-privileged entity to perform
the action. We recommend that you use the [`aws:SourceArn`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") and [`aws:SourceAccount`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") global condition context keys in
the `aws-ec2-spot-fleet-tagging-role` trust policy to limit the
permissions that Spot Fleet gives another service to the resource.

###### To add the aws:SourceArn and aws:SourceAccount condition keys to the

`aws-ec2-spot-fleet-tagging-role` trust policy

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles**.
3. Find the `aws-ec2-spot-fleet-tagging-role` that you created
   previously and choose the link (not the checkbox).
4. Under **Summary**, choose the **Trust
   relationships** tab, and then choose **Edit trust
   policy**.
5. In the JSON statement, add a `Condition` element containing
   your `aws:SourceAccount` and `aws:SourceArn`
   global condition context keys to prevent the [confused deputy
   problem](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md"), as follows:

```
"Condition": {
      "ArnLike": {
        "aws:SourceArn": "arn:aws:ec2:us-east-1:`111122223333`:spot-fleet-request/sfr-*"
      },
      "StringEquals": {
        "aws:SourceAccount": "`111122223333`"
      }
```

###### Note

If the `aws:SourceArn` value contains the account ID
and you use both global condition context keys, the
`aws:SourceAccount` value and the account in the
`aws:SourceArn` value must use the same account ID
when used in the same policy statement.

The final trust policy will be as follows:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Sid": "ConfusedDeputyPreventionExamplePolicy",
 "Effect": "Allow",
 "Principal": {
 "Service": "spotfleet.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "ArnLike": {
 "aws:SourceArn": "arn:aws:ec2:`us-east-1`:`111122223333`:spot-fleet-request/sfr-*"
 },
 "StringEquals": {
 "aws:SourceAccount": "`111122223333`"
 }
 }
 }
}`

```

6. Choose **Update policy**.

The following table provides potential values for `aws:SourceArn`
to limit the scope of the your `aws-ec2-spot-fleet-tagging-role` in
varying degrees of specificity.

| API operation    | Called service         | Scope                                                                                                                                                                                                                                                                                                      | `aws:SourceArn`                                                                                        |
| ---------------- | ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| RequestSpotFleet | AWS STS (`AssumeRole`) | Limit the `AssumeRole` capability on `aws-ec2-spot-fleet-tagging-role` to spot-fleet-requests in the specified account.                                                                                                                                                                                    | `arn:aws:ec2:*:`123456789012`:spot-fleet-request/sfr-*`                                                |
| RequestSpotFleet | AWS STS (`AssumeRole`) | Limit the `AssumeRole` capability on `aws-ec2-spot-fleet-tagging-role` to spot-fleet-requests in the specified account and specified Region. Note that this role will not be usable in other Regions.                                                                                                      | `arn:aws:ec2:`us-east-1`:`123456789012`:spot-fleet-request/sfr-*`                                      |
| RequestSpotFleet | AWS STS (`AssumeRole`) | Limit the `AssumeRole` capability on `aws-ec2-spot-fleet-tagging-role` to only actions affecting the fleet sfr-11111111-1111-1111-1111-111111111111. Note that this role may not be usable for other Spot Fleets. Also, this role cannot be used to launch any new Spot Fleets through request-spot-fleet. | `arn:aws:ec2:`us-east-1`:`123456789012`:spot-fleet-request/sfr-`11111111-1111-1111-1111-111111111111`` |
