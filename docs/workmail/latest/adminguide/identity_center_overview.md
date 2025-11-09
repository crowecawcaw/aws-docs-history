# Working with IAM Identity Center

You can enable multi-factor authentication (MFA) in Amazon WorkMail by associating your Amazon WorkMail
users with IAM Identity Center. For more information, see [What is IAM Identity Center](../../../singlesignon/latest/userguide/what-is.md "../../../singlesignon/latest/userguide/what-is.md").

The table below describes the steps to address different scenarios.

| Scenario                                                 | Steps                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| -------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Associating Amazon WorkMail users to IAM Identity Center | 1. [Enabling IAM Identity Center in Amazon WorkMail](enabling_identity_center.md "enabling_identity_center.md")<br>2. [Assigning IAM Identity Center users and groups to Amazon WorkMail<br>application](assigning_usersandgroups.md "assigning_usersandgroups.md")<br>3. [Associating Amazon WorkMail users with IAM Identity Center users](connecting_wmusers.md "connecting_wmusers.md")                                                                                                                                  |
| Existing Amazon WorkMail users                           | 1. Create IAM Identity Center users with the same username, group the users<br>together and assign the group to the Amazon WorkMail application.<br>2. Associate the Amazon WorkMail users to the IAM Identity Center users.                                                                                                                                                                                                                                                                                                 |
| Existing IAM Identity Center users                       | 1. Create Amazon WorkMail users with the same username as the IAM Identity Center<br>users.<br>2. Assign the IAM Identity Center users or groups to the Amazon WorkMail<br>application.<br>3. Associate the Amazon WorkMail users to IAM Identity Center users.                                                                                                                                                                                                                                                              |
| Connecting an external directory to IAM Identity Center  | 1. Sync the external directory users to the IAM Identity Center group. For more<br>information, see [IAM Identity Center<br>Identity source tutorials](../../../singlesignon/latest/userguide/enable-mfa.md "../../../singlesignon/latest/userguide/enable-mfa.md")<br>2. Assign the IAM Identity Center group to the Amazon WorkMail application.<br>3. Connect the external directory to Amazon WorkMail and make sure the user<br>names match<br>4. Associate the Amazon WorkMail users to the IAM Identity Center users. |

Once the above steps are completed you can view the IAM Identity Center status, link to the AWS IAM Identity Center
to manage users and groups, MFA enabled Amazon WorkMail web application URL, authentication mode,
personal access token status and timeline under IAM Identity Center under **Settings** in the Amazon WorkMail console. For more information on managing MFA in the
IAM Identity Center console, see [Multi-factor authentication for
IAM Identity Center users .](../../../singlesignon/latest/userguide/enable-mfa.md "../../../singlesignon/latest/userguide/enable-mfa.md")

###### Note

Make sure the configuration between Amazon WorkMail and IAM Identity Center is well tested and verified. Users
could lose access to their mailboxes when the configuration is not correct and
complete.

###### Topics

- [Enabling IAM Identity Center in Amazon WorkMail](enabling_identity_center.md "enabling_identity_center.md")
- [Assigning IAM Identity Center users and groups to Amazon WorkMail
  application](assigning_usersandgroups.md "assigning_usersandgroups.md")
- [Associating Amazon WorkMail users with IAM Identity Center users](connecting_wmusers.md "connecting_wmusers.md")
- [Authentication mode](authenticate_mode.md "authenticate_mode.md")
- [Configuring personal access tokens](personal_access-token.md "personal_access-token.md")
- [Disabling IAM Identity Center](disabling_sso.md "disabling_sso.md")
