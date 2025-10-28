# Managing access and roles in App Studio

One of the responsibilities of administrators in App Studio is to manage access, roles, and permissions. The following topics
contain information about the roles in App Studio, and how to add users, remove users, or change their role.

Access to AWS App Studio is managed using IAM Identity Center groups. To add users
to your App Studio instance, you must either:

- Add them to an existing IAM Identity Center group that is added to App Studio.
- Add them to a new or existing IAM Identity Center group that is not added to App Studio, and then add it
  to App Studio.
  Because roles are applied to groups, the IAM Identity Center groups should represent the access privileges (or roles) you want to assign to members of the group. For more information about IAM Identity Center,
  including information about managing users and groups, see the
  [IAM Identity Center User Guide](../../../singlesignon/latest/userguide/what-is.md "../../../singlesignon/latest/userguide/what-is.md").

## Roles and permissions

There are three roles in App Studio. The following list contains each role and their description.

- **Admin**: Admins can manage users and groups within App Studio, add and manage connectors, and manage applications created by builders. Additionally, users
  with the Admin role have all of the permissions included with the Builder role.
- **Builder**: Builders can create and build applications. Builders cannot manage users or groups, add or edit connector instances, or manage other builders' applications.
- **App User**: App Users can access and use published apps, but cannot access your App Studio instance to build apps or manage resources.

In App Studio, roles are assigned to groups, therefore each member of an added IAM Identity Center group
will be assigned the role that is assigned to the group.

## Viewing groups

Perform the following steps to view the groups added to your App Studio instance.

###### Note

You must be an Admin to view groups in your App Studio instance.

###### To view groups added to your App Studio instance

- In the navigation pane, choose **Roles** in the **Manage** section. You will
  be taken to a page displaying a list of existing groups as well as each group’s assigned role.

For information about managing groups, see [Adding users or groups](#add-group "#add-group"),
[Changing a group's role](#groups-change-role "#groups-change-role"), or [Removing users or groups from App Studio](#remove-group "#remove-group").

## Adding users or groups

To add users to App Studio, you must add them to an IAM Identity Center group and add that group to App Studio.
Perform the following steps to add users to App Studio by adding IAM Identity Center groups and assigning a role.

###### Note

You must be an Admin to add users to your App Studio instance.

###### To add users or groups to your App Studio instance

1. To add users to your App Studio instance, you must either add them to an existing IAM Identity Center group that has been added to App Studio, or
   create a new IAM Identity Center group, add the new user to it, and add the new group to App Studio.

For information about managing IAM Identity Center users
and groups, see [Manage identities in IAM Identity Center](../../../singlesignon/latest/userguide/manage-your-identity-source-sso.md "../../../singlesignon/latest/userguide/manage-your-identity-source-sso.md") in
the _AWS IAM Identity Center User Guide_. 2. If you added users to an existing IAM Identity Center group that was already added to App Studio, the new user can access App Studio with the designated permissions
after completing the setup of their IAM Identity Center permissions. If you created a new IAM Identity Center group, perform the following steps to add the group to App Studio and designate a role
for the group's members. 3. In the navigation pane, choose **Roles** in the **Manage** section. 4. On the **Roles** page, choose **+ Add group**. This will open an
**Add groups** dialog box for you to enter information about the group. 5. In the **Add groups** dialog box, enter the following information:

    * Choose the existing IAM Identity Center group in the dropdown.
    * Select a role for the group.




    	+ **Admin**: Admins can manage users and groups within App Studio, add and manage connectors, and manage applications created by builders. Additionally, users
    	with the Admin role have all of the permissions included with the Builder role.
    	+ **Builder**: Builders can create and build applications. Builders cannot manage users or groups, add or edit connector instances, or manage other builders' applications.
    	+ **App User**: App Users can access and use published apps, but cannot access your App Studio instance to build apps or manage resources.

6. Choose **Assign** to add the group to App Studio and provide its members with
   the configured role.

## Changing a group's role

Follow these steps to change the role assigned to a group in App Studio. Changing a group's role will change the role
of every member in that group.

###### Note

You must be an Admin to change the role of a group in App Studio.

###### To change the role of a group

1. In the navigation pane, choose **Roles** in the **Manage** section. You will be taken to a page displaying a list of existing groups as well as each group’s assigned role.
2. Choose the ellipses icon (**...**) and choose **Change role**.
3. In the **Change role** dialog box, select a new role for the group:
   - **Administrator**: Admins can manage users and groups within App Studio, add and manage connectors, and manage applications created by builders. Additionally, users
     with the Admin role have all of the permissions included with the Builder role.
   - **Builder**: Builders can create and build applications. Builders cannot manage users or groups, add or edit connector instances, or manage other builders' applications.
   - **App User**: App Users can access and use published apps, but cannot access your App Studio instance to build apps or manage resources.

4. Choose **Change** change the group's role.

## Removing users or groups from App Studio

You cannot remove an IAM Identity Center group from App Studio. Performing the following instructions will instead downgrade the group's role to **App User**. Members
of the group will still be able to access published App Studio apps.

To remove all access to App Studio and its apps, you must either delete the IAM Identity Center
group or users in the AWS IAM Identity Center console.
For information about managing IAM Identity Center users
and groups, see [Manage identities in IAM Identity Center](../../../singlesignon/latest/userguide/manage-your-identity-source-sso.md "../../../singlesignon/latest/userguide/manage-your-identity-source-sso.md") in
the _AWS IAM Identity Center User Guide_.

###### Note

You must be an Admin to downgrade a group's access in App Studio.

###### To remove a group

1. In the navigation pane, choose **Roles** in the **Manage** section. You will be taken to a page displaying a list of existing groups as well as each group’s assigned role.
2. Choose the ellipses icon (**...**) and choose **Revoke role**.
3. In the **Revoke role** dialog box, choose **Revoke** to downgrade the group's role to
   **App User**.
