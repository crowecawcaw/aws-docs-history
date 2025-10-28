# AWS IoT Events in AWS GovCloud (US)

AWS IoT Events enables you to monitor your equipment or device fleets for failures or changes in
operation, and to trigger actions when such events occur. AWS IoT Events continuously
watches IoT sensor data from devices, processes, applications, and other AWS services to
identify significant events so you can take action.

AWS IoT Events is only supported in the AWS GovCloud (US-West) Region.

## How AWS IoT Events differs for AWS GovCloud (US)

- SSO integration not supported.
- [Notification
  action](../../../iotevents/latest/apireference/API_NotificationAction.md "../../../iotevents/latest/apireference/API_NotificationAction.md") is not supported.

## Documentation for AWS IoT Events

[AWS IoT Events
documentation](../../../iotevents/index.md "../../../iotevents/index.md").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains
how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings.
The list can be used as a guide to help meet applicable customer compliance obligations.
Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Detector Model Name
- Alarm Model name
- Input Name
- Fields in run-time messages used as key-value in Detector Models or Alarm
  Models
- MessageId in BatchPutMessage calls
- SiteWise AssetId and PropertyId that are referenced in AlarmModel rules
