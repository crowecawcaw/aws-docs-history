# GetCalculatedAttributesForCustomerProfile

Retrieve calculated attributes for a customer profile. Customer Profiles must be enabled for
your Connect Customer instance.

## Parameter object

A `ProfileId` must be present.

```
{
    "ProfileRequestData": {
        "ProfileId": Profile owning the calculated attribute
    },
   "ProfileResponseData": {
       All of these fields are optional.
       "CalculatedAttributes._average_hold_time",
       "CalculatedAttributes._frequent_caller",
       "CalculatedAttributes.x",
   }
}
```

## Results and conditions

None. Conditions are not supported. If an error does not occur, the response's
attributes are available dynamically under the `$.Customer` path based on
the attributes included in `ProfileResponseData`.

## Errors

- NoneFoundError - if no profiles were found for the associated profile
  search key.
- NoMatchingError - if no other Error matches.

## Corresponding block in the UI

[Customer profiles block](../adminguide/customer-profiles-block.md "../adminguide/customer-profiles-block.md")
