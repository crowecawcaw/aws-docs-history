# Create an Active Directory

Make sure that you create an Active Directory (AD) before you create your cluster. For
information about how to choose the type of active directory for your cluster, see [Which to
choose](../../../directoryservice/latest/admin-guide/what_is.md#choosing_an_option "../../../directoryservice/latest/admin-guide/what_is.md#choosing_an_option") in the _AWS Directory Service Administration
Guide_.

If the directory is empty, add users with user names and passwords. For more information,
see the documentation that's specific to [AWS Directory Service for Microsoft Active Directory](../../../directoryservice/latest/admin-guide/ms_ad_manage_users_groups.md "../../../directoryservice/latest/admin-guide/ms_ad_manage_users_groups.md") or [Simple AD](../../../directoryservice/latest/admin-guide/simple_ad_manage_users_groups.md "../../../directoryservice/latest/admin-guide/simple_ad_manage_users_groups.md").

###### Note

AWS ParallelCluster requires every Active Directory user directory to be in the
`/home/$user` directory.
