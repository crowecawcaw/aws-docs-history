# Prerequisites for user management in CloudHSM CLI

Before you use CloudHSM CLI to manage hardware security modules (HSM) users in AWS CloudHSM, you must complete these prerequisites. The following topics describe getting started with the CloudHSM CLI.

###### Topics

- [Get the HSM IP address](#manage-chsm-cli-users-ip "#manage-chsm-cli-users-ip")
- [Download CloudHSM CLI](#get-cli-users-cloudhsm-cli "#get-cli-users-cloudhsm-cli")

## Get the IP address of an HSM in AWS CloudHSM

To use CloudHSM CLI, you must use the configure tool to update the local configuration. For
instructions on running the configure tool with CloudHSM CLI, see [Getting started with AWS CloudHSM Command Line
Interface (CLI)](cloudhsm_cli-getting-started.md "cloudhsm_cli-getting-started.md"). The
`-a` parameter requires you to add the IP address of an HSM in your cluster. If
you have multiple HSMs, you can use any IP address. This ensures CloudHSM CLI can propagate any
changes you make across the entire cluster. Remember that CloudHSM CLI uses its local file to
track cluster information. If the cluster has changed since the last time you used CloudHSM CLI
from a particular host, you must add those changes to the local configuration file stored on
that host. Never remove an HSM while you're using CloudHSM CLI.

###### To get an IP address for an HSM (console)

1. Open the AWS CloudHSM console at
   [https://console.aws.amazon.com/cloudhsm/home](https://console.aws.amazon.com/cloudhsm/home "https://console.aws.amazon.com/cloudhsm/home").
2. To change the AWS Region, use the Region selector in the upper-right corner of the
   page.
3. To open the cluster detail page, in the cluster table, choose the cluster ID.
4. To get the IP address, go to the HSMs tab. For IPv4 clusters, choose an address listed under **ENI IPv4 address**. For dual-stack clusters use either the ENI IPv4 or the **ENI IPv6 address**.

###### To get an IP address for an HSM (AWS CLI)

- Get the IP address of an HSM by using the **[describe-clusters](../../../cli/latest/reference/cloudhsmv2/describe-clusters.md "../../../cli/latest/reference/cloudhsmv2/describe-clusters.md")** command from the AWS CLI. In the output from the command,
  the IP address of the HSMs are the values of `EniIp` and `EniIpV6` (if it is a dual-stack cluster).

```
`$` `aws cloudhsmv2 describe-clusters`
`{
 "Clusters": [
 { ... }
 "Hsms": [
 {
...
 "EniIp": "10.0.0.9",
...
 },
 {
...
 "EniIp": "10.0.1.6",
 "EniIpV6": "2600:113f:404:be09:310e:ed34:3412:f733",
...`
```

## Download CloudHSM CLI

The latest version of CloudHSM CLI is available for HSM user management tasks for
Client SDK 5. To download and install CloudHSM CLI, follow the instructions in [Install and configure CloudHSM CLI](gs_cloudhsm_cli-install.md "gs_cloudhsm_cli-install.md").
