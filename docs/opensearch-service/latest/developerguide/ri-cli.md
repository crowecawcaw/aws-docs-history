# Purchasing Reserved Instances (AWS CLI)

The AWS CLI has commands for viewing offerings, purchasing a reservation, and viewing
your reservations. The following command and sample response show the offerings for a
given AWS Region:

```
aws opensearch describe-reserved-instance-offerings --region `us-east-1`
{
  "ReservedInstanceOfferings": [
    {
      "FixedPrice": `x`,
      "ReservedInstanceOfferingId": "`1a2a3a4a5-1a2a-3a4a-5a6a-1a2a3a4a5a6a`",
      "RecurringCharges": [
        {
          "RecurringChargeAmount": `y`,
          "RecurringChargeFrequency": "Hourly"
        }
      ],
      "UsagePrice": 0.0,
      "PaymentOption": "PARTIAL_UPFRONT",
      "Duration": 31536000,
      "InstanceType": "m4.2xlarge.search",
      "CurrencyCode": "USD"
    }
  ]
}
```

For an explanation of each return value, see the following table.

| Field                        | Description                                                                                                                                                                                                                                                                                 |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `FixedPrice`                 | The upfront cost of the reservation.                                                                                                                                                                                                                                                        |
| `ReservedInstanceOfferingId` | The offering ID. Make note of this value if you want to reserve the<br>offering.                                                                                                                                                                                                            |
| `RecurringCharges`           | The hourly rate for the reservation.                                                                                                                                                                                                                                                        |
| `UsagePrice`                 | A legacy field. For OpenSearch Service, this value is always 0.                                                                                                                                                                                                                             |
| `PaymentOption`              | No Upfront, Partial Upfront, or All Upfront.                                                                                                                                                                                                                                                |
| `Duration`                   | Length of the term in seconds:<br>• 31536000 seconds is one year.<br>• 94608000 seconds is three years.                                                                                                                                                                                     |
| `InstanceType`               | The instance type for the reservation. For information about the<br>hardware resources that are allocated to each instance type, see [Amazon OpenSearch Service<br>pricing](https://aws.amazon.com/elasticsearch-service/pricing/ "https://aws.amazon.com/elasticsearch-service/pricing/"). |
| `CurrencyCode`               | The currency for `FixedPrice` and<br>`RecurringChargeAmount`.                                                                                                                                                                                                                               |

This next example purchases a reservation:

```
aws opensearch purchase-reserved-instance-offering --reserved-instance-offering-id `1a2a3a4a5-1a2a-3a4a-5a6a-1a2a3a4a5a6a` --reservation-name `my-reservation` --instance-count 3 --region `us-east-1`
{
  "ReservationName": "`my-reservation`",
  "ReservedInstanceId": "`9a8a7a6a-5a4a-3a2a-1a0a-9a8a7a6a5a4a`"
}
```

Finally, you can list your reservations for a given Region using the
following example:

```
aws opensearch describe-reserved-instances --region `us-east-1`
{
  "ReservedInstances": [
    {
      "FixedPrice": `x`,
      "ReservedInstanceOfferingId": "`1a2a3a4a5-1a2a-3a4a-5a6a-1a2a3a4a5a6a`",
      "ReservationName": "`my-reservation`",
      "PaymentOption": "PARTIAL_UPFRONT",
      "UsagePrice": 0.0,
      "ReservedInstanceId": "`9a8a7a6a-5a4a-3a2a-1a0a-9a8a7a6a5a4a`",
      "RecurringCharges": [
        {
          "RecurringChargeAmount": `y`,
          "RecurringChargeFrequency": "Hourly"
        }
      ],
      "State": "payment-pending",
      "StartTime": 1522872571.229,
      "InstanceCount": 3,
      "Duration": 31536000,
      "InstanceType": "m4.2xlarge.search",
      "CurrencyCode": "USD"
    }
  ]
}
```

###### Note

`StartTime` is Unix epoch time, which is the number of seconds that
have passed since midnight UTC of 1 January 1970. For example, 1522872571 epoch time
is 20:09:31 UTC of 4 April 2018. You can use online converters.

To learn more about the commands used in the preceding examples, see the [AWS CLI Command Reference](../../../cli/latest/reference/es/index.md "../../../cli/latest/reference/es/index.md").
