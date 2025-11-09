# Monitoring readiness status in ARC

You can see readiness for your application in Amazon Application Recovery Controller (ARC) at the following levels:

- The readiness check level for the resources in a resource set
- The individual resource level
- The cell (application replica) level for all the resources in an Availability Zone or AWS Region
- The recovery group level for the application as a whole
  You can be notified about readiness status changes, or you can monitor readiness status changes in the Route 53 console or by using ARC CLI commands.

## Readiness status notification

You can use Amazon EventBridge to set up event-driven rules to monitor ARC resources and notify you about changes in readiness status.
For more information, see [Using readiness check in ARC with Amazon EventBridge](eventbridge-readiness.md "eventbridge-readiness.md").

## Monitoring readiness status in the

ARC console

The following procedure describes how to monitor recovery readiness in the AWS Management Console.

1. Open the ARC console at [https://console.aws.amazon.com/route53recovery/home#/dashboard](https://console.aws.amazon.com/route53recovery/home#/dashboard "https://console.aws.amazon.com/route53recovery/home#/dashboard").
2. Choose **Readiness check**.
3. On the **Readiness** page, under **Recovery group**, view the
   **Recovery group readiness status** for each recovery group (application).

You can also view the readiness of specific cells or individual resources.

## Monitoring readiness status

by using CLI commands

This section provides examples of AWS CLI commands to use to see the readiness status for your application and resources at different levels.

**Readiness for a resource set**
The status of a readiness check you've created for a resource set (a group of resources).

`aws route53-recovery-readiness --region us-west-2 get-readiness-check-status --readiness-check-name `ReadinessCheckName``

**Readiness for a single resource**
To get the status of a single resource in a readiness check, including the status of each readiness rule that is checked,
specify the readiness check name and a resource ARN. For example:

`aws route53-recovery-readiness --region us-west-2 get-readiness-check-status --readiness-check-name
 `ReadinessCheckName` --resource-arn
 "arn:aws:dynamodb:us-west-2:111122223333:table/`TableName`"`

**Readiness for a cell**
The status of a single cell, that is, a Region or Availability Zone.

`aws route53-recovery-readiness --region us-west-2 get-cell-readiness-summary --cell-name `CellName``

**Readiness for an application**
The status of the overall application, at the recovery group level.

`aws route53-recovery-readiness --region us-west-2 get-recovery-group-readiness-summary --recovery-group-name 
 `RecoveryGroupName``
