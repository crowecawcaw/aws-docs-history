# 4 – Implement data access control

**How do you manage access to data
within your organization’s source, analytics, and downstream
systems?**

An analytics workload is a centralized repository of data from
different source systems. As the analytics workload owner, you
should honor the source systems’ access management policies
when connecting to, and ingesting from, the source systems.

| **ID**
| **Priority**
| **Best practice**
|
| --- | --- | --- |
| ☐ BP 4.1 | Required | Allow data owners to determine which people or systems can access data in analytics and downstream workloads. |
| ☐ BP 4.2 | Required | Build user identity solutions that uniquely identify people and systems. |
| ☐ BP 4.3 | Required | Implement the required data authorization models. |
| ☐ BP 4.4 | Recommended | Establish an emergency access process to ensure that admin access is managed and used when required. |
| ☐ BP 4.5 | Recommended | Track data and database changes. | For more details, refer to the following documentation: <br>• AWS Lake Formation Developer Guide: [Lake Formation Access Control Overview](../../../lake-formation/latest/dg/access-control-overview.md "../../../lake-formation/latest/dg/access-control-overview.md") <br>• Amazon Athena User Guide: AWS [Identity and Access Management in Amazon Athena](../../../athena/latest/ug/security-iam-athena.md "../../../athena/latest/ug/security-iam-athena.md") <br>• Amazon Athena User Guide: [Enabling Federated Access to the Amazon Athena API](../../../athena/latest/ug/access-federation-saml.md "../../../athena/latest/ug/access-federation-saml.md") <br>• Amazon Redshift Database Developer Guide: [Managing database security](../../../redshift/latest/dg/r_Database_objects.md "../../../redshift/latest/dg/r_Database_objects.md") <br>• Amazon EMR Management Guide: [AWS Identity and Access Management for Amazon EMR](../../../emr/latest/ManagementGuide/emr-plan-access-iam.md "../../../emr/latest/ManagementGuide/emr-plan-access-iam.md") <br>• Amazon EMR Management Guide: [Use Kerberos authentication](../../../emr/latest/ManagementGuide/emr-kerberos.md "../../../emr/latest/ManagementGuide/emr-kerberos.md") <br>• Amazon EMR Management Guide: [Use an Amazon EC2 key pair for SSH credentials](../../../emr/latest/ManagementGuide/emr-plan-access-ssh.md "../../../emr/latest/ManagementGuide/emr-plan-access-ssh.md")
