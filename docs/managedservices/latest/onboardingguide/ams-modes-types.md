

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Types of modes and accounts in AMS
<a name="ams-modes-types"></a>

AWS Managed Services (AMS) modes can be defined as the ways of interacting with the AMS service under the specific governance framework for each mode. The landing zone differences, multi-account landing zone or MALZ and single-account landing zone or SALZ are noted. 

**Note**  
For details about application deployment and choosing the right AMS mode, see [AMS modes and applications or workloads](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-modes-and-apps-ug.html).  
For real-world use cases of the different modes, see [Real world use cases for AMS modes](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-modes-use-cases.html)

The following table provides descriptions of the modes per AMS service.


<table>
<thead>
  <tr><th>AMS feature</th><th>RFC mode (formerly Standard CM mode) / OOD<b>*</b></th><th>Direct Change mode</th><th>AWS Service Catalog</th><th>Self-service provisioning / Developer mode</th><th>Customer Managed</th></tr>
</thead>
<tbody>
  <tr><td>Landing Zone Configuration</td><td>MALZ and SALZ</td><td>MALZ and SALZ</td><td colspan="3">MALZ and SALZ</td></tr>
  <tr><td>Change Management</td><td>Change scheduling, review of manual changes, and change record</td><td>Same as RFC mode for high-risk changes like IAM or security groups</td><td colspan="3">None</td></tr>
  <tr><td>Logging, Monitoring, Guardrails, and Event Management</td><td colspan="3">Yes (supported resources)</td><td colspan="2">No</td></tr>
  <tr><td>Continuity management</td><td colspan="3">Yes (supported resources)</td><td>Not applicable / No</td><td>No</td></tr>
  <tr><td>Security management</td><td colspan="3">Instance level security controls and account level controls</td><td>Account level controls</td><td>AWS Org level controls</td></tr>
  <tr><td>Patch management</td><td colspan="3">Yes</td><td>Not applicable / No</td><td>No</td></tr>
  <tr><td>Incident and problem management</td><td colspan="3">Response and resolution SLA for AMS supported resources</td><td>Response SLA for resulting resources</td><td>No</td></tr>
  <tr><td>Reporting</td><td colspan="3">Yes</td><td colspan="2">No</td></tr>
  <tr><td>Service request management</td><td colspan="3">Yes</td><td>Support requests only</td><td>No</td></tr>
</tbody>
</table>


**\***Operations On Demand (OOD) has an offering for customers using the RFC mode to manage their changes through dedicated resourcing. For more details, see the [ Operations on Demand catalog of offerings](https://docs.aws.amazon.com/managedservices/latest/userguide/ood-catalog.html) and talk to your cloud service delivery manager (CSDM).

**Note**  
[Self-Service Provisioning mode in AMS](self-service-provisioning-section.md) and [AMS Advanced Developer mode](developer-mode-section.md) may both appear to be a suitable fit for an application that has complex architecture rooted in native AWS Services. When architecting workloads, you make trade-offs between operational excellence and agility, based on your business context. This is a good way to think about selecting SSP mode or Developer mode for your application. The selection may also change based on the SDLC phase of the application. For example: When the application is production-ready, then SSP mode maybe a more appropriate option due to stricter AMS guardrails in this mode. The guardrails are enforced in the form of preventative controls like RFC-based change control for IAM updates and SCPs at the application OU level. These business decisions can drive your engineering priorities. You might optimize to increase flexibility for application owners in "pre-prod" phase at the expense of governance and operational support. 

## MALZ architecture and associated AMS modes
<a name="ams-modes-and-malz"></a>

AMS multi-account landing zone (MALZ) gives you the option to automatically provision application accounts (or resource accounts) under the default Organizational Units (OU): Customer Managed OU, Managed OU, or Development OU. The infrastructure provisioned in the application accounts created under each of these OUs is subject to the specific AMS mode offered by those foundational OUs. It is common to find a mix of two or more modes in the same application account. For example: RFC mode and SSP mode can coexist in an AMS managed account that hosts pipeline architecture consisting of API Gateway and Lambda for trigger functions, and EC2, S3, and SQS for ingestion and orchestration. In this case, SSP mode would apply to Lambda and API Gateway.

Figure 1 presents how different modes are offered through the foundational OUs in AMS. When requesting a new application account in AMS, you must select the OU for the account.

MALZ architecture and associated AMS modes

![Organizational structure showing Management Account at top, four account types in middle, and application accounts with customer stacks at bottom.](http://docs.aws.amazon.com/managedservices/latest/onboardingguide/images/MALZ-high-level-(Mar2021).png)


AMS leverages the foundational OUs based on AWS best practices as a way to logically manage accounts using Service Control Policies (SCPs). This serves as a way to enforce the governance framework with each AMS mode. Any governance and security guardrails (in the form of SCPs) applied to the foundational OUs also get applied to the custom/child OUs automatically. Additional SCPs can be requested for the child OUs. It is important to understand that application accounts are not the same as modes. Modes are applied to the infrastructure provisioned within the accounts and define the operational responsibilities between AMS and customers.

Figure 1: MALZ architecture and associated AMS modes

![Table showing AMS modes with preventative and detective controls and customer governance support.](http://docs.aws.amazon.com/managedservices/latest/onboardingguide/images/ams-modes-guardrails-dcm.png)


**Note**  
"Restrictive" implies that you can request custom policies for these OUs, they are approved by AMS on a case-by-case basis to ensure they don’t interfere in AMS's capabilities to provide operational excellence. For a detailed list of AMS guardrails see [AMS Guardrails](https://docs.aws.amazon.com/managedservices/latest/userguide/security-mgmt.html#detective-rules) in the user guide.