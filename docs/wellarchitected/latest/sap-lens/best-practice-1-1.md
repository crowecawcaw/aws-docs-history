# Best Practice 1.1 – Implement

prerequisites for monitoring SAP on AWS

SAP certification requirements for SAP on AWS are outlined in SAP Note 1656250. This
note includes instructions for setting up the AWS Data Provider for SAP, enabling Amazon
CloudWatch detailed monitoring, and using SAP enhanced monitoring for SAP NetWeaver
solutions. Enabling these prerequisites helps ensure that your SAP workload state is able
to be fully understood and investigated by AWS and SAP. These prerequisites should feed
into your overall SAP monitoring strategy.

**Suggestion 1.1.1 - Check SAP support prerequisites**

Check SAP Note 1656250 on the SAP support portal for the most up-to-date support
requirements for SAP on AWS workloads. Follow the detailed instructions in this note.

- SAP Note: [1656250

* SAP on AWS: Support Prerequisites](https://launchpad.support.sap.com/#/notes/1656250 "https://launchpad.support.sap.com/#/notes/1656250") [Requires SAP Portal Access]

**Suggestion 1.1.2 - Install AWS Data Provider for SAP NetWeaver
workloads**

The AWS Data Provider for SAP is a required installation on each of your EC2
instances supporting SAP NetWeaver workloads. The AWS Data Provider for SAP is an agent
which collects performance-related metrics from AWS services and provides them to the
SAP internal application monitoring system. SAP tools, such as transaction code ST06n and
Solution Manager monitoring that use external metrics usually collected from the SAPOSCOL
service, require the AWS Data Provider for SAP to access AWS metrics.

There are indirect costs associated with running the AWS Data Provider for SAP
because of the detailed monitoring and increased API calls required for SAP to receive
monitoring data at speciﬁc intervals. See [AWS Data
Provider for SAP - Introduction - Pricing](../../../sap/latest/general/data-provider-intro.md#data-provider-pricing "../../../sap/latest/general/data-provider-intro.md#data-provider-pricing") for details.

- AWS Documentation: [AWS
  Data Provider for SAP](../../../sap/latest/general/aws-data-provider.md "../../../sap/latest/general/aws-data-provider.md")

**Suggestion 1.1.3 - Create a monitoring strategy for your SAP
workloads**

Decide how you will observe the current and historical health of your SAP application
from both an inside-out and outside-in perspective. Consider all components which work
together to provide the end-user experience. Consider how you will capture metrics from
underlying AWS compute, storage, and network services in addition to internal SAP
application metrics and external user performance and reliability monitoring. Evaluate
different tools for each component and decide how you can bring these together in a single
place (for example, log aggregation) to perform root cause analysis when needed. Determine
how you will use this information to design alert thresholds and remediation actions to be
taken when thresholds are breached.

Understand the capabilities of SAP Solution Manager monitoring, third-party
monitoring tools, and CloudWatch dashboards that can ingest custom SAP monitoring metrics
as a starting point for your design.

- AWS Documentation: [SAP
  NetWeaver on AWS: Monitoring Guide](../../../sap/latest/sap-netweaver/monitoring.md "../../../sap/latest/sap-netweaver/monitoring.md")
- SAP on AWS Blog: [Serverless Monitoring for SAP NetWeaver](https://aws.amazon.com/blogs/awsforsap/sap-monitoring-a-serverless-approach-using-amazon-cloudwatch/ "https://aws.amazon.com/blogs/awsforsap/sap-monitoring-a-serverless-approach-using-amazon-cloudwatch/")
- SAP on AWS Blog: [Serverless Monitoring for SAP HANA](https://aws.amazon.com/blogs/awsforsap/sap-hana-monitoring-a-serverless-approach-using-amazon-cloudwatch/ "https://aws.amazon.com/blogs/awsforsap/sap-hana-monitoring-a-serverless-approach-using-amazon-cloudwatch/")
- SAP on AWS Blog: [Set
  up observability for SAP HANA databases with Amazon CloudWatch Application Insights](https://aws.amazon.com/blogs/awsforsap/sap-hana-observability-with-amazon-cloudwatch-application-insights/ "https://aws.amazon.com/blogs/awsforsap/sap-hana-observability-with-amazon-cloudwatch-application-insights/")
- AWS Service Video: [Gaining Better Observability
  of Your VMs with Amazon CloudWatch](https://youtu.be/1Ck_me4azMw?ref=wellarchitected "https://youtu.be/1Ck_me4azMw?ref=wellarchitected")
- AWS Marketplace: [Products and Tools for SAP Monitoring](https://aws.amazon.com/marketplace/search/results?page=1&searchTerms=SAP&category=45c68cc2-ccd6-426b-94bd-92a791004dc2 "https://aws.amazon.com/marketplace/search/results?page=1&searchTerms=SAP&category=45c68cc2-ccd6-426b-94bd-92a791004dc2")
- SAP Documentation: [SAP Solution Manager 7.2 - Application Operations](http://help.sap.com/viewer/c3c5ec585ee248228ddb6c3f08073ea9/LATEST/en-US/456408e2a51b476c960fda046c96cb76.html "http://help.sap.com/viewer/c3c5ec585ee248228ddb6c3f08073ea9/LATEST/en-US/456408e2a51b476c960fda046c96cb76.html")
- SAP Documentation: [SAP NetWeaver Alert Monitor](https://help.sap.com/docs/ABAP_PLATFORM_NEW/984899fe989d4efab0409b818433f892/4907442b4cab209ce10000000a42189d.html?locale=en-US "https://help.sap.com/docs/ABAP_PLATFORM_NEW/984899fe989d4efab0409b818433f892/4907442b4cab209ce10000000a42189d.html?locale=en-US")
