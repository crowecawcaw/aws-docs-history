# Modifying an RDS Proxy

You can change specific settings associated with a proxy after you create the proxy. You do so by modifying
the proxy itself, its associated target group, or both. Each proxy has an associated target group.

###### Important

The values in the **Client authentication type** and **IAM authentication** fields apply to all Secrets Manager secrets that
are associated with this proxy. To specify different values for each secret, modify your proxy by using the AWS CLI or the API instead.

###### To modify the settings for a proxy

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Proxies**.
3. In the list of proxies, choose the proxy whose settings you want to modify or go to its details
   page.
4. For **Actions**, choose **Modify**.
5. Enter or choose the properties to modify. You can modify the following:
   - **Proxy identifier** – Rename the proxy by entering a new identifier.
   - **Idle client connection timeout** – Enter a time period for the idle client connection timeout.
   - **IAM role** – Change the IAM role used to retrieve the secrets from Secrets Manager.

   ###### Note

   You can't create a new IAM role if you set **Default authentication scheme** to **IAM authentication**.
   - **Secrets Manager secrets** – Add or remove Secrets Manager secrets. These secrets correspond to database user names and passwords.
   - **Client authentication type** – Change the type of authentication for client connections to the proxy.
   - **IAM authentication** – Require or disallow IAM authentication for connections to the proxy.
   - **Default authentication scheme** – Change the default authentication scheme the
     proxy uses for client connections to the proxy and connections from the proxy to the underlying database.
   - **Require Transport Layer Security** – Turn the requirement for Transport layer Security (TLS) on or off.
   - **VPC security group** – Add or remove VPC security groups for the proxy to use.
   - **Enable enhanced logging** – Enable or disable enhanced logging.

6. Choose **Modify**.
   If you didn't find the settings listed that you want to change, use the
   following procedure to update the target group for the proxy. The _target group_ associated with a proxy controls the settings
   related to the physical database connections. Each proxy has one associated target group
   named `default`, which is created automatically along with the proxy. You
   can't rename the default target group.

You can only modify the target group from the proxy details page, not from the list on the
**Proxies** page.

###### To modify the settings for a proxy target group

1.  On the **Proxies** page, go to the details page for a proxy.
2.  For **Target groups**, choose the `default` link. Currently, all proxies
    have a single target group named `default`.
3.  On the details page for the **default** target group, choose
    **Modify**.
4.  Choose new settings for the properties that you can modify:
    - **Database** – Choose a different RDS DB instance or cluster.
    - **Connection pool maximum connections** – Adjust what percentage of the maximum available connections the proxy can use.
    - **Session pinning filters** – (Optional) Choose a session
      pinning filter. This circumvents
      the default safety measures for multiplexing database connections across client connections.
      Currently, the setting isn't supported for PostgreSQL. The only choice is
      `EXCLUDE_VARIABLE_SETS`.

    Enabling this setting can cause session variables of one connection to impact other
    connections. This can cause errors or correctness issues if your queries depend on
    session variable values set outside of the current transaction.
    Consider using this option after verifying it is safe for your applications to share
    database connections across client connections.

    The following patterns can be considered safe:

        + `SET` statements where there is no change to the effective
         session variable value, i.e., there is no change to the session variable.
        + You change the session variable value and execute a statement in the
         same transaction.

    For more information, see [Avoiding pinning an RDS Proxy](rds-proxy-pinning.md "rds-proxy-pinning.md").
    - **Connection borrow timeout** – Adjust the connection borrow timeout interval. This setting applies when the maximum number of
      connections is already being used for the proxy. The setting determines how long the proxy waits
      for a connection to become available before returning a timeout error.
    - **Initialization query**. (Optional) Add an initialization
      query, or modify the current one. You can specify one or more SQL statements for
      the proxy to run when opening each new database connection. The setting is
      typically used with `SET` statements to make sure that each
      connection has identical settings. Make sure that the query you add is valid. To
      include multiple variables in a single `SET` statement, use comma
      separators. For example:

    ```
    SET `variable1`=`value1`, `variable2`=`value2`
    ```

    For multiple statements, use semicolons as the separator.

You can't change certain properties, such as the target group identifier and the database engine. 5. Choose **Modify target group**.

To modify a proxy using the AWS CLI, use the commands
[modify-db-proxy](../../../cli/latest/reference/rds/modify-db-proxy.md "../../../cli/latest/reference/rds/modify-db-proxy.md"),
[modify-db-proxy-target-group](../../../cli/latest/reference/rds/modify-db-proxy-target-group.md "../../../cli/latest/reference/rds/modify-db-proxy-target-group.md"),
[deregister-db-proxy-targets](../../../cli/latest/reference/rds/deregister-db-proxy-targets.md "../../../cli/latest/reference/rds/deregister-db-proxy-targets.md"),
and
[register-db-proxy-targets](../../../cli/latest/reference/rds/register-db-proxy-targets.md "../../../cli/latest/reference/rds/register-db-proxy-targets.md").

With the `modify-db-proxy` command, you can change properties such as the following:

- The set of Secrets Manager secrets used by the proxy.
- Whether TLS is required.
- The idle client timeout.
- Whether to log additional information from SQL statements for debugging.
- The IAM role used to retrieve Secrets Manager secrets.
- The security groups used by the proxy.
- The default authentication scheme associated with the proxy.

The following example shows how to rename an existing proxy.

```
aws rds modify-db-proxy --db-proxy-name `the-proxy` --new-db-proxy-name `the_new_name`
```

To modify connection-related settings or rename the target group, use the
`modify-db-proxy-target-group` command. Currently, all proxies have a
single target group named `default`. When you work with this target group,
you specify the name of the proxy and `default` for the name of the target
group. You can't rename the default target group.

The following example shows how to first check the `MaxIdleConnectionsPercent` setting for a
proxy and then change it, using the target group.

```
aws rds describe-db-proxy-target-groups --db-proxy-name `the-proxy`

{
    "TargetGroups": [
        {
            "Status": "available",
            "UpdatedDate": "2019-11-30T16:49:30.342Z",
            "ConnectionPoolConfig": {
                **"MaxIdleConnectionsPercent": 50,**
                "ConnectionBorrowTimeout": 120,
                "MaxConnectionsPercent": 100,
                "SessionPinningFilters": []
            },
            "TargetGroupName": "default",
            "CreatedDate": "2019-11-30T16:49:27.940Z",
            "DBProxyName": "the-proxy",
            "IsDefault": true
        }
    ]
}

aws rds modify-db-proxy-target-group --db-proxy-name `the-proxy` --target-group-name default --connection-pool-config '
{ **"MaxIdleConnectionsPercent": 75** }'

{
    "DBProxyTargetGroup": {
        "Status": "available",
        "UpdatedDate": "2019-12-02T04:09:50.420Z",
        "ConnectionPoolConfig": {
            **"MaxIdleConnectionsPercent": 75,**
            "ConnectionBorrowTimeout": 120,
            "MaxConnectionsPercent": 100,
            "SessionPinningFilters": []
        },
        "TargetGroupName": "default",
        "CreatedDate": "2019-11-30T16:49:27.940Z",
        "DBProxyName": "the-proxy",
        "IsDefault": true
    }
}
```

With the `deregister-db-proxy-targets` and
`register-db-proxy-targets` commands, you change which RDS DB instances
the proxy is associated with through its target group. Currently, each
proxy can connect to one RDS DB instance.
The target group tracks the connection details for all the
RDS DB instances in a Multi-AZ configuration.

The following example starts with a proxy that is associated with an Aurora MySQL cluster named
`cluster-56-2020-02-25-1399`. The example shows how to change the proxy so that it can
connect to a different cluster named `provisioned-cluster`.

When you work with an RDS DB instance, you specify the `--db-instance-identifier` option.

The following example modifies an Aurora MySQL proxy. An Aurora PostgreSQL proxy has port 5432.

```
aws rds describe-db-proxy-targets --db-proxy-name `the-proxy`

{
    "Targets": [
        {
            "Endpoint": "instance-9814.demo.us-east-1.rds.amazonaws.com",
            "Type": "RDS_INSTANCE",
            "Port": 3306,
            "RdsResourceId": "instance-9814"
        },
        {
            "Endpoint": "instance-8898.demo.us-east-1.rds.amazonaws.com",
            "Type": "RDS_INSTANCE",
            "Port": 3306,
            "RdsResourceId": "instance-8898"
        },
        {
            "Endpoint": "instance-1018.demo.us-east-1.rds.amazonaws.com",
            "Type": "RDS_INSTANCE",
            "Port": 3306,
            "RdsResourceId": "instance-1018"
        },
        {
            "Type": "**TRACKED\_CLUSTER**",
            "Port": 0,
            "RdsResourceId": "**cluster-56-2020-02-25-1399**"
        },
        {
            "Endpoint": "instance-4330.demo.us-east-1.rds.amazonaws.com",
            "Type": "RDS_INSTANCE",
            "Port": 3306,
            "RdsResourceId": "instance-4330"
        }
    ]
}

aws rds deregister-db-proxy-targets --db-proxy-name `the-proxy` **--db-cluster-identifier cluster-56-2020-02-25-1399**

aws rds describe-db-proxy-targets --db-proxy-name `the-proxy`

{
    "Targets": []
}

aws rds register-db-proxy-targets --db-proxy-name `the-proxy` **--db-cluster-identifier provisioned-cluster**

{
    "DBProxyTargets": [
        {
            "Type": "**TRACKED\_CLUSTER**",
            "Port": 0,
            "RdsResourceId": "**provisioned-cluster**"
        },
        {
            "Endpoint": "gkldje.demo.us-east-1.rds.amazonaws.com",
            "Type": "RDS_INSTANCE",
            "Port": 3306,
            "RdsResourceId": "gkldje"
        },
        {
            "Endpoint": "provisioned-1.demo.us-east-1.rds.amazonaws.com",
            "Type": "RDS_INSTANCE",
            "Port": 3306,
            "RdsResourceId": "provisioned-1"
        }
    ]
}
```

To modify a proxy using the RDS API, you use the operations
[ModifyDBProxy](../APIReference/API_ModifyDBProxy.md "../APIReference/API_ModifyDBProxy.md"),
[ModifyDBProxyTargetGroup](../APIReference/API_ModifyDBProxyTargetGroup.md "../APIReference/API_ModifyDBProxyTargetGroup.md"),
[DeregisterDBProxyTargets](../APIReference/API_DeregisterDBProxyTargets.md "../APIReference/API_DeregisterDBProxyTargets.md"),
and
[RegisterDBProxyTargets](../APIReference/API_RegisterDBProxyTargets.md "../APIReference/API_RegisterDBProxyTargets.md")
operations.

With `ModifyDBProxy`, you can change properties such as the following:

- The set of Secrets Manager secrets used by the proxy.
- Whether TLS is required.
- The idle client timeout.
- Whether to log additional information from SQL statements for debugging.
- The IAM role used to retrieve Secrets Manager secrets.
- The security groups used by the proxy.
  With `ModifyDBProxyTargetGroup`, you can modify connection-related
  settings. Currently, all proxies have a single target group named `default`.
  When you work with this target group, you specify the name of the proxy and
  `default` for the name of the target group. You can't rename the default
  target group.

With `DeregisterDBProxyTargets` and `RegisterDBProxyTargets`, you change which
RDS DB instance the proxy is associated with through its target group. Currently, each
proxy can connect to one RDS DB instance
. The target group tracks the connection
details for the RDS DB instances in a Multi-AZ configuration
.
