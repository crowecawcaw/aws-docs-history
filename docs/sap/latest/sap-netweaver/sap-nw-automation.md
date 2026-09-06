

# SAP NetWeaver on AWS Automation
<a name="sap-nw-automation"></a>

 AWS Systems Manager is a collection of capabilities that help you manage your applications and infrastructure running in AWS Cloud. Systems Manager simplifies application and resource management, shortens the time to detect and resolve operational problems, and helps you manage your AWS resources securely at scale.

This chapter contains information about how to use Systems Manager to automate management of your SAP applications.

## Automation prerequisites
<a name="automation-prerequisites"></a>

Because SAP automation in AWS Cloud relies on Systems Manager, you must satisfy the Systems Manager prerequisites. In addition, there are prerequisites specified in this chapter for specific tasks, such as SAP installation and operating system patching. Those prerequisites are listed in their respective sections.

Before you begin, verify the following prerequisites, which apply to all of the automation tasks described in this chapter:
+ You must have the latest SSM agent installed on your Amazon EC2 instances. For more information, see [Manually installing SSM Agent on EC2 instances for Linux](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-manual-agent-install.html) in the * AWS Systems Manager User Guide*.
+ You must satisfy the prerequisites for Systems Manager. For more information, see [Systems Manager prerequisites](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-prereqs.html) in the * AWS Systems Manager User Guide*.

**Topics**