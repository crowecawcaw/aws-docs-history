# AWS Health in AWS GovCloud (US)

AWS Health provides ongoing visibility into the state of your AWS resources, services, and accounts. The service gives you awareness and remediation guidance for resource performance or availability issues that affect your applications running on AWS. AWS Health provides relevant and timely information to help you manage events in progress. AWS Health also helps to be aware of and to prepare for planned activities. The service delivers alerts and notifications triggered by changes in the health of AWS resources, so that you get near-instant event visibility and guidance to help accelerate troubleshooting.

All customers can use the AWS Health Dashboard, powered by the AWS Health API. The dashboard requires no setup, and it's ready to use for authenticated AWS users.

Additionally, Support customers who have a Business or Enterprise support plan can use the AWS Health API to integrate with in-house and third-party systems.

## How AWS Health differs for AWS GovCloud (US)

- The Amazon EventBridge channel doesn't send public events from the Service Health View of the AWS Health Dashboard.
  - Instead, use the AWS Health API or Service Health View RSS feed to programmatically receive these events. Account specific events are accessible through the EventBridge endpoint.

- AWS Health notifies you about planned lifecycle events and service changes that can affect resource availability. You won't see the status on affected resources change in response to resolution.
  - AWS Health may send periodic reminder notifications with an updated list of outstanding resources.

- The AWS Health API is accessible through a single regional endpoint in `us-gov-west-1`, as opposed to a global endpoint with failover-capable regions behind it.

## Documentation for AWS Health

[AWS Health documentation](../../../health/index.md "../../../health/index.md").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains
how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings.
The list can be used as a guide to help meet applicable customer compliance obligations.
Data not included in the following list remains within the AWS GovCloud (US) Regions.

- This service can generate metadata from customer-defined configurations. AWS suggests customers do not enter export-controlled information in console fields, descriptions, resource names, and tagging information.
