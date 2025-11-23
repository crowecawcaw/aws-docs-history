# Account Factory guidance

###### Note

Single account provision, update and customization must target an organizational unit (OU)
with AWSControlTowerBaseline enabled. If an OU does not have the AWSControlTowerBaseline enabled, you can activate account auto-enrollment
or use ResetEnabledBaseline and ResetEnabledControl APIs on EnabledBaselines and EnabledControls on that OU to enroll accounts.
There are no single account provisioning limitations when an OU has the AWSControlTowerBaseline enabled.

You can encounter issues when using Account Factory to provision a new account in AWS Control Tower.
For information about how to troubleshoot these issues, see the section [New Account Provisioning Failed](troubleshooting.md#account-provisioning-failed "troubleshooting.md#account-provisioning-failed") in [Troubleshooting](troubleshooting.md "troubleshooting.md") of the _AWS Control Tower User Guide_.

We recommend that you create federated users or IAM roles instead of IAM users.
Federated users and IAM roles provide you with temporary credentials. IAM users have
long-term credentials that can be difficult to manage. For more information, see [IAM identities (users, user groups,
and roles)](../../../IAM/latest/UserGuide/id.md "../../../IAM/latest/UserGuide/id.md") in the _IAM User Guide_.

If you're authenticated as an IAM user or IAM Identity Center user when provisioning a new account in Account Factory or
when using the _Enroll account_ feature AWS Control Tower, verify that your user
has access to your AWS Service Catalog portfolio. Otherwise, you might receive an error message from Service Catalog.
For more information, see [No Launch Paths Found Error](troubleshooting.md#no-launch-paths-found "troubleshooting.md#no-launch-paths-found") in [the Troubleshooting section](troubleshooting.md "troubleshooting.md") of the
_AWS Control Tower User Guide_.

###### Note

Up to five accounts can be provisioned at a time.
