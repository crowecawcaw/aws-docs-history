# Set up a custom domain name end to end

This topic walks through the cluster-side configuration for custom domain names. The
networking layer (Network Load Balancer, DNS, and TLS certificate) is a prerequisite that
you own, and is covered in detail in [Configure a custom domain name for your Amazon MSK cluster](https://aws.amazon.com/blogs/big-data/configure-a-custom-domain-name-for-your-amazon-msk-cluster/ "https://aws.amazon.com/blogs/big-data/configure-a-custom-domain-name-for-your-amazon-msk-cluster/") on the AWS Big
Data Blog. With the
networking in place, the following steps cover the cluster-side setup.

###### Verify networking before you apply the configuration

When you apply `custom.advertised.listeners`, your custom domain name
replaces the default addresses for the overridden listener. Your networking layer
must be in place and verified before you apply the configuration. If clients can't
resolve the custom domain, they lose connectivity.

## Step 1: Add the custom domain to your Amazon MSK configuration

Create or update an Amazon MSK configuration that includes the
`custom.advertised.listeners` property, matching the hostnames and
ports that you provisioned on the Network Load Balancer. For a three-broker IAM
cluster fronted by a Network Load Balancer with ports 9001–9003, put the property in
a file.

```
custom.advertised.listeners=CLIENT_IAM://b-{broker_id}.example.com:9000+{broker_id}
```

Then create the configuration, passing the file as the server properties.

```
aws kafka create-configuration \
    --name "custom-domain-iam" \
    --description "Custom advertised listeners for CLIENT_IAM" \
    --server-properties fileb://custom-domain-config.txt
```

Use `fileb://` (not `file://`) so that the AWS CLI reads the
file as bytes and base64-encodes it. Passing the value inline is fragile because of
the `{broker_id}` braces. Leave `{broker_id}` literal in the
file, because Amazon MSK resolves it per broker at apply time. The response returns the
configuration `Arn` and `LatestRevision.Revision`, which you
use in the next step.

## Step 2: Apply the configuration

Apply the configuration to your cluster with
`UpdateClusterConfiguration`, using the console, AWS CLI, AWS CloudFormation,
AWS CDK, or Terraform. This is the same workflow that you already use for broker
configuration changes.

```
aws kafka update-cluster-configuration \
    --cluster-arn `your-cluster-arn` \
    --configuration-info arn=`configuration-arn`,revision=`revision` \
    --current-version `current-cluster-version`
```

Use the `DescribeCluster` operation to find the current version of your
cluster. Cluster versions aren't simple integers.

Amazon MSK validates the configuration synchronously before anything is applied, so a
malformed value never reaches your brokers. Amazon MSK rejects an invalid configuration
with an HTTP 400 error. For example errors, see [Custom domain name configuration errors](troubleshooting.md#troubleshoot-custom-domain-name-errors "troubleshooting.md#troubleshoot-custom-domain-name-errors"). Fix the reported
problem and reapply.

## Step 3: Track the rollout

```
aws kafka describe-cluster-operation-v2 \
    --cluster-operation-arn `operation-arn`
```

After the configuration is accepted, Amazon MSK applies it through a rolling restart.
Wait until the operation reports `UPDATE_COMPLETE`. If it reports
`UPDATE_FAILED`, a broker couldn't apply the change. The rollout halts
at that broker, the remaining brokers keep their previous configuration, and you can
fix the configuration and reapply it to recover.

## Step 4: Verify

Confirm that clients can connect through the custom domain by listing topics from a
client that uses the authentication settings for your listener.

If you can list topics through the custom domain endpoint, clients are successfully
connecting through your custom domain. If the operation reported
`UPDATE_COMPLETE` but clients can't connect, the cluster-side
configuration is correct but your networking layer likely needs attention. Check the
following:

- **Networking path**: Confirm that the Network
  Load Balancer listener, target group, and security group rule exist for the
  broker and port that the client is using, and that the Network Load Balancer
  is reachable from the client's network.
- **DNS resolution**: Confirm that the custom
  domain resolves to your Network Load Balancer from every network where your
  Apache Kafka clients run.
- **Certificate**: Confirm that the Network Load
  Balancer's TLS certificate covers the resolved broker hostname (through the
  common name or a subject alternative name), and that the client trusts the CA
  (root and intermediate for a private CA).

## Scaling and broker replacement

When you scale the cluster or a broker is replaced during automated healing, Amazon MSK
automatically applies the configuration to the new broker. Amazon MSK resolves
`{broker_id}` for the broker's ID, with no manual steps required on
the cluster side.

###### Note

Add the corresponding Network Load Balancer listener, target group, and DNS
record for any new broker. The networking layer doesn't scale
automatically.

## Remove a custom domain

To revert to the default Amazon MSK-generated addresses, remove the
`custom.advertised.listeners` property from your Amazon MSK configuration
and apply the updated configuration using
`UpdateClusterConfiguration`. Amazon MSK performs a rolling restart and
brokers revert to advertising their original addresses. Make sure that your clients
can reach the original Amazon MSK-generated addresses before you remove the custom domain
configuration.
