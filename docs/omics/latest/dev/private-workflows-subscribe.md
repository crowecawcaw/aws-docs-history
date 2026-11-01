

# Connecting HealthOmics runs to a Sentieon license server
<a name="private-workflows-subscribe"></a>

HealthOmics supports [VPC-connected workflows](https://aws.amazon.com/about-aws/whats-new/2026/03/aws-healthomics-vpc-connected-workflows/), which is the recommended approach for connecting to a third-party license server, such as a Sentieon license server. By default, workflow runs use `RESTRICTED` networking mode, which cannot reach a license server. The following steps show how to connect your runs to a VPC so they can reach your Sentieon license server.

## Step 1: Get your license from Sentieon
<a name="sentieon-step-get-license"></a>

Send an email to the Sentieon support group ([support@sentieon.com](mailto:support@sentieon.com)) to request a software license. Sentieon provides a license that you install on the license server in Step 2.

## Step 2: Set up your Sentieon license server
<a name="sentieon-step-license-server"></a>

Deploy a Sentieon license server on an Amazon EC2 instance in your VPC. For more details, see [Start a Sentieon license server inside your AWS VPC](https://github.com/Sentieon/sentieon-amazon-omics#step-1-start-a-sentieon-license-server-inside-your-aws-vpc) in GitHub.

## Step 3: Set up your VPC
<a name="sentieon-step-vpc"></a>

Deploy a VPC by following the [sample-healthomics-vpc-configuration](https://github.com/aws-samples/sample-healthomics-vpc-configuration) AWS CDK project. Your runs use this VPC to reach the license server from Step 2. This project deploys a VPC, subnets, NAT gateways, and a security group, and optionally creates a HealthOmics configuration if you set the `networkingConfigurationName` parameter. It also enables VPC Flow Logs, which help you monitor and troubleshoot connectivity issues to your license server.

Your VPC must meet the following requirements:
+ Your security group must allow outbound TCP on port 8990 (the default Sentieon license server port) to the license server's IP address or FQDN.
+ If your Sentieon license server runs on-premises or in a different AWS account, configure routing through VPN, AWS Direct Connect, or [cross-account VPC access](workflows-vpc-cross-account.md).
+ Your VPC must be in the same AWS Region as the run.

## Step 4: Create a HealthOmics configuration
<a name="sentieon-step-configuration"></a>

If you set the `networkingConfigurationName` parameter in Step 3, the configuration already exists, and you can skip to Step 5. Otherwise, create a configuration that points to your VPC subnets and security groups:

```
aws omics create-configuration \
  --name {{sentieon-vpc-config}} \
  --description "VPC config for Sentieon license access" \
  --run-configurations '{
    "vpcConfig": {
      "securityGroupIds": ["{{sg-0123456789abcdef0}}"],
      "subnetIds": [
        "{{subnet-0a1b2c3d4e5f6g7h8}}",
        "{{subnet-1a2b3c4d5e6f7g8h9}}"
      ]
    }
  }' \
  --region {{us-west-2}}
```

Wait until the configuration status is `ACTIVE` before you start a run. [This typically takes up to 15 minutes](workflows-vpc-networking.md#vpc-step-create-configuration). To check the status, run the following command:

```
aws omics get-configuration \
  --name {{sentieon-vpc-config}}
```

**Note**  
If the status shows `FAILED`, check the configuration details. A common cause on first use is a missing `iam:CreateServiceLinkedRole` permission. Your first configuration automatically creates the HealthOmics service-linked role, which requires this permission.

## Step 5: Update your workflow tasks to use your license server
<a name="sentieon-step-update-workflow"></a>

Update each task that uses Sentieon software to set the `SENTIEON_LICENSE` environment variable to your license server's IP address or FQDN and port (for example, `licsrvr.your-domain:8990`). The task connects to the license server over your VPC network. As a best practice, pass the address as a workflow parameter rather than hardcoding it. This makes the workflow more portable across accounts and VPC configurations.

After you update the workflow, create a workflow or workflow version before you start the run. For examples, see [Sentieon-Amazon-Omics](https://github.com/Sentieon/sentieon-amazon-omics) in GitHub.

## Step 6: Start your run with VPC networking
<a name="sentieon-step-start-run"></a>

When you call `start-run`, add the following parameters:
+ `--networking-mode VPC`
+ `--configuration-name` with the name of the configuration that you created in Step 4
+ `--parameters` with your license server address, which your tasks from Step 5 use

HealthOmics uses the VPC settings in that configuration (subnets and security groups) so that the run can reach your Sentieon license server.

```
aws omics start-run \
  --workflow-id {{1234567}} \
  --role-arn arn:aws:iam::{{123456789012}}:role/{{OmicsWorkflowRole}} \
  --output-uri s3://{{amzn-s3-demo-bucket}}/outputs/ \
  --parameters '{"sentieon_license":"{{licsrvr.your-domain:8990}}"}' \
  --networking-mode VPC \
  --configuration-name {{sentieon-vpc-config}} \
  --region {{us-west-2}}
```

## Step 7: Verify connectivity
<a name="sentieon-step-verify"></a>

Start a test run and confirm that it completes successfully with a valid Sentieon license acquired through the VPC. Check the logs in the `/aws/omics/WorkflowLog` CloudWatch Logs log group for connection success or failure messages.

If a Sentieon task fails during license validation, verify that your security group allows outbound TCP on port 8990, and confirm that the VPC subnets in your HealthOmics configuration have a route to the license server. If the license server is in a different VPC or account, confirm that the peering or transit gateway route is active. For license-specific issues, such as expired licenses, contact Sentieon support at [support@sentieon.com](mailto:support@sentieon.com).