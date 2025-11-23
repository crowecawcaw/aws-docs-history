# Log in to a cluster integrated with an AD domain

If you enabled the Active Delivery (AD) domain integration feature, authentication by password is enabled on the cluster head node. The home
directory of an AD user is created at the first user login to the head node or the first time a sudo-user switches to the AD user on
the head node.

Password authentication isn't enabled for cluster compute nodes. AD users must log in to
compute nodes with SSH keys.

By default, SSH keys are set up in the AD user `/${HOME}/.ssh` directory at the
first SSH login to the head node. This behavior can be disabled by setting [DirectoryService](DirectoryService-v3.md "DirectoryService-v3.md") / [GenerateSshKeysForUsers](DirectoryService-v3.md#yaml-DirectoryService-GenerateSshKeysForUsers "DirectoryService-v3.md#yaml-DirectoryService-GenerateSshKeysForUsers") boolean property to `false` in the
cluster configuration. By default, [DirectoryService](DirectoryService-v3.md "DirectoryService-v3.md") / [GenerateSshKeysForUsers](DirectoryService-v3.md#yaml-DirectoryService-GenerateSshKeysForUsers "DirectoryService-v3.md#yaml-DirectoryService-GenerateSshKeysForUsers") is set to `true`.

If an AWS ParallelCluster application requires passwordless SSH between cluster nodes, make sure that the SSH keys are correctly set up in the
user's home directory.

AWS Managed Microsoft AD passwords expire after 42 days. For more information, see [Manage password policies for AWS Managed Microsoft AD](../../../directoryservice/latest/admin-guide/ms_ad_password_policies.md "../../../directoryservice/latest/admin-guide/ms_ad_password_policies.md") in the _Directory Service Administration
Guide_. If your password expires, it must be reset to restore cluster access. For
more information, see [How to reset a user password and expired passwords](troubleshooting-v3-multi-user.md#troubleshooting-v3-multi-user-reset-passwd "troubleshooting-v3-multi-user.md#troubleshooting-v3-multi-user-reset-passwd").

###### Note

If the AD integration feature doesn't work as expected, the SSSD logs can provide useful
diagnostic information for troubleshooting the issue. These logs are located in the
`/var/log/sssd` directory on cluster nodes. By default, they're also stored in
a cluster’s Amazon CloudWatch log group.

For more information, see [Troubleshooting multi-user integration with Active Directory](troubleshooting-v3-multi-user.md "troubleshooting-v3-multi-user.md").
