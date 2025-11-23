# Interruptible Capacity Reservations for capacity consumers

The capacity consumer is the account that launches instances into shared interruptible Capacity Reservations, understanding that their instances may be terminated when the owner reclaims capacity.

This section covers how you (the capacity consumer) can launch instances into an interruptible Capacity Reservation and learn about what happens when capacity is reclaimed by the owner.

###### Topics

- [View an interruptible Capacity Reservation](#view-interruptible-cr-consumer "#view-interruptible-cr-consumer")
- [Launch instances into interruptible reservations](#launch-instances-interruptible "#launch-instances-interruptible")
- [Interruption experience](#interruption-experience "#interruption-experience")

## View an interruptible Capacity Reservation

Use the following procedures to view an interruptible Capacity Reservation.

Console

###### To view interruptible Capacity Reservations in your account

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. Choose **Capacity Reservations**.
3. In the **Type** column, look for reservations marked as **Interruptible**.
4. Note the reservation IDs for use in your instance launches.

AWS CLI

###### To find all interruptible Capacity Reservations in your account

Use the [describe-capacity-reservations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-capacity-reservations.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-capacity-reservations.html") command:

```
aws ec2 describe-capacity-reservations \
--filters Name=state,Values=active
```

Look for reservations where `Interruptible` is set to `true` in the response.

###### To filter specifically for interruptible reservations

Use the following command:

```
aws ec2 describe-capacity-reservations \
--capacity-reservation-ids `cr-example123` \
--query 'CapacityReservations[?Interruptible==`true`]'
```

###### Note

Interruptible Capacity Reservations are by default targeted Capacity Reservations, so you need to target them specifically
in your instance launch. Unlike open reservations, interruptible reservations will not automatically cover matching instances.
You must explicitly specify the reservation ID when launching.

## Launch instances into interruptible reservations

Use the following procedure to launch Amazon EC2 instances into interruptible Capacity Reservations within your account.

###### Note

We recommend that you only use interruptible Capacity Reservations for applications that can be interrupted.

Console

###### To launch instances into interruptible Capacity Reservations

1. Open the Amazon Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. From the Amazon EC2 dashboard, choose **Launch instance**.
3. Configure your instance settings.
4. In **Advanced details** for Capacity Reservation, choose **Launch interruptible instances in your active reservation**.
5. Select the interruptible reservation ID and the new instance purchasing option.
6. Choose **Launch instance**.

AWS CLI

```
aws ec2 run-instances \
--instance-type `m5.large` \
--count `2` \
--image-id `ami-12345678` \
--instance-market-options '{
    "MarketType": "interruptible-capacity-reservation"
}' \
--capacity-reservation-specification '{
    "CapacityReservationTarget": {
        "CapacityReservationId": "`cr-abcdef1234567890`"
    }
}'
```

### Launch instances with Auto Scaling Groups

You can also launch instances into interruptible reservations using Auto Scaling Groups with launch templates. Configure the launch template
with the interruptible market type and reservation ID, then create your Auto Scaling Group using that template. For more information, see
[Interruptible Capacity Reservations
with EC2 Auto Scaling](../../../autoscaling/ec2/userguide/asg-interruptible-capacity-reservations.md "../../../autoscaling/ec2/userguide/asg-interruptible-capacity-reservations.md").

## Interruption experience

When capacity is reclaimed by the owner, you receive an interruption notice 2 minutes before instance termination. This warning comes through EventBridge events, giving you time to:

- Save your work or checkpoint your applications
- Shut down processes
- Prepare for instance termination

The EventBridge event includes details about which instances will be terminated and the exact termination time. For more information, see [Instance interruption warning](monitor-interruptible-cr.md#instance-interruption-warning "monitor-interruptible-cr.md#instance-interruption-warning").
