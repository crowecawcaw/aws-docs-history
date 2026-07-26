# Getting started with Amazon ECS Action Logs

Amazon ECS Action Logs use the Amazon CloudWatch Logs vended log delivery mechanism to publish
detailed records of service actions to your preferred destination. When you enable
Action Logs, you can see every step that Amazon ECS takes during deployments and daemon
operations, including infrastructure provisioning, resource registration, and failure
details. This visibility helps you troubleshoot issues without contacting AWS
Support and reduces the time to identify root causes. You can enable Action Logs for
your clusters using the Amazon ECS console or CloudWatch Logs APIs.

## Prerequisites

Before you enable Action Logs, verify that your IAM identity has the
required permissions.

### Required IAM permissions

Your IAM identity must have the following permissions to enable and
manage Action Logs:

```
{
    "Effect": "Allow",
    "Action": [
        "logs:PutDeliverySource",
        "logs:PutDeliveryDestination",
        "logs:CreateDelivery",
        "logs:GetDelivery",
        "ecs:AllowVendedLogDeliveryForResource"
    ],
    "Resource": "*"
}
```

### Destination resource policy

The destination CloudWatch Logs log group must have a resource policy that
allows the `delivery.logs.amazonaws.com` service to write logs. Add
the following statement to the log group resource policy:

```
{
    "Effect": "Allow",
    "Principal": {
        "Service": "delivery.logs.amazonaws.com"
    },
    "Action": [
        "logs:CreateLogStream",
        "logs:PutLogEvents"
    ],
    "Resource": "arn:aws:logs:`region`:`account-id`:log-group:`log-group-name`:log-stream:*"
}
```

## Enable Action Logs using the Amazon ECS console

You can enable Action Logs directly from the cluster details page in the
Amazon ECS console.

###### To enable Action Logs using the console

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. In the navigation pane, choose **Clusters**,
   and then select the cluster.
3. Choose the **Configuration** tab.
4. In the **Action logs** section, choose
   **Add**.
5. For **Destination**, choose one of the
   following:

   - **CloudWatch Logs** (default)
   - **Amazon S3**
   - **Amazon Data Firehose**
     For CloudWatch Logs, Amazon ECS creates a default log group named
     `/aws/vendedlogs/ecs/action-logs/`cluster-name``
     with a 7-day retention period.

6. Choose **Save**.

## Enable Action Logs using CloudWatch Logs APIs

You can enable Action Logs programmatically by using the CloudWatch Logs vended log
delivery APIs. This approach requires three steps: register the delivery source,
configure the destination, and create the delivery.

###### To enable Action Logs using the AWS CLI

1. Register the delivery source by running the following command:

```
aws logs put-delivery-source \
    --name `my-ecs-action-logs` \
    --resource-arn arn:aws:ecs:`region`:`account-id`:cluster/`cluster-name` \
    --log-type EcsActionLogs
```

2. Configure the delivery destination by running the following
   command:

```
aws logs put-delivery-destination \
    --name `my-ecs-logs-destination` \
    --output-format json \
    --delivery-destination-configuration '{"destinationResourceArn": "arn:aws:logs:`region`:`account-id`:log-group:/aws/vendedlogs/ecs/action-logs/`cluster-name`"}'
```

3. Create the delivery to link the source to the destination by running
   the following command:

```
aws logs create-delivery \
    --delivery-source-name `my-ecs-action-logs` \
    --delivery-destination-arn arn:aws:logs:`region`:`account-id`:delivery-destination:`my-ecs-logs-destination`
```

## Verify log delivery

After you enable Action Logs, verify that logs are delivered to your
destination.

###### To verify log delivery

1. Trigger an action in your cluster. For example, create or update a
   daemon service.
2. Open the CloudWatch console at
   https://console.aws.amazon.com/cloudwatch/.
3. In the navigation pane, choose **Log
   groups**.
4. Select your Action Logs log group and verify that new log streams
   appear.

## Delete Action Logs

You can delete Action Logs by using the AWS CLI or the Amazon ECS
console.

To delete Action Logs, your IAM identity must have the following additional
permissions:

```
{
    "Effect": "Allow",
    "Action": [
        "logs:DeleteDelivery",
        "logs:DeleteDeliverySource",
        "logs:DeleteDeliveryDestination"
    ],
    "Resource": "*"
}
```

###### To delete Action Logs using the AWS CLI

1. Delete the delivery by running the following command:

```
aws logs delete-delivery \
    --delivery-id `delivery-id`
```

2. Delete the delivery source by running the following command:

```
aws logs delete-delivery-source \
    --name `my-ecs-action-logs`
```

3. Delete the delivery destination by running the following
   command:

```
aws logs delete-delivery-destination \
    --name `my-ecs-logs-destination`
```

To delete Action Logs using the console, navigate to the cluster details page,
choose the **Configuration** tab, and then choose
**Delete** in the **Action logs** section.

## Next steps

After you enable Action Logs, use the following resources to monitor and
troubleshoot your Amazon ECS clusters:

- [Troubleshooting with Amazon ECS Action Logs](action-logs-troubleshooting.md "action-logs-troubleshooting.md")
