# SAP on AWS Overview

AWS has been working with SAP since 2011 to help customers deploy and migrate their SAP applications to AWS, and SAP supports running the vast majority of available SAP applications on AWS.

## SAP Software and Licenses on AWS

This section describes the options available for SAP software and licenses on AWS.

### Bring Your Own Software and License

The majority of SAP solutions that can be run on AWS use a bring-your-own-software and bring-your-own-license (BYOL) model. Running SAP systems on AWS doesn’t require special or new SAP licenses. If you’re an existing SAP customer, you can use your existing SAP licenses when running SAP on AWS. You are responsible for obtaining a valid SAP license, and you must ensure that you are in compliance with the SAP licensing policies. AWS does not provide or sell SAP licenses.

### AWS Marketplace

[AWS Marketplace](https://aws.amazon.com/marketplace "https://aws.amazon.com/marketplace") is a digital catalog with thousands of software listings from independent software vendors that makes it easy to find, test, buy, and deploy software that runs on AWS. To view SAP-related offerings available in AWS Marketplace, follow this link: [SAP in AWS Marketplace](https://aws.amazon.com/marketplace/search/results?searchTerms=SAP "https://aws.amazon.com/marketplace/search/results?searchTerms=SAP").

### SAP Trial and Developer Licenses

The [SAP Cloud Appliance Library](https://www.sap.com/products/technology-platform/cloud-appliance-library.html "https://www.sap.com/products/technology-platform/cloud-appliance-library.html") provides access to an online repository of the latest preconfigured SAP solutions. You can quickly deploy these solutions on AWS by using a launch wizard that automates deployment. Some of the solutions available in the SAP Cloud Appliance Library are provided with free trial or developer edition licenses.

#### SAP Hardware Key Generation

SAP hardware key generation on EC2 instances uses a specific process that is dependent on the SAP kernel patch level. If a hardware key is generated before patching the SAP kernel to the proper level, and the kernel is updated at a later time, the hardware key may change, making the installed license invalid. For details on how the SAP hardware ID is generated on EC2 instances and the required SAP kernel patch levels see the following SAP notes (SAP One Support Launchpad access required):

- [SAP Note 2327159](https://launchpad.support.sap.com/#/notes/2327159 "https://launchpad.support.sap.com/#/notes/2327159") – SAP NetWeaver License Behavior in Virtual and CLoud Environments
- [SAP Note 1178686](https://launchpad.support.sap.com/#/notes/1178686 "https://launchpad.support.sap.com/#/notes/1178686") – Linux: Alternative method to generate a SAP hardware key
- [SAP Note 2327159](https://launchpad.support.sap.com/#/notes/2327159 "https://launchpad.support.sap.com/#/notes/2327159") – SAP NW License Behavior in Virtual and Cloud Environments
- [SAP Note 1697114](https://launchpad.support.sap.com/#/notes/1697114 "https://launchpad.support.sap.com/#/notes/1697114") – Determination of hardware ID in Amazon clouds
- [SAP Note 2113263](https://launchpad.support.sap.com/#/notes/2113263 "https://launchpad.support.sap.com/#/notes/2113263") – Additional public key for AWS Hardware ID
- [SAP Note 2823805](https://launchpad.support.sap.com/#/notes/2823805 "https://launchpad.support.sap.com/#/notes/2823805") – Additional public keys for AWS Hardware ID
- [SAP Note 2319387](https://launchpad.support.sap.com/#/notes/2319387 "https://launchpad.support.sap.com/#/notes/2319387") – Adjustment of the license check for AWS China

## SAP Support on AWS

AWS and SAP have worked together closely to ensure that you receive the same level of support via the same support channels, whether you’re running your SAP systems on AWS or on premises.

### SAP Solutions Supported on AWS

The majority of SAP solutions that run on traditional on-premises infrastructure are fully supported by SAP on AWS. For the complete list of SAP solutions supported on AWS, see [SAP Note 1656099](https://launchpad.support.sap.com/#/notes/1656099 "https://launchpad.support.sap.com/#/notes/1656099") and the other notes referenced within that note.

### SAP Support on AWS

To ensure full support of your SAP on AWS environment from SAP and AWS, you must follow the guidelines and requirements in [SAP Note 1656250](https://launchpad.support.sap.com/#/notes/1656250 "https://launchpad.support.sap.com/#/notes/1656250"). Here are the primary requirements you must follow to ensure support of your SAP on AWS environment:

- Enable detailed monitoring for **Amazon CloudWatch** on each EC2 instance to ensure that the required AWS metrics are provided in one-minute intervals. For additional information on Amazon CloudWatch, see [https://aws.amazon.com/cloudwatch](https://aws.amazon.com/cloudwatch "https://aws.amazon.com/cloudwatch").
- Install, configure, and run the [AWS Data Provider for SAP](data-provider-intro.md "data-provider-intro.md") on each EC2 instance. The AWS Data Provider collects the required performance and configuration data from a variety of sources, including the Amazon EC2 API, Amazon EC2 instance metadata, and Amazon CloudWatch, and shares it with SAP applications, to help monitor and improve the performance of business transations.
- Any AWS account that you use for running SAP systems must have an [AWS support plan](https://aws.amazon.com/premiumsupport/plans "https://aws.amazon.com/premiumsupport/plans") for either Business Support or Enterprise Support.

## Deploying SAP Systems on AWS

The section describes different options available for provisioning AWS infrastructure and installing SAP systems on AWS.

### Manual Deployment

The majority of SAP solutions supported on AWS can be installed by manually provisioning the required AWS infrastructure resources and then following the relevant SAP installation document on AWS.

### Automated Deployment

AWS Launch Wizard for SAP is a service that guides you through the sizing, configuration, and deployment of SAP applications on AWS. AWS Launch Wizard reduces the time it takes to deploy SAP applications on AWS. You input your application requirements, including SAP HANA settings, SAP landscape settings, and deployment details on the service console, and AWS Launch Wizard identifies the appropriate AWS resources to deploy and run your SAP application.

For more information, see [How AWS Launch Wizard for SAP works](../../../launchwizard/latest/userguide/how-launch-wizard-sap-works.md "../../../launchwizard/latest/userguide/how-launch-wizard-sap-works.md").

### Prebuilt Images

Some SAP solutions are available on AWS as a prebuilt system image that contains a preinstalled and preconfigured SAP system. A prebuilt SAP system image enables you to rapidly provision a new SAP system without spending the time and effort required by a traditional manual SAP installation.

Prebuilt SAP system images are available from the following sources:

- [AWS Marketplace](https://aws.amazon.com/marketplace/search/results?searchTerms=SAP "https://aws.amazon.com/marketplace/search/results?searchTerms=SAP")
- [SAP Cloud Appliance Library](https://www.sap.com/products/technology-platform/cloud-appliance-library.html "https://www.sap.com/products/technology-platform/cloud-appliance-library.html")

| SAP solution                                           | Deployment option(s)                                                                                                                      |
| ------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| **SAP Business Suite (ERP, CRM, etc.)**                | Manual                                                                                                                                    | [SAP CAL](https://cal.sap.com/ "https://cal.sap.com/")                                                                                                                                         |
| **SAP NetWeaver**                                      | [Manual](https://aws.amazon.com/sap/docs/#SAP_NetWeaver-based_solutions "https://aws.amazon.com/sap/docs/#SAP_NetWeaver-based_solutions") | [AWS Launch Wizard for SAP](https://aws.amazon.com/quickstart/architecture/sap-netweaver-abap "https://aws.amazon.com/quickstart/architecture/sap-netweaver-abap")                             | [SAP CAL](https://cal.sap.com/ "https://cal.sap.com/") |
| **SAP S/4HANA**                                        | Manual                                                                                                                                    | AWS Launch Wizard for SAP                                                                                                                                                                      | [SAP CAL](https://cal.sap.com/ "https://cal.sap.com/") |
| **SAP BW/4HANA**                                       | Manual                                                                                                                                    | [SAP CAL](https://cal.sap.com/ "https://cal.sap.com/")                                                                                                                                         |
| **SAP HANA**                                           | [Manual](../sap-hana/std-sap-hana-environment-setup.md "../sap-hana/std-sap-hana-environment-setup.md")                                   | AWS Launch Wizard for SAP                                                                                                                                                                      | [SAP CAL](https://cal.sap.com/ "https://cal.sap.com/") |
| **SAP BusinessObjects BI**                             | [Manual](https://aws.amazon.com/sap/docs/#SAP_BusinessObjects "https://aws.amazon.com/sap/docs/#SAP_BusinessObjects")                     | [AWS Marketplace](https://aws.amazon.com/marketplace/search/results?searchTerms=SAP+BusinessObjects+BI "https://aws.amazon.com/marketplace/search/results?searchTerms=SAP+BusinessObjects+BI") | [SAP CAL](https://cal.sap.com/ "https://cal.sap.com/") |
| **SAP Commerce (Hybris)**                              | Manual                                                                                                                                    |
| **SAP Business One, version for SAP HANA**             | Manual                                                                                                                                    | [SAP CAL](https://cal.sap.com/ "https://cal.sap.com/")                                                                                                                                         |
| **SAP Business One, version for Microsoft SQL Server** | Manual                                                                                                                                    |

### Getting Assistance from APN Partners

There are AWS Partner Networks (APN) partners who are experienced in deploying and operating SAP solutions, and can help you with your SAP workloads on AWS. For additional information see the following section.

## Partner Services for SAP on AWS

The [AWS Partner Network (APN)](https://aws.amazon.com/partners "https://aws.amazon.com/partners") is a community of companies that offer a wide range of services and products on AWS. APN SAP partners can provide SAP-specific services to help you fully maximize the benefits of running SAP solutions on AWS.

### Types of Partner Services and Solutions for SAP on AWS

- **Cloud assessment services** – Advisory services to help you develop an efficient and effective plan for your cloud adoption journey. Typical services include financial/TCO (total cost of ownership), technical, security and compliance, and licensing.
- **Proof-of-concept services** – Services to help you test SAP on AWS; for example: SAP ERP/ECC migration to SAP HANA or SAP S/4HANA, SAP Business Warehouse (BW) migration to SAP HANA or SAP BW/4HANA, SAP OS/DB migrations, new SAP solution implementation.
- **Migration services** – Services to migrate existing SAP environments or systems to AWS; for example: all-on-AWS SAP migrations (PRD/QAS/DEV), hybrid SAP migrations (QAS/DEV), single SAP system (e.g., SAP BW) migrations.
- **Managed services** – Managed services for SAP environments on AWS, including: AWS account and resource administration, OS administration/patching, backup and recovery, SAP Basis and SAP NetWeaver.
- **Packaged solutions** – Bundled software and service offerings from SAP Partners that combine SAP software, licenses, implementation, and managed services on AWS, such as SAP S/4HANA, SAP BusinessObjects BI, and many others.
- **ISV software solutions** – Partner software solutions for the migration, integration, and operation of SAP solutions on AWS; for example: system migration, high availability, backup and recovery, data replication, automatic scaling, disaster recovery.

### How to Find Partner Solutions for SAP on AWS

The **AWS SAP Partner Solutions** provides a centralized place to search, discover, and connect with trusted APN partners who offer solutions and services to help your business achieve faster time to value and maximize the benefits of running SAP solutions on AWS. For more information, see [AWS SAP Competency Partners](https://aws.amazon.com/sap/partner-solutions/ "https://aws.amazon.com/sap/partner-solutions/").
