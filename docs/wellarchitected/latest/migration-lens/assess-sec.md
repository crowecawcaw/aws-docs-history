

# Assess
<a name="assess-sec"></a>

 It's important to conduct a security review of the discovery tool used to assess on-premises inventory and understand how they work to ensure they don't introduce any vulnerabilities. During this phase, it's also key to review your current security tools and map them to their equivalents on AWS and to identify your compliance framework. 


| MIG-SEC-01: Have you performed a security review of the discovery tool you plan to use to assess your on-premises inventory? | 
| --- | 
|   | 

 Organizations have to meet different security and compliance standards. Ensure you fully understand the impact of any discovery tool against your security posture by assessing the risk profile of the discovery tool, how the data about on-premises environment is collected, where the data is stored, and how the stored data is secured. 

## MIG-SEC-BP-1.1 Understand the security credentials needed by the discovery tool
<a name="mig-sec-bp-1.1-understand-the-security-credentials-needed-by-the-discovery-tool"></a>

 This BP applies to the following best practice area: Identity and access management

### Implementation guidance
<a name="implementation-guidance-12"></a>

 **Suggestion 1.1.1**: Determine the required discovery tools and techniques. 

 Discovery tools, whether AWS native or partner solutions, typically leverage two types of discovery methodologies: agent-based discovery or agentless discovery. Agent-based tools require access to the workloads to install the discovery agent for data collection. Agentless discovery requires permission to scan the network and identify workloads. Identify the least privilege model and apply accordingly. 

 For more detail, see the following:  
+  [AWS Application Discovery Service FAQs](https://aws.amazon.com/application-discovery/faqs/) 
+  [Discovery, Planning, and Recommendation migration tool details](https://aws.amazon.com/prescriptive-guidance/migration-tools/migration-discovery-tools-details/#awsapplicationdiscovery) 

 **Suggestion 1.1.2:** Identify and safeguard credentials needed by discovery tools. 

 Follow the principle of least privilege, granting only the necessary permissions to discovery tools and their associated AWS Identity and Access Management (IAM) roles or users. Use a credential management system, such as AWS Secrets Manager, to limit sharing and proliferations of credentials. Additionally, limit the use of long-term credentials when possible. 

 For more detail, see the following:  
+  [Least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) 
+  [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) 

## MIG-SEC-BP-1.2 Understand how the discovery tool works
<a name="mig-sec-bp-1.2-understand-how-the-discovery-tool-works"></a>

 This BP applies to the following best practice areas: Infrastructure protection 

### Implementation guidance
<a name="implementation-guidance-13"></a>

 **Suggestion 1.2.1**: Understand the network requirements for discovery tools. 

 Discovery tools, whether AWS native or partner solutions, typically leverage 2 types of discovery methodologies: Agent based discovery or agentless discovery. These 2 methods use different ports and protocols to collect information. Once you choose a discovery tool, study the documentation to understand the networking and potential security and availability considerations. For example, if the tool uses a non-standard port, is that port reachable on the assets you want to assess. 

 For more detail, refer to the following information:  
+  [Agent and Agentless discovery tools](https://aws.amazon.com/application-discovery/faqs/) 
+  [Discovery, Planning, and Recommendation migration tool details](https://aws.amazon.com/prescriptive-guidance/migration-tools/migration-discovery-tools-details/#awsapplicationdiscovery) 

## MIG-SEC-BP-1.3 Understand the discovery tool's data security and apply appropriate controls
<a name="mig-sec-bp-1.3-understand-the-discovery-tools-data-security-and-apply-appropriate-controls"></a>

 This BP applies to the following best practice areas: Data protection 

### Implementation guidance
<a name="implementation-guidance-14"></a>

 **Suggestion 1.3.1:** Understand what data the discovery tool collects. 

 Discovery tools collect various pieces of data, such as server names, IP addresses, allocated and utilized resources, network ports, and applications installed on the machine. Organizations should try to limit the collection of data to only the minimum data types necessary and relevant to support migration planning. 

 **Suggestion 1.3.2**: Understand where the discovery data is stored. 

 Collected data from discovery tools is typically stored locally within a customer's data center or sent over the network directly to the tool vendor as a SaaS model. Understand the tool's data storage capabilities and vendor's security controls to verify that they align to your data management, handling, and storage policies. You can also collect the data and store it locally within your data center and only share redacted data with AWS or partners for analysis. 

 **Suggestion 1.3.3**: Understand how the data is encrypted in transit and at rest. 

 Different discovery tools come with different security controls when it comes to how data is encrypted in transit and at rest. Ensure this meets your organization's security policy requirements. 

 **Suggestion 1.3.4**: Get the necessary approval from your security team in your organization to install and use the discovery tool. 

 After deciding the right discovery tool to use, work with the security team in your organization to get the necessary approval to start using the tool. This process make take time, so plan accordingly. 

 For more detail, refer to the following information: 
+  [Selecting the discovery tool for your cloud migration](https://aws.amazon.com/blogs/architecture/selecting-the-appropriate-discovery-tool-for-your-cloud-migration/) 


| MIG-SEC-02: Have you reviewed and mapped your existing security tools and controls to equivalent AWS services? | 
| --- | 
|   | 

 Customers moving into AWS can leverage a comprehensive selection of AWS cloud-native security services. Before migrating to AWS, it is important to map your on-premise security tools and controls to those available in your AWS environment. This includes controls like identity and access management, perimeter security, encryption tools, network security, data security, vulnerability management tools, code scanning tools, and threat detection. 

## MIG-SEC-BP-2.1  Perform a tools mapping exercise
<a name="mig-sec-bp-2.1-perform-a-tools-mapping-exercise"></a>

 This BP applies to the following best practice areas: Infrastructure security 

### Implementation guidance
<a name="implementation-guidance-15"></a>

**Suggestion 2.1.1:** Understand the AWS Shared Responsibility Model.

Identify the security controls of resources hosted in AWS, keeping in mind the [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/) and how this model shifts based on the AWS service being used. While AWS is responsible for the security *of* the cloud, and the customer is responsible for security *in* the cloud, the customer needs to understand how both sides of the shared responsibility model align to any compliance and regulatory requirements. Review the security functionality and configuration options of individual AWS services within the security chapters of [AWS service documentation](https://docs.aws.amazon.com/security/). Customers can view a variety of security and compliance reports created by third-party auditors by using [AWS Artifact](https://docs.aws.amazon.com/artifact/latest/ug/what-is-aws-artifact.html).

 **Suggestion 2.1.2**: Map network security tools. 

 Map network security tools such as firewalls, IDS/IPS, deep packet inspection, and web application firewalls, and understand AWS native capabilities. Understand the difference between networking in AWS and on-premise data centers, as it is important to apply this to your design and tools selection. AWS native services can be complemented with AWS Partner services of choice through the [AWS Marketplace](https://aws.amazon.com/marketplace/search/?category=3141913d-a073-4452-8473-843f58081505) to reach a desired security posture. 

 For more detail, see the following:  
+  [Network and Application Protection](https://aws.amazon.com/free/security/#Network_and_Application_Protection) 
+  [Detection](https://aws.amazon.com/free/security/#Detection_) 

 **Suggestion 2.1.3**: Map operating system (OS) level security tools, including third-party tools. 

 Customers should understand if they can continue to use the existing OS level security tools in their self-managed EC2 instances or containers. Understand the technical and licensing limitations of porting those tools to AWS. For more detail, see [AWS Systems Manager FAQs](https://aws.amazon.com/systems-manager/faq/). 

 **Suggestion 2.1.4**: Map on-premises vulnerability management controls. 

 Map your on-premises vulnerability management security control policies and requirements to AWS workload architectures, service capabilities, and controls. 

 For more detail, see the following:  
+  [Amazon Inspector](https://aws.amazon.com/inspector/) 
+  [SEC06-BP01 Perform vulnerability management](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec_protect_compute_vulnerability_management.html) 
+  [Application Security partner tools](https://aws.amazon.com/marketplace/search/?searchTerms=application+security) 

 **Suggestion 2.1.5**: Map your on-premises data security control policies and requirements to AWS data and storage architectures, service capabilities, and controls. 

 Map data security tools and services, such as certificate management tools, key management, TLS certificates, encryption tools, and AWS Secret Manager to AWS service capabilities and controls. For more detail, see [Data Protection services](https://aws.amazon.com/free/security/#Detection_). 


| MIG-SEC-03: Do you have an established compliance framework? | 
| --- | 
|   | 

 Customers have distinct risk and compliance requirements, based on factors such as industry, geographical location, customer base, and governmental and regulatory authorities. The [AWS Compliance Program](https://aws.amazon.com/compliance/programs/) helps customers understand the robust controls in place at AWS to maintain security and compliance of the cloud. By tying together governance-focused, audit-friendly service features with applicable compliance or audit standards, [AWS Compliance Enablers](https://aws.amazon.com/compliance/resources/) build on traditional programs, helping customers to establish and operate in an AWS security control environment. 

## MIG-SEC-BP-3.1 Understand, establish, and implement compliance framework
<a name="mig-sec-bp-3.1-understand-establish-and-implement-compliance-framework"></a>

 This BP applies to the following best practice areas: Security foundations 

### Implementation guidance
<a name="implementation-guidance-16"></a>

 **Suggestion 3.1.1**: Identify your compliance requirements. 

 IT standards that AWS complies with are broken out by [Certifications and Attestations](https://aws.amazon.com/compliance/programs/#Certifications_.2F_Attestations.3A), [Laws, Regulations](https://aws.amazon.com/compliance/programs/#Laws_.2F_Regulations.3A) and [Privacy](https://aws.amazon.com/compliance/programs/#Privacy), and [Alignments and Frameworks](https://aws.amazon.com/compliance/programs/#Alignments_.2F_Frameworks.3A). Compliance certifications and attestations are assessed by third-party, independent auditors and result in a certification, audit report, or attestation of compliance. AWS customers remain responsible for complying with applicable compliance laws, regulations, and privacy programs. Compliance alignments and frameworks include published security or compliance requirements for a specific purpose, such as a specific industry or function. 

 For more detail, see the following:  
+  [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/) 
+  [AWS Customer Compliance Guides](https://aws.amazon.com/blogs/security/customer-compliance-guides-now-available-on-aws-artifact/) 

 **Suggestion 3.1.2**: Determine if you operate and store data in multiple countries and identify any geography-based compliance requirements.   

 An organization's compliance needs can vary depending on the city, state, country, or even Region. Work closely with your organization's compliance and legal teams to understand any regulatory or other compliance requirements, including data residency and [digital sovereignty](https://aws.amazon.com/compliance/digital-sovereignty/) requirements. 

 For more detail, see the following:  
+  [Compliance FAQs](https://aws.amazon.com/compliance/faq/) 
+  [Compliance Resources](https://aws.amazon.com/compliance/resources/) 
+  [Digital Sovereignty at AWS](https://aws.amazon.com/compliance/digital-sovereignty/) 

 **Suggestion 3.1.3**: Familiarize yourself with the compliance postures of the AWS services that make up your solution's architecture. 

 Security and compliance are a shared responsibility between AWS and the customer. Depending on the services deployed, this shared model can help relieve the customer's operational burden.  AWS is responsible for compliance of underlying service capabilities, while the customer is responsible for compliance of the specific implementations. Use AWS Artifact to look at compliance reports for various AWS services and assess what you as a customer are responsible for meeting in terms of compliance and what AWS as a service provider is responsible for. 

 For more detail, see the following:  
+  [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/) 
+  [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/) 
+  [AWS Artifact](https://aws.amazon.com/artifact/) 