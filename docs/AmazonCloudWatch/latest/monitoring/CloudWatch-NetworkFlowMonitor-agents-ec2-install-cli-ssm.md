# Install agents using AWS CLI with SSM commands

You can use the AWS Command Line Interface to send AWS Systems Manager commands to install and activate Network Flow Monitor agents on your EC2 instances.
This method is useful for scripted or automated deployments.

###### Step 1: Install the agent

Use the following AWS CLI command to install the Network Flow Monitor agent on one or more EC2 instances using the
`AWS-ConfigureAWSPackage` SSM document:

```
aws ssm send-command --document-name "AWS-ConfigureAWSPackage" \
  --parameters '{"action":["Install"],"installationType":["Uninstall and reinstall"],"name":["AmazonCloudWatchNetworkFlowMonitorAgent"],"version":[""],"additionalArguments":["{}"]}' \
  --targets "Key=instanceids,Values=`i-1234567890abcdef0`"
```

Replace `i-1234567890abcdef0` with the instance ID (or IDs) where you want to install the agent.
You can specify multiple instance IDs separated by commas.

###### Step 2: Activate the agent

After the installation completes, activate the agent so it begins sending performance metrics to the Network Flow Monitor backend.
Activating the agent incurs billing costs. For more information about pricing, see the
[Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/") page.

```
aws ssm send-command --document-name "AmazonCloudWatch-NetworkFlowMonitorManageAgent" \
  --parameters '{"Action":["Activate"]}' \
  --targets "Key=instanceids,Values=`i-1234567890abcdef0`"
```

After the agent is activated, it begins collecting and sending performance metrics. You should see data on the
**Workload insights** page within approximately 20 minutes.
