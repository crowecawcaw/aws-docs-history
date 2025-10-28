# Creating a global endpoint in Amazon EventBridge

Complete the following steps to set up a global endpoint:

1. Make sure that you have matching event buses and rules in both the primary and
   secondary Region.
2. Create a [Route 53 health
   check](../../../Route53/latest/DeveloperGuide/health-checks-creating.md "../../../Route53/latest/DeveloperGuide/health-checks-creating.md") to monitor your event buses. For assistance in creating your health check,
   choose **New Health Check** when creating your global endpoint.
3. Create your global endpoint.
   Once you have set up the Route 53 health check, you can create a global endpoint.

## To create a global endpoint by using the

console

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, choose **Global endpoints**.
3. Choose **Create Endpoint**.
4. Enter a name and description for the endpoint.
5. For **Event bus in primary Region**, choose the event bus you’d
   like the endpoint associated with.
6. For **Secondary Region**, choose the Region you'd like to direct
   events to in the event of a failover.

###### Note

The **Event bus in secondary Region** is auto-filled and not
editable. 7. For **Route 53 health check for triggering failover and recovery**,
choose the health check that the endpoint will monitor. If you don't already have a
health check, choose **New Health check** to open the AWS CloudFormation console and
create a health check using a CloudFormation template.

###### Note

Missing data will cause the health check to fail. If you only need to send events
intermittently, consider using a longer **MinimumEvaluationPeriod**,
or treat missing data as 'missing' instead of 'breaching'. 8. (Optional) For **Event replication** do the following:

    1. Select **Event replication enabled**.
    2. For **Execution role**, choose whether to create a new
     AWS Identity and Access Management role or use an existing one. Do the following:




    	* Choose **Create a new role for this specific resource**.
    	 Optionally, you can update the **Role name** to create a new
    	 role.
    	* Choose **Use existing role**. Then, for **Execution
    	 role**, choose the desired role to use.

9. Choose **Create**.

## To create a global endpoint by using the

API

To create a global endpoint using the EventBridge API, see [CreateEndpoint](../APIReference/API_CreateEndpoint.md "../APIReference/API_CreateEndpoint.md") in
the Amazon EventBridge API Reference.

## To create a global endpoint by using

AWS CloudFormation

To create a global endpoint using the AWS CloudFormation API, see [AWS::Events::Endpoints](../../../AWSCloudFormation/latest/UserGuide/aws-resource-events-endpoint.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-events-endpoint.md") in the AWS CloudFormation User Guide.
