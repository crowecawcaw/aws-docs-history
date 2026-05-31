# AssociateContactToCustomerProfile

Associate a contact to a customer profile. Customer Profiles must be enabled for
your Connect Customer instance.

See [AddProfileKey](../../../customerprofiles/latest/APIReference/API_AddProfileKey.md "../../../customerprofiles/latest/APIReference/API_AddProfileKey.md") in the _Connect Customer Customer Profiles API Reference_.

## Parameter object

A `ProfileId` and `ContactId` must be present.

```
{
    "ProfileRequestData": {
        "ProfileId": Profile being associated
        "ContactId": ContactId being associated
    },
   "ProfileResponseData": {
       None.
   }
}
```

## Results and conditions

None. Conditions are not supported.

## Errors

- NoMatchingError - if no other Error matches.

## Corresponding block in the UI

[Customer profiles block](../adminguide/customer-profiles-block.md "../adminguide/customer-profiles-block.md")
