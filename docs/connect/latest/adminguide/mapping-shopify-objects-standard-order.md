# Mapping Shopify

objects to the standard order in Amazon Connect Customer Profiles

This topic lists which fields in Shopify objects map to fields in the
standard order object in Customer Profiles.

## Shopify-DraftOrder

object

For a list of all the fields in a Shopify-DraftOrder object see [The DraftOrder object](https://shopify.dev/api/admin-rest/2021-10/resources/draftorder#resource_object "https://shopify.dev/api/admin-rest/2021-10/resources/draftorder#resource_object") in the Shopify documentation.

## Mapping a

Shopify-DraftOrder object to a standard order

A subset of the fields in the Shopify-DraftOrder object map to the
standard order object in Customer Profiles.

The following table lists which fields can be mapped from the
Shopify-DraftOrder object to the standard order.

The `StatusCode` is `ACTIVATED` if
`order_status_url` exists in the source. Otherwise, the
`StatusCode` is `DRAFT`.

| Shopify-DraftOrder source field | Standard order target field  |
| ------------------------------- | ---------------------------- |
| id                              | Attributes.ShopifyOrderId    |
| customer.id                     | Attributes.ShopifyCustomerId |
| note                            | AdditionalInformation        |
| email                           | CustomerEmail                |
| currency                        | Currency                     |
| created_at                      | CreatedDate                  |
| updated_at                      | UpdatedDate                  |
| name                            | Name                         |
| status                          | Status                       |
| order_status_url                | StatusCode                   |
| billing_address.address1        | BillingAddress.Address1      |
| billing_address.address2        | BillingAddress.Address2      |
| billing_address.city            | BillingAddress.City          |
| billing_address.zip             | BillingAddress.PostalCode    |
| billing_address.province        | BillingAddress.Province      |
| billing_address.country         | BillingAddress.Country       |
| billing_address.name            | BillingAddress.Name          |
| shipping_address.address1       | ShippingAddress.Address1     |
| shipping_address.address2       | ShippingAddress.Address2     |
| shipping_address.city           | ShippingAddress.City         |
| shipping_address.zip            | ShippingAddress.PostalCode   |
| shipping_address.province       | ShippingAddress.Province     |
| shipping_address.country        | ShippingAddress.Country      |
| shipping_address.name           | ShippingAddress.Name         |
| invoice_url                     | StatusUrl                    |
| total_price                     | TotalPrice                   |
| total_tax                       | TotalTax                     |
| line_items[].title              | OrderItems[].Title           |
| line_items[].price              | OrderItems[].Price           |
| line_items[].quantity           | OrderItems[].Quantity        |

### Example

The following example shows how to map a source field to a target
field.

```
"shopifyOrderId": {
    "Source": "_source.detail.event.detail.payload.id",
    "Target": "_order.Attributes.ShopifyOrderId"
}
```

The Shopify-DraftOrder customer data from the Shopify object is
associated with an Amazon Connect standard order using the following
index.

| Standard Index Name | Shopify-DraftOrder source field |
| ------------------- | ------------------------------- |
| \_shopifyOrderId    | id                              |

For example, you can use `_shopifyOrderId` as an
`ObjectFilter.KeyName` with the the [ListProfileObjects](../../../customerprofiles/latest/APIReference/API_ListProfileObjects.md "../../../customerprofiles/latest/APIReference/API_ListProfileObjects.md") API to find a standard order. You
can find the Shopify-DraftOrder objects associated with a specific
profile by using the [ListProfileObjects](../../../customerprofiles/latest/APIReference/API_ListProfileObjects.md "../../../customerprofiles/latest/APIReference/API_ListProfileObjects.md") API with the `ProfileId`
and `ObjectTypeName` set to
`Shopify-DraftOrder`.

## Shopify-Order object

For a list of all the fields in a Shopify-Order object see [The Order object](https://shopify.dev/api/admin-rest/2021-10/resources/order#resource_object "https://shopify.dev/api/admin-rest/2021-10/resources/order#resource_object") in the Shopify documentation.

## Mapping a

Shopify-Order object to a standard order

A subset of the fields in the Shopify-Order object map to the standard
order object in Customer Profiles.

The following table lists which fields can be mapped from the
Shopify-Order object to the standard order.

The `StatusCode` is `ACTIVATED` if
`order_status_url` exists in the source. Otherwise, the
`StatusCode` is `DRAFT`.

| Shopify-Order source field                 | Standard order target field  |
| ------------------------------------------ | ---------------------------- |
| id                                         | Attributes.ShopifyOrderId    |
| customer.id                                | Attributes.ShopifyCustomerId |
| cancelled_at                               | CancelledDate                |
| cancel_reason                              | CancelReason                 |
| closed_at                                  | ClosedDate                   |
| created_at                                 | CreatedDate                  |
| currency                                   | Currency                     |
| email                                      | CustomerEmail                |
| financial_status                           | Status                       |
| order_status_url                           | StatusCode                   |
| fulfillment_status                         | FulfillmentStatus            |
| gateway                                    | Gateway                      |
| name                                       | Name                         |
| note                                       | AdditionalInformation        |
| order_status_url                           | StatusUrl                    |
| phone                                      | CustomerPhone                |
| processed_at                               | ProcessedDate                |
| total_discounts                            | TotalDiscounts               |
| total_line_items_price                     | TotalItemsPrice              |
| total_price                                | TotalPrice                   |
| total_shipping_price_set.shop_money.amount | TotalShippingPrice           |
| total_tax                                  | TotalTax                     |
| total_tip_received                         | TotalTipReceived             |
| total_weight                               | TotalWeight                  |
| updated_at                                 | UpdatedDate                  |
| billing_address.address1                   | BillingAddress.Address1      |
| billing_address.address2                   | BillingAddress.Address2      |
| billing_address.city                       | BillingAddress.City          |
| billing_address.zip                        | BillingAddress.PostalCode    |
| billing_address.province                   | BillingAddress.Province      |
| billing_address.country                    | BillingAddress.Country       |
| billing_address.name                       | BillingAddress.Name          |
| payment_details.credit_card_number         | CreditCardNumber             |
| payment_details.credit_card_company        | CreditCardCompany            |
| shipping_address.address1                  | ShippingAddress.Address1     |
| shipping_address.address2                  | ShippingAddress.Address2     |
| shipping_address.city                      | ShippingAddress.City         |
| shipping_address.zip                       | ShippingAddress.PostalCode   |
| shipping_address.province                  | ShippingAddress.Province     |
| shipping_address.country                   | ShippingAddress.Country      |
| shipping_address.name                      | ShippingAddress.Name         |
| line_items[].title                         | OrderItems[].Title           |
| line_items[].price                         | OrderItems[].Price           |
| line_items[].quantity                      | OrderItems[].Quantity        |

### Example

The following example shows how to map a source field to a target
field.

```
"shopifyOrderId": {
    "Source": "_source.detail.event.detail.payload.id",
    "Target": "_order.Attributes.ShopifyOrderId"
}
```

The Shopify-Order customer data from the Shopify object is
associated with an Amazon Connect standard order using the following
index.

| Standard Index Name | Shopify-Order source field |
| ------------------- | -------------------------- |
| \_shopifyOrderId    | id                         |

For example, you can use `_shopifyOrderId` as an
`ObjectFilter.KeyName` with the the [ListProfileObjects](../../../customerprofiles/latest/APIReference/API_ListProfileObjects.md "../../../customerprofiles/latest/APIReference/API_ListProfileObjects.md") API to find a standard order. You
can find the Shopify-Order objects associated with a specific
profile by using the [ListProfileObjects](../../../customerprofiles/latest/APIReference/API_ListProfileObjects.md "../../../customerprofiles/latest/APIReference/API_ListProfileObjects.md") API with the `ProfileId`
and `ObjectTypeName` set to
`Shopify-Order`.
