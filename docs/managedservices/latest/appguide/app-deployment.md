

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Application deployment in AMS
<a name="app-deployment"></a>

During onboarding, AWS Managed Services (AMS) works with you to determine the infrastructure that you need. 

The basic infrastructure includes an AWS virtual private cloud (VPC), communication security via an ADFS forest trust, the basic subnets (DMZ, Shared Services, and Private) mirrored across two availability zones and configured with a managed NAT, bastions, public load balancers, Direct Connect (DX), and required security. Your application resources will be deployed in your private, or customer-applications, subnet. You can learn more about a typical AMS architecture in the AWS Managed Services User Guide.

The infrastructure you deploy once the basics are done, should include all components for your applications and application development.

## Application deployment capabilities in AMS
<a name="app-dep-caps"></a>

Some of the ways you can deploy applications in AMS. Details on each method follow.


**Application Deployment Capabilities Examples**  

<table>
<thead>
  <tr><th>Method Name</th><th>Infrastructure Deployment</th><th>AMI or Key Element(s)</th><th>Application Install</th></tr>
</thead>
<tbody>
  <tr><td colspan="4"><b>Mutable Applications, AMS AMI</b></td></tr>
  <tr><td>Manual application deployment</td><td rowspan="3">Full stack CT or Tier and Tie CTs</td><td rowspan="3">AMS-provided AMI</td><td>Submit Access management CT, install application manually.</td></tr>
  <tr><td>UserData application deployment with application agent (i.e. Chef, Puppet, etc.)</td><td>Use provisioning CT with UserData scripting that installs an application agent, and that script/agent installs the application.</td></tr>
  <tr><td>UserData agentless application deployment (i.e. Ansible, Salt SSH, etc.)</td><td>Submit Access management CT, install application agent. Deploy application with application deploy tooling.</td></tr>
  <tr><td colspan="4"><b>Mutable Applications, Custom AMI</b></td></tr>
  <tr><td>Custom AMI application deployment (non-ASG)</td><td>Full stack CT or Tier and Tie CTs</td><td>Custom AMI. AMS AMI -&gt; customize with application deploy tooling agent -&gt; create EC2 instance (CT) -&gt; create AMI (CT).</td><td>Application deploy tooling (i.e. Chef), leveraging agents, deploys application.</td></tr>
  <tr><td>AWS Database Migration Service (DMS) application deployment</td><td>AWS DMS sync to existing AMS Relational Database stack.</td><td rowspan="2">Custom AMI</td><td>Customer or partner employs AWS Database Migration Service; AMS verifies AMS components on launch</td></tr>
  <tr><td>Workload Ingest application deployment</td><td>Partner-migrated instance/AMI and customer-initiated Workload Ingest CT.</td><td>Partner migrates instance, creates AMI in customer AMS-managed VPC; customer uses Workload Ingest CT to launch stack in AMS.<br />For details, see <a href="ams-workload-ingest.md">AMS Workload Ingest (WIGS)</a>.</td></tr>
  <tr><td colspan="4"><b>Immutable Applications</b></td></tr>
  <tr><td>Custom AMI application deployment (ASG)</td><td>Full stack CT or Tier and Tie CTs</td><td>AMS AMI -&gt; customize -&gt; create EC2 instance (CT) -&gt; create AMI (CT) -&gt; create Auto Scaling group.</td><td>Auto Scaling deploys application with the custom AMI<br />For details, see <a href="tier-and-tie-aog.md">Tier and Tie App Deployments in AMS</a>.</td></tr>
  <tr><td colspan="4"><b>Mutable or Immutable Applications</b></td></tr>
  <tr><td>Custom CloudFormation Template application deployment</td><td>CloudFormation template</td><td>AWS CloudFormation template -&gt; customize/prepare for AMS -&gt; Deployment | Ingestion | Stack from CloudFormation Template | Create (ct-36cn2avfrrj9v).</td><td>AMS deploys your application to your account using your custom CloudFormation template, and validates the application deployment.<br />For details, see <a href="ams-cfn-ingest.md">AMS CloudFormation ingest</a>.</td></tr>
  <tr><td>SQL Database Import</td><td>AMS operations (Other | Other CT)</td><td>On premise SQL database -&gt; .bak file -&gt; AMS RDS SQL database -&gt; Management | Other | Other | Create (ct-1e1xtak34nx76) for the import.</td><td>AMS imports your on-premises database to your AMS-managed RDS database. For details, see <a href="db-to-sql-rds.md">Database (DB) import to AMS RDS for Microsoft SQL Server</a>.</td></tr>
  <tr><td>Database Migration Service (DMS)</td><td>AMS operations (Multiple CTs)</td><td>On premise database -&gt; DMS replication instance -&gt; DMS replication subnet group -&gt; DMS target endpoint -&gt; DMS source endpoint -&gt; DMS replication task.</td><td>AMS imports your on-premises database to your AMS-managed S3 or target RDS database. For details, see <a href="service-create-dms.md">AWS Database Migration Service (AWS DMS)</a>.</td></tr>
  <tr><td>CodeDeploy application deployment</td><td>CodeDeploy</td><td>Application -&gt; CodeDeploy application -&gt; CodeDeploy deployment group -&gt; CodeDeploy deployment.</td><td>Depending on usage, In-place or Blue/Green application deployment. For details, see <a href="service-create-codedeploy.md">CodeDeploy requests</a>.</td></tr>
</tbody>
</table>
