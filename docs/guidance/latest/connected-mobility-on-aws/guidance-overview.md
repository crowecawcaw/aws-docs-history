# What is Guidance for Connected Mobility on AWS?

Overview of the Guidance for Connected Mobility on AWS including features, use cases, and key concepts.

Amazon Web Services (AWS) automotive customers need efficient ways to manage connected vehicle fleets with reduced downtime through predictive maintenance, real-time location tracking, enhanced fleet safety monitoring, and modern software-driven vehicle experiences.

The Guidance for Connected Mobility on AWS addresses these needs and provides comprehensive capabilities for vehicles and fleet management systems to interact with the AWS Cloud. This guidance allows you to leverage proven architectural patterns, deploy scalable infrastructure through phase-based deployment, and extend functionality with custom modules for your specific use cases.

This guidance employs a modern, scalable telemetry architecture designed to handle high-volume, real-time data streams characteristic of connected vehicle fleets. The guidance supports fleet growth from hundreds to millions of vehicles while maintaining sub-second processing latency for safety-critical applications.

The Guidance for Connected Mobility on AWS addresses these needs and provides a complete reference architecture for building enterprise-grade connected vehicle platforms. This open-source guidance demonstrates AWS best practices for vehicle connectivity, real-time telemetry processing, and fleet management at scale.

As an open-source implementation, partners and customers can:

- Use the entire guidance as a production-ready connected vehicle platform
- Adopt specific architectural patterns and components for their unique requirements
- Reference the implementation as a blueprint for enterprise best practices
- Extend and customize the codebase to meet specific business needs
- Learn from real-world examples of AWS service integration at automotive scale
  Provided capabilities include:

- Secure vehicle-to-cloud communication using AWS IoT Core with X.509 certificates
- High-throughput telemetry ingestion and processing with Amazon MSK and Apache Flink
- Real-time stream processing for trip aggregation, safety events, and maintenance alerts
- Scalable data storage with DynamoDB and S3 for operational and analytical workloads
- Fleet management dashboard for vehicle monitoring and operations
- Integrated fleet simulator for testing and demonstration
- RESTful APIs for programmatic access to fleet data
  Original equipment manufacturers (OEMs), tier one suppliers, and fleet operators can deploy the complete guidance or leverage individual components and architectural patterns. The open-source nature enables organizations to adapt the implementation to their specific requirements while benefiting from AWS-validated best practices.

Vehicle telemetry data, such as speed, oil temperature, tire pressure, and geolocation generated from car sensors provides near real-time insights for analytics and machine learning (ML) use cases. The architecture demonstrates how to make this data available for external consumption, enabling use cases like usage-based insurance, connected accident advisor, and package delivery services.

This implementation guide provides an overview of the Guidance for Connected Mobility on AWS, its reference architecture and components, considerations for planning the deployment, and configuration steps for deploying the guidance to AWS Cloud.

The intended audience for using this solutguidanceion’s features and capabilities in their environment includes solutions architects, business decision makers, DevOps engineers, data scientists, and cloud professionals.

Use this navigation table to quickly find answers to these questions:

| If you want to . . .                                                                                                                                             | Read . . .                                                                                                                                                                                             |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Know the cost for running this guidance.<br>The estimated cost for running this guidance in the us-east-1 Region is USD $352.80 per month.                       | [Cost](cost.md "cost.md")                                                                                                                                                                              |
| Understand the security considerations for this guidance.                                                                                                        | [Security](security-considerations.md "security-considerations.md")                                                                                                                                    |
| Know how to plan for quotas for this guidance.                                                                                                                   | [Quotas](quotas.md "quotas.md")                                                                                                                                                                        |
| View or download the AWS CloudFormation template included in this guidance to automatically deploy the infrastructure resources (the "stack") for this guidance. | [AWS CloudFormation templates](cloudformation-templates.md "cloudformation-templates.md")                                                                                                              |
| Access the source code and optionally use the AWS Cloud Development Kit (AWS CDK) to deploy the guidance.                                                        | [GitHub repository](https://github.com/aws-solutions-library-samples/guidance-for-connected-mobility-on-aws "https://github.com/aws-solutions-library-samples/guidance-for-connected-mobility-on-aws") |
