

# Research and Engineering Studio on AWS in AWS GovCloud (US)
<a name="govcloud-res"></a>

Research and Engineering Studio on AWS (RES) is an AWS supported, open source product that enables IT administrators to provide a web portal for scientists and engineers to run technical computing workloads on AWS. RES provides a single pane of glass for users to launch secure virtual desktops to conduct scientific research, product design, engineering simulations, or data analysis workloads. Users can connect to the RES portal using their existing corporate credentials and work on individual or collaborative projects.

Research and Engineering Studio on AWS is currently available in AWS GovCloud (US-West).

## How Research and Engineering Studio on AWS differs
<a name="_how_research_and_engineering_studio_on_aws_differs"></a>

The following differences apply to Research and Engineering Studio on AWS. The Research and Engineering Studio User Guide already includes special instructions for AWS GovCloud (US) where appropriate. The following list describes the instances where there are special instructions.
+ In the [Deploy the product](https://docs.aws.amazon.com/res/latest/ug/deploy-the-product.html) chapter:
  + Under [Prerequisites](https://docs.aws.amazon.com/res/latest/ug/deploy-the-product.html#prerequisites):
    + You must follow the procedures under [Create domain (GovCloud only)](https://docs.aws.amazon.com/res/latest/ug/deploy-the-product.html#create-domain-govcloud).
  + Under [Step 1: Create external resources](https://docs.aws.amazon.com/res/latest/ug/deploy-the-product.html#create-external-resources):
    + We provide a different [template for AWS GovCloud (US)](https://console.amazonaws-us-gov.com/cloudformation/home?region=us-gov-west-1#/stacks/quickcreate?templateURL=https://s3.amazonaws.com/aws-hpc-recipes/main/recipes/res/res_demo_env/assets/bi.yaml).
    + The ` SubDomain ` template parameter is required.
    + Don’t use the ` PortalDomainName ` template parameter.
  + Under [Step 2: Launch the product](https://docs.aws.amazon.com/res/latest/ug/deploy-the-product.html#launch-the-product):
    + We provide a different [template for AWS GovCloud (US)](https://research-engineering-studio-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/releases/2024.01.01/ResearchAndEngineeringStudio.template.json).
+ In the [Configuration guide](https://docs.aws.amazon.com/res/latest/ug/configuration-guide.html) chapter:
  + In the [Managing users and groups](https://docs.aws.amazon.com/res/latest/ug/manage-users.html) section:
    + Under [Setting up SSO with Identity Center](https://docs.aws.amazon.com/res/latest/ug/manage-users.html#sso-idc):
      + You must set up SSO in the AWS GovCloud (US) partition where you deployed RES.
  + In the [Create an ACM certificate](https://docs.aws.amazon.com/res/latest/ug/acm-certificate.html) section:
    + You must create a certificate in your AWS GovCloud (US) account.
    + For step 7: copy the CNAME key and value. From the commercial partition account, use the values to create a new record in the Public Hosted Zone. The status of the certificate should change to **Issued**.
+ In the [Administrator guide](https://docs.aws.amazon.com/res/latest/ug/administrator-guide.html) chapter:
  + In the [eVDI](https://docs.aws.amazon.com/res/latest/ug/evdi.html) section:
    + Under [Software Stacks (AMIs)](https://docs.aws.amazon.com/res/latest/ug/evdi.html#software-stacks):
      + To run the provided CentOS7 stack, you must subscribe to the AMI in AWS Marketplace with your [linked standard account](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/getting-started-standard-account-linking.html).
  + In the [Cost monitoring and control](https://docs.aws.amazon.com/res/latest/ug/cost-management.html) section:
    + Associating RES projects to AWS Budgets is not available.
  + In the [Cost analysis dashboard](https://docs.aws.amazon.com/res/latest/ug/cost-analysis-dashboard.html) section:
    + Use of the cost analysis dashboard is not available.

## Documentation
<a name="govcloud-docs-78"></a>
+  [Research and Engineering Studio documentation](https://docs.aws.amazon.com/res/latest/ug/overview.html) 

## Export-controlled content
<a name="govcloud-itar-content-117"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+ This product can generate metadata from customer-defined configurations. AWS suggests customers do not enter export-controlled information in console fields, descriptions, resource names, and tagging information.