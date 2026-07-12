# Manage Cloud Connectors

Use the following AWS CLI commands to manage your Cloud Connectors.

###### List all Cloud Connectors

```
aws ssm list-cloud-connectors \
    --region `us-east-1`
```

###### Update a Cloud Connector

You can update the display name or subscription targets of an existing Cloud
Connector.

```
aws ssm update-cloud-connector \
    --cloud-connector-id `CLOUD_CONNECTOR_ID` \
    --display-name "`UpdatedName`" \
    --region `us-east-1`
```

###### Delete a Cloud Connector

Deleting the last Cloud Connector in an AWS account also deletes the
associated service-linked recorder.

```
aws ssm delete-cloud-connector \
    --cloud-connector-id `CLOUD_CONNECTOR_ID` \
    --region `us-east-1`
```
