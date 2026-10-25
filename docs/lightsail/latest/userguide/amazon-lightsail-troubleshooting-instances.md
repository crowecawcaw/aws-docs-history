

# Resolve common Lightsail instance issues
<a name="amazon-lightsail-troubleshooting-instances"></a>

This topic answers common questions about Lightsail instances and links to the steps to fix each issue.

## Status checks
<a name="troubleshooting-instance-status-checks"></a>

For more information about status checks, see [View status checks for your Lightsail instance](amazon-lightsail-viewing-instance-status-checks.md).

**My instance shows Status check failed.**  
One or both status checks on your instance have failed. Open the instance management page to see whether the system status check, the instance status check, or both failed. For more information, see [Find which status check failed](amazon-lightsail-instance-status-checks.md#find-failed-status-check).

**My system status check failed.**  
There is a problem with the AWS infrastructure that your instance runs on. Stop and then start the instance to move it to a new host. A reboot does not fix a failed system status check. For more information, see [Fix a failed system status check](amazon-lightsail-instance-status-checks.md#fixing-system-status-check-failures).

**My instance status check failed.**  
There is a problem inside your instance, such as exhausted memory or an incorrect network or startup configuration. For more information, see [Fix a failed instance status check](amazon-lightsail-instance-status-checks.md#fixing-instance-status-check-failures).

**A status check failed right after I rebooted or started my instance.**  
The instance status check can report a failure until the instance becomes available again. Wait a few minutes and check again before you take action.

**My instance status check failed and I can't connect to my instance.**  
For options when you can't connect, see [Unable to connect to your instance](amazon-lightsail-instance-status-checks.md#status-check-cannot-connect).

**I want to be notified when a status check fails.**  
Create an alarm on a status check metric. For more information, see [Configure status check alarms for your Lightsail instance](amazon-lightsail-configure-status-check-alarms.md).

## Capacity
<a name="troubleshooting-instance-capacity"></a>

**I get an insufficient capacity error when I create or start an instance.**  
AWS doesn't have enough capacity for the instance plan in that Availability Zone right now. Wait a few minutes and try again, or try a different Availability Zone or plan. For more information, see [Resolve insufficient instance capacity errors in Lightsail](amazon-lightsail-instance-capacity.md).