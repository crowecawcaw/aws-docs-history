

# Viewing the security profile of a product with AWS Marketplace Vendor Insights
<a name="buyer-vendor-insights-view-profile"></a>

AWS Marketplace Vendor Insights gathers security data from sellers. A product's security profile displays updated information about the product's security, resiliency, compliance, and other factors needed for your assessment. This information supports buyers like you by helping you to procure trusted software that continuously meets industry standards. For each software as a service (SaaS) product that it assesses, AWS Marketplace Vendor Insights gathers the evidence-based information for multiple security controls.

**Topics**
+ [Dashboard in AWS Marketplace Vendor Insights](#dashboard-vendor-insights)
+ [Viewing the security profile of a SaaS product](#view-data)
+ [Understanding control categories](#control-categories)

## Dashboard in AWS Marketplace Vendor Insights
<a name="dashboard-vendor-insights"></a>

The dashboard presents the compliance artifacts and security control information for a software product that is gathered by AWS Marketplace Vendor Insights. Evidence-based information for all security [control categories](#control-category-sets) is provided such as a change in data residency or certification expiration. The consolidated dashboard provides compliance information changes. AWS Marketplace Vendor Insights removes the need for you to create additional questionnaires and use risk assessment software. With a consistently updated and validated dashboard, you can continuously monitor the software's security control after procurement.

## Viewing the security profile of a SaaS product
<a name="view-data"></a>

AWS Marketplace Vendor Insights helps you make decisions about a seller's software. AWS Marketplace Vendor Insights extracts data from a seller's evidence-based information across 10 control categories and multiple controls. You can view profile and summary information for a SaaS product on the dashboard or select control categories to learn more about data gathered. You must be subscribed to the product and granted access to view compliance information through the profile.

1. Sign in to the AWS Management Console and open the [AWS Marketplace console](https://console.aws.amazon.com/marketplace/).

1. Choose **Vendor Insights**.

1. From **Vendor Insights**, choose a product. 

1. On the **Profile detail** page, choose the **Security and compliance** tab.
**Note**  
A number in a red circle indicates the number of non-compliant controls.

1. For **Control categories**, choose the text under any of the listed categories to view more information. 
   + Choose the first control name (**Do you have a policy/procedure to ensure compliance with applicable legislative, regulatory and contractual requirements?**).
   + Read the information presented. You can also view reports from AWS Artifact third-party report or view exceptions from the auditor.
   + Select the product name in the navigation above to return to the **Product detail** page.

## Understanding control categories
<a name="control-categories"></a>

AWS Marketplace Vendor Insights provides you with evidence-based information from multiple controls within 10 control categories. AWS Marketplace Vendor Insights gathers the information from three sources: vendor production accounts, vendor self-assessment, and vendor ISO 27001 and SOC 2 Type II reports. For more information about these sources, see [AWS Marketplace Vendor Insights](buyer-vendor-insights.md).

The following list provides a description of each control category:

Access management  
Identifies, tracks, manages, and controls access to a system or application.

Application security  
Verifies if security was incorporated into the application when designing, developing, and testing it.

Audit, compliance, and security policy  
Evaluates an organization's adherence to regulatory requirements.

Business resiliency and continuity  
Evaluates the organization’s ability to quickly adapt to disruptions while maintaining business continuity.

Data security  
Protects data and assets.

End user device security  
Protects portable end user devices and the networks they are connected to from threats and vulnerabilities.

Human resources  
Evaluates the employee related division for handling of sensitive data during processes such as hiring, paying, and terminating employees.

Infrastructure security  
Protects critical assets from threats and vulnerabilities.

Risk management and incident response  
Evaluates the level of risk deemed acceptable and the steps taken to respond to risks and attacks.

Security and configuration policy  
Evaluates the security policies and security configurations that protect an organization's assets.

### Control category sets
<a name="control-category-sets"></a>

The following tables provide detailed information for each category with information about the values for each category gathered. The following list describes the type of information within each column of the table:
+ **Control set** – Controls are assigned to a control set, and each control reflects the security function of its category. Each category has multiple control sets.
+ **Control name** – Name of the policy or procedure. "Requires manual attestation" means written confirmation or documentation of the policy or procedure is required.
+ **Control description** – Questions, information, or documentation needed about this policy or procedure.
+ **Evidence extraction detail** – Information and context needed about the control to further obtain the data needed for this category.
+ **Sample value** – Example given for guidance to what a compliance value for this category might look like so that it's in accordance with regulatory standards.

**Topics**
+ [Control category sets](#control-category-sets)
+ [Access management controls](#access-management)
+ [Application security controls](#application-security)
+ [Audit and compliance controls](#audit-comp-controls)
+ [Business resiliency controls](#business-resiliency)
+ [Data security controls](#data-security-controls)
+ [End user device security controls](#end-user-device-security)
+ [Human resources controls](#human-resources)
+ [Infrastructure security controls](#infrastructure-security)
+ [Risk management and incident response controls](#risk-management-incident-response)
+ [Security and configuration policy controls](#security-configuration-policy)

### Access management controls
<a name="access-management"></a>

Access management controls identify, track, manage, and control access to a system or application. This table lists the values and descriptions for access management controls.



- ****Secure authentication****
  - **Control title:** Access Management 3.1.1 - Secure Authentication - Personal Data in UserId (Requires manual attestation) / **Control description:** Do you require personal data (other than name or email address) in the user ID? / **Evidence extraction detail:** Specify if personal data, other than name or email address, is required as a part of the user identifier. If yes, what data will be used? What use case is it used for? / **Sample value:** No
  - **Control title:** Access Management 3.1.2 - Secure Authentication - Application Supports Two Factor Authentication (Requires manual attestation) / **Control description:** Does the application support two-factor authentication? / **Evidence extraction detail:** Specify if two-factor authentication can be used with the application. If yes, what tools can be used? / **Sample value:** Yes
  - **Control title:** Access Management 3.1.3 - Secure Authentication - Account Lockout (Requires manual attestation) / **Control description:** Is the customer's account locked if there are multiple failed logins? / **Evidence extraction detail:** Specify if account lockout is enabled if there are multiple failed logins. If yes, specify the number of tries after which the account will be locked out. / **Sample value:** Yes. Account is locked out after 5 failed logins.

- ** **Credential management** **
  - **Control title:** Access Management 3.2.1 - Credential Management - Password Policy / **Control description:** Does the application have a strong password policy? / **Evidence extraction detail:** Specify if a strong password policy (for example, RequireUppercaseCharacters, RequireSymbols, or PasswordReusePrevention ) is present. / **Sample value:** Yes
  - **Control title:** Access Management 3.2.2 - Credential Management - Password Encryption / **Control description:** Does the password policy require sign-in credentials (password and user ID) to be encrypted in-transit and to be hashed with salt when stored? / **Evidence extraction detail:** Specify if credentials (password and user ID) are encrypted in-transit and, when stored, if the password is hashed with salt. If yes, can you provide more details? / **Sample value:** Yes, We use code to properly salt.
  - **Control title:** Access Management 3.2.3 - Credential Management - Secret Management / **Control description:** Do you use a secret management service? / **Evidence extraction detail:** Specify if there is a secret management service in place. If yes, can you provide more details? / **Sample value:** Yes. All credentials are stored in a secret management service. They are rotated periodically.
  - **Control title:** Access Management 3.2.4 - Credential Management - Credentials in Code (Requires manual attestation) / **Control description:** Are credentials included in the code? / **Evidence extraction detail:** Specify if credentials are included in the code. If yes, can you provide more details? / **Sample value:** No

- ** **Access to production environment** **
  - **Control title:** Access Management 3.3.1 - Access to Production Environment - Single Sign-on (Requires manual attestation) / **Control description:** Is SSO enabled to access the production environment? / **Evidence extraction detail:** Specify if SSO can be used with the application. If yes, what tool is used for SSO? / **Sample value:** Yes, Duo SSO
  - **Control title:** Access Management 3.3.2 - Access to Production Environment - Two Factor Authentication / **Control description:** Is two-factor authentication required to access the production or hosted environment? / **Evidence extraction detail:** Specify if two-factor authentication (2FA) is required for access to the production environment. If yes, what tool is used for 2FA? / **Sample value:** Yes, Yubikey
  - **Control title:** Access Management 3.3.3 - Access to Production Environment - Root User (Requires manual attestation) / **Control description:** Is root user used only by exception to access the production environment? / **Evidence extraction detail:** Specify that the root user is only used by exception. If yes, can you establish the cases it will be used for?<br /> / **Sample value:** Yes. Root user is used only for device management purposes. All such accesses are logged and monitored.
  - **Control title:** Access Management 3.3.4 - Access to Production Environment - Root User MFA / **Control description:** Does root user require multi-factor authentication (MFA)? / **Evidence extraction detail:** Specify if logging in as root user requires multi-factor authentication. If yes, what tool is used for MFA? / **Sample value:** Yes. Root users are required to use MFA to login. Their root credentials are distinct from their normal corporate credentials.
  - **Control title:** Access Management 3.3.5 - Access to Production Environment - Remote Access / **Control description:** Is remote access to the production environment secured using mechanisms such as encrypted channels or key based authentication? / **Evidence extraction detail:** If the application permits remote access, specify if the access is secure (for example, will key-based authentication be used and will communication be done over encrypted channels?) / **Sample value:** Yes. Remote access is used for device management purposes. We require MFA over an approved cryptographic channel when accessing the production environment remotely.

- ****Access control policy****
  - **Control title:** Access Management 3.4.1 - Access Control Policy - Least Privilege Access / **Control description:** Do you follow least privilege access policy for users to access the production environment? / **Evidence extraction detail:** Specify if least privileges are assigned to users. If no, how do you control access? / **Sample value:** Yes
  - **Control title:** Access Management 3.4.2 - Access Control Policy - Access Policy Review / **Control description:** Are all access policies in the production environment reviewed regularly? / **Evidence extraction detail:** Specify if all access policies are reviewed regularly. If yes, provide details on how often the policies are reviewed. / **Sample value:** Yes. All access policies are reviewed every 3 months.
  - **Control title:** Access Management 3.4.3 - Access Control Policy - Users and Security Policy Configuration (Requires manual attestation) / **Control description:** Does the application allow customers to configure users and their privileges? / **Evidence extraction detail:** Specify if customers can configure users (from the customer's and the vendor's end) that will have access to their environment. / **Sample value:** Yes
  - **Control title:** Access Management 3.4.4 - Access Control Policy - Logical Segmentation (Requires manual attestation)<br /> / **Control description:** Is there logical segmentation of application users? / **Evidence extraction detail:** Specify if there is a logical segmentation of users. / **Sample value:** Yes
  - **Control title:** Access Management 3.4.5 - Access Control Policy - Access Review upon Termination / **Control description:** Are all relevant access policies updated upon employee termination or change of role? / **Evidence extraction detail:** Specify if access policies are deleted or updated upon employee termination, or change of role. / **Sample value:** Yes

- ****Access logs****
  - **Control title:** Access Management 3.5.1 - Access Logs
  - **Control description:** Do you log activities performed by individual users in the production environment?
  - **Evidence extraction detail:** Specify if a user's (employee or customer) actions and activities in a production environment are logged. If yes, how long are the logs retained?
  - **Sample value:** Yes. Logs are retained for a year.



### Application security controls
<a name="application-security"></a>

Application security controls verify if security was incorporated into the application when designing, developing, and testing it. This table lists the values and descriptions for application security policy controls.



- ** **Secure software development lifecycle** **
  - **Control title:** Application Security 4.1.1 - Secure Software Development Lifecycle - Separate Environment / **Control description:** Is the development, test, and staging environment separate from the production environment? / **Evidence extraction detail:** Specify if the development, test, and staging environment is separate from the production environment. / **Sample value:** Yes
  - **Control title:** Application Security 4.1.2 - Secure Software Development Lifecycle - Secure Coding Practice / **Control description:** Do security engineers work with developers on security practices? / **Evidence extraction detail:** Specify if developers and security engineer work together on secure coding practices. / **Sample value:** Yes
  - **Control title:** Application Security 4.1.3 - Secure Software Development Lifecycle - Use of Customer Data in Test Environment (Requires manual attestation) / **Control description:** Is customer data ever used in the test, development, or QA environments? / **Evidence extraction detail:** Is customer data ever used in the test, development, or QA environments? If yes, what data is used and what is it used for? / **Sample value:** No
  - **Control title:** Application Security 4.1.4 - Secure Software Development Lifecycle - Secure Connection / **Control description:** Is SSL/TLS enabled for all web pages and communications that uses customer data? / **Evidence extraction detail:** Specify if a secure connection (such as SSL/TLS) is used for all communication with customer data. / **Sample value:** Yes
  - **Control title:** Application Security 4.1.5 - Secure Software Development Lifecycle - Image Backup / **Control description:** Are application image snapshots backed up? / **Evidence extraction detail:** Specify if image snapshots (such as systems supporting the application and systems hosting customer data) are backed up. If yes, is there a process to ensure that image snapshots containing scoped data are authorized before being snapped? Is access control implemented for the image snapshots? / **Sample value:** Yes. Images are backed up with customer's and management's approval.

- ****Application security review****
  - **Control title:** Application Security 4.2.1 - Application Security Review - Secure Code Review / **Control description:** Is secure code review done before each release? / **Evidence extraction detail:** Specify if a security code review is done before each release. / **Sample value:** Yes
  - **Control title:** Application Security 4.2.2 - Application Security Review - Penetration Test / **Control description:** Are penetration tests performed? Can we get reports of penetration testing? / **Evidence extraction detail:** Specify if penetration tests are performed on the application. If yes, can you share the last 3 reports as manual evidence? / **Sample value:** Yes
  - **Control title:** Application Security 4.2.3 - Application Security Review - Security Patches / **Control description:** Are all available high-risk security patches applied and verified regularly? / **Evidence extraction detail:** Specify if high-risk security patches are applied regularly. If yes, how often are they applied? / **Sample value:** Yes. Security patches are applied monthly.
  - **Control title:** Application Security 4.2.4 - Application Security Review - Vulnerability Scans on Applications / **Control description:** Are vulnerability scans performed against all internet-facing applications regularly and after significant changes? / **Evidence extraction detail:** Specify if vulnerability scans are performed on all internet-facing applications. If yes, how often are vulnerability scans done? Can we get a copy of the report? / **Sample value:** Yes. Vulnerability scans are performed monthly.
  - **Control title:** Application Security 4.2.5 - Application Security Review - Threats and Vulnerabilities Management / **Control description:** Are there processes to manage threat and vulnerability assessment tools and the data they collect? / **Evidence extraction detail:** Specify if there are processes to manage threat and vulnerability assessment tools and their findings. Could you provide more details on how threats and vulnerabilities are managed? / **Sample value:** Yes. All threats and vulnerabilities from different sources are aggregated in one portal. They are managed by severity.
  - **Control title:** Application Security 4.2.6 - Application Security Review - Anti Malware Scans / **Control description:** Is anti-malware scanning done against the network and systems hosting the application regularly? / **Evidence extraction detail:** Specify if anti-malware scanning is done against the network and systems hosting the application. If yes, how often is it done? Can you provide the report? / **Sample value:** Yes. Anti-malware scans are performed monthly.

- ****Application logs****
  - **Control title:** Application Security 4.3.1 - Application Logs - Application Logs / **Control description:** Are application logs collected and reviewed? / **Evidence extraction detail:** Specify if application logs are collected and reviewed. If yes, how long are the logs retained? / **Sample value:** Yes. Logs are retained for a year.
  - **Control title:** Application Security 4.3.2 - Application Logs - Access to Logs / **Control description:** Are operating system and application logs protected against modification, deletion, and/or inappropriate access? / **Evidence extraction detail:** Specify if operating system and application logs are protected against modification, deletion, and/or inappropriate access. In the event of a breach or incident, do you have processes in place to detect loss of application logs? / **Sample value:** Yes
  - **Control title:** Application Security 4.3.3 - Application Logs - Data Stored in Logs (Requires manual attestation) / **Control description:** Do you store customer's personally identifiable information (PII) in logs? / **Evidence extraction detail:** Specify if you store customer's personally identifiable information (PII) in logs. / **Sample value:** No. No PII data will be stored in the logs.

- ****Change control policy****
  - **Control title:** Application Security 4.4.1 - Change Control Policy - Functional and Resiliency Testing / **Control description:** Is functional and resiliency testing done before releasing a change? / **Evidence extraction detail:** Specify if functional and resiliency testing is done on the application before a new release. / **Sample value:** Yes
  - **Control title:** Application Security 4.4.2 - Change Control Policy - Change Control Procedures / **Control description:** Are change control procedures required for all changes to the production environment? / **Evidence extraction detail:** Specify if change control procedures are in place for all changes made in the production environment. / **Sample value:** Yes
  - **Control title:** Application Security 4.4.3 - Change Control Policy - Avoid Human Error/Risks in Production / **Control description:** Do you have a process in place to verify that human error and risks don't get pushed into production? / **Evidence extraction detail:** Specify that there's a process to verify that human error and risks don't get pushed into production. / **Sample value:** Yes
  - **Control title:** Application Security 4.4.4 - Change Control Policy - Document and Log Changes / **Control description:** Do you document and log changes that may impact services? / **Evidence extraction detail:** Specify if service-impacting changes are documented and logged. If yes, how long are the logs retained? / **Sample value:** Yes
  - **Control title:** Application Security 4.4.5 - Change Control Policy - Change Notification for Buyers (Requires manual attestation) / **Control description:** Is there a formal process to ensure customers are notified before changes being made which may impact their service? / **Evidence extraction detail:** Specify if customers will be notified before making changes that may impact their service. If yes, what is the SLA to notify customers about impacting changes? / **Sample value:** Yes. We notify customers 90 days before impacting changes.



### Audit and compliance controls
<a name="audit-comp-controls"></a>

Audit and compliance controls evaluates an organization's adherence to regulatory requirements. This table lists the values and descriptions for audit and compliance controls.



- ** **Certifications completed** **
  - **Control title:** Audit and Compliance 1.1.1 - Certifications Completed (Requires manual attestation)
  - **Control description:** List certifications that you have.
  - **Evidence extraction detail:** Specify which certifications you have.
  - **Sample value:** SOC2, ISO/IEC 27001

- ** **Certification in progress** **
  - **Control title:** Audit and Compliance 1.2.1 - Certification in Progress (Requires manual attestation)
  - **Control description:** List additional certificates that are currently in progress.
  - **Evidence extraction detail:** List any additional certificates that are currently being audited or reviewed with an estimated completion date.
  - **Sample value:** Yes. PCI certification is in progress (ETA Q2 2022).

- ** **Procedures ensuring compliance** **
  - **Control title:** Audit and Compliance 1.3.1 - Procedures ensuring Compliance - Procedures ensuring Compliance / **Control description:** Do you have a policy or procedure to ensure compliance with applicable legislative, regulatory, and contractual requirements? / **Evidence extraction detail:** Specify if you have a policy or procedure to ensure compliance with applicable legislative, regulatory, and contractual requirements. If yes, list details about the procedure and upload manual evidence. / **Sample value:** Yes. We uploaded documents such as SOC2, ISO/IEC 27001.
  - **Control title:** Audit and Compliance 1.3.2 - Procedures ensuring Compliance - Audits to Track Outstanding Requirements / **Control description:** Are audits completed to track outstanding regulatory and compliance requirements? / **Evidence extraction detail:** Specify if audits are done to track outstanding requirements. If yes, provide details. / **Sample value:** Yes, audits are done monthly to track outstanding requirements.
  - **Control title:** Audit and Compliance 1.3.3 - Procedures ensuring Compliance - Deviations and Exceptions (Requires manual attestation) / **Control description:** Do you have a process to handle deviations and exceptions from compliance requirements? / **Evidence extraction detail:** Specify if there is a process to handle exceptions or deviations from compliance requirements. If yes, provide details. / **Sample value:** Yes. We have a deviations log and reporting tools. We investigate every exception or deviation to prevent future occurrence.



### Business resiliency controls
<a name="business-resiliency"></a>

Business resiliency controls evaluate the organization’s ability to quickly adapt to disruptions while maintaining business continuity. This table lists the values and descriptions for business resiliency policy controls.



- ****Business resiliency****
  - **Control title:** Business Resiliency and Continuity 6.1.1 - Business Resiliency - Failover Tests (Requires manual attestation) / **Control description:** Are site fail-over tests performed at least annually? / **Evidence extraction detail:** Specify if fail-over tests are performed annually. If no, how often are they performed? / **Sample value:** Yes
  - **Control title:** Business Resiliency and Continuity 6.1.2 - Business Resiliency - Business Impact Analysis (Requires manual attestation) / **Control description:** Has a business impact analysis been conducted? / **Evidence extraction detail:** Specify if a business impact analysis was done. If yes, when was it last completed? Provide details on the analysis conducted. / **Sample value:** Yes. A business impact analysis was completed 6 months ago.
  - **Control title:** Business Resiliency and Continuity 6.1.3 - Business Resiliency - Dependencies on Third-Party Vendors (Requires manual attestation) / **Control description:** Are there any dependencies on critical third-party service providers (besides a cloud service provider)? / **Evidence extraction detail:** Specify if there is any dependency on third-party vendors (besides a cloud service provider). If yes, can you provide details on the vendors? / **Sample value:** No
  - **Control title:** Business Resiliency and Continuity 6.1.4 - Business Resiliency - Third-Party Continuity and Recovery Tests (Requires manual attestation) / **Control description:** Do you require third-party vendors to have their own disaster recovery processes and exercises? / **Evidence extraction detail:** Specify if third-party vendors must have their own disaster recovery processes and exercises. / **Sample value:** Not applicable in this sample.
  - **Control title:** Business Resiliency and Continuity 6.1.5 - Business Resiliency - Third-Party Vendors Breach of Contract (Requires manual attestation) / **Control description:** Do contracts with critical service providers include a penalty or remediation clause for breach of availability and continuity Sold and Shipped by Amazon (SSA)? / **Evidence extraction detail:** Are penalty or remediation clauses for breach of availability and continuity included in contracts with third-party vendors? / **Sample value:** Not applicable in this sample.
  - **Control title:** Business Resiliency and Continuity 6.1.6 - Business Resiliency - Health of the System / **Control description:** Do you have monitors or alerts to understand the health of the system? / **Evidence extraction detail:** Specify if monitors or alerts are in place to understand the health of the system. / **Sample value:** Yes

- ** **Business continuity** **
  - **Control title:** Business Resiliency and Continuity 6.2.1 - Business Continuity - Business Continuity Policies/Procedures / **Control description:** Are formal business continuity procedures developed and documented? / **Evidence extraction detail:** Specify if formal procedures are developed and maintained for business continuity. If yes, provide more details on the procedures. / **Sample value:** Yes
  - **Control title:** Business Resiliency and Continuity 6.2.2 - Business Continuity - Response and Recovery Strategies / **Control description:** Are specific response and recovery strategies defined for the prioritized activities? / **Evidence extraction detail:** Specify if recovery and response strategies are developed for customer activities and services. / **Sample value:** Yes
  - **Control title:** Business Resiliency and Continuity 6.2.3 - Business Continuity - Business Continuity Tests / **Control description:** Do you perform recovery tests to ensure business continuity? / **Evidence extraction detail:** Specify if you perform recovery tests to ensure business continuity in case of a failure. / **Sample value:** Yes. In case of a failure, systems for business continuity will be activated within 2 hours.
  - **Control title:** Business Resiliency and Continuity 6.2.4 - Business Continuity - Availability Impact in Multi-Tenancy Environments (Requires manual attestation) / **Control description:** Do you limit a buyer's ability to impose load that may impact availability for other users of your system? / **Evidence extraction detail:** Specify if one buyer's load can impact availability for another buyer. If yes, what is the threshold until which there will be no impact? If no, can you provide more details on how you ensure services are not impacted during peak usage and above? / **Sample value:** Yes. Threshold not available for this sample.

- ****Application availability****
  - **Control title:** Business Resiliency and Continuity 6.3.1 - Application Availability - Availability Record (Requires manual attestation) / **Control description:** Were there any significant issues related to reliability or availability in the last year? / **Evidence extraction detail:** Specify if there were any significant issues related to reliability or availability in the last year. / **Sample value:** No
  - **Control title:** Business Resiliency and Continuity 6.3.2 - Application Availability - Scheduled Maintenance Window (Requires manual attestation) / **Control description:** Is downtime expected during scheduled maintenance? / **Evidence extraction detail:** Specify if there is a scheduled maintenance window during which services might be down. If yes, how long is the downtime? / **Sample value:** No
  - **Control title:** Business Resiliency and Continuity 6.3.3 - Application Availability - Online Incident Portal (Requires manual attestation) / **Control description:** Is there an online incident response status portal that outlines planned and unplanned outages? / **Evidence extraction detail:** Specify if there is an incident status portal that outlines planned and unplanned outages. If yes, provide details on how a customer can access it. How long after the outage will the portal be updated? / **Sample value:** Yes. The customer can access details through example.com.
  - **Control title:** Business Resiliency and Continuity 6.3.4 - Application Availability - Recovery Time Objective (Requires manual attestation) / **Control description:** Is there a specific recovery time objective (RTO)? / **Evidence extraction detail:** Specify if there is a recovery time objective (RTO). If yes, can you provide the RTO? / **Sample value:** Yes, a 2 hour RTO.
  - **Control title:** Business Resiliency and Continuity 6.3.5 - Application Availability - Recovery Point Objective (Requires manual attestation) / **Control description:** Is there a specific recovery point objective (RPO)? / **Evidence extraction detail:** Specify if there is a recovery point objective (RPO). If yes, can you provide the RPO? / **Sample value:** Yes, a 1 week RPO.



### Data security controls
<a name="data-security-controls"></a>

Data security controls protect data and assets. This table lists the values and descriptions for data security controls.



- ** **Customer data ingested** **
  - **Control title:** Data Security 2.1.1 - Customer Data Ingested (Requires manual attestation)
  - **Control description:** Create a list of data needed from customers for product functionality.
  - **Evidence extraction detail:** Describe all data consumed from customers. Specify if sensitive or confidential data is consumed.
  - **Sample value:** No sensitive and confidential data is consumed. This product only consumes non-sensitive information such as logs from applications, infrastructure, and AWS services. (AWS CloudTrail, AWS Config, VPC Flow Logs)

- ** **Data storage location** **
  - **Control title:** Data Security 2.2.1 - Data Storage Location (Requires manual attestation)
  - **Control description:** Where is customer data stored? List the countries and regions where data is stored.
  - **Evidence extraction detail:** Specify the list of countries and regions where data is stored.
  - **Sample value:** Ohio (US), Oregon (US), Ireland (EU)

- ****Access control****
  - **Control title:** Data Security 2.3.1 - Access Control - Employee Access (Requires manual attestation) / **Control description:** Do employees have access to unencrypted customer data? / **Evidence extraction detail:** Specify if employees have access to unencrypted customer data. If yes, explain briefly why they need access. If no, explain briefly how you control access. / **Sample value:** No, all data is encrypted when stored. Employees won't have access to customer data but only data about their usage.
  - **Control title:** Data Security 2.3.2 - Access Control - Mobile Application (Requires manual attestation) / **Control description:** Can customers access their data through a mobile application? / **Evidence extraction detail:** Specify if customers can access their data using a mobile application. If yes, provide more details. How do customers sign in? Are credentials cached by the application? How often are tokens refreshed? / **Sample value:** No, service can't be accessed using a mobile application.
  - **Control title:** Data Security 2.3.3 - Access Control - Countries Data is Transmitted to (Requires manual attestation) / **Control description:** Is customer data transmitted to countries outside the origin? / **Evidence extraction detail:** Is customer data transmitted to countries outside the origin? If yes, specify the list of countries where customer data is transmitted or received. / **Sample value:** No
  - **Control title:** Data Security 2.3.4 - Access Control - Is Data Shared with Third Party Vendors (Requires manual attestation) / **Control description:** Is customer data shared with third-party vendors (other than cloud service providers)? / **Evidence extraction detail:** Is customer data shared with third- party vendors? If yes, specify the list of third-party vendors and their countries or Region where you provide customer data. / **Sample value:** No
  - **Control title:** Data Security 2.3.5 - Access Control - Security Policy related to Third Party Vendors / **Control description:** Do you have policies or procedures in place to ensure that third-party vendors maintain the confidentiality, availability, and integrity of customer data? / **Evidence extraction detail:** Specify if you have policies or procedures in place to ensure that third-party vendors maintain the confidentiality, availability, and integrity of customer data. If yes, upload a manual or document of the policies or procedures. / **Sample value:** Not applicable in this sample.

- ** **Data encryption** **
  - **Control title:** Data Security 2.4.1 - Data Encryption - Data Encryption at Rest / **Control description:** Is all data encrypted at rest? / **Evidence extraction detail:** Specify if all data is encrypted at rest. / **Sample value:** Yes
  - **Control title:** Data Security 2.4.2 - Data Encryption - Data Encryption in Transit / **Control description:** Is all data encrypted in-transit? / **Evidence extraction detail:** Specify if all data is encrypted in-transit. / **Sample value:** Yes
  - **Control title:** Data Security 2.4.3 - Data Encryption - Strong Algorithms (Requires manual attestation) / **Control description:** Do you use strong encryption algorithms? / **Evidence extraction detail:** Do you use strong encryption algorithms? If yes, specify what encryption algorithms (such as, RSA, AES 256) are used. / **Sample value:** Yes. AES 256 is used for encrypting the data.
  - **Control title:** Data Security 2.4.4 - Data Encryption - Unique Encryption Key (Requires manual attestation) / **Control description:** Are customers provided with the ability to generate a unique encryption key? / **Evidence extraction detail:** Can customers provide or generate their own unique encryption keys? If yes, please provide more details and upload evidence. / **Sample value:** Yes
  - **Control title:** Data Security 2.4.5 - Data Encryption - Encryption Keys Access (Requires manual attestation) / **Control description:** Are employees prevented from accessing a customer's encryption keys? / **Evidence extraction detail:** Specify if your employees are prevented from accessing a customer's encryption keys. If no, explain why they have access to customer keys. If yes, explain how access is controlled. / **Sample value:** Yes. Cryptographic keys are securely stored and periodically rotated. Employees don't have access to these keys.

- ** **Data storage & classification** **
  - **Control title:** Data Security 2.5.1 - Data Storage & Classification - Data Backup / **Control description:** Do you back up customer data? / **Evidence extraction detail:** Specify if you back up customer data. If yes, describe your back up policy (including details about how often backup occurs, where the backup is stored, backup encryption and redundancy.) / **Sample value:** Yes, backup is done every three months. Backup is encrypted and stored in the same region as the customer data. The customer's support engineer has access to restore the backup but not the data in the backup.
  - **Control title:** Data Security 2.5.2 - Data Storage & Classification - Data Access Control Policy / **Control description:** Do you implement appropriate access controls for stored customer data? Provide your access control policies. / **Evidence extraction detail:** Specify if appropriate access controls (such as RBAC) are implemented for stored customer data. Provide more details and manual evidence on how you control access to the data. / **Sample value:** Yes. The least privilege access controls are implemented to restrict access to customer data.
  - **Control title:** Data Security 2.5.3 - Data Storage & Classification - Transaction Data (Requires manual attestation) / **Control description:** Are the customer's transaction details (such as payment card information and information about the groups conducting transactions) stored in a perimeter zone? / **Evidence extraction detail:** Specify if the customer's transaction details (such as payment card information and information about the groups conducting transactions) will be stored in a perimeter zone. If yes, explain why it needs to be stored in the perimeter zone. / **Sample value:** No
  - **Control title:** Data Security 2.5.4 - Data Storage & Classification - Information Classification / **Control description:** Is customer data classified according to legal or regulatory requirements, business value, and sensitivity to unauthorized disclosure or modification? / **Evidence extraction detail:** Specify if customer data is classified by sensitivity. If yes, upload manual evidence of this classification. / **Sample value:** Yes
  - **Control title:** Data Security 2.5.5 - Data Storage & Classification - Data Segmentation (Requires manual attestation) / **Control description:** Is data segmentation and separation capability between customers provided? / **Evidence extraction detail:** Specify if the data for different customers is segmented. If no, explain mechanisms you have to protect data from cross contamination. / **Sample value:** Yes

- ****Data retention****
  - **Control title:** Data Security 2.6.1 - Data Retention (Requires manual attestation)
  - **Control description:** How long do you retain data?
  - **Evidence extraction detail:** Specify the duration of data retention. If the retention period differs by data classification and sensitivity, can you provide details on each retention period?
  - **Sample value:** 6 months

- ** **Data retention after buyers unsubscribe** **
  - **Control title:** Data Security 2.6.2 - Data Retention after Client's Unsubscribe (Requires manual attestation)
  - **Control description:** How long do you retain data after buyers unsubscribe?
  - **Evidence extraction detail:** Specify the duration of data retention after customers unsubscribe.
  - **Sample value:** 3 months



### End user device security controls
<a name="end-user-device-security"></a>

End user device security controls protect portable end user devices and the networks they are connected to from threats and vulnerabilities. This table lists the values and descriptions for end user device security policy controls.



- ****Asset/software inventory****
  - **Control title:** End User Device Security 7.1.1 - Asset/Software Inventory - Asset Inventory / **Control description:** Is the asset inventory list updated periodically? / **Evidence extraction detail:** Specify if an asset inventory is maintained. If yes, how often is it updated? / **Sample value:** Yes. Inventory is updated weekly.
  - **Control title:** End User Device Security 7.1.2 - Asset/Software Inventory - Software and Applications Inventory / **Control description:** Are all installed software platforms and applications on scoped systems inventoried? / **Evidence extraction detail:** Specify if inventory of all installed software and applications is maintained. If yes, how often is it updated? / **Sample value:** Yes. Inventory is updated weekly.

- ****Asset security****
  - **Control title:** End User Device Security 7.2.1 - Asset Security - Security Patches / **Control description:** Are all available high-risk security patches applied and verified at least monthly on all end user devices? / **Evidence extraction detail:** Specify if all high risk security patches are applied at least monthly. If no, how often is it applied? Can you provide more details on how you manage patching? / **Sample value:** Yes. We have a security team that performs this process bi-weekly.
  - **Control title:** End User Device Security 7.2.2 - Asset Security - Endpoint Security / **Control description:** Do you have endpoint security? / **Evidence extraction detail:** Specify if endpoint security is installed on all devices. If yes, can you provide more details on the tool and how it is maintained? / **Sample value:** Yes. Our security team handles this bi-weekly using internal tools.
  - **Control title:** End User Device Security 7.2.3 - Asset Security - Maintenance and Repair of Assets (Requires manual attestation) / **Control description:** Is maintenance and repair of organizational assets performed and logged, with approved and controlled tools? / **Evidence extraction detail:** Specify if maintenance and repair of assets is performed and logged with controlled tools. If yes, could you provide more details on how it is managed? / **Sample value:** Yes. All maintenance of devices is logged. This maintenance does not lead to downtime.
  - **Control title:** End User Device Security 7.2.4 - Asset Security - Access Control for Devices / **Control description:** Do the devices have access control enabled? / **Evidence extraction detail:** Specify if devices have access controls (such as RBAC) enabled. / **Sample value:** Yes. Least privilege access is implemented for all devices.

- ****Device logs****
  - **Control title:** End User Device Security 7.3.1 - Device Logs - Sufficient Details in Logs (Requires manual attestation) / **Control description:** Are sufficient details logged in operating system and device logs to support incident investigation? / **Evidence extraction detail:** Specify if sufficient details (like successful and failed login attempts and changes to sensitive configuration settings and files) are included in the logs to support incident investigation. If no, provide more details on how you handle incident investigations. / **Sample value:** Yes
  - **Control title:** End User Device Security 7.3.2 - Device Logs - Access to Device Logs / **Control description:** Are device logs protected against modification, deletion, and/or inappropriate access? / **Evidence extraction detail:** Specify if device logs are protected against modification, deletion, and/or inappropriate access. If yes, can you provide details on how you enforce it? / **Sample value:** Yes. Changes to logs are enforced by access control. All changes to logs lead to an alert.
  - **Control title:** End User Device Security 7.3.3 - Device Logs - Log Retention (Requires manual attestation) / **Control description:** Are logs retained for sufficient time to investigate an attack? / **Evidence extraction detail:** How long will the logs be retained? / **Sample value:** Yes, 1 year.

- ****Mobile device management****
  - **Control title:** End User Device Security 7.4.1 - Mobile Device Management - Mobile Device Management Program / **Control description:** Is there a mobile device management program? / **Evidence extraction detail:** Specify if there is a mobile device management program. If yes, please specify what tool is used for mobile device management. / **Sample value:** Yes. We use internal tools.
  - **Control title:** End User Device Security 7.4.2 - Mobile Device Management - Access Production Environment from Private Mobile Devices (Requires manual attestation) / **Control description:** Are staff prevented from accessing the production environment by using unmanaged private mobile devices? / **Evidence extraction detail:** Specify if employees are prevented from accessing the production environment by using unmanaged private mobile devices. If no, how do you enforce this control? / **Sample value:** Yes
  - **Control title:** End User Device Security 7.4.3 - Mobile Device Management - Access Customer Data from Mobile Devices (Requires manual attestation) / **Control description:** Are employees prevented from using unmanaged private mobile devices to view or process customer data? / **Evidence extraction detail:** Specify if employees are prevented from accessing customer data by using unmanaged mobile devices. If no, what is the use case for allowing access? How do you monitor access? / **Sample value:** Yes



### Human resources controls
<a name="human-resources"></a>

Human resources controls evaluate the employee related division for handling of sensitive data during processes such as hiring, paying, and terminating employees. This table lists the values and descriptions for human resources policy controls.



- ****Human resources policy****
  - **Control title:** Human Resources 9.1.1 - Human Resources Policy - Background Screening for Employees / **Control description:** Is background screening done before employment? / **Evidence extraction detail:** Specify if background screening is done for all employees before employment. / **Sample value:** Yes
  - **Control title:** Human Resources 9.1.2 - Human Resources Policy - Employee Agreement / **Control description:** Is an employment agreement signed before employment? / **Evidence extraction detail:** Specify if an employment agreement is signed before employment. / **Sample value:** Yes
  - **Control title:** Human Resources 9.1.3 - Human Resources Policy - Security Training for Employees / **Control description:** Do all employees undergo security awareness training regularly? / **Evidence extraction detail:** Specify if employees undergo security training regularly. If yes, how often do they undergo security training? / **Sample value:** Yes. They undergo security training annually.
  - **Control title:** Human Resources 9.1.4 - Human Resources Policy - Disciplinary Process for Non Compliance of Policies / **Control description:** Is there a disciplinary process for non-compliance of human resource policies? / **Evidence extraction detail:** Specify if there is a disciplinary process for non-compliance of human resource policies. / **Sample value:** Yes
  - **Control title:** Human Resources 9.1.5 - Human Resources Policy - Background Checks for Contractors/Subcontractors (Requires manual attestation) / **Control description:** Are background checks performed for third-party vendors, contractors, and subcontractors? / **Evidence extraction detail:** Specify if background checks are done for third-party vendors, contractors, and subcontractors. If yes, is the background check done regularly? / **Sample value:** Yes. Background check is done annually.
  - **Control title:** Human Resources 9.1.6 - Human Resources Policy - Return of Assets upon Termination / **Control description:** Is there a process to verify return of constituent assets upon termination? / **Evidence extraction detail:** Specify if there is a process to verify return of constituent assets upon employee termination. / **Sample value:** Yes



### Infrastructure security controls
<a name="infrastructure-security"></a>

Infrastructure security controls protect critical assets from threats and vulnerabilities. This table lists the values and descriptions for infrastructure security policy controls.



- ****Physical security****
  - **Control title:** Infrastructure Security 8.1.1 - Physical Security - Physical Access to Facilities / **Control description:** Are individuals that require access to assets in-person (such as buildings, vehicles, or hardware) required to provide ID and any necessary credentials? / **Evidence extraction detail:** Specify if individuals that require access to assets in-person (such as buildings, vehicles, hardware) are required to provide ID and any necessary credentials. / **Sample value:** Yes
  - **Control title:** Infrastructure Security 8.1.2 - Physical Security - Physical Security and Environmental Controls in Place / **Control description:** Are physical security and environmental controls in place in the data center and office buildings? / **Evidence extraction detail:** Specify if physical security and environment controls are in place for all the facilities. / **Sample value:** Yes
  - **Control title:** Infrastructure Security 8.1.3 - Physical Security - Visitor Access (Requires manual attestation) / **Control description:** Do you record visitor access? / **Evidence extraction detail:** If visitors are permitted in the facility, are visitor access logs maintained? If yes, how long are the logs retained? / **Sample value:** Yes. Logs will be maintained for a year.

- ****Network security****
  - **Control title:** Infrastructure Security 8.2.1 - Network Security - Disable Unused Ports and Services (Requires manual attestation) / **Control description:** Are all unused ports and services disabled from the production environment and systems? / **Evidence extraction detail:** Specify if all unused ports and services are disabled from the production environment and systems. / **Sample value:** Yes
  - **Control title:** Infrastructure Security 8.2.2 - Network Security - Use of Firewalls / **Control description:** Are firewalls used to isolate critical and sensitive systems into network segments separate from network segments with less sensitive systems? / **Evidence extraction detail:** Specify if firewalls are used to isolate critical and sensitive segments from segments with less sensitive systems. / **Sample value:** Yes
  - **Control title:** Infrastructure Security 8.2.3 - Network Security - Firewall Rules Review / **Control description:** Are all firewalls rules reviewed and updated regularly? / **Evidence extraction detail:** How often are firewall rules reviewed and updated? / **Sample value:** Yes. Firewall rules are updated every 3 months.
  - **Control title:** Infrastructure Security 8.2.4 - Network Security - Intrusion Detection/Prevention Systems / **Control description:** Are intrusion detection and prevention systems deployed in all sensitive network zones and wherever firewalls are enabled? / **Evidence extraction detail:** Specify if intrusion detection and prevention systems are enabled in all sensitive network zones. / **Sample value:** Yes
  - **Control title:** Infrastructure Security 8.2.5 - Network Security - Security and Hardening Standards / **Control description:** Do you have security and hardening standards in place for network devices? / **Evidence extraction detail:** Specify if you have security and hardening standards in place for network devices. If yes, can you provide more details (including details about how often these standards are implemented and updated)? / **Sample value:** Yes. Security and hardening standards are implemented on network devices monthly.

- ****Cloud services****
  - **Control title:** Infrastructure Security 8.3.1 - Cloud Services - Platforms Used to Host Application (Requires manual attestation)
  - **Control description:** List the cloud platforms you use for hosting your application.
  - **Evidence extraction detail:** Specify which cloud platforms you use for hosting your application.
  - **Sample value:** AWS



### Risk management and incident response controls
<a name="risk-management-incident-response"></a>

Risk management and incident response controls evaluate the level of risk deemed acceptable and the steps taken to respond to risks and attacks. This table lists the values and descriptions for risk management and incident response policy controls.



- ****Risk assessment****
  - **Control title:** Risk Management/Incident Response 5.1.1 - Risk Assessment - Address and Identify Risks / **Control description:** Is there a formal process focused on identifying and addressing risks of disruptive incidents to the organization? / **Evidence extraction detail:** Specify if there is a process to identify and address risks that cause disruptive incidents for the organization. / **Sample value:** Yes
  - **Control title:** Risk Management/Incident Response 5.1.2 - Risk Assessment - Risk Management Process / **Control description:** Is there a program or process to manage the treatment of risks identified during assessments? / **Evidence extraction detail:** Specify if there is a program or process to manage risks and their mitigations. If yes, can you provide more details about the risk management process? / **Sample value:** Yes. We regularly review and remediate issues to address non-conformities. The following information is identified for any issue that affects our environment: <br /> • Details of issue identified <br /> • Root cause <br /> • Compensating controls <br /> • Severity <br /> • Owner <br /> • Near term path forward <br /> • Long term path forward
  - **Control title:** Risk Management/Incident Response 5.1.3 - Risk Assessment - Risk Assessments / **Control description:** Are risk assessments done frequently? / **Evidence extraction detail:** Are risk assessments done frequently? If yes, specify the frequency of risk assessments. / **Sample value:** Yes. Risk assessments are completed every 6 months.
  - **Control title:** Risk Management/Incident Response 5.1.4 - Risk Assessment - Third-Party Vendors Risk Assessment / **Control description:** Are risk assessments performed for all third-party vendors? / **Evidence extraction detail:** Specify if risk assessments are performed for all third-party vendors. If yes, how often? / **Sample value:** Not applicable in this sample.
  - **Control title:** Risk Management/Incident Response 5.1.5 - Risk Assessment - Risk Reassessment when Contract Changes / **Control description:** Are risk assessments performed when service delivery or contract changes occur? / **Evidence extraction detail:** Specify if risk assessments will be performed every time a service delivery or contract changes. / **Sample value:** Not applicable in this sample.
  - **Control title:** Risk Management/Incident Response 5.1.6 - Risk Assessment - Accept Risks (Requires manual attestation) / **Control description:** Is there a process for management to knowingly and objectively accept risks and approve action plans? / **Evidence extraction detail:** Specify if there is a process for management to understand and accept risks, and to approve action plans and a time line to fix a risk-related issue. Does the process include providing details of the metrics behind each risk to the management? / **Sample value:** Yes. Details about risk severity and the potential issues if it's not mitigated are provided to management before they approve a risk.
  - **Control title:** Risk Management/Incident Response 5.1.7 - Risk Assessment - Risk Metrics (Requires manual attestation) / **Control description:** Do you have measures in place to define, monitor, and report risk metrics? / **Evidence extraction detail:** Specify if there is a process to define, monitor, and report risk metrics. / **Sample value:** Yes

- ****Incident management****
  - **Control title:** Risk Management/Incident Response 5.2.1 - Incident Management - Incident Response Plan / **Control description:** Is there a formal Incident Response Plan? / **Evidence extraction detail:** Specify if there is a formal Incident Response Plan. / **Sample value:** Yes
  - **Control title:** Risk Management/Incident Response 5.2.2 - Incident Management - Contact to Report Security Incidents (Requires manual attestation) / **Control description:** Is there a process for customers to report a security incident? / **Evidence extraction detail:** Specify if there is a process for customers to report a security incident. If yes, how can a customer report security incident? / **Sample value:** Yes. Customers can report incidents to example.com.
  - **Control title:** Risk Management/Incident Response 5.2.3 - Incident Management - Report Incidents/Key Activities / **Control description:** Do you report key activities? / **Evidence extraction detail:** Do you report key activities? What is the SLA for reporting key activities? / **Sample value:** Yes. All key activities will be reported within a week.
  - **Control title:** Risk Management/Incident Response 5.2.4 - Incident Management - Incident Recovery / **Control description:** Do you have disaster recovery plans? / **Evidence extraction detail:** Specify if you have plans for recovery after an incident occurs. If yes, can you share details about the recovery plans? / **Sample value:** Yes. After an incident, recovery will be done within 24 hours.
  - **Control title:** Risk Management/Incident Response 5.2.5 - Incident Management - Logs Available to Buyers in case of an Attack (Requires manual attestation) / **Control description:** In case of an attack, will relevant resources (such as logs, incident report, or data) be available to customers? / **Evidence extraction detail:** Will relevant resources (such as logs, incident report, or data) related to their use be available to customers in case an attack or incident occurs? / **Sample value:** Yes
  - **Control title:** Risk Management/Incident Response 5.2.6 - Incident Management - Security Bulletin (Requires manual attestation) / **Control description:** Do you have a security bulletin that outlines latest attacks and vulnerabilities affecting your applications? / **Evidence extraction detail:** Specify if you have a security bulletin that outlines latest attacks and vulnerabilities affecting your applications. If yes, can you provide the details? / **Sample value:** Yes. Customers can report incidents to example.com.

- ****Incident detection****
  - **Control title:** Risk Management/Incident Response 5.3.1 - Incident Detection - Comprehensive Logging / **Control description:** Is there comprehensive logging to support the identification and mitigation of incidents? / **Evidence extraction detail:** Specify if there is comprehensive logging enabled. Identify the types of events that the system is capable of logging. How long are logs retained? / **Sample value:** Yes. The following events are logged: applications, device, and AWS services such as AWS CloudTrail, AWS Config, and VPC Flow Logs. Logs are retained for 1 year.
  - **Control title:** Risk Management/Incident Response 5.3.2 - Incident Detection - Log Monitoring / **Control description:** Do you monitor and alert on unusual or suspicious activities using detection mechanisms such as log monitoring? / **Evidence extraction detail:** Specify if regular security monitoring and alerting is performed. If yes, does it include log monitoring for unusual or suspicious behavior? / **Sample value:** Yes. All logs are monitored for unusual behavior such as multiple failed logins, login from an unusual geolocation, or other suspicious alerts.
  - **Control title:** Risk Management/Incident Response 5.3.3 - Incident Detection - Third Party Data Breach / **Control description:** Is there a process to identify and detect and log subcontractor security, privacy, or data breach issues? / **Evidence extraction detail:** Specify if there is a process in place to identify and detect third-party vendors or subcontractors for data breach, security issues, or privacy issues. / **Sample value:** Yes

- ** **SLA for incident notification** **
  - **Control title:** Risk Management/Incident Response 5.4.1 - SLA for Incident Notification (Requires manual attestation)
  - **Control description:** What is the SLA for sending notification about incidents or breaches?
  - **Evidence extraction detail:** What is the SLA for sending notification about incidents or breaches?
  - **Sample value:** 7 days



### Security and configuration policy controls
<a name="security-configuration-policy"></a>

Security and configuration policy controls evaluate security policies and security configurations that protect an organization's assets. This table lists the values and descriptions for security and configuration policy controls.



- ** **Policies for information security** **
  - **Control title:** Security and Configuration Policy 10.1.1 - Policies for Information Security - Information Security Policy / **Control description:** Do you have an information security policy that is owned and maintained by a security team? / **Evidence extraction detail:** Specify if you have an information security policy. If yes, share or upload a manual evidence. / **Sample value:** Yes. We build our security policy based on NIST framework.
  - **Control title:** Security and Configuration Policy 10.1.2 - Policies for Information Security - Policy Review / **Control description:** Are all security policies reviewed annually? / **Evidence extraction detail:** Specify if security policies are reviewed annually. If no, how often are the policies reviewed? / **Sample value:** Yes. Reviewed every year.

- ** **Policies for security configurations** **
  - **Control title:** Security and Configuration Policy 10.2.1 - Policies for Security Configurations - Security Configurations (Requires manual attestation) / **Control description:** Are security configuration standards maintained and documented? / **Evidence extraction detail:** Specify if all security configuration standards are maintained and documented. If yes, share or upload a manual evidence. / **Sample value:** Yes
  - **Control title:** Security and Configuration Policy 10.2.2 - Policies for Security Configurations - Security Configurations Review (Requires manual attestation) / **Control description:** Are security configurations reviewed at least annually? / **Evidence extraction detail:** Specify if security configurations are reviewed at least annually. If no, specify the frequency of review. / **Sample value:** Yes. Reviewed every 3 months.
  - **Control title:** Security and Configuration Policy 10.2.3 - Policies for Security Configurations - Changes to Configurations / **Control description:** Are changes to configurations logged? / **Evidence extraction detail:** Specify if configuration changes are logged. If yes, how long are the logs retained? / **Sample value:** Yes. All changes to configurations are monitored and logged. Alerts are raised when configurations are changed. Logs are retained for 6 months.

