After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Interacting with a kdb

cluster

To run commands on a Managed kdb Insights cluster, you must establish a q
connection to a cluster endpoint or individual node in a cluster. If you don’t care
which node in the cluster your connection is established with, use the cluster
endpoint. The endpoint is an IP address (elastic network interface) that resides in
your account. This provides a simple way to connect for a single-node cluster and for
other scenarios.

Alternately, from client code residing on a cluster node running with Managed kdb,
you can also make a direct connection to an individual node. This gives you full
control of which node in a cluster to use. This might be useful if you have custom
allocation logic in your client code. You can use the Managed kdb list clusters and
list node functionality to see what cluster and node resources are available in your
environment. Then, you can use the cluster connection functionality to obtain a
connection string that you can use to establish a q IPC connection to a cluster or
node.

As a part of cluster discovery, FinSpace provides you the following
capabilities:

- Listing all clusters running in your Managed kdb environment.
- Listing all nodes running in a kdb cluster. For more information on this,
  see [Listing clusters and cluster nodes](#finding-kdb-clusters "#finding-kdb-clusters").
- Connect to the underlying node from an existing cluster. For more
  information on this, see [Connecting to a cluster endpoint or node in
  a cluster](#connect-kdb-clusters "#connect-kdb-clusters").

## Listing clusters and cluster nodes

There are three ways to view a list of clusters and nodes running in a
cluster:

- **FinSpace API operations** – You can
  call the `ListKxClusterNodes` API operation to get a list of
  nodes in a cluster. For more information, see the [ListKxClusterNodes](../management-api/API_ListKxClusterNodes.md "../management-api/API_ListKxClusterNodes.md") in the _Management API Reference
  Guide_.
- **q API operations** – You can use
  the `.aws.list_kx_cluster_nodes()` and
  `.aws.list_kx_clusters()` API operations to get a list of
  nodes or clusters. For more information, see [Discovery APIs](interacting-with-kdb-q-apis.md#q-apis-discovery "interacting-with-kdb-q-apis.md#q-apis-discovery").
- **Console** – You can view a list of
  nodes from the cluster details page in the FinSpace console.

###### To view a list of clusters by using the console

1. Sign in to the AWS Management Console and open the Amazon FinSpace console at [https://console.aws.amazon.com/finspace](https://console.aws.amazon.com/finspace/landing "https://console.aws.amazon.com/finspace/landing").
2. Choose **Kdb environments**.
3. From the kdb environments table, choose the name of the
   environment.
4. On the environment details page, choose the **Clusters**
   tab.
5. Choose a cluster name to view its details. On the cluster details page,
   you can see details about a cluster.

###### To view a list of nodes available in a cluster by using the console

1. Sign in to the AWS Management Console and open the Amazon FinSpace console at [https://console.aws.amazon.com/finspace](https://console.aws.amazon.com/finspace/landing "https://console.aws.amazon.com/finspace/landing").
2. Choose **Kdb environments**.
3. From the list of environments, choose a kdb environment.
4. On the environment details page, choose the **Clusters**
   tab.
5. From the list of clusters, choose the one where you want to view
   nodes.
6. On the cluster details page, choose **Nodes** tab. All
   the nodes running in the cluster are displayed along with the information
   about the node ID , the Availability Zone ID where the node is running, and
   the time when the node was started. You can use the `nodeId` to
   call the `GetKxConnectionString` API operation, which returns a
   signed connection string.

## Connecting to a cluster endpoint or node in

a cluster

Amazon FinSpace uses the model based on AWS Identity and Access Management that allows users to control access
to clusters and their associated kdb databases using IAM roles and policies.

Administrators create users in the FinSpace kdb environment using the existing
`CreateKxUser` API operation, and associate these users with an
IAM principal. Only users that will be connecting to a kdb cluster need to be
registered as a FinSpace user.

Next, using their IAM credentials, connecting users will request a SigV4
signed authentication token to connect to the cluster. Additionally, each cluster
can be associated with an IAM execution role in the customer account when a
cluster is created. This role will be used when a cluster connects to other
clusters, or makes requests to other AWS resources in the customer’s
account.

###### To connect to a cluster endpoint or cluster node

1. **Create IAM role for a new user.**
   1. Sign in to AWS Management Console, and open IAM Identity
      Center.
   2. Create an IAM role.
   3. Assign the following policy to the IAM role that you
      created.

   In the following example, replace each `*user
 input placeholder*` with your own
   values.

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Effect": "Allow",
    "Action": "finspace:ConnectKxCluster",
    "Resource": "arn:aws:finspace:`us-east-1`:`111122223333`:kxEnvironment/sdb3moagybykax4oexvsq4/kxCluster/`testhdb-cluster`"
    },
    {
    "Effect": "Allow",
    "Action": "finspace:GetKxConnectionString",
    "Resource": "arn:aws:finspace:`us-east-1`:`111122223333`:kxEnvironment/`sdb3moagybykax4oexvsq4`/kxCluster/`testhdb-cluster`"
    }
    ]
   }`

   ```

   4. Associate the IAM role to the following trust policy that allows
      FinSpace to assume the role, as well as the account itself.

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Effect": "Allow",
    "Principal": {
    "Service": "finspace.amazonaws.com",
    "AWS": "arn:aws:iam::`111122223333`:root"
    },
    "Action": "sts:AssumeRole"
    }
    ]
   }`

   ```

2. **Create a kdb user with the environment id,
   username, and the IAM role that you created in the previous
   step.**

```
aws finspace create-kx-user
    --environment-id "`sdb3moagybykax4oexvsq4`"
    --user-name alice
    --iam-role arn:aws:iam::`111122223333`:role/`user-alice` [--tags {`tags`}]
```

3. **Federate the user that you created into its user
   role.**
   1. To get a kdb connection string for a user, you must first federated
      into the role associated with the user. How you assume this role
      depends on what federation tool you use. If you use AWS Security Token Service, you
      could run the following command and use the credentials of the
      customer account.

   ```
   export $(printf "AWS_ACCESS_KEY_ID=%s AWS_SECRET_ACCESS_KEY=%s AWS_SESSION_TOKEN=%s" \
   $(aws sts assume-role \
   --role-arn arn:aws:iam::`111122223333`:role/`user-alice` \
   --role-session-name "`alice-connect-to-testhdb`" \
   --query "Credentials.[AccessKeyId,SecretAccessKey,SessionToken]" \
   --output text))
   ```

   2. Verify that the role has been assumed.

   ```
   aws sts get-caller-identity | cat
   ```

4. **Get connection string for the
   user.**

Get signed connection strings for connecting to kdb clusters or nodes.
These connection strings are valid only for 60 minutes. To connect to a
cluster endpoint, use `get-kx-connetion-string` to obtain a
connection string.

```
aws finspace get-kx-connection-string
    --environment-id "`sdb3moax4oexvsq4`"
    --user-arn arn:aws:finspace:`us-east-1`:`111122223333`:kxEnvironment/`sdb3moax4oexvsq4`/kxUser/`alice`
    --cluster-name "`testhdb-cluster`"
    --region `us-east-1`
```

Example of the signed connection string that you get.

`:tcps://vpce-06259327736e61c9d-uczv1va3.vpce-svc-0938de45abc1ce4d8.us-east-1.vpce.amazonaws.com:443:testuser:Host=vpce-06259327736e61c9d-uczv1va3.vpce-svc-0938de45abc1ce4d8.us-east-1.vpce.amazonaws.com&Port=5000&User=testuser&Action=finspace%3AConnectKxCluster&X-Amz-Security-Token=IQoJb3JpZ2luX2Vj&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20230524T150227Z&X-Amz-SignedHeaders=host&X-Amz-Expires=900&X-Amz-Credential=ASIAR2V4%2Fus-east-1%2Ffinspace-apricot%2Faws4_request&X-Amz-Signature=28854cc2f97f8f77009928fcdf15480dd10b43c61dda22b0af5f0985d38e7114` 5. Connect to a cluster using the signed connection string.

```
hopen `:tcps://vpce-06259327736e61c9d-uczv1va3.vpce-svc-0938de45abc1ce4d8.us-east-1.vpce.amazonaws.com:443:testuser:Host=vpce-06259327736e61c9d-uczv1va3.vpce-svc-0938de45abc1ce4d8.us-east-1.vpce.amazonaws.com&Port=5000&User=testuser&Action=finspace%3AConnectKxCluster&X-Amz-Security-Token=IQoJb3JpZ2luX2Vj&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20230524T150227Z&X-Amz-SignedHeaders=host&X-Amz-Expires=900&X-Amz-Credential=ASIAR2V4%2Fus-east-1%2Ffinspace-apricot%2Faws4_request&X-Amz-Signature=28854cc2f97f8f77009928fcdf15480dd10b43c61dda22b0af5f0985d38e7114`
```

###### Note

The connection handles to the cluster VPC endpoint have an idle timeout
period of 350 seconds. If you don't send commands or data by the time that the
idle timeout period elapses, the connection closes and you will need to reopen
it.

To keep the connection open, use a timer that periodically sends a ping
message to the cluster through an active handle. For this, you can run the
following code.

```
.aws.start_keepalive:
{\t 10000;.z.ts:{con "-1 \"Ping\"";}}
.aws.stop_keepalive:
{\t 0;.z.ts:{}}
```
