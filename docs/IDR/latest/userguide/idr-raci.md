

# Roles and responsibilities in Incident Detection and Response
<a name="idr-raci"></a>

The AWS Incident Detection and Response RACI (Responsible, Accountable, Consulted, and Informed) table outlines the roles and responsibilities for various activities related to incident detection and response. This table helps define the involvement of the customer and the AWS Incident Detection and Response team for tasks such as data collection, operations readiness review, account configuration, incident management, and post-incident review.


<table>
<thead>
  <tr><th><b>Activity</b></th><th><b>Customer</b></th><th><b>Incident Detection and Response</b></th></tr>
</thead>
<tbody>
  <tr><td colspan="3"><b>Data collection</b></td></tr>
  <tr><td>Customer and workload introduction</td><td>Consulted</td><td>Responsible</td></tr>
  <tr><td>Architecture</td><td>Responsible</td><td>Accountable</td></tr>
  <tr><td>Operations</td><td>Responsible</td><td>Accountable</td></tr>
  <tr><td>Determine CloudWatch alarms to be configured</td><td>Responsible</td><td>Accountable</td></tr>
  <tr><td>Define incident response plan</td><td>Responsible</td><td>Accountable</td></tr>
  <tr><td colspan="3"><b>Operations readiness review</b></td></tr>
  <tr><td>Conduct well architected review (WAR) on workload</td><td>Consulted</td><td>Responsible</td></tr>
  <tr><td>Validate incident response</td><td>Consulted</td><td>Responsible</td></tr>
  <tr><td>Validate alarm matrix</td><td>Consulted</td><td>Responsible</td></tr>
  <tr><td>Identify key AWS services being used by the workload</td><td>Accountable</td><td>Responsible</td></tr>
  <tr><td colspan="3"><b>Account configuration</b></td></tr>
  <tr><td>Create IAM role in customer account</td><td>Responsible</td><td>Informed</td></tr>
  <tr><td>Install managed EventBridge rule using created role</td><td>Informed</td><td>Responsible</td></tr>
  <tr><td>Test onboarded alarms (CloudWatch or APM)</td><td>Accountable</td><td>Informed</td></tr>
  <tr><td>Verify that customer alarms engage the incident detection and response</td><td>Informed</td><td>Responsible</td></tr>
  <tr><td>Update alarms</td><td>Responsible</td><td>Consulted</td></tr>
  <tr><td>Update runbooks</td><td>Consulted</td><td>Responsible</td></tr>
  <tr><td colspan="3"><b>Incident management</b></td></tr>
  <tr><td>Proactively notify Incidents detected by Incident Detection and Response</td><td>Informed</td><td>Responsible</td></tr>
  <tr><td>Provide incident response</td><td>Informed</td><td>Responsible</td></tr>
  <tr><td>Provide incident resolution / infrastructure restore</td><td>Responsible</td><td>Consulted</td></tr>
  <tr><td colspan="3"><b>Post-incident review</b></td></tr>
  <tr><td>Request post-incident review</td><td>Responsible</td><td>Informed</td></tr>
  <tr><td>Provide post-incident review</td><td>Informed</td><td>Responsible</td></tr>
</tbody>
</table>
