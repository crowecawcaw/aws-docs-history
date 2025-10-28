# Best Practice 1.7 – Implement single

pane of glass health monitoring across your SAP workloads

Configure your SAP applications, AWS services, and any dependent components to
provide information about the flow of transactions across the workload. Combine metrics
from multiple sources to create a single pane of glass visualization for the health of
your SAP workload and make this dashboard accessible to your key users. Use this
information to determine when a response is required and to assist you in quickly
identifying the factors contributing to an issue impacting your business.

**Suggestion 1.7.1 - Combine application metrics, workload
configuration, user metrics, and dependency health in a single location**

Combine application monitoring metrics, workload configuration data, user metrics and
dependency health in a single location or tool to allow end-to-end monitoring of your SAP
workload and its health for end-user business processes. This can be achieved through the
use of SAP Solution Manager, custom CloudWatch dashboards and metrics, or third-party
monitoring tools.

Best practice is to create business facing health dashboards with traffic light
health and trends, which allow a drill-down view of workload availability. Drill down
capabilities allow users and operators to assess the specific component of the technology
stack which may be causing a problem or underperforming.

- AWS Documentation: [Create a CloudWatch Dashboard](../../../AmazonCloudWatch/latest/monitoring/create_dashboard.md "../../../AmazonCloudWatch/latest/monitoring/create_dashboard.md")
- SAP on AWS Blog: [Serverless Monitoring for SAP NetWeaver](https://aws.amazon.com/blogs/awsforsap/sap-monitoring-a-serverless-approach-using-amazon-cloudwatch/ "https://aws.amazon.com/blogs/awsforsap/sap-monitoring-a-serverless-approach-using-amazon-cloudwatch/")
- SAP on AWS Blog: [Serverless Monitoring for SAP HANA](https://aws.amazon.com/blogs/awsforsap/sap-hana-monitoring-a-serverless-approach-using-amazon-cloudwatch/ "https://aws.amazon.com/blogs/awsforsap/sap-hana-monitoring-a-serverless-approach-using-amazon-cloudwatch/")
- AWS Marketplace: [Products and Tools for SAP Monitoring](https://aws.amazon.com/marketplace/search/results?page=1&searchTerms=SAP&category=45c68cc2-ccd6-426b-94bd-92a791004dc2 "https://aws.amazon.com/marketplace/search/results?page=1&searchTerms=SAP&category=45c68cc2-ccd6-426b-94bd-92a791004dc2")
- SAP Documentation: [SAP Solution Manager 7.2 - Application Operations](http://help.sap.com/viewer/c3c5ec585ee248228ddb6c3f08073ea9/LATEST/en-US/456408e2a51b476c960fda046c96cb76.html "http://help.sap.com/viewer/c3c5ec585ee248228ddb6c3f08073ea9/LATEST/en-US/456408e2a51b476c960fda046c96cb76.html")
