# 6 – Use infrastructure and software controls to reduce

security misconfigurations

**How do you protect your SAP application and the underlying database,
operating system, storage, and networks?** We recommend that SAP software
solutions and the associated underlying configurations—such as operating system and database
patches, parameters, cloud services, and infrastructure —be hardened. Hardening helps ensure
the safety of all SAP environments, both production and non-production, at the appropriate
level determined by your organization.

Use the [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/") to guide your activities regarding the security
of your SAP environment. For example, firmware updates for your EC2 instances are “security
of the cloud” activities for which AWS is responsible, while operating system and
application management for those same EC2 instances are “security in the cloud” activities
for which you are responsible.

| ID       | Priority | Best Practice                                                           |
| -------- | -------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ☐ BP 6.1 | Required | Ensure that security and auditing are built into the SAP network design |
| ☐ BP 6.2 | Required | Build and protect the operating system                                  |
| ☐ BP 6.3 | Required | Protect the database and the application                                |
| ☐ BP 6.4 | Required | Establish a plan for upgrading and patching all applicable software     | For more details, refer to the following information: <br>• AWS Documentation: [Best practices for Security, Identity, & Compliance](https://aws.amazon.com/architecture/security-identity-compliance/ "https://aws.amazon.com/architecture/security-identity-compliance/") <br>• SAP Note: [2191528 - Third-party report showing security vulnerabilities](https://launchpad.support.sap.com/#/notes/2191528 "https://launchpad.support.sap.com/#/notes/2191528") [Requires SAP Portal Access] <br>• SAP Documentation: [ABAP Platform Security Guide](https://help.sap.com/viewer/621bb4e3951b4a8ca633ca7ed1c0aba2/LATEST/en-US/4aaf6fd65e233893e10000000a42189c.html "https://help.sap.com/viewer/621bb4e3951b4a8ca633ca7ed1c0aba2/LATEST/en-US/4aaf6fd65e233893e10000000a42189c.html") |
