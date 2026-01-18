# Monitoring AWS Systems Manager for SAP events using EventBridge

###### Topics

- [Monitor events using EventBridge](#monitoring-events-in-eventbridge "#monitoring-events-in-eventbridge")
- [Example](#example "#example")

## Monitor events using EventBridge

You can track the following AWS Systems Manager for SAP-related events in EventBridge.

| Event type                         | Status                           | Event details                                                                     |
| ---------------------------------- | -------------------------------- | --------------------------------------------------------------------------------- |
| SSM for SAP Operation State Change | `InProgress`, `Success`, `Error` | operationId, type, applicationId, resourceId, resourceType, status, statusMessage |

Use these sample JSON payloads if you would like to use these events programmatically.

| Event state                       | JSON payload                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SSM for SAP Operation: InProgress | `<br>{<br>"version": "0",<br>"id": "6b41eac1-3685-c064-12a3-f16b57f30114",<br>"detail-type": "SSM for SAP Operation State Change",<br>"source": "aws.ssm-sap",<br>"account": "112233445566",<br>"time": "2023-01-25T08:04:33Z",<br>"region": "us-east-1",<br>"resources": [],<br>"detail": {<br>"operationId": "dbfd5c7d-0f5a-4ad3-87bf-d04b65eba21e",<br>"type": "REGISTER_APPLICATION",<br>"applicationId": "HANA_TEST",<br>"resourceId": "HDB",<br>"resourceType": "APPLICATION",<br>"status": "InProgress",<br>"statusMessage": null<br>}<br>}<br>` |
| SSM for SAP Operation: Success    | `<br>{<br>"version": "0",<br>"id": "05595cb1-ceac-1fb0-9040-045ca7865146",<br>"detail-type": "SSM for SAP Operation State Change",<br>"source": "aws.ssm-sap",<br>"account": "112233445566",<br>"time": "2023-01-26T04:45:43Z",<br>"region": "us-east-1",<br>"resources": [],<br>"detail": {<br>"operationId": "e5de5599-3b1e-4892-9201-835e71c6090a",<br>"type": "REGISTER_APPLICATION",<br>"applicationId": "HANA_TEST",<br>"resourceId": "HDB",<br>"resourceType": "APPLICATION",<br>"status": "Success",<br>"statusMessage": null<br>}<br>}<br>`    |
| SSM for SAP Operation: Error      | `<br>{<br>"version": "0",<br>"id": "fb715f90-e80c-1c7f-f179-e6646f4b97d9",<br>"detail-type": "SSM for SAP Operation State Change",<br>"source": "aws.ssm-sap",<br>"account": "112233445566",<br>"time": "2023-01-26T04:46:34Z",<br>"region": "us-east-1",<br>"resources": [],<br>"detail": {<br>"operationId": "77c8f0e6-6987-4e2b-9517-c5a44388992a",<br>"type": "UPDATE_CREDENTIALS",<br>"applicationId": "HANA",<br>"resourceId": "HDB",<br>"resourceType": "APPLICATION",<br>"status": "Error",<br>"statusMessage": null<br>}<br>}<br>`             |

## Example

The following is an event pattern example of Operation State Change event from AWS Systems Manager for SAP using the `RegisterApplication` API.

```
 {
  "source": ["aws.ssm-sap"],
  "detail-type": ["SSM for SAP Operation State Change"],
  "detail": {
    "type": ["REGISTER_APPLICATION"]
  }
}
```
