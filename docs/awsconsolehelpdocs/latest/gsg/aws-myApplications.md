# What is myApplications in AWS Console Home?

myApplications is an extension of Console Home that helps you manage and monitor the cost, health, security posture, and performance of your applications on AWS. Applications allow you to group resources and metadata.
You can access all applications in your account, key metrics across all applications, and an overview of cost, security, and operations metrics and insights from multiple service consoles from one view in the AWS Management Console. myApplications includes the following:

- Applications widget on the Console Home page
- myApplications that you can use to view application resource costs and security findings
- myApplications dashboard that provides a view of key application metrics such as cost, performance, and security findings

###### Topics

- [Features of myApplications](#myApp-benefits "#myApp-benefits")
- [Related services](#myApp-related-services "#myApp-related-services")
- [Accessing myApplications](#myApp-access "#myApp-access")
- [Pricing](#myApp-pricing "#myApp-pricing")
- [Supported Regions for myApplications](supported-regions.md "supported-regions.md")
- [Applications in myApplications](myApp-manage-apps.md "myApp-manage-apps.md")
- [Resources in myApplications](myApp-manage-resources.md "myApp-manage-resources.md")
- [myApplications dashboard in AWS Console Home](myApp-app-dash.md "myApp-app-dash.md")

## Features of myApplications

- **Create applications** – Create new applications and organize their resources. Your applications are automatically shown in the myApplications, so you can take action
  in the AWS Management Console, APIs, CLI, and SDKs. Infrastructure as code (IaC) is generated when you create an application and is accessible from the myApplication dashboard. IaC is useable in IaC tools including AWS CloudFormation and Terraform.
- **Access your applications** – You can quickly access any of your applications from the myApplications widget by selecting it.
- **Access your resources** – You can quickly view your application resources from the Services menu by selecting the application. When you select a resource, you go directly to the relevant service console. Your place in the resource table is saved, so you can continue browsing at any time from the Services menu.
- **Compare application metrics** – Use myApplications to compare key metrics for applications like cost of application resources and
  number of critical security findings for multiple applications.
- **Monitor and manage applications** – Assess application health and performance using alarms, canaries, and service level objectives from Amazon CloudWatch, findings from AWS Security Hub CSPM, and
  cost trends from AWS Cost Explorer Service. You can also find compute metrics summaries and optimizations and manage resource compliance and configuration status from AWS Systems Manager.

## Related services

myApplications makes use of the following services:

- AppRegistry
- AppManager
- Amazon CloudWatch
- Amazon EC2
- AWS Lambda
- AWS Resource Explorer
- AWS Security Hub CSPM
- Systems Manager
- AWS Service Catalog
- Tagging

## Accessing myApplications

You can access myApplications from the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") by choosing **myApplications** in the left sidebar.

## Pricing

myApplications on AWS is offered at no additional charge. There are no set-up fees or upfront commitments. Usage charges for the underlying resources and services that the myApplication dashboard summarizes still apply at published rates for those resources.
