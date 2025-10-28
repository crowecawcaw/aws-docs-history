# Create a Hyperledger Fabric Peer Node on Amazon Managed Blockchain (AMB)

You can create a Hyperledger Fabric peer node in a member that is in your AWS account using the AWS Management Console, the AWS CLI, or the AMB Access SDK [CreateNode](../APIReference/>API_CreateNode.md "../APIReference/>API_CreateNode.md") action.

1. Open the AMB Access console at [https://console.aws.amazon.com/managedblockchain/](https://console.aws.amazon.com/managedblockchain/ "https://console.aws.amazon.com/managedblockchain/").
2. Choose **Networks**, select the network from the list, and then choose **View details**.
3. Select a **Member** from the list, and then choose **Create peer node**.
4. Choose configuration parameters for your peer node according to the guidelines in [Work with Hyperledger Fabric Peer Nodes on AMB Access](managed-blockchain-hyperledger-peer-nodes.md "managed-blockchain-hyperledger-peer-nodes.md"), and
   then choose **Create peer node**.

- Use the `create-node` command, as shown in the following example. Replace the value
  of `--network-id`, `--member-id`, and `AvailabilityZone` as appropriate.

```
`[ec2-user@ip-192-0-2-17 ~]$` aws managedblockchain create-node \
--node-configuration '{"InstanceType":"`bc.t3.small`","AvailabilityZone":"`us-east-1a`"}' \
--network-id `n-MWY63ZJZU5HGNCMBQER7IN6OIU` \
--member-id `m-K46ICRRXJRCGRNNS4ES4XUUS5A`
```

The command returns output that includes the peer node's `NodeID`, as
shown in the following example:

```
{
     "NodeId": "nd-6EAJ5VA43JGGNPXOUZP7Y47E4Y"
}
```
