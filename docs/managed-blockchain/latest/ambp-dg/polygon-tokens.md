Amazon Managed Blockchain (AMB) Access Polygon is in preview release and is subject to change.

# Creating and managing Accessor tokens for token-based access to

make AMB Access Polygon requests

You can also use _Accessor_ tokens to make JSON-RPC
calls to the Polygon network endpoints as a convenient alternative to the Signature Version 4 (SigV4) signing
process. You must provide a `BILLING_TOKEN` from one of the Accessor tokens you [create](../APIReference/API_CreateAccessor.md "../APIReference/API_CreateAccessor.md") and add as a parameter with your calls.

###### Important

- If you prioritize security and auditability over convenience, use the SigV4 signing
  process instead.
- You can access the Polygon JSON-RPCs using Signature Version 4 (SigV4) and token-based access.
  However, if you choose to use both protocols, your request is rejected.
- You must never embed Accessor tokens in user-facing applications.
  In the console, the **Token Accessors** page displays a list of all the
  Accessor tokens that you can use to make AMB Access Polygon JSON-RPC calls from your AWS account from
  code on a client.

For more information about AMB Access Polygon JSON-RPC requests, see [Managed Blockchain API and the JSON-RPCs supported with AMB Access Polygon](polygon-api.md "polygon-api.md").

You can create and manage Accessor tokens using the AWS Management Console. You can also create and manage
Accessor tokens using the following API operations: `CreateAccessor`, `GetAccessor`,
`ListAccessors`, and `DeleteAccessor`. A `BILLING_TOKEN` is a property of the Accessor. This
`BILLING_TOKEN` property is used to track your Accessor and for billing AMB Access Polygon
JSON-RPC requests made from your AWS account.

All API actions related to creating and managing Accessor tokens are also available through
the AWS Management Console, AWS CLI, and SDKs.

## Creating an Accessor token for token-based access

You can create an Accessor token and use it to make AMB Access Polygon API calls on any AMB Access Polygon node in
your AWS account.

1. Open the Managed Blockchain console at [https://console.aws.amazon.com/managedblockchain/](https://console.aws.amazon.com/managedblockchain/ "https://console.aws.amazon.com/managedblockchain/").
2. Choose **Token Accessors**.
3. Choose **Create Accessor**.
4. Choose a valid _Polygon_ blockchain **Network**.
5. Optional, add **Tags** for your Accessor.
6. Choose **Create Accessor** to create a new Accessor token.

```
aws managedblockchain create-accessor --accessor-type BILLING_TOKEN --network-type POLYGON_MAINNET
```

The previous command returns the `AccessorId` along with the
`BillingToken`, as shown in the following example.

```
{
"AccessorId": "ac-NGQ6QNKXLNEBXD3UI6********",
"NetworkType": "POLYGON_MAINNET",
"BillingToken": "jZlP8OUI-PcQSKINyX9euJJDC5-IcW9e-n********"
}
```

The _key_ element in your response is the
`BillingToken`. You can use this property to make AMB Access Polygon JSON-RPC calls.
Some values in the example have been obfuscated for security reasons but will appear
fully in actual responses.

###### Note

After the operation is run, Managed Blockchain provisions and configures the token for you.
The length of this process depends on many variables.

## Viewing an Accessor token details

You can view the properties for each Accessor token that your AWS account owns. For
example, you can view the Accessor ID or the Amazon Resource Name (ARN) of the Accessor. You can
also view the status, the type, the creation date, and the `BillingToken`.

1. Open the Managed Blockchain console at [https://console.aws.amazon.com/managedblockchain/](https://console.aws.amazon.com/managedblockchain/ "https://console.aws.amazon.com/managedblockchain/").
2. In the navigation pane, choose **Token Accessors**.
3. Choose the **Accessor ID** of the token from the list.
   The token details page the pops up. From this page, you can view the properties of the token.

Run the following command to view the details of an Accessor token. Replace values of
`--accessor-id` with your Accessor ID.

```
aws managedblockchain get-accessor --accessor-id `ac-NGQ6QNKXLNEBXD3UI6********`
```

The `BillingToken` and other key properties are returned as shown in the
following example. Some values in the example have been obfuscated for security reasons but
appear fully in actual responses.

```
{
  "Accessor": {
  "Id": "ac-NGQ6QNKXLNEBXD3UI6********",
  "Type": "BILLING_TOKEN",
  "BillingToken": "jZlP8OUI-PcQSKINyX9euJJDC5-IcW9e-n********",
  "Status": "AVAILABLE",
  "NetworkType": "POLYGON_MAINNET"
  "CreationDate": "2022-01-04T23:09:47.750Z",
  "Arn": "arn:aws:managedblockchain:us-east-1:666666666666:accessors/ac-NGQ6QNKXLNEBXD3UI6********"
  }
}

```

## Deleting an Accessor token

When you delete an Accessor token, the token changes from the `AVAILABLE` to the
`PENDING_DELETION` status. You can't use an Accessor token with the
`PENDING_DELETION` status.

1. Open the Managed Blockchain console at [https://console.aws.amazon.com/managedblockchain/](https://console.aws.amazon.com/managedblockchain/ "https://console.aws.amazon.com/managedblockchain/").
2. In the navigation pane, choose **Token Accessors**.
3. Select the Accessor token that you want from the list.
4. Choose **Delete**.
5. Confirm your choice.
   You're returned to the **Tokens accessors** page with your deleted Accessor token. The
   page displays the `PENDING_DELETION` status.

The following example shows how to delete a token. Use the `delete-accessor`
command to delete a token. Set the value of `--accessor-id` with your Accessor
ID.

**Deleting an Accessor token using the AWS CLI**

```
aws managedblockchain delete-accessor --accessor-id `ac-NGQ6QNKXLNEBXD3UI6********`
```

If this command runs successfully, no messages are returned.
