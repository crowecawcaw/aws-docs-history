

# Actions, resources, and condition keys for Amazon Managed Blockchain Query
<a name="list_managedblockchain-query"></a>

Amazon Managed Blockchain Query (service prefix: `managedblockchain-query`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/managed-blockchain/latest/ambq-dg/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/managed-blockchain/latest/ambq-dg/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/managedblockchain-query/managedblockchain-query.json) for this service.

**Topics**
+ [API operations defined by Amazon Managed Blockchain Query](#list_managedblockchain-query-operations)
+ [Actions defined by Amazon Managed Blockchain Query](#list_managedblockchain-query-actions-as-permissions)
+ [Resource types defined by Amazon Managed Blockchain Query](#list_managedblockchain-query-resources-for-iam-policies)
+ [Condition keys for Amazon Managed Blockchain Query](#list_managedblockchain-query-policy-keys)

## API operations defined by Amazon Managed Blockchain Query
<a name="list_managedblockchain-query-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_managedblockchain-query-actions-as-permissions).




- **   BatchGetTokenBalance  **
  - **IAM action:**  [managedblockchain-query:BatchGetTokenBalance](#list_managedblockchain-query-action-BatchGetTokenBalance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAssetContract  **
  - **IAM action:**  [managedblockchain-query:GetAssetContract](#list_managedblockchain-query-action-GetAssetContract) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTokenBalance  **
  - **IAM action:**  [managedblockchain-query:GetTokenBalance](#list_managedblockchain-query-action-GetTokenBalance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTransaction  **
  - **IAM action:**  [managedblockchain-query:GetTransaction](#list_managedblockchain-query-action-GetTransaction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAssetContracts  **
  - **IAM action:**  [managedblockchain-query:ListAssetContracts](#list_managedblockchain-query-action-ListAssetContracts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFilteredTransactionEvents  **
  - **IAM action:**  [managedblockchain-query:ListFilteredTransactionEvents](#list_managedblockchain-query-action-ListFilteredTransactionEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTokenBalances  **
  - **IAM action:**  [managedblockchain-query:ListTokenBalances](#list_managedblockchain-query-action-ListTokenBalances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTransactionEvents  **
  - **IAM action:**  [managedblockchain-query:ListTransactionEvents](#list_managedblockchain-query-action-ListTransactionEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTransactions  **
  - **IAM action:**  [managedblockchain-query:ListTransactions](#list_managedblockchain-query-action-ListTransactions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List



## Actions defined by Amazon Managed Blockchain Query
<a name="list_managedblockchain-query-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [BatchGetTokenBalance](${APIReferenceDocPage}API_BatchGetTokenBalance.html)  | Grants permission to batch calls for GetTokenBalance API |  |   | Read | 
|   [GetAssetContract](${APIReferenceDocPage}API_GetAssetContract.html)  | Grants permission to fetch information about a contract on the blockchain |  |   | Read | 
|   [GetTokenBalance](${APIReferenceDocPage}API_GetTokenBalance.html)  | Grants permission to retrieve balance of a token for an address on the blockchain |  |   | Read | 
|   [GetTransaction](${APIReferenceDocPage}API_GetTransaction.html)  | Grants permission to retrieve a transaction on the blockchain |  |   | Read | 
|   [ListAssetContracts](${APIReferenceDocPage}API_ListAssetContracts.html)  | Grants permission to fetch multiple contracts on the blockchain |  |   | List | 
|   [ListFilteredTransactionEvents](${APIReferenceDocPage}API_ListFilteredTransactionEvents.html)  | Grants permission to retrieve events on the blockchain with additional filters |  |   | List | 
|   [ListTokenBalances](${APIReferenceDocPage}API_ListTokenBalances.html)  | Grants permission to retrieve multiple balances on the blockchain |  |   | List | 
|   [ListTransactionEvents](${APIReferenceDocPage}API_ListTransactionEvents.html)  | Grants permission to retrieve events in a transaction on the blockchain |  |   | List | 
|   [ListTransactions](${APIReferenceDocPage}API_ListTransactions.html)  | Grants permission to retrieve a multiple transactions on a blockchain |  |   | List | 

## Resource types defined by Amazon Managed Blockchain Query
<a name="list_managedblockchain-query-resources-for-iam-policies"></a>

Amazon Managed Blockchain Query does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for Amazon Managed Blockchain Query
<a name="list_managedblockchain-query-policy-keys"></a>

Amazon Managed Blockchain Query has no service-specific condition keys that can be used in the `Condition` element of policy statements.