

# Creating logs in embedded metric format using the client libraries
<a name="CloudWatch_Embedded_Metric_Format_Libraries"></a>

 You can use the open-sourced client libraries that Amazon provides to create embedded metric format logs. Full examples for different setups can be found in our client libraries under **/examples**. The libraries and the instructions for how to use them are located on Github. 
+ [Node.Js](https://github.com/awslabs/aws-embedded-metrics-node)
+ [Python](https://github.com/awslabs/aws-embedded-metrics-python)
+ [Java](https://github.com/awslabs/aws-embedded-metrics-java)
+ [C\#](https://github.com/awslabs/aws-embedded-metrics-dotnet)

Client libraries are meant to work out of the box with the CloudWatch agent. Generated embedded metric format logs are sent to the CloudWatch agent, which then aggregates and publishes them to CloudWatch Logs for you.