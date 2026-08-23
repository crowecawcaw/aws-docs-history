# Configure custom domain names for your Amazon MSK cluster

You can configure your MSK Provisioned cluster to advertise custom domain names instead of
the default AWS-generated broker addresses. Custom domain names are defined once in your
Amazon MSK configuration and applied automatically to every broker in the cluster, including new
brokers added during scaling operations. This works in both ZooKeeper and KRaft metadata
management mode.

###### Topics

- [How custom domain names work](#custom-domain-names-how-it-works "#custom-domain-names-how-it-works")
- [Prerequisites](#custom-domain-names-prerequisites "#custom-domain-names-prerequisites")
- [Set up a custom domain name end to end](custom-domain-setup.md "custom-domain-setup.md")

## How custom domain names work

When you add the `custom.advertised.listeners` property to your Amazon MSK
configuration, Amazon MSK does the following:

1. Validates the configuration (listener name, format, and uniqueness).
2. Resolves the `{broker_id}` template for each broker.
3. Applies the configuration through a rolling restart, one broker at a
   time.

The property takes the following format.

```
custom.advertised.listeners=LISTENER_NAME://hostname-pattern:port+{broker_id}
```

For example, on an IAM cluster with three brokers:

```
custom.advertised.listeners=CLIENT_IAM://b-{broker_id}.example.com:9000+{broker_id}
```

This resolves to the following addresses:

- Broker 1: `b-1.example.com:9001`
- Broker 2: `b-2.example.com:9002`
- Broker 3: `b-3.example.com:9003`

The `{broker_id}` template variable is required and must appear in the port
so that each broker resolves to a unique address. The `+` operator adds the
broker ID to the base port (9000 + 1 = 9001, 9000 + 2 = 9002, 9000 + 10 = 9010).

If your cluster has multiple client-facing listeners, you can assign a different domain
to each one by separating them with commas.

```
custom.advertised.listeners=CLIENT_IAM://b-{broker_id}.iam.example.com:9000+{broker_id},CLIENT_SASL_SCRAM://b-{broker_id}.scram.example.com:19000+{broker_id}
```

Each listener maps to one custom domain. You can't assign multiple domains to the same
listener. However, listeners can share the same domain name as long as each one resolves
to a unique `host:port` combination per broker. For example, two listeners can
share `b-{broker_id}.example.com` and differ only by port.

```
custom.advertised.listeners=CLIENT_IAM://b-{broker_id}.example.com:9000+{broker_id},CLIENT_SASL_SCRAM://b-{broker_id}.example.com:19000+{broker_id}
```

This behavior is identical in ZooKeeper and KRaft metadata management mode.

###### Verify networking before you apply the configuration

When you apply `custom.advertised.listeners`, your custom domain name
replaces the default addresses for the overridden listener. Therefore, your
networking layer must be in place and verified before you apply the configuration. If
the networking and trust layer isn't in place, resolvable, reachable, and trusted
from the client, the client can't reconnect. This is true even if the client was
connected moments earlier. If clients can't resolve the custom domain, they lose
connectivity.

## Prerequisites

Before you configure custom domain names on your cluster, make sure that the following
is true:

- Your cluster is an MSK Provisioned cluster (Standard or Express brokers) in the
  `ACTIVE` state.
- Each listener corresponds to an authentication type on your cluster. You can
  set custom advertised endpoints only for client listeners:
  `CLIENT`, `CLIENT_SECURE`,
  `CLIENT_SECURE_PUBLIC`, `CLIENT_SASL_SCRAM`,
  `CLIENT_SASL_SCRAM_PUBLIC`, `CLIENT_IAM`, and
  `CLIENT_IAM_PUBLIC`. Internal listeners
  (`REPLICATION` and `CONTROLLER`) aren't supported and are
  rejected at validation. The listener that you specify must also be bound (active)
  on your cluster. For example, if your cluster uses only IAM authentication,
  specifying `CLIENT_SECURE` is rejected, and the error message lists
  the valid client listeners for your cluster.
- Your networking layer is in place and verified before you apply the
  configuration. After you apply it, all clients that refresh metadata receive the
  custom domain address. If clients can't resolve the custom domain, they lose
  connectivity. Make sure that your networking layer is set up and reachable from
  all clients before you apply the configuration. For a complete, diagrammed
  walkthrough of the Network Load Balancer, Route 53, and AWS Certificate
  Manager setup, see [Configure a custom domain name for your Amazon MSK cluster](https://aws.amazon.com/blogs/big-data/configure-a-custom-domain-name-for-your-amazon-msk-cluster/ "https://aws.amazon.com/blogs/big-data/configure-a-custom-domain-name-for-your-amazon-msk-cluster/") on the
  AWS Big Data Blog.
