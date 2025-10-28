# Mapping Shopify objects to the

standard profile object in Amazon Connect Customer Profiles

This topic lists which fields in Shopify objects map to fields in the
standard profile object in Amazon Connect Customer Profiles.

## Shopify-Customer

object

Following is a list of all the fields in a Shopify-Customer
object.

- accepts_marketing
- accepts_marketing_updated_at
- addresses
- currency
- created_at
- default_address.address1
- default_address.address2
- default_address.city
- default_address.company
- default_address.country
- default_address.country_code
- default_address.country_name
- default_address.customer_id
- default_address.default
- default_address.first_name
- default_address.id
- default_address.last_name
- default_address.name
- default_address.phone
- default_address.province
- default_address.province_code
- default_address.zip
- email
- first_name
- id
- last_name
- last_order_id
- last_order_name
- metafield.key
- metafield.value
- metafield.namespace
- metafield.value_type
- marketing_opt_in_level
- multipass_identifier
- note
- orders_count
- phone
- sms_marketing_consent.state
- sms_marketing_consent.opt_in_level
- sms_marketing_consent.consent_updated_at
- sms_marketing_consent.consent_collected_from
- state
- tags
- tax_exempt
- tax_exemptions
- total_spent
- updated_at
- verified_email

## Mapping a

Shopify-Customer object to a standard profile

A subset of the fields in the Shopify-Customer object map to the
standard profile object in Customer Profiles.

The following table lists which fields can be mapped from the
Shopify-Customer object to the standard profile.

| Shopify-Customer source field | Standard profile target field |
| ----------------------------- | ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id                            | Attributes.ShopifyCustomerId  |
| email                         | EmailAddress                  |
| first_name                    | FirstName                     |
| last_name                     | LastName                      |
| note                          | AdditionalInformation         |
| phone                         | PhoneNumber                   |
| default_address.address1      | Address.Address1              |
| default_address.address2      | Address.Address2              |
| default_address.city          | Address.City                  |
| default_address.province      | Address.Province              |
| default_address.country       | Address.Country               |
| default_address.zip           | Address.PostalCode            | ### Example The following example shows how to map a source field to a target field. `"shopifyCustomerId": { "Source": "_source.detail.event.detail.payload.id", "Target": "_profile.Attributes.ShopifyCustomerId" }` The Shopify-Customer customer data from the Shopify object is associated with an Amazon Connect customer profile using the following index.                                                                                                                                                                                                                                                           |
| Standard Index Name           | Shopify-Customer source field |
| ---                           | ---                           |
| \_shopifyCustomerId           | id                            | For example, you can use `_shopifyCustomerId` as a key name with the [SearchProfiles](../../../customerprofiles/latest/APIReference/API_SearchProfiles.md "../../../customerprofiles/latest/APIReference/API_SearchProfiles.md") API to find an Amazon Connect customer profile. You can find the Shopify-Customer objects associated with a specific profile by using the [ListProfileObjects](../../../customerprofiles/latest/APIReference/API_ListProfileObjects.md "../../../customerprofiles/latest/APIReference/API_ListProfileObjects.md") API with the `ProfileId` and `ObjectTypeName` set to `Shopify-Customer`. |
