After careful consideration, we have made the decision to close new customer access to **AWS Mainframe Modernization self-managed experience**,
effective June 30, 2026. Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for
AWS Mainframe Modernization self-managed experience, but we do not plan to introduce new features. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

**AWS Mainframe Modernization Service (Managed Runtime Environment experience)** is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# AWS Transform for mainframe Runtime

AWS Transform for mainframe offers a single Runtime to cater to different stages of your
modernization journey and operational needs. This page describes its
characteristics, use cases, and how to access it.

## AWS Transform for mainframe Runtime

With AWS Transform for mainframe Runtime you can deploy your modernized application in your own AWS account
, allowing you to manage your own infrastructure. This option provides both
release and alpha pre-release versions, giving you the flexibility to operate all the
technical components required to run your modernized application the way you want. You
can choose between stable releases for production environments or alpha pre-release versions
for testing and development purposes.

The AWS Transform for mainframe Runtime is deployed and managed by the customer, offering more control
over the runtime environment. It provides automated refactoring capabilities and is
suitable for customized deployment scenarios.

### When to use

The AWS Transform for mainframe Runtime is suitable for testing and production environments, and
is particularly useful when specific customization of the runtime environment is
required.

### How to access

The AWS Transform for mainframe Runtime is accessible from [AWS Transform for mainframe refactor Toolbox](https://bluinsights.aws/docs/bluage-toolbox-introduction "https://bluinsights.aws/docs/bluage-toolbox-introduction").

###### Note

Access to the [AWS Transform for mainframe refactor Toolbox](https://bluinsights.aws/docs/bluage-toolbox-introduction "https://bluinsights.aws/docs/bluage-toolbox-introduction") is provided as part of your AWS Transform for mainframe project
engagement.

### Deployment

AWS Transform for mainframe Runtime is available for deployment on:

- Amazon EC2
- Amazon ECS on Amazon EC2
- Amazon EKS on Amazon EC2
- Amazon ECS managed by AWS Fargate

Deploying on Amazon EC2 can be done directly in the instance or through a Docker
containerized application, which is the preferred way when using Amazon ECS or
Amazon EKS.

For detailed deployment instructions, see [Set
up AWS Transform for mainframe Runtime](ba-runtime-setup.md "ba-runtime-setup.md") documentation.
