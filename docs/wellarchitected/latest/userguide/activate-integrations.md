# Activating support in AWS WA Tool for other AWS

services

Activating Organization access permits AWS Well-Architected Tool to gather information about your
organization's structure to share resources more easily (see [Activate resource sharing within
AWS Organizations](sharing.md#getting-started-sharing-orgs "sharing.md#getting-started-sharing-orgs") for more information). Activating Discovery
support gathers information from [AWS Trusted Advisor](../../../awssupport/latest/user/trusted-advisor.md "../../../awssupport/latest/user/trusted-advisor.md"), [AWS Service Catalog AppRegistry](../../../servicecatalog/latest/arguide/intro-app-registry.md "../../../servicecatalog/latest/arguide/intro-app-registry.md"), and related resources (such as CloudFormation stacks in AppRegistry resource
collections) to help you more easily discover the information needed to answer
Well-Architected review questions, and tailor the Trusted Advisor checks for a workload.

Activating support for AWS Organizations, or activating Discovery support automatically creates
a service-linked role for your account.

**To turn on support for other services that AWS WA Tool can interact
with, navigate to Settings.**

1. To gather information from AWS Organizations, turn on **Activate AWS Organizations support**.
2. Turn on **Activate Discovery support** to gather information from other AWS
   services and resources.
3. Select **View role permissions** to view the service-linked role permissions or trust relationship policies.
4. Select **Save settings**.
