# Actions, resources, and condition keys for Amazon Managed Blockchain Query

Amazon Managed Blockchain Query (service prefix: `managedblockchain-query`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../managed-blockchain/latest/ambq-dg.md "../../../managed-blockchain/latest/ambq-dg.md").
- View a list of the [API operations available for
  this service](../../../managed-blockchain/latest/AMBQ-APIReference.md "../../../managed-blockchain/latest/AMBQ-APIReference.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../managed-blockchain/latest/ambq-dg/security-iam.md "../../../managed-blockchain/latest/ambq-dg/security-iam.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/managedblockchain-query/managedblockchain-query.json "https://servicereference.us-east-1.amazonaws.com/v1/managedblockchain-query/managedblockchain-query.json") for this service.

###### Topics

- [API operations defined by Amazon Managed Blockchain Query](#list_managedblockchain-query-operations "#list_managedblockchain-query-operations")
- [Actions defined by Amazon Managed Blockchain Query](#list_managedblockchain-query-actions-as-permissions "#list_managedblockchain-query-actions-as-permissions")
- [Resource types defined by Amazon Managed Blockchain Query](#list_managedblockchain-query-resources-for-iam-policies "#list_managedblockchain-query-resources-for-iam-policies")
- [Condition keys for Amazon Managed Blockchain Query](#list_managedblockchain-query-policy-keys "#list_managedblockchain-query-policy-keys")

## API operations defined by Amazon Managed Blockchain Query

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_managedblockchain-query-actions-as-permissions "#list_managedblockchain-query-actions-as-permissions").

| Operation                     | IAM action                                                                                                                                                                                       | Condition key | Possible value(s) | Access level |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------- | ----------------- | ------------ |
| BatchGetTokenBalance          | [managedblockchain-query:BatchGetTokenBalance](#list_managedblockchain-query-action-BatchGetTokenBalance "#list_managedblockchain-query-action-BatchGetTokenBalance")                            |               |                   | Read         |
| GetAssetContract              | [managedblockchain-query:GetAssetContract](#list_managedblockchain-query-action-GetAssetContract "#list_managedblockchain-query-action-GetAssetContract")                                        |               |                   | Read         |
| GetTokenBalance               | [managedblockchain-query:GetTokenBalance](#list_managedblockchain-query-action-GetTokenBalance "#list_managedblockchain-query-action-GetTokenBalance")                                           |               |                   | Read         |
| GetTransaction                | [managedblockchain-query:GetTransaction](#list_managedblockchain-query-action-GetTransaction "#list_managedblockchain-query-action-GetTransaction")                                              |               |                   | Read         |
| ListAssetContracts            | [managedblockchain-query:ListAssetContracts](#list_managedblockchain-query-action-ListAssetContracts "#list_managedblockchain-query-action-ListAssetContracts")                                  |               |                   | List         |
| ListFilteredTransactionEvents | [managedblockchain-query:ListFilteredTransactionEvents](#list_managedblockchain-query-action-ListFilteredTransactionEvents "#list_managedblockchain-query-action-ListFilteredTransactionEvents") |               |                   | List         |
| ListTokenBalances             | [managedblockchain-query:ListTokenBalances](#list_managedblockchain-query-action-ListTokenBalances "#list_managedblockchain-query-action-ListTokenBalances")                                     |               |                   | List         |
| ListTransactionEvents         | [managedblockchain-query:ListTransactionEvents](#list_managedblockchain-query-action-ListTransactionEvents "#list_managedblockchain-query-action-ListTransactionEvents")                         |               |                   | List         |
| ListTransactions              | [managedblockchain-query:ListTransactions](#list_managedblockchain-query-action-ListTransactions "#list_managedblockchain-query-action-ListTransactions")                                        |               |                   | List         |

## Actions defined by Amazon Managed Blockchain Query

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                                  | Description                                                                       | Resource types (\*required) | Condition keys | Access level |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------- | -------------- | ------------ |
| [BatchGetTokenBalance](${APIReferenceDocPage}API_BatchGetTokenBalance.md "${APIReferenceDocPage}API_BatchGetTokenBalance.md")                            | Grants permission to batch calls for GetTokenBalance API                          |                             |                | Read         |
| [GetAssetContract](${APIReferenceDocPage}API_GetAssetContract.md "${APIReferenceDocPage}API_GetAssetContract.md")                                        | Grants permission to fetch information about a contract on the blockchain         |                             |                | Read         |
| [GetTokenBalance](${APIReferenceDocPage}API_GetTokenBalance.md "${APIReferenceDocPage}API_GetTokenBalance.md")                                           | Grants permission to retrieve balance of a token for an address on the blockchain |                             |                | Read         |
| [GetTransaction](${APIReferenceDocPage}API_GetTransaction.md "${APIReferenceDocPage}API_GetTransaction.md")                                              | Grants permission to retrieve a transaction on the blockchain                     |                             |                | Read         |
| [ListAssetContracts](${APIReferenceDocPage}API_ListAssetContracts.md "${APIReferenceDocPage}API_ListAssetContracts.md")                                  | Grants permission to fetch multiple contracts on the blockchain                   |                             |                | List         |
| [ListFilteredTransactionEvents](${APIReferenceDocPage}API_ListFilteredTransactionEvents.md "${APIReferenceDocPage}API_ListFilteredTransactionEvents.md") | Grants permission to retrieve events on the blockchain with additional filters    |                             |                | List         |
| [ListTokenBalances](${APIReferenceDocPage}API_ListTokenBalances.md "${APIReferenceDocPage}API_ListTokenBalances.md")                                     | Grants permission to retrieve multiple balances on the blockchain                 |                             |                | List         |
| [ListTransactionEvents](${APIReferenceDocPage}API_ListTransactionEvents.md "${APIReferenceDocPage}API_ListTransactionEvents.md")                         | Grants permission to retrieve events in a transaction on the blockchain           |                             |                | List         |
| [ListTransactions](${APIReferenceDocPage}API_ListTransactions.md "${APIReferenceDocPage}API_ListTransactions.md")                                        | Grants permission to retrieve a multiple transactions on a blockchain             |                             |                | List         |

## Resource types defined by Amazon Managed Blockchain Query

Amazon Managed Blockchain Query does not support specifying a resource ARN in the
`Resource` element of an IAM policy statement.

## Condition keys for Amazon Managed Blockchain Query

Amazon Managed Blockchain Query has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
