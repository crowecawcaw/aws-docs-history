

# Creating a proxy for Amazon RDS
<a name="rds-proxy-creating"></a>

You can associate a proxy with an RDS for MariaDB, RDS for Microsoft SQL Server, RDS for MySQL, or RDS for PostgreSQL DB instance. 

## Console
<a name="rds-proxy-creating.console"></a>

**To create a proxy**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Proxies**. 

1. Choose **Create proxy**. 

1. Configure the following settings for your proxy.


<table>
<thead>
  <tr><th>Setting</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td><b>Engine family</b></td><td>The database network protocol the proxy recognizes when it interprets network traffic to and from the database.  To use RDS for PostgreSQL, make sure to retain the <code>postgres</code> database in your instance. See <a href="rds-proxy.troubleshooting.md#rds-proxy-PostgreSQL-troubleshooting.postgresDBDelete">Troubleshooting deleted `postgres` database</a>.  </td></tr>
  <tr><td><b>Proxy identifier</b></td><td>A name that is unique within your AWS account ID and current AWS Region. </td></tr>
  <tr><td><b>Idle client connection timeout</b></td><td>The proxy closes a client connection if it remains idle for a set period. By default, this is 1,800 seconds (30 minutes). A connection is idle when the application doesn’t submit a new request within the specified time after completing the previous request. The proxy keeps the underlying database connection open and returns it to the connection pool, making it available for new client connections.<br />To proactively remove stale connections, reduce the idle client connection timeout. To minimize connection costs during workload spikes, increase the timeout.</td></tr>
  <tr><td><b>Database</b></td><td>The RDS DB instance to access through this proxy. The list only includes DB instances and clusters with compatible database engines, engine versions, and other settings. If the list is empty, create a new DB instance or cluster that's compatible with RDS Proxy. To do so, follow the procedure in <a href="USER_CreateDBInstance.md">Creating an Amazon RDS DB instance</a>. Then, try creating the proxy again. </td></tr>
  <tr><td><b>Connection pool maximum connections</b></td><td>A value between 1 and 100 to define the percentage of the <code>max_connections</code> limit that RDS Proxy can use. If you only intend to use one proxy with this DB instance or cluster, set this value to 100. For more information about how RDS Proxy uses this setting, see <a href="rds-proxy-connections.md#rds-proxy-connection-pooling-tuning.maxconnectionspercent">MaxConnectionsPercent</a>.</td></tr>
  <tr><td><b>Session pinning filters</b></td><td>Prevents RDS Proxy from pinning certain detected session states, which bypasses default safety measures for multiplexing connections. Currently, PostgreSQL doesn't support this setting, and the only available option is <code>EXCLUDE_VARIABLE_SETS</code>. Enabling it might cause session variables from one connection to affect others, leading to errors or correctness issues if queries rely on session variables set outside the current transaction. Use this option only after confirming that your applications can safely share database connections.<br />The following patterns are considered safe:<ul><li> <code>SET</code> statements where there is no change to the effective session variable value. In other words, there is no change to the session variable. </li><li> You change the session variable value and execute a statement in the same transaction. </li></ul><br />For more information, see <a href="rds-proxy-pinning.md">Avoiding pinning an RDS Proxy</a>.</td></tr>
  <tr><td><b>Connection borrow timeout</b></td><td>If you expect the proxy to use all available database connections, set the wait time before it returns a timeout error. You can specify up to five minutes. This setting applies only when the proxy has reached the maximum number of connections and all are in use.</td></tr>
  <tr><td><b>Initialization query</b></td><td>(Optional) Add an initialization query, or modify the current one. You can specify one or more SQL statements for the proxy to run when opening each new database connection. The setting is typically used with <code>SET</code> statements to make sure that each connection has identical settings. Make sure that the query you add is valid. To include multiple variables in a single <code>SET</code> statement, use comma separators. For example:<pre>SET {{variable1}}={{value1}}, {{variable2}}={{value2}}</pre><br />For multiple statements, use semicolons as the separator. Since you can access initialization query as part of target group configuration, it is not protected by authentication or cryptographic methods. Anyone with access to view or manage your proxy target group configuration can view the initialization query. You should not add sensitive data, such as passwords or long-lived encryption keys, to this option. </td></tr>
  <tr><td><b>AWS Identity and Access Management (IAM) role</b></td><td>An IAM role with permission to access the Secrets Manager secrets, which represent the credentials for database user accounts that the proxy can use. Alternatively, you can create a new IAM role from the AWS Management Console. If role manager is enabled in your account, Amazon RDS attaches the role for you, and the role options described here are replaced by a <b>Customize</b> option. To use a different role, choose <b>Customize</b>. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html">IAM role creation</a> in the <i>IAM User Guide</i>. </td></tr>
  <tr><td><b>Secrets Manager secrets</b></td><td>Create or choose Secrets Manager secrets representing the credentials for database users accounts that can use the proxy.<br />When <b>Default authentication scheme</b> is set to <b>None</b>, this field is required. When <b>Default authentication scheme</b> is set to <b>IAM authentication</b>, this field becomes optional and is marked as such in the console.<br />You can choose one or more secrets from the dropdown or create a new secret using the <b>Create a new secret</b> link.</td></tr>
  <tr><td><b>Client authentication type</b></td><td>The type of authentication the proxy uses for connections from clients. Your choice applies to all Secrets Manager secrets that you associate with this proxy. If you need to specify a different client authentication type for each secret, create your proxy by using the AWS CLI or the API instead. Specify this option only when your client connection uses database credentials for authentication.</td></tr>
  <tr><td><b>IAM authentication</b></td><td>Specify <b>Required</b>, <b>Allowed</b>, or <b>Not Allowed</b> for IAM authentication for connections to your proxy. The <b>Allowed</b> option is only valid for proxies for RDS for SQL Server. Your choice applies to all Secrets Manager secrets that you associate with this proxy. If you need to specify a different IAM authentication for each secret, create your proxy by using the AWS CLI or the API instead. </td></tr>
  <tr><td><b>Default authentication scheme</b></td><td>Choose the default type of authentication that the proxy uses for client connections to the proxy and the connections from the proxy to the underlying database. You have the following options:<ul><li><b>None</b> (default) - The proxy retrieves database credentials from Secrets Manager secrets.</li><li><b>IAM authentication</b> - The proxy uses IAM authentication to connect to the database, enabling end-to-end IAM authentication.</li></ul><br />When you select <b>IAM authentication</b>, an information alert appears reminding you to enable IAM database authentication for the databases in the target group configuration. This option is supported for MySQL, PostgreSQL, and MariaDB engine families only. </td></tr>
  <tr><td><b>Database accounts for IAM authentication</b></td><td>This field appears only when <b>Default authentication scheme</b> is set to <b>IAM authentication</b> and <b>Identity and access management (IAM) role</b> is set to <b>Create IAM role</b>.<br />Name the database user accounts for the proxy to use with IAM authentication. This is a required field. Specify multiple accounts by:<ul><li>Typing a database user name to add it as a tag</li><li>Using specific database user names (for example, <code>db_user</code>, <code>jane_doe</code>)</li><li>Using wildcard patterns for multiple users (for example, <code>db_test_*</code>)</li></ul><br />Each account appears as a removable tag that you can delete by clicking the X icon. The console uses these values to create the appropriate <code>rds-db:connect</code> permissions in the IAM role policy.</td></tr>
  <tr><td><b>Require Transport Layer Security</b></td><td>Enforces TLS/SSL for all client connections. The proxy uses the same encryption setting for its connection to the underlying database, whether the client connection is encrypted or unencrypted.</td></tr>
  <tr><td><b>Target connection network type</b></td><td>The IP version that the proxy uses to connect to the target database. Choose from the following options:<ul><li> <b>IPv4</b> – The proxy connects to the database using IPv4 addresses. </li><li> <b>IPv6</b> – The proxy connects to the database using IPv6 addresses. </li></ul><br />The default is IPv4. To use IPv6, your database must support dual-stack mode. Dual-stack mode is not available for target connections.</td></tr>
  <tr><td><b>Endpoint network type</b></td><td>The IP version for the proxy endpoint that clients use to connect to the proxy. Choose from the following options:<ul><li> <b>IPv4</b> – The proxy endpoint uses IPv4 addresses only. </li><li> <b>IPv6</b> – The proxy endpoint uses IPv6 addresses only. </li><li> <b>Dual-stack</b> – The proxy endpoint supports both IPv4 and IPv6 addresses. </li></ul><br />The default is IPv4. To use IPv6 or dual-stack, your VPC and subnets must be configured to support the selected network type.</td></tr>
  <tr><td><b>Subnets</b></td><td>This field is prepopulated with all subnets associated with your VPC. You can remove any subnets not needed for the proxy, but you must leave at least two subnets. For IPv6 or dual-stack endpoint network types, ensure that the selected subnets support the chosen network type.</td></tr>
  <tr><td><b>VPC security group</b></td><td>Choose an existing VPC security group or create a new one from the AWS Management Console. Configure the inbound rules to allow your applications to access the proxy and the outbound rules to permit traffic from your database targets. The security group must allow connections from the proxy to the database. It serves both for ingress from your applications to the proxy and egress from the proxy to the database. For example, if you use the same security group for both the database and the proxy, make sure that resources within that security group can communicate with each other. <br />When you use a shared VPC, avoid using the default security group for the VPC or one associated with another account. Instead, select a security group that belongs to your account. If none exists, create one. For more information, see <a href="https://docs.aws.amazon.com/vpc/latest/userguide/vpc-sharing.html#vpc-share-limitations"> Work with shared VPCs</a>.  <br />RDS deploys a proxy across multiple Availability Zones to ensure high availability. To enable cross-AZ communication, the network access control list (ACL) for your proxy subnet must allow egress on the engine port and ingress on all ports. For more information about network ACLs, see <a href="https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html">Control traffic to subnets using network ACLs</a>. If the network ACL for your proxy and target are identical, you must add a <b>TCP</b> protocol ingress rule where the <b>Source</b> is set to the VPC CIDR. You must also add an engine port specific <b>TCP</b> protocol egress rule where the <b>Destination</b> is set to the VPC CIDR.</td></tr>
  <tr><td><b>Activate enhanced logging</b></td><td>Enable this setting to troubleshoot proxy compatibility or performance issues. When enabled, RDS Proxy logs detailed performance information to help you debug SQL behavior or proxy connection performance and scalability. <br />Only enable this setting for debugging and ensure proper security measures are in place to protect sensitive information in the logs. To minimize overhead, RDS Proxy automatically disables this setting 24 hours after activation. Use it temporarily to troubleshoot specific issues.</td></tr>
</tbody>
</table>


1.  Choose **Create proxy**. 

## AWS CLI
<a name="rds-proxy-creating.CLI"></a>

 To create a proxy by using the AWS CLI, call the [create-db-proxy](https://docs.aws.amazon.com/cli/latest/reference/rds/create-db-proxy.html) command with the following required parameters: 
+ `--db-proxy-name`
+ `--engine-family`
+ `--role-arn`
+ `--vpc-subnet-ids`

The `--engine-family` value is case-sensitive.

**Example**  
For Linux, macOS, or Unix:  

```
aws rds create-db-proxy \
    --db-proxy-name {{proxy_name}} \
    --engine-family { MYSQL | POSTGRESQL | SQLSERVER } \
    --role-arn {{iam_role}} \
    --vpc-subnet-ids {{space_separated_list}} \
    [--default-auth-scheme { NONE | IAM_AUTH }] \
    [--auth {{ProxyAuthenticationConfig_JSON_string}}] \
    [--vpc-security-group-ids {{space_separated_list}}] \
    [--require-tls | --no-require-tls] \
    [--idle-client-timeout {{value}}] \
    [--debug-logging | --no-debug-logging] \
    [--endpoint-network-type { IPV4 | IPV6 | DUAL }] \
    [--target-connection-network-type { IPV4 | IPV6 }] \
    [--tags {{comma_separated_list}}]
```
For Windows:  

```
aws rds create-db-proxy ^
    --db-proxy-name {{proxy_name}} ^
    --engine-family { MYSQL | POSTGRESQL | SQLSERVER } ^
    --role-arn {{iam_role}} ^
    --vpc-subnet-ids {{space_separated_list}} ^
    [--default-auth-scheme { NONE | IAM_AUTH }] ^
    [--auth {{ProxyAuthenticationConfig_JSON_string}}] ^
    [--vpc-security-group-ids {{space_separated_list}}] ^
    [--require-tls | --no-require-tls] ^
    [--idle-client-timeout {{value}}] ^
    [--debug-logging | --no-debug-logging] ^
    [--endpoint-network-type { IPV4 | IPV6 | DUAL }] ^
    [--target-connection-network-type { IPV4 | IPV6 }] ^
    [--tags {{comma_separated_list}}]
```

The following is an example of the JSON value for the `--auth` option. This example applies a different client authentication type to each secret.

```
[
  {
    "Description": "proxy description 1",
    "AuthScheme": "SECRETS",
    "SecretArn": "arn:aws:secretsmanager:us-west-2:123456789123:secret/1234abcd-12ab-34cd-56ef-1234567890ab",
    "IAMAuth": "DISABLED",
    "ClientPasswordAuthType": "POSTGRES_SCRAM_SHA_256"
  },
  
  {
    "Description": "proxy description 2",
    "AuthScheme": "SECRETS",
    "SecretArn": "arn:aws:secretsmanager:us-west-2:111122223333:secret/1234abcd-12ab-34cd-56ef-1234567890cd",
    "IAMAuth": "DISABLED",
    "ClientPasswordAuthType": "POSTGRES_MD5"
    
  },
  
  {
    "Description": "proxy description 3",
    "AuthScheme": "SECRETS",
    "SecretArn": "arn:aws:secretsmanager:us-west-2:111122221111:secret/1234abcd-12ab-34cd-56ef-1234567890ef",
    "IAMAuth": "REQUIRED"
  }
  
]
```

The `--endpoint-network-type` parameter specifies the IP version for the proxy endpoint that clients use to connect to the proxy. Valid values are:
+ `IPV4` – The proxy endpoint uses IPv4 addresses only (default).
+ `IPV6` – The proxy endpoint uses IPv6 addresses only.
+ `DUAL` – The proxy endpoint supports both IPv4 and IPv6 addresses.

The `--target-connection-network-type` parameter specifies the IP version that the proxy uses to connect to the target database. Valid values are:
+ `IPV4` – The proxy connects to the database using IPv4 addresses (default).
+ `IPV6` – The proxy connects to the database using IPv6 addresses.

To use IPv6 or dual-stack endpoint network types, your VPC and subnets must be configured to support the selected network type. To use IPv6 target connection network type, your database must support dual-stack mode.

**Tip**  
 If you don't already know the subnet IDs to use for the `--vpc-subnet-ids` parameter, see [Setting up network prerequisites for RDS Proxy](rds-proxy-network-prereqs.md) for examples of how to find them. 

**Note**  
The security group must allow access to the database the proxy connects to. The same security group is used for ingress from your applications to the proxy, and for egress from the proxy to the database. For example, suppose that you use the same security group for your database and your proxy. In this case, make sure that you specify that resources in that security group can communicate with other resources in the same security group.  
When using a shared VPC, you can't use the default security group for the VPC, or one that belongs to another account. Choose a security group that belongs to your account. If one doesn't exist, create one. For more information about this limitation, see [Work with shared VPCs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-sharing.html#vpc-share-limitations). 

 To create the right associations for the proxy, you also use the [register-db-proxy-targets](https://docs.aws.amazon.com/cli/latest/reference/rds/register-db-proxy-targets.html) command. Specify the target group name `default`. RDS Proxy automatically creates a target group with this name when you create each proxy. 

```
aws rds register-db-proxy-targets
    --db-proxy-name {{value}}
    [--target-group-name {{target_group_name}}]
    [--db-instance-identifiers {{space_separated_list}}]  # rds db instances, or
    [--db-cluster-identifiers {{cluster_id}}]        # rds db cluster (all instances)
```

## RDS API
<a name="rds-proxy-creating.API"></a>

 To create an RDS proxy, call the Amazon RDS API operation [CreateDBProxy](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBProxy.html). You pass a parameter with the [AuthConfig](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_AuthConfig.html) data structure. 

 RDS Proxy automatically creates a target group named `default` when you create each proxy. You associate an RDS DB instance with the target group by calling the function [RegisterDBProxyTargets](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RegisterDBProxyTargets.html). 

**Important**  
When you select **IAM authentication** for the default authentication scheme:  
You must enable IAM database authentication on your target database instances or clusters before the proxy can successfully connect.
If you choose **Create IAM role**, the **Database accounts for IAM authentication** field is required.
If you select an existing IAM role, the console does not automatically update the role with database connection permissions. Check that the role has the necessary `rds-db:connect` permissions.