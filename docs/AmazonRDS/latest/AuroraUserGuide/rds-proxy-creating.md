

# Creating a proxy for Amazon Aurora
<a name="rds-proxy-creating"></a>

You can use Amazon RDS Proxy to improve the scalability, availability, and security of your database applications by pooling connections and managing database failovers more efficiently. This topic walks you through creating a proxy. Before you start, make sure your database meets the necessary prerequisites, including IAM permissions and VPC configuration.

You can associate a proxy with an Aurora MySQL or Aurora PostgreSQL DB cluster. 

## Console
<a name="rds-proxy-creating.console"></a>

**To create a proxy**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Proxies**. 

1. Choose **Create proxy**. 

1. Configure the following settings for your proxy.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy-creating.html)

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

 RDS Proxy automatically creates a target group named `default` when you create each proxy. You associate an Aurora DB cluster with the target group by calling the function [RegisterDBProxyTargets](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RegisterDBProxyTargets.html). 

**Important**  
When you select **IAM authentication** for the default authentication scheme:  
You must enable IAM database authentication on your target database instances or clusters before the proxy can successfully connect.
If you choose **Create IAM role**, the **Database accounts for IAM authentication** field is required.
If you select an existing IAM role, the console does not automatically update the role with database connection permissions. Check that the role has the necessary `rds-db:connect` permissions.