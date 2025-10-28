# Configuring ServiceNow for integration with AWS Systems Manager Incident Manager

This section shows you how to integrate AWS Systems Manager Incident Manager in ServiceNow.

###### To configure the AWS Systems Manager Incident Manager integration system properties

1. In the navigator, enter `AWS Service Management Connector`.
2. Choose **System Properties**, then **AWS Systems Manager Incident Manager.**
3. Review the available settings and recommendations in the table below.

| Available settings                                                                                                                  | Description                                                                                                                                                                                                                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Assignment Group value (SYS_ID) to use when creating ServiceNow Incidents from AWS Systems Manager Incident Manager synchronization | sys_id of the assignment group that the Connector uses when synching Incidents from AWS Systems Manager Incident Manager Default value: <empty>                                                                                                                                                                                                                         |
| Synchronization of the resolved status                                                                                              | Bidirectional. Sync Resolve status of the incident from AWS to ServiceNow and ServiceNow to AWS Unidirectional: AWS to ServiceNow. Sync Resolve status of the incident only from AWS to ServiceNow Unidirectional: ServiceNow to AWS. Sync Resolve status of the incident only from ServiceNow to AWS None. Resolve status are not synched Default value: Bidirectional |
