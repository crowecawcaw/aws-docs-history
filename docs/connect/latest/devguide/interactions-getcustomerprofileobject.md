

# GetCustomerProfileObject
<a name="interactions-getcustomerprofileobject"></a>

Retrieve a customer profile object of the desired type, based on recency or any search identifier. Customer Profiles must be enabled for your Connect Customer instance.

See [ListProfileObjects](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListProfileObjects.html) in the *Connect Customer Customer Profiles API Reference*.

## Parameter object
<a name="getcustomerprofileobject-parameter"></a>

A `ProfileId` and `ObjectType` must be present. Either `UseLatest`, or `IdentifierName` and `IdentifierValue` must be present.

```
{
    "ProfileRequestData": {
        "ProfileId": Profile owning the object,
        "ObjectType": Type of object being retrieved,
        
        "IdentifierName": Optional name of search identifier,
        "IdentifierValue": Optional value of search identifier,
        "UseLatest": true / false 
    },
   "ProfileResponseData": {
       All of these fields are optional.
       Asset ID, if a single asset is found, is always persisted under the Customer -> Asset -> AssetID attribute + $.Customer.Asset.AssetId
       Order ID, if a single order is found, is always persisted under the Customer -> Order -> OrderId attribute + $.Customer.Order.OrderId
       Case ID, if a single case is found, is always persisted under the Customer -> Case -> CaseID attribute + $.Customer.Case.CaseId
        "AssetAssetId",
        "AssetProfileId",
        "AssetAssetName",
        "AssetSerialNumber",
        "AssetModelNumber",
        "AssetModelName",
        "AssetProductSKU",
        "AssetPurchaseDate",
        "AssetUsageEndDate",
        "AssetStatus",
        "AssetPrice",
        "AssetQuantity",
        "AssetDescription",
        "AssetAdditionalInformation",
        "AssetDataSource",
        "AssetAttributes.x",
        "OrderOrderId",
        "OrderProfileId",
        "OrderCustomerEmail",
        "OrderCustomerPhone",
        "OrderCreatedDate",
        "OrderUpdatedDate",
        "OrderProcessedDate",
        "OrderClosedDate",
        "OrderCancelledDate",
        "OrderCancelReason",
        "OrderName",
        "OrderAdditionalInformation",
        "OrderGateway",
        "OrderStatus",
        "OrderStatusCode",
        "OrderStatusUrl",
        "OrderCreditCardNumber",
        "OrderCreditCardCompany",
        "OrderFulfillmentStatus",
        "OrderTotalPrice",
        "OrderTotalTax",
        "OrderTotalDiscounts",
        "OrderTotalItemsPrice",
        "OrderTotalShippingPrice",
        "OrderTotalTipReceived",
        "OrderCurrency",
        "OrderTotalWeight",
        "OrderBillingName",
        "OrderBillingAddress1",
        "OrderBillingAddress2",
        "OrderBillingAddress3",
        "OrderBillingAddress4",
        "OrderBillingCity",
        "OrderBillingCounty",
        "OrderBillingCountry",
        "OrderBillingPostalCode",
        "OrderBillingProvince",
        "OrderBillingState",
        "OrderShippingName",
        "OrderShippingAddress1",
        "OrderShippingAddress2",
        "OrderShippingAddress3",
        "OrderShippingAddress4",
        "OrderShippingCity",
        "OrderShippingCounty",
        "OrderShippingCountry",
        "OrderShippingPostalCode",
        "OrderShippingProvince",
        "OrderShippingState",
        "OrderAttributes.x",
        "CaseCaseId",
        "CaseProfileId",
        "CaseTitle",
        "CaseSummary",
        "CaseStatus",
        "CaseReason",
        "CaseCreatedBy",
        "CaseCreatedDate",
        "CaseUpdatedDate",
        "CaseClosedDate",
        "CaseAdditionalInformation",
        "CaseDataSource",
        "CaseAttributes.x",
        "ObjectAttributes.x"
   }
}
```

## Results and conditions
<a name="getcustomerprofileobject-results"></a>

None. Conditions are not supported. If an error does not occur, the response's attributes are available dynamically under the `$.Customer` path based on the attributes included in `ProfileResponseData`.

## Errors
<a name="getcustomerprofileobject-errors"></a>
+ NoneFoundError - if no profiles were found for the associated profile search key.
+ NoMatchingError - if no other Error matches.

## Corresponding block in the UI
<a name="getcustomerprofileobject-ui"></a>

[Customer profiles block](https://docs.aws.amazon.com/connect/latest/adminguide/customer-profiles-block.html) 