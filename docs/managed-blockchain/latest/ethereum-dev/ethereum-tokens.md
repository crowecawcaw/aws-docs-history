# Using token based access to make Ethereum API calls to Ethereum

nodes in Amazon Managed Blockchain (AMB)

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
  In the console, the **Token accessors** page displays a list of all the
  Accessor tokens that you can use to make Ethereum API calls to nodes in your AWS account from code
  on a client. There are separate endpoints for HTTP connections and WebSocket connections.

To learn more about how to make Ethereum API calls using token based access with your Accessor tokens, see:

- [Using token based access to make JSON-RPC API calls to an Ethereum node](json-rpc-api-examples.md#json-rpc-api-tba-examples "json-rpc-api-examples.md#json-rpc-api-tba-examples").
- [Using token based access to make Consensus API calls
  to an Ethereum node](consensus-api-examples.md#consensus-api-tba-examples "consensus-api-examples.md#consensus-api-tba-examples").
  You can create and manage Accessor tokens using the AWS Management Console. You can also create and
  manage Accessor tokens using the following API operations: `CreateAccessor`, `GetAccessor`,
  `ListAccessors`, and `DeleteAccessor`. A `BILLING_TOKEN` is a property of the Accessor. This
  `BillingToken` property is used to track your Accessor and for billing Ethereum API
  requests made to Ethereum nodes in your AWS account.

All API actions related to creating and managing Accessor tokens are also available through
the AWS CLI and SDKs.

## Creating an Accessor token for token based

access

You can create an Accessor token and use it to make Ethereum API calls on any Ethereum node in
your AWS account.

1. Open the AMB Access console at [https://console.aws.amazon.com/managedblockchain/](https://console.aws.amazon.com/managedblockchain/ "https://console.aws.amazon.com/managedblockchain/").
2. Choose **Token accessors**.
3. Choose **Create accessor**.
4. Choose a valid _Ethereum_ blockchain **Network**.
5. Optional, add **Tags** for your Accessor.
6. Choose **Create accessor** to create a new Accessor token.

```
aws managedblockchain create-accessor --accessor-type BILLING_TOKEN --network-type ETHEREUM_MAINNET
```

The previous command returns the `AccessorId` along with the
`BillingToken`, as shown in the following example.

```
{
"AccessorId": "ac-NGQ6QNKXLNEBXD3UI6XFDIL3VA",
"NetworkType": "ETHEREUM_MAINNET",
"BillingToken": "jZlP8OUI-PcQSKINyX9euJJDC5-IcW9e-nm1NyKH3n"
}
```

The key element in the response is the `BillingToken`. You can use this
property to make Ethereum API calls to your Ethereum nodes.

###### Note

You can use `BillingToken` to make Ethereum API calls to all the nodes owned by
the AWS account that created the Accessor token.

## Viewing an Accessor token details

You can view the properties for each Accessor token that your AWS account owns. For
example, you can view the Accessor ID or the Amazon Resource Name (ARN) of the Accessor. You can
also view the status, the type, the creation date, and the `BILLING_TOKEN`.

1. Open the AMB Access console at [https://console.aws.amazon.com/managedblockchain/](https://console.aws.amazon.com/managedblockchain/ "https://console.aws.amazon.com/managedblockchain/").
2. In the navigation pane, choose **Token accessors**.
3. Choose the **Accessor ID** of the token from the list.
   Run the following command to view the details of an Accessor token. Replace values of
   `--accessor-id` with your Accessor ID.

```
aws managedblockchain get-accessor --accessor-id `ac-NGQ6QNKXLNEBXD3UI6XFDIL3VA`
```

The `BillingToken` and other key properties are returned as shown in the following example.

```
{
  "Accessor": {
  "Id": "ac-NGQ6QNKXLNEBXD3UI6XFDIL3VA",
  "Type": "BILLING_TOKEN",
  "BillingToken": "jZlP8OUI-PcQSKINyX9euJJDC5-IcW9e-nm1NyKH3n",
  "Status": "AVAILABLE",
  "NetworkType": "ETHEREUM_MAINNET",
  "CreationDate": "2022-01-04T23:09:47.750Z",
  "Arn": "arn:aws:managedblockchain:us-east-1:251534485660:accessors/ac-NGQ6QNKXLNEBXD3UI6XFDIL3VA"
  }
}

```

## Deleting an Accessor token

When you delete an Accessor token, the token changes from the `AVAILABLE` to the
`PENDING_DELETION` status. You can't use an Accessor token with the
`PENDING_DELETION` status for WebSocket requests and HTTP requests.

###### Note

WebSocket connections that were initiated while the Accessor token was in
`AVAILABLE` status might remain open for up to 2 hours after they expire. An
Accessor token with the `PENDING_DELETION` status eventually becomes unavailable
through `GetAccessor` calls. Within 48 hours, it also disappears from
`ListAccessor` results.

1. Open the AMB Access console at [https://console.aws.amazon.com/managedblockchain/](https://console.aws.amazon.com/managedblockchain/ "https://console.aws.amazon.com/managedblockchain/").
2. In the navigation pane, choose **Token accessors**.
3. Select the Accessor token that you want from the list.
4. Choose **Delete**.
5. Confirm your choice.
   The following example shows how to delete a token. Use the `delete-accessor`
   command to delete a token. Set the value of `--accessor-id` with your Accessor
   ID.

**Deleting an Accessor token using the AWS CLI**

```
aws managedblockchain delete-accessor --accessor-id `ac-NGQ6QNKXLNEBXD3UI6XFDIL3VA`
```

If this command runs successfully, no messages are returned.
