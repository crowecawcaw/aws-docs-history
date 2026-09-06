

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Security and compliance
<a name="dcm-security-n-compliance"></a>

Security and compliance is a shared responsibility between AMS Advanced and you, as our customer. AMS Advanced Direct Change mode does not change this shared responsibility.

## Security in Direct Change mode
<a name="dcm-security"></a>

AMS Advanced offers additional value with a prescriptive landing zone, a change management system, and access management. When using Direct Change mode, this responsibility model does not change. However, you should be aware of additional risks.

The Direct Change Mode "Update" role (see [Direct Change mode IAM roles and policies](dcm-get-started.md#dcm-gs-iam-roles-and-policies)) provides elevated permissions allowing the entity with access to it, to make changes to infrastructure resources of AMS-supported services within your account. With elevated permissions, varied risks exist depending on the resource, service, and actions, especially in situations where an incorrect change is made due to oversight, mistake, or lack of adherence to your internal process and control framework.

As per AMS Technical Standards, the following risks have been identified and recommendations are made as follows. Detailed information about AMS Technical Standards is available through AWS Artifact. To access AWS Artifact, contact your CSDM for instructions or go to [Getting Started with AWS Artifact](http://aws.amazon.com/artifact/getting-started).

**AMS-STD-001: Tagging**

<a name="AMS-STD-001"></a>
<table>
<thead>
  <tr><th>Standards</th><th>Does it break</th><th>Risks</th><th>Recommendations</th></tr>
</thead>
<tbody>
  <tr><td>All the AMS owned resources must have following key-value pair</td><td rowspan="2">Yes. Breaks for CloudFormation,CloudTrail, EFS, OpenSearch, CloudWatch Logs, SQS, SSM, Tagging api - as these services do not support the <code>aws:TagsKey</code> condition to restrict tagging for the AMS namespace.<br />Standard given in table <b>AMS-STD-003</b>, following, states that you can change AppId, Environment and AppName, but not for AMS-owned resources. Not achievable through IAM permissions.</td><td rowspan="4">Incorrect tagging of AMS resources may adversly impact the reporting, alerting and patching operations of your resources, on the AMS side.</td><td rowspan="4">Access must be restrticted to make any changes on the AMS default tagging requirements for anyone other than AMS teams.</td></tr>
  <tr><td>All the AMS-owned tags other than those listed above must have prefixes like <code>AMS*</code> or <code>MC*</code> in upper/lower/mix case.</td></tr>
  <tr><td>Any tag on AMS-owned stacks must not be deleted based on your change requests.</td><td>Yes. CloudFormation does not support the <code>aws:TagsKey</code> condition to restrict tags for the AMS namespace.</td></tr>
  <tr><td>You are not permitted to use AMS tag naming convention in your infrastructure as mentioned in table <b>AMS-STD-002</b>, next.</td><td>Yes. Breaks for CloudFormation, CloudTrail, Amazon Elastic File System (EFS), OpenSearch, CloudWatch Logs, Amazon Simple Queue Service (SQS), Amazon EC2 Systems Manager (SSM), Tagging API; these services do not support the <code>aws:TagsKey</code> condition to restrict tagging for the AMS namespace.</td></tr>
</tbody>
</table>


**AMS-STD-002: Identity and Access Management (IAM)**


| Standards | Does it break | Risks | Recommendations | 
| --- | --- | --- | --- | 
| 4.7 Actions, which bypass the change management process (RFC), must not be permitted such as starting or stopping of an instance, creation of S3 buckets or RDS instances, and so forth. Developer mode accounts and Self-Service Provisioned mode services (SSPS) are exempted as long as actions are performed within the boundaries of the assigned role. | Yes. The purpose of self service actions allow you to perform actions bypassing the AMS RFC system. | The secure access model is a core technical facet of AMS and an IAM user for console or programmatic access circumvents this access control. The IAM users access is not monitored by AMS change management. Access is logged in CloudTrail only. | The IAM user should be time-bounded and granted permissions based on least-privilege and need-to-know. | 

**AMS-STD-003: Network Security**

<a name="AMS-STD-003"></a>
<table>
<thead>
  <tr><th>Standards</th><th>Does it break</th><th>Risks</th><th>Recommendations</th></tr>
</thead>
<tbody>
  <tr><td>S2. Elastic IP on EC2 instances must be used only with a formal risk acceptance agreement, or with a valid use case by internal teams.</td><td>Yes. Self service actions allow you to associate and disassociate elastic IP addresses (EIP).</td><td>Adding an elastic IP to an instance exposes it to the Internet. This increases the risk of information disclosure and unauthorized activity.</td><td>Block any unnecessary traffic to that instance through security groups, and verify that your security groups are attached with the instance to ensure that it allows the traffic only as needed for business reasons.</td></tr>
  <tr><td>S14. VPC Peering and endpoint connections between accounts that belong to the same customer can be permitted.</td><td rowspan="2">Yes. Not possible through IAM policy.</td><td>Traffic leaving your AMS account is not monitored once egressing the account boundary.</td><td>We recommend peering only with AMS accounts that you own. If your use case requires this, use security groups and route tables to limit what traffic ranges, resources, and types can egress through the relevant connection.</td></tr>
  <tr><td>AMS base AMIs can be shared between AMS-managed and unmanaged accounts as long as we can verify that they are owned by the same AWS organization.</td><td>AMIs may contain sensitive data and it may be exposed to unintended accounts.</td><td>Share AMIs with only the account owned by your organization or validate the use-case and account information before sharing outside the organization.</td></tr>
</tbody>
</table>


**AMS-STD-007: Logging**

<a name="AMS-STD-007"></a>
<table>
<thead>
  <tr><th>Standards</th><th>Does it break</th><th>Risks</th><th>Recommendations</th></tr>
</thead>
<tbody>
  <tr><td>19. Any log can be forwarded from one AMS account to another AMS account of the same customer.</td><td rowspan="2">Yes. Potential insecurity for customer logs as verification of the customer accounts being in the same organization can not be achieved through IAM policy.</td><td rowspan="2">Logs may contain sensitive data and it may be exposed to unintended accounts.</td><td rowspan="2">Share logs with only accounts managed by your AWS Org, or validate the use-case and account information before sharing outside of your organization. We can verify this via multiple ways, check with your cloud service delivery manager (CSDM).</td></tr>
  <tr><td>20. Any log can be forwarded from AMS to a non-AMS account only if the non-AMS account is owned by the same AMS customer (by confirming that they are under the same AWS Organizations account or by matching the email domain with the customer's company name and PAYER linked account) using internal tools.</td></tr>
</tbody>
</table>


Work with your internal authorization and authentication team to control the permissions to the Direct Change mode roles accordingly.

## Compliance in Direct Change mode
<a name="dcm-compliance"></a>

Direct Change mode is compatible with both production and non-production workloads. It's your responsibility to ensure adherence to any compliance standards (for example, PHI, HIPAA, PCI), and to ensure that the use of Direct Change mode complies with your internal control frameworks and standards.