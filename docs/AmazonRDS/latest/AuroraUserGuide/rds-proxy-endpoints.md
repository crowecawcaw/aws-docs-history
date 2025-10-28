# Creating a proxy endpoint

To create a proxy endpoint, follow these instructions:

###### To create a proxy endpoint

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Proxies**.
3. Click the name of the proxy that you want to create a new endpoint for.

The details page for that proxy appears. 4. In the **Proxy endpoints** section, choose **Create proxy
endpoint**.

The **Create proxy endpoint** window appears. 5. For **Proxy endpoint name**, enter a descriptive name of your choice. 6. For **Target role**, choose whether to make the endpoint read/write or read-only.

Connections that use read/write endpoints can perform any kind of operations, such as data definition language
(DDL) statements, data manipulation language (DML) statements, and queries. These endpoints always
connect to the primary instance of the Aurora cluster. You can use read/write endpoints for general
database operations when you only use a single endpoint in your application. You can also use
read/write endpoints for administrative operations, online transaction processing (OLTP) applications,
and extract-transform-load (ETL) jobs.

Connections that use a read-only endpoint can only perform queries. When there are multiple reader
instances in the Aurora cluster, RDS Proxy can use a different reader instance for each connection to the
endpoint. That way, a query-intensive application can take advantage of Aurora's clustering
capability. You can add more query capacity to the cluster by adding more reader DB instances. These
read-only connections don't impose any overhead on the primary instance of the cluster. That way,
your reporting and analysis queries don't slow down the write operations of your OLTP
applications. 7. For **Virtual Private Cloud (VPC)**, choose the default to
access the endpoint from the same EC2 instances or other resources that normally use to access the proxy or its associated database. To set up cross-VPC
access for this proxy, choose a VPC other than the default. For more information about
cross-VPC access, see [Accessing Aurora databases across VPCs](rds-proxy-endpoints.md#rds-proxy-cross-vpc "rds-proxy-endpoints.md#rds-proxy-cross-vpc"). 8. For **Endpoint network type**, choose the IP version for the proxy endpoint. The available options are:

    * **IPv4** – The proxy endpoint uses IPv4 addresses only (default).
    * **IPv6** – The proxy endpoint uses IPv6 addresses only.
    * **Dual-stack** – The proxy endpoint supports both IPv4 and IPv6 addresses.

To use IPv6 or dual-stack, your VPC and subnets must be configured to support the selected network type. 9. For **Subnets**, RDS Proxy fills in the same subnets as the
associated proxy by default. To restrict access to the endpoint to only a portion of
the VPC's address range being able to connect to it, remove one or more subnets. 10. For **VPC security group**, you can choose an existing security
group or create a new one. RDS Proxy fills in the same security group or groups as the
associated proxy by default. If the inbound and outbound rules for the proxy are
appropriate for this endpoint, then keep the default choice.

If you choose to create a new security group, specify a name for the security group on this page. Then
edit the security group settings from the EC2 console later. 11. Choose **Create proxy endpoint**.

To create a proxy endpoint, use the AWS CLI
[create-db-proxy-endpoint](../../../cli/latest/reference/rds/create-db-proxy-endpoint.md "../../../cli/latest/reference/rds/create-db-proxy-endpoint.md") command.

Include the following required parameters:

- `--db-proxy-name `value``
- `--db-proxy-endpoint-name `value``
- `--vpc-subnet-ids `list_of_ids``. Separate the subnet IDs with
  spaces. You don't specify the ID of the VPC itself.

You can also include the following optional parameters:

- `--target-role { READ_WRITE | READ_ONLY }`. This parameter defaults to
  `READ_WRITE`. The `READ_ONLY` value
  affects only Aurora provisioned clusters that contain one or more reader DB
  instances. When the proxy is associated with an Aurora cluster that only
  contains a writer DB instance, you can't specify `READ_ONLY`. For more
  information about the intended use of read-only endpoints with Aurora clusters, see
  [Using reader endpoints with Aurora clusters](rds-proxy-endpoints.md#rds-proxy-endpoints-reader "rds-proxy-endpoints.md#rds-proxy-endpoints-reader")
  .
- `--vpc-security-group-ids `value``. Separate the security group
IDs with spaces. If you omit this parameter, RDS Proxy uses the default security group for the VPC.
RDS Proxy determines the VPC based on the subnet IDs that you specify for the
`--vpc-subnet-ids` parameter.
- `--endpoint-network-type { IPV4 | IPV6 | DUAL }`. This parameter specifies the IP version for the proxy endpoint. The default is `IPV4`. To use `IPV6` or `DUAL`, your VPC and subnets must be configured to support the selected network type.

###### Example

The following example creates a proxy endpoint named `my-endpoint`.

For Linux, macOS, or Unix:

```
aws rds create-db-proxy-endpoint \
  --db-proxy-name `my-proxy` \
  --db-proxy-endpoint-name `my-endpoint` \
  --vpc-subnet-ids `subnet_id` `subnet_id` `subnet_id` ... \
  --target-role READ_ONLY \
  --vpc-security-group-ids `security_group_id` \
  --endpoint-network-type DUAL

```

For Windows:

```
aws rds create-db-proxy-endpoint ^
  --db-proxy-name `my-proxy` ^
  --db-proxy-endpoint-name `my-endpoint` ^
  --vpc-subnet-ids `subnet_id_1` `subnet_id_2` `subnet_id_3` ... ^
  --target-role READ_ONLY ^
  --vpc-security-group-ids `security_group_id` ^
  --endpoint-network-type DUAL

```

To create a proxy endpoint, use the RDS API
[CreateDBProxyEndpoint](../APIReference/API_CreateDBProxyEndpoint.md "../APIReference/API_CreateDBProxyEndpoint.md") action.
