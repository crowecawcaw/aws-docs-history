

# Canceling an active reservation
<a name="canceling-active-reservation"></a>

You can cancel an active reservation during the calendar month (UTC) in which you purchased it. The reservation ends when you cancel it. You pay On-Demand rates for usage that the reservation would have covered that month.

You can't cancel these reservations:
+ A reservation that you purchased in an earlier month, including a reservation that renewed automatically.
+ Any reservation during the last hour of the month, from 23:00 UTC on the last day of the month until 00:00 UTC on the 1st. If you purchased the reservation this month, you can't cancel it after the month ends.

**To cancel a reservation (console)**

1. Open the MediaLive console at [https://console.aws.amazon.com/medialive/](https://console.aws.amazon.com/medialive/).

1. In the navigation pane, choose **Reservations**.

1. Choose the reservation name, and then choose **Cancel reservation**.

1. In the confirmation dialog box, choose **Cancel reservation**.

**To cancel a reservation (AWS CLI)**
+ Run the following command:

  `aws medialive delete-reservation --reservation-id {{reservation-id}}`