# Best Practice 7.3 – Understand your

organization’s identity management approach, and its application to SAP

Typical SAP workloads will consist of multiple systems and therefore multiple
identities. A centralized approach for managing these users can reduce the security risk and
operational complexity. Your focus should be on how to use AWS services and third-party
tools in your approach to SAP security, considering such options as centralized user
management, single sign-on, and multi-factor authentication.

**Suggestion 7.3.1 – Determine an Identity Provider for named
users**

Users will be associated with an identity store, for example Active Directory. This
acts as a central repository for managing identity information, such as roles,
permissions, and identifiers. For each set of identities, determine if this can be
associated with an Identity Provider. An identity provider enables you to off-load the
authentication of users. It facilitates single sign-on (SSO) and also manages the user
identity lifecycle (for example joiners, movers, leavers).

Consider exceptions for named users that are not associated with a human. This may
include batch, job scheduling, integration, and monitoring users.

- AWS Documentation: [AWS
  Directory Service | Amazon Web Services (AWS)](https://aws.amazon.com/directoryservice/ "https://aws.amazon.com/directoryservice/")
- AWS Documentation: [AWS Identity
  Services](https://aws.amazon.com/identity/ "https://aws.amazon.com/identity/")

**Suggestion 7.3.2 – Determine the authentication
mechanisms**

Understand the supported authentication mechanisms (for example, SAML, Kerberos,
X.509, SAP Single Sign-On tickets) at each of the layers for your SAP workload. Evaluate
the requirements to integrate with your application. Where possible use single sign-on to
avoid the administrative and security impact of managing multiple user credentials.

- SAP Documentation: [User Authentication and single sign-on](https://help.sap.com/viewer/621bb4e3951b4a8ca633ca7ed1c0aba2/LATEST/en-US/4a112f1a2228101ee10000000a42189b.html "https://help.sap.com/viewer/621bb4e3951b4a8ca633ca7ed1c0aba2/LATEST/en-US/4a112f1a2228101ee10000000a42189b.html")
- AWS Documentation: [Cloud
  applications - AWS IAM Identity Center](../../../singlesignon/latest/userguide/saasapps.md "../../../singlesignon/latest/userguide/saasapps.md")
- SAP on AWS Blog: [Enable SAP Single Sign On with AWS IAM Identity Center Part 1: Integrate SAP NetWeaver ABAP with
  IAM Identity Center](https://aws.amazon.com/blogs/awsforsap/enable-sap-single-sign-on-with-aws-sso-part1-integrate-sap-netweaver-abap-based-applications-sso-with-aws-sso/ "https://aws.amazon.com/blogs/awsforsap/enable-sap-single-sign-on-with-aws-sso-part1-integrate-sap-netweaver-abap-based-applications-sso-with-aws-sso/")
- SAP on AWS Blog: [Enable SAP Single Sign On with AWS IAM Identity Center Part 2: Integrate SAP NetWeaver Java](https://aws.amazon.com/blogs/awsforsap/enable-sap-single-sign-on-with-aws-sso-part-2-integrate-sap-netweaver-java/ "https://aws.amazon.com/blogs/awsforsap/enable-sap-single-sign-on-with-aws-sso-part-2-integrate-sap-netweaver-java/")
- SAP on AWS Blog: [Enable Single Sign On for SAP Cloud Platform Foundry and SAP Cloud Platform Neo
  with IAM Identity Center](https://aws.amazon.com/blogs/awsforsap/enable-single-sign-on-for-sap-cloud-platform-foundry-and-sap-cloud-platform-neo-with-aws-sso/ "https://aws.amazon.com/blogs/awsforsap/enable-single-sign-on-for-sap-cloud-platform-foundry-and-sap-cloud-platform-neo-with-aws-sso/")

**Suggestion 7.3.3 – Consider multi-factor authentication**

Multi-Factor Authentication (MFA) is a best practice that adds an extra layer of
protection on top of your logon credentials. These multiple factors provide increased
security for your SAP application. Use cases include: access to SAP from an untrusted
device; access to the AWS Management Console; and privileged activities such as deletion of backups or
termination of EC2 instances.

- SAP on AWS Blog: [Securing SAP Fiori with MFA](https://aws.amazon.com/blogs/awsforsap/securing-sap-fiori-with-multi-factor-authentication/ "https://aws.amazon.com/blogs/awsforsap/securing-sap-fiori-with-multi-factor-authentication/")
- AWS Documentation: [Using MFA devices with your IAM sign-in page - AWS Identity and Access](../../../IAM/latest/UserGuide/console_sign-in-mfa.md "../../../IAM/latest/UserGuide/console_sign-in-mfa.md")
- AWS Documentation: [Configuring MFA delete -Amazon Simple Storage Service](../../../AmazonS3/latest/userguide/MultiFactorAuthenticationDelete.md "../../../AmazonS3/latest/userguide/MultiFactorAuthenticationDelete.md")
- AWS Documentation: [Amazon EC2: Requires MFA (GetSessionToken) for specific EC2 operations](../../../IAM/latest/UserGuide/reference_policies_examples_ec2_require-mfa.md "../../../IAM/latest/UserGuide/reference_policies_examples_ec2_require-mfa.md")

**Suggestion 7.3.4 – Determine the approach to certificate
management**

Client-based certificates can be used for authentication without the need for
credentials. Determine an approach which includes time-based expiration for session
management and certificate rotation for system to system communication. AWS provides a
Certificate Authority (CA) that is trusted by SAP. Certificates can be issued and managed
using [AWS Certificate Manager
(ACM)](https://aws.amazon.com/certificate-manager/ "https://aws.amazon.com/certificate-manager/").

- SAP Note: [2801396

* SAP Global Trust List](https://launchpad.support.sap.com/#/notes/2801396 "https://launchpad.support.sap.com/#/notes/2801396") [Requires SAP Portal Access]

- SAP Note: [3040959

* How to get a CA signed server certificate in ABAP](https://launchpad.support.sap.com/#/notes/3040959 "https://launchpad.support.sap.com/#/notes/3040959") [Requires SAP Portal
  Access]

- SAP Lens [Operational Excellence]: [Suggestion
  3.4.1 - Create specific runbooks for SAP security operations](best-practice-3-4.md "best-practice-3-4.md")
- SAP Lens [Operational Excellence]: [Suggestion
  4.1.2 - Maintain a calendar for expiring of credentials, certificates and
  licenses](best-practice-4-1.md "best-practice-4-1.md")
