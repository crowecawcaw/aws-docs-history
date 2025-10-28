# Viewing the billing for reserved DB instances for Amazon RDS

You can view the billing for your reserved DB instances in the Billing Dashboard in the AWS Management Console.

###### To view reserved DB instance billing

1. Sign in to the AWS Management Console.
2. From the **account menu** at the upper right, choose **Billing Dashboard**.
3. Choose **Bill Details** at the upper right of the dashboard.
4. Under **AWS Service Charges**, expand **Relational Database Service**.
5. Expand the AWS Region where your reserved DB instances are, for example **US West
   (Oregon)**.

Your reserved DB instances and their hourly charges for the current month are shown under **Amazon Relational
Database Service for `Database Engine` Reserved Instances**.

![View monthly costs for a reserved DB instance](images/ri-db-billing1.png)

The reserved DB instance in this example was purchased All Upfront, so there are no hourly charges. 6. Choose the **Cost Explorer** (bar graph) icon next to the **Reserved Instances**
heading.

The Cost Explorer displays the **Monthly EC2 running hours costs and usage** graph. 7. Clear the **Usage Type Group** filter to the right of the graph. 8. Choose the time period and time unit for which you want to examine usage costs.

The following example shows usage costs for on-demand and reserved DB instances for the year to date by month.

![View usage costs for on-demand and reserved DB instances](images/ri-db-billing2.png)

The reserved DB instance costs from January through June 2021 are monthly charges for a Partial Upfront instance,
while the cost in August 2021 is a one-time charge for an All Upfront instance.

The reserved instance discount for the Partial Upfront instance expired in June 2021, but the DB instance wasn't
deleted. After the expiration date, it was simply charged at the on-demand rate.
