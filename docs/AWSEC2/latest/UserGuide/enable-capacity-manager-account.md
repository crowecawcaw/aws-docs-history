# Enabling EC2 Capacity Manager at the account-level

Enable Capacity Manager at the account-level to monitor and analyze your EC2 capacity usage within a single AWS account. After you enable it, Capacity Manager
collects data about your On-Demand Instances, Spot Instances, and Capacity Reservations to help you identify optimization
opportunities and track usage patterns.

## Enable Capacity Manager at the account-level

Console

###### To enable Capacity Manager for your account

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Capacity Manager**.
3. On the Capacity Manager page, choose **Enable in Region**.

AWS CLI

###### To enable Capacity Manager for your account

Run the following command:

```

aws ec2 enable-capacity-manager

```

###### Note

- After you enable Capacity Manager, it collects and aggregates 14 days of historical data. This process might take a few hours.
- While collecting your historical data, an `initial-ingestion-in-progress` state will be displayed. During this collection
  period you might observe gaps in your historical data. Once data collection is complete, an `ingestion-complete` state will be displayed.
