

# Enable VM onboarding (AWS CLI)

To enable VM onboarding using the AWS CLI, create a State Manager association that targets the Cloud Connector. The command requires the following roles:
+ `AutomationAssumeRole` – The Automation execution role that the runbook assumes to create activations and authenticate with GCP. See [Automation assume role](cloud-connector-gcp-automation-assume-role.md).
+ `ManagedInstanceIamRole` – The hybrid activation instance role assigned to VMs when they register as managed instances. See [Managed instance role](cloud-connector-gcp-managed-instance-role.md).
+ `--association-dispatch-assume-role` – The State Manager dispatch role that launches the Automation. See [Automation dispatch role](cloud-connector-gcp-automation-dispatch-role.md).

```
aws ssm create-association \
    --association-name "AWSSSMGcpConnector-{{CLOUD_CONNECTOR_ID}}" \
    --name "AWS-InstallSSMAgentOnGCP" \
    --association-dispatch-assume-role "arn:aws:iam::{{ACCOUNT_ID}}:role/service-role/{{DISPATCH_ROLE_NAME}}" \
    --parameters '{
        "AutomationAssumeRole": ["arn:aws:iam::{{ACCOUNT_ID}}:role/service-role/{{ASSUME_ROLE_NAME}}"],
        "ManagedInstanceIamRole": ["service-role/AmazonEC2RunCommandRoleForManagedInstances"],
        "CloudConnector": ["{{CLOUD_CONNECTOR_ID}}"]
    }' \
    --schedule-expression "rate(48 hours)"
```

To limit onboarding to specific GCP Regions or projects, add the `GCPRegions` and `GCPProjectIds` parameters. For `GCPRegions`, specify up to 25 GCP Regions (such as `us-central1`). Each Region includes all of its zones. If you omit this parameter, the runbook onboards VMs in every zone of every project in scope. For `GCPProjectIds`, specify up to 25 project IDs, each of which must be in the connector's scope. If you omit this parameter, the runbook uses the connector's projects. The following example sets both parameters:

```
--parameters '{
    "AutomationAssumeRole": ["arn:aws:iam::{{ACCOUNT_ID}}:role/service-role/{{ASSUME_ROLE_NAME}}"],
    "ManagedInstanceIamRole": ["service-role/AmazonEC2RunCommandRoleForManagedInstances"],
    "CloudConnector": ["{{CLOUD_CONNECTOR_ID}}"],
    "GCPProjectIds": ["{{my-project-prod}}"],
    "GCPRegions": ["us-central1", "us-east1"]
}'
```

To add custom tags to managed instances during onboarding, include the `ManagedInstanceTags` parameter. Tag keys can't start with `aws:` or use the reserved key `CloudConnector`.

```
--parameters '{
    "AutomationAssumeRole": ["arn:aws:iam::{{ACCOUNT_ID}}:role/service-role/{{ASSUME_ROLE_NAME}}"],
    "ManagedInstanceIamRole": ["service-role/AmazonEC2RunCommandRoleForManagedInstances"],
    "CloudConnector": ["{{CLOUD_CONNECTOR_ID}}"],
    "ManagedInstanceTags": ["{\"Key\":\"Environment\",\"Value\":\"Production\"}","{\"Key\":\"Team\",\"Value\":\"DevOps\"}"]
}'
```