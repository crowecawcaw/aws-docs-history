# Select the Region

In choosing the Region for deployment, you’ll need to consider some key factors. For more details, see our [Overview and Planning](../general/sap-on-aws-overview.md "../general/sap-on-aws-overview.md") guide.

- Service availability
  - Not all AWS services or features are available in all Regions. Verify that all services and features that you want to use in your deployment are available in the Region you choose. You can check [availability on our website](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/ "https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/"). If certain services or features are not available in your desired Region, there are alternatives that we mention in the guide.
  - For SAP workloads discussed in this guide, this is particularly true for:
    - EC2 instance types
    - Amazon FSx for Windows File Server
    - AWS Backup

- Proximity and connectivity options
- Data residency
  - You retain complete control and ownership over your data in the Region in which it is physically located, making it easy to meet regional compliance and data residency requirements.
