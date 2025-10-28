# Understanding reservations in Cost Explorer

Balancing your reservation usage and your On-Demand instance or provisioned capacity usage
can help you achieve better efficiency. To help, Cost Explorer provides tools that help you
understand where your greatest reservation costs are and how you can potentially lower your
costs. Cost Explorer provides you with an overview of your current reservations, shows your
utilization and coverage, and calculates reservation recommendations that could save you
money if you purchase them.

## Using your reservation reports

You can use the **Reservations Overview** page in the Billing and Cost
Management console to see how many reservations you have, how much your reservations are
saving you compared to similar usage of On-Demand Instances, and how many of your
reservations are expiring this month.

Cost Explorer breaks down your reservations and savings by service and lists your potential
savings; that is, the cost of On-Demand usage compared to what that usage could cost you
with a reservation.

To use your potential savings, see [Accessing reservation recommendations](ri-recommendations.md "ri-recommendations.md").

## Managing your reservation expiration alerts

You can track your reservations and when those reservations expire in Cost Explorer. With
reservation expiration alerts, you receive email alerts 7, 30, or 60 days in advance
before your reservation expires. These alerts can be sent to up to 10 email recipients.
You can also choose to be notified on the day that your reservation expires. Reservation
expiration alerts are supported for Amazon EC2, Amazon RDS, Amazon Redshift, Amazon ElastiCache, and Amazon OpenSearch Service
reservations.

###### To turn on reservation expiration alerts

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. Navigate to the **Overview** page under the
   **Reservations** section.
3. Choose **Manage alert subscriptions** in the upper right corner.
4. Select the check boxes for when you want to receive your alerts.
5. Enter email addresses for who you want to notify. You can have up to 10 email
   recipients.
6. Choose **Save**.

AWS starts monitoring your reservation portfolio and sends alerts based on the preferences
that you specify.
