

# UpdateCustomerProfile
<a name="interactions-updatecustomerprofile"></a>

Update a customer profile that was previously created or retrieved in the flow. Customer Profiles must be enabled for your Connect Customer instance.

See [UpdateProfile](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_UpdateProfile.html) in the *Connect Customer Customer Profiles API Reference*.

## Parameter object
<a name="updatecustomerprofile-parameter"></a>

```
{
"ProfileRequestData": {
    All of these fields are optional.
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
<a name="updatecustomerprofile-results"></a>

None. Conditions are not supported. If an error does not occur, the response's attributes are available dynamically under the `$.Customer` path based on the attributes included in `ProfileResponseData`.

## Errors
<a name="updatecustomerprofile-errors"></a>
+ NoMatchingError - if no other Error matches.

## Corresponding block in the UI
<a name="updatecustomerprofile-ui"></a>

[Customer profiles block](https://docs.aws.amazon.com/connect/latest/adminguide/customer-profiles-block.html) 