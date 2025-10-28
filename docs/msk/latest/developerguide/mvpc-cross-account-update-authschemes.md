# Update the authorization schemes on a cluster

Multi-VPC private connectivity supports several authorization schemes: SASL/SCRAM, IAM, and TLS. The cluster owner can turn on/off private connectivity for one or more auth schemes. The cluster has to be in ACTIVE state to perform this action.

###### To turn on an auth scheme using the Amazon MSK console

1. Open the Amazon MSK console at [AWS Management Console](https://console.aws.amazon.com/msk "https://console.aws.amazon.com/msk") for the cluster
   that you want to edit.
2. In the navigation pane, under **MSK Clusters**, choose **Clusters** to display the list of clusters in the account.
3. Select the cluster that you want to edit. The cluster must be in an ACTIVE state.
4. Select the cluster **Properties** tab, and then go to **Network
   settings**.
5. Select the **Edit** dropdown menu and select **Turn on multi-VPC
   connectivity** to turn on a new auth scheme.
6. Select one or more authentication types that you want turned on for this cluster.
7. Select **Turn on selection**.
   When you turn on a new auth scheme, you should also create new managed VPC connections for the new auth scheme and update your clients to use the bootstrap brokers specific to the new auth scheme.

###### To turn off an auth scheme using the Amazon MSK console

###### Note

When you turn off multi-VPC private connectivity for auth schemes, all connectivity related infrastructure, including the managed VPC connections, are deleted.

When you turn off multi-VPC private connectivity for auth schemes,
existing VPC connections on client side change to INACTIVE, and Privatelink
infrastructure on the cluster side, including the managed VPC connections,
on the cluster side is removed. The cross-account user can only delete the
inactive VPC connection. If private connectivity is turned on again on the
cluster, the cross-account user needs to create a new connection to the
cluster.

1. Open the Amazon MSK console at [AWS Management Console](https://console.aws.amazon.com/msk "https://console.aws.amazon.com/msk").
2. In the navigation pane, under **MSK Clusters**, choose **Clusters** to display the list of clusters in the account.
3. Select the cluster you want to edit. The cluster must be in an ACTIVE state.
4. Select the cluster **Properties** tab, then go to **Network settings**.
5. Select the **Edit** drop down menu and select **Turn off multi-VPC connectivity** (to turn off an auth scheme).
6. Select one or more authentication types you want turned off for this cluster.
7. Select **Turn off selection**.

###### Example To turn on/off an auth scheme with the API

As an alternative to the MSK console, you can use the [UpdateConnectivity API](../../1.0/apireference/clusters-clusterarn-connectivity.md "../../1.0/apireference/clusters-clusterarn-connectivity.md") to turn on multi-VPC private connectivity and configure auth schemes on an ACTIVE cluster. The following example shows SASL/SCRAM and IAM auth schemes turned on for the cluster.

When you turn on a new auth scheme, you should also create new managed VPC connections for the new auth scheme and update your clients to use the bootstrap brokers specific to the new auth scheme.

When you turn off multi-VPC private connectivity for auth schemes,
existing VPC connections on client side change to INACTIVE, and Privatelink
infrastructure on the cluster side, including the managed VPC connections,
is removed. The cross-account user can only delete the inactive VPC
connection. If private connectivity is turned on again on the cluster, the
cross-account user needs to create a new connection to the cluster.

```
Request:
{
  "currentVersion": "string",
  "connnectivityInfo": {
    "publicAccess": {
      "type": "string"
    },
    "vpcConnectivity": {
      "clientAuthentication": {
        "sasl": {
          "scram": {
            "enabled": TRUE
          },
          "iam": {
            "enabled": TRUE
          }
        },
        "tls": {
          "enabled": FALSE
        }
      }
    }
  }
}

Response:
{
  "clusterArn": "string",
  "clusterOperationArn": "string"
}
```
