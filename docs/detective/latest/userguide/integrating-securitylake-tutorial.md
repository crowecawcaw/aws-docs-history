# Enabling Detective integration with Security Lake

To integrate Detective with Security Lake, you must complete the following steps.

1. [Before you begin](securitylake-integration.md#Prerequisites "securitylake-integration.md#Prerequisites")

Use an Organizations management account to designate a delegated Security Lake administrator for
your organization. Make sure that Security Lake is enabled and verify that Security Lake is collecting
logs and events from AWS CloudTrail management events and Amazon Virtual Private Cloud (Amazon VPC) Flow Logs.

In alignment with the Security Reference Architecture, Detective recommends using a
Log Archive account and defer from using a Security Tooling account for the Security Lake
deployment. 2. [Creating a Security Lake subscriber](securitylake-integration.md#securitylake-subscriber "securitylake-integration.md#securitylake-subscriber")

To consume logs and events from Amazon Security Lake, you must be a Security Lake subscriber. Follow these steps to grant query access to a Detective account administrator. 3. Addding the required AWS Identity and Access Management (IAM) permissions to your IAM identity.

    * Add these permissions to create Detective integration with Security Lake:




    	+ Attach these AWS Identity and Access Management (IAM) permissions to your IAM identity. For details, see the [Add the required IAM permissions to your account](securitylake-integration.md#iam-permissions "securitylake-integration.md#iam-permissions") section.
    	+ Add this IAM policy to the IAM principal that you plan to use to pass the AWS CloudFormation service role. For more details, see the [Add permissions to your IAM principal](securitylake-integration.md#cloud-formation-template "securitylake-integration.md#cloud-formation-template") section.
    * If you have already integrated Detective with Security Lake, to use the integration attach these (IAM) permissions to your IAM identity. For details, see the [Add the required IAM permissions to your account](securitylake-integration.md#iam-permissions "securitylake-integration.md#iam-permissions") section.

4. [Accepting the Resource Share ARN invitation and enable the
   integration](securitylake-integration.md#resource-share-arn "securitylake-integration.md#resource-share-arn")
   Use the AWS CloudFormation template to set up the parameters required to create and manage
   query access for Security Lake subscribers. For the detailed steps to create a stack, see
   [Create a stack using the AWS CloudFormation template](securitylake-integration.md#cloud-formation-template "securitylake-integration.md#cloud-formation-template"). After you finish creating
   the stack, enable the integration.

For a demonstration of how to integrate Amazon Detective with Amazon Security Lake using the Detective console, watch the following video:
