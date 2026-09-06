

# Viewing a proxy
<a name="rds-proxy-viewing"></a>

 After you create one or more RDS proxies, you can view and manage them in the AWS Management Console, the AWS CLI, or the RDS API. You can review their configuration details, monitor performance, and determine which proxies to modify or delete as needed.

To enable database applications to route traffic through a proxy, you must specify the proxy endpoint in the connection string.

## Console
<a name="rds-proxy-viewing.console"></a>

**To view a proxy in the console**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Proxies**. 

1. Select the proxy name to view its details. 

1. On the details page, the **Target groups** section shows how the proxy is linked to a specific RDS DB instance. You can navigate to the default target group page for a deeper view of this association, including configuration settings defined during proxy creation. These settings include the maximum connection percentage, connection borrow timeout, engine family, and session pinning filters.

## CLI
<a name="rds-proxy-viewing.cli"></a>

 To view your proxy using the CLI, use the [describe-db-proxies](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-proxies.html) command. By default, the request returns all proxies owned by your AWS account. To see details for a single proxy, specify its name with the `--db-proxy-name` parameter. 

```
aws rds describe-db-proxies [--db-proxy-name {{proxy_name}}]
```

 To view other information associated with the proxy, use the following commands. 

```
aws rds describe-db-proxy-target-groups  --db-proxy-name {{proxy_name}}

aws rds describe-db-proxy-targets --db-proxy-name {{proxy_name}}
```

 Use the following sequence of commands to see more detail about the things that are associated with the proxy: 

1.  To get a list of proxies, run [describe-db-proxies](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-proxies.html). 

1.  To show connection parameters such as the maximum percentage of connections that the proxy can use, run [describe-db-proxy-target-groups](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-proxy-target-groups.html) `--db-proxy-name`. Use the name of the proxy as the parameter value. 

1.  To see the details of the RDS DB instance associated with the returned target group, run [describe-db-proxy-targets](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-proxy-targets.html). 

## RDS API
<a name="rds-proxy-viewing.api"></a>

 To view your proxies using the RDS API, use the [DescribeDBProxies](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBProxies.html) operation. It returns values of the [DBProxy](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DBProxy.html) data type. 

 To see details of the connection settings for the proxy, use the proxy identifiers from this return value with the [DescribeDBProxyTargetGroups](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBProxyTargetGroups.html) operation. It returns values of the [DBProxyTargetGroup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DBProxyTargetGroup.html) data type. 

 To see the RDS instance or Aurora DB cluster associated with the proxy, use the [DescribeDBProxyTargets](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBProxyTargets.html) operation. It returns values of the [DBProxyTarget](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DBProxyTarget.html) data type. 