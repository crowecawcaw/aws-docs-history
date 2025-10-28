# Manage VSS components package

for Windows VSS based EBS snapshots

Before you create VSS based EBS snapshots, ensure that you have the latest version of the VSS
components package installed on your Windows instance. There are several ways that you can install
the `AwsVssComponents` package onto an existing instance, as follows:

- (Recommended) [Run the
  AWSEC2-VssInstallAndSnapshot command document (recommended)](create-vss-snapshots-ssm.md#create-with-AWSEC2-VssInstallAndSnapshot "create-vss-snapshots-ssm.md#create-with-AWSEC2-VssInstallAndSnapshot"). This automatically
  installs or updates if needed every time it runs.
- [Manually install the VSS components on an EC2 Windows instance](#install-vss-comps "#install-vss-comps").
- [Update the VSS components package on your EC2 Windows instance](#update-vss-comps "#update-vss-comps").
  You can also create an AMI with EC2 Image Builder that uses the
  `aws-vss-components-windows` managed component to install the
  `AwsVssComponents` package for the image. The managed component
  uses AWS Systems Manager Distributor to install the package. After Image Builder creates the image, every
  instance that you launch from the associated AMI will have the VSS package installed
  on it. For more information about how you can create an AMI with the VSS package installed,
  see [Distributor
  package managed components for Windows](../../../imagebuilder/latest/userguide/mgdcomponent-distributor-win.md "../../../imagebuilder/latest/userguide/mgdcomponent-distributor-win.md") in the
  _EC2 Image Builder User Guide_.

###### Contents

- [Manual install](#install-vss-comps "#install-vss-comps")
- [Update components](#update-vss-comps "#update-vss-comps")

## Manually install the VSS components on an EC2 Windows instance

Your EC2 Windows instance must have VSS components installed before you can create
application-consistent snapshots with Systems Manager. If you don't run the
`AWSEC2-VssInstallAndSnapshot` command document to automatically
install or update the package every time you create application-consistent snapshots,
you must manually install the package.

You must also install manually if you plan to use one of the following methods to
create application-consistent snapshots from your EC2 instance.

- Create VSS snapshots using AWS Backup
- Create VSS snapshots using Amazon Data Lifecycle Manager

If you need to perform a manual install, we recommend that you use
the latest AWS VSS component package to improve the reliability and
performance of application-consistent snapshots on your EC2 Windows
instances.

###### Note

To automatically install or update the `AwsVssComponents`
package whenever you create application-consistent snapshots, we recommend that
you use Systems Manager to run the `AWSEC2-VssInstallAndSnapshot` document. For
more information, see [Run the
AWSEC2-VssInstallAndSnapshot command document (recommended)](create-vss-snapshots-ssm.md#create-with-AWSEC2-VssInstallAndSnapshot "create-vss-snapshots-ssm.md#create-with-AWSEC2-VssInstallAndSnapshot").

To install the VSS components on an Amazon EC2 Windows instance, follow the steps for
your preferred environment.

Console

###### To install the VSS components using SSM Distributor

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Run Command**.
3. Choose **Run command**.
4. For **Command document**, choose the button next to
   **AWS-ConfigureAWSPackage**.
5. For **Command parameters**, do the following:
   1. Verify that **Action** is set to
      **Install**.
   2. For **Name**, enter
      `AwsVssComponents`.
   3. For **Version**, enter a version or leave the field
      empty so that Systems Manager installs the latest version.

6. For **Targets**, identify the instances on which you want
   to run this operation by specifying tags or selecting instances
   manually.

###### Note

If you choose to select instances manually, and an instance you expect
to see is not included in the list, see [Where Are My Instances?](../../../systems-manager/latest/userguide/troubleshooting-remote-commands.md#where-are-instances "../../../systems-manager/latest/userguide/troubleshooting-remote-commands.md#where-are-instances") in the
_AWS Systems Manager User Guide_ for troubleshooting
tips. 7. For **Other parameters**:

    * (Optional) For **Comment**, type information
     about this command.
    * For **Timeout (seconds)**, specify the number of
     seconds for the system to wait before failing the overall command
     execution.

8. (Optional) For **Rate control**:
   - For **Concurrency**, specify either a number or a
     percentage of instances on which to run the command at the same
     time.

   ###### Note

   If you selected targets by choosing Amazon EC2 tags, and you are
   not certain how many instances use the selected tags, then limit
   the number of instances that can run the document at the same
   time by specifying a percentage.
   - For **Error threshold**, specify when to stop
     running the command on other instances after it fails on either a
     number or a percentage of instances. For example, if you specify
     three errors, then Systems Manager stops sending the command when the fourth
     error is received. Instances still processing the command might also
     send errors.

9. (Optional) For **Output options** section, if you want to
   save the command output to a file, select the box next to **Enable
   writing to an S3 bucket**. Specify the bucket and (optional)
   prefix (folder) names.

###### Note

The S3 permissions that grant the ability to write the data to an S3
bucket are those of the instance profile assigned to the instance, not
those of the user performing this task. For more information, see
[Configure EC2 instance permissions](../../../systems-manager/latest/userguide/setup-instance-permissions.md#instance-profile-add-permissions "../../../systems-manager/latest/userguide/setup-instance-permissions.md#instance-profile-add-permissions") in the
_AWS Systems Manager User Guide_. 10. (Optional) Specify options for **SNS
notifications**.

For information about configuring Amazon SNS notifications for Run Command, see
[Configuring
Amazon SNS Notifications for AWS Systems Manager](../../../systems-manager/latest/userguide/monitoring-sns-notifications.md "../../../systems-manager/latest/userguide/monitoring-sns-notifications.md"). 11. Choose **Run**.

AWS CLI
Use the following procedure to download and install the
`AwsVssComponents` package on your instances
by using Run Command from the AWS CLI. The package installs two
components: a VSS requester and a VSS provider. The system copies
these components to a directory on the instance, and then registers
the provider DLL as a VSS provider.

###### To install the VSS package

Run the following command to download and install the required VSS
components for Systems Manager.

```
aws ssm send-command \
    --document-name "AWS-ConfigureAWSPackage" \
    --instance-ids "`i-1234567890abcdef0`" \
    --parameters '{"action":["Install"],"name":["AwsVssComponents"]}'
```

PowerShell
Use the following procedure to download and install the
`AwsVssComponents` package on your instances
by using Run Command from the Tools for Windows PowerShell. The package installs two
components: a VSS requester and a VSS provider. The system copies
these components to a directory on the instance, and then registers
the provider DLL as a VSS provider.

###### To install the VSS package

Run the following command to download and install the required VSS
components for Systems Manager.

```
Send-SSMCommand `
    -DocumentName "AWS-ConfigureAWSPackage" `
    -InstanceId "`i-1234567890abcdef0`" `
    -Parameter @{'action'='Install';'name'='AwsVssComponents'}
```

### Verify the signature on AWS VSS components

Use the following procedure to verify the signature on the `AwsVssComponents` package.

1. Connect to your Windows instance. For more information, see [Connect to your Windows instance using RDP](connecting_to_windows_instance.md "connecting_to_windows_instance.md").
2. Navigate to C:\Program Files\Amazon\AwsVssComponents.
3. Open the context (right-click) menu for `ec2-vss-agent.exe`, and then choose
   **Properties**.
4. Navigate to the **Digital Signatures**
   tab and verify that the name of the signer is Amazon Web Services Inc.
5. Use the preceding steps to verify the signature on `Ec2VssInstaller` and
   `Ec2VssProvider.dll`.

## Update the VSS components package on your EC2 Windows instance

We recommend that you keep the VSS components updated with the latest recommended
version. There are several different ways that you can update components when a new version
of the `AwsVssComponents` package is released.

###### Update methods

- You can repeat the steps described in [Manually install the VSS components on an EC2 Windows instance](#install-vss-comps "#install-vss-comps") when a new version of the AWS VSS components
  is released.
- You can configure a Systems Manager State Manager association to automatically download and
  install new or updated VSS components when the `AwsVssComponents`
  package becomes available.
- You can automatically install or update the `AwsVssComponents`
  package whenever you create application-consistent snapshots, when you use Systems Manager to run
  the `AWSEC2-VssInstallAndSnapshot` document.

###### Note

We recommend that you use Systems Manager to run the `AWSEC2-VssInstallAndSnapshot`
command document, which automatically installs or updates the
`AwsVssComponents` package before it creates the
application-consistent snapshots. For more information, see
[Run the
AWSEC2-VssInstallAndSnapshot command document (recommended)](create-vss-snapshots-ssm.md#create-with-AWSEC2-VssInstallAndSnapshot "create-vss-snapshots-ssm.md#create-with-AWSEC2-VssInstallAndSnapshot").

To create a Systems Manager State Manager association, follow the steps for your preferred
environment.

Console
When you create a Systems Manager State Manager association, there are two options
for updating the `AwsVssComponents` package, as follows:

**Uninstall and reinstall**

This method downloads and installs the package with no
additional prerequisites.

**In-place update**

This performs an in-place update for the package, and
has the following prerequisites:

- The SSM Agent version that's installed on the instance must be
  version `3.3.808.0` or later. For more information, see
  [Working
  with SSM Agent on EC2 instances for Windows Server](../../../systems-manager/latest/userguide/ssm-agent-windows.md "../../../systems-manager/latest/userguide/ssm-agent-windows.md") in the
  _AWS Systems Manager User Guide_.
- If specified, the `AwsVssComponents` package version must
  be version `2.5.0` or later. Earlier versions don't support
  in-place update.

###### Note

if your instance doesn't meet these prerequisites, in-place update will fail.
Use the **Uninstall and reinstall** option instead.

###### To create a State Manager association

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **State Manager**.

Or, if the Systems Manager homepage opens first, open the navigation
pane and then choose **State Manager**. 3. Choose **Create association**. 4. In the **Name** field, enter a descriptive name. 5. In the **Document** list, choose **AWS-ConfigureAWSPackage**. 6. In the **Parameters** section, choose
**Install** from the **Action** list. 7. For **Installation type**, choose either
**Uninstall and reinstall** or
**In-place update**. 8. In the **Name** field, enter `AwsVssComponents`.
You can keep the **Version** and **Additional Arguments**
fields empty. 9. In the **Targets** section, choose an option.

###### Note

If you choose to target instances by using tags, and you specify tags that
map to Linux instances, the association succeeds on the Windows instance but
fails on the Linux instances. The overall status of the association shows
**Failed**. 10. In the **Specify schedule** section, choose an option. 11. In the **Advanced options** section, for **Compliance severity**,
choose a severity level for the association. For more information, see [Learn about association compliance](../../../systems-manager/latest/userguide/compliance-about.md "../../../systems-manager/latest/userguide/compliance-about.md").
For **Change Calendars**, select a preconfigured change calendar. For more information,
see about [AWS Systems Manager Change Calendar](../../../systems-manager/latest/userguide/systems-manager-change-calendar.md "../../../systems-manager/latest/userguide/systems-manager-change-calendar.md"). 12. For **Rate control**, do the following:

    * For **Concurrency**, specify either a number or a
     percentage of managed nodes on which to run the command at the same time.
    * For **Error threshold**, specify when to stop running
     the command on other managed nodes after it fails on either a number or a
     percentage of nodes.

13. (Optional) For **Output options**, to save the command
    output to a file, select **Enable writing output to S3**.
    Enter the bucket and prefix (folder) names in the boxes.
14. Choose **Create association**, and then choose
    **Close**. The system attempts to create the
    association on the instances and immediately apply the state.

###### Note

If EC2 instances for Windows Server show a status of **Failed**,
verify that the SSM Agent is running on the instance, and verify that the instance
is configured with an AWS Identity and Access Management (IAM) role for Systems Manager. For more information, see
[Setting up AWS Systems Manager](../../../systems-manager/latest/userguide/systems-manager-setting-up-ec2.md "../../../systems-manager/latest/userguide/systems-manager-setting-up-ec2.md").

AWS CLI
Use the [create-association](../../../cli/latest/reference/ssm/create-association.md "../../../cli/latest/reference/ssm/create-association.md") command to update a Distributor package on a schedule without
taking the associated application offline. Only new or updated files in the package are replaced.

###### To create a State Manager association

Run the following command to create an association. The value of `--name`,
the document name, is always `AWS-ConfigureAWSPackage`. The following command
uses the key `InstanceIds` to specify target instances.

```
aws ssm create-association \
    --name "AWS-ConfigureAWSPackage" \
    --parameters action=Install,installationType="Uninstall and reinstall",name=AwsVssComponents \
    --targets Key=InstanceIds,Values=`i-1234567890abcdef0`,`i-000011112222abcde`
```

PowerShell

###### To create a State Manager association

Use the [New-SSMAssociation](../../../powershell/latest/reference/items/New-SSMAssociation.md "../../../powershell/latest/reference/items/New-SSMAssociation.md")
cmdlet.

```
New-SSMAssociation `
    -Name "AWS-ConfigureAWSPackage" `
    -Parameter  @{
        "action" = "Install"
        "installationType" = "Uninstall and reinstall"
        "name" = "AwsVssComponents"
    } `
    -Target @{
        "Key" = "InstanceIds"
        "Values" = @("`i-1234567890abcdef0`", "`i-000011112222abcde`")
    }
```
