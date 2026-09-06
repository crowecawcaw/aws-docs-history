

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Service management alignment
<a name="service-mgmt-alignment"></a>

This Connector aligns to industry best practices, such as ITIL®’s service management areas by enabling tools (services) with the intersection of people, processes and partners. The Connector also addresses a baseline set of service management practices you can use in existing operational tooling:


| Service management area | AWS service(s) integration | 
| --- | --- | 
| Service Catalog management deployment management (Provisioning) | [AWS Service Catalog](https://aws.amazon.com/servicecatalog/), AWS CloudFormation, and AWS Systems Manager Automation requests and provisions vetted and predictable products and performs post-provision actions. | 
| Incident management (Ticketing) | [Support](https://aws.amazon.com/premiumsupport/) (AWS services and platform incidents).<br />[AWS Systems Manager](https://aws.amazon.com/hsystems-manager/) OpsCenter (Jira operational Issues derived and detected for solutions built on AWS platform).<br />[AWS Security Hub CSPM](https://aws.amazon.com/security-hub/) (Jira Issues from security Findings).<br />AWS Systems Manager Incident Manager (AWS services and platform incidents). | 
| Service configuration management (CMDB) | [AWS Config](https://aws.amazon.com/config/) (Track AWS resources related to the Jira Issue). | 

In addition, [Atlassian Jira Service Management](https://www.atlassian.com/software/jira/service-management/features/service-desk) (JSM) is service desk software for modern IT teams. Jira Service Management request types enable self-service for developers and end users to order IT services based on request fulfillment approvals and workflows.