AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Create a hybrid activation to register

nodes with Systems Manager

To set up machines other than Amazon Elastic Compute Cloud (EC2) instances as managed nodes for a
[hybrid and multicloud](operating-systems-and-machine-types.md#supported-machine-types "operating-systems-and-machine-types.md#supported-machine-types") environment, you create and apply a _hybrid
activation_. After you successfully complete the activation, you
_immediately_ receive an Activation Code and Activation ID at the
top of the console page. You specify this Code and ID combination when you install
AWS Systems Manager SSM Agent on non-EC2 machines for your hybrid and multicloud environment. The
Code and ID provide secure access to the Systems Manager service from your managed nodes.

###### Important

Systems Manager immediately returns the Activation Code and ID to the console or the command
window, depending on how you created the activation. Copy this information and store
it in a safe place. If you navigate away from the console or close the command
window, you might lose this information. If you lose it, you must create a new
activation.

###### About activation expirations

An _activation expiration_ is a window of time when you can
register on-premises machines with Systems Manager. An expired activation has no impact on
your servers or VMs that you previously registered with Systems Manager. If an activation
expires then you can’t register more servers or VMs with Systems Manager by using that
specific activation. You simply need to create a new one.

Every on-premises server and VM you previously registered remains registered as a
Systems Manager managed node until you explicitly deregister it. You can deregister a non-EC2
managed node in the following ways:

- Use the **Managed nodes** tab in Fleet Manager in the Systems Manager
  console
- Use the AWS CLI command [deregister-managed-instance](../../../cli/latest/reference/ssm/deregister-managed-instance.md "../../../cli/latest/reference/ssm/deregister-managed-instance.md")
- Use the API action [DeregisterManagedInstance](../APIReference/API_DeregisterManagedInstance.md "../APIReference/API_DeregisterManagedInstance.md").
  For more information, see the following topics

- [Deregister and reregister a managed node (Linux)](hybrid-multicloud-ssm-agent-install-linux.md#systems-manager-install-managed-linux-deregister-reregister "hybrid-multicloud-ssm-agent-install-linux.md#systems-manager-install-managed-linux-deregister-reregister")
- [Deregister and reregister a managed node (Windows Server)](hybrid-multicloud-ssm-agent-install-windows.md#systems-manager-install-managed-win-deregister-reregister "hybrid-multicloud-ssm-agent-install-windows.md#systems-manager-install-managed-win-deregister-reregister")

###### About managed nodes

A managed node is any machine configured for AWS Systems Manager. AWS Systems Manager supports
Amazon Elastic Compute Cloud (Amazon EC2) instances, edge devices, and on-premises servers or VMs, including
VMs in other cloud environments. Previously, managed nodes were all referred to as
managed instances. The term _instance_ now refers
to EC2 instances only. The [deregister-managed-instance](../../../cli/latest/reference/ssm/deregister-managed-instance.md "../../../cli/latest/reference/ssm/deregister-managed-instance.md") command was named before this terminology
change.

###### About activation tags

If you create an activation by using either the AWS Command Line Interface (AWS CLI) or AWS Tools for Windows PowerShell,
you can specify tags. Tags are optional metadata that you assign to a resource. Tags
allow you to categorize a resource in different ways, such as by purpose, owner, or
environment. Here is an AWS CLI sample command to run in the US East (Ohio) Region on a local
Linux machine that includes optional tags.

```
aws ssm create-activation \
  --default-instance-name MyWebServers \
  --description "Activation for Finance department webservers" \
  --iam-role service-role/AmazonEC2RunCommandRoleForManagedInstances \
  --registration-limit 10 \
  --region us-east-2 \
  --tags "Key=`Department`,Value=`Finance`"
```

If you specify tags when you create an activation, then those tags are automatically
assigned to your managed nodes when you activate them.

You can't add tags to or delete tags from an existing activation. If you don't want to
automatically assign tags to your on-premises servers and VMs using an activation, then
you can add tags to them later. More specifically, you can tag your on-premises servers
and VMs after they connect to Systems Manager for the first time. After they connect, they're
assigned a managed node ID and listed in the Systems Manager console with an ID that is prefixed
with "mi-".

###### Note

You can't assign tags to an activation if you create it by using the Systems Manager
console. You must create it by using either the AWS CLI or Tools for Windows PowerShell.

If you no longer want to manage an on-premises server or virtual machine (VM) by using
Systems Manager, you can deregister it. For information, see [Deregistering managed nodes
in a hybrid and multicloud environment](fleet-manager-deregister-hybrid-nodes.md "fleet-manager-deregister-hybrid-nodes.md").

###### Topics

- [Using the AWS Management Console to
  create an activation for registering managed nodes with Systems Manager](#create-managed-node-activation-console "#create-managed-node-activation-console")
- [Using the command line
  to create an activation for registering managed nodes with Systems Manager](#create-managed-node-activation-command-line "#create-managed-node-activation-command-line")

## Using the AWS Management Console to

create an activation for registering managed nodes with Systems Manager

###### To create a managed-node activation

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Hybrid Activations**.
3. Choose **Create activation**.

-or-

If you are accessing **Hybrid Activations** for the first
time in the current AWS Region, choose **Create an
Activation**. 4. (Optional) For **Activation description**, enter a
description for this activation. We recommend entering a description if you
plan to activate large numbers of servers and VMs. 5. For
**Instance
limit**, specify
the total number of nodes that you want to register with AWS as part of
this activation. The default value is 1 instance. 6. For **IAM role**, choose a service role option that
allows your servers and VMs to communicate with AWS Systems Manager in the
cloud:

    * **Option 1**: Choose **Use
     the default role created by the system** to use a role
     and managed policy provided by AWS.
    * **Option 2**: Choose **Select
     an existing custom IAM role that has the required
     permissions** to use the optional custom role you
     created earlier. This role must have a trust relationship policy
     that specifies `"Service": "ssm.amazonaws.com"`. If your
     IAM role doesn't specify this principle in a trust relationship
     policy, you receive the following error:



    ```
    An error occurred (ValidationException) when calling the CreateActivation
                                        operation: Not existing role: arn:aws:iam::<accountid>:role/SSMRole
    ```

    For more information about creating this role, see [Create the IAM service role required
     for Systems Manager in hybrid and multicloud environments](hybrid-multicloud-service-role.md "hybrid-multicloud-service-role.md").

7. For **Activation expiry date**, specify an expiration
   date for the activation. The expiry date must be in the future, and not more
   than 30 days into the future. The default value is 24 hours.

###### Note

If you want to register additional managed nodes after the expiry
date, you must create a new activation. The expiry date has no impact on
registered and running nodes. 8. (Optional) For **Default instance name** field, specify
an identifying name value to be displayed for all managed nodes associated
with this activation. 9. Choose **Create activation**. Systems Manager immediately returns
the Activation Code and ID to the console.

## Using the command line

to create an activation for registering managed nodes with Systems Manager

The following procedure describes how to use the AWS Command Line Interface (AWS CLI) (on Linux or
Windows Server) or AWS Tools for PowerShell to create a managed node
activation.

###### To create an activation

1. Install and configure the AWS CLI or the AWS Tools for PowerShell, if you haven't already.

For information, see [Installing or updating the
latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") and [Installing the
AWS Tools for PowerShell](../../../powershell/latest/userguide/pstools-getting-set-up.md "../../../powershell/latest/userguide/pstools-getting-set-up.md"). 2. Run the following command to create an activation.

###### Note

    * In the following command, replace `region` with your own
     information. For a list of supported `region` values, see the
     **Region** column in [Systems Manager service endpoints](../../../general/latest/gr/ssm.md#ssm_region "../../../general/latest/gr/ssm.md#ssm_region") in the
     *Amazon Web Services General Reference*.
    * The role you specify for the
     `iam-role` parameter must have a
     trust relationship policy that specifies `"Service":
     "ssm.amazonaws.com"`. If your AWS Identity and Access Management (IAM) role
     doesn't specify this principle in a trust relationship policy,
     you receive the following error:



    ```
    An error occurred (ValidationException) when calling the CreateActivation
                                            operation: Not existing role: arn:aws:iam::<accountid>:role/SSMRole
    ```

    For more information about creating this role, see [Create the IAM service role required
     for Systems Manager in hybrid and multicloud environments](hybrid-multicloud-service-role.md "hybrid-multicloud-service-role.md").
    * For `--expiration-date`, provide a date in
     timestamp format, such as `"2021-07-07T00:00:00"`,
     for when the activation code expires. You can specify a date up
     to 30 days in advance. If you don't provide an expiration date,
     the activation code expires in 24 hours.

Linux & macOS

```
aws ssm create-activation \
    --default-instance-name `name` \
    --iam-role `iam-service-role-name` \
    --registration-limit `number-of-managed-instances` \
    --region `region` \
    --expiration-date "`timestamp`" \\
    --tags "Key=`key-name-1`,Value=`key-value-1`" "Key=`key-name-2`,Value=`key-value-2`"
```

Windows

```
aws ssm create-activation ^
    --default-instance-name `name` ^
    --iam-role `iam-service-role-name` ^
    --registration-limit `number-of-managed-instances` ^
    --region `region` ^
    --expiration-date "`timestamp`" ^
    --tags "Key=`key-name-1`,Value=`key-value-1`" "Key=`key-name-2`,Value=`key-value-2`"
```

PowerShell

```
New-SSMActivation -DefaultInstanceName `name` `
    -IamRole `iam-service-role-name` `
    -RegistrationLimit `number-of-managed-instances` `
    –Region `region` `
    -ExpirationDate "`timestamp`" `
    -Tag @{"Key"="`key-name-1`";"Value"="`key-value-1`"},@{"Key"="`key-name-2`";"Value"="`key-value-2`"}
```

Here is an example.

Linux & macOS

```
aws ssm create-activation \
    --default-instance-name MyWebServers \
    --iam-role service-role/AmazonEC2RunCommandRoleForManagedInstances \
    --registration-limit 10 \
    --region us-east-2 \
    --expiration-date "2021-07-07T00:00:00" \
    --tags "Key=Environment,Value=Production" "Key=Department,Value=Finance"
```

Windows

```
aws ssm create-activation ^
    --default-instance-name MyWebServers ^
    --iam-role service-role/AmazonEC2RunCommandRoleForManagedInstances ^
    --registration-limit 10 ^
    --region us-east-2 ^
    --expiration-date "2021-07-07T00:00:00" ^
    --tags "Key=Environment,Value=Production" "Key=Department,Value=Finance"
```

PowerShell

```
New-SSMActivation -DefaultInstanceName MyWebServers `
    -IamRole service-role/AmazonEC2RunCommandRoleForManagedInstances `
    -RegistrationLimit 10 `
    –Region us-east-2 `
    -ExpirationDate "2021-07-07T00:00:00" `
    -Tag @{"Key"="Environment";"Value"="Production"},@{"Key"="Department";"Value"="Finance"}
```

If the activation is created successfully, the system immediately returns
an Activation Code and ID.
