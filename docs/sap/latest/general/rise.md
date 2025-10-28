# RISE with SAP on AWS Cloud

RISE with SAP S/4HANA Cloud, private edition is a cloud ERP offering from SAP. Along with ERP, it includes Business Process Intelligence, Business Platform and Analytics, and Business Networks. SAP maintains responsibility for the holistic service level agreement, cloud operations, and technical support for RISE. You can choose your own cloud service provider in RISE with SAP.

SAP S/4 HANA Cloud, private edition is a single-tenant setup where different customer environments are isolated by AWS accounts and a dedicated Virtual Private Cloud (VPC).

###### Important

SAP owns and manages the AWS account where RISE with SAP is deployed, and is responsible for the AWS services used to serve your SAP landscape on AWS.

SAP is responsible for security in the cloud in RISE with SAP. For more information, see [AWS Cloud Security – Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/") and [SAP and Hyperscalers: Clarifying Security in the Cloud](https://spc.2bm.dk/wp-content/uploads/2021/08/SAP-and-Hyperscalers_-Clarifying-Security-in-the-Cloud.pdf "https://spc.2bm.dk/wp-content/uploads/2021/08/SAP-and-Hyperscalers_-Clarifying-Security-in-the-Cloud.pdf"). In addition to the security provided by SAP, you can also implement additional security for your SAP landscape. See the [Security](security-rise.md "security-rise.md") section for more details.

In your AWS account managed by SAP, SAP manages the AWS services required to run your SAP landscape on AWS. You can still utilize AWS services to extend RISE with SAP in your own AWS account that is not managed by SAP. For example, you can create a data lake with Amazon AppFlow or AWS Glue. See the [Extensions](extensions-rise.md "extensions-rise.md") section for more details.

###### Note

You must create a separate AWS account or use your existing AWS account that is not managed by SAP for creating extensions with AWS services.

SAP avails Support for AWS account that is managed by SAP. You are not required to establish additional Support for the AWS account managed by SAP.

This documentation is focused on RISE with SAP S/4HANA Cloud, private edition and SAP S/4HANA Cloud, private edition, tailored option. The following topics are covered in this document.

###### Topics

- [Connectivity](connectivity-rise.md "connectivity-rise.md")
- [Security](security-rise.md "security-rise.md")
- [Reliability](reliability-rise.md "reliability-rise.md")
- [Observability](rise-observability.md "rise-observability.md")
- [Change Management](rise-change-management.md "rise-change-management.md")
- [Data Integration and Analytics](rise-data-integration-analytics.md "rise-data-integration-analytics.md")
- [Agentic AI](rise-agenticai.md "rise-agenticai.md")
- [AWS and SAP JRA](rise-jra.md "rise-jra.md")
- [Extensions](extensions-rise.md "extensions-rise.md")
