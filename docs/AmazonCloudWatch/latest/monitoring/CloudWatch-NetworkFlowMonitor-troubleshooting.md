# Troubleshoot issues in Network Flow Monitor

This section provides guidance for troubleshooting errors with Network Flow Monitor, including solving issues with
installing agents.

## Troubleshoot issues in EKS agents installation

When you try to upgrade the AWS Network Flow Monitor Agent add-on for EKS from v1.0.0 to v1.0.1 in AWS Management Console, you might receive the following
error message:

"Service account `aws-network-flow-monitoring-agent-service-account` in pod identity configuration is not supported for
addon `aws-network-flow-monitoring-agent`."

This error is returned because a resource was renamed. The EKS add-on v1.0.1 changes the service account name from
`aws-network-flow-monitoring-agent-service-account` to
`aws-network-flow-monitor-agent-service-account`.

Then, if **Not set** is not selected in the console, the pod identity association is not reset to the new
resource name.

To fix this issue, do the following when you upgrade to the new version by using the console:

1. Under **Pod Identity IAM role for service account**, select **Not set**.
2. Select **New version (v1.0.1)**.
3. Select **Upgrade**.
4. Choose **Save changes**.
