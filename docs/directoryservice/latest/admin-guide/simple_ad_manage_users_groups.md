# Users and groups management in Simple AD

Users represent individual people or entities that have access to your directory. Groups are
very useful for giving or denying privileges to groups of users, rather than having to apply
those privileges to each individual user. If a user moves to a different organization, you move
that user to a different group and they automatically receive the privileges needed for the new
organization.

To create users and groups in an AWS Directory Service directory, you must use any instance (from either on-premises or EC2)
that has been joined to your AWS Directory Service directory, and be logged in as a user that has privileges to
create users and groups. You will also need to install the Active Directory Tools on your EC2
instance so you can add your users and groups with the Active Directory Users and Computers
snap-in. For more information about how to set up an EC2 instance and install the necessary
tools, see [Ways to join an Amazon EC2 instance to your
Simple AD](simple_ad_join_instance.md "simple_ad_join_instance.md").

###### Note

Your user accounts must have Kerberos preauthentication enabled. This is the default
setting for new user accounts, but it should not be modified. For more information about
this setting, go to [Preauthentication](http://technet.microsoft.com/en-us/library/cc961961.aspx "http://technet.microsoft.com/en-us/library/cc961961.aspx") on Microsoft TechNet.

The following topics include instructions on how to create and manage users and groups.

###### Topics

- [Installing the Active Directory Administration
  Tools for Simple AD](simple_ad_install_ad_tools.md "simple_ad_install_ad_tools.md")
- [Creating a Simple AD user](simple_ad_manage_users_groups_create_user.md "simple_ad_manage_users_groups_create_user.md")
- [Deleting a Simple AD user](simple_ad_manage_users_groups_delete_user.md "simple_ad_manage_users_groups_delete_user.md")
- [Resetting a Simple AD user
  password](simple_ad_manage_users_groups_reset_password.md "simple_ad_manage_users_groups_reset_password.md")
- [Creating a Simple AD group](simple_ad_manage_users_groups_create_group.md "simple_ad_manage_users_groups_create_group.md")
- [Adding a Simple AD user to a group](simple_ad_manage_users_groups_add_user_to_group.md "simple_ad_manage_users_groups_add_user_to_group.md")
