

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# AMS modes and applications or workloads
<a name="ams-modes-and-apps-ug"></a>

Consider operational and governance requirements for your applications when selecting the right mode, either by requesting a new application account or hosting the application in an existing application account. The selection of the appropriate AMS mode for each application or workload depends on the following factors:
+ The type of SDLC lifecycle function that the environment will provide (e.g., sandbox with unmoderated changes, UAT with some frequent changes, production with minimal changes and highly regulated)
+ The governance policies needed (enforced through SCPs at the OU level)
+ Operational Model (if you want to own the operational responsibility or want to outsource that to AMS)
+ The desired business outcomes, like time to operate in the cloud, and cost of operations. 

**Note**  
For a descriptions of the mode types per AMS service, see [Types of modes and accounts in AMS](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-modes-types.html).  
For real-world use cases of the different modes, see [Real world use cases for AMS modes](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-modes-and-use-cases.html)

The following table outlines key considerations for application owners to help decide on the most suitable AMS mode. Application owners should include an assessment phase ahead of application migration to fully understand which mode applies to their specific application. Example: For applications based on cloud-native services or serverless architecture, the best option could be to start building and iterating in Developer mode and deploy the final Infrastructure as Code using AMS Managed – SSP mode. In this case light re-factoring may be required to ensure that any CloudFormation templates created for automated deployment meet the ingest guidelines laid out by AMS. Additionally, any IAM permissions need to be approved by AMS Security to ensure they follow the least privilege model.

The AMS mode selected to host the application, can help enable you to build towards you desired cloud operating model.

**Note**  
More than one cloud operating model can existing in a single AMS Managed Landing Zone based on the different AMS modes selected to host the applications. 


<table>
<thead>
  <tr><th>Decision issues</th><th>Standard CM mode / OOD<b>*</b></th><th>AWS Service Catalog</th><th>Direct Change mode</th><th>Self-service provisioning</th><th>Developer mode</th><th>Customer Managed</th></tr>
</thead>
<tbody>
  <tr><td colspan="7">Operational readiness</td></tr>
  <tr><td>Logging, Monitoring and Event Management</td><td colspan="3">AMS responsible for all managed infrastructure</td><td>Customer responsible for Self-Service Provisioned Services (SSP)</td><td>Customer responsible for resources provisioned using developer IAM role outside AMS CM system</td><td rowspan="8">Customer responsible</td></tr>
  <tr><td>Continuity Management</td><td colspan="3">AMS responsibility to execute backup plan selected by customer</td><td>Customer responsible for Self-Service Provisioned Services (SSP)</td><td>Customer responsible for resources provisioned using developer IAM role outside AMS CM system</td></tr>
  <tr><td>Instance Level Access Management</td><td colspan="3">AMS-managed through one-way AD trust with on-prem domain. Requires managed infrastructure to join AMS domain</td><td>Not applicable</td><td>Customer responsible for resources provisioned using developer IAM role outside AMS CM system</td></tr>
  <tr><td>Security Management and Account Level Access Management</td><td colspan="3">AMS responsibility for all managed accounts</td><td>AMS responsible for all managed accounts</td><td>Customer responsible for resources provisioned using developer IAM role outside AMS CM system</td></tr>
  <tr><td>Patch Management</td><td colspan="3">AMS responsibility for all managed accounts</td><td>Customer responsible for Self-Service Provisioned Services (SSP)</td><td>Customer responsible for resources provisioned using developer IAM role outside AMS CM system</td></tr>
  <tr><td>Change Management</td><td colspan="3">AMS responsibility for all managed accounts</td><td>Customer responsible for Self-Service Provisioned Services (SSP)</td><td>Customer responsible for resources provisioned using developer IAM role outside AMS CM system</td></tr>
  <tr><td>Provisioning Management</td><td>Prescriptive and standardized for the provisioning options offered in AMS</td><td>Flexibility to directly use AWS service API for AWS Service Catalog following AMS prescriptive standards</td><td>Flexibility to directly use AWS service API following AMS prescriptive standards</td><td>Flexibility to directly use AWS service APIs for SSP services</td><td>Flexibility to directly use AWS service API for provisioning</td></tr>
  <tr><td>Incident Management and Audit</td><td colspan="4">AMS responsibile for all managed accounts</td><td>Customer responsible for resources provisioned using developer IAM role outside AMS Change Management System</td></tr>
  <tr><td>GuardRails and Shared infrastructure (Network) and Security Framework</td><td colspan="5">Prescriptive and standardized leveraging AMS Core Accounts</td><td>Flexible and bespoke leveraging AMS Core Accounts</td></tr>
  <tr><td colspan="7">Application readiness</td></tr>
  <tr><td>Application refactoring</td><td colspan="4">Light refactoring is needed</td><td>Light refactoring is needed (if provisioned using AMS Standard CM)</td><td>No need for refactoring</td></tr>
  <tr><td>Support for AWS services</td><td colspan="5">Limited to what is supported by AMS</td><td>Not limited</td></tr>
  <tr><td colspan="7">Business considerations</td></tr>
  <tr><td>Time to operational readiness</td><td colspan="3">Three to six months</td><td colspan="2">6 months + dependent on customer application operations competencies</td><td>6-18 months dependent on customer infrastructure and application operations competencies</td></tr>
  <tr><td>Costs</td><td colspan="3">$$$$</td><td>$$$</td><td>$$</td><td>$</td></tr>
  <tr><td>Application examples</td><td colspan="3">Webserver with 3 tier stack, apps with compliance and regulatory requirements</td><td>Webserver using API Gateway, containerized application leveraging ECS/EKS</td><td>Iterating/optimizing on Data Lake application that uses Lambda, Glue, Athena, etc</td><td>De-centralized accounts/applications like sandbox, third party managed applications</td></tr>
</tbody>
</table>


**\***Operations On Demand (OOD) has an offering for customers using the Standard CM mode to manage their changes through dedicated resourcing. For more details, see the [ Operations on Demand catalog of offerings](https://docs.aws.amazon.com/managedservices/latest/userguide/ood-catalog.html) and talk to your cloud service delivery manager (CSDM).

**Note**  
The price comparison between SSP mode and Developer mode assumes that the same AWS services are provisioned.

Comparing AMS Modes against business and IT objectives

![Chart comparing AMS modes by time to operationalize and governance level.](http://docs.aws.amazon.com/managedservices/latest/userguide/images/ams-modes-choosing-dcm.png)


As shown, if you are looking for a highly controlled and standardized governance model for you applications, then AMS-managed Standard Change, AWS Service Catalog, or Direct Change modes are the best fit. If you require a bespoke governance model with a focus on application innovation without the need for operational readiness, select Customer Managed mode. With Customer Managed mode, it could take you a longer time to operationalize you applications as you bear the responsibility to establish people, processes, and tools to support operational capabilities such as Incident Management, Configuration Management, Provisioning Management, Security Management, Patch Management, etc.