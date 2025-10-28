# Block public access for Amazon EBS snapshots

To prevent public sharing of your snapshots, you can enable _block public access
for snapshots_. After you enable block public access for snapshots in a Region, any
attempt to publicly share snapshots in that Region is automatically blocked. This can help you
to improve the security of your snapshots and to protect your snapshot data from unauthorized
or unintended access.

Block public access for snapshots can be enabled in one of two modes:

- **Block all sharing** — Blocks all public sharing of your
  snapshots. Users in the account can't request new public sharing. Additionally, snapshots that
  were already publicly shared are treated as private and are no longer publicly available.
- **Block new sharing** — Blocks only new public sharing of
  your snapshots. Users in the account can't request new public sharing. However, snapshots that were
  already publicly shared, remain publicly available.

###### Considerations

Keep the following in mind when working with block public access for snapshots.

- Block public access for snapshots does not prevent private snapshot sharing.
- Enabling block public access for snapshots in _block all sharing_
  mode does not change the permissions for snapshots that are already publicly shared.
  Instead, it prevents these snapshots from be publicly visible and publicly accessible.
  Therefore, the attributes for these snapshots still indicate that they are publicly
  shared, even though they are not publicly available.

If you later disable block public access or change the mode to _block new
sharing_, these snapshots will become publicly available again.

- Block public access for snapshots is a Regional setting. It applies to all snapshots
  in the Region in which it is enabled. You need to enable block public access for snapshots
  in each Region in which you want to prevent the public sharing of your snapshots.
- Block public access is an account-level setting. It applies to all users, including
  administrator users, in the account. You can't enable block public access for snapshots
  at the organization level.
- The block public access setting is configured either directly in the account or by
  using a declarative policy. Using a declarative policy allows you to apply the setting
  across multiple Regions simultaneously, as well as across multiple accounts
  simultaneously. When a declarative policy is in use, you can't modify the setting directly
  within an account. This topic describes how to configure the setting directly within an
  account. For information about using declarative policies, see [Declarative
  policies](../../../organizations/latest/userguide/orgs_manage_policies_declarative.md "../../../organizations/latest/userguide/orgs_manage_policies_declarative.md") in the _AWS Organizations User Guide_.
- Block public access for snapshots does not prevent the public sharing of EBS-backed
  AMIs. If you enable block public access for snapshots, users can still publicly share
  EBS-backed AMIs. If an EBS-backed AMI is publicly shared, users with access to that AMI
  can create volumes from its associated snapshots. To prevent public sharing of your
  AMIs, enable _[block public access for AMIs](../../../AWSEC2/latest/UserGuide/sharingamis-intro.md#block-public-access-to-amis "../../../AWSEC2/latest/UserGuide/sharingamis-intro.md#block-public-access-to-amis")_.
- Block public access for snapshots is not supported with local snapshots on AWS Outposts.

###### Pricing

Block public access for snapshots can be enabled at no additional cost.

###### Contents

- [IAM permissions](block-public-access-snapshots-perms.md "block-public-access-snapshots-perms.md")
- [Configure block public access](block-public-access-snapshots-enable.md "block-public-access-snapshots-enable.md")
- [View block public access setting](block-public-access-snapshots-view.md "block-public-access-snapshots-view.md")
- [Disable block public access](block-public-access-snapshots-disable.md "block-public-access-snapshots-disable.md")
- [Monitor block public access](block-public-access-snapshots-events.md "block-public-access-snapshots-events.md")
