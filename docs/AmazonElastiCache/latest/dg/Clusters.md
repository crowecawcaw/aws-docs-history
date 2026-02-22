# Role-Based Access Control (RBAC)

With the Valkey and Redis OSS AUTH command as described in [Authenticating with the Valkey and Redis OSS AUTH command](auth.md "auth.md") you can use Role-Based Access Control (RBAC). RBAC is also the only way to control access to serverless caches. This is available for Valkey 7.2 and onward, and Redis OSS 6.0 to 7.2.

RBAC enables you to:

- Control cache access through user
  groups. These user groups are designed as a way to organize access to caches.
- With _authN_, have per user passwords as opposed to per cluster auth tokens.
- With _authZ_, have fine-grained user permissions.
- Base your cluster access on ACLs.
  Unlike Valkey and Redis OSS AUTH, where all authenticated clients have full cache access if
  their token is authenticated, RBAC enables you to assign users to sets depending on the users' desired roles. These sets are designed as a way to organize access to caches.

With RBAC, you create users and assign them specific permissions by using an access
string, as described following. You assign the users to sets aligned with a specific
role (administrators, human resources) that are then deployed to one or more ElastiCache
caches. By doing this, you can establish security boundaries between clients
using the same Valkey or Redis OSS cache or caches, and prevent clients from accessing each
other’s data.

RBAC is designed to support the introduction of [ACL](https://valkey.io/topics/acl/ "https://valkey.io/topics/acl/")
in Redis OSS 6. When you use RBAC with your ElastiCache Valkey or Redis OSS cache, there are
some limitations:

- A user group configured for the "VALKEY" engine can only contain users who are using an authentication mechanism (either password or IAM). This means all users with the engine "VALKEY", and any other users with the engine "Redis" who have their setup configured to authenticate with password or IAM, can be in this user group.
- When using RBAC with Valkey clusters, both user groups with engine "VALKEY" and with engine "REDIS" can be used.
- When using RBAC with Redis OSS clusters, only user groups with the engine "REDIS" can be used.
- You can't specify passwords in an access string. You set passwords with [CreateUser](../APIReference/API_CreateUser.md "../APIReference/API_CreateUser.md") or [ModifyUser](../APIReference/API_ModifyUser.md "../APIReference/API_ModifyUser.md") calls.
- For user rights, you enable or disable users with the `on` and `off` as a part of the access string.
  If neither is specified in the access string, the user is assigned `off`
  and doesn't have access rights to the cache.
- You can't use forbidden and renamed commands as part of the access string. If you specify a forbidden or a renamed command,
  an exception will be thrown. If you want to use access control lists (ACLs) for a
  renamed command, specify the original name of the command, in other words the name
  of the command before it was renamed.
- You can't use the `reset` command as a part of an access string. You specify
  passwords with API parameters, and ElastiCache for Valkey and Redis OSS manages passwords. Thus, you can't use
  `reset` because it would remove all passwords for a user.
- Redis OSS 6 introduces the [ACL LIST](https://valkey.io/commands/acl-list "https://valkey.io/commands/acl-list")
  command. This command returns a list of users along with the ACL rules applied to
  each user. ElastiCache supports the `ACL LIST` command, but does not include support for password hashes as Redis OSS does. With ElastiCache, you can use the [DescribeUsers](../APIReference/API_DescribeUsers.md "../APIReference/API_DescribeUsers.md") operation to get similar information, including the
  rules contained within the access string. However, [DescribeUsers](../APIReference/API_DescribeUsers.md "../APIReference/API_DescribeUsers.md") doesn't retrieve a user password.
- Other read-only commands supported by ElastiCache for Valkey and Redis OSS include
  [ACL WHOAMI](https://valkey.io/commands/acl-whoami "https://valkey.io/commands/acl-whoami"),
  [ACL USERS](https://valkey.io/commands/acl-users "https://valkey.io/commands/acl-users"), and
  [ACL CAT](https://valkey.io/commands/acl-cat "https://valkey.io/commands/acl-cat"). ElastiCache for Valkey and Redis OSS doesn't support
  any other write-based ACL commands.
- The following limits apply:

| Resource              | Maximum allowed |
| --------------------- | --------------- |
| Users per user group  | 100             |
| Number of users       | 1000            |
| Number of user groups | 100             |

**RBAC with Valkey**

When using Role Based Access Control with Valkey, users and user groups are made with the
"VALKEY" engine type. This is recommended, as by default Valkey with RBAC provides increased
security compared to Redis OSS. Both provisioned and serverless Valkey clusters support
VALKEY user and user group associations.

Key features of Valkey Access Control include:

- Valkey users are restricted to Valkey user group associations only.
- Valkey user groups can contain Valkey users, and Redis OSS users who are either password protected or IAM auth enabled.
- Valkey users must use either password protection or IAM authentication.
- VALKEY user groups can only be associated to VALKEY clusters
- There is no default user requirement. When the Valkey user group is attached to clusters, the default user requirement is automatically disabled. Customers will see that default user is turned off when using the ACL LIST command.
  More information on using RBAC with ElastiCache for Valkey and Redis OSS follows.

###### Topics

- [Specifying Permissions Using an Access String](#Access-string "#Access-string")
- [Applying RBAC to a Cache for ElastiCache for Valkey or Redis OSS](#rbac-using "#rbac-using")
- [Migrating from AUTH to RBAC](#Migrate-From-RBAC-to-Auth "#Migrate-From-RBAC-to-Auth")
- [Migrating from RBAC to AUTH](#Migrate-From-RBAC-to-AUTH-1 "#Migrate-From-RBAC-to-AUTH-1")
- [Automatically rotating passwords for users](User-Secrets-Manager.md "User-Secrets-Manager.md")
- [Authenticating with IAM](auth-iam.md "auth-iam.md")

## Specifying Permissions Using an Access String

To specify permissions to an ElastiCache Valkey or Redis OSS cache, you create an access string and assign it to a user through either the AWS CLI or AWS Management Console.

Access strings are defined as a list of space-delimited rules which are applied on the user.
They define which commands a user can execute and which keys a user can operate on.
In order to execute a command, a user must have access to the command being executed and all keys being accessed by the command.
Rules are applied from left to right cumulatively, and a simpler string may be used instead of the one provided if there are redundancies in the string provided.

For information about the syntax of the ACL rules, see [ACL](https://valkey.io/topics/acl/ "https://valkey.io/topics/acl/").

In the following example, the access string represents an active user with access to all
available keys and commands.

`on ~* +@all`

The access string syntax is broken down as follows:

- `on` – The user is an active user.
- `~*` – Access is given to all available keys.
- `+@all` – Access is given to all available commands.

The preceding settings are the least restrictive. You can modify these settings to
make them more secure.

In the following example, the access string represents a user with access restricted to read access on keys that start with “app::” keyspace

`on ~app::* -@all +@read`

You can refine these permissions further by listing commands the user has access to:

`+`command1`– The user's access to
 commands is limited to`command1``.

`+@category` – The user's access is limited to a category of
commands.

For information on assigning an access string to a user, see [Creating Users and User Groups with the Console and
CLI](#Users-management "#Users-management").

If you are migrating an existing workload to ElastiCache, you can retrieve the access string by calling `ACL LIST`, excluding the user and any password hashes.

For Redis OSS version 6.2 and above the following access string syntax is also supported:

- `&*` – Access is given to all available channels.

For Redis OSS version 7.0 and above the following access string syntax is also supported:

- `|` – Can be used for blocking subcommands (e.g "-config|set").
- `%R~<pattern>` – Add the specified read key pattern. This behaves similar to the regular key pattern but only grants permission to read
  from keys that match the given pattern. See [key permissions](https://valkey.io/topics/acl/ "https://valkey.io/topics/acl/") for more information.
- `%W~<pattern>` – Add the specified write key pattern. This behaves similar to the regular key pattern but only grants permission to write to keys that match the given pattern.
  See [ACL key permissions](https://valkey.io/topics/acl/ "https://valkey.io/topics/acl/") for more information.
- `%RW~<pattern>` – Alia for `~<pattern>`.
- `(<rule list>)` – Create a new selector to match rules against. Selectors are evaluated after the user permissions, and are evaluated according to the
  order they are defined. If a command matches either the user permissions or any selector, it is allowed. See [ACL selectors](https://valkey.io/topics/acl/ "https://valkey.io/topics/acl/") more information.
- `clearselectors` – Delete all of the selectors attached to the user.

## Applying RBAC to a Cache for ElastiCache for Valkey or Redis OSS

To use ElastiCache for Valkey or Redis OSS RBAC, you take the following steps:

1. Create one or more users.
2. Create a user group and add users to the group.
3. Assign the user group to a cache that has in-transit encryption enabled.

These steps are described in detail as follows.

###### Topics

- [Creating Users and User Groups with the Console and
  CLI](#Users-management "#Users-management")
- [Managing User Groups with the Console and CLI](#User-Groups "#User-Groups")
- [Assigning User Groups to Serverless Caches](#Users-groups-to-serverless-caches "#Users-groups-to-serverless-caches")
- [Assigning User Groups to Replication Groups](#Users-groups-to-RGs "#Users-groups-to-RGs")

### Creating Users and User Groups with the Console and

CLI

The user information for RBAC users is a user ID, user name, and optionally a password
and an access string. The access string provides the permission level on keys and
commands. The user ID is unique to the user, and the user name is what is passed to
the engine.

Make sure that the user permissions you provide make sense with the intended
purpose of the user group. For example, if you create a user group called
`Administrators`, any user you add to that group should have its
access string set to full access to keys and commands. For users in an
`e-commerce` user group, you might set their access strings to
read-only access.

ElastiCache automatically configures a default user with user ID and user name
`"default"` and adds it to all user groups. You can't
modify or delete this user. This user is intended for compatibility with the default
behavior of previous Redis OSS versions and has an access string that permits it to call
all commands and access all keys.

To add proper access control to a cache, replace this default user with a new
one that isn't enabled or uses a strong password. To change the default user,
create a new user with the user name set to `default`. You can then swap
it with the original default user.

The following procedures shows how to swap the original `default` user
with another `default` user that has a modified access string.

###### To modify the default user on the console

1. Sign in to the AWS Management Console and open the Amazon ElastiCache console at [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/ "https://console.aws.amazon.com/elasticache/").
2. Choose **User group management** from the navigation pane.
3. For **User group ID**, choose the ID that you want to modify. Make sure that you choose the link and not the check box.
4. Choose **Modify**.
5. In the **Modify** window, choose **Manage**. For "select the user that you want", select the user with the **User name** as default.
6. Choose **Choose**.
7. Choose **Modify**. When you do this, any existing connections to
   a cache that the original default user has are
   terminated.

###### To modify the default user with the AWS CLI

1. Create a new user with the user name `default` by using the following
   commands.

For Linux, macOS, or Unix:

```
aws elasticache create-user \
 --user-id "new-default-user" \
 --user-name "default" \
 --engine "VALKEY" \
 --passwords `"a-str0ng-pa))word"` \
 --access-string "off +get ~keys*"
```

For Windows:

```
aws elasticache create-user ^
 --user-id "new-default-user" ^
 --user-name "default" ^
 --engine "VALKEY" ^
 --passwords `"a-str0ng-pa))word"` ^
 --access-string "off +get ~keys*"
```

2. Create a user group and add the user that you created previously.

For Linux, macOS, or Unix:

```
aws elasticache create-user-group \
  --user-group-id "new-group-2" \
  --engine "VALKEY" \
  --user-ids "new-default-user"

```

For Windows:

```
aws elasticache create-user-group ^
  --user-group-id "new-group-2" ^
  --engine "VALKEY" ^
  --user-ids "new-default-user"

```

When creating a user, you can set up to two passwords. When you modify a password,
any existing connections to caches are maintained.

In particular, be aware of these user password constraints when using RBAC for ElastiCache for Valkey and Redis OSS:

- Passwords must be 16–128 printable characters.
- The following nonalphanumeric characters are not allowed: `,` `""` `/` `@`.

#### Managing Users with the Console and CLI

Use the following procedure to manage users on the console.

###### To manage users on the console

1. Sign in to the AWS Management Console and open the Amazon ElastiCache console at [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/ "https://console.aws.amazon.com/elasticache/").
2. On the Amazon ElastiCache dashboard, choose **User management**. The following
   options are available:
   - **Create user** – When creating a user, you enter a user ID, user
     name, authentication mode, and access string. The access string sets the
     permission level for what keys and commands the user is allowed.

   When creating a user, you can set up to two passwords. When you
   modify a password, any existing connections to caches
   are maintained.
   - **Modify user** – Enables you to update a user's authentication settings or change its access string.
   - **Delete user** – The account will be removed from any User Groups to which it belongs.

Use the following procedures to manage users with the AWS CLI.

###### To modify a user by using the CLI

- Use the `modify-user` command to update a user's password or
  passwords or change a user's access permissions.

When a
user is modified, the user groups associated with the user are updated, along with
any caches associated with the user group. All existing connections are
maintained. The following are examples.

For Linux, macOS, or Unix:

```
aws elasticache modify-user \
  --user-id user-id-1 \
  --access-string "~objects:* ~items:* ~public:*" \
  --authentication-mode Type=iam
```

For Windows:

```
aws elasticache modify-user ^
  --user-id user-id-1 ^
  --access-string "~objects:* ~items:* ~public:*" ^
  --authentication-mode Type=iam
```

###### Note

We don't recommend using the `nopass` option. If you do, we recommend setting the user's permissions to read-only with access to a limited set of keys.

###### To delete a user by using the CLI

- Use the `delete-user` command to delete a user. The account is deleted and removed from any user groups to which it belongs. The
  following is an example.

For Linux, macOS, or Unix:

```
aws elasticache delete-user \
  --user-id user-id-2

```

For Windows:

```
aws elasticache delete-user ^
  --user-id user-id-2

```

To see a list of users, call the
[describe-users](../../../cli/latest/reference/elasticache/describe-users.md "../../../cli/latest/reference/elasticache/describe-users.md") operation.

```
aws elasticache describe-users
```

### Managing User Groups with the Console and CLI

You can create user groups to organize and control access of users to one or more
caches, as shown following.

Use the following procedure to manage user groups using the console.

###### To manage user groups using the console

1. Sign in to the AWS Management Console and open the Amazon ElastiCache console at [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/ "https://console.aws.amazon.com/elasticache/").
2. On the Amazon ElastiCache dashboard, choose **User group management**.

The following operations are available to create new user groups:

    * **Create** – When you create a user group, you add users and then assign the user groups to caches. For example, you can create an `Admin` user group for users who have administrative roles on a cache.


    ###### Important

    If you are not using a Valkey or Redis OSS user group then you must include a default user when creating a user group.
    * **Add Users** – Add users to the user group.
    * **Remove Users** – Remove users from the user group. When users are
     removed from a user group, any existing connections they have to a cache are terminated.
    * **Delete** – Use this to delete a user group. Note that the user group itself, not the users belonging to the group, will be deleted.

For existing user groups, you can do the following:

    * **Add Users** – Add existing users to the user group.
    * **Delete Users** – Removes existing users from the user group.


    ###### Note

    Users are removed from the user group, but not deleted from the system.

Use the following procedures to manage user groups using the CLI.

###### To create a new user group and add a user by using the CLI

- Use the `create-user-group` command as shown following.

For Linux, macOS, or Unix:

```
aws elasticache create-user-group \
  --user-group-id "new-group-1" \
  --engine "VALKEY" \
  --user-ids `user-id-1`, `user-id-2`
```

For Windows:

```
aws elasticache create-user-group ^
  --user-group-id "new-group-1" ^
  --engine "VALKEY" ^
  --user-ids `user-id-1`, `user-id-2`
```

###### To modify a user group by adding new users or removing current members by using the

CLI

- Use the `modify-user-group` command as shown following.

For Linux, macOS, or Unix:

```
aws elasticache modify-user-group --user-group-id new-group-1 \
--user-ids-to-add `user-id-3` \
--user-ids-to-remove `user-id-2`
```

For Windows:

```
aws elasticache modify-user-group --user-group-id new-group-1 ^
--user-ids-to-add `user-id-3` ^
--user-ids-to-removere `user-id-2`
```

###### Note

Any open connections belonging to a user removed from a user group are ended by this command.

###### To delete a user group by using the CLI

- Use the `delete-user-group` command as shown following. The user group itself, not the users belonging to the group, is deleted.

For Linux, macOS, or Unix:

```
aws elasticache delete-user-group /
   --`user-group-id`
```

For Windows:

```
aws elasticache delete-user-group ^
   --`user-group-id`
```

To see a list of user groups, you can call the [describe-user-groups](../../../cli/latest/reference/elasticache/describe-user-groups.md "../../../cli/latest/reference/elasticache/describe-user-groups.md") operation.

```
aws elasticache describe-user-groups \
  --user-group-id test-group

```

### Assigning User Groups to Serverless Caches

After you have created a user group and added users, the final step in implementing RBAC is assigning the user group to a serverless cache.

#### Assigning User Groups to Serverless Caches

Using the Console

To add a user group to a serverless cache using the AWS Management Console, do the following:

- For cluster mode disabled, see [Creating a Valkey (cluster mode disabled) cluster (Console)](SubnetGroups.designing-cluster-pre.md#Clusters.Create.CON.valkey-gs "SubnetGroups.designing-cluster-pre.md#Clusters.Create.CON.valkey-gs")
- For cluster mode enabled, see [Creating a Valkey or Redis OSS (cluster mode enabled) cluster (Console)](Clusters.md#Clusters.Create.CON.RedisCluster "Clusters.md#Clusters.Create.CON.RedisCluster")

#### Assigning User Groups to Serverless Caches Using the AWS CLI

The following AWS CLI operation creates a serverless cache using the **user-group-id** parameter with the value `my-user-group-id`. Replace the
subnet group `sng-test` with a subnet group that exists.

###### Key Parameters

- `--engine` – Must be `VALKEY` or `REDIS`.
- `--user-group-id` – This value provides the ID of the user group, comprised of users with specified access permissions for the cache.

For Linux, macOS, or Unix:

```
aws elasticache create-serverless-cache \
    --serverless-cache-name "new-serverless-cache" \
    --description `"new-serverless-cache"` \
    --engine "VALKEY" \
    --user-group-id "new-group-1"

```

For Windows:

```
aws elasticache create-serverless-cache ^
    --serverless-cache-name "new-serverless-cache" ^
    --description `"new-serverless-cache"` ^
    --engine "VALKEY" ^
    --user-group-id "new-group-1"

```

The following AWS CLI operation modifies a serverless cache with the **user-group-id** parameter with the value `my-user-group-id`.

For Linux, macOS, or Unix:

```
aws elasticache modify-serverless-cache \
    --serverless-cache-name serverless-cache-1 \
    --user-group-id "new-group-2"

```

For Windows:

```
aws elasticache modify-serverless-cache ^
    --serverless-cache-name serverless-cache-1 ^
    --user-group-id "new-group-2"

```

Note that any modifications made to a
cache are updated asynchronously. You can monitor this progress by
viewing the events. For more information, see [Viewing ElastiCache events](ECEvents.md "ECEvents.md").

### Assigning User Groups to Replication Groups

After you have created a user group and added users, the final step in implementing RBAC is assigning the user group to a replication group.

#### Assigning User Groups to Replication Groups

Using the Console

To add a user group to a replication using the AWS Management Console, do the following:

- For cluster mode disabled, see [Creating a Valkey (cluster mode disabled) cluster (Console)](SubnetGroups.designing-cluster-pre.md#Clusters.Create.CON.valkey-gs "SubnetGroups.designing-cluster-pre.md#Clusters.Create.CON.valkey-gs")
- For cluster mode enabled, see [Creating a Valkey or Redis OSS (cluster mode enabled) cluster (Console)](Clusters.md#Clusters.Create.CON.RedisCluster "Clusters.md#Clusters.Create.CON.RedisCluster")

#### Assigning User Groups to Replication Groups Using the AWS CLI

The following AWS CLI operation creates a replication group with encryption in transit (TLS)
enabled and the **user-group-ids** parameter with the value `my-user-group-id`. Replace the
subnet group `sng-test` with a subnet group that exists.

###### Key Parameters

- `--engine` – Must be `valkey` or `redis`.
- `--engine-version` – Must be 6.0 or later.
- `--transit-encryption-enabled` – Required for authentication and
  for associating a user group.
- `--user-group-ids` – This value provides the ID of the user group, comprised of users with specified access permissions for the cache.
- `--cache-subnet-group` – Required for associating a user group.

For Linux, macOS, or Unix:

```
aws elasticache create-replication-group \
    --replication-group-id "new-replication-group" \
    --replication-group-description `"new-replication-group"` \
    --engine "VALKEY" \
    --cache-node-type cache.m5.large \
    --transit-encryption-enabled \
    --user-group-ids "new-group-1" \
    --cache-subnet-group `"cache-subnet-group"`
```

For Windows:

```
aws elasticache create-replication-group ^
    --replication-group-id "new-replication-group" ^
    --replication-group-description `"new-replication-group"` ^
    --engine "VALKEY" ^
    --cache-node-type cache.m5.large ^
    --transit-encryption-enabled ^
    --user-group-ids "new-group-1" ^
    --cache-subnet-group `"cache-subnet-group"`
```

The following AWS CLI operation modifies a replication group with encryption in transit (TLS)
enabled and the **user-group-ids** parameter with the value `my-user-group-id`.

For Linux, macOS, or Unix:

```
aws elasticache modify-replication-group \
    --replication-group-id replication-group-1 \
    --user-group-ids-to-remove "new-group-1" \
    --user-group-ids-to-add "new-group-2"
```

For Windows:

```
aws elasticache modify-replication-group ^
    --replication-group-id replication-group-1 ^
    --user-group-ids-to-remove "new-group-1" ^
    --user-group-ids-to-add "new-group-2"
```

Note the `PendingChanges` in the response. Any modifications made to a
cache are updated asynchronously. You can monitor this progress by
viewing the events. For more information, see [Viewing ElastiCache events](ECEvents.md "ECEvents.md").

## Migrating from AUTH to RBAC

If you are using AUTH as described in [Authenticating with the Valkey and Redis OSS AUTH command](auth.md "auth.md")
and want to migrate to using RBAC, use the following procedures.

Use the following procedure to migrate from AUTH to RBAC using the console.

###### To migrate from Valkey or Redis OSS AUTH to RBAC using the console

1. Sign in to the AWS Management Console and open the ElastiCache console at
   [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/ "https://console.aws.amazon.com/elasticache/").
2. From the list in the upper-right corner, choose the AWS Region where the cache that you
   want to modify is located.
3. In the navigation pane, choose the engine that runs on the cache that you want to
   modify.

A list of the chosen engine's caches appears. 4. In the list of caches, for the cache that you want to modify, choose its name. 5. For **Actions**, choose **Modify**.

The **Modify** window appears. 6. For **Access control**, choose **User group
access control list**. 7. For **User group access control list**, choose a user group. 8. Choose **Preview changes** and then on the next screen, **Modify**.

Use the following procedure to migrate from Valkey or Redis OSS AUTH to RBAC using the CLI.

###### To migrate from AUTH to RBAC using the CLI

- Use the `modify-replication-group` command as shown
  following.

For Linux, macOS, or Unix:

```
aws elasticache modify-replication-group --replication-group-id test \
    --auth-token-update-strategy DELETE \
    --user-group-ids-to-add `user-group-1`
```

For Windows:

```
aws elasticache modify-replication-group --replication-group-id test ^
    --auth-token-update-strategy DELETE ^
    --user-group-ids-to-add `user-group-1`
```

## Migrating from RBAC to AUTH

If you are using RBAC and want to migrate to Redis OSS AUTH, see [Migrating from RBAC to AUTH](auth.md#Migrate-From-RBAC-to-AUTH "auth.md#Migrate-From-RBAC-to-AUTH").

###### Note

If you need to disable access control on an ElastiCache cache, you'll need to do it through the AWS CLI. For more information, see [Disabling access control on an ElastiCache
Valkey or Redis OSS cache](in-transit-encryption-disable.md "in-transit-encryption-disable.md").
