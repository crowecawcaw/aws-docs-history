

# EDI Cloud Operations roles and responsibilities
<a name="eco-raci"></a>

The ECO responsible, accountable, consulted, and informed, or RACI, matrix assigns primary responsibility either to you or ECO for a variety of activities.

Each letter in RACI represents a different party that's involved in the matrix:
+ **R** is the responsible party that does the work to achieve the task.
+ **A** is the accountable party that gets the work done to complete the task.
+ **C** is the consulted party whose opinions are sought, typically as subject matter experts (SMEs); and with whom there's bilateral communication.
+ **I** is the informed party who's notified about the progress of a task, usually only on task completion.

ECO manages your EDI on AWS environment. The following table provides an overview of the activities in the lifecycle of an EDI application that runs within the managed environment. The "Customer" column represents your roles and responsibilities, and the "AWS" column represents the roles and responsibilities of ECO.


<table>
<thead>
  <tr><th><b>Activity</b></th><th><b>Customer</b></th><th><b>AWS</b></th></tr>
</thead>
<tbody>
  <tr><td colspan="3"><b>Provisioning</b></td></tr>
  <tr><td>EDI solution (Operations, Data Platform, and EDI IQ) deployment in the customer's account</td><td>C, I</td><td>R, A</td></tr>
  <tr><td>EDI Data Portal initial admin user creation</td><td>C, I</td><td>R, A</td></tr>
  <tr><td>EDI Data Portal user creation and management</td><td>R, A</td><td>C</td></tr>
  <tr><td>EDI hosted zone creation and management for Data Portal</td><td>R</td><td>I</td></tr>
  <tr><td colspan="3"><b>Monitoring and Logging</b></td></tr>
  <tr><td>EDI solution monitoring</td><td>I</td><td>R, A</td></tr>
  <tr><td>AWS infrastructure monitoring</td><td>C, I</td><td>R, A</td></tr>
  <tr><td>Recording AWS infrastructure change logs</td><td>I</td><td>R, A</td></tr>
  <tr><td>Deploying and managing third-party monitoring tools, such as Dynatrace and New Relic</td><td>R, A</td><td>C</td></tr>
  <tr><td colspan="3"><b>Data load and ingestion</b></td></tr>
  <tr><td>Data ingestion and reingestion from the application, the EDI IQ and custom sources—such as CSV, WITSML, Manifest, and Code Pipeline— into the EDI cluster</td><td>R, A</td><td>C</td></tr>
  <tr><td>Missing or incorrect data validation and indexing issues</td><td>R</td><td>C</td></tr>
  <tr><td colspan="3"><b>Disaster recovery</b></td></tr>
  <tr><td>Performing point-in-time backup restoration activities through AWS managed services, such as Amazon Relational Database Service (Amazon RDS), and Amazon DynamoDB</td><td>C</td><td>R, A</td></tr>
  <tr><td>Backup and restore for EDI entitlement through Amazon OpenSearch Service</td><td>C</td><td>R, A</td></tr>
  <tr><td>Deploying and reviewing backup plans</td><td>C</td><td>R, A</td></tr>
  <tr><td>Deploying and managing third-party backup tools, such as Commvault</td><td>R, A</td><td>C</td></tr>
  <tr><td colspan="3"><b>Migration</b></td></tr>
  <tr><td>Migrating data from the existing OSDU® to the EDI environment</td><td>R, A</td><td>C</td></tr>
  <tr><td>Data snapshot backup and restore through AWS Disaster Recovery</td><td>R, A</td><td>C</td></tr>
  <tr><td colspan="3"><b>Upgrades and patching</b></td></tr>
  <tr><td>Upgrading the EDI environment</td><td>I</td><td>R</td></tr>
  <tr><td>Patching the EDI environment and AWS infrastructure for hotfixes or security vulnerabilities</td><td>I</td><td>R</td></tr>
  <tr><td>Notification for EDI end of life support</td><td>I</td><td>R</td></tr>
  <tr><td>Approval for EDI environment upgrade</td><td>R</td><td>I</td></tr>
  <tr><td colspan="3"><b>Incident management</b></td></tr>
  <tr><td>Proactively notifying incidents on the EDI environment and AWS infrastructure that are based on monitoring</td><td>I</td><td>R</td></tr>
  <tr><td>Categorizing incident priority</td><td>I</td><td>R</td></tr>
  <tr><td>Providing incident response</td><td>I</td><td>R</td></tr>
  <tr><td>Providing incident resolution and infrastructure restore</td><td>C, I</td><td>R</td></tr>
  <tr><td colspan="3"><b>Documentation and training</b></td></tr>
  <tr><td>Providing customer documentation about the EDI architecture and EDI on AWS operations</td><td>I</td><td>R</td></tr>
  <tr><td>Leading and conducting incident response processes through game days with the customer</td><td>C, I</td><td>R, A</td></tr>
  <tr><td>Participating in incident response processes through game days</td><td>R</td><td>A, C</td></tr>
  <tr><td colspan="3"><b>Troubleshooting</b></td></tr>
  <tr><td>EDI deployment issues</td><td>I</td><td>R</td></tr>
  <tr><td>API endpoint connection failures</td><td>I</td><td>R</td></tr>
  <tr><td>Data ingestion failures</td><td>R</td><td>C</td></tr>
  <tr><td>EDI environment functionality issues and outages</td><td>C</td><td>R</td></tr>
</tbody>
</table>
