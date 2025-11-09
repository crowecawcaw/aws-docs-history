# Red Hat OpenShift Service on AWS in AWS GovCloud (US)

Red Hat OpenShift Service on AWS (ROSA) is a managed service that you can use to build, scale, and deploy containerized applications with Red Hat OpenShift running on AWS infrastructure. ROSA is jointly supported and operated by AWS and Red Hat. ROSA offers 24-hour site reliability engineering (SRE) support for cluster installation, management, and upgrades backed by Red Hat’s 99.95% uptime service-level agreement.

###### Note

Red Hat OpenShift Service on AWS has achieved an agency Authority to Operate (ATO) at the FedRAMP High Baseline.

## How Red Hat OpenShift Service on AWS differs for AWS GovCloud (US)

- You must have access to the [Red Hat Hybrid Cloud Console on AWS GovCloud (US)](https://console.openshiftusgov.com/openshift "https://console.openshiftusgov.com/openshift"). To obtain access, complete the [ROSA FedRAMP access request form](https://console.redhat.com/openshift/create/rosa/govcloud "https://console.redhat.com/openshift/create/rosa/govcloud").
- Support does not yet have the ability to transfer support cases to Red Hat on behalf of customers.
- Red Hat support cases are managed through ServiceNow. ServiceNow has a Provisional Authority to Operate (P-ATO) at the FedRAMP High benchmark. Red Hat personnel that manage ROSA support cases through ServiceNow are U.S. persons. For more information, see [ServiceNow’s FedRAMP authorization details](https://marketplace.fedramp.gov/products/F1305072116 "https://marketplace.fedramp.gov/products/F1305072116") on the FedRAMP Marketplace.
  - Customers set up access to ServiceNow during the onboarding process.

- ROSA with hosted control planes (HCP) is not yet available in the AWS GovCloud (US) Regions. Only ROSA classic is supported.
- The AWS
  ROSA console is not yet available in AWS GovCloud (US) Regions.
- Only ROSA clusters that use AWS PrivateLink can be deployed in AWS GovCloud (US).
- You must meet the U.S. regulatory requirements as described in [AWS GovCloud (US) Sign Up](getting-started-sign-up.md "getting-started-sign-up.md").
- You must deploy ROSA into an existing VPC.
- ROSA only supports the use of AWS Security Token Service (AWS STS) temporary security credentials to allow the service to perform actions in the customer AWS account.
- ROSA only uses FIPS-validated modules to process cryptographic libraries.
- You must have a FIPS 140-3 compliant hardware token for use with the service.
- You need to configure the AWS CLI on your local machine to use your AWS GovCloud (US) account. This configuration is required to create ROSA clusters.
- ROSA entitlements cannot be shared between AWS standard accounts and AWS GovCloud (US) accounts using AWS License Manager.
- VPC sharing is not supported.

## Enabling ROSA

To enable access to ROSA in the AWS GovCloud (US) Regions, the AWS GovCloud (US) account root user must complete the following steps.

###### Note

For AWS Organizations users, repeat these steps for each member account that requires access.

1. Create a Red Hat commercial account or use an existing one.
2. Create an AWS standard account. AWS recommends creating a new AWS standard account that will only be used for AWS GovCloud (US) sign-up and billing.
3. Log in to the AWS standard account.
4. Go to the [ROSA console](https://console.aws.amazon.com/rosa "https://console.aws.amazon.com/rosa") and enable ROSA.
5. Sign up for an AWS GovCloud (US) account. For more information, see [AWS GovCloud (US) Sign Up](getting-started-sign-up.md "getting-started-sign-up.md").

###### Note

Before creating accounts in the AWS GovCloud (US) Regions, make sure that you meet specific U.S. regulatory requirements as described in [AWS GovCloud (US) Sign Up](getting-started-sign-up.md "getting-started-sign-up.md"). 6. Link your AWS GovCloud account to your AWS standard account. 7. Complete the [ROSA FedRAMP access request form](https://console.redhat.com/openshift/create/rosa/govcloud "https://console.redhat.com/openshift/create/rosa/govcloud") to initiate onboarding to AWS GovCloud (US). Upon submission, this form will be processed by Red Hat. If Red Hat requires further information, you will receive a follow-up email, or you will receive instructions on how to access the service.

###### Note

You can use the Red Hat Hybrid Cloud Console on AWS GovCloud (US) to deploy ROSA to multiple AWS GovCloud (US) accounts.

## Creating and deploying a ROSA classic cluster into the AWS GovCloud (US) Regions

After enabling ROSA for AWS GovCloud (US), you can create and deploy ROSA classic clusters into the AWS GovCloud (US) Regions.

### Prerequisites

To deploy ROSA classic clusters into the AWS GovCloud (US) Regions, the following prerequisites must be met.

- You have access to the Red Hat Hybrid Cloud Console on AWS GovCloud (US).
- You have an AWS GovCloud (US) account linked to an AWS standard account.
- You configured the AWS CLI on your local machine to use your AWS GovCloud (US) account. For more information, see [Configure your Account using AWS CLI](configure-using-cli.md "configure-using-cli.md").
- You created your own Amazon VPC architecture to deploy your clusters into. For more information, see [Create Amazon VPC architecture for the cluster](../../../ROSA/latest/userguide/getting-started-private-link.md#getting-started-private-link-step-2 "../../../ROSA/latest/userguide/getting-started-private-link.md#getting-started-private-link-step-2") in the _ROSA User Guide_.
- You completed the prerequisite actions documented in [Getting started with ROSA classic using AWS PrivateLink](../../../rosa/latest/userguide/getting-started-private-link.md#getting-started-private-link-prereqs "../../../rosa/latest/userguide/getting-started-private-link.md#getting-started-private-link-prereqs").

### Log in to your AWS GovCloud (US) and Red Hat Hybrid Cloud Console on AWS GovCloud (US) accounts

Once the prerequisites have been met, follow these steps.

###### Note

If you cannot sign in to your AWS GovCloud (US) account or Red Hat Hybrid Cloud Console on AWS GovCloud (US) account, ask your administrator for the information that you need to sign in.

1. Sign in to your AWS GovCloud (US) account.
2. Go to the [Red Hat Hybrid Cloud Console on AWS GovCloud (US) login page](https://console.openshiftusgov.com/openshift "https://console.openshiftusgov.com/openshift") and sign in with your Red Hat account credentials.
3. The remaining procedure varies depending on whether you are creating clusters using the Red Hat Hybrid Cloud Console on AWS GovCloud (US) or ROSA CLI.
   1. Console
      1. Choose **Create cluster with web interface**.
      2. Follow the console prompts to create the ROSA cluster.

   2. ROSA CLI
      1. Choose **Create cluster with CLI**.
      2. Copy the following command:

      ```
      rosa login --govcloud <TOKEN>
      ```

      3. Open a terminal session and run the command.

### Create and deploy a ROSA classic cluster that uses AWS PrivateLink

Once logged in to your AWS GovCloud (US) and Red Hat Hybrid Cloud Console on AWS GovCloud (US) accounts, you can create a ROSA classic cluster that uses AWS PrivateLink and deploys into the AWS GovCloud (US) Regions.

The procedure is the same for deploying a ROSA classic cluster in AWS GovCloud (US) Regions and AWS standard Regions. For more information, see [Getting started with ROSA using AWS PrivateLink](../../../ROSA/latest/userguide/getting-started-private-link.md#getting-started-private-link-step-3 "../../../ROSA/latest/userguide/getting-started-private-link.md#getting-started-private-link-step-3") in the _ROSA User Guide_.

## Documentation for Red Hat OpenShift Service on AWS

[ROSA documentation.](../../../ROSA/latest/userguide/what-is-rosa.md "../../../ROSA/latest/userguide/what-is-rosa.md")

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- This service can generate metadata from customer-defined configurations. AWS suggests customers do not enter export-controlled information in console fields, descriptions, resource names, and tagging information.
