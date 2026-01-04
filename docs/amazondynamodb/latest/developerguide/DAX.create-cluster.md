# DAX and IPv6

DynamoDB DAX now supports IPv6 addressing, that allows you to create clusters that
operate in IPv4-only, IPv6-only, or dual-stack networking modes. This helps in enhancing
networking capabilities to meet evolving infrastructure requirements.

**Network Types:**

You can create clusters with the following network types:

- IPv4-only
- IPv6-only
- Dual-stack (supports both IPv4 and IPv6)
  **Key Features:**

With IPv6 support, you can do the following:

- **Network configuration options:**
  - IPv4-only and dual-stack clusters on `dual_stack
subnets`.
  - IPv6-only clusters on IPv6-only subnets.

- **Subnet group management:**
  - Create subnet groups with IPv4-only, IPv6-only, or dual-stack
    support
  - Modify existing subnet groups with additional VPC subnets
  - Add IPv6-only subnets to IPv6-configured subnet groups
  - Add IPv4 or dual-stack subnets to IPv4 and dual-stack configured
    groups

- **Client configuration:**

      + When making data plane calls, you can set preferred IP protocol for
       dual\_stack clusters using:




      	- `ip_discovery` parameter in Python SDK
      	- `ipDiscovery` parameter in other SDKs
      + Default: IPv4 when protocol preference not specified

  Before implementing IPv6 in your DAX clusters, you must consider the following:

- Network type cannot be changed after cluster creation
- For dual-stack clusters, the `ip_discovery/ipDiscovery` parameter
  in the client configuration determines which IP protocol to use (IPv4 or
  IPv6)
- Different applications can connect to the same dual-stack cluster using
  different IP protocols based on their configuration

###### Example client configuration

```
DynamoDbAsyncClient client = ClusterDaxAsyncClient.builder()
        .overrideConfiguration(Configuration.builder()
            .url(endpoint)             // DAX cluster endpoint
            .ipDiscovery(ipDiscovery)       // IP discovery type (IPv4 or IPv6)
            .build())
        .build();
```

###### Important

When you use resource-based IAM policies to restrict IP addresses for DynamoDB tables
in IPv6-only environments with DAX, you must create an exception for your DAX
cluster's IAM role if you block the IPv4 address space
(`0.0.0.0/0`). Add an `ArnNotEquals` condition to your policy
that specifically allows access for the DAX cluster's IAM role while
maintaining IP-based restrictions for other access paths. Without this exception,
DAX cannot access your DynamoDB table.

For example:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Principal": "*",
 "Action": "dynamodb:PutItem",
 "Resource": "arn:aws:dynamodb:`us-east-1:123456789012`:table/`MusicCollection`",
 "Condition": {
 "ArnNotEquals": {
 "aws:PrincipalArn": "arn:aws:iam::`123456789012`:role/DAXServiceRoleForDynamoDBAccess"
 },
 "IpAddress": {
 "aws:SourceIp": "`0.0.0.0/0`"
 }
 }
 }
 ]
}`

```
