# Database access using Role-Based

Access Control

You can restrict access to the actions that users can perform on databases using
_role-based access control_ (RBAC) in Amazon DocumentDB (with MongoDB compatibility). RBAC works by
granting one or more roles to a user. These roles determine the operations that a user can
perform on database resources. Amazon DocumentDB currently supports both built-in roles that are
scoped at the database level, such as `read`, `readWrite`,
`readAnyDatabase`, `clusterAdmin`, and user-defined roles that can
be scoped to specific actions and granular resources such as collections based on your
requirements.

Common use cases for RBAC include enforcing least privileges by creating users with
read-only access to the databases or collections in a cluster, and multi-tenant application
designs that enable a single user to access a given database or collection in a
cluster.

###### Note

All new users created before **March 26, 2020** have been
granted the `dbAdminAnyDatabase`, `readWriteAnyDatabase`, and
`clusterAdmin` roles. It is recommended that you reevaluate all existing
users and modify the roles as necessary to enforce least privileges for your clusters.

###### Topics

- [RBAC concepts](#role_based_access_control-concepts "#role_based_access_control-concepts")
- [Getting started with RBAC
  built-in roles](#role_based_access_control-getting_started "#role_based_access_control-getting_started")
- [Getting started with RBAC user-defined roles](#w5aac29c29c15 "#w5aac29c29c15")
- [Connecting to Amazon DocumentDB as
  a User](#role_based_access_control-connecting_as_user "#role_based_access_control-connecting_as_user")
- [Common commands](#role_based_access_control-common_commands "#role_based_access_control-common_commands")
- [Functional differences](#role_based_access_control-functional_differences "#role_based_access_control-functional_differences")
- [Limits](#role_based_access_control-limits "#role_based_access_control-limits")
- [Database access using Role-Based Access Control](#role_based_access_control-built_in_roles "#role_based_access_control-built_in_roles")

## RBAC concepts

The following are important terms and concepts related to role-based access control.
For more information on Amazon DocumentDB users, see [Managing Amazon DocumentDB users](security.md "security.md").

- **User** — An individual entity that can
  authenticate to the database and perform operations.
- **Password** — A secret that is used to
  authenticate the user.
- **Role** — Authorizes a user to perform
  actions on one or more databases.
- **Admin Database** — The database in which
  users are stored and authorized against.
- **Database (`db`)** — The
  namespace within clusters that contains collections for storing documents.

The following command creates a user named `sample-user`.

```
db.createUser({user: "sample-user", pwd: "abc123", roles: [{role: "read", db: "sample-database"}]})
```

In this example:

- `user: "sample-user"` — Indicates the user name.
- `pwd: "abc123"` — Indicates the user password.
- `role: "read", "db: "sample-database"` — Indicates that the
  user `sample-user` will have read permissions in
  `sample-database`.

![Code example showing a createUser command indicating user name, password, and permissions.](images/rbac-createuser-command.png)

The following example shows the output after you get the user `sample-user`
with `db.getUser(sample-user)`. In this example, the user
`sample-user` resides in the `admin` database but has the read
role for the database `sample-database`.

![Code output example showing the result of the createUser command defining the new user ID, the admin database the new user is assigned to, and role permissions applied to the user.](images/rbac-createuser-output-json.png)

When creating users, if you omit the `db` field when specifying the role,
Amazon DocumentDB will implicitly attribute the role to the database in which the connection is
being issued against. For example, if your connection is issued against the database
`sample-database` and you run the following command, the user
`sample-user` will be created in the `admin` database and will
have `readWrite` permissions to the database
`sample-database`.

```
db.createUser({user: "sample-user", pwd: "abc123", roles: ["readWrite"]})
```

Output from this operation looks something like the following.

```
{
   "user":"sample-user",
   "roles":[
      {
         "db":"sample-database",
         "role":"readWrite"
      }
   ]
}
```

Creating users with roles that are scoped across all databases (for example,
`readAnyDatabase`) require that you either be in the context of the
`admin` database when creating the user, or you explicitly state the
database for the role when creating the user. To issue commands against the
`admin` database, you can use the command `use admin`. For
more information, see [Common commands](#role_based_access_control-common_commands "#role_based_access_control-common_commands").

## Getting started with RBAC

built-in roles

To help you get started with role-based access control, this section walks you through
an example scenario of enforcing least privilege by creating roles for three users with
different job functions.

- `user1` is a new manager that needs to be able to view and access
  all databases in a cluster.
- `user2` is a new employee that needs access to only one database,
  `sample-database-1`, in that same cluster.
- `user3` is an existing employee that needs to view and access a
  different database, `sample-database-2` that they didn't have access
  to before, in the same cluster.

At a point later, both `user1` and `user2` leave the company and
so their access must be revoked.

To create users and grant roles, the user that you authenticate to the cluster with
must have an associated role that can perform actions for `createUser` and
`grantRole`. For example, the roles `admin` and
`userAdminAnyDatabase` can both grant such abilities, for example. For
actions per role, see [Database access using Role-Based Access Control](#role_based_access_control-built_in_roles "#role_based_access_control-built_in_roles").

###### Note

In Amazon DocumentDB, all user and role operations (for example, `create`,
`get`, `drop`, `grant`, `revoke`,
etc.) are implicitly performed in the `admin` database whether or not you
are issuing commands against the `admin` database.

First, to understand what the current users and roles are in the cluster, you can run
the `show users` command, as in the following example. You will see two
users, `serviceadmin` and the primary user for the cluster. These two users
always exist and cannot be deleted. For more information, see [Managing Amazon DocumentDB users](security.md "security.md").

```
show users
```

For `user1`, create a role with read and write access to all databases in
the entire cluster with the following command.

```
db.createUser({user: "user1", pwd: "abc123", roles: [{role: "readWriteAnyDatabase", db: "admin"}]})
```

Output from this operation looks something like the following.

```
{
   "user":"user1",
   "roles":[
      {
         "role":"readWriteAnyDatabase",
         "db":"admin"
      }
   ]
}
```

For `user2`, create a role with read-only access to the database
`sample-database-1` with the following command.

```
db.createUser({user: "user2", pwd: "abc123", roles: [{role: "read", db: "sample-database-1"}]})
```

Output from this operation looks something like the following.

```
{
   "user":"user2",
   "roles":[
      {
         "role":"read",
         "db":"sample-database-1"
      }
   ]
}
```

To simulate the scenario that `user3` is an existing user, first create the
user `user3`, and then assign a new role to `user3`.

```
db.createUser({user: "user3", pwd: "abc123", roles: [{role: "readWrite", db: "sample-database-1"}]})
```

Output from this operation looks something like the following.

```
{
   "user":"user3",
   "roles":[
      {
         "role":"readWrite",
         "db":"sample-database-1"
      }
   ]
}
```

Now that the user `user3` has been created, assign `user3` the
role `read` to `sample-database-2`.

```
db.grantRolesToUser("user3", [{role: "read", db: "sample-database-2"}])
```

Lastly, both `user1` and `user2` leave the company and need
their access to the cluster revoked. You can do this by dropping the users, as
follows.

```
db.dropUser("user1")
db.dropUser("user2")
```

To ensure that all users have the appropriate roles, you can list all users with the
following command.

```
show users
```

Output from this operation looks something like the following.

```
{
   "_id":"serviceadmin",
   "user":"serviceadmin",
   "db":"admin",
   "roles":[
      {
         "db":"admin",
         "role":"root"
      }
   ]
}
{
   "_id":"master-user",
   "user":"master-user",
   "db":"admin",
   "roles":[
      {
         "db":"admin",
         "role":"root"
      }
   ]
}
{
   "_id":"user3",
   "user":"user3",
   "db":"admin",
   "roles":[
      {
         "db":"sample-database-2",
         "role":"read"
      },
      {
         "db":"sample-database-1",
         "role":"readWrite"
      }
   ]
}
```

## Getting started with RBAC user-defined roles

To help you get started with user-defined roles, this section walks you through an
example scenario of enforcing least privilege by creating roles for three users with
different job functions.

In this example, the following applies:

- `user1` is a new manager that needs to be able to view and access
  all databases in a cluster.
- `user2` is a new employee that needs only the ‘find’ action to only
  one database, `sample-database-1`, in that same cluster.
- `user3` is an existing employee that needs to view and access a
  specific collection, col2 in a different database,
  `sample-database-2` that they didn't have access to before, in
  the same cluster.
- For `user1`, create a role with read and write access to all
  databases in the entire cluster with the following command.

```
db.createUser(
	{
	    user: "user1", pwd: "abc123",
	    roles: [{role: "readWriteAnyDatabase", db: "admin"}]
	}
	)
```

Output from this operation looks something like the following.

```
{
   "user":"user1",
   "roles":[
      {
         "role":"readWriteAnyDatabase",
         "db":"admin"
      }
   ]
}
```

For `user2`, create a role with ‘find’ privileges to all collections in the
database `sample-database-1` with the following command. Note that this role
would ensure that any associated users can only run find queries.

```
db.createRole(
{
    role: "findRole",
    privileges: [
    {
        resource: {db: "sample-database-1", collection: ""}, actions: ["find"]
    }],
    roles: []
}
)
```

Output from this operation looks something like the following.

```
{
   "role":"findRole",
   "privileges":[
      {
         "resource":{
            "db":"sample-database-1",
            "collection":""
         },
         "actions":[
            "find"
         ]
      }
   ],
   "roles":[

   ]
}
```

Next, create the user (`user2`) and attach the recently created role
`findRole` to the user.

```
db.createUser(
{
    user: "user2",
    pwd: "abc123",
    roles: []
})

	db.grantRolesToUser("user2",["findRole"])
```

To simulate the scenario that `user3` is an existing user, first create the
user `user3`, and then create a new role called collectionRole which we will
in the next step assing to `user3`.

Now you can assign a new role to `user3`. This new role will allow
`user3` to be able to insert, update, delete and find access to one
specific collection col2 in `sample-database-2`.

```
db.createUser(
{
    user: "user3",
    pwd: "abc123",
    roles: []
})

db.createRole(
{
    role: "collectionRole",
    privileges: [
    {
        resource: {db: "sample-database-2", collection: "col2"}, actions: ["find", "update", "insert", "remove"]
    }],
    roles: []
}
)
```

Output from this operation looks something like the following.

```
{
   "role":"collectionRole",
   "privileges":[
      {
         "resource":{
            "db":"sample-database-2",
            "collection":"col2"
         },
         "actions":[
            "find",
            "update",
            "insert",
            "remove"
         ]
      }
   ],
   "roles":[

   ]
}
```

Now that the user `user3` has been created, you can grant
`user3` the role `collectionFind`.

```
db.grantRolesToUser("user3",["collectionRole"])
```

Lastly, both `user1` and `user2` leave the company and need
their access to the cluster revoked. You can do this by dropping the users, as
follows.

```
db.dropUser("user1")
db.dropUser("user2")
```

To ensure that all users have the appropriate roles, you can list all users with the
following command.

```
show users
```

Output from this operation looks something like the following.

```
{
   "_id":"serviceadmin",
   "user":"serviceadmin",
   "db":"admin",
   "roles":[
      {
         "db":"admin",
         "role":"root"
      }
   ]
}
{
   "_id":"master-user",
   "user":"master-user",
   "db":"admin",
   "roles":[
      {
         "db":"admin",
         "role":"root"
      }
   ]
}
{
   "_id":"user3",
   "user":"user3",
   "db":"admin",
   "roles":[
      {
         "db":"admin",
         "role":"collectionRole"
      }
   ]
}
```

## Connecting to Amazon DocumentDB as

a User

When connecting to an Amazon DocumentDB cluster, you connect in the context of a particular
database. By default, if you don't specify a database in your connection string, you are
automatically connected to the cluster in the context of the `test` database.
All collection level commands like `insert` and `find` are issued
against collections in the `test` database.

To see the database you are in the context of or — in other words —
issuing commands against, use the `db` command in the mongo shell, as
follows.

Query:

```
db
```

Output:

```
test
```

Although the default connection might be in the context of the `test`
database, that does not necessarily mean that the user associated with the connection is
authorized to perform actions on the `test` database. In the preceding
example scenario, if you authenticate as the user `user3`, which has the
`readWrite` role for the `sample-database-1` database, the
default context of your connection is the `test` database. However, if you
try to insert a document into a collection on the `test` database, you will
receive an _Authorization failure_ error message. This is because
that user is not authorized to perform that command on that database, as shown
below.

Query:

```
db
```

Output:

```
test
```

Query:

```
db.col.insert({x:1})
```

Output:

```
WriteCommandError({ "ok" : 0, "code" : 13, "errmsg" : "Authorization failure" })
```

If you change the context of your connection to the `sample-database-1`
database, you can write to the collection for which the user has the authorization to do
so.

Query:

```
use sample-database-1
```

Output:

```
switched to db sample-database-1
```

Query:

```
db.col.insert({x:1})
```

Output:

```
WriteResult({ "nInserted" : 1})
```

When you authenticate to a cluster with a particular user, you can also specify the
database in the connection string. Doing so removes the necessity to perform the
`use` command after the user has been authenticated to the
`admin` database.

The following connection string authenticates the user against the `admin`
database, but the context of the connection will be against the
`sample-database-1` database.

```
mongo "mongodb://user3:abc123@sample-cluster.node.us-east-1.docdb.amazonaws.com:27017/sample-database-2"
```

## Common commands

This section provides examples of common commands using role-based access control in
Amazon DocumentDB. You must be in the context of the `admin` database to create and
modify users and roles. You can use the `use admin` command to switch to the
`admin` database.

###### Note

Modifications to the users and roles will implicitly occur in the
`admin` database. Creating users with roles that are scoped across
all databases (for example, `readAnyDatabase`) requires that you are
either in the context of the `admin` database (that is, `use
 admin`) when creating the user, or you explicitly state the database for
the role when creating the user (as shown in Example 2 in this section).

**Example 1**: Create a user with `read` role for the
database `foo`.

```
db.createUser({user: "readInFooBar", pwd: "abc123", roles: [{role: "read", db: "foo"}]})
```

Output from this operation looks something like the following.

```
{
   "user":"readInFooBar",
   "roles":[
      {
         "role":"read",
         "db":"foo"
      }
   ]
}
```

**Example 2**: Create a user with read access on all
databases.

```
db.createUser({user: "readAllDBs", pwd: "abc123", roles: [{role: "readAnyDatabase", db: "admin"}]})
```

Output from this operation looks something like the following.

```
{
   "user":"readAllDBs",
   "roles":[
      {
         "role":"readAnyDatabase",
         "db":"admin"
      }
   ]
}
```

**Example 3**: Grant `read` role to an existing user on a
new database.

```
db.grantRolesToUser("readInFooBar", [{role: "read", db: "bar"}])
```

**Example 4**: Update a user's role.

```
db.updateUser("readInFooBar", {roles: [{role: "read", db: "foo"}, {role: "read", db: "baz"}]})
```

**Example 5**: Revoke access to a database for a user.

```
db.revokeRolesFromUser("readInFooBar", [{role: "read", db: "baz"}])
```

**Example 6**: Describe a built-in role.

```
db.getRole("read", {showPrivileges:true})
```

Output from this operation looks something like the following.

```
{
   "role":"read",
   "db":"sample-database-1",
   "isBuiltin":true,
   "roles":[

   ],
   "inheritedRoles":[

   ],
   "privileges":[
      {
         "resource":{
            "db":"sample-database-1",
            "collection":""
         },
         "actions":[
            "changeStream",
            "collStats",
            "dbStats",
            "find",
            "killCursors",
            "listCollections",
            "listIndexes"
         ]
      }
   ],
   "inheritedPrivileges":[
      {
         "resource":{
            "db":"sample-database-1",
            "collection":""
         },
         "actions":[
            "changeStream",
            "collStats",
            "dbStats",
            "find",
            "killCursors",
            "listCollections",
            "listIndexes"
         ]
      }
   }
```

**Example 7**: Drop a user from the cluster.

```
db.dropUser("readInFooBar")
```

Output from this operation looks something like the following.

```
true
```

**Example 8**: Create a role with read and write access to a specific
collection

```
db.createRole(
{
    role: "collectionRole",
    privileges: [
    {
        resource: {db: "sample-database-2", collection: "col2"}, actions: ["find", "update", "insert", "remove"]
    }],
    roles: []
}
)
```

Output from this operation looks something like the following.

```
{
   "role":"collectionRole",
   "privileges":[
      {
         "resource":{
            "db":"sample-database-2",
            "collection":"col2"
         },
         "actions":[
            "find",
            "update",
            "insert",
            "remove"
         ]
      }
   ],
   "roles":[

   ]
}
```

**Example 9**: Create a user and assign a user defined role

```
db.createUser(
{
    user: "user3",
    pwd: "abc123",
    roles: []
})

db.grantRolesToUser("user3",["collectionRole"])
```

**Example 10**: Grant additional privileges to a user defined role

```
db.grantPrivilegesToRole(
  "collectionRole",
  [
    {
      resource: { db: "sample-database-1", collection: "col1" },
      actions: ["find", "update", "insert", "remove"]
    }
  ]
)
```

**Example 11**: Remove privileges from a user defined role

```
db.revokePrivilegesFromRole(
  "collectionRole",
  [
    {
      resource: { db: "sample-database-1", collection: "col2" },
      actions: ["find", "update", "insert", "remove"]
    }
  ]
)
```

**Example 12**: Update an existing user defined role

```
db.updateRole(
  "collectionRole",
  {
    privileges: [
    {
        resource: {db: "sample-database-3", collection: "sample-collection-3"}, actions: ["find", "update", "insert", "remove"]
    }],
    roles: []
  }
)
```

## Functional differences

In Amazon DocumentDB, user and role definitions are stored in the `admin` database
and users are authenticated against the `admin` database. This functionality
differs from the MongoDB Community Edition, but is consistent with MongoDB Atlas.

Amazon DocumentDB also supports change streams, which provide a time-ordered sequence of change
events that occur within your cluster’s collections. The `listChangeStreams`
action is applied at the cluster level (that is, across all databases), and the
`modifyChangeStreams` action can be applied at the database level and
cluster level.

## Limits

The following table contains the limits for Role-Based Access Control in
Amazon DocumentDB.

| Description                                     | Limit |
| ----------------------------------------------- | ----- |
| Number of users per cluster                     | 1000  |
| Number of roles associated with a user          | 1000  |
| Number of user-defined roles                    | 100   |
| Number of resources associated with a privilege | 100   |

## Database access using Role-Based Access Control

With role-based access control, you can create a user and grant it one or more roles
to determine what operations that user can perform in a database or cluster.

The following is a list of built-in roles that are currently supported in
Amazon DocumentDB.

###### Note

In Amazon DocumentDB 4.0 and 5.0, the `ListCollection` and `ListDatabase`
commands can optionally use the `authorizedCollections` and
`authorizedDatabases` parameters to list the collections and
databases that the user has permission to access with requiring the
`listCollections` and `listDatabase` roles, respectively.
Also, users now have the ability to kill their own cursors without requiring the
`KillCursor` role.

Database user

| Role name   | Description                                                         | Actions                                                                                                                                                                                                   |
| ----------- | ------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `read`      | Grants a user read access to the specified database.                | `changeStreams`<br>`collStats`<br>`dbStats`<br>`find`<br>`killCursors`<br>`listIndexes`<br>`listCollections`                                                                                              |
| `readWrite` | Grants the user read and write access to the specified<br>database. | All actions from `read` permissions.<br>`createCollection`<br>`dropCollection`<br>`createIndex`<br>`dropIndex`<br>`insert`<br>`killCursors`<br>`listIndexes`<br>`listCollections`<br>`remove`<br>`update` |

Cluster user

| Role name              | Description                                                                                                       | Actions                                                                                                                                                          |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| readAnyDatabase        | Grants a user read access to all databases in the cluster.                                                        | All actions from `read` permissions.<br>`listChangeStreams`<br>`listDatabases`                                                                                   |
| `readWriteAnyDatabase` | Grants a user read and write access to all databases in the<br>cluster.                                           | All actions from `readWrite` permissions.<br>`listChangeStreams`<br>`listDatabases`                                                                              |
| `userAdminAnyDatabase` | Grants a user the ability to assign and modify the roles or<br>privileges any user has to the specified database. | `changeCustomData`<br>`changePassword`<br>`createUser`<br>`dropRole`<br>`dropUser`<br>`grantRole`<br>`listDatabases`<br>`revokeRole`<br>`viewRole`<br>`viewUser` |
| `dbAdminAnyDatabase`   | Grants a user the ability to perform database administration roles on<br>any specified database.                  | All actions from `dbAdmin` permissions.<br>`dropCollection`<br>`listDatabases`<br>`listChangeStreams`<br>`modifyChangeStreams`                                   |

Superuser

| Role name | Description                                                                                                                                                                                                          | Actions                                                                                                                                  |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `root`    | Grants a user access to the resources and operations of all the<br>following roles combined: `readWriteAnyDatabase`,<br>`dbAdminAnyDatabase`, `userAdminAnyDatabase`,<br>`clusterAdmin`, `restore`, and<br>`backup`. | All actions from `readWriteAnyDatabase`,<br>`dbAdminAnyDatabase`,<br>`userAdminAnyDatabase`, `clusterAdmin`,<br>`restore`, and `backup`. |

Database administrator

| Role name | Description                                                                                                                                     | Actions                                                                                                                                                                                                                                                   |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `dbAdmin` | Grants a user the ability to perform administrative tasks on the<br>specified database.                                                         | `bypassDocumentValidation`<br>`collMod`<br>`collStats`<br>`createCollection`<br>`createIndex`<br>`dropCollection`<br>`dropDatabase`<br>`dropIndex`<br>`dbStats`<br>`find`<br>`killCursors`<br>`listIndexes`<br>`listCollections`<br>`modifyChangeStreams` |
| `dbOwner` | Grants a user the ability to perform any administrative tasks on the<br>specified database by combining the roles `dbAdmin` and<br>`readWrite`. | All actions from `dbAdmin` and<br>`readWrite`.                                                                                                                                                                                                            |

Cluster administrator

| role Name        | Description                                                                                                                              | Actions                                                                                                                                                                                                                                                |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `clusterAdmin`   | Grants a user the greatest cluster management access by combining the<br>`clusterManager`, `clusterMonitor`, and<br>`hostManager` roles. | All actions from `clusterManager`,<br>`clusterMonitor`, and<br>`hostManager`.<br>`listChangeStreams`<br>`dropDatabase`<br>`modifyChangeStreams`                                                                                                        |
| `clusterManager` | Grants a user the ability to take management and monitoring actions<br>on the specified cluster.                                         | `listChangeStreams`<br>`listSessions`<br>`modifyChangeStreams`<br>`replSetGetConfig`                                                                                                                                                                   |
| `clusterMonitor` | Grants a user the ability to have read-only access to monitoring<br>tools.                                                               | `collStats`<br>`dbStats`<br>`find`<br>`getParameter`<br>`hostInfo`<br>`indexStats`<br>`killCursors`<br>`listChangeStreams`<br>`listCollections`<br>`listDatabases`<br>`listIndexes`<br>`listSessions`<br>`replSetGetConfig`<br>`serverStatus`<br>`top` |
| `hostManager`    | Grants a user the ability to monitor and manage servers.                                                                                 | `auditConfigure`<br>`killCursors`<br>`killAnyCursor`<br>`killAnySession`<br>`killop`                                                                                                                                                                   |

Backup administrator

| Role name | Description                                      | Actions                                                                                                                                                                                                                                                                                                                                                           |
| --------- | ------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `backup`  | Grants a user the access needed to back up data. | `getParameter`<br>`insert`<br>`find`<br>`listChangeStreams`<br>`listCollections`<br>`listDatabases`<br>`listIndexes`<br>`update`                                                                                                                                                                                                                                  |
| `restore` | Grants a user the access needed to restore data. | `bypassDocumentValidation`<br>`changeCustomData`<br>`changePassword`<br>`collMod`<br>`createCollection`<br>`createIndex`<br>`createUser`<br>`dropCollection`<br>`dropRole`<br>`dropUser`<br>`getParameter`<br>`grantRole`<br>`find`<br>`insert`<br>`listCollections`<br>`modifyChangeStreams`<br>`revokeRole`<br>`remove`<br>`viewRole`<br>`viewUser`<br>`update` |
