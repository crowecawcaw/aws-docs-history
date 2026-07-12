# Tags applied to managed instances

When Systems Manager onboards an Azure virtual machine through a Cloud Connector, it
automatically applies the following tag to the resulting managed instance. This tag
identifies which Cloud Connector was used to onboard the VM and can be used to filter,
organize, and apply policies to managed instances based on their originating
connector.

| Tag key          | Tag value                                                                                 | Description                                                                                                                                                                                                                                                                                                                                         |
| ---------------- | ----------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CloudConnector` | The Cloud Connector ID as a GUID (for example,<br>`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`) | Identifies the Systems Manager Cloud Connector that was used to onboard the<br>Azure VM as a managed instance. This tag is applied automatically<br>during the onboarding process. You can use this tag to filter<br>managed instances by connector in the Systems Manager console, AWS CLI, or<br>API operations that support tag-based filtering. |

For example, to list all managed instances onboarded through a specific Cloud
Connector, use the following AWS CLI command:

```
aws ssm describe-instance-information \
    --filters "Key=tag:CloudConnector,Values=`CLOUD_CONNECTOR_ID`"
```
