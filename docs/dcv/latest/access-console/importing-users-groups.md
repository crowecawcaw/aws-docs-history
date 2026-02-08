# Importing users and groups

Users will only appear in the Amazon DCV Access Console if they have been directly imported from the
Access Console, or have already logged in. Users are imported into the Access Console by uploading
a CSV file. Once imported, user names populate on the **Users** page of the Access Console.

User groups can also be imported with a CSV file to the Access Console. If you choose
not to import user groups, you can create from the Access Console directly.

###### To import users and groups with a CSV file

1. Go to the **Users** page.
2. Select the **Import users** button.
3. Upload a CSV file where each row has the following format:

userId,loginUsername,displayName,role,groupIds

With the following parameters:

    * **userId**– This field is required.
    * **loginUsername**– This field is optional. It will be set to the same as userId, if left empty. When using external OAuth, this should match the username from the OAuth provider.
    * **displayName**– This field is optional. It
     will be set to the same as userId, if left empty.
    * **role**– This field is optional, and can be
     set to either Admin or User. It will be set to User, if left
     empty.
    * **groupIds**– This field is optional. You can
     include multiple GroupIDs, separated by “|”.

###### Note

You can import users and groups from the same CSV file.

## User and group assignment from OAuth claims

Importing users by CSV is not supported for some external OAuth setups because the userId may not be known until first login. When using external OAuth, you can configure the Amazon DCV Access Console to automatically assign roles and groups to users based on claims in the OAuth token.

The following properties in the `access-console-handler.properties` file enable role and group assignment from OAuth claims:

- `jwt-default-groups-claim-key` is the key that contains the default groups. To enable access to session templates on first login, create groups and assign them session templates through the Access Console, then use the group IDs in your external OAuth configuration. Groups are only assigned on first login and subsequent group management should be done through the Access Console. The groups value should be comma-separated group IDs (e.g., "group1,group2"). If a group does not exist, it will be created.
- `jwt-role-claim-key` is the key that contains the user's role. The role value must match a configured role (e.g., Admin, User, Guest). Invalid roles fall back to the default role defined in `default-role` in the Handler configuration file.

For more information about these and other Handler configuration parameters, see [Handler configuration files](handler-config-files.md "handler-config-files.md").
