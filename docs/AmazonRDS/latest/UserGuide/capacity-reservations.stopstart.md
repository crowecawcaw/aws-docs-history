

# Stopping and starting a DB instance in a reservation
<a name="capacity-reservations.stopstart"></a>

When you stop a DB instance that is using reserved capacity, the instance stays associated with the reservation, but the capacity it was using is released back to the reservation for other DB instances to use. Stopping a DB instance does not hold capacity aside for it.

Because the association persists, starting the instance again returns it to the same reservation – you don't need to specify the reservation on start. Amazon RDS places it back into the reservation using whatever capacity is available at that point.

**Important**  
Reserved capacity is targeted, so a start that returns a DB instance to its reservation fails if the reservation has no available capacity in that DB instance's Availability Zone. It does not fall back to On-Demand capacity. Because stopping the instance releases the capacity, another DB instance can take it while the instance is stopped. If you depend on being able to restart into the reservation, avoid launching other DB instances into that capacity in the meantime.

Stopping a DB instance doesn't change what the reservation costs. The reservation is billed for its full reserved capacity whether DB instances are running in it, so capacity left unused while your instance is stopped appears as an unused reservation charge.

To drop the association as well, release the reserved capacity when you stop the instance. The instance is then no longer associated with the reservation, so it starts as a normal On-Demand instance the next time you start it, unless you specify a reservation on start. To place a stopped DB instance into a reservation, or to move it into a different one, specify the reservation when you start it.

## Console
<a name="capacity-reservations.stopstart.console"></a>

**To stop a DB instance in a reservation**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Databases**, and then choose the DB instance that you want to stop.

1. For **Actions**, choose **Stop temporarily**.

1. In the **Stop DB instance temporarily** window, under **Acknowledgement**, select the check box.

1. (Optional) To drop the association with the reservation, under **Additional actions**, select **Release reserved capacity**. If you don't select it, the DB instance stays associated with the reservation and returns to it when you start the DB instance.  
![The "Stop DB instance temporarily" window, with the "Release reserved capacity" check box under "Additional actions - optional".](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/odcr-stop-db-instance.png)

1. Choose **Stop temporarily**.

**To start a DB instance in a reservation**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Databases**, and then choose the stopped DB instance that you want to start.

1. For **Actions**, choose **Start**.

1. (Optional) To place the DB instance into a reservation, or to move it into a different one, for **Specify capacity reservation**, choose the reservation. If you keep **No capacity reservation** selected, a DB instance that is still associated with a reservation returns to that reservation.  
![The Start DB instance window, with the Specify Capacity Reservation list.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/odcr-start-db-instance.png)

1. Choose **Start DB instance**.

## AWS CLI
<a name="capacity-reservations.stopstart.cli"></a>

To also remove the association with the reservation when you stop the DB instance, add `--detach-from-db-capacity-reservation` to the [stop-db-instance](https://docs.aws.amazon.com/cli/latest/reference/rds/stop-db-instance.html) command:

```
1. aws rds stop-db-instance \
2.     --db-instance-identifier {{my-db-instance}} \
3.     --detach-from-db-capacity-reservation
```

To place a stopped DB instance into a reservation, or to move it into a different one, specify the reservation in the [start-db-instance](https://docs.aws.amazon.com/cli/latest/reference/rds/start-db-instance.html) command:

```
1. aws rds start-db-instance \
2.     --db-instance-identifier {{my-db-instance}} \
3.     --db-capacity-reservation-identifier {{my-reservation}}
```

The start fails if the reservation you specify has no available capacity in that DB instance's Availability Zone. This is the same as when a DB instance returns to its existing reservation.

## RDS API
<a name="capacity-reservations.stopstart.api"></a>

To drop the association when you stop a DB instance, set `DetachFromDBCapacityReservation` to `true` in the [StopDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_StopDBInstance.html) operation.

To place a stopped DB instance into a reservation, or to move it into a different one, specify `DBCapacityReservationIdentifier` in the [StartDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_StartDBInstance.html) operation.