# Set up to use ROSA

To prepare your environment for creating a ROSA cluster, you need to complete the following actions.

## Prerequisites

The following prerequisites must be met to enable ROSA cluster creation.

- Install and configure the latest AWS CLI.
  For more information, see [Installing or updating the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").
- Install and configure the latest ROSA CLI and OpenShift Container Platform CLI.
  For more information, see [Getting started with the ROSA CLI](https://access.redhat.com/documentation/en-us/red_hat_openshift_service_on_aws/4/html/rosa_cli/rosa-get-started-cli "https://access.redhat.com/documentation/en-us/red_hat_openshift_service_on_aws/4/html/rosa_cli/rosa-get-started-cli").
- You must have the required service quotas set for Amazon EC2, Amazon VPC, Amazon EBS, and Elastic Load Balancing.
  AWS or Red Hat may request service quota increases on your behalf as required for issue resolution.
  To view the service quotas required for ROSA, see [Red Hat OpenShift Service on AWS endpoints and quotas](../../../general/latest/gr/rosa.md#limits_rosa "../../../general/latest/gr/rosa.md#limits_rosa") in the _AWS General Reference_.
- To receive AWS support for ROSA, you must enable AWS Business, Enterprise On-Ramp, or Enterprise support plans.
  Red Hat may request AWS support on your behalf as required for issue resolution.
  For more information, see [Getting ROSA support](rosa-support.md "rosa-support.md").
  To enable Support, see the [Support page](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/").
- If you’re using AWS Organizations to manage the AWS accounts that host the ROSA service, the organization’s service control policy (SCP) must be configured to allow Red Hat to perform policy actions that’s listed in the SCP without restriction.
  For more information, see the [AWS Organizations service control policy denies required AWS Marketplace permissions](security-iam-troubleshoot.md#error-aws-orgs-scp-denies-permissions "security-iam-troubleshoot.md#error-aws-orgs-scp-denies-permissions").
  For more information about SCPs, see [Service control policies (SCPs)](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md").
- If deploying a ROSA
  cluster with AWS STS into an enabled AWS Region that’s disabled by default, you must update the security token to version 2 for all the Regions in the AWS account with the following command.

```
aws iam set-security-token-service-preferences --global-endpoint-token-version v2Token
```

For more information about enabling Regions, see link:accounts/latest/reference/manage

## Enable ROSA and configure AWS prerequisites

To create a ROSA
cluster, you must enable the ROSA service in the AWS
ROSA console.
The AWS
ROSA console verifies if your AWS account has the necessary AWS Marketplace permissions, service quotas, and the Elastic Load Balancing (ELB) service-linked role named `AWSServiceRoleForElasticLoadBalancing`.
If any of these prerequisites are missing, the console provides guidance on how to configure your account to meet the prerequisites.

1. Navigate to the [ROSA console](https://console.aws.amazon.com/rosa "https://console.aws.amazon.com/rosa").
2. Choose **Get started**.
3. On the **Verify ROSA prerequisites** page, select **I agree to share my contact information with Red Hat**.
4. Choose **Enable ROSA** .
5. Once the page has verified your service quotas meet ROSA prerequisites and the ELB service-linked role is created, open a new terminal session to create your first ROSA
   cluster using the ROSA CLI.
