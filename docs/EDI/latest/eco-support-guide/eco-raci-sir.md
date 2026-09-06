

# ECO SIR roles and responsibilities
<a name="eco-raci-sir"></a>

The following tables describe your (the "Customer") responsibilities compared with our ("AWS") responsibilities for the phases of security incident response (SIR).

Security incident response – Detect Phase


<table>
<thead>
  <tr><th><b>Activity</b></th><th><b>Customer</b></th><th><b>AWS</b></th></tr>
</thead>
<tbody>
  <tr><td colspan="3"><b>Logging, indicators, and monitors</b></td></tr>
  <tr><td>Configuring logs and monitors to enable event management for instances and accounts</td><td>C, I</td><td>R</td></tr>
  <tr><td>Monitoring supported AWS services for security alerts</td><td>I</td><td>R</td></tr>
  <tr><td>Deploying and managing endpoint security tools</td><td>R</td><td>I</td></tr>
  <tr><td>Monitoring for malware on instances using endpoint security</td><td>R</td><td>I</td></tr>
  <tr><td>Notifying customers of detected events through outbound messaging</td><td>I</td><td>R</td></tr>
  <tr><td>Routing notification and subsequent updates to the decision makers for specific accounts and workloads to improve incident response time</td><td>C, I</td><td>R</td></tr>
  <tr><td>Defining, deploying, and maintaining ECO standard detection services such as Amazon GuardDuty and AWS Config</td><td>C, I</td><td>R</td></tr>
  <tr><td>Recording AWS infrastructure change logs</td><td>C</td><td>R</td></tr>
  <tr><td>Implementing and maintaining an allowlist, denylist, and custom detections on supported AWS security services, such as Amazon GuardDuty</td><td>R</td><td>C</td></tr>
</tbody>
</table>


Security incident response – Analyze Phase


<table>
<thead>
  <tr><th><b>Activity</b></th><th><b>Customer</b></th><th><b>AWS</b></th></tr>
</thead>
<tbody>
  <tr><td colspan="3"><b>Investigation and analysis</b></td></tr>
  <tr><td>Performing an initial response for supported security alerts that a supported detection source generated</td><td>I</td><td>R, C</td></tr>
  <tr><td>Using available data to assess false and true positives</td><td>C, I</td><td>R</td></tr>
  <tr><td>Reviewing ECO assessments for false and true positives that ECO shares</td><td>R</td><td>C</td></tr>
  <tr><td>Generating a snapshot of affected instances that ECO shares with the customer, if needed</td><td>I</td><td>R</td></tr>
  <tr><td>Performing forensics tasks such as chain of custody, file system analysis, memory forensics, and binary analysis</td><td>R</td><td>C, I</td></tr>
  <tr><td>Collecting application logs to help with troubleshooting</td><td>C</td><td>R</td></tr>
  <tr><td>Collecting data and logs that are accessible to ECO to help investigate security alerts</td><td>C, I</td><td>R</td></tr>
  <tr><td>Responding to the alerts to help ECO investigate</td><td>R</td><td>C, I</td></tr>
  <tr><td>Engaging SMEs within ECO services on security investigations</td><td>C, I</td><td>R</td></tr>
  <tr><td>Engaging third-party vendors during investigation such as for EPS anti-malware </td><td>R, C, I</td><td>I</td></tr>
  <tr><td>Sharing investigation logs from supported AWS services to customers during an investigation</td><td>I</td><td>R</td></tr>
  <tr><td colspan="3"><b>Communication</b></td></tr>
  <tr><td>Sending alerts and notifications from ECO detection sources for managed resources</td><td>I</td><td>R</td></tr>
  <tr><td>Managing alerts and notifications for application security events</td><td>C</td><td>R</td></tr>
  <tr><td>Engaging the customer security point of contact during a security incident investigation</td><td>R</td><td>I</td></tr>
</tbody>
</table>


Security incident response – Contain Phase


<table>
<thead>
  <tr><th><b>Activity</b></th><th><b>Customer</b></th><th><b>AWS</b></th></tr>
</thead>
<tbody>
  <tr><td colspan="3"><b>Containment strategy and execution</b></td></tr>
  <tr><td>Deciding on the execution of the agreed containment strategy and agreeing with the consequences that might affect the availability of services during the containment window</td><td>R</td><td>C, I</td></tr>
  <tr><td>Backing up affected systems for further analysis</td><td>C, I</td><td>R</td></tr>
  <tr><td>Containing applications and workloads through application-specific configuration or response activity</td><td>C, I</td><td>R</td></tr>
  <tr><td>Defining the containment strategy based on the security incident and the affected resource</td><td>C, I</td><td>R</td></tr>
  <tr><td>Enabling encryption and secure storage of point-in-time backups of affected systems</td><td>R, C, I</td><td>C</td></tr>
  <tr><td>Executing supported containment actions for AWS resources, including Amazon Elastic Compute Cloud (Amazon EC2) instances, network, and AWS Identity and Access Management (IAM)</td><td>C, I</td><td>R</td></tr>
</tbody>
</table>


Security incident response – Eradicate Phase


<table>
<thead>
  <tr><th><b>Activity</b></th><th><b>Customer</b></th><th><b>AWS</b></th></tr>
</thead>
<tbody>
  <tr><td colspan="3"><b>Eradication strategy and execution</b></td></tr>
  <tr><td>Defining eradication options based on the security incident and the affected resource on customer application workloads</td><td>R</td><td>C, I</td></tr>
  <tr><td>Deciding on the agreed eradication strategy, timing of eradication execution and the consequences</td><td>R</td><td>C, I</td></tr>
  <tr><td>Defining eradication steps based on the security incident and the affected resource on ECO managed workloads</td><td>C, I</td><td>R</td></tr>
  <tr><td>Eradicating and hardening AWS resources including Amazon EC2 instances, network, and IAM</td><td>C, I</td><td>R</td></tr>
  <tr><td>Eradicating and hardening applications and workloads through application-specific configuration or response activity</td><td>R</td><td>I</td></tr>
</tbody>
</table>


Security incident response – Recover Phase


<table>
<thead>
  <tr><th><b>Activity</b></th><th><b>Customer</b></th><th><b>AWS</b></th></tr>
</thead>
<tbody>
  <tr><td colspan="3"><b>Recovery preparation and execution</b></td></tr>
  <tr><td>Configuring backup plans and targets as requested by the customer</td><td>C</td><td>R</td></tr>
  <tr><td>Reviewing backup plans to restore ECO managed workloads</td><td>C</td><td>R</td></tr>
  <tr><td>Performing backup restoration activities for resources of supported AWS services</td><td>I</td><td>R</td></tr>
  <tr><td>Reviewing and confirming backup plans to restore customer applications and workloads post-incident</td><td>R, A</td><td>C, I</td></tr>
  <tr><td>Backing up customer applications, application configurations, and deployment settings to restore customer applications and workloads post-incident</td><td>C, I</td><td>R, A</td></tr>
  <tr><td>Restoring applications and customer workloads through application-specific restoration steps</td><td>R, C</td><td>R, C</td></tr>
</tbody>
</table>


Security incident response – PIR Phase


<table>
<thead>
  <tr><th><b>Activity</b></th><th><b>Customer</b></th><th><b>AWS</b></th></tr>
</thead>
<tbody>
  <tr><td colspan="3"><b>Post incident reporting</b></td></tr>
  <tr><td>Sharing appropriate lessons learned and action items with customer as required</td><td>I</td><td>R, A</td></tr>
</tbody>
</table>
