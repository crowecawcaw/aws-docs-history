# Service-linked role for

EC2 Fast Launch

Amazon EC2 uses service-linked roles for the permissions that it requires to call other
AWS services on your behalf. A service-linked role is a unique type of IAM role that
is linked directly to an AWS service. Service-linked roles provide a secure way to
delegate permissions to AWS services because only the linked service can assume a
service-linked role. For more information about how Amazon EC2 uses IAM roles, including
service-linked roles, see [IAM roles for Amazon EC2](iam-roles-for-amazon-ec2.md "iam-roles-for-amazon-ec2.md").

Amazon EC2 uses the service-linked role named AWSServiceRoleForEC2FastLaunch to
create and manage a set of pre-provisioned snapshots that reduce the time it takes to
launch instances from your Windows AMI.

## Permissions granted by AWSServiceRoleForEC2FastLaunch

The AWSServiceRoleForEC2FastLaunch service-linked role trusts the
following service to assume the role:

- `ec2fastlaunch.amazonaws.com`

Amazon EC2 uses the [EC2FastLaunchServiceRolePolicy](../../../aws-managed-policy/latest/reference/EC2FastLaunchServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/EC2FastLaunchServiceRolePolicy.md")
managed policy to complete the following actions:

- **AWS CloudFormation** – Allow EC2 Fast Launch
  to get a description of associated CloudFormation stacks.
- **Amazon CloudWatch** – Post metric data associated
  with EC2 Fast Launch to the Amazon EC2 namespace.
- **Amazon EC2** – Access is granted for
  EC2 Fast Launch to perform the following actions:
  - Launch instances from an Amazon EC2 Windows Server AMI with EC2 Fast Launch enabled, in order to perform
    provisioning steps. Additionally specify resource pattern that allows
    `ec2:RunInstances` for an AMI that's associated with License Manager.
  - Stop and terminate an instance that was launched by EC2 Fast Launch
    after it creates the pre-provisioned snapshot.
  - Describe image and instance type resources used to launch instances from
    an Amazon EC2 Windows Server AMI with EC2 Fast Launch enabled and create snapshots from them.
  - Describe launch template resources and launch instances from a launch
    template.
  - Describe instances, instance attributes and instance status, volumes and
    volume attributes.
  - Describe network interfaces.
  - Delete resources that EC2 Fast Launch created, including snapshots,
    launch templates, volumes and network interfaces.
  - Tag resources that EC2 Fast Launch creates to launch and pre-provision,
    Windows instances, and create snapshots for the final launch process
    to consume.

- **Amazon EventBridge** – Includes access to create
  EventBridge event rules and retrieve details about or delete rules that it created.
  EC2 Fast Launch may also get a list of target services that receive
  EC2 Fast Launch events that are forwarded based on event rules, and add target
  services to or remove them from event rules that it created.
- **IAM** – Allows EC2 Fast Launch
  to create the `EC2FastLaunchServiceRolePolicy`
  service-linked role, to get and use instance profiles whose name contains
  `ec2fastlaunch`, and to launch instances on your behalf using the
  instance profile from your launch template.
- **AWS KMS** – Includes access to
  create grants and list grants that were created by EC2 Fast Launch that
  can be retired. Also to describe or use keys for the purpose of encrypting or
  decrypting volumes attached to instances that EC2 Fast Launch creates,
  and to generate data keys that are not plaintext.

To view the permissions for this policy, see [EC2FastLaunchServiceRolePolicy](../../../aws-managed-policy/latest/reference/EC2FastLaunchServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/EC2FastLaunchServiceRolePolicy.md") in the _AWS Managed
Policy Reference_.

For more information about using managed policies for Amazon EC2, see [AWS managed policies for Amazon EC2](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

## Create a service-linked role

You don't need to create this service-linked role manually. When you start using
EC2 Fast Launch for your AMI, Amazon EC2 creates the service-linked role for you,
if it doesn't already exist.

If the service-linked role is deleted from your account, you can enable
EC2 Fast Launch for another Windows AMI to re-create the role in your
account. Alternatively, you can disable EC2 Fast Launch for your current AMI,
and then enable it again. However, disabling the feature results in your AMI using the
standard launch process for all new instances while Amazon EC2 removes all of your
pre-provisioned snapshots. After all of the pre-provisioned snapshots are gone, you
can enable using EC2 Fast Launch for your AMI again.

## Access to customer managed keys

To enable EC2 Fast Launch for an [encrypted AMI](AMIEncryption.md "AMIEncryption.md") that
uses a customer managed key for encryption, you must grant the
AWSServiceRoleForEC2FastLaunch role permission to use the CMK. To do
this, call the [create-grant](../../../cli/latest/reference/kms/create-grant.md "../../../cli/latest/reference/kms/create-grant.md")
command. For `--grantee-principal`, specify the ARN for the
AWSServiceRoleForEC2FastLaunch role in your account. For
`--operations`, specify `CreateGrant`.

```
aws kms create-grant \
    --key-id arn:aws:kms:`us-east-1`:`111122223333`:key/`1234abcd-12ab-34cd-56ef-1234567890ab` \
    --grantee-principal arn:aws:iam::`111122223333`:role/AWSServiceRoleForEC2FastLaunch \
    --operations CreateGrant
```

## Edit a service-linked role

Amazon EC2 does not allow you to edit the AWSServiceRoleForEC2FastLaunch
service-linked role. After you create a service-linked role, you can't change the name
of the role, because various entities might reference the role. However, you can edit the
description of the role by using IAM. For more information, see [Editing a service-linked role](../../../IAM/latest/UserGuide/id_roles_update-service-linked-role.md "../../../IAM/latest/UserGuide/id_roles_update-service-linked-role.md") in the
_IAM User Guide_.

## Delete a service-linked role

You can delete a service-linked role only after first deleting all of the related
resources. This protects the Amazon EC2 resources that are associated with your
Amazon EC2 Windows Server AMI with EC2 Fast Launch enabled, because you can't inadvertently remove permission to
access the resources.

Use the IAM console, the AWS CLI, or the AWS API to delete the
**AWSServiceRoleForEC2FastLaunch** service-linked role. For more information,
see [Delete a service-linked role](../../../IAM/latest/UserGuide/id_roles_manage_delete.md#id_roles_manage_delete_slr "../../../IAM/latest/UserGuide/id_roles_manage_delete.md#id_roles_manage_delete_slr") in the _IAM User Guide_.

## Supported Regions

Amazon EC2 supports the EC2 Fast Launch service-linked role in all of the Regions
where the Amazon EC2 service is available.
