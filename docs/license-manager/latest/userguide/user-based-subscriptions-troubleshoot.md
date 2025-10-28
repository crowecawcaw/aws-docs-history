# Troubleshoot user-based

subscriptions in License Manager

The following are troubleshooting tips to help solve issues that can occur with
user-based subscriptions in AWS License Manager.

###### Contents

- [Troubleshoot
  instance compliance](user-based-subscriptions-troubleshoot.md#user-based-subscriptions-troubleshoot-instance-compliance "user-based-subscriptions-troubleshoot.md#user-based-subscriptions-troubleshoot-instance-compliance")
- [Troubleshoot license
  compliance](user-based-subscriptions-troubleshoot.md#user-based-subscriptions-troubleshoot-license-compliance "user-based-subscriptions-troubleshoot.md#user-based-subscriptions-troubleshoot-license-compliance")
- [Troubleshoot
  instance connectivity](user-based-subscriptions-troubleshoot.md#user-based-subscriptions-troubleshoot-instance-connectivity "user-based-subscriptions-troubleshoot.md#user-based-subscriptions-troubleshoot-instance-connectivity")
- [Troubleshoot failures to
  join the domain](user-based-subscriptions-troubleshoot.md#user-based-subscriptions-troubleshoot-domain-join "user-based-subscriptions-troubleshoot.md#user-based-subscriptions-troubleshoot-domain-join")
- [Troubleshoot Systems Manager connectivity](user-based-subscriptions-troubleshoot.md#user-based-subscriptions-troubleshoot-systems-manager-connectivity "user-based-subscriptions-troubleshoot.md#user-based-subscriptions-troubleshoot-systems-manager-connectivity")
- [Troubleshoot
  Systems Manager Run Command](user-based-subscriptions-troubleshoot.md#user-based-subscriptions-troubleshoot-systems-manager-commands "user-based-subscriptions-troubleshoot.md#user-based-subscriptions-troubleshoot-systems-manager-commands")
- [Troubleshoot Microsoft RDS Licensing failures](user-based-subscriptions-troubleshoot.md#usubs-troubleshoot-rds-licensing "user-based-subscriptions-troubleshoot.md#usubs-troubleshoot-rds-licensing")
- [Troubleshoot Microsoft Office activation failures](user-based-subscriptions-troubleshoot.md#usubs-troubleshoot-office-activation "user-based-subscriptions-troubleshoot.md#usubs-troubleshoot-office-activation")

## Troubleshoot

instance compliance

Instances providing user-based subscriptions must remain in a healthy status to be in
compliance. Instances that are marked as unhealthy no longer meet the required
prerequisites. License Manager will attempt to return the instance to a healthy status, but
instances that are not able to return to a healthy status are terminated.

Instances which are launched to provide user-based subscriptions and are unable to
complete the initial configuration will be terminated. You must correct the
configuration issue and launch new instances to provide user-based subscriptions in this
scenario. For more information, see the [Prerequisites to create
user-based subscriptions in License Manager](user-based-subscriptions.md#usubs-prerequisites "user-based-subscriptions.md#usubs-prerequisites").

## Troubleshoot license

compliance

If you configured your Active Directory to provide user-based subscriptions with Microsoft Office, you
must ensure your resources can connect to the VPC endpoints License Manager creates. The endpoints
require inbound traffic on TCP port 1688 from the instances providing user-based
subscriptions.

You can use [Reachability Analyzer](../../../vpc/latest/reachability/what-is-reachability-analyzer.md "../../../vpc/latest/reachability/what-is-reachability-analyzer.md") to
help confirm that the networking configuration from your instances providing user-based
subscriptions and the VPC endpoints are configured properly. You can specify an instance
ID launched in a subnet providing user-based subscriptions as the source, and a VPC
endpoint provisioned for Microsoft Office products as the destination. Specify TCP as the protocol
and 1688 for the destination port for the path to analyze. For more information, see
[How can
I troubleshoot connectivity issues over my gateway and interface VPC
endpoints?](https://aws.amazon.com/premiumsupport/knowledge-center/vpc-fix-gateway-or-interface-endpoint/ "https://aws.amazon.com/premiumsupport/knowledge-center/vpc-fix-gateway-or-interface-endpoint/").

## Troubleshoot

instance connectivity

Users must be able to use RDP to connect to the instances providing user-based
subscriptions in order to use the products within. For more information on
troubleshooting instance connectivity, see [Troubleshoot connecting to your Windows instance](../../../AWSEC2/latest/UserGuide/troubleshoot-connect-windows-instance.md "../../../AWSEC2/latest/UserGuide/troubleshoot-connect-windows-instance.md") in the
_Amazon EC2 User Guide_.

## Troubleshoot failures to

join the domain

Users must be able to connect to the instances providing the user-based subscription
products with their user identities from the Active Directory configured in the License Manager settings.
Instances that fail to join the domain will be terminated.

To troubleshoot, you may need to launch an instance and [manually join
the domain](../../../directoryservice/latest/admin-guide/join_windows_instance.md "../../../directoryservice/latest/admin-guide/join_windows_instance.md") so that the resource is not terminated before you can investigate.
The instance must receive and execute the Systems Manager Run Command successfully, and the
instance must also be able to complete the domain join within the operating system. For
more information, see [Understanding command
statuses](../../../systems-manager/latest/userguide/monitor-commands.md "../../../systems-manager/latest/userguide/monitor-commands.md") in the _AWS Systems Manager User Guide_ and [How to troubleshoot errors that occur when you join Windows-based computers to a
domain](https://docs.microsoft.com/en-US/troubleshoot/windows-server/identity/troubleshoot-errors-join-computer-to-domain "https://docs.microsoft.com/en-US/troubleshoot/windows-server/identity/troubleshoot-errors-join-computer-to-domain") on the Microsoft website.

If you launch instances from a custom AMI that uses a user-based subscription product AMI
as its base image, you must perform Sysprep steps on the custom AMI to ensure a unique
computer name at launch. Before you run Sysprep with /generalize, ensure that the machine
is removed from the domain.

## Troubleshoot Systems Manager connectivity

Instances that provide user-based subscriptions must be managed by AWS Systems Manager or they
will be terminated. For more information, see [Troubleshooting
SSM Agent](../../../systems-manager/latest/userguide/troubleshooting-ssm-agent.md "../../../systems-manager/latest/userguide/troubleshooting-ssm-agent.md") and [Troubleshooting managed node availability](../../../systems-manager/latest/userguide/troubleshooting-managed-instances.md "../../../systems-manager/latest/userguide/troubleshooting-managed-instances.md") in the _AWS Systems Manager User
Guide_.

## Troubleshoot

Systems Manager Run Command

Run Command, a capability of Systems Manager, is used with instances providing user-based
subscriptions to join the domain, harden the operating system, and perform access audits
for the included product. For more information, see [Understanding command
statuses](../../../systems-manager/latest/userguide/monitor-commands.md "../../../systems-manager/latest/userguide/monitor-commands.md") in the _AWS Systems Manager User Guide_.

## Troubleshoot Microsoft RDS Licensing failures

If you experience issues with CAL (Client Access License) issuance, check whether there
are additional Microsoft RDS licensing servers present in your server farm or Terminal Servers
group. We do not recommend having additional licensing servers in these locations, as that can
interfere with CAL issuance and lead to licensing complications.

To resolve this issue, ensure that only the intended Microsoft RDS servers remain in your
server farm and Terminal Servers group.

When troubleshooting licensing issues, be aware that connections using the /admin flag bypass
standard licensing checks, as this flag is intended for administrative purposes, and doesn't
consume a CAL. This can mask underlying licensing problems. To diagnose licensing issues, verify
that standard user connections (without the /admin flag) are functioning correctly for license
management.

## Troubleshoot Microsoft Office activation failures

If Microsoft Office activation fails, verify that your instance has access to the VPC that's
defined for License Manager. Either of the following options satisfies this requirement:

- Your instance is running in the VPC that's onboarded with License Manager (through VPC
  endpoint)
- Your instance is running in a VPC that's peered with the License Manager onboarded VPC.

To resolve this issue, ensure that your instance is moved to the correct VPC, or establish VPC
peering with the License Manager onboarded VPC.
