

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Configuring ServiceNow for integration with AWS Systems Manager Incident Manager
<a name="sn-im-config"></a>

This section shows you how to integrate AWS Systems Manager Incident Manager in ServiceNow.

**To configure the AWS Systems Manager Incident Manager integration system properties**

1. In the navigator, enter **AWS Service Management Connector**. 

1. Choose **System Properties**, then **AWS Systems Manager Incident Manager.**

1. Review the available settings and recommendations in the table below.


| Available settings | Description | 
| --- | --- | 
| Assignment Group value (SYS\_ID) to use when creating ServiceNow Incidents from AWS Systems Manager Incident Manager synchronization | sys\_id of the assignment group that the Connector uses when synching Incidents from AWS Systems Manager Incident Manager<br />Default value: <empty> | 
| Synchronization of the resolved status | Bidirectional. Sync Resolve status of the incident from AWS to ServiceNow and ServiceNow to AWS<br />Unidirectional: AWS to ServiceNow. Sync Resolve status of the incident only from AWS to ServiceNow<br />Unidirectional: ServiceNow to AWS. Sync Resolve status of the incident only from ServiceNow to AWS<br />None. Resolve status are not synched <br />Default value: Bidirectional | 