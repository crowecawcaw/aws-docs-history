# Viewing a proxy

After you create one or more RDS proxies, you can view and manage them in the
AWS Management Console, the AWS CLI, or the RDS API. You can review their configuration details, monitor
performance, and determine which proxies to modify or delete as needed.

To enable database applications to route traffic through a proxy, you must specify the
proxy endpoint in the connection string.

###### To view a proxy in the console

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Proxies**.
3. Select the proxy name to view its details.
4. On the details page, the **Target groups** section shows how
   the proxy is linked to a specific RDS DB
   instance. You can
   navigate to the default target group page for a deeper view of this association,
   including configuration settings defined during proxy creation. These settings
   include the maximum connection percentage, connection borrow timeout, engine family,
   and session pinning filters.
   To view your proxy using the CLI, use the [describe-db-proxies](../../../cli/latest/reference/rds/describe-db-proxies.md "../../../cli/latest/reference/rds/describe-db-proxies.md") command.
   By default, the request returns all proxies owned by your AWS account. To see details
   for a single proxy, specify its name with the `--db-proxy-name` parameter.

```
aws rds describe-db-proxies [--db-proxy-name `proxy_name`]
```

To view other information associated with the proxy, use the following commands.

```
aws rds describe-db-proxy-target-groups  --db-proxy-name `proxy_name`

aws rds describe-db-proxy-targets --db-proxy-name `proxy_name`
```

Use the following sequence of commands to see more detail about the things that are associated with the
proxy:

1. To get a list of proxies, run
   [describe-db-proxies](../../../cli/latest/reference/rds/describe-db-proxies.md "../../../cli/latest/reference/rds/describe-db-proxies.md").
2. To show connection parameters such as the maximum percentage of connections
   that the proxy can use, run [describe-db-proxy-target-groups](../../../cli/latest/reference/rds/describe-db-proxy-target-groups.md "../../../cli/latest/reference/rds/describe-db-proxy-target-groups.md")
   `--db-proxy-name`. Use the name of the proxy as the parameter value.
3. To see the details of the RDS DB
   instance associated
   with the returned target group, run [describe-db-proxy-targets](../../../cli/latest/reference/rds/describe-db-proxy-targets.md "../../../cli/latest/reference/rds/describe-db-proxy-targets.md").

To view your proxies using the RDS API, use the
[DescribeDBProxies](../APIReference/API_DescribeDBProxies.md "../APIReference/API_DescribeDBProxies.md")
operation. It returns values of the
[DBProxy](../APIReference/API_DBProxy.md "../APIReference/API_DBProxy.md") data
type.

To see details of the connection settings for the proxy, use the proxy identifiers from this return
value with the
[DescribeDBProxyTargetGroups](../APIReference/API_DescribeDBProxyTargetGroups.md "../APIReference/API_DescribeDBProxyTargetGroups.md")
operation. It returns values of the
[DBProxyTargetGroup](../APIReference/API_DBProxyTargetGroup.md "../APIReference/API_DBProxyTargetGroup.md")
data type.

To see the RDS instance or Aurora DB cluster associated with the proxy, use the
[DescribeDBProxyTargets](../APIReference/API_DescribeDBProxyTargets.md "../APIReference/API_DescribeDBProxyTargets.md")
operation. It returns values of the
[DBProxyTarget](../APIReference/API_DBProxyTarget.md "../APIReference/API_DBProxyTarget.md")
data type.
