# Managing gateway updates

Storage Gateway consists of a managed cloud services component and a gateway appliance component
that you deploy either on-premises, or on an Amazon EC2 instance in the AWS cloud. Both
components receive regular updates. The topics in this section describe the cadence of these
updates, how they are applied, and how to configure update-related settings on the gateways
in your deployment.

###### Important

You should treat the Storage Gateway appliance as a managed virtual machine, and should not
attempt to access or modify its installation or content in any way. Attempting to install or update
any software packages using methods other than the normal AWS gateway update mechanism
(for example, SSM or hypervisor tools) might cause the gateway to malfunction.

Storage Gateway automatically and regularly patches the appliance to maintain security and stability. Storage Gateway appliances use Amazon Linux as their base
operating system. You can check the status of detected Common Vulnerabilities and Exposures (CVE) issues on the
[Amazon Linux Security Center](https://explore.alas.aws.amazon.com/ "https://explore.alas.aws.amazon.com/"). CVE patches are automatically applied within 30 days after they are
released, as shown on the Amazon Linux Security Center. Patches are installed during your gateway maintenance schedule, provided your gateway is online.

Storage Gateway doesn't support manually updating an Amazon EC2 gateway using cloud-init directives. If you use this method to update a gateway, you might encounter
interoperability issues that prevent you from activating or using the gateway appliance.

## Update frequency and expected behavior

AWS updates the cloud services component as needed without causing disruption to
deployed gateways. Your deployed gateway appliances receive monthly maintenance updates.
Monthly maintenance updates can include operating system and software upgrades, fixes to
address stability, performance, and security, and access to new features. All updates
are cumulative, and upgrade gateways to the current version when applied. For
information about the specific changes included in each update, see [Release Notes for Volume Gateway
Appliance Software](release-notes.md "release-notes.md").

Monthly maintenance updates might cause a brief disruption of service. The gateway's VM
host doesn't need to reboot during updates, but the gateway will be unavailable for
a short period while the gateway appliance updates and restarts. You can minimize the
chance of any disruption to your applications due to the gateway restart by increasing
the timeouts of your iSCSI initiator. For more information about increasing iSCSI
initiator timeouts for Windows and Linux, see [Customizing Your Windows iSCSI
Settings](recommendediSCSISettings.md#CustomizeWindowsiSCSISettings "recommendediSCSISettings.md#CustomizeWindowsiSCSISettings") and [Customizing Your Linux iSCSI
Settings](recommendediSCSISettings.md#CustomizeLinuxiSCSISettings "recommendediSCSISettings.md#CustomizeLinuxiSCSISettings").

When you deploy and activate your gateway, a default weekly maintenance window
schedule is set. You can modify the maintenance window schedule at any time. You can
also turn off monthly maintenance updates, but we recommend leaving them turned
on.

###### Note

Urgent updates will sometimes be applied according to the maintenance window
schedule, even if regular maintenance updates are turned off.

Before any update is applied to your gateway, AWS notifies you with a message on the
Storage Gateway console and your AWS Health Dashboard. For more information, see [AWS Health Dashboard](https://aws.amazon.com/premiumsupport/phd/ "https://aws.amazon.com/premiumsupport/phd/"). To modify the email
address where software update notifications are sent, see [Update the alternate contacts for your AWS account](../../../accounts/latest/reference/manage-acct-update-contact-alternate.md "../../../accounts/latest/reference/manage-acct-update-contact-alternate.md") in the _AWS
Account Management Reference Guide_.

When updates are available, the gateway **Details** tab displays a
maintenance message. You can also see the date and time that the last successful update
was applied on the **Details** tab.
