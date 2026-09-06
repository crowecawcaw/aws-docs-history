

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Change management in Direct Change mode
<a name="dcm-change-mgmt"></a>

Change management is the process that AMS Advanced uses to implement requests for change. A request for change (RFC) is a request created by either you, or AMS Advanced through the AMS Advanced interface to make a change to your managed environment and includes an AMS Advanced change type (CT) ID for a particular operation. For more information, see [Change management](https://docs.aws.amazon.com/managedservices/latest/userguide/ex-what-is.html).

**Note**  
Direct Change mode does not remove AMS change management RFCs, you still have full access to AMS RFCs with DCM.

AMS Direct Change mode (DCM) extends AMS Advanced change management by providing native AWS access to AMS Advanced Plus and Premium accounts to provision and update AWS resources. Users who have been granted Direct Change mode permission through the IAM roles, can use native AWS API access to provision and make changes to resources in their AMS Advanced accounts. The users can still use AMS Advanced change management RFCs using the same IAM roles. In both cases the resources and changes to them are fully supported by AMS, including monitoring, patch, backup, incident response management. Users who do not have the appropriate role in these accounts must use the AMS Advanced change management RFC process to make changes. 

## Change management use cases
<a name="dcm-cm-use-cases"></a>

For security reasons, some changes in AMS Advanced can only be done through the change management request for change (RFC) process. The `AWSManagedServicesCloudFormationAdminRole` is restricted to actions taken through CloudFormation (CFN). For more about how to create stacks through DCM, see [Creating stacks using Direct Change mode](https://docs.aws.amazon.com/managedservices/latest/userguide/dcm-creating-stacks.html). The `AWSManagedServicesUpdateRole` is restricted for the following actions.

For example walkthroughs for each change type, including the Management \| Managed account \| Direct Change mode \| Enable (ct-3rd4781c2nnhp) change type, see the "Additional Information" section for the relevant change type in the *AMS Advanced Change Type Reference* [Change Types by Classification](https://docs.aws.amazon.com/managedservices/latest/ctref/classifications.html) section.

<a name="AMS-STD-007"></a>
<table>
<thead>
  <tr><th>Service</th><th>Action</th></tr>
</thead>
<tbody>
  <tr><td>AWS Key Management Service (AWS KMS)</td><td>Update</td></tr>
  <tr><td>AWS Certificate Manager</td><td>Create</td></tr>
  <tr><td>AWS Identity and Access Management (IAM)</td><td>Any</td></tr>
  <tr><td>Site-to-Site VPN</td><td rowspan="2">Any</td></tr>
  <tr><td>AMS Resource Scheduler</td></tr>
  <tr><td>AWS Backup</td><td>Create backup plan</td></tr>
  <tr><td>AMS Workload Ingestion (WIGs)</td><td rowspan="3">Any</td></tr>
  <tr><td>AMS Advanced MALZ account changes</td></tr>
  <tr><td>Amazon GuardDuty</td></tr>
  <tr><td>AMS Advanced Stack Access</td><td>Any</td></tr>
  <tr><td>Amazon Elastic Block Store (EBS) volume</td><td>Delete</td></tr>
  <tr><td>Amazon Elastic Block Store (EBS) default encryption</td><td>Enable default encryption</td></tr>
  <tr><td>Amazon Elastic Compute Cloud (Amazon EC2)</td><td>Change hostname</td></tr>
  <tr><td>Amazon Machine Images (AMI)</td><td>Delete, share</td></tr>
  <tr><td>Amazon EC2 Security Group</td><td rowspan="4">Any</td></tr>
  <tr><td>AMS Advanced SSPS</td></tr>
  <tr><td>AWS Managed Microsoft AD</td></tr>
  <tr><td>AMS Advanced developer mode</td></tr>
  <tr><td>Amazon Simple Storage Service (Amazon S3)</td><td>Create S3 bucket policies</td></tr>
  <tr><td>AWS Systems Manager</td><td>Create</td></tr>
</tbody>
</table>
