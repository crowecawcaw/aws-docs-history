# Understand block public access for AMIs

To prevent the public sharing of your AMIs, you can enable _block public access
for AMIs_ at the account level.

When block public access is enabled, any attempt to make an AMI public is automatically
blocked. However, if you already have public AMIs, they remain publicly available.

To publicly share AMIs, you must disable block public access. When you’re
done sharing, it's best practice to re-enable block public access to prevent any
unintended public sharing of your AMIs.

###### Note

This setting is configured at the account level, either directly in the account or by using
a declarative policy. It must be configured in each AWS Region where you want to
prevent the public sharing of your AMIs. Using a declarative policy allows you to
apply the setting across multiple Regions simultaneously, as well as across multiple
accounts simultaneously. When a declarative policy is in use, you can't modify the
setting directly within an account. This topic describes how to configure the
setting directly within an account. For information about using declarative
policies, see [Declarative policies](../../../organizations/latest/userguide/orgs_manage_policies_declarative.md "../../../organizations/latest/userguide/orgs_manage_policies_declarative.md") in the _AWS Organizations User
Guide._

You can restrict IAM permissions to an administrator user so that only they can enable or
disable block public access for AMIs.

###### Topics

- [Default settings](#block-public-access-to-amis-default-settings "#block-public-access-to-amis-default-settings")
- [Manage the block public access setting for
  AMIs](manage-block-public-access-for-amis.md "manage-block-public-access-for-amis.md")

## Default settings

The **Block public access for AMIs** setting is either enabled or
disabled by default depending on whether your account is new or existing, and
whether you have public AMIs. The following table lists the default
settings:

| AWS account                                    | Block public access for AMIs default setting |
| ---------------------------------------------- | -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| New accounts                                   | Enabled                                      |
| Existing accounts with no public AMIs ¹        | Enabled                                      |
| Existing accounts with one or more public AMIs | Disabled                                     | ¹ If your account had one or more public AMIs on or after July 15, 2023, **Block public access for AMIs** is disabled by default for your account, even if you subsequently made all the AMIs private. |
