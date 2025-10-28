# Troubleshoot FAILED contacts

A contact will have a terminal contact status of **FAILED** when AWS Ground Station detects an issue with your resource configuration. The common use cases that can cause **FAILED** contacts are provided below, along with steps to help troubleshoot.

###### Note

This guide is specifically for the **FAILED** contact status - and is not intended for other failure statuses, such as **AWS_FAILED**,
**AWS_CANCELLED**, or **FAILED_TO_SCHEDULE**. For more information on contact statuses, see
[AWS Ground Station contact statuses](contacts.md#contact-statuses "contacts.md#contact-statuses")

## Dataflow endpoint FAILED use cases

The following is the list of common use cases that can result in a **FAILED** contact status for dataflow endpoint based dataflows:

- **Dataflow endpoint never connects** - The connection between AWS Ground Station Antenna and your Dataflow Endpoint Group for one or more dataflows was never established.
- **Dataflow endpoint connects late** - The connection between AWS Ground Station Antenna and your Dataflow Endpoint Group for one or more dataflows was established after the contact start time.
- **Dataflow endpoint’s subnet is out of available IP addresses** - AWS Ground Station’s data delivery solution is not able to create an ENI in your private network due to not having any available IP address in the reciever instance's subnet.
- **Dataflow endpoint’s subnet is invalid** - AWS Ground Station’s data delivery solution is not able to create an ENI in your private network due to inability to access the provided subnet specified in the Dataflow Endpoint Group.

For any dataflow endpoint failure cases, it is recommended to look into the following:

- Confirm the receiver Amazon EC2 instance was started successfully, prior to contact start time.
- Confirm the dataflow endpoint software was up and running during the contact.
- Ensure you have at least one available IP address per dataflow endpoint per receiver instance subnet.
- Ensure subnets associated to your Dataflow Endpoint Group, through dataflows configured in
  [Set up and configure Amazon VPC](dataflows.md "dataflows.md"),
  remain active and available to AWS Ground Station.

See the section on [Troubleshoot contacts that deliver data to Amazon EC2](troubleshooting-contact.md "troubleshooting-contact.md") for more specific troubleshooting steps.

## AWS Ground Station Agent FAILED use cases

The following is the list of common use cases that can result in a **FAILED** contact status for Agent-based dataflows:

- **AWS Ground Station Agent Never Reported Status** - The Agent responsible for orchestrating data delivery on your Dataflow Endpoint Group for one or more dataflows never successfully reported status to AWS Ground Station. This status update should happen within a few seconds of the contact end time.
- **AWS Ground Station Agent Started Late** - The Agent responsible for orchestrating data delivery on your Dataflow Endpoint Group for one or more dataflows was started late, after the contact start time.

For any AWS Ground Station Agent dataflow failure cases, it is recommended to look into the following:

- Confirm the receiver Amazon EC2 instance was started successfully, prior to contact start time.
- Confirm the Agent application was up and running at the start and during the contact.
- Confirm the Agent application and Amazon EC2 instance were not shut down within 15 seconds of contact end. This provides the Agent sufficient time to report status to AWS Ground Station.

See the section on [Troubleshoot contacts that deliver data to Amazon EC2](troubleshooting-contact.md "troubleshooting-contact.md") for more specific troubleshooting steps.
