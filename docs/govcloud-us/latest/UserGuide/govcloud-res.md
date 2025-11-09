# Research and Engineering Studio on AWS in AWS GovCloud (US)

This product is currently available in AWS GovCloud (US-West) only.

Research and Engineering Studio on AWS (RES) is an AWS supported, open source product that enables IT administrators to provide a web portal for scientists and engineers to run technical computing workloads on AWS. RES provides a single pane of glass for users to launch secure virtual desktops to conduct scientific research, product design, engineering simulations, or data analysis workloads. Users can connect to the RES portal using their existing corporate credentials and work on individual or collaborative projects.

## How Research and Engineering Studio on AWS differs for AWS GovCloud (US)

The Research and Engineering Studio User Guide already includes special instructions for AWS GovCloud (US) where appropriate. The following list describes the instances where there are special instructions for AWS GovCloud (US).

- In the [Deploy the product](../../../res/latest/ug/deploy-the-product.md "../../../res/latest/ug/deploy-the-product.md") chapter:
  - Under [Prerequisites](../../../res/latest/ug/deploy-the-product.md#prerequisites "../../../res/latest/ug/deploy-the-product.md#prerequisites"):
    - You must follow the procedures under [Create domain (GovCloud only)](../../../res/latest/ug/deploy-the-product.md#create-domain-govcloud "../../../res/latest/ug/deploy-the-product.md#create-domain-govcloud").

  - Under [Step 1: Create external resources](../../../res/latest/ug/deploy-the-product.md#create-external-resources "../../../res/latest/ug/deploy-the-product.md#create-external-resources"):
    - We provide a different [template for AWS GovCloud (US)](https://console.amazonaws-us-gov.com/cloudformation/home?region=us-gov-west-1#/stacks/quickcreate?templateURL=https://s3.amazonaws.com/aws-hpc-recipes/main/recipes/res/res_demo_env/assets/bi.yaml "https://console.amazonaws-us-gov.com/cloudformation/home?region=us-gov-west-1#/stacks/quickcreate?templateURL=https://s3.amazonaws.com/aws-hpc-recipes/main/recipes/res/res_demo_env/assets/bi.yaml").
    - The `SubDomain` template parameter is required in AWS GovCloud (US).
    - Don’t use the `PortalDomainName` template parameter.

  - Under [Step 2: Launch the product](../../../res/latest/ug/deploy-the-product.md#launch-the-product "../../../res/latest/ug/deploy-the-product.md#launch-the-product"):
    - We provide a different [template for AWS GovCloud (US)](https://research-engineering-studio-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/releases/2024.01.01/ResearchAndEngineeringStudio.template.json "https://research-engineering-studio-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/releases/2024.01.01/ResearchAndEngineeringStudio.template.json").

- In the [Configuration guide](../../../res/latest/ug/configuration-guide.md "../../../res/latest/ug/configuration-guide.md") chapter:
  - In the [Managing users and groups](../../../res/latest/ug/manage-users.md "../../../res/latest/ug/manage-users.md") section:
    - Under [Setting up SSO with Identity Center](../../../res/latest/ug/manage-users.md#sso-idc "../../../res/latest/ug/manage-users.md#sso-idc"):
      - You must set up SSO in the AWS GovCloud (US) partition where you deployed RES.

  - In the [Create an ACM certificate](../../../res/latest/ug/acm-certificate.md "../../../res/latest/ug/acm-certificate.md") section:
    - You must create a certificate in your AWS GovCloud (US) account.
    - For step 7: copy the CNAME key and value. From the commercial partition account, use the values to create a new record in the Public Hosted Zone. The status of the certificate should change to **Issued**.

- In the [Administrator guide](../../../res/latest/ug/administrator-guide.md "../../../res/latest/ug/administrator-guide.md") chapter:
  - In the [eVDI](../../../res/latest/ug/evdi.md "../../../res/latest/ug/evdi.md") section:
    - Under [Software Stacks (AMIs)](../../../res/latest/ug/evdi.md#software-stacks "../../../res/latest/ug/evdi.md#software-stacks"):
      - To run the provided CentOS7 stack, you must subscribe to the AMI in AWS Marketplace with your [linked standard account](getting-started-standard-account-linking.md "getting-started-standard-account-linking.md").

  - In the [Cost monitoring and control](../../../res/latest/ug/cost-management.md "../../../res/latest/ug/cost-management.md") section:
    - Associating RES projects to AWS Budgets isn’t supported.

  - In the [Cost analysis dashboard](../../../res/latest/ug/cost-analysis-dashboard.md "../../../res/latest/ug/cost-analysis-dashboard.md") section:
    - Use of the cost analysis dashboard isn’t supported.

## Documentation for Research and Engineering Studio on AWS

[Research and Engineering Studio documentation](../../../res/latest/ug/overview.md "../../../res/latest/ug/overview.md").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- This product can generate metadata from customer-defined configurations. AWS suggests customers do not enter export-controlled information in console fields, descriptions, resource names, and tagging information.
