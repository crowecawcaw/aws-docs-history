# Offer product data feed

One offer can have several products, and one product can be included in different offers.
This data feed lists information about the relationships between offers and products.

This data feed provides information about all product offers you've created as the seller of
record.

When you add or remove a product from an offer, you create an offer revision.

The offer product data feed is refreshed every 24 hours, so new data is available
daily.

The following table explains the names and descriptions of the data feed's columns. For
information about the data feed history columns, see [Historization of the data](data-feed-details.md#data-feed-historization "data-feed-details.md#data-feed-historization").

| Column name    | Description                                                                                                                                                                             |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| offer_id       | The friendly identifier of this offer.Can be used to join to the<br>`offer_id` field of the `Offer` data feed.                                                                          |
| offer_revision | Combines with `offer_id` field to form the foreign key to the offer revision.                                                                                                           |
| product_id     | The friendly identifier of the product, this is the foreign key to the product that<br>this offer exposes. Can be used to join to the `product_id` field of<br>the `Product` data feed. |

## Example of Offer product data feed

The following shows an example of the Offer product data feed.

| offer_id            | offer_revision | product_id         |
| ------------------- | -------------- | ------------------ |
| offer-dacpxznflfwin | 10             | prod-o4grxfafcxxxx |
| offer-gszhmle5npzip | 24             | prod-o4grxfafcxxxy |
