# Recommended alarms

The following sections list the metrics that we recommend that you set best practice
 alarms for. For each metric, the dimensions, alarm intent, recommended threshold, threshold
 justification, and the period length and number of datapoints is also displayed.

Some metrics might appear twice in the list. This happens when different alarms are
 recommended for different combinations of dimensions of that metric.

**Datapoints to alarm** is the number of data points that
 must be breaching to send the alarm into ALARM state. **Evaluation
 periods** is the number of periods that are taken into account when the alarm is
 evaluated. If these numbers are the same, the alarm goes into ALARM state only when that
 number of consecutive periods have values that breach the threshold. If **Datapoints to alarm** is lower than **Evaluation
 periods**, then it is an "M out of N" alarm and the alarm goes into ALARM state
 if at least **Datapoints to alarm** data points are breaching
 within any **Evaluation periods** set of data points. For more
 information, see [Evaluating an alarm](AlarmThatSendsEmail.md#alarm-evaluation "AlarmThatSendsEmail.md#alarm-evaluation").

###### Topics

* [Amazon API Gateway](#ApiGateway "#ApiGateway")
* [Amazon EC2 Auto Scaling](#AutoScaling "#AutoScaling")
* [AWS Certificate Manager (ACM)](#CertificateManager "#CertificateManager")
* [Amazon CloudFront](#CloudFront "#CloudFront")
* [Amazon Cognito](#Cognito "#Cognito")
* [Amazon DynamoDB](#DynamoDB "#DynamoDB")
* [Amazon EBS](#Recommended_EBS "#Recommended_EBS")
* [Amazon EC2](#EC2 "#EC2")
* [Amazon ElastiCache](#ElastiCache "#ElastiCache")
* [Amazon ECS](#ECS "#ECS")
* [Amazon ECS with Container Insights](#ECS-ContainerInsights "#ECS-ContainerInsights")
* [Amazon ECS with Container Insights with enhanced observability](#ECS-ContainerInsights_enhanced "#ECS-ContainerInsights_enhanced")
* [Amazon EFS](#EFS "#EFS")
* [Amazon EKS with Container Insights](#EKS-ContainerInsights "#EKS-ContainerInsights")
* [Amazon EventBridge Scheduler](#Eventbridge-Scheduler "#Eventbridge-Scheduler")
* [Amazon Kinesis Data Streams](#Kinesis "#Kinesis")
* [Lambda](#Lambda "#Lambda")
* [Lambda Insights](#LambdaInsights "#LambdaInsights")
* [Amazon VPC (AWS/NATGateway)](#NATGateway "#NATGateway")
* [AWS Private Link (AWS/PrivateLinkEndpoints)](#PrivateLinkEndpoints "#PrivateLinkEndpoints")
* [AWS Private Link (AWS/PrivateLinkServices)](#PrivateLinkServices "#PrivateLinkServices")
* [Amazon RDS](#RDS "#RDS")
* [Amazon Route 53 Public Data Plane](#Route53 "#Route53")
* [Amazon S3](#S3 "#S3")
* [S3ObjectLambda](#S3ObjectLambda "#S3ObjectLambda")
* [Amazon SNS](#SNS "#SNS")
* [Amazon SQS](#SQS "#SQS")
* [AWS VPN](#VPN "#VPN")

## Amazon API Gateway




**4XXError**

**Dimensions:** ApiName, Stage


**Alarm description:** This alarm detects a high rate of client-side errors. This can indicate an issue in the authorization or client request parameters. It could also mean that a resource was removed or a client is requesting one that doesn't exist. Consider enabling CloudWatch Logs and checking for any errors that may be causing the 4XX errors. Moreover, consider enabling detailed CloudWatch metrics to view this metric per resource and method and narrow down the source of the errors. Errors could also be caused by exceeding the configured throttling limit. If the responses and logs are reporting high and unexpected rates of 
 429 errors, follow [this guide](https://repost.aws/knowledge-center/api-gateway-429-limit "https://repost.aws/knowledge-center/api-gateway-429-limit") to troubleshoot this issue.


**Intent:** This alarm can detect high rates of client-side errors for the API Gateway requests.


**Statistic:** Average


**Recommended threshold:** 0.05


**Threshold justification:** The suggested threshold detects when more than 5% of total requests are getting 4XX errors. However, you can tune the threshold to suit the traffic of the requests as well as acceptable error rates. You can also analyze historical data to determine the acceptable error rate for the application workload and then tune the threshold accordingly. Frequently occurring 4XX errors need to be alarmed on. However, setting a very low value for the threshold can cause the alarm to be too sensitive.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**5XXError**

**Dimensions:** ApiName, Stage


**Alarm description:** This alarm helps to detect a high rate of server-side errors. This can indicate that there is something wrong on the API backend, the network, or the integration between the API gateway and the backend API. This [documentation](https://repost.aws/knowledge-center/api-gateway-5xx-error "https://repost.aws/knowledge-center/api-gateway-5xx-error") can help you troubleshoot the cause of 5xx errors.


**Intent:** This alarm can detect high rates of server-side errors for the API Gateway requests.


**Statistic:** Average


**Recommended threshold:** 0.05


**Threshold justification:** The suggested threshold detects when more than 5% of total requests are getting 5XX errors. However, you can tune the threshold to suit the traffic of the requests as well as acceptable error rates. you can also analyze historical data to determine the acceptable error rate for the application workload and then tune the threshold accordingly. Frequently occurring 5XX errors need to be alarmed on. However, setting a very low value for the threshold can cause the alarm to be too sensitive.


**Period:** 60


**Datapoints to alarm:** 3


**Evaluation periods:** 3


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**Count**

**Dimensions:** ApiName, Stage


**Alarm description:** This alarm helps to detect low traffic volume for the REST API stage. This can be an indicator of an issue with the application calling the API such as using incorrect endpoints. It could also be an indicator of an issue with the configuration or permissions of the API making it unreachable for clients.


**Intent:** This alarm can detect unexpectedly low traffic volume for the REST API stage. We recommend that you create this alarm if your API receives a predictable and consistent number of requests under normal conditions. If you have detailed CloudWatch metrics enabled and you can predict the normal traffic volume per method and resource, we recommend that you create alternative alarms to have more fine-grained monitoring of traffic volume drops for each resource and method. This alarm is not recommended for APIs that don't expect constant and consistent traffic.


**Statistic:** SampleCount


**Recommended threshold:** Depends on your situation


**Threshold justification:** Set the threshold based on historical data analysis to determine what the expected baseline request count for your API is. Setting the threshold at a very high value might cause the alarm to be too sensitive at periods of normal and expected low traffic. Conversely, setting it at a very low value might cause the alarm to miss anomalous smaller drops in traffic volume.


**Period:** 60


**Datapoints to alarm:** 10


**Evaluation periods:** 10


**Comparison Operator:** LESS\_THAN\_THRESHOLD



**Count**

**Dimensions:** ApiName, Stage, Resource, Method


**Alarm description:** This alarm helps to detect low traffic volume for the REST API resource and method in the stage. This can indicate an issue with the application calling the API such as using incorrect endpoints. It could also be an indicator of an issue with the configuration or permissions of the API making it unreachable for clients.


**Intent:** This alarm can detect unexpectedly low traffic volume for the REST API resource and method in the stage. We recommend that you create this alarm if your API receives a predictable and consistent number of requests under normal conditions. This alarm is not recommended for APIs that don't expect constant and consistent traffic.


**Statistic:** SampleCount


**Recommended threshold:** Depends on your situation


**Threshold justification:** Set the threshold based on historical data analysis to determine what the expected baseline request count for your API is. Setting the threshold at a very high value might cause the alarm to be too sensitive at periods of normal and expected low traffic. Conversely, setting it at a very low value might cause the alarm to miss anomalous smaller drops in traffic volume.


**Period:** 60


**Datapoints to alarm:** 10


**Evaluation periods:** 10


**Comparison Operator:** LESS\_THAN\_THRESHOLD



**Count**

**Dimensions:** ApiId, Stage


**Alarm description:** This alarm helps to detect low traffic volume for the HTTP API stage. This can indicate an issue with the application calling the API such as using incorrect endpoints. It could also be an indicator of an issue with the configuration or permissions of the API making it unreachable for clients.


**Intent:** This alarm can detect unexpectedly low traffic volume for the HTTP API stage. We recommend that you create this alarm if your API receives a predictable and consistent number of requests under normal conditions. If you have detailed CloudWatch metrics enabled and you can predict the normal traffic volume per route, we recommend that you create alternative alarms to this in order to have more fine-grained monitoring of traffic volume drops for each route. This alarm is not recommended for APIs that don't expect constant and consistent traffic.


**Statistic:** SampleCount


**Recommended threshold:** Depends on your situation


**Threshold justification:** Set the threshold value based on historical data analysis to determine what the expected baseline request count for your API is. Setting the threshold at a very high value might cause the alarm to be too sensitive at periods of normal and expected low traffic. Conversely, setting it at a very low value might cause the alarm to miss anomalous smaller drops in traffic volume.


**Period:** 60


**Datapoints to alarm:** 10


**Evaluation periods:** 10


**Comparison Operator:** LESS\_THAN\_THRESHOLD



**Count**

**Dimensions:** ApiId, Stage, Resource, Method


**Alarm description:** This alarm helps to detect low traffic volume for the HTTP API route in the stage. This can indicate an issue with the application calling the API such as using incorrect endpoints. It could also indicate an issue with the configuration or permissions of the API making it unreachable for clients.


**Intent:** This alarm can detect unexpectedly low traffic volume for the HTTP API route in the stage. We recommend that you create this alarm if your API receives a predictable and consistent number of requests under normal conditions. This alarm is not recommended for APIs that don't expect constant and consistent traffic.


**Statistic:** SampleCount


**Recommended threshold:** Depends on your situation


**Threshold justification:** Set the threshold value based on historical data analysis to determine what the expected baseline request count for your API is. Setting the threshold at a very high value might cause the alarm to be too sensitive at periods of normal and expected low traffic. Conversely, setting it at a very low value might cause the alarm to miss anomalous smaller drops in traffic volume.


**Period:** 60


**Datapoints to alarm:** 10


**Evaluation periods:** 10


**Comparison Operator:** LESS\_THAN\_THRESHOLD



**IntegrationLatency**

**Dimensions:** ApiId, Stage


**Alarm description:** This alarm helps to detect if 
 there is high integration latency for the API requests in a stage. You can correlate 
 the `IntegrationLatency` metric value with the corresponding latency metric of your backend such as 
 the `Duration` metric for Lambda integrations. This helps you determine whether the API backend is taking more time to process requests from clients due to performance issues, or if there is some other overhead from initialization or cold start. Additionally, consider enabling CloudWatch Logs for your API and checking the logs for any errors that may be causing the high latency issues. Moreover, consider enabling detailed CloudWatch metrics to get a view of this metric per route, to help you narrow down the source of the integration latency.


**Intent:** This alarm can detect when the API Gateway requests in a stage have a high integration latency. We recommend this alarm for WebSocket APIs, and we consider it optional for HTTP APIs because they already have separate alarm recommendations for the Latency metric. If you have detailed CloudWatch metrics enabled and you have different integration latency performance requirements per route, we recommend that you create alternative alarms in order to have more fine-grained monitoring of the integration latency for each route.


**Statistic:** p90


**Recommended threshold:** 2000.0


**Threshold justification:** The suggested threshold value does not work for all the API workloads. However, you can use it as a starting point for the threshold. You can then choose different threshold values based on the workload and acceptable latency, performance, and SLA requirements for the API. If is acceptable for the API to have a higher latency in general, set a higher threshold value to make the alarm less sensitive. However, if the API is expected to provide near real-time responses, set a lower threshold value. You can also analyze historical data to determine the expected baseline latency for the application workload, and then used to tune the threshold value accordingly.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_OR\_EQUAL\_TO\_THRESHOLD



**IntegrationLatency**

**Dimensions:** ApiId, Stage, Route


**Alarm description:** This alarm helps to detect if there is high integration 
 latency for the WebSocket API requests for a route in a stage. You can correlate the `IntegrationLatency` 
 metric value with the corresponding latency metric of your backend such as the `Duration` metric for 
 Lambda integrations. This helps you determine whether the API backend is taking more time to process requests from clients due to performance issues or if there is some other overhead from initialization or cold start. Additionally, consider enabling CloudWatch Logs for your API and checking the logs for any errors that may be causing the high latency issues.


**Intent:** This alarm can detect when the API Gateway requests for a route in a stage have high integration latency.


**Statistic:** p90


**Recommended threshold:** 2000.0


**Threshold justification:** The suggested threshold value does not work for all the API workloads. However, you can use it as a starting point for the threshold. You can then choose different threshold values based on the workload and acceptable latency, performance, and SLA requirements for the API. If it is acceptable for the API to have a higher latency in general, you can set a higher threshold value to make the alarm less sensitive. However, if the API is expected to provide near real-time responses, set a lower threshold value. You can also analyze historical data to determine the expected baseline latency for the application workload, and then used to tune the threshold value accordingly.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_OR\_EQUAL\_TO\_THRESHOLD



**Latency**

**Dimensions:** ApiName, Stage


**Alarm description:** This alarm detects high latency in a stage. Find 
 the `IntegrationLatency` metric value to check the API backend latency. If the two metrics are 
 mostly aligned, the API backend is the source of higher latency and you should investigate there for issues. Consider also enabling CloudWatch Logs and checking for errors that might be causing the high latency. Moreover, consider enabling detailed CloudWatch metrics to view this metric per resource and method and narrow down the source of the latency. If applicable, refer to the [troubleshooting with Lambda](https://repost.aws/knowledge-center/api-gateway-high-latency-with-lambda "https://repost.aws/knowledge-center/api-gateway-high-latency-with-lambda") or [troubleshooting for edge-optimized API endpoints](https://repost.aws/knowledge-center/source-latency-requests-api-gateway "https://repost.aws/knowledge-center/source-latency-requests-api-gateway") guides.


**Intent:** This alarm can detect when the API Gateway requests in a stage have high latency. If you have detailed CloudWatch metrics enabled and you have different latency performance requirements for each method and resource, we recommend that you create alternative alarms to have more fine-grained monitoring of the latency for each resource and method.


**Statistic:** p90


**Recommended threshold:** 2500.0


**Threshold justification:** The suggested threshold value does not work for all API workloads. However, you can use it as a starting point for the threshold. You can then choose different threshold values based on the workload and acceptable latency, performance, and SLA requirements for the API. If it is acceptable for the API to have a higher latency in general, you can set a higher threshold value to make the alarm less sensitive. However, if the API is expected to provide near real-time responses, set a lower threshold value. You can also analyze historical data to determine what the expected baseline latency is for the application workload and then tune the threshold value accordingly.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_OR\_EQUAL\_TO\_THRESHOLD



**Latency**

**Dimensions:** ApiName, Stage, Resource, Method


**Alarm description:** This alarm detects high latency for a resource and method 
 in a stage. Find the `IntegrationLatency` metric value to check the API backend latency. If the two
 metrics are mostly aligned, the API backend is the source of higher latency and you should investigate there for performance issues. Consider also enabling CloudWatch Logs and checking for any errors that might be causing the high latency. You can also refer to the [troubleshooting with Lambda](https://repost.aws/knowledge-center/api-gateway-high-latency-with-lambda "https://repost.aws/knowledge-center/api-gateway-high-latency-with-lambda") or [troubleshooting for edge-optimized API endpoints](https://repost.aws/knowledge-center/source-latency-requests-api-gateway "https://repost.aws/knowledge-center/source-latency-requests-api-gateway") guides if applicable.


**Intent:** This alarm can detect when the API Gateway requests for a resource and method in a stage have high latency.


**Statistic:** p90


**Recommended threshold:** 2500.0


**Threshold justification:** The suggested threshold value does not work for all the API workloads. However, you can use it as a starting point for the threshold. You can then choose different threshold values based on the workload and acceptable latency, performance, and SLA requirements for the API. If it is acceptable for the API to have a higher latency in general, you can set a higher threshold value to make the alarm less sensitive. However, if the API is expected to provide near real-time responses, set a lower threshold value. You can also analyze historical data to determine the expected baseline latency for the application workload and then tune the threshold value accordingly.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_OR\_EQUAL\_TO\_THRESHOLD



**Latency**

**Dimensions:** ApiId, Stage


**Alarm description:** This alarm detects high latency in a stage. Find 
 the `IntegrationLatency` metric value to check the API backend latency. If the two metrics are mostly aligned, the API backend is the source of higher latency and you should investigate there for performance issues. Consider also enabling CloudWatch Logs and checking for any errors that may be causing the high latency. Moreover, consider enabling detailed CloudWatch metrics to view this metric per route and narrow down the source of the latency. You can also refer to the [troubleshooting with Lambda integrations guide](https://repost.aws/knowledge-center/api-gateway-high-latency-with-lambda "https://repost.aws/knowledge-center/api-gateway-high-latency-with-lambda") if applicable.


**Intent:** This alarm can detect when the API Gateway requests in a stage have high latency. If you have detailed CloudWatch metrics enabled and you have different latency performance requirements per route, we recommend that you create alternative alarms to have more fine-grained monitoring of the latency for each route.


**Statistic:** p90


**Recommended threshold:** 2500.0


**Threshold justification:** The suggested threshold value does not work for all the API workloads. However, it can be used as a starting point for the threshold. You can then choose different threshold values based on the workload and acceptable latency, performance and SLA requirements for the API. If it is acceptable for the API to have a higher latency in general, you can set a higher threshold value to make it less sensitive.However, if the API is expected to provide near real-time responses, set a lower threshold value. You can also analyze historical data to determine the expected baseline latency for the application workload and then tune the threshold value accordingly.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_OR\_EQUAL\_TO\_THRESHOLD



**Latency**

**Dimensions:** ApiId, Stage, Resource, Method


**Alarm description:** This alarm detects high latency for a route in a stage. Find 
 the `IntegrationLatency` metric value to check the API backend latency. If the two metrics are mostly aligned, the API backend is the source of higher latency and should be investigated for performance issues. Consider also enabling CloudWatch logs and checking for any errors that might be causing the high latency. You can also refer to the [troubleshooting with Lambda integrations guide](https://repost.aws/knowledge-center/api-gateway-high-latency-with-lambda "https://repost.aws/knowledge-center/api-gateway-high-latency-with-lambda") if applicable.


**Intent:** This alarm is used to detect when the API Gateway requests for a route in a stage have high latency.


**Statistic:** p90


**Recommended threshold:** 2500.0


**Threshold justification:** The suggested threshold value does not work for all the API workloads. However, it can be used as a starting point for the threshold. You can then choose different threshold values based on the workload and acceptable latency, performance, and SLA requirements for the API. If it is acceptable for the API to have a higher latency in general, you can set a higher threshold value to make the alarm less sensitive. However, if the API is expected to provide near real-time responses, set a lower threshold value. You can also analyze historical data to determine the expected baseline latency for the application workload and then tune the threshold value accordingly.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_OR\_EQUAL\_TO\_THRESHOLD



**4xx**

**Dimensions:** ApiId, Stage


**Alarm description:** This alarm detects a high rate of client-side errors. This can indicate an issue in the authorization or client request parameters. It could also mean that a route was removed or a client is requesting one that doesn't exist in the API. Consider enabling CloudWatch Logs and checking for any errors that may be causing the 4xx errors. Moreover, consider enabling detailed CloudWatch metrics to view this metric per route, to help you narrow down the source of the errors. Errors can also be caused by exceeding the configured throttling limit. If the responses and logs are reporting high and unexpected rates of 429 errors, follow [this guide](https://repost.aws/knowledge-center/api-gateway-429-limit "https://repost.aws/knowledge-center/api-gateway-429-limit") to troubleshoot this issue.


**Intent:** This alarm can detect high rates of client-side errors for the API Gateway requests.


**Statistic:** Average


**Recommended threshold:** 0.05


**Threshold justification:** The suggested threshold detects when more than 5% of total requests are getting 4xx errors. However, you can tune the threshold to suit the traffic of the requests as well as acceptable error rates. You can also analyze historical data to determine the acceptable error rate for the application workload and then tune the threshold accordingly. Frequently occurring 4xx errors need to be alarmed on. However, setting a very low value for the threshold can cause the alarm to be too sensitive.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**5xx**

**Dimensions:** ApiId, Stage


**Alarm description:** This alarm helps to detect a high rate of server-side errors. This can indicate that there is something wrong on the API backend, the network, or the integration between the API gateway and the backend API. This [documentation](https://repost.aws/knowledge-center/api-gateway-5xx-error "https://repost.aws/knowledge-center/api-gateway-5xx-error") can help you troubleshoot the cause for 5xx errors.


**Intent:** This alarm can detect high rates of server-side errors for the API Gateway requests.


**Statistic:** Average


**Recommended threshold:** 0.05


**Threshold justification:** The suggested threshold detects when more than 5% of total requests are getting 5xx errors. However, you can tune the threshold to suit the traffic of the requests as well as acceptable error rates. You can also analyze historical data to determine what the acceptable error rate is for the application workload, and then you can tune the threshold accordingly. Frequently occurring 5xx errors need to be alarmed on. However, setting a very low value for the threshold can cause the alarm to be too sensitive.


**Period:** 60


**Datapoints to alarm:** 3


**Evaluation periods:** 3


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**MessageCount**

**Dimensions:** ApiId, Stage


**Alarm description:** This alarm helps to detect low traffic volume for the WebSocket API stage. This can indicate an issue when clients call the API such as using incorrect endpoints, or issues with the backend sending messages to clients. It could also indicate an issue with the configuration or permissions of the API, making it unreachable for clients.


**Intent:** This alarm can detect unexpectedly low traffic volume for the WebSocket API stage. We recommend that you create this alarm if your API receives and sends a predictable and consistent number of messages under normal conditions. If you have detailed CloudWatch metrics enabled and you can predict the normal traffic volume per route, it is better to create alternative alarms to this one, in order to have more fine-grained monitoring of traffic volume drops for each route. We do not recommend this alarm for APIs that don't expect constant and consistent traffic.


**Statistic:** SampleCount


**Recommended threshold:** Depends on your situation


**Threshold justification:** Set the threshold value based on historical data analysis to determine what the expected baseline message count for your API is. Setting the threshold to a very high value might cause the alarm to be too sensitive at periods of normal and expected low traffic. Conversely, setting it to a very low value might cause the alarm to miss anomalous smaller drops in traffic volume.


**Period:** 60


**Datapoints to alarm:** 10


**Evaluation periods:** 10


**Comparison Operator:** LESS\_THAN\_THRESHOLD



**MessageCount**

**Dimensions:** ApiId, Stage, Route


**Alarm description:** This alarm helps detect low traffic volume for the WebSocket API route in the stage. This can indicate an issue with the clients calling the API such as using incorrect endpoints, or issues with the backend sending messages to clients. It could also indicate an issue with the configuration or permissions of the API, making it unreachable for clients.


**Intent:** This alarm can detect unexpectedly low traffic volume for the WebSocket API route in the stage. We recommend that you create this alarm if your API receives and sends a predictable and consistent number of messages under normal conditions. We do not recommend this alarm for APIs that don't expect constant and consistent traffic.


**Statistic:** SampleCount


**Recommended threshold:** Depends on your situation


**Threshold justification:** Set the threshold based on historical data analysis to determine what the expected baseline message count for your API is. Setting the threshold to a very high value might cause the alarm to be too sensitive at periods of normal and expected low traffic. Conversely, setting it to a very low value might cause the alarm to miss anomalous smaller drops in traffic volume.


**Period:** 60


**Datapoints to alarm:** 10


**Evaluation periods:** 10


**Comparison Operator:** LESS\_THAN\_THRESHOLD



**ClientError**

**Dimensions:** ApiId, Stage


**Alarm description:** This alarm detects a high rate of client errors. This can indicate an issue in the authorization or message parameters. It could also mean that a route was removed or a client is requesting one that doesn't exist in the API. Consider enabling CloudWatch Logs and checking for any errors that may be causing the 4xx errors. Moreover, consider enabling detailed CloudWatch metrics to view this metric per route, to help you narrow down the source of the errors. Errors could also be caused by exceeding the configured throttling limit. If the responses and logs are reporting high and unexpected rates of 429 errors, follow [this guide](https://repost.aws/knowledge-center/api-gateway-429-limit "https://repost.aws/knowledge-center/api-gateway-429-limit") to troubleshoot this issue.


**Intent:** This alarm can detect high rates of client errors for the WebSocket API Gateway messages.


**Statistic:** Average


**Recommended threshold:** 0.05


**Threshold justification:** The suggested threshold detects when more than 5% of total requests are getting 4xx errors. You can tune the threshold to suit the traffic of the requests as well as to suit your acceptable error rates. You can also analyze historical data to determine the acceptable error rate for the application workload, and then tune the threshold accordingly. Frequently occurring 4xx errors need to be alarmed on. However, setting a very low value for the threshold can cause the alarm to be too sensitive.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**ExecutionError**

**Dimensions:** ApiId, Stage


**Alarm description:** This alarm helps to detect a high rate of execution errors. This can be caused by 5xx errors from your integration, permission issues, or other factors preventing successful invocation of the integration, such as the integration being throttled or deleted. Consider enabling CloudWatch Logs for your API and checking the logs for the type and cause of the errors. Moreover, consider enabling detailed CloudWatch metrics to get a view of this metric per route, to help you narrow down the source of the errors. This [documentation](https://repost.aws/knowledge-center/api-gateway-websocket-error "https://repost.aws/knowledge-center/api-gateway-websocket-error") can also help you troubleshoot the cause of any connection errors.


**Intent:** This alarm can detect high rates of execution errors for the WebSocket API Gateway messages.


**Statistic:** Average


**Recommended threshold:** 0.05


**Threshold justification:** The suggested threshold detects when more than 5% of total requests are getting execution errors. You can tune the threshold to suit the traffic of the requests, as well as to suit your acceptable error rates. You can analyze historical data to determine the acceptable error rate for the application workload, and then tune the threshold accordingly. Frequently occurring execution errors need to be alarmed on. However, setting a very low value for the threshold can cause the alarm to be too sensitive.


**Period:** 60


**Datapoints to alarm:** 3


**Evaluation periods:** 3


**Comparison Operator:** GREATER\_THAN\_THRESHOLD




## Amazon EC2 Auto Scaling




**GroupInServiceCapacity**

**Dimensions:** AutoScalingGroupName


**Alarm description:** This alarm helps to detect when the capacity in the group is below the desired capacity required for your workload. To troubleshoot, check your scaling activities for launch failures and confirm that your desired capacity configuration is correct.


**Intent:** This alarm can detect a low availability in your auto scaling group because of launch failures or suspended launches.


**Statistic:** Average


**Recommended threshold:** Depends on your situation


**Threshold justification:** The threshold value should be the minimum capacity required to run your workload. In most cases, you can set this to match the GroupDesiredCapacity metric.


**Period:** 60


**Datapoints to alarm:** 10


**Evaluation periods:** 10


**Comparison Operator:** LESS\_THAN\_THRESHOLD




## AWS Certificate Manager (ACM)




**DaysToExpiry**

**Dimensions:** CertificateArn


**Alarm description:** This alarm helps you detect when a certificate managed by or imported into ACM is approaching its expiration date. 
 It helps to prevent unexpected certificate expirations that could lead to service disruptions. When the alarm transitions into ALARM state, you should take immediate action 
 to renew or re-import the certificate. For ACM-managed certificates, see the instructions at [certificate renewal process](https://docs.aws.amazon.com/acm/latest/userguide/troubleshooting-renewal.html "https://docs.aws.amazon.com/acm/latest/userguide/troubleshooting-renewal.html"). For 
 imported certificates, see the instructions at [re-import process](https://docs.aws.amazon.com/acm/latest/userguide/import-reimport.html "https://docs.aws.amazon.com/acm/latest/userguide/import-reimport.html").


**Intent:** This alarm can proactively alert you about upcoming certificate expirations. It provides sufficient 
 advance notice to allow for manual intervention, enabling you to renew or replace certificates before they expire. This helps you maintain 
 the security and availability of TLS-enabled services. When this goes into ALARM, immediately investigate the certificate status and initiate the renewal process if necessary.


**Statistic:** Minimum


**Recommended threshold:** 44.0


**Threshold justification:** The 44-day threshold provides a balance between early warning and avoiding false alarms. It 
 allows sufficient time for manual intervention if automatic renewal fails. Adjust this value based on your certificate renewal process and operational response times.


**Period:** 86400


**Datapoints to alarm:** 1


**Evaluation periods:** 1


**Comparison Operator:** LESS\_THAN\_OR\_EQUAL\_TO\_THRESHOLD




## Amazon CloudFront




**5xxErrorRate**

**Dimensions:** DistributionId, Region=Global


**Alarm description:** This alarm monitors the percentage of 5xx error responses from your origin server, to help you detect if the CloudFront service is having issues. See 
 [Troubleshooting error responses from your origin](../../../AmazonCloudFront/latest/DeveloperGuide/troubleshooting-response-errors.md "../../../AmazonCloudFront/latest/DeveloperGuide/troubleshooting-response-errors.md") for information to help you understand the problems with your server. Also, [turn on additional metrics](../../../AmazonCloudFront/latest/DeveloperGuide/viewing-cloudfront-metrics.md#monitoring-console.distributions-additional "../../../AmazonCloudFront/latest/DeveloperGuide/viewing-cloudfront-metrics.md#monitoring-console.distributions-additional") to get detailed error metrics.


**Intent:** This alarm is used to detect problems with serving requests from the origin server, or problems with communication between CloudFront and your origin server.


**Statistic:** Average


**Recommended threshold:** Depends on your situation


**Threshold justification:** The recommended threshold value for this alarm is highly dependent on the tolerance for 5xx responses. You can analyze historical data and trends, and then set the threshold accordingly. Because 5xx errors can be caused by transient issues, we recommend that you set the threshold to a value greater than 0 so that the alarm is not too sensitive.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**OriginLatency**

**Dimensions:** DistributionId, Region=Global


**Alarm description:** The alarm helps to monitor if the origin server 
 is taking too long to respond. If the server takes too long to respond, it might lead to a timeout. 
 Refer to [find and fix delayed responses from applications on your origin server](../../../AmazonCloudFront/latest/DeveloperGuide/http-504-gateway-timeout.md#http-504-gateway-timeout-slow-application "../../../AmazonCloudFront/latest/DeveloperGuide/http-504-gateway-timeout.md#http-504-gateway-timeout-slow-application") if you experience consistently high `OriginLatency` values.


**Intent:** This alarm is used to detect problems with the origin server taking too long to respond.


**Statistic:** p90


**Recommended threshold:** Depends on your situation


**Threshold justification:** You should calculate the value of about 80% of the origin response timeout, and use the result as the threshold value. If this metric is consistently close to the origin response timeout value, you might start experiencing 504 errors.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**FunctionValidationErrors**

**Dimensions:** DistributionId, FunctionName, Region=Global


**Alarm description:** This alarm helps you monitor validation errors from CloudFront functions so that you can take steps to resolve them. Analyze the CloudWatch function logs and look at the function code to find and resolve the root cause of the problem. See [Restrictions on edge functions](../../../AmazonCloudFront/latest/DeveloperGuide/edge-functions-restrictions.md "../../../AmazonCloudFront/latest/DeveloperGuide/edge-functions-restrictions.md") to understand the common misconfigurations for CloudFront Functions.


**Intent:** This alarm is used to detect validation errors from CloudFront functions.


**Statistic:** Sum


**Recommended threshold:** 0.0


**Threshold justification:** A value greater than 0 indicates a validation error. We recommend setting the threshold to 0 because validation errors imply a problem when CloudFront functions hand off back to CloudFront. For example, CloudFront needs the HTTP Host header in order to process a request. There is nothing stopping a user from deleting the Host header in their CloudFront functions code. But when CloudFront gets the response back and the Host header is missing, CloudFront throws a validation error.


**Period:** 60


**Datapoints to alarm:** 2


**Evaluation periods:** 2


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**FunctionExecutionErrors**

**Dimensions:** DistributionId, FunctionName, Region=Global


**Alarm description:** This alarm helps you monitor execution errors from CloudFront functions so that you can take steps to resolve them. Analyze the CloudWatch function logs and look at the function code to find and resolve the root cause of the problem.


**Intent:** This alarm is used to detect execution errors from CloudFront functions.


**Statistic:** Sum


**Recommended threshold:** 0.0


**Threshold justification:** We recommend to set the threshold to 0 because an execution error indicates a problem with the code that occurs at runtime.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**FunctionThrottles**

**Dimensions:** DistributionId, FunctionName, Region=Global


**Alarm description:** This alarm helps you to monitor if your CloudFront function is throttled. If your function is throttled, it means that it is taking too long to execute. To avoid function throttles, consider optimizing the function code.


**Intent:** This alarm can detect when your CloudFront function is throttled so that you can react and resolve the issue for a smooth customer experience.


**Statistic:** Sum


**Recommended threshold:** 0.0


**Threshold justification:** We recommend setting the threshold to 0, to allow quicker resolution of the function throttles.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD




## Amazon Cognito




**SignUpThrottles**

**Dimensions:** UserPool, UserPoolClient


**Alarm description:** This alarm monitors the count of throttled requests. If users are consistently getting throttled, you should increase the limit by requesting a service quota increase. Refer to [Quotas in Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/limits.html "https://docs.aws.amazon.com/cognito/latest/developerguide/limits.html") to learn how to request a quota increase. To take actions proactively, consider tracking the [usage quota](https://docs.aws.amazon.com/cognito/latest/developerguide/limits.html#track-quota-usage "https://docs.aws.amazon.com/cognito/latest/developerguide/limits.html#track-quota-usage").


**Intent:** This alarm helps to monitor the occurrence of throttled sign-up requests. This can help you know when to take actions to mitigate any degradation in sign-up experience. Sustained throttling of requests is a negative user sign-up experience.


**Statistic:** Sum


**Recommended threshold:** Depends on your situation


**Threshold justification:** A well-provisioned user pool should not encounter any throttling which spans across multiple data points. So, a typical threshold for an expected workload should be zero. For an irregular workload with frequent bursts, you can analyze historical data to determine the acceptable throttling for the application workload, and then you can tune the threshold accordingly. A throttled request should be retried to minimize the impact on the application.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**SignInThrottles**

**Dimensions:** UserPool, UserPoolClient


**Alarm description:** This alarm monitors the count of throttled user authentication requests. If users are consistently getting throttled, you might need to increase the limit by requesting a service quota increase. Refer to [Quotas in Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/limits.html "https://docs.aws.amazon.com/cognito/latest/developerguide/limits.html") to learn how to request a quota increase. To take actions proactively, consider tracking the [usage quota](https://docs.aws.amazon.com/cognito/latest/developerguide/limits.html#track-quota-usage "https://docs.aws.amazon.com/cognito/latest/developerguide/limits.html#track-quota-usage").


**Intent:** This alarm helps to monitor the occurrence of throttled sign-in requests. This can help you know when to take actions to mitigate any degradation in sign-in experience. Sustained throttling of requests is a bad user authentication experience.


**Statistic:** Sum


**Recommended threshold:** Depends on your situation


**Threshold justification:** A well-provisioned user pool should not encounter any throttling which spans across multiple data points. So, a typical threshold for an expected workload should be zero. For an irregular workload with frequent bursts, you can analyze historical data to determine the acceptable throttling for the application workload, and then you can tune the threshold accordingly. A throttled request should be retried to minimize the impact on the application.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**TokenRefreshThrottles**

**Dimensions:** UserPool, UserPoolClient


**Alarm description:** You can set the threshold value can to suit the traffic of the request as well as to match acceptable throttling for token refresh requests. Throttling is used to protect your system from too many requests. However, it is important to monitor if you are under provisioned for your normal traffic as well. You can analyze historical data to find the acceptable throttling for the application workload, and then you can tune your alarm threshold to be higher than your acceptable throttling level. Throttled requests should be retried by the application/service as they are transient. Therefore, a very low value for the threshold can cause alarm to be sensitive.


**Intent:** This alarm helps to monitor the occurrence of throttled token refresh requests. This can help you know when to take actions to mitigate any potential problems, to ensure a smooth user experience and the health and reliability of your authentication system. Sustained throttling of requests is a bad user authentication experience.


**Statistic:** Sum


**Recommended threshold:** Depends on your situation


**Threshold justification:** Threshold value can also be set/tuned to suit the traffic of the request as well as acceptable throttling for token refresh requests. Throttling are there for protecting your system from too many requests, however it is important to monitor if you are under provisioned for your normal traffic as well and see if it is causing the impact. Historical data can also be analyzed to see what is the acceptable throttling for the application workload and threshold can be tuned higher than your usual acceptable throttling level. Throttled requests should be retried by the application/service as they are transient. Therefore, a very low value for the threshold can cause alarm to be sensitive.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**FederationThrottles**

**Dimensions:** UserPool, UserPoolClient, IdentityProvider


**Alarm description:** This alarm monitors the count of throttled identity federation requests. If you consistently see throttling, it might indicate that you need to increase the limit by requesting a service quota increase. Refer to [Quotas in Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/limits.html "https://docs.aws.amazon.com/cognito/latest/developerguide/limits.html") to learn how to request a quota increase.


**Intent:** This alarm helps to monitor the occurrence of throttled identity federation requests. This can help you take proactive responses to performance bottlenecks or misconfigurations, and ensure a smooth authentication experience for your users. Sustained throttling of requests is a bad user authentication experience.


**Statistic:** Sum


**Recommended threshold:** Depends on your situation


**Threshold justification:** You can set the threshold to suit the traffic of the request as well as to match the acceptable throttling for identity federation requests. Throttling is used for protecting your system from too many requests. However, it is important to monitor if you are under provisioned for your normal traffic as well. You can analyze historical data to find the acceptable throttling for the application workload, and then set the threshold to a value above your acceptable throttling level. Throttled requests should be retried by the application/service as they are transient. Therefore, a very low value for the threshold can cause alarm to be sensitive.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD




## Amazon DynamoDB




**AccountProvisionedReadCapacityUtilization**

**Dimensions:** None


**Alarm description:** This alarm detects if the account’s read capacity is reaching its provisioned limit. You can raise the account quota for read capacity utilization if this occurs. You can view your current quotas for read capacity units and request increases using [Service Quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html "https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html").


**Intent:** The alarm can detect if the account’s read capacity utilization is approaching its provisioned read capacity utilization. If the utilization reaches its maximum limit, DynamoDB starts to throttle read requests.


**Statistic:** Maximum


**Recommended threshold:** 80.0


**Threshold justification:** Set the threshold to 80%, so that action (such as raising the account limits) can be taken before it reaches full capacity to avoid throttling.


**Period:** 300


**Datapoints to alarm:** 2


**Evaluation periods:** 2


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**AccountProvisionedWriteCapacityUtilization**

**Dimensions:** None


**Alarm description:** This alarm detects if the account’s write capacity is reaching its provisioned limit. You can raise the account quota for write capacity utilization if this occurs. You can view your current quotas for write capacity units and request increases using [Service Quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html "https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html").


**Intent:** This alarm can detect if the account’s write capacity utilization is approaching its provisioned write capacity utilization. If the utilization reaches its maximum limit, DynamoDB starts to throttle write requests.


**Statistic:** Maximum


**Recommended threshold:** 80.0


**Threshold justification:** Set the threshold to 80%, so that the action (such as raising the account limits) can be taken before it reaches full capacity to avoid throttling.


**Period:** 300


**Datapoints to alarm:** 2


**Evaluation periods:** 2


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**AgeOfOldestUnreplicatedRecord**

**Dimensions:** TableName, DelegatedOperation


**Alarm description:** This alarm detects the delay in replication to a 
 Kinesis data stream. Under normal operation, `AgeOfOldestUnreplicatedRecord` should be only milliseconds. This number grows based on unsuccessful replication attempts caused by customer-controlled configuration choices. Customer-controlled configuration examples that lead to unsuccessful replication attempts are an under-provisioned Kinesis data stream capacity that leads to excessive throttling. or a manual update to the Kinesis data stream’s access policies that prevents DynamoDB from adding data to the data stream. To keep this metric as low as possible, you need to ensure the right provisioning of Kinesis data stream capacity and make sure that DynamoDB’s permissions are unchanged.


**Intent:** This alarm can monitor unsuccessful replication attempts and the resulting delay in replication to the Kinesis data stream.


**Statistic:** Maximum


**Recommended threshold:** Depends on your situation


**Threshold justification:** Set the threshold according to the desired replication delay measured in milliseconds. This value depends on your workload's requirements and expected performance.


**Period:** 300


**Datapoints to alarm:** 3


**Evaluation periods:** 3


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**FailedToReplicateRecordCount**

**Dimensions:** TableName, DelegatedOperation


**Alarm description:** This alarm detects the number of records that DynamoDB failed to replicate to your Kinesis data stream. Certain items larger than 34 KB might expand in size to change data records that are larger than the 1 MB item size limit of Kinesis Data Streams. This size expansion occurs when these larger than 34 KB items include a large number of Boolean or empty attribute values. Boolean and empty attribute values are stored as 1 byte in DynamoDB, but expand up to 5 bytes when they’re serialized using standard JSON for Kinesis Data Streams replication. DynamoDB can’t replicate such change records to your Kinesis data stream. DynamoDB skips these change data records, and automatically continues replicating subsequent records.


**Intent:** This alarm can monitor the number of records that DynamoDB failed to replicate to your Kinesis data stream because of the item size limit of Kinesis Data Streams.


**Statistic:** Sum


**Recommended threshold:** 0.0


**Threshold justification:** Set the threshold to 0 to detect any records that DynamoDB failed to replicate.


**Period:** 60


**Datapoints to alarm:** 1


**Evaluation periods:** 1


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**ReadThrottleEvents**

**Dimensions:** TableName


**Alarm description:** This alarm detects if there are high number of read requests getting throttled for the DynamoDB table. To troubleshoot the issue, see [Troubleshooting throttling issues in Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TroubleshootingThrottling.html "https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TroubleshootingThrottling.html").


**Intent:** This alarm can detect sustained throttling for read requests to the DynamoDB table. Sustained throttling of read requests can negatively impact your workload read operations and reduce the overall efficiency of the system.


**Statistic:** Sum


**Recommended threshold:** Depends on your situation


**Threshold justification:** Set the threshold according to the expected read traffic for the DynamoDB table, accounting for an acceptable level of throttling. It is important to monitor whether you are under provisioned and not causing consistent throttling. You can also analyze historical data to find the acceptable throttling level for the application workload, and then tune the threshold to be higher than your usual throttling level. Throttled requests should be retried by the application or service as they are transient. Therefore, a very low threshold may cause the alarm to be too sensitive, causing unwanted state transitions.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**ReadThrottleEvents**

**Dimensions:** TableName, GlobalSecondaryIndexName


**Alarm description:** This alarm detects if there are a high number of read requests getting throttled for the Global Secondary Index of the DynamoDB table. To troubleshoot the issue, see [Troubleshooting throttling issues in Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TroubleshootingThrottling.html "https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TroubleshootingThrottling.html").


**Intent:** The alarm can detect sustained throttling for read requests for the Global Secondary Index of the DynamoDB Table. Sustained throttling of read requests can negatively impact your workload read operations and reduce the overall efficiency of the system.


**Statistic:** Sum


**Recommended threshold:** Depends on your situation


**Threshold justification:** Set the threshold according to the expected read traffic for the DynamoDB table, accounting for an acceptable level of throttling. It is important to monitor if you are under provisioned and not causing consistent throttling. You can also analyze historical data to find an acceptable throttling level for the application workload, and then tune the threshold to be higher than your usual acceptable throttling level. Throttled requests should be retried by the application or service as they are transient. Therefore, a very low threshold may cause the alarm to be too sensitive, causing unwanted state transitions.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**ReplicationLatency**

**Dimensions:** TableName, ReceivingRegion


**Alarm description:** The alarm detects if the replica in a Region for the global table is lagging behind the source Region. The latency can increase if an AWS Region becomes degraded and you have a replica table in that Region. In this case, you can temporarily redirect your application's read and write activity to a different AWS Region. If you are using 2017.11.29 (Legacy) of global tables, you should verify that write capacity units (WCUs) are identical for each of the replica tables. You can also make sure to follow recommendations in [Best practices and requirements for managing capacity](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables_reqs_bestpractices.html#globaltables_reqs_bestpractices.tables "https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables_reqs_bestpractices.html#globaltables_reqs_bestpractices.tables").


**Intent:** The alarm can detect if the replica table in a Region is falling behind replicating the changes from another Region. This could cause your replica to diverge from the other replicas. It’s useful to know the replication latency of each AWS Region and alert if that replication latency increases continually. The replication of the table applies to global tables only.


**Statistic:** Average


**Recommended threshold:** Depends on your situation


**Threshold justification:** The recommended threshold value for this alarm is highly dependent on your use case. Replication latencies longer than 3 minutes are generally a cause for investigation. Review the criticality and requirements of replication delay and analyze historical trends, and then select the threshold accordingly.


**Period:** 60


**Datapoints to alarm:** 15


**Evaluation periods:** 15


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**SuccessfulRequestLatency**

**Dimensions:** TableName, Operation


**Alarm description:** This alarm detects a high latency for the DynamoDB 
 table operation ( indicated by the dimension value of the `Operation` in the alarm). See [this troubleshooting document](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TroubleshootingLatency.html "https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TroubleshootingLatency.html") for troubleshooting latency issues in Amazon DynamoDB.


**Intent:** This alarm can detect a high latency for the DynamoDB table operation. Higher latency for the operations can negatively impact the overall efficiency of the system.


**Statistic:** Average


**Recommended threshold:** Depends on your situation


**Threshold justification:** DynamoDB provides single-digit millisecond latency on average for singleton operations such as GetItem, PutItem, and so on. However, you can set the threshold based on acceptable tolerance for the latency for the type of operation and table involved in the workload. You can analyze historical data of this metric to find the usual latency for the table operation, and then set the threshold to a number which represents critical delay for the operation.


**Period:** 60


**Datapoints to alarm:** 10


**Evaluation periods:** 10


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**SystemErrors**

**Dimensions:** TableName


**Alarm description:** This alarm detects a sustained high number of system errors for the DynamoDB table requests. If you continue to get 5xx errors, open the [AWS Service Health Dashboard](https://status.aws.amazon.com/ "https://status.aws.amazon.com/") to check for operational issues with the service. You can use this alarm to get notified in case there is a prolonged internal service issue from DynamoDB and it helps you correlate with the issue your client application is facing. Refer [Error handling for DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.Errors.html#Programming.Errors.MessagesAndCodes.http5xx "https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.Errors.html#Programming.Errors.MessagesAndCodes.http5xx") for more information.


**Intent:** This alarm can detect sustained system errors for the DynamoDB table requests. System errors indicate internal service errors from DynamoDB and helps correlate to the issue that the client is having.


**Statistic:** Sum


**Recommended threshold:** Depends on your situation


**Threshold justification:** Set the threshold according to the expected traffic, accounting for an acceptable level of system errors. You can also analyze historical data to find the acceptable error count for the application workload, and then tune the threshold accordingly. System errors should be retried by the application/service as they are transient. Therefore, a very low threshold might cause the alarm to be too sensitive, causing unwanted state transitions.


**Period:** 60


**Datapoints to alarm:** 15


**Evaluation periods:** 15


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**ThrottledPutRecordCount**

**Dimensions:** TableName, DelegatedOperation


**Alarm description:** This alarm detects the records getting throttled by your Kinesis data stream during the replication of change data capture to Kinesis. This throttling happens because of insufficient Kinesis data stream capacity. If you experience excessive and regular throttling, you might need to increase the number of Kinesis stream shards proportionally to the observed write throughput of your table. To learn more about determining the size of a Kinesis data stream, see [Determining the Initial Size of a Kinesis Data Stream](https://docs.aws.amazon.com/streams/latest/dev/amazon-kinesis-streams.html#how-do-i-size-a-stream "https://docs.aws.amazon.com/streams/latest/dev/amazon-kinesis-streams.html#how-do-i-size-a-stream").


**Intent:** This alarm can monitor the number of records that that were throttled by your Kinesis data stream because of insufficient Kinesis data stream capacity.


**Statistic:** Maximum


**Recommended threshold:** Depends on your situation


**Threshold justification:** You might experience some throttling during exceptional usage peaks, but throttled records should remain as low as possible to avoid higher replication latency (DynamoDB retries sending throttled records to the Kinesis data stream). Set the threshold to a number which can help you catch regular excessive throttling. You can also analyze historical data of this metric to find the acceptable throttling rates for the application workload. Tune the threshold to a value that the application can tolerate based on your use case.


**Period:** 60


**Datapoints to alarm:** 10


**Evaluation periods:** 10


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**UserErrors**

**Dimensions:** None


**Alarm description:** This alarm detects a sustained high number of user errors for the DynamoDB table requests. You can check client application logs during the issue time frame to see why the requests are invalid. You can check [HTTP status code 400](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.Errors.html#Programming.Errors.MessagesAndCodes.http400 "https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.Errors.html#Programming.Errors.MessagesAndCodes.http400") to see the type of error you are getting and take action accordingly. You might have to fix the application logic to create valid requests.


**Intent:** This alarm can detect sustained user errors for the DynamoDB table requests. User errors for requested operations mean that the client is producing invalid requests and it is failing.


**Statistic:** Sum


**Recommended threshold:** Depends on your situation


**Threshold justification:** Set the threshold to zero to detect any client side errors. Or you can set it to a higher value if you want to avoid the alarm triggering for a very lower number of errors. Decide based on your use case and traffic for the requests.


**Period:** 60


**Datapoints to alarm:** 10


**Evaluation periods:** 10


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**WriteThrottleEvents**

**Dimensions:** TableName


**Alarm description:** This alarm detects if there are a high number of write requests getting throttled for the DynamoDB table. See [Troubleshooting throttling issues in Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TroubleshootingThrottling.html "https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TroubleshootingThrottling.html") to troubleshoot the issue.


**Intent:** This alarm can detect sustained throttling for write requests to the DynamoDB table. Sustained throttling of write requests can negatively impact your workload write operations and reduce the overall efficiency of the system.


**Statistic:** Sum


**Recommended threshold:** Depends on your situation


**Threshold justification:** Set the threshold according to the expected write traffic for the DynamoDB table, accounting for an acceptable level of throttling. It is important to monitor if you are under provisioned and not causing consistent throttling. You can also analyze historical data to find the acceptable level of throttling for the application workload, and then tune the threshold to a value higher than your usual acceptable throttling level. Throttled requests should be retried by the application/service as they are transient. Therefore, a very low threshold might cause the alarm to be too sensitive, causing unwanted state transitions.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**WriteThrottleEvents**

**Dimensions:** TableName, GlobalSecondaryIndexName


**Alarm description:** This alarm detects if there are a high number of write requests getting throttled for Global Secondary Index of the DynamoDB table. See [Troubleshooting throttling issues in Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TroubleshootingThrottling.html "https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TroubleshootingThrottling.html") to troubleshoot the issue.


**Intent:** This alarm can detect sustained throttling for write requests for the Global Secondary Index of DynamoDB Table. Sustained throttling of write requests can negatively impact your workload write operations and reduce the overall efficiency of the system.


**Statistic:** Sum


**Recommended threshold:** Depends on your situation


**Threshold justification:** Set the threshold according to the expected Write traffic for the DynamoDB table, accounting for an acceptable level of throttling. It is important to monitor if you are under provisioned and not causing consistent throttling. You can also analyze historical data to find the acceptable throttling level for the application workload, and then tune the threshold to a value higher than your usual acceptable throttling level. Throttled requests should be retried by the application/service as they are transient. Therefore, a very low value might cause the alarm to be too sensitive, causing unwanted state transitions.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD




## Amazon EBS




**VolumeStalledIOCheck**

**Dimensions:** VolumeId, InstanceId


**Alarm description:** This alarm helps you monitor the IO performance of your Amazon EBS volumes. This check detects underlying issues with the 
 Amazon EBS infrastructure, such as hardware or software issues on the storage subsystems underlying the Amazon EBS volumes, hardware issues on the physical host that impact the reachability
 of the Amazon EBS volumes from your Amazon EC2 instance, and can detect connectivity issues between the instance and the Amazon EBS volumes. If the Stalled IO Check fails, you can either wait 
 for AWS to resolve the issue, or you can take action such as replacing the affected volume or stopping and restarting the instance to which the volume is attached. In 
 most cases, when this metric fails, Amazon EBS will automatically diagnose and recover your volume within a few minutes.


**Intent:** This alarm can detect the status of your Amazon EBS volumes to determine when these volumes are impaired and can not complete I/O operations.


**Statistic:** Maximum


**Recommended threshold:** 1.0


**Threshold justification:** When a status check fails, the value of this metric is 1. The threshold is set so that whenever the status check fails, 
 the alarm is in ALARM state.


**Period:** 60


**Datapoints to alarm:** 10


**Evaluation periods:** 10


**Comparison Operator:** GREATER\_THAN\_OR\_EQUAL\_TO\_THRESHOLD




## Amazon EC2




**CPUUtilization**

**Dimensions:** InstanceId


**Alarm description:** This alarm helps to monitor the CPU utilization of an EC2 instance. Depending on the application, consistently high utilization levels might be normal. But if performance is degraded, and the application is not constrained by disk I/O, memory, or network resources, then a maxed-out CPU might indicate a resource bottleneck or application performance problems. High CPU utilization might indicate that an upgrade to a more CPU intensive instance is required. If detailed monitoring is enabled, you can change the period to 60 seconds instead of 300 seconds. For more information, see [Enable or turn off detailed monitoring for your instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-cloudwatch-new.html "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-cloudwatch-new.html").


**Intent:** This alarm is used to detect high CPU utilization.


**Statistic:** Average


**Recommended threshold:** 80.0


**Threshold justification:** Typically, you can set the threshold for CPU utilization to 70-80%. However, you can adjust this value based on your acceptable performance level and workload characteristics. For some systems, consistently high CPU utilization may be normal and not indicate a problem, while for others, it may be cause of concern. Analyze historical CPU utilization data to identify the usage, find what CPU utilization is acceptable for your system, and set the threshold accordingly.


**Period:** 300


**Datapoints to alarm:** 3


**Evaluation periods:** 3


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**StatusCheckFailed**

**Dimensions:** InstanceId


**Alarm description:** This alarm helps to monitor both system status checks and instance status checks. If either type of status check fails, then this alarm should be in ALARM state.


**Intent:** This alarm is used to detect the underlying problems with instances, including both system status check failures and instance status check failures.


**Statistic:** Maximum


**Recommended threshold:** 1.0


**Threshold justification:** When a status check fails, the value of this metric is 1. The threshold is set so that whenever the status check fails, the alarm is in ALARM state.


**Period:** 300


**Datapoints to alarm:** 2


**Evaluation periods:** 2


**Comparison Operator:** GREATER\_THAN\_OR\_EQUAL\_TO\_THRESHOLD



**StatusCheckFailed\_AttachedEBS**

**Dimensions:** InstanceId


**Alarm description:** This alarm helps you monitor whether the Amazon EBS volumes attached to an instance are reachable and able to complete I/O operations. This status check detects underlying issues with the compute or Amazon EBS
 infrastructure such as the following:



* Hardware or software issues on the storage subsystems underlying the Amazon EBS volumes
* Hardware issues on the physical host that impact reachability of the Amazon EBS volumes
* Connectivity issues between the instance and Amazon EBS volumes

When the attached EBS status check fails, you can either wait for Amazon to resolve the issue, or you can take an action such as replacing the affected volumes or stopping and restarting the instance.


**Intent:** This alarm is used to detect unreachable Amazon EBS volumes attached to an instance. These can cause failures in I/O operations.


**Statistic:** Maximum


**Recommended threshold:** 1.0


**Threshold justification:** When a status check fails, the value of this metric is 1. The threshold is set so that whenever the status check fails, the alarm is in ALARM state.


**Period:** 60


**Datapoints to alarm:** 10


**Evaluation periods:** 10


**Comparison Operator:** GREATER\_THAN\_OR\_EQUAL\_TO\_THRESHOLD




## Amazon ElastiCache




**CPUUtilization**

**Dimensions:** CacheClusterId, CacheNodeId


**Alarm description:** This alarm helps to monitor the CPU utilization for the entire ElastiCache instance, including the database engine processes and other processes running on the instance. AWS Elasticache supports two engine types: Memcached and Redis OSS. When you reach high CPU utilization on a Memcached node, you should consider scaling up your instance type or adding new cache nodes. For Redis OSS, if your main workload is from read requests, you should consider adding more read replicas to your cache cluster. If your main workload is from write requests, you should consider adding more shards to distribute the workload across more primary nodes if you’re running in clustered mode, or scaling up your instance type if you’re running Redis OSS in non-clustered mode.


**Intent:** This alarm is used to detect high CPU utilization of ElastiCache hosts. It is useful to get a broad view of the CPU usage across the entire instance, including non-engine processes.


**Statistic:** Average


**Recommended threshold:** Depends on your situation


**Threshold justification:** Set the threshold to the percentage that reflects a critical CPU utilization level for your application. For Memcached, the engine can use up to num\_threads cores. For Redis OSS, the engine is largely single-threaded, but might use additional cores if available to accelerate I/O. In most cases, you can set the threshold to about 90% of your available CPU. Because Redis OSS is single-threaded, the actual threshold value should be calculated as a fraction of the node's total capacity.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**CurrConnections**

**Dimensions:** CacheClusterId, CacheNodeId


**Alarm description:** This alarm detects high connection count, which 
 might indicate heavy load or performance issues. A constant increase of `CurrConnections` might lead to exhaustion of the 65,000 available connections. It may indicate that connections improperly closed on the application side and were left established on the server side. You should consider using connection pooling or idle connection timeouts to limit the number of connections made to the cluster, or for Redis OSS, consider tuning [tcp-keepalive](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/ParameterGroups.Redis.html "https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/ParameterGroups.Redis.html") on your cluster to detect and terminate potential dead peers.


**Intent:** The alarm helps you identify high connection counts that could impact the performance and stability of your ElastiCache cluster.


**Statistic:** Average


**Recommended threshold:** Depends on your situation


**Threshold justification:** The recommended threshold value for this alarm is highly dependent on the acceptable range of connections for your cluster. Review the capacity and the expected workload of your ElastiCache cluster and analyze the historical connection counts during regular usage to establish a baseline, and then select a threshold accordingly. Remember that each node can support up to 65,000 concurrent connections.


**Period:** 60


**Datapoints to alarm:** 10


**Evaluation periods:** 10


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**DatabaseMemoryUsagePercentage**

**Dimensions:** CacheClusterId


**Alarm description:** This alarm helps you monitor the memory utilization of your 
 cluster. When your `DatabaseMemoryUsagePercentage` reaches 100%, the Redis OSS maxmemory policy is 
 triggered and evictions might occur based on the policy selected. If no object in the cache matches the eviction policy, write operations fail. Some workloads expect or rely on evictions, but if not, you will need to increase the memory capacity of your cluster. You can scale your cluster out by adding more primary nodes, or scale it up by using a larger node type. Refer to [Scaling ElastiCache for Redis OSS clusters](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Scaling.html "https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Scaling.html") for details.


**Intent:** This alarm is used to detect high memory utilization of your cluster so that you can avoid failures when writing to your cluster. It is useful to know when you’ll need to scale up your cluster if your application does not expect to experience evictions.


**Statistic:** Average


**Recommended threshold:** Depends on your situation


**Threshold justification:** Depending on your application’s memory requirements and the memory capacity of your ElastiCache cluster, you should set the threshold to the percentage that reflects the critical level of memory usage of the cluster. You can use historical memory usage data as reference for acceptable memory usage threshold.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**EngineCPUUtilization**

**Dimensions:** CacheClusterId


**Alarm description:** This alarm helps to monitor the CPU utilization of a Redis OSS engine thread within the ElastiCache instance. Common reasons for high engine CPU are long-running commands that consume high CPU, a high number of requests, an increase of new client connection requests in a short time period, and high evictions when the cache doesn’t have enough memory to hold new data. You should consider [Scaling ElastiCache for Redis OSS clusters](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Scaling.html "https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Scaling.html") by adding more nodes or scaling up your instance type.


**Intent:** This alarm is used to detect high CPU utilization of the Redis OSS engine thread. It is useful if you want to monitor the CPU usage of the database engine itself.


**Statistic:** Average


**Recommended threshold:** 90.0


**Threshold justification:** Set the threshold to a percentage that reflects the critical engine CPU utilization level for your application. You can benchmark your cluster using your application and expected workload to correlate EngineCPUUtilization and performance as a reference, and then set the threshold accordingly. In most cases, you can set the threshold to about 90% of your available CPU.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**ReplicationLag**

**Dimensions:** CacheClusterId


**Alarm description:** This alarm helps to monitor the replication health of your ElastiCache cluster. A high replication lag means that the primary node or the replica can’t keep up the pace of the replication. If your write activity is too high, consider scaling your cluster out by adding more primary nodes, or scaling it up by using a larger node type. Refer to [Scaling ElastiCache for Redis OSS clusters](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Scaling.html "https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Scaling.html") for details. If your read replicas are overloaded by the amount of read requests, consider adding more read replicas.


**Intent:** This alarm is used to detect a delay between data updates on the primary node and their synchronization to replica node. It helps to ensure data consistency of a read replica cluster node.


**Statistic:** Average


**Recommended threshold:** Depends on your situation


**Threshold justification:** Set the threshold according to your application's requirements and the potential impact of replication lag. You should consider your application's expected write rates and network conditions for the acceptable replication lag.


**Period:** 60


**Datapoints to alarm:** 15


**Evaluation periods:** 15


**Comparison Operator:** GREATER\_THAN\_THRESHOLD




## Amazon ECS


The following are the recommended alarms for Amazon ECS.




**CPUReservation**

**Dimensions:** ClusterName


**Alarm description:** This alarm helps you detect a high CPU reservation of the ECS cluster. High CPU reservation might indicate that the cluster is running out of registered CPUs for the task. To troubleshoot, you can add more capacity, you can scale the cluster, or you can set up auto scaling.


**Intent:** The alarm is used to detect whether the total number of CPU units reserved by tasks on the cluster is reaching the total CPU units registered for the cluster. This helps you know when to scale up the cluster. Reaching the total CPU units for the cluster can result in running out of CPU for tasks. If you have EC2 capacity providers managed scaling turned on, or you have associated Fargate to capacity providers, then this alarm is not recommended.


**Statistic:** Average


**Recommended threshold:** 80.0


**Threshold justification:** Set the threshold for
 CPU reservation to 80%. Alternatively, you can choose a lower value based on
 cluster characteristics.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**CPUUtilization**

**Dimensions:** ClusterName, ServiceName


**Alarm description:** This alarm helps you detect a high CPU utilization of the ECS service. If there is no ongoing ECS deployment, a maxed-out CPU utilization might indicate a resource bottleneck or application performance problems. To troubleshoot, you can increase the CPU limit.


**Intent:** This alarm is used to detect high CPU
 utilization for the Amazon ECS service. Consistent high CPU utilization can indicate
 a resource bottleneck or application performance problems.


**Statistic:** Average


**Recommended threshold:** 80.0


**Threshold justification:** The service metrics for
 CPU utilization might exceed 100% utilization. However, we recommend that you
 monitor the metric for high CPU utilization to avoid impacting other services.
 Set the threshold to about 80-85%. We recommend that you update your task
 definitions to reflect actual usage to prevent future issues with other
 services.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**EBSFilesystemUtilization**

**Dimensions:** ClusterName, ServiceName


**Alarm description:** This alarm helps you detect high storage utilization of the Amazon EBS volume attached to Amazon ECS tasks. If the utilization of the Amazon EBS volume is 
 consistently high, you can check the usage and increase the volume size for new tasks.


**Intent:** This alarm is used to detect high storage utilization of the Amazon EBS volumes attached to Amazon ECS tasks. Consistently high storage 
 utilization can indicate that the Amazon EBS volume is full and it might lead to failure of the container.


**Statistic:** Average


**Recommended threshold:** 80.0


**Threshold justification:** You can set the
 threshold for Amazon EBS file system utilization to about 80%. You can adjust this
 value based on the acceptable storage utilization. For a read-only snapshot
 volume, a high utilization might indicate that the volume is right sized. For an
 active data volume, high storage utilization might indicate that the application
 is writing a large amount of data which may cause the container to fail if there
 is not enough capacity.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**MemoryReservation**

**Dimensions:** ClusterName


**Alarm description:** This alarm helps you detect a
 high memory reservation of the Amazon ECS cluster. High memory reservation might
 indicate a resource bottleneck for the cluster. To troubleshoot, analyze the
 service task for performance to see if memory utilization of the task can be
 optimized. Also, you can register more memory or set up auto scaling.


**Intent:** The alarm is used to detect whether the total memory units reserved by tasks on the cluster is reaching the total memory units registered for the cluster. This can help you know when to scale up the cluster. Reaching the total memory units for the cluster can cause the cluster to be unable to launch new tasks. If you have EC2 capacity providers managed scaling turned on or you have associated Fargate to capacity providers, this alarm is not recommended.


**Statistic:** Average


**Recommended threshold:** 80.0


**Threshold justification:** Set the threshold for
 memory reservation to 80%. You can adjust this to a lower value based on cluster
 characteristics.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**MemoryUtilization**

**Dimensions:** ClusterName, ServiceName


**Alarm description:** This alarm helps you detect a high memory utilization of the Amazon ECS service. If there is no ongoing Amazon ECS deployment, 
 a maxed-out memory utilization might indicate a resource bottleneck or application performance problems. To troubleshoot, you can increase the memory limit.


**Intent:** This alarm is used to detect high memory utilization for the Amazon ECS service. Consistent high memory utilization can
 indicate a resource bottleneck or application performance problems.


**Statistic:** Average


**Recommended threshold:** 80.0


**Threshold justification:** The service metrics for memory utilization might exceed 100% utilization. However, we recommend that you monitor the metric for high memory utilization to avoid impacting other services. Set the threshold to about 80%. We recommend that you update your task definitions to reflect actual usage to prevent future issues with other services.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**HTTPCode\_Target\_5XX\_Count**

**Dimensions:** ClusterName, ServiceName


**Alarm description:** This alarm helps you detect a high server-side error count for the ECS service. This can indicate that there are errors that cause the server to be unable to serve requests. To troubleshoot, check your application logs.


**Intent:** This alarm is used to detect a high server-side error count for the ECS service.


**Statistic:** Sum


**Recommended threshold:** Depends on your situation


**Threshold justification:** Calculate the value of about 5% of 
 the your average traffic and use this value as a starting point for the threshold. You can find 
 the average traffic by using the `RequestCount` metric. You can also analyze historical 
 data to determine the acceptable error rate for the application workload, and then tune the threshold accordingly. Frequently occurring 5XX errors need to be alarmed on. However, setting a very low value for the threshold can cause the alarm to be too sensitive.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**TargetResponseTime**

**Dimensions:** ClusterName, ServiceName


**Alarm description:** This alarm helps you detect a high target response time for ECS service requests. This can indicate that there are problems that cause the service to be unable to serve requests in time. To troubleshoot, check the CPUUtilization metric to see if the service is running out of CPU, or check the CPU utilization of other downstream services that your service depends on.


**Intent:** This alarm is used to detect a high target response time for ECS service requests.


**Statistic:** Average


**Recommended threshold:** Depends on your situation


**Threshold justification:** The recommended threshold value for this alarm is highly dependent on your use case. Review the criticality and requirements of the target response time of the service and analyze the historical behavior of this metric to determine sensible threshold levels.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD




## Amazon ECS with Container Insights


The following are the recommended alarms for Amazon ECS with Container Insights.




**EphemeralStorageUtilized**

**Dimensions:** ClusterName, ServiceName


**Alarm description:** This alarm helps you detect high ephemeral storage 
 utilized of the Fargate cluster. If ephemeral storage is consistently high, you can check ephemeral storage 
 usage and increase the ephemeral storage.


**Intent:** This alarm is used to detect high ephemeral storage usage for the 
 Fargate cluster. Consistent high ephemeral storage utilized can indicate that the disk is full and it 
 might lead to failure of the container.


**Statistic:** Average


**Recommended threshold:** Depends on your situation


**Threshold justification:** Set the threshold to about 90% of the 
 ephemeral storage size. You can adjust this value based on your acceptable ephemeral storage utilization 
 of the Fargate cluster. For some systems, a consistently high ephemeral storage utilized might be normal, 
 while for others, it might lead to failure of the container.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**RunningTaskCount**

**Dimensions:** ClusterName, ServiceName


**Alarm description:** This alarm helps you detect a low running task 
 count of the Amazon ECS service. If the running task count is too low, it can can indicate that the application 
 can’t handle the service load and it might lead to performance issues. If there is no running task, the Amazon ECS 
 service might be unavailable or there might be deployment issues.


**Intent:** This alarm is used to detect whether the number of running 
 tasks are too low. A consistent low running task count can indicate Amazon ECS service deployment or performance 
 issues.


**Statistic:** Average


**Recommended threshold:** 0.0


**Threshold justification:** You can adjust the threshold based on the 
 minimum running task count of the Amazon ECS service. If the running task count is 0, the Amazon ECS service will be 
 unavailable.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** LESS\_THAN\_OR\_EQUAL\_TO\_THRESHOLD



**TaskCpuUtilization**

**Dimensions:** ClusterName


**Alarm description:** This alarm helps you detect high CPU utilization of tasks in your Amazon ECS cluster. 
 If task CPU utilization is consistently high, you might need to optimize your tasks or increase their CPU reservation.


**Intent:** This alarm is used to detect high CPU utilization for tasks in the Amazon ECS cluster. 
 Consistent high CPU utilization can indicate that the tasks are under stress and might need more CPU resources or optimization to maintain performance.


**Statistic:** Average


**Recommended threshold:** 80.0


**Threshold justification:** Set the threshold to about 80% of the task's CPU reservation.
 You can adjust this value based on your acceptable CPU utilization for the tasks. For some workloads, consistently high CPU utilization 
 might be normal, while for others, it might indicate performance issues or the need for more resources.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**TaskCpuUtilization**

**Dimensions:** ClusterName, ServiceName


**Alarm description:** This alarm helps you detect high CPU utilization of tasks belonging to the Amazon ECS service. 
 If task CPU utilization is consistently high, you might need to optimize your tasks or increase their CPU reservation.


**Intent:** This alarm is used to detect high CPU utilization for tasks belonging to the Amazon ECS service. 
 Consistent high CPU utilization can indicate that the tasks are under stress and might need more CPU resources or optimization to maintain performance.


**Statistic:** Average


**Recommended threshold:** 80.0


**Threshold justification:** Set the threshold to about 80% of the task's CPU reservation. You can 
 adjust this value based on your acceptable CPU utilization for the tasks. For some workloads, consistently high CPU utilization might be normal, 
 while for others, it might indicate performance issues or the need for more resources.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**ContainerCpuUtilization**

**Dimensions:** ClusterName


**Alarm description:** This alarm monitors the percentage of CPU units used by containers in your Amazon ECS cluster 
 relative to their reserved CPU. It helps detect when containers are approaching their CPU limits based on the ContainerCpuUtilized/ContainerCpuReserved ratio.


**Intent:** This alarm detects when containers in the Amazon ECS cluster are using a high percentage of their 
 reserved CPU capacity, calculated as `ContainerCpuUtilized/ContainerCpuReserved`. Sustained high values indicate containers are operating 
 near their CPU limits and might need capacity adjustments.


**Statistic:** Average


**Recommended threshold:** 80.0


**Threshold justification:** Set the threshold to about 80% of the container's CPU utilization ratio. 
 This provides an early warning when containers are approaching their CPU capacity limits while allowing for normal fluctuations in CPU usage. 
 The threshold can be adjusted based on your workload characteristics and performance requirements.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**ContainerCpuUtilization**

**Dimensions:** ClusterName, ServiceName


**Alarm description:** This alarm monitors the percentage of CPU units used by 
 containers belonging to the Amazon ECS service relative to their reserved CPU. It helps detect when containers are 
 approaching their CPU limits based on the ContainerCpuUtilized/ContainerCpuReserved ratio.


**Intent:** This alarm detects when containers belonging to the Amazon ECS service 
 are using a high percentage of their reserved CPU capacity, calculated as ContainerCpuUtilized/ContainerCpuReserved. 
 Sustained high values indicate containers are operating near their CPU limits and might need capacity adjustments.


**Statistic:** Average


**Recommended threshold:** 80.0


**Threshold justification:** Set the threshold to about 80% of the container's 
 CPU utilization ratio. This provides an early warning when containers are approaching their CPU capacity limits 
 while allowing for normal fluctuations in CPU usage. The threshold can be adjusted based on your workload characteristics and performance requirements.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**TaskEphemeralStorageUtilization**

**Dimensions:** ClusterName


**Alarm description:** This alarm helps you detect high ephemeral storage utilization of 
 tasks in your Amazon ECS cluster. If storage utilization is consistently high, you might need to optimize your storage usage or increase the storage reservation.


**Intent:** This alarm is used to detect high ephemeral storage utilization for tasks in the Amazon ECS 
 cluster. Consistent high storage utilization can indicate that the task is running out of disk space and might need more storage 
 resources or optimization to maintain proper operation.


**Statistic:** Average


**Recommended threshold:** 80.0


**Threshold justification:** Set the threshold to about 80% of the task's ephemeral storage reservation. 
 You can adjust this value based on your acceptable storage utilization for the tasks. For some workloads, consistently high storage 
 utilization might be normal, while for others, it might indicate potential disk space issues or the need for more storage.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**TaskEphemeralStorageUtilization**

**Dimensions:** ClusterName, ServiceName


**Alarm description:** This alarm helps you detect high ephemeral storage utilization of tasks belonging to 
 the Amazon ECS service. If storage utilization is consistently high, you might need to optimize your storage usage or increase the storage reservation.


**Intent:** This alarm is used to detect high ephemeral storage utilization for tasks belonging to the Amazon ECS 
 service. Consistent high storage utilization can indicate that the task is running out of disk space and might need more storage resources 
 or optimization to maintain proper operation.


**Statistic:** Average


**Recommended threshold:** 80.0


**Threshold justification:** Set the threshold to about 80% of the task's ephemeral storage reservation. 
 You can adjust this value based on your acceptable storage utilization for the tasks. For some workloads, consistently high storage 
 utilization might be normal, while for others, it might indicate potential disk space issues or the need for more storage.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**TaskMemoryUtilization**

**Dimensions:** ClusterName


**Alarm description:** This alarm helps you detect high memory utilization of tasks in your Amazon ECS cluster. If memory utilization is consistently high, you might need to optimize your tasks or increase the memory reservation.


**Intent:** This alarm is used to detect high memory utilization for tasks in the Amazon ECS cluster. Consistent high memory utilization can indicate that the task is under memory pressure and might need more memory resources or optimization to maintain stability.


**Statistic:** Average


**Recommended threshold:** 80.0


**Threshold justification:** Set the threshold to about 80% of the task's memory reservation. You can adjust this value based on your acceptable memory utilization for the tasks. For some workloads, consistently high memory utilization might be normal, while for others, it might indicate memory pressure or the need for more resources.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**TaskMemoryUtilization**

**Dimensions:** ClusterName, ServiceName


**Alarm description:** This alarm helps you detect high memory utilization of tasks belonging to the Amazon ECS service. 
 If memory utilization is consistently high, you might need to optimize your tasks or increase the memory reservation.


**Intent:** This alarm is used to detect high memory utilization for tasks belonging to the Amazon ECS service. 
 Consistent high memory utilization can indicate that the task is under memory pressure and might need more memory resources or optimization to maintain stability.


**Statistic:** Average


**Recommended threshold:** 80.0


**Threshold justification:** Set the threshold to about 80% of the task's memory reservation. 
 You can adjust this value based on your acceptable memory utilization for the tasks. For some workloads, consistently high 
 memory utilization might be normal, while for others, it might indicate memory pressure or the need for more resources.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**ContainerMemoryUtilization**

**Dimensions:** ClusterName


**Alarm description:** This alarm helps you detect high memory utilization of containers in your Amazon ECS cluster. 
 If memory utilization is consistently high, you might need to optimize your containers or increase the memory reservation.


**Intent:** This alarm is used to detect high memory utilization for containers in the Amazon ECS cluster. 
 Consistent high memory utilization can indicate that the container is under memory pressure and might need more memory resources or optimization to maintain stability.


**Statistic:** Average


**Recommended threshold:** 80.0


**Threshold justification:** Set the threshold to about 80% of the container's memory reservation. 
 You can adjust this value based on your acceptable memory utilization for the containers. For some workloads, consistently high 
 memory utilization might be normal, while for others, it might indicate memory pressure or the need for more resources.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**ContainerMemoryUtilization**

**Dimensions:** ClusterName, ServiceName


**Alarm description:** This alarm helps you detect high memory utilization of containers belonging to the Amazon ECS service. 
 If memory utilization is consistently high, you might need to optimize your containers or increase the memory reservation.


**Intent:** This alarm is used to detect high memory utilization for containers belonging to the Amazon ECS service. 
 Consistent high memory utilization can indicate that the container is under memory pressure and might need more memory resources or optimization to maintain stability.


**Statistic:** Average


**Recommended threshold:** 80.0


**Threshold justification:** Set the threshold to about 80% of the container's memory reservation. You 
 can adjust this value based on your acceptable memory utilization for the containers. For some workloads, consistently high memory
 utilization might be normal, while for others, it might indicate memory pressure or the need for more resources.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**instance\_filesystem\_utilization**

**Dimensions:** InstanceId, ContainerInstanceId, ClusterName


**Alarm description:** This alarm helps you detect a high file system 
 utilization of the Amazon ECS cluster. If the file system utilization is consistently high, check the disk usage.


**Intent:** This alarm is used to detect high file system utilization 
 for the Amazon ECS cluster. A consistent high file system utilization can indicate a resource bottleneck or 
 application performance problems, and it might prevent running new tasks.


**Statistic:** Average


**Recommended threshold:** 90.0


**Threshold justification:** You can set the threshold for file system 
 utilization to about 90-95%. You can adjust this value based on the acceptable file system capacity level of 
 the Amazon ECS cluster. For some systems, a consistently high file system utilization might be normal and 
 not indicate a problem, while for others, it might be a cause of concern and might lead to performance 
 issues and prevent running new tasks.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD




## Amazon ECS with Container Insights with enhanced observability


The following are the recommended alarms for Amazon ECS with Container Insights with enhanced observability.




**TaskCpuUtilization**

**Dimensions:** ClusterName, ServiceName


**Alarm description:** This alarm helps you
 detect the total percentage of CPU units being used by a task. 


**Intent:** This alarm is used to detect high task CPU utilization.


**Statistic:** Average


**Recommended threshold:** 80.0


**Threshold justification:** Typically, you can
 set the threshold for CPU utilization to 80%. However, you can adjust this value
 based on your acceptable performance level and workload characteristics. For
 some tasks, consistently high CPU utilization may be normal and not indicate a
 problem, while for others, it may be cause of concern. Analyze historical CPU
 utilization data to identify the usage, find what CPU utilization is acceptable
 for your tasks, and set the threshold accordingly.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**TaskMemoryUtilization**

**Dimensions:** ClusterName, ServiceName


**Alarm description:** This alarm helps you
 detect the total percentage of memory being used by a task. 


**Intent:** This alarm is used to detect high
 memory utilization.


**Statistic:** Average


**Recommended threshold:** 80.0


**Threshold justification:** Typically, you can
 set the threshold for memory utilization to 80%. However, you can adjust this
 value based on your acceptable performance level and workload characteristics.
 For some tasks, consistently high memory utilization may be normal and not
 indicate a problem, while for others, it may be cause of concern. Analyze
 historical memory utilization data to identify the usage, find what memory
 utilization is acceptable for your tasks, and set the threshold
 accordingly.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** LESS\_THAN\_OR\_EQUAL\_TO\_THRESHOLD



**ContainerCPUUtilization**

**Dimensions:** ContainerName, ClusterName,
 ServiceName


**Alarm description:** This alarm helps you
 detect the total percentage of CPU units being used by a container. 


**Intent:** This alarm is used to detect high task CPU utilization.


**Statistic:** Average


**Recommended threshold:** 80.0


**Threshold justification:** Typically, you can
 set the threshold for CPU utilization to 80%. However, you can adjust this value
 based on your acceptable performance level and workload characteristics. For
 some containers, consistently high CPU utilization may be normal and not
 indicate a problem, while for others, it may be cause of concern. Analyze
 historical CPU utilization data to identify the usage, find what CPU utilization
 is acceptable for your containers, and set the threshold accordingly.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**ContainerMemoryUtilization**

**Dimensions:** ContainerName, ClusterName, ServiceName


**Alarm description:** This alarm helps you
 detect the total percentage of memory units being used by a container.


**Intent:** This alarm is used to detect high
 task memory utilization.


**Statistic:** Average


**Recommended threshold:** 80.0


**Threshold justification:** Typically, you can
 set the threshold for memory utilization to 80%. However, you can adjust this
 value based on your acceptable performance level and workload characteristics.
 For some containers, consistently high memory utilization may be normal and not
 indicate a problem, while for others, it may be cause of concern. Analyze
 historical memory utilization data to identify the usage, find what memory
 utilization is acceptable for your tasks, and set the threshold
 accordingly.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** LESS\_THAN\_OR\_EQUAL\_TO\_THRESHOLD



**TaskEBSfilesystemUtilization**

**Dimensions:** ClusterName, ServiceName


**Alarm description:** This alarm helps you detect the total percentage of ephemeral storage being used by a task. .


**Intent:** This alarm is used to detect high
 Amazon EBS file system usage for a task. 


**Statistic:** Average


**Recommended threshold:** 80.0


**Threshold justification:** Set the threshold to
 about 80% of the Amazon EBS file system size. 


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**TaskEphemeralStorageUtilization**

**Dimensions:** ClusterName, ServiceName


**Alarm description:** This alarm helps you detect the total percentage of ephemeral storage being used by a task.


**Intent:** This alarm is used to detect high
 ephemeral storage usage for a task. Consistent high ephemeral storage utilized
 can indicate that the disk is full and it might lead to failure of the
 task.


**Statistic:** Average


**Recommended threshold:** 80.0


**Threshold justification:** Set the threshold to
 about 80% of the ephemeral storage size. 


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD




## Amazon EFS




**PercentIOLimit**

**Dimensions:** FileSystemId


**Alarm description:** This alarm helps in ensuring that the workload stays within the I/O limit available to the file system. If the metric reaches its I/O limit consistently, consider moving the application to a file system that uses Max I/O performance as mode. For troubleshooting, check clients that are connected to the file system and applications of the clients that throttles the file system.


**Intent:** This alarm is used to detect how close the file system is to reach the I/O limit of the General Purpose performance mode. Consistent high I/O percentage can be an indicator of the file system cannot scale with respect to I/O requests enough and the file system can be a resource bottleneck for the applications that use the file system.


**Statistic:** Average


**Recommended threshold:** 100.0


**Threshold justification:** When the file system reaches its I/O limit, it may respond to read and write requests slower. Therefore, it is recommended that the metric is monitored to avoid impacting applications that use the file system. The threshold can be set around 100%. However, this value can be adjusted to a lower value based on file system characteristics.


**Period:** 60


**Datapoints to alarm:** 15


**Evaluation periods:** 15


**Comparison Operator:** GREATER\_THAN\_OR\_EQUAL\_TO\_THRESHOLD



**BurstCreditBalance**

**Dimensions:** FileSystemId


**Alarm description:** This alarm helps in ensuring that there is available burst credit balance for the file system usage. When there is no available burst credit, applications access to the the file system will be limited due to low throughput. If the metric drops to 0 consistently, consider changing the throughput mode to [Elastic or Provisioned throughput mode](https://docs.aws.amazon.com/efs/latest/ug/performance.html#throughput-modes "https://docs.aws.amazon.com/efs/latest/ug/performance.html#throughput-modes").


**Intent:** This alarm is used to detect low burst credit balance of the file system. Consistent low burst credit balance can be an indicator of the slowing down in throughput and increase in I/O latency.


**Statistic:** Average


**Recommended threshold:** 0.0


**Threshold justification:** When the file system run out of burst credits and even if the baseline throughput rate is lower, EFS continues to provide a metered throughput of 1 MiBps to all file systems. However, it is recommended that the metric is monitored for low burst credit balance to avoid the file system acting as resource bottleneck for the applications. The threshold can be set around 0 bytes.


**Period:** 60


**Datapoints to alarm:** 15


**Evaluation periods:** 15


**Comparison Operator:** LESS\_THAN\_OR\_EQUAL\_TO\_THRESHOLD




## Amazon EKS with Container Insights




**node\_cpu\_utilization**

**Dimensions:** ClusterName


**Alarm description:** This alarm helps to detect high CPU utilization in worker nodes of the EKS cluster. If the utilization is consistently high, it might indicate a need for replacing your worker nodes with instances that have greater CPU or a need to scale the system horizontally.


**Intent:** This alarm helps to monitor the CPU utilization of the worker nodes in the EKS cluster so that the system performance doesn't degrade.


**Statistic:** Maximum


**Recommended threshold:** 80.0


**Threshold justification:** It is recommended to set the threshold at less than or equal to 80% to allow enough time to debug the issue before the system starts seeing impact.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**node\_filesystem\_utilization**

**Dimensions:** ClusterName


**Alarm description:** This alarm helps to detect high file system utilization in the worker nodes of the EKS cluster. If the utilization is consistently high, you might need to update your worker nodes to have larger disk volume, or you might need to scale horizontally.


**Intent:** This alarm helps to monitor the filesystem utilization of the worker nodes in the EKS cluster. If the utilization reaches 100%, it can lead to application failure, disk I/O bottlenecks, pod eviction, or the node to become unresponsive entirely.


**Statistic:** Maximum


**Recommended threshold:** Depends on your situation


**Threshold justification:** If there's sufficient disk pressure (meaning that the disk is getting full), nodes are marked as not healthy, and the pods are evicted from the node. Pods on a node with disk pressure are evicted when the available file system is lower than the eviction thresholds set on the kubelet. Set the alarm threshold so that you have enough time to react before the node is evicted from the cluster.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**node\_memory\_utilization**

**Dimensions:** ClusterName


**Alarm description:** This alarm helps in detecting high memory utilization in worker nodes of the EKS cluster. If the utilization is consistently high, it might indicate a need to scale the number of pod replicas, or optimize your application.


**Intent:** This alarm helps to monitor the memory utilization of the worker nodes in the EKS cluster so that the system performance doesn't degrade.


**Statistic:** Maximum


**Recommended threshold:** 80.0


**Threshold justification:** It is recommended to set the threshold at less than or equal to 80% to allow having enough time to debug the issue before the system starts seeing impact.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**pod\_cpu\_utilization\_over\_pod\_limit**

**Dimensions:** ClusterName, Namespace, Service


**Alarm description:** This alarm helps in detecting high CPU utilization in pods of the EKS cluster. If the utilization is consistently high, it might indicate a need to increase the CPU limit for the affected pod.


**Intent:** This alarm helps to monitor the CPU utilization of the pods belonging to a Kubernetes Service in the EKS cluster, so that you can quickly identify if a service's pod is consuming higher CPU than expected.


**Statistic:** Maximum


**Recommended threshold:** 80.0


**Threshold justification:** It is recommended to set the threshold at less than or equal to 80% to allow having enough time to debug the issue before the system starts seeing impact.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**pod\_memory\_utilization\_over\_pod\_limit**

**Dimensions:** ClusterName, Namespace, Service


**Alarm description:** This alarm helps in detecting high memory utilization in pods of the EKS cluster. If the utilization is consistently high, it might indicate a need to increase the memory limit for the affected pod.


**Intent:** This alarm helps to monitor the memory utilization of the pods in the EKS cluster so that the system performance doesn't degrade.


**Statistic:** Maximum


**Recommended threshold:** 80.0


**Threshold justification:** It is recommended to set the threshold at less than or equal to 80% to allow having enough time to debug the issue before the system starts seeing impact.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD




## Amazon EventBridge Scheduler




**TargetErrorThrottledCount**

**Dimensions:** None


**Alarm description:** This alarm helps you identify target throttling. To avoid target throttling error, 
 consider [configuring 
 flexible time windows](https://docs.aws.amazon.com/scheduler/latest/UserGuide/managing-schedule-flexible-time-windows.html "https://docs.aws.amazon.com/scheduler/latest/UserGuide/managing-schedule-flexible-time-windows.html") to spread your invocation load or increasing limits with the target service.


**Intent:** This alarm is used to detect target throttling errors, which can cause schedule delays.


**Statistic:** Sum


**Recommended threshold:** 0.0


**Threshold justification:** If the target throttling error is consistently greater than 0, 
 schedule delivery is delayed. For some systems, target throttling errors for a brief period of time might be normal, while 
 for others, it might be a cause of concern. Set this alarm's threshold, `datapointsToAlarm`, and `evaluationPeriods` accordingly.


**Period:** 60


**Datapoints to alarm:** 15


**Evaluation periods:** 15


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**InvocationThrottleCount**

**Dimensions:** None


**Alarm description:** This alarm helps you identify invocation throttling by Amazon EventBridge Scheduler. To avoid invocation 
 throttling errors, consider [configuring 
 flexible time windows](https://docs.aws.amazon.com/scheduler/latest/UserGuide/managing-schedule-flexible-time-windows.html "https://docs.aws.amazon.com/scheduler/latest/UserGuide/managing-schedule-flexible-time-windows.html") to spread your invocation load or [increasing 
 invocations throttle limit](https://docs.aws.amazon.com/scheduler/latest/UserGuide/scheduler-quotas.html "https://docs.aws.amazon.com/scheduler/latest/UserGuide/scheduler-quotas.html").


**Intent:** This alarm is used to detect Amazon EventBridge Scheduler invocation throttling errors, which can cause schedule delays.


**Statistic:** Sum


**Recommended threshold:** 0.0


**Threshold justification:** If the invocation throttling is consistently greater than 0, schedule delivery is delayed. 
 For some systems, invocation throttling errors for a brief period of time might be normal, while for others, it might be a cause of concern. 
 Set this alarm's threshold, `datapointsToAlarm`, and `evaluationPeriods` accordingly.


**Period:** 60


**Datapoints to alarm:** 15


**Evaluation periods:** 15


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**InvocationDroppedCount**

**Dimensions:** None


**Alarm description:** This alarm helps you identify invocations dropped by Amazon EventBridge Scheduler. Consider 
 investigating by [configuring 
 a DLQ](https://docs.aws.amazon.com/scheduler/latest/UserGuide/configuring-schedule-dlq.html "https://docs.aws.amazon.com/scheduler/latest/UserGuide/configuring-schedule-dlq.html") for the schedule.


**Intent:** This alarm is used to detect dropped invocations by Amazon EventBridge Scheduler. If you have configured a 
 DLQ correctly on all of your schedules, dropped invocations will appear in the DLQ and you can skip setting up this alarm.


**Statistic:** Sum


**Recommended threshold:** 0.0


**Threshold justification:** Set the threshold to 0 to detect dropped invocations.


**Period:** 60


**Datapoints to alarm:** 1


**Evaluation periods:** 1


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**InvocationsFailedToBeSentToDeadLetterCount**

**Dimensions:** None


**Alarm description:** This alarm helps you identify invocations that were 
 failed to be sent to the configured DLQ by Amazon EventBridge Scheduler. If the metric is consistently greater than 0, modify your DLQ configuration to resolve the issue. 
 Use `InvocationsFailedToBeSentToDeadLetterCount`\_metrics to determine the issue.


**Intent:** This alarm is used to detect invocations failed to be sent to the configured DLQ by Amazon EventBridge Scheduler.


**Statistic:** Sum


**Recommended threshold:** 0.0


**Threshold justification:** Set the threshold to 0 to detect any invocations that were failed to be 
 sent to the configured DLQ. Retryable errors also show up in this metric, so `datapointsToAlarm` for this alarm has been set to 15.


**Period:** 60


**Datapoints to alarm:** 15


**Evaluation periods:** 15


**Comparison Operator:** GREATER\_THAN\_THRESHOLD




## Amazon Kinesis Data Streams




**GetRecords.IteratorAgeMilliseconds**

**Dimensions:** StreamName


**Alarm description:** This alarm can detect if iterator maximum age is too high. For real-time data processing applications, configure data retention according to tolerance of the delay. This is usually within minutes. For applications that process historic data, use this metric to monitor catchup speed. A quick solution to stop data loss is to increase the retention period while you troubleshoot the issue. You can also increase the number of workers processing records in your consumer application. The most common causes for gradual iterator age increase are insufficient physical resources or record processing logic that has not scaled with an increase in stream throughput. See [link](https://repost.aws/knowledge-center/kinesis-data-streams-iteratorage-metric "https://repost.aws/knowledge-center/kinesis-data-streams-iteratorage-metric") for more details.


**Intent:** This alarm is used to detect if data in your stream is going to expire because of being preserved too long or because record processing is too slow. It helps you avoid data loss after reaching 100% of the stream retention time.


**Statistic:** Maximum


**Recommended threshold:** Depends on your situation


**Threshold justification:** The recommended threshold value for this alarm is highly dependent on the stream retention period and tolerance of processing delay for the records. Review your requirements and analyze historical trends, and then set the threshold to the number of milliseconds that represents a critical processing delay. If an iterator's age passes 50% of the retention period (by default, 24 hours, configurable up to 365 days), there is a risk for data loss because of record expiration. You can monitor the metric to make sure that none of your shards ever approach this limit.


**Period:** 60


**Datapoints to alarm:** 15


**Evaluation periods:** 15


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**GetRecords.Success**

**Dimensions:** StreamName


**Alarm description:** This metric increments whenever your consumers 
 successfully read data from your stream. `GetRecords` doesn't return any data when it throws 
 an exception. The most common exception is `ProvisionedThroughputExceededException` because 
 request rate for the stream is too high, or because available throughput is already served for 
 the given second. Reduce the frequency or size of your requests. For more information, see 
 Streams [Limits](https://docs.aws.amazon.com/streams/latest/dev/service-sizes-and-limits.html "https://docs.aws.amazon.com/streams/latest/dev/service-sizes-and-limits.html") 
 in the Amazon Kinesis Data Streams Developer Guide, and 
[Error Retries and Exponential Backoff 
 in AWS](https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html "https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html").


**Intent:** This alarm can detect if the retrieval of records from the stream by consumers is failing. By setting an alarm on this metric, you can proactively detect any issues with data consumption, such as increased error rates or a decline in successful retrievals. This allows you to take timely actions to resolve potential problems and maintain a smooth data processing pipeline.


**Statistic:** Average


**Recommended threshold:** Depends on your situation


**Threshold justification:** Depending on the importance of retrieving records from the stream, set the threshold based on your application’s tolerance for failed records. The threshold should be the corresponding percentage of successful operations. You can use historical GetRecords metric data as reference for the acceptable failure rate. You should also consider retries when setting the threshold because failed records can be retried. This helps to prevent transient spikes from triggering unnecessary alerts.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** LESS\_THAN\_THRESHOLD



**PutRecord.Success**

**Dimensions:** StreamName


**Alarm description:** This alarm detects when the number of failed `PutRecord` operations breaches the threshold. Investigate the data producer logs to find the root causes of the failures. The most common reason is insufficient provisioned throughput on the shard that caused the `ProvisionedThroughputExceededException`. It happens because the request rate for the stream is too high, or the throughput attempted to be ingested into the shard is too high. Reduce the frequency or size of your requests. For more information, see Streams [Limits](https://docs.aws.amazon.com/streams/latest/dev/service-sizes-and-limits.html "https://docs.aws.amazon.com/streams/latest/dev/service-sizes-and-limits.html") and [Error Retries and Exponential Backoff in AWS](https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html "https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html").


**Intent:** This alarm can detect if ingestion of records into the stream is failing. It helps you identify issues in writing data to the stream. By setting an alarm on this metric, you can proactively detect any issues of producers in publishing data to the stream, such as increased error rates or a decrease in successful records being published. This enables you to take timely actions to address potential problems and maintain a reliable data ingestion process.


**Statistic:** Average


**Recommended threshold:** Depends on your situation


**Threshold justification:** Depending on the importance of data ingestion and processing to your service, set the threshold based on your application’s tolerance for failed records. The threshold should be the corresponding percentage of successful operations. You can use historical PutRecord metric data as reference for the acceptable failure rate. You should also consider retries when setting the threshold because failed records can be retried.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** LESS\_THAN\_THRESHOLD



**PutRecords.FailedRecords**

**Dimensions:** StreamName


**Alarm description:** This alarm detects when the number of failed `PutRecords` exceeds the threshold. Kinesis Data Streams attempts to process all records in each `PutRecords` request, but a single record failure does not stop the processing of subsequent records. The main reason for these failures is exceeding the throughput of a stream or an individual shard. Common causes are traffic spikes and network latencies that cause records to arrive to the stream unevenly. You should detect unsuccessfully processed records and retry them in a subsequent call. Refer to [Handling Failures When Using PutRecords](https://docs.aws.amazon.com/streams/latest/dev/developing-producers-with-sdk.html "https://docs.aws.amazon.com/streams/latest/dev/developing-producers-with-sdk.html") for more details.


**Intent:** This alarm can detect consistent failures when using batch operation to put records to your stream. By setting an alarm on this metric, you can proactively detect an increase in failed records, enabling you to take timely actions to address the underlying problems and ensure a smooth and reliable data ingestion process.


**Statistic:** Sum


**Recommended threshold:** Depends on your situation


**Threshold justification:** Set the threshold to the number of failed records reflecting the tolerance of the the application for failed records. You can use historical data as reference for the acceptable failure value. You should also consider retries when setting the threshold because failed records can be retried in subsequent PutRecords calls.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**ReadProvisionedThroughputExceeded**

**Dimensions:** StreamName


**Alarm description:** The alarm tracks the number of records that result in read throughput capacity throttling. If you find that you are being consistently throttled, you should consider adding more shards to your stream to increase your provisioned read throughput. If there is more than one consumer application running on the stream, and they share the `GetRecords` limit, we recommend that you register new consumer applications via Enhanced Fan-Out. If adding more shards does not lower the number of throttles, you may have a “hot” shard that is being read from more than other shards are. Enable enhanced monitoring, find the “hot” shard, and split it.


**Intent:** This alarm can detect if consumers are throttled when they exceed your provisioned read throughput (determined by the number of shards you have). In that case, you won’t be able to read from the stream, and the stream can start backing up.


**Statistic:** Average


**Recommended threshold:** Depends on your situation


**Threshold justification:** Usually throttled requests can be retried and hence setting the threshold to zero makes the alarm too sensitive. However, consistent throttling can impact reading from the stream and should trigger the alarm. Set the threshold to a percentage according to the throttled requests for the application and retry configurations.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**SubscribeToShardEvent.MillisBehindLatest**

**Dimensions:** StreamName, ConsumerName


**Alarm description:** This alarm detects when the delay of record processing in the application breaches the threshold. Transient problems such as API operation failures to a downstream application can cause a sudden increase in the metric. You should investigate if they consistently happen. A common cause is the consumer is not processing records fast enough because of insuﬃcient physical resources or record processing logic that has not scaled with an increase in stream throughput. Blocking calls in critical path is often the cause of slowdowns in record processing. You can increase your parallelism by increasing the number of shards. You should also confirm underlying processing nodes have sufficient physical resources during peak demand.


**Intent:** This alarm can detect delay in the subscription to shard event of the stream. This indicates a processing lag and can help identify potential issues with the consumer application's performance or the overall stream's health. When the processing lag becomes significant, you should investigate and address any bottlenecks or consumer application inefficiencies to ensure real-time data processing and minimize data backlog.


**Statistic:** Average


**Recommended threshold:** Depends on your situation


**Threshold justification:** The recommended threshold value for this alarm is highly dependent on the delay that your application can tolerate. Review your application's requirements and analyze historical trends, and then select a threshold accordingly. When the SubscribeToShard call succeeds, your consumer starts receiving SubscribeToShardEvent events over the persistent connection for up to 5 minutes, after which time you need to call SubscribeToShard again to renew the subscription if you want to continue to receive records.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**WriteProvisionedThroughputExceeded**

**Dimensions:** StreamName


**Alarm description:** This alarm detects when the number of records resulting in write throughput capacity throttling reached the threshold. When your producers exceed your provisioned write throughput (determined by the number of shards you have), they are throttled and you won’t be able to put records to the stream. To address consistent throttling, you should consider adding shards to your stream. This raises your provisioned write throughput and prevents future throttling. You should also consider partition key choice when ingesting records. Random partition key is preferred because it spreads records evenly across the shards of the stream, whenever possible.


**Intent:** This alarm can detect if your producers are being rejected for writing records because of throttling of the stream or shard. If your stream is in Provisioned mode, then setting this alarm helps you proactively take actions when the data stream reaches its limits, allowing you to optimize the provisioned capacity or take appropriate scaling actions to avoid data loss and maintain smooth data processing.


**Statistic:** Average


**Recommended threshold:** Depends on your situation


**Threshold justification:** Usually throttled requests can be retried, so setting the threshold to zero makes the alarm too sensitive. However, consistent throttling can impact writing to the stream, and you should set the alarm threshold to detect this. Set the threshold to a percentage according to the throttled requests for the application and retry configurations.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD




## Lambda




**ClaimedAccountConcurrency**

**Dimensions:** None


**Alarm description:** This alarm helps to monitor if the concurrency of your Lambda functions is approaching the Region-level concurrency limit of your account. A function 
 starts to be throttled if it reaches the concurrency limit. You can take the following actions to avoid throttling. 



1. [Request a concurrency increase](https://repost.aws/knowledge-center/lambda-concurrency-limit-increase "https://repost.aws/knowledge-center/lambda-concurrency-limit-increase") in this Region.
2. Identify and reduce any unused reserved concurrency or provisioned concurrency.
3. Identify performance issues in the functions to improve the speed of processing and
 therefore improve throughput.
4. Increase the batch size of the functions, so that more messages are processed by each function invocation.

**Intent:** This alarm can proactively detect if the concurrency of your Lambda functions is approaching the Region-level concurrency quota of your account, so that you 
 can act on it. Functions are throttled if `ClaimedAccountConcurrency` reaches the Region-level concurrency quota of the account. If you are using Reserved Concurrency (RC) or Provisioned Concurrency (PC), this 
 alarm gives you more visibility on concurrency utilization than an alarm on `ConcurrentExecutions` would.


**Statistic:** Maximum


**Recommended threshold:** Depends on your situation


**Threshold justification:** You should calculate the value of about 90% of the concurrency quota set for the account in the Region, and use the result as the 
 threshold value. By default, your account has a concurrency quota of 1,000 across all functions in a Region. However, you should check the quota of your account from the Service Quotas dashboard.


**Period:** 60


**Datapoints to alarm:** 10


**Evaluation periods:** 10


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**Errors**

**Dimensions:** FunctionName


**Alarm description:** This alarm detects high error counts. Errors includes the exceptions thrown by the code as well as exceptions thrown by the Lambda runtime. You can check the logs related to the function to diagnose the issue.


**Intent:** The alarm helps detect high error counts in function invocations.


**Statistic:** Sum


**Recommended threshold:** Depends on your situation


**Threshold justification:** Set the threshold to a number greater than zero. The exact value can depend on the tolerance for errors in your application. Understand the criticality of the invocations that the function is handling. For some applications, any error might be unacceptable, while other applications might allow for a certain margin of error.


**Period:** 60


**Datapoints to alarm:** 3


**Evaluation periods:** 3


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**Throttles**

**Dimensions:** FunctionName


**Alarm description:** This alarm detects a high number of throttled invocation requests. Throttling occurs when there is no concurrency is available for scale up. There are several approaches to resolve this issue. 1) Request a concurrency increase from AWS Support in this Region. 2) Identify performance issues in the function to improve the speed of processing and therefore improve throughput. 3) Increase the batch size of the function, so that more messages are processed by each function invocation.


**Intent:** The alarm helps detect a high number of throttled invocation requests for a Lambda function. It is important to know if requests are constantly getting rejected due to throttling and if you need to improve Lambda function performance or increase concurrency capacity to avoid constant throttling.


**Statistic:** Sum


**Recommended threshold:** Depends on your situation


**Threshold justification:** Set the threshold to a number greater than zero. The exact value of the threshold can depend on the tolerance of the application. Set the threshold according to its usage and scaling requirements of the function.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_OR\_EQUAL\_TO\_THRESHOLD



**Duration**

**Dimensions:** FunctionName


**Alarm description:** This alarm detects long duration times for processing an event by a Lambda function. Long durations might be because of changes in function code making the function take longer to execute, or the function's dependencies taking longer.


**Intent:** This alarm can detect a long running duration of a Lambda function. High runtime duration indicates that a function is taking a longer time for invocation, and can also impact the concurrency capacity of invocation if Lambda is handling a higher number of events. It is critical to know if the Lambda function is constantly taking longer execution time than expected.


**Statistic:** p90


**Recommended threshold:** Depends on your situation


**Threshold justification:** The threshold for the duration depends on your application and workloads and your performance requirements. For high-performance requirements, set the threshold to a shorter time to see if the function is meeting expectations. You can also analyze historical data for duration metrics to see the if the time taken matches the performance expectation of the function, and then set the threshold to a longer time than the historical average. Make sure to set the threshold lower than the configured function timeout.


**Period:** 60


**Datapoints to alarm:** 15


**Evaluation periods:** 15


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**ConcurrentExecutions**

**Dimensions:** FunctionName


**Alarm description:** This alarm helps to monitor if the concurrency of the function is approaching the Region-level concurrency limit of your account. A function starts to be 
 throttled if it reaches the concurrency limit. You can take the following actions to avoid throttling.



1. Request a concurrency increase in this Region.
2. Identify performance issues in the functions to improve the speed of processing and
 therefore improve throughput.
3. Increase the batch size of the functions, so that more messages are processed by each function invocation.

To get better visibility on reserved concurrency and provisioned concurrency utilization, set an alarm on the new metric `ClaimedAccountConcurrency` instead.


**Intent:** This alarm can proactively detect if the concurrency of the function is approaching the Region-level concurrency quota of your account, so that you can act on it. A function is throttled if it reaches the Region-level concurrency quota of the account.


**Statistic:** Maximum


**Recommended threshold:** Depends on your situation


**Threshold justification:** Set the threshold to about 90% of the concurrency quota set for the account in the Region. By default, your account has a concurrency quota of 1,000 across all functions in a Region. However, you can check the quota of your account, as it can be increased by contacting AWS support.


**Period:** 60


**Datapoints to alarm:** 10


**Evaluation periods:** 10


**Comparison Operator:** GREATER\_THAN\_THRESHOLD




## Lambda Insights


We recommend setting best-practice alarms for the following Lambda Insights metrics.




**memory\_utilization**

**Dimensions:** function\_name


**Alarm description:** This alarm is used to detect if the memory utilization of a lambda function is approaching the configured limit. For troubleshooting, you can try to 1) Optimize your code. 2) Rightly size your memory allocation by accurately estimating the memory requirements. You can refer to 
 [Lambda Power Tuning](https://docs.aws.amazon.com/lambda/latest/operatorguide/profile-functions.html "https://docs.aws.amazon.com/lambda/latest/operatorguide/profile-functions.html") for the same. 3) Use connection pooling. Refer to [Using Amazon RDS Proxy with Lambda](https://aws.amazon.com/blogs/compute/using-amazon-rds-proxy-with-aws-lambda/ "https://aws.amazon.com/blogs/compute/using-amazon-rds-proxy-with-aws-lambda/") for the connection pooling for RDS database. 4) You can also consider designing your functions to avoid storing large amounts of data in memory between invocations.


**Intent:** This alarm is used to detect if the memory utilization for the Lambda function is approaching the configured limit.


**Statistic:** Average


**Threshold Suggestion:** 90.0


**Threshold Justification:** Set the threshold to 90% to get an alert when memory utilization exceeds 90% of the allocated memory. You can adjust this to a lower value if you have a concern for the workload for memory utilization. You can also check the historical data for this metric and set the threshold accordingly.


**Period:** 60


**Datapoints to alarm:** 10


**Evaluation Periods:** 10


**ComparisonOperator:** GREATER\_THAN\_THRESHOLD




## Amazon VPC (`AWS/NATGateway`)




**ErrorPortAllocation**

**Dimensions:** NatGatewayId


**Alarm description:** This alarm helps to detect when the NAT Gateway is unable to allocate ports to new connections. To resolve this issue, see [Resolve port allocation errors on NAT Gateway.](https://repost.aws/knowledge-center/vpc-resolve-port-allocation-errors "https://repost.aws/knowledge-center/vpc-resolve-port-allocation-errors")


**Intent:** This alarm is used to detect if the NAT gateway could not allocate a source port.


**Statistic:** Sum


**Recommended threshold:** 0.0


**Threshold justification:** If the value of ErrorPortAllocation is greater than zero, that means too many concurrent connections to a single popular destination are open through NATGateway.


**Period:** 60


**Datapoints to alarm:** 15


**Evaluation periods:** 15


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**PacketsDropCount**

**Dimensions:** NatGatewayId


**Alarm description:** This alarm helps to detect when packets are dropped by NAT Gateway. This might happen because of an issue with NAT Gateway, so check [AWS service health dashboard](https://health.aws.amazon.com/health/status "https://health.aws.amazon.com/health/status") for the status of AWS NAT Gateway in your Region. This can help you correlate the network issue related to traffic using NAT gateway.


**Intent:** This alarm is used to detect if packets are being dropped by NAT Gateway.


**Statistic:** Sum


**Recommended threshold:** Depends on your situation


**Threshold justification:** You should calculate the value of 0.01 percent of the total traffic on the NAT Gateway and use that result as the threshold value. Use historical data of the traffic on NAT Gateway to determine the threshold.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD




## AWS Private Link (`AWS/PrivateLinkEndpoints`)




**PacketsDropped**

**Dimensions:** VPC Id, VPC Endpoint Id, Endpoint Type, Subnet Id, Service Name


**Alarm description:** This alarm helps to detect if the endpoint or endpoint service is unhealthy by monitoring the number of packets dropped by the endpoint. Note that packets larger than 8500 bytes that arrive at the VPC endpoint are dropped. For troubleshooting, see [connectivity problems between an interface VPC endpoint and an endpoint service](https://repost.aws/knowledge-center/connect-endpoint-service-vpc "https://repost.aws/knowledge-center/connect-endpoint-service-vpc").


**Intent:** This alarm is used to detect if the endpoint or endpoint service is unhealthy.


**Statistic:** Sum


**Recommended threshold:** Depends on your situation


**Threshold justification:** Set the threshold according to the use case. If you want to be aware of the unhealthy status of the endpoint or endpoint service, you should set the threshold low so that you get a chance to fix the issue before a huge data loss. You can use historical data to understand the tolerance for dropped packets and set the threshold accordingly.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD




## AWS Private Link (`AWS/PrivateLinkServices`)




**RstPacketsSent**

**Dimensions:** Service Id, Load Balancer Arn, Az


**Alarm description:** This alarm helps you detect unhealthy targets of an endpoint service based on the number of reset packets that are sent to endpoints. When you debug connection errors with a consumer of your service, you can validate whether the service is resetting connections with the RstPacketsSent metric, or if something else is failing on the network path.


**Intent:** This alarm is used to detect unhealthy targets of an endpoint service.


**Statistic:** Sum


**Recommended threshold:** Depends on your situation


**Threshold justification:** The threshold depends on the use case. If your use case can tolerate targets being unhealthy, you can set the threshold high. If the use case can’t tolerate unhealthy targets you can set the threshold very low.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD




## `Amazon RDS`




**CPUUtilization**

**Dimensions:** DBInstanceIdentifier


**Alarm description:** This alarm helps to monitor consistent high CPU utilization. 
 CPU utilization measures non-idle time. Consider using 
 [Enhanced Monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.Enabling.html "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.Enabling.html") or 
 [Performance Insights](https://aws.amazon.com/rds/performance-insights/ "https://aws.amazon.com/rds/performance-insights/") to review which 
 [wait time](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring-Available-OS-Metrics.html "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring-Available-OS-Metrics.html") is 
 consuming the most of the CPU time (`guest`, `irq`, `wait`, `nice`, and so on) for 
 MariaDB, MySQL, Oracle, and PostgreSQL. Then evaluate which queries consume the highest 
 amount of CPU. If you can't tune your workload, consider moving to a larger DB instance class.


**Intent:** This alarm is used to detect consistent high CPU utilization in order to 
 prevent very high response time and time-outs. If you want to check micro-bursting of CPU utilization you can set a 
 lower alarm evaluation time.


**Statistic:** Average


**Recommended threshold:** 90.0


**Threshold justification:** Random spikes in CPU consumption 
 might not hamper database performance, but sustained high CPU can hinder upcoming database requests. Depending 
 on the overall database workload, high CPU at your RDS/Aurora instance can degrade the overall performance.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**DatabaseConnections**

**Dimensions:** DBInstanceIdentifier


**Alarm description:** This alarm detects a high number of connections. 
 Review existing connections and terminate any that are in `sleep` state or that are improperly closed. 
 Consider using connection pooling to limit the number of new connections. Alternatively, increase the DB 
 instance size to use a class with more memory and hence a higher default value for `max\_connections` or 
 increase the `max\_connections` value in [RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Limits.html "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Limits.html") and 
 Aurora [MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Managing.Performance.html "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Managing.Performance.html") and
 [PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Managing.html "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Managing.html") for the current 
 class if it can support your workload.


**Intent:** This alarm is used to help prevent rejected connections when the maximum 
 number of DB connections is reached. This alarm is not recommended if you frequently change DB instance class, because 
 doing so changes the memory and default maximum number of connections.


**Statistic:** Average


**Recommended threshold:** Depends on your situation


**Threshold justification:** The number of connections allowed depends on the size of 
 your DB instance class and database engine-specific parameters related to processes/connections. You should calculate a 
 value between 90-95% of the maximum number of connections for your database and use that result as the threshold value.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**EBSByteBalance%**

**Dimensions:** DBInstanceIdentifier


**Alarm description:** This alarm helps to monitor a low percentage of throughput credits remaining. 
 For troubleshooting, check [latency problems in RDS](https://repost.aws/knowledge-center/rds-latency-ebs-iops-bottleneck "https://repost.aws/knowledge-center/rds-latency-ebs-iops-bottleneck").


**Intent:** This alarm is used to detect a low percentage of throughput credits remaining in the burst bucket. Low byte balance percentage can cause throughput bottleneck issues. This alarm is not recommended for Aurora PostgreSQL instances.


**Statistic:** Average


**Recommended threshold:** 10.0


**Threshold justification:** A throughput credit balance below 10% is considered to be 
 poor and you should set the threshold accordingly. You can also set a lower threshold if your application can tolerate 
 a lower throughput for the workload.


**Period:** 60


**Datapoints to alarm:** 3


**Evaluation periods:** 3


**Comparison Operator:** LESS\_THAN\_THRESHOLD



**EBSIOBalance%**

**Dimensions:** DBInstanceIdentifier


**Alarm description:** This alarm helps to monitor low percentage of IOPS credits remaining. For 
 troubleshooting, see [latency problems in RDS](https://repost.aws/knowledge-center/rds-latency-ebs-iops-bottleneck "https://repost.aws/knowledge-center/rds-latency-ebs-iops-bottleneck").


**Intent:** This alarm is used to detect a low percentage of I/O credits remaining in the burst bucket. Low IOPS balance percentage can cause IOPS bottleneck issues. This alarm is not recommended for Aurora instances.


**Statistic:** Average


**Recommended threshold:** 10.0


**Threshold justification:** An IOPS credits balance below 10% is considered to be poor and 
 you can set the threshold accordingly. You can also set a lower threshold, if your application can tolerate a lower IOPS for the workload.


**Period:** 60


**Datapoints to alarm:** 3


**Evaluation periods:** 3


**Comparison Operator:** LESS\_THAN\_THRESHOLD



**FreeableMemory**

**Dimensions:** DBInstanceIdentifier


**Alarm description:** This alarm helps to monitor low freeable memory which can mean that there is a spike in 
 database connections or that your instance may be under high memory pressure. Check for memory pressure by monitoring the CloudWatch metrics 
 for `SwapUsage``in addition to `FreeableMemory`. If the instance memory consumption is frequently too high, 
 this indicates that you should check your workload or upgrade your instance class. For Aurora reader DB instance, consider 
 adding additional reader DB instances to the cluster. For information about troubleshooting Aurora, see 
 [freeable memory 
 issues](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_Troubleshooting.html#Troubleshooting.FreeableMemory "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_Troubleshooting.html#Troubleshooting.FreeableMemory").


**Intent:** This alarm is used to help prevent running out of memory which can result in 
 rejected connections.


**Statistic:** Average


**Recommended threshold:** Depends on your situation


**Threshold justification:** Depending on the workload and instance class, different values 
 for the threshold can be appropriate. Ideally, available memory should not go below 25% of total memory for prolonged periods. For 
 Aurora, you can set the threshold close to 5%, because the metric approaching 0 means that the DB instance has scaled up as much as it can. 
 You can analyze the historical behavior of this metric to determine sensible threshold levels.


**Period:** 60


**Datapoints to alarm:** 15


**Evaluation periods:** 15


**Comparison Operator:** LESS\_THAN\_THRESHOLD



**FreeLocalStorage**

**Dimensions:** DBInstanceIdentifier


**Alarm description:** This alarm helps to monitor low free local storage. Aurora PostgreSQL-Compatible Edition uses 
 local storage for storing error logs and temporary files. Aurora MySQL uses local storage for storing error logs, general logs, 
 slow query logs, audit logs, and non-InnoDB temporary tables. These local storage volumes are backed by Amazon EBS Store 
 and can be extended by using a larger DB instance class. For troubleshooting, check 
 Aurora [PostgreSQL-Compatible](https://repost.aws/knowledge-center/postgresql-aurora-storage-issue "https://repost.aws/knowledge-center/postgresql-aurora-storage-issue") and 
 [MySQL-Compatible](https://repost.aws/knowledge-center/aurora-mysql-local-storage "https://repost.aws/knowledge-center/aurora-mysql-local-storage").


**Intent:** This alarm is used to detect how close the Aurora DB instance is to reaching the 
 local storage limit, if you do not use Aurora Serverless v2 or higher. Local storage can reach capacity when you store 
 non-persistent data, such as temporary table and log files, in the local storage. This alarm can prevent an 
 out-of-space error that occurs when your DB instance runs out of local storage.


**Statistic:** Average


**Recommended threshold:** Depends on your situation


**Threshold justification:** You should calculate about 10%-20% of the amount of storage 
 available based on velocity and trend of volume usage, and then use that result as the threshold value to proactively take 
 action before the volume reaches its limit.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** LESS\_THAN\_THRESHOLD



**FreeStorageSpace**

**Dimensions:** DBInstanceIdentifier


**Alarm description:** This alarm watches for a low amount of available storage space. Consider 
 scaling up your database storage if you frequently approach storage capacity limits. Include some buffer to accommodate unforeseen 
 increases in demand from your applications. Alternatively, consider enabling RDS storage auto scaling. Additionally, consider 
 freeing up more space by deleting unused or outdated data and logs. For further information, check 
 [RDS run out of storage document](https://repost.aws/knowledge-center/rds-out-of-storage "https://repost.aws/knowledge-center/rds-out-of-storage") and 
 [PostgreSQL storage issues document](https://repost.aws/knowledge-center/diskfull-error-rds-postgresql "https://repost.aws/knowledge-center/diskfull-error-rds-postgresql").


**Intent:** This alarm helps prevent storage full issues. This can prevent downtime that occurs when your database instance runs out of storage. We do not recommend using this alarm if you have storage auto scaling enabled, or if you frequently change the storage capacity of the database instance.


**Statistic:** Minimum


**Recommended threshold:** Depends on your situation


**Threshold justification:** The threshold value will depend on the currently allocated storage 
 space. Typically, you should calculate the value of 10 percent of the allocated storage space and use that result as the threshold value.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** LESS\_THAN\_THRESHOLD



**MaximumUsedTransactionIDs**

**Dimensions:** DBInstanceIdentifier


**Alarm description:** This alarm helps prevent transaction ID wraparound for PostgreSQL. Refer to the 
 troubleshooting steps in 
[this 
 blog](https://aws.amazon.com/blogs/database/implement-an-early-warning-system-for-transaction-id-wraparound-in-amazon-rds-for-postgresql/ "https://aws.amazon.com/blogs/database/implement-an-early-warning-system-for-transaction-id-wraparound-in-amazon-rds-for-postgresql/") to investigate and resolve the issue. You can also refer to 
 [this 
 blog](https://aws.amazon.com/blogs/database/understanding-autovacuum-in-amazon-rds-for-postgresql-environments/ "https://aws.amazon.com/blogs/database/understanding-autovacuum-in-amazon-rds-for-postgresql-environments/") to familiarize yourself further with autovacuum concepts, common issues and best practices.


**Intent:** This alarm is used to help prevent transaction ID wraparound for PostgreSQL.


**Statistic:** Average


**Recommended threshold:** 1.0E9


**Threshold justification:** Setting this threshold to 1 billion should give you time to investigate the 
 problem. The default autovacuum\_freeze\_max\_age value is 200 million. If the age of the oldest transaction is 1 billion, autovacuum is 
 having a problem keeping this threshold below the target of 200 million transaction IDs.


**Period:** 60


**Datapoints to alarm:** 1


**Evaluation periods:** 1


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**ReadLatency**

**Dimensions:** DBInstanceIdentifier


**Alarm description:** This alarm helps to monitor high read latency. If storage latency is high, it's 
 because the workload is exceeding resource limits. You can review I/O utilization relative to instance and allocated storage 
 configuration. Refer to [troubleshoot the 
 latency of Amazon EBS volumes caused by an IOPS bottleneck](https://repost.aws/knowledge-center/rds-latency-ebs-iops-bottleneck "https://repost.aws/knowledge-center/rds-latency-ebs-iops-bottleneck"). For Aurora, you can switch to an instance class 
 that has [I/O-Optimized 
 storage configuration](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.Aurora_Fea_Regions_DB-eng.Feature.storage-type.html "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.Aurora_Fea_Regions_DB-eng.Feature.storage-type.html"). See 
 [Planning I/O in Aurora](https://aws.amazon.com/blogs/database/planning-i-o-in-amazon-aurora/ "https://aws.amazon.com/blogs/database/planning-i-o-in-amazon-aurora/") for guidance.


**Intent:** This alarm is used to detect high read latency. Database disks normally have a low 
 read/write latency, but they can have issues that can cause high latency operations.


**Statistic:** p90


**Recommended threshold:** Depends on your situation


**Threshold justification:** The recommended threshold value for this alarm is highly dependent on your 
 use case. Read latencies higher than 20 milliseconds are likely a cause for investigation. You can also set a higher threshold if your 
 application can have higher latency for read operations. Review the criticality and requirements of read latency and analyze 
 the historical behavior of this metric to determine sensible threshold levels.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**ReplicaLag**

**Dimensions:** DBInstanceIdentifier


**Alarm description:** This alarm helps you understand the number of seconds a replica is behind the 
 primary instance. A PostgreSQL Read Replica reports a replication lag of up to five minutes if there are no user transactions 
 occurring on the source database instance. When the ReplicaLag metric reaches 0, the replica has caught up to the primary DB instance. 
 If the ReplicaLag metric returns -1, then replication is currently not active. For guidance related to RDS PostgreSQL, 
 see [replication best 
 practices](https://aws.amazon.com/blogs/database/best-practices-for-amazon-rds-postgresql-replication/ "https://aws.amazon.com/blogs/database/best-practices-for-amazon-rds-postgresql-replication/") and for troubleshooting `ReplicaLag` and related errors, see 
 [troubleshooting ReplicaLag](https://repost.aws/knowledge-center/rds-postgresql-replication-lag "https://repost.aws/knowledge-center/rds-postgresql-replication-lag").


**Intent:** This alarm can detect the replica lag which reflects the data loss that could happen in case 
 of a failure of the primary instance. If the replica gets too far behind the primary and the primary fails, the replica will be missing 
 data that was in the primary instance.


**Statistic:** Maximum


**Recommended threshold:** 60.0


**Threshold justification:** Typically, the acceptable lag depends on the application. We recommend no 
 more than 60 seconds.


**Period:** 60


**Datapoints to alarm:** 10


**Evaluation periods:** 10


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**WriteLatency**

**Dimensions:** DBInstanceIdentifier


**Alarm description:** This alarm helps to monitor high write latency. If storage latency is high, it's 
 because the workload is exceeding resource limits. You can review I/O utilization relative to instance and allocated storage configuration. 
 Refer to [troubleshoot the 
 latency of Amazon EBS volumes caused by an IOPS bottleneck](https://repost.aws/knowledge-center/rds-latency-ebs-iops-bottleneck "https://repost.aws/knowledge-center/rds-latency-ebs-iops-bottleneck"). For Aurora, you can switch to an instance class that has 
 [I/O-Optimized 
 storage configuration](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.Aurora_Fea_Regions_DB-eng.Feature.storage-type.html "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.Aurora_Fea_Regions_DB-eng.Feature.storage-type.html"). See [Planning I/O in 
 Aurora](https://aws.amazon.com/blogs/database/planning-i-o-in-amazon-aurora/ "https://aws.amazon.com/blogs/database/planning-i-o-in-amazon-aurora/") for guidance.


**Intent:** This alarm is used to detect high write latency. Although database disks typically 
 have low read/write latency, they may experience problems that cause high latency operations. Monitoring this will 
 assure you the disk latency is as low as expected.


**Statistic:** p90


**Recommended threshold:** Depends on your situation


**Threshold justification:** The recommended threshold value for this alarm is highly dependent 
 on your use case. Write latencies higher than 20 milliseconds are likely a cause for investigation. You can also set a higher 
 threshold if your application can have a higher latency for write operations. Review the criticality and requirements of write 
 latency and analyze the historical behavior of this metric to determine sensible threshold levels.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**DBLoad**

**Dimensions:** DBInstanceIdentifier


**Alarm description:** This alarm helps to monitor high DB load. If the number of processes exceed the 
 number of vCPUs, the processes start queuing. When the queuing increases, the performance is impacted. If the DB load is often above the 
 maximum vCPU, and the primary wait state is CPU, the CPU is overloaded. In this case, you can 
 monitor `CPUUtilization`, `DBLoadCPU` and queued tasks in Performance Insights/Enhanced Monitoring. 
 You might want to throttle connections to the instance, tune any SQL queries with a high CPU load, or consider a larger 
 instance class. High and consistent instances of any wait state indicate that there might be bottlenecks or resource 
 contention issues to resolve.


**Intent:** This alarm is used to detect a high DB load. High DB load can cause performance 
 issues in the DB instance. This alarm is not applicable to serverless DB instances.


**Statistic:** Average


**Recommended threshold:** Depends on your situation


**Threshold justification:** The maximum vCPU value is determined by the number of vCPU (virtual CPU) cores for your DB instance. Depending on the maximum vCPU, different values for the threshold can be appropriate. Ideally, DB load should not go above vCPU line.


**Period:** 60


**Datapoints to alarm:** 15


**Evaluation periods:** 15


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**AuroraVolumeBytesLeftTotal**

**Dimensions:** DBClusterIdentifier


**Alarm description:** This alarm helps to monitor low remaining total volume. When the total volume 
 left reaches the size limit, the cluster reports an out-of-space error. Aurora storage automatically scales with the data in 
 the cluster volume and expands up to 128 TiB or 64 TiB depending on the 
 [DB engine version](https://repost.aws/knowledge-center/aurora-version-number "https://repost.aws/knowledge-center/aurora-version-number"). Consider 
 reducing storage by dropping tables and databases that you no longer need. For more information, 
 check [storage scaling](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.Performance.html "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.Performance.html").


**Intent:** This alarm is used to detect how close the Aurora cluster is to the volume size limit. This 
 alarm can prevent an out-of-space error that occurs when your cluster runs out of space. This alarm is recommended only for Aurora MySQL.


**Statistic:** Average


**Recommended threshold:** Depends on your situation


**Threshold justification:** You should calculate 10%-20% of the actual size limit based on 
 velocity and trend of volume usage increase, and then use that result as the threshold value to proactively take action before 
 the volume reaches its limit.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** LESS\_THAN\_THRESHOLD



**AuroraBinlogReplicaLag**

**Dimensions:** DBClusterIdentifier, Role=WRITER


**Alarm description:** This alarm helps to monitor the error state of Aurora writer instance replication. 
 For more information, see [Replicating 
 Aurora MySQL DB clusters across AWS Regions](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Replication.CrossRegion.html "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Replication.CrossRegion.html"). For troubleshooting, see 
 [Aurora MySQL replication 
 issues](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_Troubleshooting.html#CHAP_Troubleshooting.MySQL "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_Troubleshooting.html#CHAP_Troubleshooting.MySQL").


**Intent:** This alarm is used to detect whether the writer instance is in an error state and 
 can’t replicate the source. This alarm is recommended only for Aurora MySQL.


**Statistic:** Average


**Recommended threshold:** -1.0


**Threshold justification:** We recommend that you use -1 as the threshold value because Aurora MySQL publishes 
 this value if the replica is in an error state.


**Period:** 60


**Datapoints to alarm:** 2


**Evaluation periods:** 2


**Comparison Operator:** LESS\_THAN\_OR\_EQUAL\_TO\_THRESHOLD



**BlockedTransactions**

**Dimensions:** DBInstanceIdentifier


**Alarm description:** This alarm helps to monitor a high blocked transaction count in an Aurora DB 
 instance. Blocked transactions can end in either a rollback or a commit. High concurrency, idles in transaction, or long 
 running transactions can lead to blocked transactions. For troubleshooting, see 
 [Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/ams-waits.row-lock-wait.html "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/ams-waits.row-lock-wait.html") documentation.


**Intent:** This alarm is used to detect a high count of blocked transactions in an Aurora DB 
 instance in order to prevent transaction rollbacks and performance degradation.


**Statistic:** Average


**Recommended threshold:** Depends on your situation


**Threshold justification:** You should calculate 5% of all transactions of your instance using the 
 `ActiveTransactions` metric and use that result as the threshold value. You can also review the criticality and 
 requirements of blocked transactions and analyze the historical behavior of this metric to determine sensible threshold levels.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**BufferCacheHitRatio**

**Dimensions:** DBInstanceIdentifier


**Alarm description:** This alarm helps you monitor a consistent low cache hit ratio of the Aurora cluster. A 
 low hit ratio indicates that your queries on this DB instance are frequently going to disk. For troubleshooting, investigate your 
 workload to see which queries are causing this behavior, and see the 
 [DB 
 instance RAM recommendations](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.BestPractices.html#Aurora.BestPractices.Performance.Sizing "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.BestPractices.html#Aurora.BestPractices.Performance.Sizing") document.


**Intent:** This alarm is used to detect consistent low cache hit ratio in order to prevent a 
 sustained performance decrease in the Aurora instance.


**Statistic:** Average


**Recommended threshold:** 80.0


**Threshold justification:** You can set the threshold for buffer cache hit ratio to 80%. 
 However, you can adjust this value based on your acceptable performance level and workload characteristics.


**Period:** 60


**Datapoints to alarm:** 10


**Evaluation periods:** 10


**Comparison Operator:** LESS\_THAN\_THRESHOLD



**EngineUptime**

**Dimensions:** DBClusterIdentifier, Role=WRITER


**Alarm description:** This alarm helps to monitor low downtime of the writer DB instance. The writer 
 DB instance can go down due to a reboot, maintenance, upgrade, or failover. When the uptime reaches 0 because of a failover in the 
 cluster, and the cluster has one or more Aurora Replicas, then an Aurora Replica is promoted to the primary writer instance during a 
 failure event. To increase the availability of your DB cluster, consider creating one or more Aurora Replicas in two or more different 
 Availability Zones. For more information check 
 [factors that influence Aurora downtime](https://repost.aws/knowledge-center/aurora-mysql-downtime-factors "https://repost.aws/knowledge-center/aurora-mysql-downtime-factors").


**Intent:** This alarm is used to detect whether the Aurora writer DB instance is in downtime. This 
 can prevent long-running failure in the writer instance that occurs because of a crash or failover.


**Statistic:** Average


**Recommended threshold:** 0.0


**Threshold justification:** A failure event results in a brief interruption, during which read and 
 write operations fail with an exception. However, service is typically restored in less than 60 seconds, and often less than 30 seconds.


**Period:** 60


**Datapoints to alarm:** 2


**Evaluation periods:** 2


**Comparison Operator:** LESS\_THAN\_OR\_EQUAL\_TO\_THRESHOLD



**RollbackSegmentHistoryListLength**

**Dimensions:** DBInstanceIdentifier


**Alarm description:** This alarm helps to monitor a consistent high rollback segment history length of 
 an Aurora instance. A high InnoDB history list length indicates that a large number of old row versions, queries and database 
 shutdowns have become slower. For more information and troubleshooting, see 
 [the InnoDB history list 
 length increased significantly](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/proactive-insights.history-list.html "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/proactive-insights.history-list.html") documentation.


**Intent:** This alarm is used to detect consistent high rollback segment history length. This 
 can help you prevent sustained performance degradation and high CPU usage in the Aurora instance. This alarm is recommended 
 only for Aurora MySQL.


**Statistic:** Average


**Recommended threshold:** 1000000.0


**Threshold justification:** Setting this threshold to 1 million should give you time to 
 investigate the problem. However, you can adjust this value based on your acceptable performance level and workload characteristics.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**StorageNetworkThroughput**

**Dimensions:** DBClusterIdentifier, Role=WRITER


**Alarm description:** This alarm helps to monitor high storage network throughput. If storage 
 network throughput passes the total network bandwidth of the 
 [EC2 instance](https://aws.amazon.com/ec2/instance-types/ "https://aws.amazon.com/ec2/instance-types/"), it can lead to high read and write latency, 
 which can cause degraded performance. You can check your EC2 instance type from AWS Console. For troubleshooting, check 
 any changes on write/read latencies and evaluate if you’ve also hit an alarm on this metric. If that is the case, 
 evaluate your workload pattern during the times that the alarm was triggered. This can help you identify if you can optimize y
 our workload to reduce the total amount of network traffic. If this is not possible, you might need to consider scaling your instance.


**Intent:** This alarm is used to detect high storage network throughput. Detecting high throughput 
 can prevent network packet drops and degraded performance.


**Statistic:** Average


**Recommended threshold:** Depends on your situation


**Threshold justification:** You should calculate about 80%-90% of the total network bandwidth of the 
 EC2 instance type, and then use that result as the threshold value to proactively take action before the network packets 
 are affected. You can also review the criticality and requirements of storage network throughput and analyze the historical 
 behavior of this metric to determine sensible threshold levels.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD




## `Amazon Route 53 Public Data Plane`




**HealthCheckStatus**

**Dimensions:** HealthCheckId


**Alarm description:** This alarm helps to detect unhealthy endpoints as per health checkers. To understand the reason for a failure that results in unhealthy status, use the Health Checkers tab in the Route 53 Health Check Console to view the status from each Region as well as the last failure of the health check. The status tab also displays the reason that the endpoint is reported as unhealthy. Refer to [troubleshooting steps](https://repost.aws/knowledge-center/route-53-fix-unhealthy-health-checks "https://repost.aws/knowledge-center/route-53-fix-unhealthy-health-checks").


**Intent:** This alarm uses Route53 health checkers to detect unhealthy endpoints.


**Statistic:** Average


**Recommended threshold:** 1.0


**Threshold justification:** The status of the endpoint is reported as 1 when it's healthy. Everything less than 1 is unhealthy.


**Period:** 60


**Datapoints to alarm:** 3


**Evaluation periods:** 3


**Comparison Operator:** LESS\_THAN\_THRESHOLD




## `Amazon S3`




**4xxErrors**

**Dimensions:** BucketName, FilterId


**Alarm description:** This alarm helps us report the total number of 4xx error status codes that are made in response to client requests. 403 error codes might indicate an incorrect IAM policy, and 404 error codes might indicate mis-behaving client application, for example. [Enabling S3 server access logging](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-server-access-logging.html "https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-server-access-logging.html") on a temporary basis will help you to pinpoint the issue's origin using the fields HTTP status and Error Code. To understand more about the error code, see [Error Responses](https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html "https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html").


**Intent:** This alarm is used to create a baseline for typical 4xx error rates so that you can look into any abnormalities that might indicate a setup issue.


**Statistic:** Average


**Recommended threshold:** 0.05


**Threshold justification:** The recommended threshold is to detect if more than 5% of total requests are getting 4XX errors. Frequently occurring 4XX errors should be alarmed. However, setting a very low value for the threshold can cause alarm to be too sensitive. You can also tune the threshold to suit to the load of the requests, accounting for an acceptable level of 4XX errors. You can also analyze historical data to find the acceptable error rate for the application workload, and then tune the threshold accordingly.


**Period:** 60


**Datapoints to alarm:** 15


**Evaluation periods:** 15


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**5xxErrors**

**Dimensions:** BucketName, FilterId


**Alarm description:** This alarm helps you detect a high number of server-side errors. These errors indicate that a client made a request that the server couldn’t complete. This can help you correlate the issue your application is facing because of S3. For more information to help you efficiently handle or reduce errors, see [Optimizing performance design patterns](https://docs.aws.amazon.com/AmazonS3/latest/userguide/optimizing-performance-design-patterns.html#optimizing-performance-timeouts-retries "https://docs.aws.amazon.com/AmazonS3/latest/userguide/optimizing-performance-design-patterns.html#optimizing-performance-timeouts-retries"). Errors might also be caused by an the issue with S3, check [AWS service health dashboard](https://health.aws.amazon.com/health/status "https://health.aws.amazon.com/health/status") for the status of Amazon S3 in your Region.


**Intent:** This alarm can help to detect if the application is experiencing issues due to 5xx errors.


**Statistic:** Average


**Recommended threshold:** 0.05


**Threshold justification:** We recommend setting the threshold to detect if more than 5% of total requests are getting 5XXError. However, you can tune the threshold to suit the traffic of the requests, as well as acceptable error rates. You can also analyze historical data to see what is the acceptable error rate for the application workload, and tune the threshold accordingly.


**Period:** 60


**Datapoints to alarm:** 15


**Evaluation periods:** 15


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**OperationsFailedReplication**

**Dimensions:** SourceBucket, DestinationBucket, RuleId


**Alarm description:** This alarm helps in understanding a replication failure. This metric tracks the status of new objects replicated using S3 CRR or S3 SRR, and also tracks existing objects replicated using S3 batch replication. See [Replication troubleshooting](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-troubleshoot.html "https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-troubleshoot.html") for more details.


**Intent:** This alarm is used to detect if there is a failed replication operation.


**Statistic:** Maximum


**Recommended threshold:** 0.0


**Threshold justification:** This metric emits a value of 0 for successful operations, and nothing when there are no replication operations carried out for the minute. When the metric emits a value greater than 0, the replication operation is unsuccessful.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD




## `S3ObjectLambda`




**4xxErrors**

**Dimensions:** AccessPointName, DataSourceARN


**Alarm description:** This alarm helps us report the total number of 4xx error status code that are made in response to client requests. [Enabling S3 server access logging](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-server-access-logging.html "https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-server-access-logging.html") on a temporary basis will help you to pinpoint the issue's origin using the fields HTTP status and Error Code.


**Intent:** This alarm is used to create a baseline for typical 4xx error rates so that you can look into any abnormalities that might indicate a setup issue.


**Statistic:** Average


**Recommended threshold:** 0.05


**Threshold justification:** We recommend setting the threshold to detect if more than 5% of total requests are getting 4XXError. Frequently occurring 4XX errors should be alarmed. However, setting a very low value for the threshold can cause alarm to be too sensitive. You can also tune the threshold to suit to the load of the requests, accounting for an acceptable level of 4XX errors. You can also analyze historical data to find the acceptable error rate for the application workload, and then tune the threshold accordingly.


**Period:** 60


**Datapoints to alarm:** 15


**Evaluation periods:** 15


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**5xxErrors**

**Dimensions:** AccessPointName, DataSourceARN


**Alarm description:** This alarm helps to detect high number of server-side errors. These errors indicate that a client made a request that the server couldn’t complete. These errors might be caused by an issue with S3, check [AWS service health dashboard](https://health.aws.amazon.com/health/status "https://health.aws.amazon.com/health/status") for the status of Amazon S3 in your Region. This can help you correlate the issue your application is facing because of S3. For information to help you efficiently handle or reduce these errors, see [Optimizing performance design patterns](https://docs.aws.amazon.com/AmazonS3/latest/userguide/optimizing-performance-design-patterns.html#optimizing-performance-timeouts-retries "https://docs.aws.amazon.com/AmazonS3/latest/userguide/optimizing-performance-design-patterns.html#optimizing-performance-timeouts-retries").


**Intent:** This alarm can help to detect if the application is experiencing issues due to 5xx errors.


**Statistic:** Average


**Recommended threshold:** 0.05


**Threshold justification:** We recommend setting the threshold to detect if more than 5% of total requests are getting 5XX errors. However, you can tune the threshold to suit the traffic of the requests, as well as acceptable error rates. You can also analyze historical data to see what is the acceptable error rate for the application workload, and tune the threshold accordingly.


**Period:** 60


**Datapoints to alarm:** 15


**Evaluation periods:** 15


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**LambdaResponse4xx**

**Dimensions:** AccessPointName, DataSourceARN


**Alarm description:** This alarm helps you detect and diagnose failures (500s) in calls to S3 Object Lambda. These errors can be caused by errors or misconfigurations in the Lambda function responsible for responding to your requests. Investigating the CloudWatch Log Streams of the Lambda function associated with the Object Lambda Access Point can help you pinpoint the issue's origin based on the response from S3 Object Lambda.


**Intent:** This alarm is used to detect 4xx client errors for WriteGetObjectResponse calls.


**Statistic:** Average


**Recommended threshold:** 0.05


**Threshold justification:** We recommend setting the threshold to detect if more than 5% of total requests are getting 4XXError. Frequently occurring 4XX errors should be alarmed. However, setting a very low value for the threshold can cause alarm to be too sensitive. You can also tune the threshold to suit to the load of the requests, accounting for an acceptable level of 4XX errors. You can also analyze historical data to find the acceptable error rate for the application workload, and then tune the threshold accordingly.


**Period:** 60


**Datapoints to alarm:** 15


**Evaluation periods:** 15


**Comparison Operator:** GREATER\_THAN\_THRESHOLD




## Amazon SNS




**NumberOfMessagesPublished**

**Dimensions:** TopicName


**Alarm description:** This alarm can detect when the number of SNS messages published is too low. For troubleshooting, check why the publishers are sending less traffic.


**Intent:** This alarm helps you proactively monitor and detect significant drops in notification publishing. This helps you identify potential issues with your application or business processes, so that you can take appropriate actions to maintain the expected flow of notifications. You should create this alarm if you expect your system to have a minimum traffic that it is serving.


**Statistic:** Sum


**Recommended threshold:** Depends on your situation


**Threshold justification:** The number of messages published should be in line with the expected number of published messages for your application. You can also analyze the historical data, trends and traffic to find the right threshold.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** LESS\_THAN\_THRESHOLD



**NumberOfNotificationsDelivered**

**Dimensions:** TopicName


**Alarm description:** This alarm can detect when the number of SNS messages delivered is too low. This could be because of unintentional unsubscribing of an endpoint, or because of an SNS event that causes messages to experience delay.


**Intent:** This alarm helps you detect a drop in the volume of messages delivered. You should create this alarm if you expect your system to have a minimum traffic that it is serving.


**Statistic:** Sum


**Recommended threshold:** Depends on your situation


**Threshold justification:** The number of messages delivered should be in line with the expected number of messages produced and the number of consumers. You can also analyze the historical data, trends and traffic to find the right threshold.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** LESS\_THAN\_THRESHOLD



**NumberOfNotificationsFailed**

**Dimensions:** TopicName


**Alarm description:** This alarm can detect when the number of failed SNS messages is too high. To troubleshoot failed notifications, enable logging to CloudWatch Logs. Checking the logs can help you find which subscribers are failing, as well as the status codes they are returning.


**Intent:** This alarm helps you proactively find issues with the delivery of notifications and take appropriate actions to address them.


**Statistic:** Sum


**Recommended threshold:** Depends on your situation


**Threshold justification:** The recommended threshold value for this alarm is highly dependent on the impact of failed notifications. Review the SLAs provided to your end users, fault tolerance and criticality of notifications and analyze historical data, and then select a threshold accordingly. The number of notifications failed should be 0 for topics that have only SQS, Lambda or Firehose subscriptions.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**NumberOfNotificationsFilteredOut-InvalidAttributes**

**Dimensions:** TopicName


**Alarm description:** This alarm helps to monitor and resolve potential problems with the publisher or subscribers. Check if a publisher is publishing messages with invalid attributes or if an inappropriate filter is applied to a subscriber. You can also analyze CloudWatch Logs to help find the root cause of the issue.


**Intent:** The alarm is used to detect if the published messages are not valid or if inappropriate filters have been applied to a subscriber.


**Statistic:** Sum


**Recommended threshold:** 0.0


**Threshold justification:** Invalid attributes are almost always a mistake by the publisher. We recommend to set the threshold to 0 because invalid attributes are not expected in a healthy system.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**NumberOfNotificationsFilteredOut-InvalidMessageBody**

**Dimensions:** TopicName


**Alarm description:** This alarm helps to monitor and resolve potential problems with the publisher or subscribers. Check if a publisher is publishing messages with invalid message bodies, or if an inappropriate filter is applied to a subscriber. You can also analyze CloudWatch Logs to help find the root cause of the issue.


**Intent:** The alarm is used to detect if the published messages are not valid or if inappropriate filters have been applied to a subscriber.


**Statistic:** Sum


**Recommended threshold:** 0.0


**Threshold justification:** Invalid message bodies are almost always a mistake by the publisher. We recommend to set the threshold to 0 because invalid message bodies are not expected in a healthy system.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**NumberOfNotificationsRedrivenToDlq**

**Dimensions:** TopicName


**Alarm description:** This alarm helps to monitor the number of messages that are moved to a dead-letter queue.


**Intent:** The alarm is used to detect messages that moved to a dead-letter queue. We recommend that you create this alarm when SNS is coupled with SQS, Lambda or Firehose.


**Statistic:** Sum


**Recommended threshold:** 0.0


**Threshold justification:** In a healthy system of any subscriber type, messages should not be moved to the dead-letter queue. We recommend that you be notified if any messages land in the queue, so that you can identify and address the root cause, and potentially redrive the messages in the dead-letter queue to prevent data loss.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**NumberOfNotificationsFailedToRedriveToDlq**

**Dimensions:** TopicName


**Alarm description:** This alarm helps to monitor messages that couldn't be moved to a dead-letter queue. Check whether your dead-letter queue exists and that it's configured correctly. Also, verify that SNS has permissions to access the dead-letter queue. Refer to the [dead-letter queue documentation](https://docs.aws.amazon.com/sns/latest/dg/sns-dead-letter-queues.html "https://docs.aws.amazon.com/sns/latest/dg/sns-dead-letter-queues.html") to learn more.


**Intent:** The alarm is used to detect messages that couldn't be moved to a dead-letter queue.


**Statistic:** Sum


**Recommended threshold:** 0.0


**Threshold justification:** It's almost always a mistake if messages can't be moved to the dead-letter queue. The recommendation for the threshold is 0, meaning all messages that fail processing must be able to reach the dead-letter queue when the queue has been configured.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**SMSMonthToDateSpentUSD**

**Dimensions:** TopicName


**Alarm description:** The alarm helps to monitor if you have a sufficient quota in your account for SNS to be able to deliver messages. If you reach your quota, SNS won't be able to deliver SMS messages. For information about setting your monthly SMS spend quota, or for information about requesting a spend quota increase with AWS, see [Setting SMS messaging preferences](https://docs.aws.amazon.com/sns/latest/dg/sms_preferences.html "https://docs.aws.amazon.com/sns/latest/dg/sms_preferences.html").


**Intent:** This alarm is used to detect if you have a sufficient quota in your account for your SMS messages to be delivered successfully.


**Statistic:** Maximum


**Recommended threshold:** Depends on your situation


**Threshold justification:** Set the threshold in accordance with the quota (Account spend limit) for the account. Choose a threshold which informs you early enough that you are reaching your quota limit so that you have time to request an increase.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD



**SMSSuccessRate**

**Dimensions:** TopicName


**Alarm description:** This alarm helps to monitor the rate of failing SMS message deliveries. You can set up [Cloudwatch Logs](https://docs.aws.amazon.com/sns/latest/dg/sms_stats_cloudwatch.html "https://docs.aws.amazon.com/sns/latest/dg/sms_stats_cloudwatch.html") to understand the nature of the failure and take action based on that.


**Intent:** This alarm is used to detect failing SMS message deliveries.


**Statistic:** Average


**Recommended threshold:** Depends on your situation


**Threshold justification:** Set the threshold for the alarm in line with your tolerance for failing SMS message deliveries.


**Period:** 60


**Datapoints to alarm:** 5


**Evaluation periods:** 5


**Comparison Operator:** GREATER\_THAN\_THRESHOLD




## Amazon SQS




**ApproximateAgeOfOldestMessage**

**Dimensions:** QueueName


**Alarm description:** This alarm watches the age of the oldest message 
 in the queue. You can use this alarm to monitor if your consumers are processing SQS messages at the 
 desired speed. Consider increasing the consumer count or consumer throughput to reduce message age. 
 This metric can be used in combination with `ApproximateNumberOfMessagesVisible` to determine how big the queue backlog is and how quickly messages are being processed. To prevent messages from being deleted before processed, consider configuring the dead-letter queue to sideline potential poison pill messages.


**Intent:** This alarm is used to detect whether the age of the oldest message in the QueueName queue is too high. High age can be an indication that messages are not processed quickly enough or that there are some poison-pill messages that are stuck in the queue and can't be processed. 


**Statistic:** Maximum


**Recommended threshold:** Depends on your situation


**Threshold justification:** The recommended threshold value for this alarm is highly dependent on the expected message processing time. You can use historical data to calculate the average message processing time, and then set the threshold to 50% higher than the maximum expected SQS message processing time by queue consumers.


**Period:** 60


**Datapoints to alarm:** 15


**Evaluation periods:** 15


**Comparison Operator:** GREATER\_THAN\_OR\_EQUAL\_TO\_THRESHOLD



**ApproximateNumberOfMessagesNotVisible**

**Dimensions:** QueueName


**Alarm description:** This alarm helps to detect a high number of in-flight
 messages with respect to `QueueName`. For troubleshooting, check 
 [message backlog decreasing](https://repost.aws/knowledge-center/sqs-message-backlog "https://repost.aws/knowledge-center/sqs-message-backlog").


**Intent:** This alarm is used to detect a high number of in-flight messages in the queue. If consumers do not delete messages within the visibility timeout period, when the queue is polled, messages reappear in the queue. For FIFO queues, there can be a maximum of 20,000 in-flight messages. If you reach this quota, SQS returns no error messages. A FIFO queue looks through the first 20k messages to determine available message groups. This means that if you have a backlog of messages in a single message group, you cannot consume messages from other message groups that were sent to the queue at a later time until you successfully consume the messages from the backlog.


**Statistic:** Average


**Recommended threshold:** Depends on your situation


**Threshold justification:** The recommended threshold value for this alarm is highly dependent on the expected number of messages in flight. You can use historical data to calculate the maximum expected number of messages in flight and set the threshold to 50% over this value. If consumers of the queue are processing but not deleting messages from the queue, this number will suddenly increase.


**Period:** 60


**Datapoints to alarm:** 15


**Evaluation periods:** 15


**Comparison Operator:** GREATER\_THAN\_OR\_EQUAL\_TO\_THRESHOLD



**ApproximateNumberOfMessagesVisible**

**Dimensions:** QueueName


**Alarm description:** This alarm watches for the message queue backlog to be bigger than expected, indicating that consumers are too slow or there are not enough consumers. Consider increasing the consumer count or speeding up consumers, if this alarm goes into ALARM state.


**Intent:** This alarm is used to detect whether the message count of the active queue is too high and consumers are slow to process the messages or there are not enough consumers to process them.


**Statistic:** Average


**Recommended threshold:** Depends on your situation


**Threshold justification:** An unexpectedly high number of messages visible indicates that messages are not being processed by a consumer at the expected rate. You should consider historical data when you set this threshold.


**Period:** 60


**Datapoints to alarm:** 15


**Evaluation periods:** 15


**Comparison Operator:** GREATER\_THAN\_OR\_EQUAL\_TO\_THRESHOLD



**NumberOfMessagesSent**

**Dimensions:** QueueName


**Alarm description:** This alarm helps to detect if there are no messages being 
 sent from a producer with respect to `QueueName`. For troubleshooting, check the reason that the 
 producer is not sending messages.


**Intent:** This alarm is used to detect when a producer stops sending messages.


**Statistic:** Sum


**Recommended threshold:** 0.0


**Threshold justification:** If the number of messages sent is 0, the producer is not sending any messages. If this queue has a low TPS, increase the number of EvaluationPeriods accordingly. 


**Period:** 60


**Datapoints to alarm:** 15


**Evaluation periods:** 15


**Comparison Operator:** LESS\_THAN\_OR\_EQUAL\_TO\_THRESHOLD




## AWS VPN




**TunnelState**

**Dimensions:** VpnId


**Alarm description:** This alarm helps you understand if the state of one or more tunnels is DOWN. For troubleshooting, see [VPN tunnel troubleshooting](https://repost.aws/knowledge-center/vpn-tunnel-troubleshooting "https://repost.aws/knowledge-center/vpn-tunnel-troubleshooting").


**Intent:** This alarm is used to detect if at least one tunnel is in the DOWN state for this VPN, so that you can troubleshoot the impacted VPN. This alarm will always be in the ALARM state for networks that only have a single tunnel configured.


**Statistic:** Minimum


**Recommended threshold:** 1.0


**Threshold justification:** A value less than 1 indicates that at least one tunnel is in DOWN state.


**Period:** 300


**Datapoints to alarm:** 3


**Evaluation periods:** 3


**Comparison Operator:** LESS\_THAN\_THRESHOLD



**TunnelState**

**Dimensions:** TunnelIpAddress


**Alarm description:** This alarm helps you understand if the state of this tunnel is DOWN. For troubleshooting, see [VPN tunnel troubleshooting](https://repost.aws/knowledge-center/vpn-tunnel-troubleshooting "https://repost.aws/knowledge-center/vpn-tunnel-troubleshooting").


**Intent:** This alarm is used to detect if the tunnel is in the DOWN state, so that you can troubleshoot the impacted VPN. This alarm will always be in the ALARM state for networks that only have a single tunnel configured.


**Statistic:** Minimum


**Recommended threshold:** 1.0


**Threshold justification:** A value less than 1 indicates that the tunnel is in DOWN state.


**Period:** 300


**Datapoints to alarm:** 3


**Evaluation periods:** 3


**Comparison Operator:** LESS\_THAN\_THRESHOLD
