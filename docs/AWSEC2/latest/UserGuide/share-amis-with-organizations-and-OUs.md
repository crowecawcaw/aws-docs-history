# Share an AMI with organizations and

organizational units

[AWS Organizations](../../../organizations/latest/userguide/orgs_integrate_services_list.md "../../../organizations/latest/userguide/orgs_integrate_services_list.md") is an account management service that enables
you to consolidate multiple AWS accounts into an organization that you create and
centrally manage. You can share an AMI with an organization or an organizational unit
(OU) that you have created, in addition to [sharing
it with specific accounts](sharingamis-explicit.md "sharingamis-explicit.md").

An organization is an entity that you create to consolidate and centrally manage your
AWS accounts. You can organize the accounts in a hierarchical, tree-like structure,
with a [root](../../../organizations/latest/userguide/orgs_getting-started_concepts.md#root "../../../organizations/latest/userguide/orgs_getting-started_concepts.md#root") at the top and [organizational units](../../../organizations/latest/userguide/orgs_getting-started_concepts.md#organizationalunit "../../../organizations/latest/userguide/orgs_getting-started_concepts.md#organizationalunit") nested under the organization root. Each account can be added
directly to the root, or placed in one of the OUs in the hierarchy. For more
information, see [AWS
Organizations terminology and concepts](../../../organizations/latest/userguide/orgs_getting-started_concepts.md "../../../organizations/latest/userguide/orgs_getting-started_concepts.md") in the _AWS Organizations User Guide_.

When you share an AMI with an organization or an OU, all of the children accounts gain
access to the AMI. For example, in the following diagram, the AMI is shared with a
top-level OU (indicated by the arrow at the number **1**).
All of the OUs and accounts that are nested underneath that top-level OU (indicated by
the dotted line at number **2**) also have access to the
AMI. The accounts in the organization and OU outside the dotted line (indicated by the
number **3**) do not have access to the AMI because they
are not children of the OU that the AMI is shared with.

![The AMI is shared with an OU, and all children OUs and accounts get access to the AMI.](images/ami-share-with-orgs-and-ous.png)

###### Topics

- [Considerations](#considerations-org-ou "#considerations-org-ou")
- [Get the ARN of an organization or organizational unit](get-org-ou-ARN.md "get-org-ou-ARN.md")
- [Allow organizations and OUs to use a KMS key](allow-org-ou-to-use-key.md "allow-org-ou-to-use-key.md")
- [Manage AMI sharing with an organization or OU](share-amis-org-ou-manage.md "share-amis-org-ou-manage.md")

## Considerations

Consider the following when sharing AMIs with specific organizations or organizational
units.

- **Ownership** – To share an AMI, your
  AWS account must own the AMI.
- **Sharing limits** – The AMI owner can share an AMI
  with any organization or OU, including organizations and OUs that they’re
  not a member of.

For the maximum number of entities to which an AMI can be shared within a Region, see the
[Amazon EC2 service
quotas](../../../general/latest/gr/ec2-service.md#limits_ec2 "../../../general/latest/gr/ec2-service.md#limits_ec2").

- **Tags** – You can't share user-defined tags (tags
  that you attach to an AMI). When you share an AMI, your user-defined tags
  are not available to any AWS account in an organization or OU with which
  the AMI is shared.
- **ARN format** – When you specify an organization or
  OU in a command, make sure to use the correct ARN format. You'll get an
  error if you specify only the ID, for example, if you specify only
  `o-123example` or `ou-1234-5example`.

Correct ARN formats:

    + Organization ARN:
     `arn:aws:organizations::`111122223333`:organization/`organization-id``
    + OU ARN:
     `arn:aws:organizations::`111122223333`:ou/`organization-id`/`ou-id``

Where:

    + ``111122223333`` is an example of the
     12-digit account ID for the management account. If you don't know
     the management account number, you can describe the organization or
     the organizational unit to get the ARN, which includes the
     management account number. For more information, see [Get the ARN of an organization or organizational unit](get-org-ou-ARN.md "get-org-ou-ARN.md").
    + ``organization-id`` is the organization ID, for
     example, `o-123example`.
    + ``ou-id`` is the organizational unit ID, for
     example, `ou-1234-5example`.

For more information about the format of ARNs, see [Amazon Resource Names (ARNs)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md")
in the _IAM User Guide_.

- **Encryption and keys** – You can share AMIs that are
  backed by unencrypted and encrypted snapshots.
  - The encrypted snapshots must be encrypted with a customer managed key. You can’t share
    AMIs that are backed by snapshots that are encrypted with the
    default AWS managed key.
  - If you share an AMI that is backed by encrypted snapshots, you must allow the
    organizations or OUs to use the customer managed keys that were used to
    encrypt the snapshots. For more information, see [Allow organizations and OUs to use a KMS key](allow-org-ou-to-use-key.md "allow-org-ou-to-use-key.md").

- **Region** – AMIs are a Regional resource. When you
  share an AMI, it is available only in the Region from which you shared it.
  To make an AMI available in a different Region, copy the AMI to the Region
  and then share it. For more information, see [Copy an Amazon EC2 AMI](CopyingAMIs.md "CopyingAMIs.md").
- **Usage** – When you share an AMI, users can only
  launch instances from the AMI. They can’t delete, share, or modify it.
  However, after they have launched an instance using your AMI, they can then
  create an AMI from the instance they launched.
- **Billing** – You are not billed when your AMI is
  used by other AWS accounts to launch instances. The accounts that launch
  instances using the AMI are billed for the instances that they
  launch.
