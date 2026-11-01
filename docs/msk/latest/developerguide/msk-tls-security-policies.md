

# TLS security policies for Amazon MSK
<a name="msk-tls-security-policies"></a>

Amazon MSK encrypts data in transit using TLS. By default, Amazon MSK clusters use TLS 1.2. To use TLS 1.3, you select a TLS security policy. The policy determines the following for your cluster:
+ The TLS protocol versions that Amazon MSK accepts.
+ The cipher suites that Amazon MSK can use to encrypt the connection.

A policy applies to every encrypted link that Amazon MSK manages, not only client connections. On clusters in KRaft mode, this covers client-to-broker, broker-to-broker replication, broker-to-controller, and the controller quorum. On clusters in ZooKeeper mode, it covers client-to-broker, broker-to-broker replication, broker-to-ZooKeeper, and the ZooKeeper quorum.

**Note**  
Selecting a security policy is optional. A cluster with no policy set keeps its current TLS configuration, which is referred to as `MSK-TLS1.2-Default-2026`. Nothing changes until you apply a policy.

**Topics**
+ [Prerequisites](#msk-tls-security-policies-prerequisites)
+ [Available security policies](#msk-tls-security-policies-available)
+ [Moving between policies](#msk-tls-security-policies-moving)
+ [Before you apply a policy](#msk-tls-security-policies-before)
+ [Apply a security policy](#msk-tls-security-policies-apply)
+ [View the current policy](#msk-tls-security-policies-view)
+ [Roll back a security policy](#msk-tls-security-policies-rollback)
+ [Troubleshooting](#msk-tls-security-policies-troubleshooting)

## Prerequisites
<a name="msk-tls-security-policies-prerequisites"></a>

Before you apply a TLS security policy, confirm the following:
+ Your cluster is an Amazon MSK Provisioned cluster. TLS security policies aren't available on Amazon MSK Serverless.
+ Your cluster runs Apache Kafka version 3.6 or later.
+ Your cluster is in the `ACTIVE` state, with no other operation in progress. Amazon MSK runs one cluster operation at a time.
+ You have permission to create or update an Amazon MSK configuration and to update the configuration of your cluster. You apply a policy through a configuration revision, and nothing else about the cluster needs to change.
+ If you're updating an existing cluster, the policy that you want is next to the current policy of your cluster in the policy order. You can't move from `MSK-TLS1.2-Default-2026` to `MSK-TLSv1.3-Only-2026` in a single step. For more information, see [Moving between policies](#msk-tls-security-policies-moving).

## Available security policies
<a name="msk-tls-security-policies-available"></a>

The following table describes the TLS security policies that Amazon MSK offers.


| Policy | Description | 
| --- | --- | 
| MSK-TLS1.2-Default-2026 | The default. Accepts TLS 1.2 only. Every Amazon MSK cluster uses this configuration unless you select another policy. | 
| MSK-TLSv1.3-2026 | Accepts TLS 1.2 and TLS 1.3. This policy is additive. It adds TLS 1.3 and removes no TLS 1.2 cipher suite. Each connection negotiates the highest version that the client supports. If a client negotiates TLS 1.3 and the handshake fails, the connection does not fall back to TLS 1.2. | 
| MSK-TLSv1.3-Only-2026 | Accepts TLS 1.3 only. Amazon MSK rejects connections that can't negotiate TLS 1.3. | 

Policy names are case sensitive and must match exactly.

### Supported protocols
<a name="msk-tls-security-policies-protocols"></a>

The following table shows which TLS protocol versions each policy supports.


| Protocol | `MSK-TLS1.2-Default-2026` | `MSK-TLSv1.3-2026` | `MSK-TLSv1.3-Only-2026` | 
| --- | --- | --- | --- | 
| TLS 1.3 | No | Yes | Yes | 
| TLS 1.2 | Yes | Yes | No | 

### Supported TLS 1.3 cipher suites
<a name="msk-tls-security-policies-tls13-ciphers"></a>

The following table shows which TLS 1.3 cipher suites each policy supports.


| Cipher suite | `MSK-TLS1.2-Default-2026` | `MSK-TLSv1.3-2026` | `MSK-TLSv1.3-Only-2026` | 
| --- | --- | --- | --- | 
| TLS\_AES\_128\_GCM\_SHA256 | No | Yes | Yes | 
| TLS\_AES\_256\_GCM\_SHA384 | No | Yes | Yes | 

**Important**  
Amazon MSK does not support `TLS_CHACHA20_POLY1305_SHA256`. A client that offers only this suite for TLS 1.3 can't complete a TLS 1.3 handshake with Amazon MSK. Most Apache Kafka clients offer the AES-GCM suites in the preceding table by default.

### Supported TLS 1.2 cipher suites
<a name="msk-tls-security-policies-tls12-ciphers"></a>

The following table shows which TLS 1.2 cipher families each policy supports. The number in parentheses is how many cipher suites Amazon MSK supports in that family.


| Cipher family (TLS 1.2) | `MSK-TLS1.2-Default-2026` | `MSK-TLSv1.3-2026` | `MSK-TLSv1.3-Only-2026` | 
| --- | --- | --- | --- | 
| ECDHE (ECDSA/RSA) AES-GCM (4) | Yes | Yes | No | 
| ECDH static (ECDSA/RSA) AES-GCM (4) | Yes | Yes | No | 
| RSA AES-GCM (2) | Yes | Yes | No | 
| DHE\_DSS AES-GCM (2) | Yes | Yes | No | 
| ECDHE (ECDSA/RSA) AES-CBC (8) | Yes | Yes | No | 
| ECDH static (ECDSA/RSA) AES-CBC (8) | Yes | Yes | No | 
| RSA AES-CBC (4) | Yes | Yes | No | 
| DHE\_DSS AES-CBC (4) | Yes | Yes | No | 

## Moving between policies
<a name="msk-tls-security-policies-moving"></a>

### Existing clusters
<a name="msk-tls-security-policies-moving-existing"></a>

For updating an existing cluster's policy, you can move only one rung at a time, in either direction, using `UpdateClusterConfiguration` or `UpdateClusterKafkaVersion`:

```
MSK-TLS1.2-Default-2026  <->  MSK-TLSv1.3-2026  <->  MSK-TLSv1.3-Only-2026
```

To go from the default to TLS 1.3 only, apply `MSK-TLSv1.3-2026` first, wait for the update to complete, then apply `MSK-TLSv1.3-Only-2026`. This restriction exists so that every node in your cluster shares a protocol version with every other node at every point during the rolling restart, which is what keeps the cluster serving throughout the change.

**Important**  
Clearing the property is not a way to leave TLS 1.3 enforcement. On a cluster running `MSK-TLSv1.3-Only-2026`, removing the property requests a move to TLS 1.2 only, which is two rungs, and the request is rejected. Apply `MSK-TLSv1.3-2026` first.

### New clusters
<a name="msk-tls-security-policies-moving-new"></a>

For new clusters, you are able to select `MSK-TLSv1.3-Only-2026` directly. Make sure that your clients are configured to support TLS 1.3.

## Before you apply a policy
<a name="msk-tls-security-policies-before"></a>

**Warning**  
Both TLS 1.3 policies can break client connections, and a failed TLS 1.3 handshake does not fall back to TLS 1.2. Under `MSK-TLSv1.3-Only-2026`, clients that do not support TLS 1.3 can't connect. Under `MSK-TLSv1.3-2026`, clients that support only TLS 1.2 still connect, but clients with a faulty TLS 1.3 implementation fail. Make sure that your clients support the policy that you select before you apply it.

Under `MSK-TLSv1.3-2026`, each connection negotiates the highest version that both sides support. A client that advertises TLS 1.3 but does not implement it correctly negotiates TLS 1.3 and then fails the handshake. Check the following:
+ The TLS libraries that your clients use support TLS 1.3.
+ Those clients implement TLS 1.3 as specified in [RFC 8446](https://www.rfc-editor.org/rfc/rfc8446). Some older implementations abort the handshake instead of negotiating a version that both sides support.
+ Any firewall, proxy, load balancer, or traffic inspection appliance between your clients and your brokers handles TLS 1.3.

Under `MSK-TLSv1.3-Only-2026`, any client that can't negotiate TLS 1.3 fails to connect.

Confirm that every client, tool, and intermediary that connects to your cluster supports TLS 1.3 correctly before you apply either policy. We recommend that you apply `MSK-TLSv1.3-2026` to a non-production cluster first and confirm that your clients connect.

## Apply a security policy
<a name="msk-tls-security-policies-apply"></a>

You set `tls.security.policy` in an Amazon MSK configuration and apply that configuration to your cluster. There is no separate API.

**Important**  
The new configuration revision replaces the existing configuration. Keep any other properties that your configuration contains.

**To apply a security policy**

1. Add the property to a `server.properties` file.

   ```
   tls.security.policy=MSK-TLSv1.3-2026
   ```

   For the other properties that a configuration can contain, see [Custom Amazon MSK configurations](msk-configuration-properties.md).

1. Create or update an Amazon MSK configuration.

   ```
   aws kafka create-configuration \
       --name tls13-additive \
       --kafka-versions {{kafka-version}} \
       --server-properties fileb://server.properties
   ```

1. Apply the configuration revision to your cluster with either `UpdateClusterConfiguration` or `UpdateClusterKafkaVersion`.

   ```
   aws kafka update-cluster-configuration \
       --cluster-arn {{cluster-arn}} \
       --current-version {{current-cluster-version}} \
       --configuration-info '{"Arn":"{{configuration-arn}}","Revision":1}'
   ```

   Replace the placeholders as follows:
   + {{cluster-arn}} – The ARN of your cluster.
   + {{current-cluster-version}} – The current version of your cluster, from the `CurrentVersion` field that `DescribeCluster` returns.
   + {{configuration-arn}} – The ARN that `create-configuration` returned in the previous step.

Amazon MSK performs a rolling restart to apply the policy. Each broker restarts once. Clients reconnect and negotiate TLS under the new policy as the broker that they are connected to restarts. The cluster continues to serve traffic during the restart if your topics have a replication factor of 3 or more, `min.insync.replicas` is at most the replication factor minus 1, and your clients retry. For more information, see [Build highly available clusters](bestpractices.md#ensure-high-availability).

You can also set `tls.security.policy` in the `ServerProperties` of an `AWS::MSK::Configuration` resource in AWS CloudFormation, or in a configuration that you create in the Amazon MSK console at [https://console.aws.amazon.com/msk/](https://console.aws.amazon.com/msk/).

## View the current policy
<a name="msk-tls-security-policies-view"></a>

Get the configuration ARN and revision applied to your cluster, and then read the revision.

```
aws kafka describe-cluster --cluster-arn {{cluster-arn}}
```

```
aws kafka describe-configuration-revision \
    --arn {{configuration-arn}} \
    --revision {{revision}}
```

If `tls.security.policy` is absent, the cluster uses the default policy, `MSK-TLS1.2-Default-2026`.

## Roll back a security policy
<a name="msk-tls-security-policies-rollback"></a>

If clients fail to connect after you apply a TLS 1.3 policy, you can roll back by applying the previous policy in the order. Rolling back uses the same steps as applying a policy, and you can still move only one policy at a time. The following table shows the updates that each rollback takes.


| Current policy | Target policy | Steps | 
| --- | --- | --- | 
| MSK-TLSv1.3-Only-2026 | MSK-TLSv1.3-2026 | One update. Clients that support only TLS 1.2 can connect again. | 
| MSK-TLSv1.3-2026 | MSK-TLS1.2-Default-2026 | One update. The cluster accepts TLS 1.2 only. | 
| MSK-TLSv1.3-Only-2026 | MSK-TLS1.2-Default-2026 | Two updates. Apply MSK-TLSv1.3-2026, wait for the update to complete, and then apply MSK-TLS1.2-Default-2026. | 

**Important**  
To restore access for clients that support only TLS 1.2, roll back from `MSK-TLSv1.3-Only-2026` to `MSK-TLSv1.3-2026`. You do not need to return to the default policy, because `MSK-TLSv1.3-2026` accepts both TLS 1.2 and TLS 1.3. This is the quickest way to restore access while you upgrade your clients. Under `MSK-TLSv1.3-2026`, each connection still negotiates the highest version that both sides support, so a client that advertises TLS 1.3 but does not implement it correctly still fails the handshake. For more information, see [Before you apply a policy](#msk-tls-security-policies-before).  
When you roll back to `MSK-TLS1.2-Default-2026`, the cluster no longer accepts TLS 1.3. Any client that you configured to use only TLS 1.3 fails to connect. Before you roll back to the default policy, confirm that every client can negotiate TLS 1.2.

Before you roll back, confirm the current policy and the cluster state. The cluster must be `ACTIVE`. If an update is in progress, wait for it to complete.

```
aws kafka describe-cluster --cluster-arn {{cluster-arn}} \
    --query "ClusterInfo.{State:State,CurrentVersion:CurrentVersion,Configuration:CurrentBrokerSoftwareInfo}"
```

**To roll back a security policy**

1. Set the target policy, the one before the current policy in the order, in a `server.properties` file. Keep any other properties that your configuration contains.

   ```
   tls.security.policy=MSK-TLSv1.3-2026
   ```

   To roll back from `MSK-TLSv1.3-2026` to the default policy, you can set `tls.security.policy=MSK-TLS1.2-Default-2026` or remove the property. Setting the value explicitly makes the intent of the configuration clear.

1. Create a new revision of your configuration.

   ```
   aws kafka update-configuration \
       --arn {{configuration-arn}} \
       --server-properties fileb://server.properties
   ```

   Note the revision number in the response.

1. Apply the new revision to your cluster.

   ```
   aws kafka update-cluster-configuration \
       --cluster-arn {{cluster-arn}} \
       --current-version {{current-cluster-version}} \
       --configuration-info '{"Arn":"{{configuration-arn}}","Revision":{{revision}}}'
   ```

1. Wait for the update to complete. Amazon MSK performs a rolling restart. As each broker restarts with the new policy, it accepts the connections that the new policy allows. When the operation state is `UPDATE_COMPLETE`, every broker uses the new policy.

   ```
   aws kafka describe-cluster-operation \
       --cluster-operation-arn {{operation-arn}} \
       --query "ClusterOperationInfo.OperationState"
   ```

   If you're rolling back from `MSK-TLSv1.3-Only-2026` to the default policy, repeat steps 1 through 4 with `MSK-TLS1.2-Default-2026`.

1. Confirm the rollback. Check the applied policy, and then confirm that a client limited to TLS 1.2 can connect.

   ```
   openssl s_client -connect {{broker-endpoint}}:{{port}} -tls1_2
   ```

   A successful handshake prints a line such as `New, TLSv1.2, Cipher is {{cipher-suite}}`. A rejected handshake prints `New, (NONE), Cipher is (NONE)` and a `protocol version` alert. To confirm that the cluster rejects TLS 1.3 after you roll back to the default policy, repeat the command with `-tls1_3` and check that the handshake fails.

If you manage the configuration with AWS CloudFormation, set `tls.security.policy` in the `ServerProperties` of your `AWS::MSK::Configuration` resource to the previous policy in the order, and update the stack. To roll back from `MSK-TLSv1.3-Only-2026` to the default policy, update the stack twice, and wait for the cluster update to complete between the two updates.

## Troubleshooting
<a name="msk-tls-security-policies-troubleshooting"></a>

The following table lists errors that Amazon MSK returns when it rejects a `tls.security.policy` value, and how to resolve each one.


| Error | What to do | 
| --- | --- | 
| Invalid value '{{value}}' for tls.security.policy | Valid values are MSK-TLS1.2-Default-2026, MSK-TLSv1.3-2026, and MSK-TLSv1.3-Only-2026, and they are case sensitive. Update the value in your configuration to one of these names and apply the revision again. | 
| Cannot change tls.security.policy from {{current-policy}} to {{target-policy}} in one step | For example, you can't move from MSK-TLS1.2-Default-2026 to MSK-TLSv1.3-Only-2026 in one step. Apply MSK-TLSv1.3-2026 first and wait for the update to complete. Then apply MSK-TLSv1.3-Only-2026. | 
| Unsupported config tls.security.policy for Apache Kafka version {{kafka-version}} | Upgrade the cluster to Apache Kafka version 3.6 or later, and then apply the policy. If you can't upgrade, remove the property from your configuration to keep the current TLS settings. | 
| Setting tls.security.policy is not supported for this account | Remove the property from your configuration. To request access, contact your AWS account team or AWS Support. | 

**Warning**  
Do not set TLS properties directly on individual brokers using the Apache Kafka admin API, for example `kafka-configs.sh --alter --entity-type brokers --add-config ssl.enabled.protocols=...`. Amazon MSK rejects raw `ssl.*` keys in a configuration revision, but the Kafka admin API does not, and a per-broker setting takes precedence over the configuration that Amazon MSK applies. Instead, select a named security policy using the steps in this topic, and let Amazon MSK apply it across your cluster.  
If a protocol that you set directly has no cipher suite in common with your security policy, the broker can fail to start, or can lose replication with other brokers. For example, pinning `ssl.enabled.protocols=TLSv1.2` on a broker running `MSK-TLSv1.3-Only-2026` leaves no usable cipher suite. The broker reads this setting only when it starts, so the failure appears at the next restart. That restart might be an Amazon MSK operation such as patching, long after you made the change. If every broker is affected, the cluster becomes unavailable. Recovery then requires AWS Support, because removing a per-broker setting requires a reachable broker.