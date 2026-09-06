

# Creating a global endpoint in Amazon EventBridge
<a name="eb-ge-create-endpoint"></a>

Complete the following steps to set up a global endpoint:

1. Make sure that you have matching event buses and rules in both the primary and secondary Region.

1. Create a [Route 53 health check](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-creating.html) to monitor your event buses. For assistance in creating your health check, choose **New Health Check** when creating your global endpoint.

1. Create your global endpoint.

Once you have set up the Route 53 health check, you can create a global endpoint.

## To create a global endpoint by using the console
<a name="eb-ge-create-endpoint-console"></a>

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/).

1. In the navigation pane, choose **Global endpoints**.

1. Choose **Create Endpoint**.

1. Enter a name and description for the endpoint.

1. For **Event bus in primary Region**, choose the event bus you’d like the endpoint associated with.

1. For **Secondary Region**, choose the Region you'd like to direct events to in the event of a failover.
**Note**  
The **Event bus in secondary Region** is auto-filled and not editable.

1. For **Route 53 health check for triggering failover and recovery**, choose the health check that the endpoint will monitor. If you don't already have a health check, choose **New Health check** to open the CloudFormation console and create a health check using a CloudFormation template.
**Note**  
Missing data will cause the health check to fail. If you only need to send events intermittently, consider using a longer **MinimumEvaluationPeriod**, or treat missing data as 'missing' instead of 'breaching'.

1. (Optional) For **Event replication** do the following:

   1. Select **Event replication enabled**.

   1. For **Execution role**, choose whether to create a new AWS Identity and Access Management role or use an existing one. Do the following:
      + Choose **Create a new role for this specific resource**. Optionally, you can update the **Role name** to create a new role.
      + Choose **Use existing role**. Then, for **Execution role**, choose the desired role to use.

1. Choose **Create**.

## To create a global endpoint by using the API
<a name="eb-ge-create-endpoint-api"></a>

To create a global endpoint using the EventBridge API, see [CreateEndpoint](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_CreateEndpoint.html) in the Amazon EventBridge API Reference.

## To create a global endpoint by using CloudFormation
<a name="eb-ge-create-endpoint-cfn"></a>

To create a global endpoint using the AWS CloudFormation API, see [AWS::Events::Endpoints](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-endpoint.html) in the AWS CloudFormation User Guide.