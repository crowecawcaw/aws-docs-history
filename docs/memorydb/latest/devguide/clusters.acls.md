

# Authenticating users with Access Control Lists (ACLs)
<a name="clusters.acls"></a>

You can authenticate users with Access control lists (ACLs). 

ACLs enable you to control cluster access by grouping users. These Access control lists are designed as a way to organize access to clusters. 

With ACLs, you create users and assign them specific permissions by using an access string, as described in the next section. You assign the users to Access control lists aligned with a specific role (administrators, human resources) that are then deployed to one or more MemoryDB clusters. By doing this, you can establish security boundaries between clients using the same MemoryDB cluster or clusters and prevent clients from accessing each other’s data. 

ACLs are designed to support the introduction of [ACL](https://valkey.io/docs/topics/acl/) in Redis OSS 6. When you use ACLs with your MemoryDB cluster, there are some limitations: 
+ You can't specify passwords in an access string. You set passwords with [CreateUser](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_CreateUser.html) or [UpdateUser](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_UpdateUser.html) calls.
+ For user rights, you pass `on` and `off` as a part of the access string. If neither is specified in the access string, the user is assigned `off` and doesn't have access rights to the cluster.
+ You can't use forbidden commands. If you specify a forbidden command, an exception will be thrown. For a list of those commands, see [Restricted commands](restrictedcommands.md).
+ You can't use the `reset` command as a part of an access string. You specify passwords with API parameters, and MemoryDB manages passwords. Thus, you can't use `reset` because it would remove all passwords for a user.
+ Redis OSS 6 introduces the [ACL LIST](https://valkey.io/commands/acl-list) command. This command returns a list of users along with the ACL rules applied to each user. MemoryDB supports the `ACL LIST` command, but does not include support for password hashes as Redis OSS does. With MemoryDB, you can use the [DescribeUsers](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeUsers.html) operation to get similar information, including the rules contained within the access string. However, [DescribeUsers](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeUsers.html) doesn't retrieve a user password. 

  Other read-only commands supported by MemoryDB include [ACL WHOAMI](https://valkey.io/commands/acl-whoami), [ACL USERS](https://valkey.io/commands/acl-users), and [ACL CAT](https://valkey.io/commands/acl-cat). MemoryDB doesn't support any other write-based ACL commands.

Using ACLs with MemoryDB is described in more detail following.

**Topics**
+ [Specifying Permissions Using an Access String](#access-string)
+ [Vector search capabilities](#access-vss)
+ [Applying ACLs to a cluster for MemoryDB](#rbac-using)

## Specifying Permissions Using an Access String
<a name="access-string"></a>

To specify permissions to a MemoryDB cluster, you create an access string and assign it to a user, using either the AWS CLI or AWS Management Console. 

Access strings are defined as a list of space-delimited rules which are applied on the user. They define which commands a user can execute and which keys a user can operate on. In order to execute a command, a user must have access to the command being executed and all keys being accessed by the command. Rules are applied from left to right cumulatively, and a simpler string may be used instead of the one provided if there is redundancies in the string provided.

For information about the syntax of the ACL rules, see [ACL](https://valkey.io/topics/acl). 

In the following example, the access string represents an active user with access to all available keys and commands.

 `on ~* &* +@all`

The access string syntax is broken down as follows:
+ `on` – The user is an active user.
+ `~*` – Access is given to all available keys.
+ `&*` – Access is given to all pubsub channels.
+ `+@all` – Access is given to all available commands.

The preceding settings are the least restrictive. You can modify these settings to make them more secure.

In the following example, the access string represents a user with access restricted to read access on keys that start with “app::” keyspace

`on ~app::* -@all +@read`

You can refine these permissions further by listing commands the user has access to:

`+{{command1}}` – The user's access to commands is limited to {{`command1`}}.

 `+@category` – The user's access is limited to a category of commands.

For information on assigning an access string to a user, see [Creating Users and Access Control Lists with the Console and CLI](#users-management).

If you are migrating an existing workload to MemoryDB, you can retrieve the access string by calling `ACL LIST`, excluding the user and any password hashes.

## Vector search capabilities
<a name="access-vss"></a>

For [Vector search](vector-search.md), all search commands belong to the `@search` category and existing categories `@read`, `@write`, `@fast` and `@slow` are updated to include search commands. If a user does not have access to a category, then the user does not have access to any commands within the category. For example, if the user does not have access to `@search`, then the user cannot execute any search related command.

The following table indicates the mapping of search commands to the appropriate categories.


| VSS Commands | @read | @write | @fast | @slow | 
| --- | --- | --- | --- | --- | 
| FT.CREATE |  | Y | Y |  | 
| FT.DROPINDEX |  | Y | Y |  | 
| FT.LIST | Y |  |  | Y | 
| FT.INFO | Y |  | Y |  | 
| FT.SEARCH | Y |  |  | Y | 
| FT.AGGREGATE | Y |  |  | Y | 
| FT.PROFILE | Y |  |  | Y | 
| FT.ALIASADD |  | Y | Y |  | 
| FT.ALIASDEL |  | Y | Y |  | 
| FT.ALIASUPDATE |  | Y | Y |  | 
| FT.\_ALIASLIST | Y |  |  | Y | 
| FT.EXPLAIN | Y |  | Y |  | 
| FT.EXPLAINCLI | Y |  | Y |  | 
| FT.CONFIG | Y |  | Y |  | 

## Applying ACLs to a cluster for MemoryDB
<a name="rbac-using"></a>

To use MemoryDB ACLs, you take the following steps: 

1. Create one or more users.

1. Create an ACL and add users to the list.

1. Assign the ACL to a cluster.

These steps are described in detail following.

**Topics**
+ [Creating Users and Access Control Lists with the Console and CLI](#users-management)
+ [Managing Access Control Lists with the Console and CLI](#user-groups)
+ [Assigning Access control lists to clusters](#users-groups-to-clusterss)

### Creating Users and Access Control Lists with the Console and CLI
<a name="users-management"></a>

The user information for ACLs users is a user name, and optionally a password and an access string. The access string provides the permission level on keys and commands. The name is unique to the user and is what is passed to the engine. 

Make sure that the user permissions you provide make sense with the intended purpose of the ACL. For example, if you create an ACL called `Administrators`, any user you add to that group should have its access string set to full access to keys and commands. For users in an `e-commerce` ACL, you might set their access strings to read-only access.

MemoryDB automatically configures a default user per account with a user name `"default"`. It will not be associated with any cluster unless explicity added to an ACL. You can't modify or delete this user. This user is intended for compatibility with the default behavior of previous Redis OSS versions and has an access string that permits it to call all commands and access all keys. 

An immutable “open-access” ACL will be created for every account which contains the default user. This is the only ACL the default user can be a member of. When you create a cluster, you must select an ACL to associate with the cluster. While you do have the option to apply the "open-access" ACL with the default user, we highly recommend creating an ACL with users that have permissions restricted to their business needs.

Clusters that do not have TLS enabled must use the "open-access" ACL to provide open authentication.

ACLs can be created with no users. An empty ACL would have no access to a cluster and can only be associated with TLS-enabled clusters.

When creating a user, you can set up to two passwords. When you modify a password, any existing connections to clusters are maintained.

In particular, be aware of these user password constraints when using ACLs for MemoryDB:
+ Passwords must be 16–128 printable characters.
+ The following nonalphanumeric characters are not allowed: `,` `""` `/` `@`. 

#### Managing Users with the Console and CLI
<a name="users-console"></a>

##### Creating a user (Console)
<a name="users.Createclusters.viewdetails"></a>

**To create users on the console**

1. Sign in to the AWS Management Console and open the MemoryDB console at [https://console.aws.amazon.com/memorydb/](https://console.aws.amazon.com/memorydb/).

1. On the left navigation pane, choose **Users**. 

1. Choose **Create user**

1. On the **Create user** page, enter a **Name**.

   Cluster naming constraints are as follows:
   + Must contain 1–40 alphanumeric characters or hyphens.
   + Must begin with a letter.
   + Can't contain two consecutive hyphens.
   + Can't end with a hyphen.

1. Under **Passwords**, you can enter up to two passwords.

1. Under **Access string**, enter an access string. The access string sets the permission level for what keys and commands the user is allowed.

1. For **Tags**, you can optionally apply tags to search and filter your users or track your AWS costs. 

1. Choose **Create**.

##### Creating a user using the AWS CLI
<a name="users.Create.cli"></a>

**To create a user by using the CLI**
+ Use the [create-user](https://docs.aws.amazon.com/cli/latest/reference/memorydb/create-user.html) command to create a user. 

  For Linux, macOS, or Unix:

  ```
  aws memorydb create-user \
    --user-name user-name-1 \
    --access-string "~objects:* ~items:* ~public:*" \
    --authentication-mode \
          Passwords={{"abc"}},Type=password
  ```

  For Windows:

  ```
  aws memorydb create-user ^
    --user-name user-name-1 ^
    --access-string "~objects:* ~items:* ~public:*" ^
    --authentication-mode \
          Passwords={{"abc"}},Type=password
  ```

##### Modifying a user (Console)
<a name="users.modifyclusters.viewdetails"></a>

**To modify users on the console**

1. Sign in to the AWS Management Console and open the MemoryDB console at [https://console.aws.amazon.com/memorydb/](https://console.aws.amazon.com/memorydb/).

1. On the left navigation pane, choose **Users**. 

1. Choose the radio button next to the user you want to modify and then choose **Actions**->**Modify**

1. If you want to modify a password, choose the **Modify passwords** radio button. Note that if you have two passwords, you must enter both when modifying one of them.

1. If you are updating the access string, enter the new one.

1. Choose **Modify**.

##### Modifying a user using AWS CLI
<a name="users.modify.cli"></a>

**To modify a user by using the CLI**

1. Use the [update-user](https://docs.aws.amazon.com/cli/latest/reference/memorydb/update-user.html) command to modify a user. 

1. When a user is modified, the Access control lists associated with the user are updated, along with any clusters associated with the ACL. All existing connections are maintained. The following are examples.

   For Linux, macOS, or Unix:

   ```
   aws memorydb update-user \
     --user-name user-name-1 \
     --access-string "~objects:* ~items:* ~public:*"
   ```

   For Windows:

   ```
   aws memorydb update-user ^
     --user-name user-name-1 ^
     --access-string "~objects:* ~items:* ~public:*"
   ```

##### Viewing user details (Console)
<a name="users.viewclusters.viewdetails"></a>

**To view user details on the console**

1. Sign in to the AWS Management Console and open the MemoryDB console at [https://console.aws.amazon.com/memorydb/](https://console.aws.amazon.com/memorydb/).

1. On the left navigation pane, choose **Users**. 

1. Choose the user under **User name** or use the search box to find the user.

1. Under **User settings** you can review the user's access string, password count, status and Amazon Resource Name (ARN).

1. Under **Access control lists (ACL)** you can review the ACL the user belongs to.

1. Under **Tags** you can review any tags associated with the user.

##### Viewing user details using the AWS CLI
<a name="user.view.cli"></a>

Use the [describe-users](https://docs.aws.amazon.com/cli/latest/reference/memorydb/describe-users.html) command to view details of a user. 

```
aws memorydb describe-users \
  --user-name {{my-user-name}}
```

##### Deleting a user (Console)
<a name="users.deleteclusters"></a>

**To delete users on the console**

1. Sign in to the AWS Management Console and open the MemoryDB console at [https://console.aws.amazon.com/memorydb/](https://console.aws.amazon.com/memorydb/).

1. On the left navigation pane, choose **Users**. 

1. Choose the radio button next to the user you want to modify and then choose **Actions**->**Delete**

1. To confirm, enter `delete` in the confirmation text box and then choose **Delete**.

1. To cancel, choose **Cancel**.

##### Deleting a user using the AWS CLI
<a name="users.delete.cli"></a>

**To delete a user by using the CLI**
+ Use the [delete-user](https://docs.aws.amazon.com/cli/latest/reference/memorydb/delete-user.html) command to delete a user. 

  The account is deleted and removed from any Access control lists to which it belongs. The following is an example.

  For Linux, macOS, or Unix:

  ```
  aws memorydb delete-user \
    --user-name user-name-2
  ```

  For Windows:

  ```
  aws memorydb delete-user ^
    --user-name user-name-2
  ```

### Managing Access Control Lists with the Console and CLI
<a name="user-groups"></a>

You can create Access control lists to organize and control access of users to one or more clusters, as shown following.

Use the following procedure to manage Access control lists using the console.

#### Creating an Access Control List (ACL) (Console)
<a name="acl.createclusters.viewdetails"></a>

**To create an Access control list using the console**

1. Sign in to the AWS Management Console and open the MemoryDB console at [https://console.aws.amazon.com/memorydb/](https://console.aws.amazon.com/memorydb/).

1. On left navigation pane, choose **Access control lists (ACL)**. 

1. Choose **Create ACL**.

1. On the **Create access control list (ACL)** page, enter an ACL name.

   Cluster naming constraints are as follows:
   + Must contain 1–40 alphanumeric characters or hyphens.
   + Must begin with a letter.
   + Can't contain two consecutive hyphens.
   + Can't end with a hyphen.

1. Under **Selected users** do one of the following:

   1. Create a new user by choosing **Create user**

   1. Add users by choosing **Manage** and then selecting users from the **Manage users** dialog and then selecting **Choose**.

1. For **Tags**, you can optionally apply tags to search and filter your ACLs or track your AWS costs. 

1. Choose **Create**.

#### Creating an Access Control List (ACL) using the AWS CLI
<a name="acl.create.cli"></a>

Use the following procedures to create an Access control list using the CLI.

**To create a new ACL and add a user by using the CLI**
+ Use the [create-acl](https://docs.aws.amazon.com/cli/latest/reference/memorydb/create-acl.html) command to create an ACL. 

  For Linux, macOS, or Unix:

  ```
  aws memorydb create-acl \
    --acl-name "new-acl-1" \
    --user-names {{"user-name-1"}} {{"user-name-2"}}
  ```

  For Windows:

  ```
  aws memorydb create-acl ^
    --acl-name "new-acl-1" ^
    --user-names {{"user-name-1"}} {{"user-name-2"}}
  ```

#### Modifying an Access Control List (ACL) (console)
<a name="acl.modifyclusters.viewdetails"></a>

**To modify an Access control lists using the console**

1. Sign in to the AWS Management Console and open the MemoryDB console at [https://console.aws.amazon.com/memorydb/](https://console.aws.amazon.com/memorydb/).

1. On left navigation pane, choose **Access control lists (ACL)**. 

1. Choose the ACL you wish to modify and then choose **Modify**

1. On the **Modify** page, under **Selected users** do one of the following:

   1. Create a new user by choosing **Create user** to add to the ACL.

   1. Add or remove users by choosing **Manage** and then selecting or de-selecting users from the **Manage users** dialog and then selecting **Choose**.

1. On the **Create access control list (ACL)** page, enter an ACL name.

   Cluster naming constraints are as follows:
   + Must contain 1–40 alphanumeric characters or hyphens.
   + Must begin with a letter.
   + Can't contain two consecutive hyphens.
   + Can't end with a hyphen.

1. Under **Selected users** do one of the following:

   1. Create a new user by choosing **Create user**

   1. Add users by choosing **Manage** and then selecting users from the **Manage users** dialog and then selecting **Choose**.

1. Choose **Modify** to save your changes or **Cancel** to discard them.

#### Modifying an Access Control List (ACL) using the AWS CLI
<a name="acl.modify.acl"></a>

**To modify a ACL by adding new users or removing current members by using the CLI**
+ Use the [update-acl](https://docs.aws.amazon.com/cli/latest/reference/memorydb/update-acl.html) command to modfy an ACL. 

  For Linux, macOS, or Unix:

  ```
  aws memorydb update-acl --acl-name new-acl-1 \
  --user-names-to-add {{user-name-3}} \
  --user-names-to-remove {{user-name-2}}
  ```

  For Windows:

  ```
  aws memorydb update-acl --acl-name new-acl-1 ^
  --user-names-to-add {{user-name-3}} ^
  --user-names-to-remove {{user-name-2}}
  ```

**Note**  
Any open connections belonging to a user removed from an ACL are ended by this command.

#### Viewing Access Control List (ACL) details (Console)
<a name="acls.viewclusters.viewdetails"></a>

**To view ACL details on the console**

1. Sign in to the AWS Management Console and open the MemoryDB console at [https://console.aws.amazon.com/memorydb/](https://console.aws.amazon.com/memorydb/).

1. On the left navigation pane, choose **Access control lists (ACL)**. 

1. Choose the ACL under **ACL name** or use the search box to find the ACL.

1. Under **Users** you can review list of users associated with the ACL.

1. Under **Associated clusters** you can review the cluster the ACL belongs to.

1. Under **Tags** you can review any tags associated with the ACL.

#### Viewing Access Control Lists (ACL) using the AWS CLI
<a name="acl.view.cli"></a>

Use the [describe-acls](https://docs.aws.amazon.com/cli/latest/reference/memorydb/describe-acls.html) command to view details of an ACL. 

```
aws memorydb describe-acls \
  --acl-name test-group
```

#### Deleting an Access Control List (ACL) (console)
<a name="acl.deleteacl"></a>

**To delete Access control lists using the console**

1. Sign in to the AWS Management Console and open the MemoryDB console at [https://console.aws.amazon.com/memorydb/](https://console.aws.amazon.com/memorydb/).

1. On left navigation pane, choose **Access control lists (ACL)**. 

1. Choose the ACL you wish to modify and then choose **Delete**

1. On the **Delete** page, enter `delete` in the confirmation box and choose **Delete** or **Cancel** to avoid deleting the ACL.

The ACL itself, not the users belonging to the group, is deleted.

#### Deleting an Access Control List (ACL) using the AWS CLI
<a name="acl.delete.cli"></a>

**To delete an ACL by using the CLI**
+ Use the [delete-acl](https://docs.aws.amazon.com/cli/latest/reference/memorydb/delete-acl.html) command to delete an ACL. 

  For Linux, macOS, or Unix:

  ```
  aws memorydb delete-acl /
     --{{acl-name}}
  ```

  For Windows:

  ```
  aws memorydb delete-acl ^
     --{{acl-name}}
  ```

  The preceding examples return the following response.

  ```
  aws memorydb delete-acl --acl-name "new-acl-1"
  {
      "ACLName": "new-acl-1",
      "Status": "deleting",
      "EngineVersion": "6.2",
      "UserNames": [
          "user-name-1", 
          "user-name-3"
      ],
      "clusters": [],
      "ARN":"arn:aws:memorydb:us-east-1:493071037918:acl/new-acl-1"
  }
  ```

### Assigning Access control lists to clusters
<a name="users-groups-to-clusterss"></a>

After you have created an ACL and added users, the final step in implementing ACLs is assigning the ACL to a cluster.

#### Assigning Access control lists to clusters Using the Console
<a name="users-groups-to-clusters-con"></a>

To add an ACL to a cluster using the AWS Management Console, see [Creating a MemoryDB cluster](getting-started.md#clusters.create).

#### Assigning Access control lists to clusters Using the AWS CLI
<a name="users-groups-to-clusters-CLI"></a>

 The following AWS CLI operation creates a cluster with encryption in transit (TLS) enabled and the **acl-name** parameter with the value `{{my-acl-name}}`. Replace the subnet group `subnet-group` with a subnet group that exists.

**Key Parameters**
+ **--engine-version** – Must be 6.2.
+ **--tls-enabled** – Used for authentication and for associating an ACL.
+ **--acl-name** – This value provides Access control lists comprised of users with specified access permissions for the cluster.

For Linux, macOS, or Unix:

```
aws memorydb create-cluster \
    --cluster-name "new-cluster" \
    --description {{"new-cluster"}} \
    --engine-version "6.2" \
    --node-type db.r6g.large \
    --tls-enabled \
    --acl-name "new-acl-1" \
    --subnet-group-name {{"subnet-group"}}
```

For Windows:

```
aws memorydb create-cluster ^
    --cluster-name "new-cluster" ^
    --cluster-description {{"new-cluster"}} ^
    --engine-version "6.2" ^
    --node-type db.r6g.large ^
    --tls-enabled ^
    --acl-name "new-acl-1" ^
    --subnet-group-name {{"subnet-group"}}
```

The following AWS CLI operation modifies a cluster with encryption in transit (TLS) enabled and the **acl-name** parameter with the value `new-acl-2`. 

For Linux, macOS, or Unix:

```
aws memorydb update-cluster \
    --cluster-name cluster-1 \
    --acl-name "new-acl-2"
```

For Windows:

```
aws memorydb update-cluster ^
    --cluster-name cluster-1 ^
    --acl-name "new-acl-2"
```