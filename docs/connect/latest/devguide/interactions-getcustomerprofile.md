# GetCustomerProfile

Retrieve a customer profile based any search identifier, up to five total. Customer Profiles must be enabled for
your Connect Customer instance.

See [SearchProfiles](../../../customerprofiles/latest/APIReference/API_SearchProfiles.md "../../../customerprofiles/latest/APIReference/API_SearchProfiles.md") in the _Connect Customer Customer Profiles API Reference_.

## Parameter object

At least one search identifier must be present.

```
{
    "ProfileRequestData": {
        Requires either IdentiferName and IdentifierValue, or SearchCriteria.

        "IdentifierName": Name to search for profiles with one identifier,
        "IdentiferValue": Value to search for profiles with one identifier,

        "SearchCriteria": [
            {
                "IdentifierName": Name to search for profiles with multiple identifiers,
                "IdentifierValue": Value to search for profiles with multiple identifiers
            }
        ],
        Required when using SearchCriteria
        "LogicalOperator": AND or OR

    },
   "ProfileResponseData": {
       All of these fields are optional.
       Newly created profile ID is persisted under the Customer -> ProfileID attribute + $.Customer.ProfileId
        "FirstName",
        "MiddleName",
        "LastName",
        "PhoneNumber",
        "EmailAddress",
        "AccountNumber",
        "AdditionalInformation",
        "PartyType",
        "BusinessName",
        "BirthDate",
        "Gender",
        "MobilePhoneNumber",
        "HomePhoneNumber",
        "BusinessPhoneNumber",
        "BusinessEmailAddress",
        "Address1",
        "Address2",
        "Address3",
        "Address4",
        "City",
        "County",
        "Country",
        "PostalCode",
        "Province",
        "State",
        "ShippingAddress1",
        "ShippingAddress2",
        "ShippingAddress3",
        "ShippingAddress4",
        "ShippingCity",
        "ShippingCounty",
        "ShippingCountry",
        "ShippingPostalCode",
        "ShippingProvince",
        "ShippingState",
        "MailingAddress1",
        "MailingAddress2",
        "MailingAddress3",
        "MailingAddress4",
        "MailingCity",
        "MailingCounty",
        "MailingCountry",
        "MailingPostalCode",
        "MailingProvince",
        "MailingState",
        "BillingAddress1",
        "BillingAddress2",
        "BillingAddress3",
        "BillingAddress4",
        "BillingCity",
        "BillingCounty",
        "BillingCountry",
        "BillingPostalCode",
        "BillingProvince",
        "BillingState",
        "Attributes.x"
}
```

## Results and conditions

None. Conditions are not supported. If an error does not occur, the response's
attributes are available dynamically under the `$.Customer` path based on
the attributes included in `ProfileResponseData`.

## Errors

- MultipleFoundError - if multiple profiles were found for the associated
  profile search key.
- NoneFoundError - if no profiles were found for the associated profile
  search key.
- NoMatchingError - if no other Error matches.

## Corresponding block in the UI

[Customer profiles block](../adminguide/customer-profiles-block.md "../adminguide/customer-profiles-block.md")
