

# Create an Active Directory
<a name="create-addir-v3"></a>

Make sure that you create an Active Directory (AD) before you create your cluster. For information about how to choose the type of active directory for your cluster, see [Which to choose](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/what_is.html#choosing_an_option) in the *AWS Directory Service Administration Guide*.

If the directory is empty, add users with user names and passwords. For more information, see the documentation that's specific to [AWS Directory Service for Microsoft Active Directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_manage_users_groups.html) or [Simple AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/simple_ad_manage_users_groups.html).

**Note**  
AWS ParallelCluster requires every Active Directory user directory to be in the `/home/$user` directory.