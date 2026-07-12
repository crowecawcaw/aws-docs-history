# Enable VM onboarding (AWS CLI)

To enable VM onboarding using the AWS CLI, create a State Manager association
that targets the Cloud Connector. The command requires the following
roles:

- `AutomationAssumeRole` – The Automation execution
  role that the runbook assumes to create activations and authenticate
  with Azure. See [Automation assume role](cloud-connector-automation-assume-role.md "cloud-connector-automation-assume-role.md").
- `ManagedInstanceIamRole` – The hybrid activation
  instance role assigned to VMs when they register as managed instances.
  See [Managed instance role](cloud-connector-managed-instance-role.md "cloud-connector-managed-instance-role.md").
- `--association-dispatch-assume-role` –
  The State Manager dispatch role that launches the Automation. See [Automation dispatch role](cloud-connector-automation-dispatch-role.md "cloud-connector-automation-dispatch-role.md").

```
aws ssm create-association \
    --association-name "AWSSSMAzureConnector-`CLOUD_CONNECTOR_ID`" \
    --name "AWS-InstallSSMAgentOnAzure" \
    --automation-target-parameter-name "AzureVmResourceId" \
    --association-dispatch-assume-role "arn:aws:iam::`ACCOUNT_ID`:role/service-role/`DISPATCH_ROLE_NAME`" \
    --parameters '{
        "AutomationAssumeRole": ["arn:aws:iam::`ACCOUNT_ID`:role/service-role/`ASSUME_ROLE_NAME`"],
        "ManagedInstanceIamRole": ["service-role/AmazonEC2RunCommandRoleForManagedInstances"],
        "CloudConnector": ["`CLOUD_CONNECTOR_ID`"]
    }' \
    --targets 'Key=CloudConnector,Values=["{\"CloudConnectorId\":\"`CLOUD_CONNECTOR_ID`\",\"SsmManagedNodeFilter\":\"UNMANAGED\"}"]' \
    --schedule-expression "rate(48 hours)" \
    --max-concurrency "50"
```

To target specific Azure Regions, add the
`CloudProviderRegions` field to the target value:

```
--targets 'Key=CloudConnector,Values=["{\"CloudConnectorId\":\"`CLOUD_CONNECTOR_ID`\",\"SsmManagedNodeFilter\":\"UNMANAGED\",\"CloudProviderRegions\":[\"eastus\",\"westus2\"]}"]'
```

To add custom tags to managed instances during onboarding, include the
`ManagedInstanceTags` parameter:

```
--parameters '{
    "AutomationAssumeRole": ["arn:aws:iam::`ACCOUNT_ID`:role/service-role/`ASSUME_ROLE_NAME`"],
    "ManagedInstanceIamRole": ["service-role/AmazonEC2RunCommandRoleForManagedInstances"],
    "CloudConnector": ["`CLOUD_CONNECTOR_ID`"],
    "ManagedInstanceTags": ["{\"Key\":\"Environment\",\"Value\":\"Production\"}","{\"Key\":\"Team\",\"Value\":\"DevOps\"}"]
}'
```
