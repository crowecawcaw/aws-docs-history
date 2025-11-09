# Mapping Salesforce

objects to the standard asset in Customer Profiles

This topic lists which fields in Salesforce objects map to fields in the
standard asset object in Customer Profiles.

## Salesforce-Asset

object

Following is a list of all the fields in a Salesforce-Asset object.

- Id
- ContactId
- AccountId
- ParentId
- RootAssetId
- Product2Id
- ProductCode
- IsCompetitorProduct
- CreatedDate
- CreatedById
- LastModifiedDate
- LastModifiedById
- SystemModstamp
- IsDeleted
- Name
- SerialNumber
- InstallDate
- PurchaseDate
- UsageEndDate
- LifecycleStartDate
- LifecycleEndDate
- Status
- Price
- Quantity
- Description
- OwnerId
- AssetProvidedById
- AssetServiceById
- IsInternal
- AssetLevel
- StockKeepingUnit
- HasLifecycleManagement
- CurrentMrr
- CurrentLifecycleEndDate
- CurrentQuantity
- CurrentAmount
- LastViewedDate
- LastReferencedDate

## Mapping a

Salesforce-Asset object to a standard asset

A subset of the fields in the Salesforce-Asset object map to the
standard asset object in Customer Profiles.

The following table lists which fields can be mapped from the
Salesforce-Asset object to the standard asset.

| Saleforce-Asset source field | Standard asset target field |
| ---------------------------- | --------------------------- |
| Id                           | Attributes.sfdcAssetId      |
| ContactId                    | Attributes.sfdcContactId    |
| AccountId                    | Attributes.sfdcAccountId    |
| SerialNumber                 | SerialNumber                |
| StockKeepingUnit             | ProductSKU                  |
| UsageEndDate                 | UsageEndDate                |
| Status                       | Status                      |
| Price                        | Price                       |
| Quantity                     | Quantity                    |
| Description                  | Description                 |

The Salesforce-Asset customer data from the Salesforce object is
associated with an Amazon Connect standard asset using the indexes in the
following table.

| Standard Index Name   | Salesforce-Asset source field |
| --------------------- | ----------------------------- |
| \_salesforceAssetId   | Id                            |
| \_salesforceContactId | ContactId                     |
| \_salesforceAccountId | AccountId                     |

For example, you can use `_salesforceAssetId` and
`_salesforceAccountId` as an
`ObjectFilter.KeyName` with the [ListProfileObjects](../../../customerprofiles/latest/APIReference/API_ListProfileObjects.md "../../../customerprofiles/latest/APIReference/API_ListProfileObjects.md") API to find a standard asset. You can
find the Salesforce-Asset objects associated with a specific profile by
using the [ListProfileObjects](../../../customerprofiles/latest/APIReference/API_ListProfileObjects.md "../../../customerprofiles/latest/APIReference/API_ListProfileObjects.md") API with the `ProfileId` and
`ObjectTypeName` set to `Salesforce-Asset`.
