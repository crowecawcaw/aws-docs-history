# Getting started with AWS Elemental MediaConnect

This Getting Started tutorial shows you how to use AWS Elemental MediaConnect to create and share
flows. The tutorial is based on a scenario where you want to do all of the following:

- Ingest a live video stream of an awards show that is taking place in New York City.
- Distribute your video to an affiliate in Boston who does not have an AWS account, and wants
  content sent to their on-premises encoder.
- Share your video with an affiliate in Philadelphia who wants to use their AWS account to
  distribute the video to their three local stations.

###### Topics

- [Prerequisites](#getting-started-prerequisites "#getting-started-prerequisites")
- [Step 1: Access AWS Elemental MediaConnect](#getting-started-access-console "#getting-started-access-console")
- [Step 2: Create a flow](#getting-started-create-flow "#getting-started-create-flow")
- [Step 3: Add an output](#getting-started-add-output "#getting-started-add-output")
- [Step 4: Grant an entitlement](#getting-started-add-entitlement "#getting-started-add-entitlement")
- [Step 5: Share details with your
  affiliates](#getting-started-share-with-affiliates "#getting-started-share-with-affiliates")
- [Step 6: Clean up](#getting-started-clean-up "#getting-started-clean-up")

## Prerequisites

Before you can use AWS Elemental MediaConnect, you need an AWS account and the appropriate permissions to access, view, and edit MediaConnect components.
Complete the steps in [Setting up AWS Elemental MediaConnect](setting-up.md "setting-up.md"), and then return to this tutorial.

## Step 1: Access AWS Elemental MediaConnect

After you set up your AWS account and create IAM roles, you sign in to the console
for AWS Elemental MediaConnect.

###### To access AWS Elemental MediaConnect

- Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/ "https://console.aws.amazon.com/mediaconnect/").

## Step 2: Create a flow

First, you create an AWS Elemental MediaConnect flow to ingest your video from your on-premises encoder into the AWS Cloud. For the purposes of this
tutorial, we use the following details:

- Flow name: AwardsNYCShow
- Source name: AwardsNYCSource
- Source protocol: Zixi push
- Zixi stream ID: ZixiAwardsNYCFeed
- CIDR block sending the content: 10.24.34.0/23
- Source encryption: None

###### To create a flow

1. On the **Flows** page, choose **Create
   flow**.
2. In the **Details** section, for **Name**,
   enter `AwardsNYCShow`.
3. For **Availability Zone**, choose
   **Any**.
4. In the **Source** section, for **Source
   type** select **Standard source**.
5. For **Name**, enter
   `AwardsNYCSource`.
6. For **Protocol**, choose **Zixi push**.
   AWS Elemental MediaConnect will populate the value of the ingest port.
7. For **Stream ID**, enter
   `ZixiAwardsNYCFeed`.
8. For **Allowlist CIDR**, enter
   `10.24.34.0/23`.
9. Choose **Create flow**.

## Step 3: Add an output

To send content to your affiliate in Boston, you must add an output to your flow. This output will send your video to your Boston affiliate's
on-premises encoder. For the purposes of this tutorial, we use the following details:

- Output name: AwardsNYCOutput
- Output protocol: Zixi push
- Zixi stream ID: ZixiAwardsOutput
- IP address of the Boston affiliate's on-premises encoder: 198.51.100.11
- Output encryption: None

###### To add an output

1. On the **Flows** page, choose the `AwardsNYCShow` flow.
2. Choose the **Outputs** tab.
3. Choose **Add output**.
4. For **Name**, enter `AwardsNYCOutput`.
5. For **Output type**, select **Standard
   output**.
6. For **Protocol**, choose **Zixi
   push**.
7. For **Stream ID**, enter `ZixiAwardsOutput`.
8. For **Destination IP address**, enter
   `198.51.100.11`.
9. For **Port**, enter `1024`.
10. Choose **Add output**.

## Step 4: Grant an entitlement

You must grant an entitlement to allow your Philadelphia affiliate to use your content as the source for their AWS Elemental MediaConnect flow. For
purposes of this tutorial, we use the following details:

- Entitlement name: PhillyTeam
- Philadelphia affiliate's AWS account ID: 222233334444
- Output encryption: None

###### To grant an entitlement

1. Choose the **Entitlements** tab.
2. Choose **Grant entitlement**.
3. For **Name**, enter `PhillyTeam`.
4. For **Subscriber**, enter `222233334444`.
5. Choose **Grant entitlement**.

## Step 5: Share details with your

affiliates

Now that you've created your AWS Elemental MediaConnect flow with an output for your Boston affiliate and an entitlement for your Philadelphia affiliate,
you need to communicate details about the flow.

Your Boston affiliate will receive the flow on their on-premises encoder. The details of where to send your video stream were provided by your
Boston affiliate, and you don't need to provide any other information. After you start your flow, the content will be sent to the IP address that
you specified when you created the flow.

Your Philadelphia affiliate must create their own AWS Elemental MediaConnect flow, using your flow as the source. You must provide the following
information to your Philadelphia affiliate:

- Entitlement ARN: You can find this value on the **Entitlement** tab of the **AwardsNYCShow** flow
  details page.
- Region: This is the AWS Region that you created the **AwardsNYCShow** flow in.

## Step 6: Clean up

To avoid extraneous charges, be sure to delete all unnecessary flows. You must stop the flow before it can be deleted.

###### To stop your flow

1. On the **Flows** page, choose the `AwardsNYCShow` flow.

The details page for the **AwardsNYCShow** flow appears. 2. Choose **Stop**.

###### To delete your flow

1. On the **AwardsNYCShow** flow details page, choose **Delete**.

A confirmation message appears. 2. Choose **Delete flow**.
