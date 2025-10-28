# Use AMS SSP to provision Amazon WorkSpaces in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access WorkSpaces capabilities directly in your AMS managed account. WorkSpaces enables you to provision virtual, cloud-based Microsoft Windows or Amazon Linux desktops for
your users, known as WorkSpaces. WorkSpaces eliminates the need to procure and deploy hardware
or install complex software. You can quickly add or remove users as your needs change.
Users access their WorkSpaces by using a client application from a supported device or,
for Windows WorkSpaces, a web browser, and they log in by using their existing on-premises Active Directory (AD)
credentials.

To learn more, see [Amazon WorkSpaces](https://aws.amazon.com/workspaces/ "https://aws.amazon.com/workspaces/").

## WorkSpaces in AWS Managed Services FAQ

Common questions and answers:

**Q: How do I request access to WorkSpaces in my AMS account?**

Request access by submitting a Management | AWS service | Self-provisioned service | Add (managed automation) (ct-3qe6io8t6jtny) change type.
This RFC provisions the following IAM role to your account: `customer_workspaces_console_role`.
Once provisioned in your account, you must onboard the role in your federation solution.

**Q: What are the restrictions to using WorkSpaces in my AMS account?**

Full functionality of Workspaces is available with the Amazon WorkSpaces
self-provisioned service role.

**Q: What are the prerequisites or dependencies to using WorkSpaces in my AMS account?**

- WorkSpaces are limited by AWS Region; therefore, the AD Connector must be configured in the same
  AWS Region where the WorkSpaces instances are hosted.

Customers can connect WorkSpaces to customer AD using one of the following two methods:

    1. Using AD connector to proxy authentication to on-premises Active Directory service
     (preferred):


    Configure Active Directory (AD) Connector in your AMS account prior to integrating your
     WorkSpaces instance with your on-premises directory service. The AD Connector acts as a proxy for
     your existing AD users (from your domain) to connect to WorkSpaces using existing on-premises AD
     credentials. This is preferred because WorkSpaces are directly joined to the customer's on-prem
     domain, which acts as both Resource and User forest, leading to more control on the customer side.


    For more information, see
     [Best Practices for Deploying Amazon WorkSpaces (Scenario 1)](../../../whitepapers/latest/best-practices-deploying-amazon-workspaces/scenario-1-using-ad-connector-to-proxy-authentication-to-on-premises-active-directory-service.md "../../../whitepapers/latest/best-practices-deploying-amazon-workspaces/scenario-1-using-ad-connector-to-proxy-authentication-to-on-premises-active-directory-service.md").
    2. Using AD Connector with AWS Microsoft AD, Shared Services VPC, and a one-way trust to on-premises:


    You can also authenticate users with your on-premises directory by first establishing a
     one-way outgoing trust from AMS-managed AD to your on-premises AD. WorkSpaces will join AMS-managed AD using an AD Connector. WorkSpaces access permissions will then be delegated to the WorkSpaces instances through the AMS-managed AD, without the need to establish a two-way trust with your on-premises environment. In this scenario, the User forest will be in the customer AD and the Resource forest will be in the AMS-managed AD (changes to AMS-managed AD can be requested via RFC). Note that the connectivity between WorkSpaces VPC and the MALZ Shared Services VPC running AMS-managed AD is established via Transit Gateway.


    For more information, see
     [Best Practices for Deploying Amazon WorkSpaces (Scenario 6)](../../../whitepapers/latest/best-practices-deploying-amazon-workspaces/scenario-6-aws-microsoft-ad-shared-services-vpc-and-a-one-way-trust-to-on-premises.md "../../../whitepapers/latest/best-practices-deploying-amazon-workspaces/scenario-6-aws-microsoft-ad-shared-services-vpc-and-a-one-way-trust-to-on-premises.md").

###### Note

The AD Connector can be configured by submitting a
Management | Other | Other | Create change type RFC with the prerequisite AD configuration details; for more information, see
[Create an AD Connector](../../../directoryservice/latest/admin-guide/create_ad_connector.md "../../../directoryservice/latest/admin-guide/create_ad_connector.md"). If method 2 is used to create a
Resource forest in AMS-managed AD, submit another Management | Other | Other | Create change type RFC in AMS shared-services account by running the
AMS-managed AD.
