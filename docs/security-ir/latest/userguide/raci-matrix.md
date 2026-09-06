

# RACI matrix
<a name="raci-matrix"></a>

 The following RACI matrix defines roles and responsibilities across the Security Incident Response implementation process. RACI stands for Responsible (R), Accountable (A), Consulted (C), and Informed (I). 


<table>
<thead>
  <tr><th>Activity</th><th>Customer</th><th>AWS Account Team</th><th>SIR Team</th></tr>
</thead>
<tbody>
  <tr><td colspan="4"><b>Pre-Onboarding</b></td></tr>
  <tr><td>Identify Key Stakeholders</td><td>R</td><td></td><td>I</td></tr>
  <tr><td>Validate Finding Sources</td><td>R</td><td>C</td><td>I</td></tr>
  <tr><td>[3rd Party EDR integration] Security Hub CSPM</td><td>R</td><td>C</td><td>I</td></tr>
  <tr><td>GuardDuty Validation/Health Check</td><td>C</td><td>R</td><td>I</td></tr>
  <tr><td>Determine Account Scope</td><td>R</td><td></td><td></td></tr>
  <tr><td>Establish Escalation Protocols</td><td>R</td><td>I</td><td>C</td></tr>
  <tr><td>Enable AWS Organizations</td><td>R</td><td>C</td><td></td></tr>
  <tr><td>Associate accounts with AWS Organizations</td><td>R</td><td>I</td><td></td></tr>
  <tr><td>Select Delegated Administrator / Security Tooling Account</td><td>R</td><td>I</td><td></td></tr>
  <tr><td colspan="4"><b>Onboarding</b></td></tr>
  <tr><td>Setup membership details</td><td>R</td><td>I</td><td></td></tr>
  <tr><td>Walkthrough (Setup proactive response and alert triaging workflows; Deploy service-linked role to management account; Authorize containment actions)</td><td>R</td><td>C</td><td>I</td></tr>
  <tr><td colspan="4"><b>Post-Deployment Configuration</b></td></tr>
  <tr><td>Review operational integration capabilities</td><td>R</td><td>C</td><td>I</td></tr>
  <tr><td>Submit Security Incident Response Reactive Cases</td><td>R</td><td></td><td></td></tr>
  <tr><td>Configure Amazon EventBridge integrations</td><td>R</td><td>C</td><td>C</td></tr>
  <tr><td>Connect 3rd party tooling (Jira, ServiceNow, PagerDuty, Teams, etc.)</td><td>R</td><td>I</td><td>C</td></tr>
  <tr><td>Service deep dive and demo</td><td>A</td><td>R</td><td>C</td></tr>
</tbody>
</table>


 **RACI Definitions:** 
+ **Responsible (R)** - The party who performs the work to complete the task
+ **Accountable (A)** - The party ultimately answerable for the correct completion of the task
+ **Consulted (C)** - The party whose opinions are sought and with whom there is two-way communication
+ **Informed (I)** - The party who is kept up-to-date on progress and with whom there is one-way communication