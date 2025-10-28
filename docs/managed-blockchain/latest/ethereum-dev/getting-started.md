# Getting started with Amazon Managed Blockchain (AMB) Access Ethereum

The step-by-step tutorials in this section will show you how to perform the following tasks using Amazon Managed Blockchain (AMB) Access Ethereum.
Each task builds on the previous one, ending in making JSON-RPC calls to your Ethereum node.

###### Topics

- [Create an IAM policy to access the Ethereum network](#getting-started-next-steps "#getting-started-next-steps")
- [Create a node using the AWS Management Console](#gs-console-ethereum-node "#gs-console-ethereum-node")
- [Create an Accessor token using the AWS Management Console](#gs-console-accessor "#gs-console-accessor")
- [Find your HTTP or Websocket endpoints and make JSON-RPC calls](#gs-json-rpc-call "#gs-json-rpc-call")

## Create an IAM policy to access the Ethereum network

In order to access the Ethereum Mainnet to make
JSON-RPC and Consensus API calls, you must have user credentials (`AWS_ACCESS_KEY_ID` and
`AWS_SECRET_ACCESS_KEY`) that have the appropriate IAM permissions for
Amazon Managed Blockchain (AMB) Access Ethereum.

This example shows how you grant users AWS account access in the
`us-east-1` Region so that they can do the following:

- List all Ethereum networks
- Create and list nodes on all those networks
- Get and delete nodes in AWS account
  `111122223333`
- Get and delete accessors in AWS account
  `555555555555`
- Create WebSocket connections, and send HTTP requests
  to an Ethereum node

###### Note

- If you want to grant access across all Regions, replace `us-east-1`
  with `*`.
- You must specify the AWS account ID of the
  node and accessor resources in the policy that you want to enforce.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "WorkWithEthereumNetworks",
            "Effect": "Allow",
            "Action": [
                "managedblockchain:ListNetworks",
                "managedblockchain:GetNetwork"
            ],
            "Resource": [
                "arn:aws:managedblockchain:`us-east-1`::networks/n-ethereum-mainnet"


            ]
        },
        {
            "Sid": "CreateAndListEthereumNodes",
            "Effect": "Allow",
            "Action": [
                "managedblockchain:CreateNode",
                "managedblockchain:ListNodes"
            ],
            "Resource": [
                "arn:aws:managedblockchain:`us-east-1`::networks/*"
            ]
        },
        {
            "Sid": "ManageEthereumNodes",
            "Effect": "Allow",
            "Action": [
                "managedblockchain:GetNode",
                "managedblockchain:DeleteNode"
            ],
            "Resource": [
                "arn:aws:managedblockchain:`us-east-1`:`111122223333`:nodes/*"
            ]
        },
         {
            "Sid": "GetAndDeleteAccessors",
            "Effect": "Allow",
            "Action": [
                "managedblockchain:GetAccessor",
                "managedblockchain:DeleteAccessor"
            ],
            "Resource": [
                "arn:aws:managedblockchain:`us-east-1`:`555555555555`:accessors/*"
            ]
        },
        {
            "Sid": "CreateAndListAccessors",
            "Effect": "Allow",
            "Action": [
                "managedblockchain:CreateAccessor",
                "managedblockchain:ListAccessors"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Sid": "WorkWithEthereumNodes",
            "Effect": "Allow",
            "Action": [
                "managedblockchain:POST",
                "managedblockchain:GET",
                "managedblockchain:Invoke"

            ],
            "Resource": [
                "arn:aws:managedblockchain:`us-east-1`:`111122223333`:*"
             ]
        }
    ]
}

```

After you create the policy, attach that policy to your IAM user’s role for it to take
effect. For
more information, see [Creating a Role and assigning to
an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md").

## Create a node using the AWS Management Console

You must create an Ethereum node to make requests to the Ethereum network. The following example shows
you how to create a node using the AWS Management Console

To create an Ethereum node, you must consider and select the following characteristics:

- **Blockchain network** – Amazon Managed Blockchain (AMB) supports the following public Ethereum networks:

**Mainnet** – The proof-of-stake network of the primary public Ethereum blockchain. Transactions on Mainnet have actual value (that is, they incur real costs) and are recorded on the distributed ledger. This network supports the JSON-RPC and Consensus API operations.

- **Blockchain instance type** – This determines the computational
  and memory capacity allocated to this node for the blockchain workload. If you anticipate a
  more demanding workload for each node, you can choose more CPU and RAM. For example, your nodes
  might need to process a higher rate of transactions. Different instance types are subject to
  different pricing.

###### Note

For optimal performance and minimal degradation, we recommend the `bc.t3.xlarge` (or larger) instance size.

- **Ethereum node type** – The only node type that is currently
  supported is **Full node (Geth)**. The node uses the Geth execution client and
  the Lighthouse consensus client. For more information about node types, see [Node
  Types](https://ethereum.org/en/developers/docs/nodes-and-clients/#node-types "https://ethereum.org/en/developers/docs/nodes-and-clients/#node-types") in the Ethereum developer documentation. For more information on
  _Execution clients_ such as Geth, see [Execution
  clients](https://ethereum.org/en/developers/docs/nodes-and-clients/#execution-clients "https://ethereum.org/en/developers/docs/nodes-and-clients/#execution-clients") in the Ethereum developer documentation. For more information on
  _Consensus clients_ such as Lighthouse, see [Consensus
  clients](https://ethereum.org/en/developers/docs/nodes-and-clients/#consensus-clients "https://ethereum.org/en/developers/docs/nodes-and-clients/#consensus-clients") in the Ethereum developer documentation.
- **Availability Zone** – You can select the Availability Zone to
  launch the Ethereum node in. You can distribute nodes across different Availability Zones. This
  way, you can design your blockchain application for resiliency. For more information, see
  [Regions and Availability
  Zones](../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md "../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md") in the _Amazon EC2 User Guide_.

1. Open the AMB Access console at [https://console.aws.amazon.com/managedblockchain/](https://console.aws.amazon.com/managedblockchain/ "https://console.aws.amazon.com/managedblockchain/").
2. Choose **Networks** from the **Access** header in the left navigation.
3. Choose the **Dedicated networks** tab and select
   **Ethereum Mainnet** as your network to the details page.
4. Choose **Create node**.
5. In the **Create node** page, choose the **Blockchain instance type** suitable for your application. If your
   nodes need to process a higher rate of transactions more efficiently, choose an instance type
   with more CPU and RAM.
6. Choose the **Ethereum node type**, choose **Full node (Geth)**.
7. Choose the **Availability zone** such as **us-east-1**.
8. Optional, choose **Add new tag** in the **Tags** section.
9. Choose **Create node**.

###### Note

Amazon Managed Blockchain (AMB) Access Ethereum provisions and configures the node for you. The length of this process is not instantaneous depends on
many variables.

After you create the node, the **Node** details page in the AWS Management Console displays
the endpoints that you can use to make Ethereum API calls from code on a client. There are separate endpoints for
HTTP connections and WebSocket connections. For more information about sending API calls to
an Ethereum node in Amazon Managed Blockchain (AMB) to interact with smart contracts, see [Using Ethereum APIs with Amazon Managed Blockchain (AMB)](ethereum-api.md "ethereum-api.md").

## Create an Accessor token using the AWS Management Console

You can use Accessor tokens to make Ethereum API calls to an Ethereum node as a convenient
alternative to the Signature Version 4 (SigV4) signing process. You must provide a `BILLING_TOKEN`
from one of the Accessor tokens that you create as a query parameter with the call.

###### Important

- If you prioritize security and auditability over convenience, use the SigV4 signing
  process instead.
- You can access the Ethereum APIs using Signature Version 4 (SigV4) and token based access. However,
  if you choose to use token based access, then any security benefits that are provided by using
  SigV4 are negated.
- Never embed Accessor tokens in user-facing applications.

The following example shows how to create an Accessor token on the AWS Management Console and use it to
make Ethereum API calls on any Ethereum node in your AWS account.

1. Open the AMB Access console at [https://console.aws.amazon.com/managedblockchain/](https://console.aws.amazon.com/managedblockchain/ "https://console.aws.amazon.com/managedblockchain/").
2. Choose **Token accessors**.
3. Choose **Create accessor**.
4. Choose a valid _Ethereum_ blockchain **Network**.
5. Optional, add **Tags** for your Accessor.
6. Choose **Create accessor** to create a new Accessor token.

## Find your HTTP or Websocket endpoints and make JSON-RPC calls

In the console, the **Token accessors** page displays a list of all the
Accessor tokens that you can use to make Ethereum API calls to nodes in your AWS account from code
on a client. There are separate endpoints for HTTP connections and WebSocket connections.

These endpoints will be formatted as follows:

- **HTTPS —** `https://`your-node-id-lowercase`.t.ethereum.managedblockchain.`us-east-1`.amazonaws.com/?billingtoken=`your-billing-token``
- **Websocket —** `wss://`your-node-id-lowercase`.wss.t.ethereum.managedblockchain.`us-east-1`.amazonaws.com/?billingtoken=`your-billing-token``

After you have completed all the steps in this chapter, you have set up your IAM
permissions, created your Ethereum node and Accessor tokens, and have your relevant endpoints.
You can proceed to the [Using token based access to make JSON-RPC API calls to an Ethereum node](json-rpc-api-examples.md#json-rpc-api-tba-examples "json-rpc-api-examples.md#json-rpc-api-tba-examples") topic and run those examples.
