# Troubleshooting

The following page details some common issues encountered while creating or managing ROSA clusters.

###### Topics

- [Access ROSA cluster debug logs](#access-rosa-debug-logs "#access-rosa-debug-logs")
- [ROSA cluster fails AWS service quota check during cluster creation](#service-quotas-missing-error "#service-quotas-missing-error")
- [Troubleshoot ROSA CLI expired offline access tokens](#rosa-cli-expired-token "#rosa-cli-expired-token")
- [Failed to create a cluster with an osdCcsAdmin error](#osdccsadmin-error "#osdccsadmin-error")
- [Next steps](#next-steps "#next-steps")
- [Getting ROSA support](rosa-support.md "rosa-support.md")

## Access ROSA cluster debug logs

To begin to troubleshoot issues with your application, first review the debug logs.
The ROSA CLI debug logs provide details on the error messages that are produced when a cluster fails to create.

To display cluster debug information, run the following ROSA CLI command.
In the command, replace `<cluster_name>` with the name of your cluster.

```
 rosa describe cluster -c <cluster_name> --debug
```

## ROSA cluster fails AWS service quota check during cluster creation

To use ROSA, the service quotas for your account may need increased.
For more information, see [Red Hat OpenShift Service on AWS endpoints and quotas](../../../general/latest/gr/rosa.md "../../../general/latest/gr/rosa.md").

1. Run the following command to identify your account’s quotas.

```
 rosa verify quota
```

###### Note

Quotas are different in different AWS Regions.
Make sure to verify each of the quotas for your Regions. 2. If you need to increase your quota, navigate to the [Service Quotas console](https://console.aws.amazon.com/servicequotas "https://console.aws.amazon.com/servicequotas"). 3. On the navigation pane, choose **AWS services**. 4. Choose the service that needs a quota increase. 5. Select the quota that needs to be increased and choose **Request quota increase**. 6. For **Request quota increase**, enter the total amount that you want the quota to be and choose **Request**.

## Troubleshoot ROSA CLI expired offline access tokens

If you use the ROSA CLI and your [api.openshift.com](https://api.openshift.com/ "https://api.openshift.com/") offline access token expires, an error message appears.
This happens when [sso.redhat.com](https://sso.redhat.com "https://sso.redhat.com") invalidates the token.

1. Navigate to the [OpenShift Cluster Manager API Token page](https://console.redhat.com/openshift/token/rosa "https://console.redhat.com/openshift/token/rosa") and choose **Load Token**.
2. Copy and paste the following authentication command in the terminal.

```
 rosa login --token="<api_token>"
```

## Failed to create a cluster with an osdCcsAdmin error

###### Note

This error occurs only when you use the non-STS method of provisioning ROSA clusters.
To avoid this issue, provision your ROSA clusters using AWS STS.
For more information, see [Create a ROSA classic cluster using the ROSA CLI](getting-started-classic-cli.md "getting-started-classic-cli.md").

If your cluster fails to create, you might receive the following error message:

```
 Failed to create cluster: Unable to create cluster spec: Failed to get access keys for user 'osdCcsAdmin': NoSuchEntity: The user with name osdCcsAdmin cannot be found.
```

1. Delete the stack.

```
 rosa init --delete-stack
```

2. Reinitialize your account.

```
 rosa init
```

## Next steps

- Visit the [OpenShift documentation](https://docs.openshift.com/container-platform/4.16/welcome/ "https://docs.openshift.com/container-platform/4.16/welcome/").
- Open an [Support case](https://console.aws.amazon.com/support "https://console.aws.amazon.com/support") or [Red Hat Support case](https://access.redhat.com/support/ "https://access.redhat.com/support/").
- Find answers to [frequently asked questions about Red Hat OpenShift Service on AWS](https://aws.amazon.com/rosa/faqs/ "https://aws.amazon.com/rosa/faqs/").
- For more information about ROSA’s support model, see [Getting ROSA support](rosa-support.md "rosa-support.md").
