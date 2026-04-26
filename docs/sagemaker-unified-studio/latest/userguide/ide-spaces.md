# Code spaces in Amazon SageMaker Unified Studio

Amazon SageMaker Unified Studio provides compute spaces for integrated development environments (IDEs) that you
can use to code and develop your resources. When you create and use these IDEs in a Amazon SageMaker Unified Studio
project, you have access to all the data in that project and can share coding work with other
project members. Each space maintains its own persistent Amazon EBS volume, compute instance, and
runtime configuration, so your files, data, and session state are fully isolated between
spaces. You can scale compute and storage independently per space, and pause or resume spaces at
any time.

The code spaces experience differs depending on your domain type. Choose the section that
matches your domain configuration:

- [Code spaces in IAM domains](code-spaces-iam.md "code-spaces-iam.md")—For domains configured with IAM roles.
- [Code spaces in Identity Center domains](code-spaces-idc.md "code-spaces-idc.md")—For domains configured with AWS IAM Identity
  Center.
