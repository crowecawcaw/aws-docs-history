

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Why and when AMS accesses your account
<a name="access-justification"></a>

AWS Managed Services (AMS) manages your AWS infrastructure and sometimes, for specific reasons, AMS operators and administrators access your account. These access events are documented in your AWS CloudTrail (CloudTrail) logs.

Why, when, and how AMS accesses your account is explained in the following topics.

## AMS customer account access triggers
<a name="access-mgmt-triggers"></a>

AMS customer account access activity is driven by triggers. The triggers today are the AWS tickets created in our issues management system in response to Amazon CloudWatch (CloudWatch) alarms and events, and incident reports or service requests that you submit. Multiple service calls and host-level activities might be performed for each access. 

Access justification, the triggers, and the initiator of the trigger are listed in the following table.


**Access Triggers**  

<table>
<thead>
  <tr><th>Access</th><th>Initiator</th><th>Trigger</th></tr>
</thead>
<tbody>
  <tr><td>Patching</td><td>AMS</td><td>Patch issue</td></tr>
  <tr><td>Infrastructure deployments</td><td>AMS</td><td>Deployment issue</td></tr>
  <tr><td>Internal problem investigation</td><td>AMS</td><td>Problem issue (an issue that has been identified as systemic)</td></tr>
  <tr><td>Alert investigation and remediation</td><td>AMS</td><td>AWS Systems Manager operational work items (SSM OpsItems)</td></tr>
  <tr><td>Manual RFC execution</td><td>You</td><td>Request for Change (RFC) issue. (Non-automated RFCs may require AMS access to your resources)</td></tr>
  <tr><td>Incident investigation and remediation</td><td>You</td><td rowspan="2">Inbound support case (an incident or service request you submit)</td></tr>
  <tr><td>Inbound service request fulfillment</td><td>You</td></tr>
</tbody>
</table>


## AMS customer account access IAM roles
<a name="access-mgmt-iam-roles"></a>

When triggered, AMS accesses customer accounts using AWS Identity and Access Management (IAM) roles. Like all activity in your account, the roles and their usage are logged in CloudTrail.

**Important**  
Do not modify or delete these roles.


**IAM roles for AMS access to customer accounts**  
<a name="iam-access-roles-table"></a>
<table>
<thead>
  <tr><th>Role Name</th><th>Account Type (SALZ, MALZ Management, MALZ Application, etc.)</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>ams-service-admin</td><td>SALZ, MALZ</td><td>AMS Service automation access and automated infrastructure deployments e.g Patch, Backup, Automated Remediation.</td></tr>
  <tr><td>ams-application-infra-read-only</td><td rowspan="3">SALZ, MALZ Application, MALZ Tools-Application</td><td>Operator read only access</td></tr>
  <tr><td>ams-application-infra-operations</td><td>Operator access for incidents/service requests</td></tr>
  <tr><td>ams-application-infra-admin</td><td>AD Admin access</td></tr>
  <tr><td>ams-primary-read-only</td><td rowspan="3">MALZ Management</td><td>Operator read only access</td></tr>
  <tr><td>ams-primary-operations</td><td>Operator access for incidents/service requests</td></tr>
  <tr><td>ams-primary-admin</td><td>AD Admin access</td></tr>
  <tr><td>ams-logging-read-only</td><td rowspan="3">MALZ Logging</td><td>Operator read only access</td></tr>
  <tr><td>ams-logging-operations</td><td>Operator access for incidents/service requests</td></tr>
  <tr><td>ams-logging-admin</td><td>AD Admin access</td></tr>
  <tr><td>ams-networking-read-only</td><td rowspan="3">MALZ Networking</td><td>Operator read only access</td></tr>
  <tr><td>ams-networking-operations</td><td>Operator access for incidents/service requests</td></tr>
  <tr><td>ams-networking-admin</td><td>AD Admin access</td></tr>
  <tr><td>ams-shared-services-read-only</td><td rowspan="3">MALZ Shared Services</td><td>Operator read only access</td></tr>
  <tr><td>ams-shared-services-operations</td><td>Operator access for incidents/service requests</td></tr>
  <tr><td>ams-shared-services-admin</td><td>AD Admin access</td></tr>
  <tr><td>ams-security-read-only</td><td rowspan="3">MALZ Security</td><td>Operator read only access</td></tr>
  <tr><td>ams-security-operations</td><td>Operator access for incidents/service requests</td></tr>
  <tr><td>ams-security-admin</td><td>AD Admin access</td></tr>
  <tr><td>ams-access-security-analyst</td><td rowspan="2">SALZ, MALZ Application, MALZ Tools-Application, MALZ Core</td><td>AMS Security access</td></tr>
  <tr><td>ams-access-security-analyst-read-only</td><td>AMS Security, read only access</td></tr>
  <tr><td>Sentinel_AdminUser_Role_PXHazRQadu0PVcCDcMbHE</td><td>SALZ</td><td>[BreakGlassRole]Used to breakGlass into the customer accounts</td></tr>
  <tr><td>Sentinel_PowerUser_Role_wZuPuS0ROOl0IazDbRI9</td><td rowspan="5">SALZ, MALZ</td><td>Poweruser access to customer accounts for RFC execution</td></tr>
  <tr><td>Sentinel_ReadOnlyUser_Role_Pd4L6Rw9RD0lnLkD5JOo</td><td>ReadOnly access to customer accounts for RFC execution</td></tr>
  <tr><td>ams_admin_role</td><td>Admin access to customer accounts for RFC execution</td></tr>
  <tr><td>AWSManagedServices_Provisioning_CustomerStacksRole</td><td>Used to launch and update CFN stacks on behalf of customers through CloudFormation Ingest</td></tr>
  <tr><td>customer_ssm_automation_role</td><td>Role passed by CT executions to SSM Automation for runbook execution</td></tr>
  <tr><td>ams_ssm_automation_role</td><td>SALZ, MALZ Application, MALZ Core</td><td>Role passed by AMS services to SSM Automation for runbook execution</td></tr>
  <tr><td>ams_ssm_iam_deployment_role</td><td>MALZ Application</td><td>Role used by IAM catalog</td></tr>
  <tr><td>ams_ssm_shared_svcs_intermediary_role</td><td>MALZ Shared Services</td><td>Role used by application ams_ssm_automation_role to execute specific SSM Documents in Shared Services account</td></tr>
  <tr><td>AmsOpsCenterRole</td><td rowspan="3">SALZ, MALZ</td><td>Used to create and update OpsItems in customer accounts</td></tr>
  <tr><td>AMSOpsItemAutoExecutionRole</td><td>Used to get SSM Documents, describe resource tags, update OpsItems, and start automation</td></tr>
  <tr><td>customer-mc-ec2-instance-profile</td><td>Default customer EC2 instance profile (role)</td></tr>
</tbody>
</table>


## Requesting instance access
<a name="req-instance-access"></a>

To access a resource, you must first submit a request for change (RFC) for that access. There are two types of access that you can request: admin (read/write permissions) and read-only (standard user access). Access lasts for eight hours, by default. This information is required:
+ Stack ID, or set of stack IDs, for the instance or instances you want to access.
+ The fully qualified domain name of your AMS-trusted domain.
+ The Active Directory username of the person who wants access.
+ The ID of the VPC where the stacks are that you want access to.

Once you've been granted access, you can update the request as needed.

For examples of how to request access, see [Stack Admin Access \| Grant](https://docs.aws.amazon.com/managedservices/latest/ctref/management-access-stack-admin-access-grant.html) or [Stack Read-only Access \| Grant](https://docs.aws.amazon.com/managedservices/latest/ctref/management-access-stack-read-only-access-grant.html).