# Onboarding to Oracle Database@AWS

Before you can begin using Oracle Database@AWS, make sure you're signed up for AWS and create
necessary users. Then you can purchase Oracle Database@AWS from AWS Marketplace by accepting a private
offer from Oracle or by subscribing to a public offer.

###### Required SCP permission for odb:GetOciOnboardingStatus

If your organization uses service control policies (SCPs) that restrict AWS Regions,
the `odb:GetOciOnboardingStatus` action must be allowed in
US East (N. Virginia). This requirement applies to all accounts that use Oracle Database@AWS. The service
might call this API in US East (N. Virginia) regardless of the Region where you operate
Oracle Database@AWS. Without this permission, the service fails to initialize.

## Sign up for an AWS account

To get started with AWS, you need an AWS account. For information about creating an AWS account, see
[Getting started with an AWS account](../../../accounts/latest/reference/getting-started.md "../../../accounts/latest/reference/getting-started.md")
in the _AWS Account Management Reference Guide_.

## Request a private offer for Oracle Database@AWS

The AWS Marketplace seller private offer feature enables you to request and receive
Oracle Database@AWS pricing and EULA terms from Oracle. You negotiate pricing and terms with
Oracle, and then Oracle creates a private offer for the AWS account that you designate. You
accept the private offer and receive the negotiated price and terms of use. At this time, you
can use the Oracle Database@AWS dashboard. When the private offer agreement reaches its expiration date,
you're either moved automatically to the product's public pricing or unsubscribed from
Oracle Database@AWS. For more information about private offers, see [Private
offers in AWS Marketplace](../../../marketplace/latest/buyerguide/buyer-private-offers.md "../../../marketplace/latest/buyerguide/buyer-private-offers.md").

###### To request and accept a private offer for Oracle Database@AWS

1. Sign in to the AWS Management Console.
2. Search for and then choose Oracle Database@AWS.
3. Choose **Request private offer**.

###### Note

The Oracle Database@AWS dashboard isn't available until after you have accepted a private
offer. 4. On the Oracle Cloud Infrastructure (OCI) site, specify details such as the region and your contact
information. 5. Wait for an OCI representative to contact you and make a private offer available. 6. In the AWS Management Console, choose **View private offer**. 7. Choose the offer and then choose **View offer**. 8. Choose **Create contract** and respond to the subsequent prompts to
accept the private offer. 9. After accepting the private offer, you'll need to activate your OCI account. You can
access the Oracle activation links directly from AWS Management Console.

    1. In the console, navigate to the **Get started** section.
    2. Click on the Oracle activation link provided in the console. Alternatively, you can also use the activation link sent to you via email.
    3. On the Oracle activation page, choose whether to create a new Oracle cloud account or add to an existing account.
    4. Complete the activation process by following the on-screen instructions.
    5. After submitting your activation request, you'll see an **Activation in progress** status in the AWS Management Console, and the dashboard will be temporarily disabled with a reason displayed.
    6. After activation is complete, the Oracle Database@AWS dashboard becomes available, allowing you to
     manage your resources.

10. In the AWS Management Console, choose **Dashboard**.

## Accept a public offer for Oracle Database@AWS

Autonomous Database Serverless (ADB-S) is available via public offer on AWS Marketplace. With a
public offer, you can subscribe directly without waiting for an Oracle sales representative to
create a private offer.

###### To accept a public offer for Oracle Database@AWS

1. Sign in to the AWS Management Console.
2. Navigate to Oracle Database@AWS in AWS Marketplace.
3. Choose the public offer and then choose **Subscribe**.
4. Review the terms and choose **Create contract** to accept the public
   offer.
5. Activate your OCI account using the activation link provided in the AWS Management Console or sent
   via email.
6. After activation is complete, the Oracle Database@AWS dashboard becomes available and you can begin
   provisioning Autonomous Database Serverless instances.

###### Note

For public offer subscribers, the onboarding process is streamlined. No “Request
private offer” step is required.

## Subscribe to Oracle Database@AWS in multiple Regions

When you subscribe to Oracle Database@AWS through AWS Marketplace and finish onboarding, your AWS account is
linked to your OCI tenancy. This link, along with related resources, is automatically
replicated to all AWS Regions where Oracle Database@AWS is available. You subscribe and onboard once
rather than repeating the process for each Region.

To use Oracle Database@AWS in multiple Regions, perform the following steps:

1. Subscribe to Oracle Database@AWS through AWS Marketplace and complete the onboarding process.

When you first subscribe to Oracle Database@AWS, your account is activated in a home Region. You
specify the home Region in Oracle Cloud Infrastructure (OCI). 2. Enable your preferred Regions through the OCI console.

If you don't enable a Region in OCI, and then you switch to this Region in the
Oracle Database@AWS console, you receive an error stating that you haven't subscribed. In this case,
you must enable this Region in OCI before you can use the Oracle Database@AWS dashboard in this
Region. 3. Access Oracle Database@AWS in any supported AWS Region without repeating the subscription
process.
