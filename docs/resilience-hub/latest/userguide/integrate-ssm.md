# AWS Systems Manager

AWS Resilience Hub works with Systems Manager to automate the steps of your SOPs by providing a number of
SSM documents you can use as the basis for those SOPs.

AWS Resilience Hub provides you CloudFormation templates that contains the IAM roles required to run
different Systems Manager documents, one role per document with permissions required for the
specific document. After creating a stack with the CloudFormation template, it will setup the
IAM roles and save metadata in Systems Manager parameter for the Systems Manager automation document to
run for different recovery procedures.

For more information on using SOPs, see [Managing standard operating procedures](sops.md "sops.md").
