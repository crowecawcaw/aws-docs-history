# Exchange Convertible Reserved Instances

You can exchange one or more Convertible Reserved Instances for another Convertible Reserved Instance with a different configuration,
including instance family, operating system, and tenancy. There are no limits to how
many times you perform an exchange, as long as the new Convertible Reserved Instance is of an equal or higher
value than the Convertible Reserved Instances that you are exchanging.

When you exchange your Convertible Reserved Instance, the number of instances for your current reservation is
exchanged for a number of instances that cover the equal or higher value of the
configuration of the new Convertible Reserved Instance. Amazon EC2 calculates the number of Reserved Instances that you can
receive as a result of the exchange.

You can't exchange Standard Reserved Instances, but you can modify them. For more information, see
[Modify Reserved Instances](ri-modifying.md "ri-modifying.md") .

###### Contents

- [Requirements for exchanging
  Convertible Reserved Instances](#riconvertible-exchange-limits "#riconvertible-exchange-limits")
- [Calculate Convertible Reserved Instances exchanges](#riconvertible-exchange-cost "#riconvertible-exchange-cost")
- [Merge Convertible Reserved Instances](#ri-merge-convertible "#ri-merge-convertible")
- [Exchange a portion of a Convertible Reserved Instance](#ri-split-convertible "#ri-split-convertible")
- [Submit exchange requests](#ri-exchange-process "#ri-exchange-process")

## Requirements for exchanging

Convertible Reserved Instances

If the following conditions are met, Amazon EC2 processes your exchange request. Your
Convertible Reserved Instance must be:

- Active
- Not pending a previous exchange request
- Have at least 24 hours remaining before it expires

The following rules apply:

- Convertible Reserved Instances must be exchanged for other Convertible Reserved Instances currently offered by
  AWS.
- Convertible Reserved Instances are associated with a specific Region, which is fixed for the
  duration of the reservation's term. You can't exchange a Convertible Reserved Instance for a Convertible Reserved Instance
  in a different Region.
- To exchange a zonal Convertible Reserved Instance, AWS must have enough capacity for the new
  instance type in the Region.
- You can exchange one or more Convertible Reserved Instances at a time for one Convertible Reserved Instance only.
- To exchange a portion of a Convertible Reserved Instance, you can modify it into two or more
  reservations, and then exchange one or more of the reservations for a new
  Convertible Reserved Instance. For more information, see [Exchange a portion of a Convertible Reserved Instance](#ri-split-convertible "#ri-split-convertible"). For more information about
  modifying your Reserved Instances, see [Modify Reserved Instances](ri-modifying.md "ri-modifying.md").
- All Upfront Convertible Reserved Instances can be exchanged for Partial Upfront Convertible Reserved Instances, and vice
  versa.

###### Note

If the total upfront payment required for the exchange (true-up cost)
is less than $0.00, AWS automatically gives you a quantity of
instances in the Convertible Reserved Instance that ensures that true-up cost is $0.00 or
more.

###### Note

If the total value (upfront price + hourly price \* number of remaining
hours) of the new Convertible Reserved Instance is less than the total value of the exchanged
Convertible Reserved Instance, AWS automatically gives you a quantity of instances in the
Convertible Reserved Instance that ensures that the total value is the same or higher than that
of the exchanged Convertible Reserved Instance.

- To benefit from better pricing, you can exchange a No Upfront Convertible Reserved Instance for an
  All Upfront or Partial Upfront Convertible Reserved Instance.
- You can't exchange All Upfront and Partial Upfront Convertible Reserved Instances for No Upfront
  Convertible Reserved Instances.
- You can exchange a No Upfront Convertible Reserved Instance for another No Upfront Convertible Reserved Instance only if
  the new Convertible Reserved Instance's hourly price is the same or higher than the exchanged
  Convertible Reserved Instance's hourly price.

###### Note

If the total value (hourly price \* number of remaining hours) of the
new Convertible Reserved Instance is less than the total value of the exchanged Convertible Reserved Instance, AWS
automatically gives you a quantity of instances in the Convertible Reserved Instance that
ensures that the total value is the same or higher than that of the
exchanged Convertible Reserved Instance.

- If you exchange multiple Convertible Reserved Instances that have different expiration dates, the
  expiration date for the new Convertible Reserved Instance is the date that's furthest in the
  future.
- If you exchange a single Convertible Reserved Instance, it must have the same term (1-year or
  3-years) as the new Convertible Reserved Instance. If you merge multiple Convertible Reserved Instances with different term
  lengths, the new Convertible Reserved Instance has a 3-year term. For more information, see [Merge Convertible Reserved Instances](#ri-merge-convertible "#ri-merge-convertible").
- When Amazon EC2 exchanges a Convertible Reserved Instance, it retires the associated reservation, and
  transfers the end date to the new reservation. After the exchange, Amazon EC2
  sets both the end date for the old reservation and the start date for the
  new reservation equal to the date of the exchange. For example, if you
  exchange a three-year reservation that had 16 months left in its term, the
  new reservation is a 16-month reservation with the same end date as the
  reservation from the Convertible Reserved Instance that you exchanged.

## Calculate Convertible Reserved Instances exchanges

Exchanging Convertible Reserved Instances is free. However, you might be required to pay a true-up cost,
which is a prorated upfront cost of the difference between the Convertible Reserved Instances that you had
and the new Convertible Reserved Instances that you receive from the exchange.

Each Convertible Reserved Instance has a list value. This list value is compared to the list value of the
Convertible Reserved Instances that you want in order to determine how many instance reservations you can
receive from the exchange.

For example: You have 1 x $35-list value Convertible Reserved Instance that you want to exchange for a new
instance type with a list value of $10.

```
$35/$10 = 3.5
```

You can exchange your Convertible Reserved Instance for three $10 Convertible Reserved Instances. It's not possible to purchase
half reservations; therefore you must purchase an additional Convertible Reserved Instance to cover the
remainder:

```
3.5 = 3 whole Convertible Reserved Instances + 1 additional Convertible Reserved Instance
```

The fourth Convertible Reserved Instance has the same end date as the other three. If you are exchanging
Partial or All Upfront Convertible Reserved Instances, you pay the true-up cost for the fourth reservation.
If the remaining upfront cost of your Convertible Reserved Instances is $500, and the new reservation would
normally cost $600 on a prorated basis, you are charged $100.

```
$600 prorated upfront cost of new reservations - $500 remaining upfront cost of old reservations = $100 difference
```

## Merge Convertible Reserved Instances

If you merge two or more Convertible Reserved Instances, the term of the new Convertible Reserved Instance must be the same as the
old Convertible Reserved Instances, or the highest of the Convertible Reserved Instances. The expiration date for the new Convertible Reserved Instance is
the expiration date that's furthest in the future.

For example, you have the following Convertible Reserved Instances in your account:

| Reserved Instance ID | Term   | Expiration date |
| -------------------- | ------ | --------------- |
| aaaa1111             | 1-year | 2018-12-31      |
| bbbb2222             | 1-year | 2018-07-31      |
| cccc3333             | 3-year | 2018-06-30      |
| dddd4444             | 3-year | 2019-12-31      |

- You can merge `aaaa1111` and `bbbb2222` and exchange
  them for a 1-year Convertible Reserved Instance. You cannot exchange them for a 3-year Convertible Reserved Instance. The
  expiration date of the new Convertible Reserved Instance is 2018-12-31.
- You can merge `bbbb2222` and `cccc3333` and exchange
  them for a 3-year Convertible Reserved Instance. You cannot exchange them for a 1-year Convertible Reserved Instance. The
  expiration date of the new Convertible Reserved Instance is 2018-07-31.
- You can merge `cccc3333` and `dddd4444` and exchange
  them for a 3-year Convertible Reserved Instance. You cannot exchange them for a 1-year Convertible Reserved Instance. The
  expiration date of the new Convertible Reserved Instance is 2019-12-31.

## Exchange a portion of a Convertible Reserved Instance

You can use the modification process to split your Convertible Reserved Instance into smaller
reservations, and then exchange one or more of the new reservations for a new Convertible Reserved Instance.
The following examples demonstrate how you can do this.

###### Example: Convertible Reserved Instance with multiple instances

In this example, you have a `t2.micro` Convertible Reserved Instance with four instances in
the reservation. To exchange two `t2.micro` instances for an
`m4.xlarge` instance:

1. Modify the `t2.micro` Convertible Reserved Instance by splitting it into two
   `t2.micro` Convertible Reserved Instances with two instances each.
2. Exchange one of the new `t2.micro` Convertible Reserved Instances for an
   `m4.xlarge` Convertible Reserved Instance.

![Modifying and exchange Reserved Instances.](images/ri-split-cri-multiple.png)

###### Example: Convertible Reserved Instance with a single instance

In this example, you have a `t2.large` Convertible Reserved Instance. To change it to a
smaller `t2.medium` instance and a `m3.medium`
instance:

1. Modify the `t2.large` Convertible Reserved Instance by splitting it into two
   `t2.medium` Convertible Reserved Instances. A single `t2.large`
   instance has the same instance size footprint as two
   `t2.medium` instances.
2. Exchange one of the new `t2.medium` Convertible Reserved Instances for an
   `m3.medium` Convertible Reserved Instance.

![Modify and exchange Reserved Instances.](images/ri-split-cri-single.png)
For more information, see [Support for modifying instance
sizes](ri-modifying.md#ri-modification-instancemove "ri-modifying.md#ri-modification-instancemove") and [Submit exchange requests](#ri-exchange-process "#ri-exchange-process").

## Submit exchange requests

You can exchange your Convertible Reserved Instances. Reserved Instances that are exchanged are retired.

Console

###### To exchange Convertible Reserved Instances

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. Choose **Reserved Instances**, select the
   Convertible Reserved Instances to exchange, and choose **Actions**,
   **Exchange Reserved Instance**.
3. Select the attributes of the desired configuration, and choose
   **Find offering**.
4. Select a new Convertible Reserved Instance. At the bottom of the screen, you can view
   the number of Reserved Instances that you receive for the exchange, and any
   additional costs.
5. When you have selected a Convertible Reserved Instance that meets your needs, choose
   **Review**.
6. Choose **Exchange**, and then
   **Close**.

AWS CLI

###### To exchange a Convertible Reserved Instance

1. Find a new Convertible Reserved Instance that meets your needs by using the [describe-reserved-instances-offerings](../../../cli/latest/reference/ec2/describe-reserved-instances-offerings.md "../../../cli/latest/reference/ec2/describe-reserved-instances-offerings.md")
   command.
2. Get a quote for the exchange by using the [get-reserved-instances-exchange-quote](../../../cli/latest/reference/ec2/get-reserved-instances-exchange-quote.md "../../../cli/latest/reference/ec2/get-reserved-instances-exchange-quote.md") command. This
   includes the number of Reserved Instances you get from the exchange, and the
   true-up cost for the exchange:
3. Perform the exchange by using the [accept-reserved-instances-exchange-quote](../../../cli/latest/reference/ec2/accept-reserved-instances-exchange-quote.md "../../../cli/latest/reference/ec2/accept-reserved-instances-exchange-quote.md")
   command.

PowerShell

###### To exchange a Convertible Reserved Instance

1. Find a new Convertible Reserved Instance that meets your needs by using the [Get-EC2ReservedInstancesOffering](../../../powershell/latest/reference/items/Get-EC2ReservedInstancesOffering.md "../../../powershell/latest/reference/items/Get-EC2ReservedInstancesOffering.md") cmdlet.
2. Get a quote for the exchange by using the [GetEC2-ReservedInstancesExchangeQuote](../../../powershell/latest/reference/items/Get-EC2ReservedInstancesExchangeQuote.md "../../../powershell/latest/reference/items/Get-EC2ReservedInstancesExchangeQuote.md") cmdlet. This
   includes the number of Reserved Instances you get from the exchange, and the
   true-up cost for the exchange:
3. Perform the exchange by using the [Approve-EC2ReservedInstancesExchangeQuote](../../../powershell/latest/reference/items/Approve-EC2ReservedInstancesExchangeQuote.md "../../../powershell/latest/reference/items/Approve-EC2ReservedInstancesExchangeQuote.md")
   cmdlet
