# Customer

Profiles standard loyalty transaction object fields

The following table lists all the fields in the Customer Profiles standard
loyalty transaction object.

| Loyalty Transaction     | Standard loyaltyTransaction field | Type                                                                  | Description            |
| ----------------------- | --------------------------------- | --------------------------------------------------------------------- | ---------------------- | ------------------- | -------------------------------- | --------------------------------- | ---- | ----------- |
| TransactionId           | String                            | Unique identifier of the standard loyalty transaction.                |
| TransactionName         | String                            | Name or label of the transaction.                                     |
| TransactionType         | String                            | Type of transaction (e.g., earn, redeem, adjust).                     |
| ProgramRef              | String                            | Reference to the associated loyalty program.                          |
| MembershipRef           | String                            | Reference to the loyalty membership used in the transaction.          |
| PromotionRef            | String                            | Reference to a promotion that influenced this transaction.            |
| CreatedDate             | String                            | Date the transaction was created.                                     |
| TransactionDate         | String                            | Date the transaction occurred.                                        |
| Industry                | String                            | Industry associated with the transaction (e.g., airline, hotel).      |
| Location                | String                            | Location where the transaction occurred.                              |
| CreatedBy               | String                            | Identifier for who created the transaction.                           |
| UpdatedDate             | String                            | Last date the transaction was updated.                                |
| UpdatedBy               | String                            | Identifier of who last updated the transaction.                       |
| Status                  | String                            | Current status of the transaction.                                    |
| AccrualType             | String                            | Method of accrual (manual, automated, etc.).                          |
| Category                | String                            | Category of the transaction (e.g., flight, hotel stay).               |
| Channel                 | String                            | Channel where the transaction was initiated (e.g., online, in-store). |
| ProductId               | String                            | Identifier of the product or service tied to the transaction.         |
| Amount                  | String                            | Amount spent or transacted in the transaction.                        |
| OriginValue             | String                            | Original value before any conversion or offset.                       |
| OriginValueCurrency     | String                            | Currency of the original transaction value.                           |
| OriginValueOffset       | String                            | Adjustment to the original value for promotions, refunds, etc.        |
| PointsEarned            | String                            | Total points earned from this transaction.                            |
| PointOffset             | String                            | Points adjusted (e.g., bonuses, penalties).                           |
| QualifyingPointsEarned  | String                            | Points that count toward tier qualification.                          |
| TierBefore              | String                            | Customer tier before the transaction.                                 |
| TierAfter               | String                            | Customer tier after the transaction.                                  |
| Brand                   | String                            | Brand associated with the transaction.                                |
| Description             | String                            | Narrative description of the transaction.                             |
| AdditionalInformation   | String                            | Freeform additional information related to the transaction.           |
| PaymentMethod           | String                            | Payment method used (e.g., card, voucher).                            |
| PointTransfer           | PointTransfer                     | Point transfer details                                                |
| Attributes              | Map<String, String>               | Additional attributes.                                                | Standard Index Fields  | Standard index name | Standard preference record field |
| ---                     | ---                               |                                                                       | \_loyaltyTransactionId | TransactionId       | PointTransfer data type          | Standard loyaltyTransaction field | Type | Description |
| ---                     | ---                               | ---                                                                   |
| TransferId              | String                            | Identifier for the transfer transaction.                              |
| SourceProgramId         | String                            | ID of the source loyalty program.                                     |
| DestinationProgrmId     | String                            | ID of the destination loyalty program.                                |
| SourceMembershipId      | String                            | Membership ID in the source program.                                  |
| DestinationMembershipId | String                            | Membership ID in the destination program.                             |
| PointsTransferred       | String                            | Points deducted from the source program.                              |
| PointsReceived          | String                            | Points credited to the destination program.                           |
