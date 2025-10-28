# Creating logs in embedded metric format using the client libraries

You can use the open-sourced client libraries that Amazon provides to create embedded metric format logs.
Full examples for different setups can be found in our client libraries under **/examples**.
The libraries and the instructions for how to use them are located on Github.

- [Node.Js](https://github.com/awslabs/aws-embedded-metrics-node "https://github.com/awslabs/aws-embedded-metrics-node")

###### Note

For Node.js, versions 4.1.1+, 3.0.2+, 2.0.7+ are required for use with the Lambda JSON log format.
Using previous versions in such Lambda environments will lead to metric loss.

For more information, see
[Accessing Amazon CloudWatch logs for AWS Lambda](../../../lambda/latest/dg/monitoring-cloudwatchlogs.md "../../../lambda/latest/dg/monitoring-cloudwatchlogs.md").

- [Python](https://github.com/awslabs/aws-embedded-metrics-python "https://github.com/awslabs/aws-embedded-metrics-python")
- [Java](https://github.com/awslabs/aws-embedded-metrics-java "https://github.com/awslabs/aws-embedded-metrics-java")
- [C#](https://github.com/awslabs/aws-embedded-metrics-dotnet "https://github.com/awslabs/aws-embedded-metrics-dotnet")
  Client libraries are meant to work out of the box with the CloudWatch agent. Generated embedded metric format logs
  are sent to the CloudWatch agent, which then aggregates and publishes them to CloudWatch Logs for you.

###### Note

When using Lambda, no agent is required to send the logs to CloudWatch. Anything logged to STDOUT is
sent to CloudWatch Logs via the Lambda Logging Agent.
