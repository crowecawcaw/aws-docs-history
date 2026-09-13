

# Create a log delivery for REST API execution logs
<a name="rest-api-create-log-delivery"></a>

You can route execution logs to your own CloudWatch Logs log groups, Amazon S3 buckets, or Firehose streams. To do this, create a Amazon CloudWatch Logs delivery. This involves three steps: creating a delivery source, creating a delivery destination, and linking them with a delivery.

## Prerequisites
<a name="rest-api-create-log-delivery-prereqs"></a>

Before you create a log delivery, make sure you have the following:
+ Execution logging enabled on your REST API stage. Set `loggingLevel` to `ERROR` or `INFO`. If logging is not enabled, the delivery source creation fails.
+ A destination resource: a CloudWatch Logs log group, Amazon S3 bucket, or Firehose stream that you own.
+ Permissions to call Amazon CloudWatch Logs delivery APIs. For more information, see [Enable logging from AWS services](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html) in the *Amazon CloudWatch Logs User Guide*.

## API Gateway-specific values for Amazon CloudWatch Logs delivery
<a name="rest-api-create-log-delivery-values"></a>

When you create a delivery for API Gateway execution logs, use the following values:

Resource ARN  
`arn:aws:apigateway:{{{region}}}:{{{account-id}}}:/restapis/{{{rest-api-id}}}/stages/{{{stage-name}}}`

Log type  
`EXECUTION_LOGS`

## Create a log delivery (AWS CLI)
<a name="rest-api-create-log-delivery-cli"></a>

The following example creates a delivery that sends execution logs from a REST API to a CloudWatch Logs log group that you own.

1. 

**Create the delivery source**

   Register your REST API as a delivery source.

   ```
   aws logs put-delivery-source \
       --name {{my-apigw-source}} \
       --log-type EXECUTION_LOGS \
       --resource-arn arn:aws:apigateway:{{{region}}}:{{{account-id}}}:/restapis/{{{rest-api-id}}}/stages/{{{stage-name}}}
   ```

1. 

**Create the delivery destination**

   Register your log group as a delivery destination.

   ```
   aws logs put-delivery-destination \
       --name {{my-log-destination}} \
       --delivery-destination-configuration "destinationResourceArn=arn:aws:logs:{{{region}}}:{{{account-id}}}:log-group:{{{log-group-name}}}"
   ```

1. 

**Create the delivery**

   Link the source to the destination.

   ```
   aws logs create-delivery \
       --delivery-source-name {{my-apigw-source}} \
       --delivery-destination-arn arn:aws:logs:{{{region}}}:{{{account-id}}}:delivery-destination:{{my-log-destination}}
   ```

To send logs to Amazon S3 or Firehose, specify the appropriate resource ARN in the `put-delivery-destination` command. For more information about the complete Amazon CloudWatch Logs delivery workflow, see [Enable logging from AWS services](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html) in the *Amazon CloudWatch Logs User Guide*.

To send logs to multiple destinations, create additional deliveries using the same delivery source with different destinations.

## Record fields
<a name="rest-api-create-log-delivery-record-fields"></a>

With Amazon CloudWatch Logs delivery, execution logs include structured fields that you can customize per destination. The following fields are available:
+ `resource_arn` – The ARN of the API stage
+ `event_timestamp` – The time of the log event
+ `api_id` – The REST API identifier
+ `stage` – The stage name
+ `resource_path` – The resource path of the request
+ `http_method` – The HTTP method
+ `payload` – The execution log content (same as standard execution logs)

You can select which fields to include and the output format for each destination using the `--record-fields` parameter on `create-delivery` and the `--output-format` parameter on `put-delivery-destination`.

Available output formats depend on the destination:
+ **CloudWatch Logs** – json, plain
+ **Amazon S3** – json, plain, w3c, parquet
+ **Firehose** – json, plain

**Match standard execution log output**  
If you want delivery output that matches standard execution logging (payload only, no additional fields), add `--output-format "plain"` to `put-delivery-destination` and `--record-fields "payload" --field-delimiter ""` to `create-delivery`.

## Create a log delivery (CloudFormation)
<a name="rest-api-create-log-delivery-cfn"></a>

When assembling the stage ARN for CloudFormation templates, use the following pattern:

```
  DeliverySource:
    Type: AWS::Logs::DeliverySource
    Properties:
      Name: my-apigw-source
      LogType: EXECUTION_LOGS
      ResourceArn: !Sub "arn:${AWS::Partition}:apigateway:${AWS::Region}:${AWS::AccountId}:/restapis/${MyApi}/stages/${MyStageName}"
```

## Create a log delivery (API Gateway console)
<a name="rest-api-create-log-delivery-console"></a>

You can create a log delivery from the **Logs and tracing** section of your stage details page.

1. Sign in to the API Gateway console at [https://console.aws.amazon.com/apigateway](https://console.aws.amazon.com/apigateway).

1. Choose your REST API, and then choose **Stages**.

1. Choose a stage.

1. In the **Logs and tracing** section, under **Log delivery destinations**, choose **Add destination**.

1. Choose a destination type (CloudWatch Logs, Amazon S3, or Firehose) and specify the destination resource.

1. Choose **Save**.

**Important**  
You must enable execution logging on the stage before you can add delivery destinations. If logging is set to **Off**, the delivery configuration does not generate logs.

**Note**  
To configure cross-account delivery destinations, use the AWS CLI. You must create a delivery destination policy in the destination account before creating the delivery in the source account. For more information, see [Cross-account delivery example](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/vended-logs-crossaccount-example.html) in the *Amazon CloudWatch Logs User Guide*.