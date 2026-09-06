

# Stored procedures for granting and revoking privileges for RDS for Db2
<a name="db2-sp-granting-revoking-privileges"></a>

The built-in stored procedures described in this topic manage users, roles, groups, and authorization for Amazon RDS for Db2 databases. To run these procedures, the master user must first connect to the `rdsadmin` database. 

For tasks that use these stored procedures, see [Granting and revoking privileges](db2-granting-revoking-privileges.md) and [Setting up Kerberos authentication](db2-kerberos-setting-up.md). 

Refer to the following built-in stored procedures for information about their syntax, parameters, usage notes, and examples.

**Topics**
+ [rdsadmin.create\_role](#db2-sp-create-role)
+ [rdsadmin.grant\_role](#db2-sp-grant-role)
+ [rdsadmin.revoke\_role](#db2-sp-revoke-role)
+ [rdsadmin.drop\_role](#db2-sp-drop-role)
+ [rdsadmin.add\_user](#db2-sp-add-user)
+ [rdsadmin.change\_password](#db2-sp-change-password)
+ [rdsadmin.list\_users](#db2-sp-list-users)
+ [rdsadmin.remove\_user](#db2-sp-remove-user)
+ [rdsadmin.add\_groups](#db2-sp-add-groups)
+ [rdsadmin.remove\_groups](#db2-sp-remove-groups)
+ [rdsadmin.dbadm\_grant](#db2-sp-dbadm-grant)
+ [rdsadmin.dbadm\_revoke](#db2-sp-dbadm-revoke)
+ [rdsadmin.set\_sid\_group\_mapping](#db2-sp-set-sid-group-mapping)
+ [rdsadmin.list\_sid\_group\_mapping](#db2-sp-list-sid-group-mapping)
+ [rdsadmin.remove\_sid\_group\_mapping](#db2-sp-remove-sid-group-mapping)

## rdsadmin.create\_role
<a name="db2-sp-create-role"></a>

Creates a role.

### Syntax
<a name="db2-sp-create-role-syntax"></a>

```
db2 "call rdsadmin.create_role(
    '{{database_name}}',
    '{{role_name}}')"
```

### Parameters
<a name="db2-sp-create-role-parameters"></a>

The following parameters are required:

{{database\_name}}  
The name of the database the command will run on. The data type is `varchar`.

{{role\_name}}  
The name of the role that you want to create. The data type is `varchar`.

### Usage notes
<a name="db2-sp-create-role-usage-notes"></a>

For information about checking the status of creating a role, see [rdsadmin.get\_task\_status](db2-user-defined-functions.md#db2-udf-get-task-status). 

### Examples
<a name="db2-sp-create-role-examples"></a>

The following example creates a role called `MY_ROLE` for database `DB2DB`.

```
db2 "call rdsadmin.create_role(
    'DB2DB',
    'MY_ROLE')"
```

## rdsadmin.grant\_role
<a name="db2-sp-grant-role"></a>

Assigns a role to a role, user, or group.

### Syntax
<a name="db2-sp-grant-role-syntax"></a>

```
db2 "call rdsadmin.grant_role(
    ?,
    '{{database_name}}',
    '{{role_name}}',
    '{{grantee}}',
    '{{admin_option}}')"
```

### Parameters
<a name="db2-sp-grant-role-parameters"></a>

The following output parameter is required: 

?  
A parameter marker that outputs the unique identifier for the task. This parameter only accepts `?`.

The following input parameters are required:

{{database\_name}}  
The name of the database the command will run on. The data type is `varchar`.

{{role\_name}}  
The name of the role that you want to create. The data type is `varchar`.

{{grantee}}  
The role, user, or group to receive authorization. The data type is `varchar`. Valid values: `ROLE`, `USER`, `GROUP`, `PUBLIC`.   
Format must be value followed by name. Separate multiple values and names with commas. Example: '`USER {{user1}}, {{user2}}, GROUP {{group1}}, {{group2}}`'. Replace the names with your own information.

The following input parameter is optional:

{{admin\_option}}  
Specifies whether the grantee `ROLE` has `DBADM` authorization to assign roles. The data type is `char`. The default is `N`.

### Usage notes
<a name="db2-sp-grant-role-usage-notes"></a>

For information about checking the status of assigning a role, see [rdsadmin.get\_task\_status](db2-user-defined-functions.md#db2-udf-get-task-status). 

### Examples
<a name="db2-sp-grant-role-examples"></a>

**Example 1: Assigning role to role, user, and group, and granting authorization**

The following example assigns a role called `ROLE_TEST` for database `TESTDB` to the role called `role1`, the user called `user1`, and the group called `group1`. `ROLE_TEST` is given admin authorization to assign roles.

```
db2 "call rdsadmin.grant_role(
    ?,
    'TESTDB',
    'ROLE_TEST',
    'ROLE role1, USER user1, GROUP group1',
    'Y')"
```

**Example 2: Assigning role to `PUBLIC` and not granting authorization**

The following example assigns a role called `ROLE_TEST` for database `TESTDB` to `PUBLIC`. `ROLE_TEST` isn't given admin authorization to assign roles.

```
db2 "call rdsadmin.grant_role(
    ?,
    'TESTDB',
    'ROLE_TEST',
    'PUBLIC')"
```

## rdsadmin.revoke\_role
<a name="db2-sp-revoke-role"></a>

Revokes a role from a role, user, or group.

### Syntax
<a name="db2-sp-revoke-role-syntax"></a>

```
db2 "call rdsadmin.revoke_role(
    ?,
    '{{database_name}}',
    '{{role_name}}',
    '{{grantee}}')"
```

### Parameters
<a name="db2-sp-revoke-role-parameters"></a>

The following output parameter is required: 

?  
A parameter marker that outputs the unique identifier for the task. This parameter only accepts ?.

The following input parameters are required:

{{database\_name}}  
The name of the database the command will run on. The data type is `varchar`.

{{role\_name}}  
The name of the role that you want to revoke. The data type is `varchar`.

{{grantee}}  
The role, user, or group to lose authorization. The data type is `varchar`. Valid values: `ROLE`, `USER`, `GROUP`, `PUBLIC`.   
Format must be value followed by name. Separate multiple values and names with commas. Example: '`USER {{user1}}, {{user2}}, GROUP {{group1}}, {{group2}}`'. Replace the names with your own information.

### Usage notes
<a name="db2-sp-revoke-role-usage-notes"></a>

For information about checking the status of revoking a role, see [rdsadmin.get\_task\_status](db2-user-defined-functions.md#db2-udf-get-task-status). 

### Examples
<a name="db2-sp-revoke-role-examples"></a>

**Example 1: Revoking role from role, user, and group**

The following example revokes a role called `ROLE_TEST` for database `TESTDB` from the role called `role1`, the user called `user1`, and the group called `group1`.

```
db2 "call rdsadmin.revoke_role(
    ?,
    'TESTDB',
    'ROLE_TEST',
    'ROLE role1, USER user1, GROUP group1')"
```

**Example 2: Revoking role from `PUBLIC`**

The following example revokes a role called `ROLE_TEST` for database `TESTDB` from `PUBLIC`. 

```
db2 "call rdsadmin.revoke_role(
    ?,
    'TESTDB',
    'ROLE_TEST',
    'PUBLIC')"
```

## rdsadmin.drop\_role
<a name="db2-sp-drop-role"></a>

Drops a role.

### Syntax
<a name="db2-sp-drop-role-syntax"></a>

```
db2 "call rdsadmin.drop_role(
    ?,
    '{{database_name}}',
    '{{role_name}}')"
```

### Parameters
<a name="db2-sp-drop-role-parameters"></a>

The following output parameter is required: 

?  
A parameter marker that outputs the unique identifier for the task. This parameter only accepts ?.

The following input parameters are required:

{{database\_name}}  
The name of the database the command will run on. The data type is `varchar`.

{{role\_name}}  
The name of the role that you want to drop. The data type is `varchar`.

### Usage notes
<a name="db2-sp-drop-role-usage-notes"></a>

For information about checking the status of dropping a role, see [rdsadmin.get\_task\_status](db2-user-defined-functions.md#db2-udf-get-task-status). 

### Examples
<a name="db2-sp-drop-role-examples"></a>

The following example drops a role called `ROLE_TEST` for database `TESTDB`.

```
db2 "call rdsadmin.drop_role(
    ?,
    'TESTDB',
    'ROLE_TEST')"
```

## rdsadmin.add\_user
<a name="db2-sp-add-user"></a>

Adds a user to an authorization list.

### Syntax
<a name="db2-sp-add-user-syntax"></a>

```
db2 "call rdsadmin.add_user(
    '{{username}}',
    '{{password}}',
    '{{group_name}},{{group_name}}')"
```

### Parameters
<a name="db2-sp-add-user-parameters"></a>

The following parameters are required:

{{username}}  
A user's username. The data type is `varchar`.

{{password}}  
A user's password. The data type is `varchar`.

The following parameter is optional:

{{group\_name}}  
The name of a group that you want to add the user to. The data type is `varchar`. The default is an empty string or null. 

### Usage notes
<a name="db2-sp-add-user-usage-notes"></a>

You can add a user to one or more groups by separating the group names with commas. 

You can create a group when you create a new user, or when you [add a group to an existing user](db2-granting-revoking-privileges.md#add-group-to-user). You can't create a group by itself.

**Note**  
The maximum number of users that you can add by calling `rdsadmin.add_user` is 5,000.

For information about checking the status of adding a user, see [rdsadmin.get\_task\_status](db2-user-defined-functions.md#db2-udf-get-task-status). 

### Examples
<a name="db2-sp-add-user-examples"></a>

The following example creates a user called `jorge_souza` and assigns the user to the groups called `sales` and `inside_sales`.

```
db2 "call rdsadmin.add_user(
    'jorge_souza',
    '*******',
    'sales,inside_sales')"
```

## rdsadmin.change\_password
<a name="db2-sp-change-password"></a>

Changes a user's password.

### Syntax
<a name="db2-sp-change-password-syntax"></a>

```
db2 "call rdsadmin.change_password(
    '{{username}}',
    '{{new_password}}')"
```

### Parameters
<a name="db2-sp-change-password-parameters"></a>

The following parameters are required:

{{username}}  
A user's username. The data type is `varchar`.

{{new\_password}}  
A new password for the user. The data type is `varchar`.

### Usage notes
<a name="db2-sp-change-password-usage-notes"></a>

For information about checking the status of changing a password, see [rdsadmin.get\_task\_status](db2-user-defined-functions.md#db2-udf-get-task-status). 

### Examples
<a name="db2-sp-change-password-examples"></a>

The following example changes the password for `jorge_souza`.

```
db2 "call rdsadmin.change_password(
    'jorge_souza',
    '*******')"
```

## rdsadmin.list\_users
<a name="db2-sp-list-users"></a>

Lists users on an authorization list. 

### Syntax
<a name="db2-sp-list-users-syntax"></a>

```
db2 "call rdsadmin.list_users()"
```

### Usage notes
<a name="db2-sp-list-users-usage-notes"></a>

For information about checking the status of listing users, see [rdsadmin.get\_task\_status](db2-user-defined-functions.md#db2-udf-get-task-status). 

## rdsadmin.remove\_user
<a name="db2-sp-remove-user"></a>

Removes user from authorization list.

### Syntax
<a name="db2-sp-remove-user-syntax"></a>

```
db2 "call rdsadmin.remove_user('{{username}}')"
```

### Parameters
<a name="db2-sp-remove-user-parameters"></a>

The following parameter is required:

{{username}}  
A user's username. The data type is `varchar`.

### Usage notes
<a name="db2-sp-remove-user-usage-notes"></a>

For information about checking the status of removing a user, see [rdsadmin.get\_task\_status](db2-user-defined-functions.md#db2-udf-get-task-status). 

### Examples
<a name="db2-sp-remove-user-examples"></a>

The following example removes `jorge_souza` from being able to access databases in RDS for Db2 DB instances.

```
db2 "call rdsadmin.remove_user('jorge_souza')"
```

## rdsadmin.add\_groups
<a name="db2-sp-add-groups"></a>

Adds groups to a user.

### Syntax
<a name="db2-sp-add-groups-syntax"></a>

```
db2 "call rdsadmin.add_groups(
    '{{username}}',
    '{{group_name}},{{group_name}}')"
```

### Parameters
<a name="db2-sp-add-groups-parameters"></a>

The following parameters are required:

{{username}}  
A user's username. The data type is `varchar`.

{{group\_name}}  
The name of a group that you want to add the user to. The data type is `varchar`. The default is an empty string.

### Usage notes
<a name="db2-sp-add-groups-usage-notes"></a>

You can add one or more groups to a user by separating the group names with commas. For information about checking the status of adding groups, see [rdsadmin.get\_task\_status](db2-user-defined-functions.md#db2-udf-get-task-status). 

### Examples
<a name="db2-sp-add-groups-examples"></a>

The following example adds the `direct_sales` and `b2b_sales` groups to user `jorge_souza`. 

```
db2 "call rdsadmin.add_groups(
    'jorge_souza',
    'direct_sales,b2b_sales')"
```

## rdsadmin.remove\_groups
<a name="db2-sp-remove-groups"></a>

Removes groups from a user.

### Syntax
<a name="db2-sp-remove-groups-syntax"></a>

```
db2 "call rdsadmin.remove_groups(
    '{{username}}',
    '{{group_name}},{{group_name}}')"
```

### Parameters
<a name="db2-sp-remove-groups-parameters"></a>

The following parameters are required:

{{username}}  
A user's username. The data type is `varchar`.

{{group\_name}}  
The name of a group that you want to remove the user from. The data type is `varchar`.

### Usage notes
<a name="db2-sp-remove-groups-usage-notes"></a>

You can remove one or more groups from a user by separating the group names with commas. 

For information about checking the status of removing groups, see [rdsadmin.get\_task\_status](db2-user-defined-functions.md#db2-udf-get-task-status). 

### Examples
<a name="db2-sp-remove-groups-examples"></a>

The following example removes the `direct_sales` and `b2b_sales` groups from user `jorge_souza`. 

```
db2 "call rdsadmin.remove_groups(
    'jorge_souza',
    'direct_sales,b2b_sales')"
```

## rdsadmin.dbadm\_grant
<a name="db2-sp-dbadm-grant"></a>

Grants `DBADM`, `ACCESSCTRL`, or `DATAACCESS` authorization to a role, user, or group.

### Syntax
<a name="db2-sp-dbadm-grant-syntax"></a>

```
db2 "call rdsadmin.dbadm_grant(
    ?,
    '{{database_name}}',
    '{{authorization}}',
    '{{grantee}}')"
```

### Parameters
<a name="db2-sp-dbadm-grant-parameters"></a>

The following output parameter is required: 

?  
A parameter marker that outputs the unique identifier for the task. This parameter only accepts `?`.

The following input parameters are required:

{{database\_name}}  
The name of the database the command will run on. The data type is `varchar`. 

{{authorization}}  
The type of authorization to grant. The data type is `varchar`. Valid values: `DBADM`, `ACCESSCTRL`, `DATAACCESS`.   
Separate multiple types with commas.

{{grantee}}  
The role, user, or group to receive authorization. The data type is `varchar`. Valid values: `ROLE`, `USER`, `GROUP`.   
Format must be value followed by name. Separate multiple values and names with commas. Example: '`USER {{user1}}, {{user2}}, GROUP {{group1}}, {{group2}}`'. Replace the names with your own information.

### Usage notes
<a name="db2-sp-dbadm-grant-usage-notes"></a>

The role to receive access must exist.

For information about checking the status of granting database admin access, see [rdsadmin.get\_task\_status](db2-user-defined-functions.md#db2-udf-get-task-status).

### Examples
<a name="db2-sp-dbadm-grant-examples"></a>

**Example 1: Granting database admin access to role**

The following example grants database admin access to the database named `TESTDB` for the role `ROLE_DBA`.

```
db2 "call rdsadmin.dbadm_grant(
    ?, 
    'TESTDB',
    'DBADM',
    'ROLE ROLE_DBA')"
```

**Example 2: Granting database admin access to user and group**

The following example grants database admin access to the database named `TESTDB` for `user1` and `group1`.

```
db2 "call rdsadmin.dbadm_grant(
    ?, 
    'TESTDB', 
    'DBADM', 
    'USER user1, GROUP group1')"
```

**Example 3: Granting database admin access to multiple users and groups**

The following example grants database admin access to the database named `TESTDB` for `user1`, `user2`, `group1`, and `group2`.

```
db2 "call rdsadmin.dbadm_grant(
    ?, 
    'TESTDB', 
    'DBADM', 
    'USER user1, user2, GROUP group1, group2')"
```

## rdsadmin.dbadm\_revoke
<a name="db2-sp-dbadm-revoke"></a>

Revokes `DBADM`, `ACCESSCTRL`, or `DATAACCESS` authorization from a role, user, or group.

### Syntax
<a name="db2-sp-dbadm-revoke-syntax"></a>

```
db2 "call rdsadmin.dbadm_revoke(
    ?,
    '{{database_name}}',
    '{{authorization}}',
    '{{grantee}}')"
```

### Parameters
<a name="db2-sp-dbadm-revoke-parameters"></a>

The following output parameter is required: 

?  
The unique identifier for the task. This parameter only accepts `?`.

The following input parameters are required:

{{database\_name}}  
The name of the database the command will run on. The data type is `varchar`.

{{authorization}}  
The type of authorization to revoke. The data type is `varchar`. Valid values: `DBADM`, `ACCESSCTRL`, `DATAACCESS`.   
Separate multiple types with commas.

{{grantee}}  
The role, user, or group to revoke authorization from. The data type is `varchar`. Valid values: `ROLE`, `USER`, `GROUP`.   
Format must be value followed by name. Separate multiple values and names with commas. Example: '`USER {{user1}}, {{user2}}, GROUP {{group1}}, {{group2}}`'. Replace the names with your own information.

### Usage notes
<a name="db2-sp-dbadm-revoke-usage-notes"></a>

For information about checking the status of revoking database admin access, see [rdsadmin.get\_task\_status](db2-user-defined-functions.md#db2-udf-get-task-status).

### Examples
<a name="db2-sp-dbadm-revoke-examples"></a>

**Example 1: Revoking database admin access from role**

The following example revokes database admin access to the database named `TESTDB` for the role `ROLE_DBA`.

```
db2 "call rdsadmin.dbadm_revoke(
    ?, 
    'TESTDB',
    'DBADM',
    'ROLE ROLE_DBA')"
```

**Example 2: Revoking database admin access from user and group**

The following example revokes database admin access to the database named `TESTDB` for `user1` and `group1`.

```
db2 "call rdsadmin.dbadm_revoke(
    ?, 
    'TESTDB', 
    'DBADM', 
    'USER user1, GROUP group1')"
```

**Example 3: Revoking database admin access from multiple users and groups**

The following example revokes database admin access to the database named `TESTDB` for `user1`, `user2`, `group1`, and `group2`.

```
db2 "call rdsadmin.dbadm_revoke(
    ?, 
    'TESTDB', 
    'DBADM', 
    'USER user1, user2, GROUP group1, group2')"
```

## rdsadmin.set\_sid\_group\_mapping
<a name="db2-sp-set-sid-group-mapping"></a>

Creates a mapping between a security ID (SID) and the corresponding Active Directory group.

### Syntax
<a name="db2-sp-set-sid-group-mapping-syntax"></a>

```
db2 "call rdsadmin.set_sid_group_mapping(
    ?,
    'SID',
    'group_name')"
```

### Parameters
<a name="db2-sp-set-sid-group-mapping-parameters"></a>

The following output parameter is required:

?  
A parameter marker that outputs an error message. This parameter only accepts `?`.

The following input parameters are required:

{{SID}}  
The security ID (SID). The data type is `varchar`.

{{group\_name}}  
The name of the Active Directory group to map to the SID. The data type is `varchar`.

### Usage notes
<a name="db2-sp-set-sid-group-mapping-usage-notes"></a>

Use this stored procedure to enable Kerberos authentication with Active Directory groups. If the `SID` or `group_name` already exists in the mapping, this stored procedure fails.

For information about how to find the SID for a group, see [Step 8: Retrieve the Active Directory group SID in PowerShell](db2-kerberos-setting-up.md#db2-kerberos-setting-up-retrieve-ad-group-sid).

For information about checking the status of creating a mapping, see [rdsadmin.get\_task\_status](db2-user-defined-functions.md#db2-udf-get-task-status).

### Examples
<a name="db2-sp-set-sid-group-mapping-examples"></a>

The following example maps a SID to a group called `my_group`.

```
db2 "call rdsadmin.set_sid_group_mapping(
    ?,
    'S-1-5-21-9146495592-531070549-834388463-513',
    'my_group')"
```

## rdsadmin.list\_sid\_group\_mapping
<a name="db2-sp-list-sid-group-mapping"></a>

Lists all security ID (SID) and Active Directory group mappings configured on the DB instance.

### Syntax
<a name="db2-sp-list-sid-group-mapping-syntax"></a>

```
db2 "call rdsadmin.list_sid_group_mapping()"
```

### Usage notes
<a name="db2-sp-list-sid-group-mapping-usage-notes"></a>

For information about checking the status of listing mappings, see [rdsadmin.get\_task\_status](db2-user-defined-functions.md#db2-udf-get-task-status).

## rdsadmin.remove\_sid\_group\_mapping
<a name="db2-sp-remove-sid-group-mapping"></a>

Removes a security ID (SID) and its corresponding Active Directory group mapping from a DB instance.

### Syntax
<a name="db2-sp-remove-sid-group-mapping-syntax"></a>

```
db2 "call rdsadmin.remove_sid_group_mapping(
    ?,
    'SID')"
```

### Parameters
<a name="db2-sp-remove-sid-group-mapping-parameters"></a>

The following output parameter is required:

?  
A parameter marker that outputs an error message. This parameter only accepts `?`.

The following input parameter is required:

{{SID}}  
The security ID (SID). The data type is `varchar`.

### Usage notes
<a name="db2-sp-remove-sid-group-mapping-usage-notes"></a>

For information about how to find the SID for a group, see [Step 8: Retrieve the Active Directory group SID in PowerShell](db2-kerberos-setting-up.md#db2-kerberos-setting-up-retrieve-ad-group-sid).

For information about checking the status of removing mappings, see [rdsadmin.get\_task\_status](db2-user-defined-functions.md#db2-udf-get-task-status).

### Examples
<a name="db2-sp-remove-sid-group-mapping-examples"></a>

The following example removes a SID mapping from the group it was mapped to.

```
db2 "call rdsadmin.remove_sid_group_mapping(
    ?,
    'S-1-5-21-9146495592-531070549-834388463-513')"
```