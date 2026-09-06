

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Fields mapped from OpsCenter OpsItem records to ServiceNow Incident records
<a name="fields-opsitems"></a>

This table shows how AWS OpsItems map to ServiceNow Incidents.


| AWS Ops Center | ServiceNow Incident | 
| --- | --- | 
| Title  | short\_description  | 
| Description | description  | 
| CreatedTime  | opened\_at  | 
| Status | incident\_state  | 
| Severity  | impact/urgency  | 
| Priority | priority | 
| CreatedBy  | Not synced  | 
| LastModifiedTime | Not synced  | 
| LastModifiedBy | Not synced  | 
| Source | Not synced  | 
| OpsItemId  | Not synced  | 
| OperationalData | Not synced  | 
| Category  | Software | 

**Incident Status** is an integer in ServiceNow. We map OpsItem status values to values.


| ServiceNow Incident Status  | OpsCenter Status  | 
| --- | --- | 
| New (primary) | Open | 
| On Hold | Open | 
| In Progress | In Progress | 
| Resolved (primary) | Resolved | 
| Closed | Resolved | 
| Cancelled | Resolved | 

In this type of subjective mapping, we only change the target value if it is incompatible. An example of subjective mapping would be if *New* and *On Hold* in ServiceNow both map to *Open* in AWS. An example of an incompatible target would be if the Incident is *On Hold*, while we're synchronizing from AWS an OpsItem that is *Open*, and we don't change *On Hold*.

**Priority** - In Incident, you can’t set the Priority field directly. The values of the **Impact** and **Urgency** fields calculate the **Priority** field. When synchronizing from AWS, we set by default the fields shown in the table below: 


<table>
<thead>
  <tr><th>OpsItem Priority </th><th colspan="3">ServiceNow Incident</th></tr>
</thead>
<tbody>
  <tr><td></td><td><b>Impact</b></td><td><b>Urgency</b></td><td><b>Priority (Calculated)</b></td></tr>
  <tr><td>1</td><td>High</td><td>High</td><td> Critical (1)</td></tr>
  <tr><td>2</td><td>Medium</td><td>High</td><td>High (2)</td></tr>
  <tr><td>3</td><td>Medium</td><td>Medium</td><td>Moderate (3)</td></tr>
  <tr><td>4</td><td>Low </td><td>Medium</td><td>Low (4)</td></tr>
  <tr><td>5</td><td>Low </td><td>Low </td><td>Planning (5)</td></tr>
</tbody>
</table>


You can find these mappings in a ServiceNow table *Priority Data Lookup*. While we can use this table to find the required values of **Impact** and **Urgency**, note that you can customize the mappings and also define new priority values. Additionally, you might want a specific priority in AWS to map to an entirely different priority in an Incident or Problem. 