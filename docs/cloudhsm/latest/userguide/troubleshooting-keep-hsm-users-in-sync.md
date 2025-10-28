# Keep HSM users in sync across HSMs in

the AWS CloudHSM cluster

To [manage your HSM's users](manage-hsm-users.md "manage-hsm-users.md"), you use a AWS CloudHSM command
line tool known as cloudhsm_mgmt_util. It communicates only with the HSMs that are in the tool's
configuration file. It's not aware of other HSMs in the cluster that are not in the
configuration file.

AWS CloudHSM synchronizes the keys on your HSMs across all other HSMs in the cluster, but it
doesn't synchronize the HSM's users or policies. When you use cloudhsm_mgmt_util to [manage HSM users](manage-hsm-users.md "manage-hsm-users.md"), these user changes might affect only some of
the cluster's HSMs—the ones that are in the cloudhsm_mgmt_util configuration file. This
can cause problems when AWS CloudHSM syncs keys across HSMs in the cluster, because the users that own
the keys might not exist on all HSMs in the cluster.

To avoid these problems, edit the cloudhsm_mgmt_util configuration file
_before_ managing users. For more information, see [Prerequisites for user management in AWS CloudHSM Management Utility](understand-users.md "understand-users.md").
