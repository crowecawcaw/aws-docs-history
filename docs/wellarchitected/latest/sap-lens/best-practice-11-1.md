# Best Practice 11.1 – Monitor failures

of the SAP application, AWS resources, and connectivity

Monitoring for failures of the SAP application, AWS resources, and connectivity
helps you to react to failures or potential failures in a timely manner.

**Suggestion 11.1.1 – Use AWS Personal Health Dashboard and
notifications**

The [Health Dashboard](https://aws.amazon.com/premiumsupport/technology/aws-health-dashboard/ "https://aws.amazon.com/premiumsupport/technology/aws-health-dashboard/") gives you a personalized view of the status of the AWS services that
power your applications, enabling you to quickly see when there are issues impacting your
SAP workload. For example, in the event of a lost [Amazon Elastic Block Store (Amazon EBS)](https://aws.amazon.com/ebs/ "https://aws.amazon.com/ebs/") volume associated with one of your [Amazon EC2](https://aws.amazon.com/ec2/ "https://aws.amazon.com/ec2/") instances.

The dashboard also provides forward looking notifications, and you can set up alerts
across multiple channels, including email, so that you receive timely and relevant
information to help plan for scheduled changes. For example, in the event of AWS hardware
maintenance activities that impact one of your [Amazon EC2](https://aws.amazon.com/ec2/ "https://aws.amazon.com/ec2/") instances, you would receive a notification with information to help you
plan for and proactively address any issues associated with the upcoming change.

**Suggestion 11.1.2 – Evaluate AWS services to understand the health
of your SAP system**

AWS provides a number of [management and
governance](https://aws.amazon.com/products/management-and-governance/ "https://aws.amazon.com/products/management-and-governance/") services that you should evaluate, including Amazon CloudWatch and Amazon CloudWatch Application Insights for
SAP. Focus on the metrics that indicate a failure or potential failure, such as EC2 instance
failure, high CPU utilization, and file system utilization.

Refer to the Operational Excellence pillar for more details:

- SAP Lens [Operational Excellence]: [Best
  Practice 1.1 - Implement prerequisites for monitoring SAP on AWS](best-practice-1-1.md "best-practice-1-1.md")
- SAP Lens [Operational Excellence]: [Best
  Practice 1.4 - Implement workload configuration monitoring](best-practice-1-4.md "best-practice-1-4.md")

**Suggestion 11.1.3 – Evaluate the capability of SAP tools to monitor
failures**

Tools from SAP, such as Solution Manager and Landscape Manager, allow you to view any
monitoring data in the context of the application. The following monitoring solutions are
available from SAP. Review any additional licensing costs as part of the evaluation of
these tools.

- SAP Documentation: [SAP Focused run](https://support.sap.com/en/alm/sap-focused-run.html "https://support.sap.com/en/alm/sap-focused-run.html")
- SAP Documentation: [SAP Solution
  Manager](https://support.sap.com/en/alm/solution-manager.html "https://support.sap.com/en/alm/solution-manager.html")
- SAP Documentation: [SAP
  Landscape Manager (LaMa)](https://help.sap.com/viewer/lama_help "https://help.sap.com/viewer/lama_help")
- SAP Note: [2574820

* SAP Landscape Management Cloud Manager for Amazon Web Services (AWS)](https://launchpad.support.sap.com/#/notes/2574820 "https://launchpad.support.sap.com/#/notes/2574820")
  [Requires SAP Portal Access]

**Suggestion 11.1.4 – Evaluate third-party tools for AWS and SAP
monitoring**

The following monitoring solutions are available from the AWS Marketplace. You should evaluate
these and other third-party tools.

- AWS Documentation: [Monitoring Solutions in AWS Marketplace](https://aws.amazon.com/marketplace/b/2649280011?ref_=mp_nav_category_2649280011 "https://aws.amazon.com/marketplace/b/2649280011?ref_=mp_nav_category_2649280011")
