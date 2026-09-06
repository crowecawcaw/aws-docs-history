

# Document history for the AMB Query User Guide
<a name="doc-history"></a>

The following table describes the documentation releases for AMB Query.

| Change | Description | Date | 
| --- |--- |--- |
| [AMB Query supports Bitcoin transaction identifiers and transaction hashes](https://docs.aws.amazon.com/managed-blockchain/latest/ambq-dg/key-concepts.html#bitcoin-enhancement) | For Bitcoin networks, AMB Query API operations support both the transaction identifier (`transactionId`) and the transaction hash (`transactionHash`). | March 21, 2024 | 
| [Support for API usage metrics on Amazon CloudWatch](https://docs.aws.amazon.com/managed-blockchain/latest/ambq-dg/cw-usage-metrics.html) | AMB Query added support for API usage metrics on CloudWatch. These usage metrics correspond to the AMB Query service quotas.  | February 8, 2024 | 
| [Support for transactions that have not reached finality](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_GetTransaction.html) | AMB Query added support for transactions that have not reached *[*finality*](https://docs.aws.amazon.com/managed-blockchain/latest/ambq-dg/key-concepts.html#finality)*. It also removes support for the `status` property from the response of the `GetTransaction` operation. Instead, you will use the `confirmationStatus` and `executionStatus` properties to determine the status of the transaction.  | February 1, 2024 | 
| [Deprecation of the `status` property in the Transaction data type](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_Transaction.html#API_Transaction_Contents) | Amazon Managed Blockchain (AMB) Query has deprecated the `status` property in the Transaction data type. You must use the `confirmationStatus` and `executionStatus` fields to determine if the `status` of the transaction is `FINAL` or `FAILED`. | December 20, 2023 | 
| [Support for Sepolia Testnet](https://docs.aws.amazon.com/managed-blockchain/latest/ambq-dg/key-concepts.html#ambq-considerations) | Amazon Managed Blockchain (AMB) Query now supports queries on the Ethereum Sepolia Testnet. | October 19, 2023 | 
| [Support for asset contracts](https://docs.aws.amazon.com/managed-blockchain/latest/ambq-dg/query-usecases.html#query-contract-info) | You can use the `[`ListAssetContracts`](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/ListAssetContracts.html)` API operation to list deployed by a given address. Additionally, if you have the contract address, you can use the `[`GetAssetContract`](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/ListAssetContracts.html)` API operation to retrieve the contract's details. | October 16, 2023 | 
| [Support for Bitcoin Testnet](https://docs.aws.amazon.com/managed-blockchain/latest/ambq-dg/key-concepts.html#ambq-considerations) | Amazon Managed Blockchain (AMB) Query now supports queries on the Bitcoin Testnet. | October 16, 2023 | 
| [Initial release](https://docs.aws.amazon.com/managed-blockchain/latest/ambq-dg/what-is-service.html) | Initial release of the AMB Query service. | July 27, 2023 | 