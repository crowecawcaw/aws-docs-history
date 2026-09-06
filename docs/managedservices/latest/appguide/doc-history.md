

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Document history
<a name="doc-history"></a>

The following table describes the documentation for this release of AMS.
+ **API version:** 2019-05-21
+ **Latest documentation update: **February 16, 2023



<table>
<thead>
  <tr><th>Change</th><th>Description</th><th>Link</th></tr>
</thead>
<tbody>
  <tr><td>Drift remediation not supported for CloudFormation-ingested stacks</td><td>Added a note that drift remediation is not supported by AMS for CloudFormation-ingested stacks, and removed the drift remediation mention from the ingest process overview.</td><td><a href="https://docs.aws.amazon.com/managedservices/latest/appguide/ams-cfn-ingest.html">AMS CloudFormation ingest</a></td></tr>
  <tr><td>TOC link removed</td><td>TOC <a href="https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html">AWS Glossary</a> link removed.</td><td>August 08, 2025</td></tr>
  <tr><td>Updated content: Migrating Workloads: Windows pre-ingestion validation</td><td>Updated section to include detailed steps for using the pre-WIGs validater script to validate that your Windows instance is ready for ingestion into your AMS account;.</td><td><a href="ex-migrate-instance-win-validation.md">Migrating workloads: Windows pre-ingestion validation</a></td></tr>
  <tr><td>Updated content, DMS configuration</td><td>an important note about the required role, dms-vpc-role.</td><td><a href="ex-dms-rsg-create-1.md">1: AWS DMS replication subnet group: Create</a></td></tr>
  <tr><td>Updated content, CFN Ingest supported resources</td><td>Added OpenSearch.</td><td><a href="cfn-ingest-supp-services.md">Supported Resources</a></td></tr>
  <tr><td>Updated content, Migrating workloads</td><td>Updated instructions for pre-ingestion validation.</td><td><a href="ex-migrate-instance-win-validation.md">Migrating workloads: Windows pre-ingestion validation</a></td></tr>
  <tr><td>Updated content, CFN Ingest.</td><td>Removed restricted "supported resources" from CFN ingest content.</td><td><a href="cfn-ingest-supp-services.md#ex-cfn-ingest-supp-resources">CloudFormation Ingest Stack: Supported resources</a></td></tr>
  <tr><td>Updated supported Windows versions</td><td>Added support for Windows Server 2022.</td><td> <a href="ams-amis.md">AMS Amazon Machine Images (AMIs)</a>, <a href="ex-migrate-instance-prereqs.md">Migrating Workloads: Prerequisites for Linux and Windows</a>, and <a href="ex-migrate-instance-win-validation.md">Migrating workloads: Windows pre-ingestion validation</a> </td></tr>
  <tr><td>Updated content, Resource Scheduler.</td><td>Updated instructions to use the dedicated deployment CT, ct-0ywnhc8e5k9z5, applicable to both SALZ and MALZ.</td><td><a href="qs-resource-scheduler.md">AMS Resource Scheduler quick start</a></td></tr>
  <tr><td>Updated content, Workload Ingest.</td><td>Updated supported SUSE Linux versions.</td><td><a href="ex-migrate-instance-prereqs.md">Migrating Workloads: Prerequisites for Linux and Windows</a></td></tr>
  <tr><td>Updated content, Database Migration Service.</td><td>Added to prerequisites and made several changes for usefulness and usability.</td><td><a href="service-create-dms.md">AWS Database Migration Service (AWS DMS)</a></td></tr>
  <tr><td>Updated content, Workload Ingest.</td><td>The Linux Pre-WIGS Validation Zip has been updated.</td><td><a href="ex-migrate-instance-prereqs.md">Migrating Workloads: Prerequisites for Linux and Windows</a></td></tr>
  <tr><td>Updated content.</td><td>Updated the pre-WIGS validation zip for Linux. Also, added Windows Server 2008 R2 as a supported operating system.</td><td><a href="ex-migrate-instance-prereqs.md">Migrating Workloads: Prerequisites for Linux and Windows</a></td></tr>
  <tr><td>New content</td><td>Quick Starts and Tutorials have been moved here from the retired <i>AMS Advanced Change Management Guide</i>.</td><td><a href="quick-starts.md">Quick starts</a>, <a href="tutorials.md">Tutorials</a>.</td></tr>
  <tr><td>Updated content</td><td>Deployment | Advanced stack components | Database Migration Service (DMS) | Start replication task (ct-1yq7hhqse71yg)<br />Updated to indicate the <b>DocumentName</b> and <b>Region are required parameters</b>; previously, they were erroneously listed as optional.</td><td><a href="https://docs.aws.amazon.com/managedservices/latest/ctref/management-advanced-database-migration-service-dms-start-replication-task.html"> Database Migration Service (DMS) | Start Replication Task</a></td></tr>
  <tr><td>Updated content</td><td>CloudFormation Ingest<br />Updated to indicate two new supported resources, AWS::Route53Resolver::ResolverRuleAssociation and AWS::Route53Resolver::ResolverRule.</td><td><a href="cfn-ingest-supp-services.md">Supported Resources</a></td></tr>
  <tr><td>Updated content</td><td>Migrating workloads: Windows pre-ingestion validation</td><td>Sysprep information updated with more specifics.<br /><a href="ex-migrate-instance-win-validation.md">Migrating workloads: Windows pre-ingestion validation</a></td></tr>
  <tr><td rowspan="2">Updated content</td><td>Management | Custom stack | Stack from CloudFormation Template | Approve Changeset and Update (ct-1404e21baa2ox)<br />The CT walkthrough description for the <b>ChangeSetName</b> parameter has been updated with additional information.</td><td><a href="https://docs.aws.amazon.com/managedservices/latest/ctref/management-custom-stack-from-cloudformation-template-approve-changeset-and-update.html">Stack from CloudFormation Template | Approve Changeset and Update</a></td></tr>
  <tr><td>Ubuntu 18.04 and Oracle Linux 8.3 available</td><td><a href="ex-migrate-instance-prereqs.md">Migrating Workloads: Prerequisites for Linux and Windows</a></td></tr>
  <tr><td colspan="3"> </td></tr>
  <tr><td>New content:</td><td>IAM deployments through CFN Ingest and Stack Update CTs.</td><td>February 10, 2022 </td></tr>
  <tr><td>Database Migration Service (DMS) replication tasks</td><td>Change types updated so regular expressions permit task ARNs that contain hyphens. <a href="ex-create-dms-manage.md#ex-dms-rt-start-col">Start AWS DMS replication task</a> and <a href="https://docs.aws.amazon.com/managedservices/latest/ctref/management-advanced-database-migration-service-dms-stop-replication-task.html">Database Migration Service (DMS) | Stop Replication Task</a>. </td><td>January 13, 2022</td></tr>
  <tr><td>Linux WIGS pre-ingestion validation</td><td>The zip file was updated. <a href="ex-migrate-instance-linux-validation.md">Migrating workloads: Linux pre-ingestion validation</a>. </td><td>January 13, 2022</td></tr>
  <tr><td>Fixed links</td><td>The Database (DB) Import to AMS SQL RDS -&gt; <a href="db-to-sql-rds-setup.md">Setting up</a> section had some bad links. </td><td>January 13, 2022</td></tr>
</tbody>
</table>
