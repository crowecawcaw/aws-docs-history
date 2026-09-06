

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Manage Cloud Connectors
<a name="cloud-connector-manage"></a>

Use the following AWS CLI commands to manage your Cloud Connectors.

**List all Cloud Connectors**  


```
aws ssm list-cloud-connectors \
    --region {{us-east-1}}
```

**Update a Cloud Connector**  
You can update the display name or subscription targets of an existing Cloud Connector.

```
aws ssm update-cloud-connector \
    --cloud-connector-id {{CLOUD_CONNECTOR_ID}} \
    --display-name "{{UpdatedName}}" \
    --region {{us-east-1}}
```

**Delete a Cloud Connector**  
Deleting the last Cloud Connector in an AWS account also deletes the associated AWS Config service-linked recorder.

```
aws ssm delete-cloud-connector \
    --cloud-connector-id {{CLOUD_CONNECTOR_ID}} \
    --region {{us-east-1}}
```