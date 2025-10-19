# IAM Identity Center configurable AD
 sync

IAM Identity Center configurable Active Directory (AD) sync enables you to explicitly configure the
 identities in Microsoft Active Directory that are automatically synchronized into IAM Identity Center and
 control the synchronization process.


* With this sync method, you can do the following:




	+ Control data boundaries by explicitly defining the users and groups in Microsoft
	 Active Directory that are automatically synchronized into IAM Identity Center. You can [add users and
	 groups](manage-sync-add-users-groups-configurable-ADsync.md "manage-sync-add-users-groups-configurable-ADsync.md") or [remove users and groups](manage-sync-remove-users-groups-configurable-ADsync.md "manage-sync-remove-users-groups-configurable-ADsync.md") to change the scope of the sync at any time.
	+ Assign synchronized users and groups single sign-on [access to AWS accounts](useraccess.md "useraccess.md") or [access to
	 applications](assignuserstoapp.md "assignuserstoapp.md"). The applications can be AWS managed applications or customer
	 managed applications.
	+ Control the synchronization process by [pausing and resuming the
	 sync](manage-sync-pause-resume-sync-configurable-ADsync.md "manage-sync-pause-resume-sync-configurable-ADsync.md") as needed. This helps you regulate the load on production
	 systems.

## Prerequisites and considerations


Before you use configurable AD sync, be aware of the following prerequisites and
 considerations:



* **Specifying users and groups in Active Directory to
 sync**


Before you can use IAM Identity Center to assign new users and groups access to AWS accounts and
 to AWS managed applications or customer managed applications, you must specify the
 users and groups in Active Directory to sync, and then sync them into IAM Identity Center.




	+ **Configurable AD sync** – IAM Identity Center doesn't
	 search your domain controller directly for users and groups. Instead, you must first
	 specify the list of users and groups to sync. You can configure this list, also
	 known as the *sync scope*, in one of the following ways,
	 depending on whether you have users and groups that are already synced into IAM Identity Center,
	 or you have new users and groups that you are syncing for the first time by using
	 configurable AD sync.
	
	
	
	
		- Existing users and groups: If you have users and groups that are already
		 synced into IAM Identity Center, the sync scope in configurable AD sync is prepopulated with a
		 list of those users and groups. To assign new users or groups, you must
		 specifically add them to the sync scope. For more information, see [Add users and groups to
		 your sync scope](manage-sync-add-users-groups-configurable-ADsync.md "manage-sync-add-users-groups-configurable-ADsync.md").
		- New users and groups: If you want to assign new users and groups access to
		 AWS accounts and to applications, you must specify which users and groups to
		 add to the sync scope in configurable AD sync before you can use IAM Identity Center to make
		 the assignment. For more information, see [Add users and groups to
		 your sync scope](manage-sync-add-users-groups-configurable-ADsync.md "manage-sync-add-users-groups-configurable-ADsync.md").


* **Making assignments to nested groups in Active
 Directory**


Groups that are members of other groups are called *nested
 groups* (or child groups). 




	+ **Configurable AD sync** – Using
	 configurable AD sync to make assignments to a group in Active Directory that
	 contains nested groups might increase the scope of users who have access to
	 AWS accounts or to applications. In this case, the assignment applies to all
	 users, including those in nested groups. For example, if you assign access to Group
	 A, and Group B is a member of Group A, members of Group B also inherit this
	 access.
* **Updating automated workflows**


If you have automated workflows that use the IAM Identity Center identity store API actions and
 IAM Identity Center assignment API actions to assign new users and groups access to accounts and to
 applications, and to sync them into IAM Identity Center, you must adjust those workflows by April 15,
 2022 so that they function as expected with configurable AD sync. Configurable AD sync
 changes the order in which user and group assignment and provisioning occur, and the way
 in which queries are performed.




	+ **Configurable AD sync** – Provisioning
	 occurs first, and it is not automatically performed. Instead, you must first
	 explicitly add users and groups to the identity store by adding them to your sync
	 scope. For information about the recommended steps for automating your sync
	 configuration for configurable AD sync, see [Automate your sync
	 configuration for configurable AD sync](automate-sync-configuration-configurable-ADsync.md "automate-sync-configuration-configurable-ADsync.md").

###### Topics

* [How configurable AD sync works](how-it-works-configurable-ADsync.md "how-it-works-configurable-ADsync.md")
* [Configure
 attribute mappings for your sync](manage-sync-configure-attribute-mapping-configurable-ADsync.md "manage-sync-configure-attribute-mapping-configurable-ADsync.md")
* [First-time Active Directory to IAM Identity Center sync
 setup](manage-sync-configurable-ADsync.md "manage-sync-configurable-ADsync.md")
* [Add users and groups to
 your sync scope](manage-sync-add-users-groups-configurable-ADsync.md "manage-sync-add-users-groups-configurable-ADsync.md")
* [Remove users and
 groups from your sync scope](manage-sync-remove-users-groups-configurable-ADsync.md "manage-sync-remove-users-groups-configurable-ADsync.md")
* [Pause and resume your
 sync](manage-sync-pause-resume-sync-configurable-ADsync.md "manage-sync-pause-resume-sync-configurable-ADsync.md")
* [Automate your sync
 configuration for configurable AD sync](automate-sync-configuration-configurable-ADsync.md "automate-sync-configuration-configurable-ADsync.md")
