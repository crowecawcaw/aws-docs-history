This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Infrastructure 6.50 release

The following release notes include information for infrastructure release 6.50. For
information on the release timeline, see [Change log](#infra-release-notes-6.50-change-log "#infra-release-notes-6.50-change-log").

**Platform version**

|                |                                                                      |
| -------------- | -------------------------------------------------------------------- |
| Infrastructure | 6.50<br>Replicated Native Scheduler (2130)<br>Replicated KOTS (1849) |

**Changes and resolved issues**:

- Updates to third-party libraries have been made to address security vulnerabilities. For
  more information, see [Appendix](#infra-release-notes-6.50-appendix "#infra-release-notes-6.50-appendix").
- Removed the **Suspend Device** and **Activate Device**
  options from **User Device Management**. We identified an issue where a user’s
  device can get into a bad state if the device is first suspended and later activated.

Administrators should now take one of the following actions:

    1. Use the **Reset Device** option. This will suspend and remove access to
     all data on the device and place it into the new device setup process. If the user wants to
     reuse that device, it will be treated as a new device. If the user has another SSO device,
     they can sync the reactivated device.
    2. Suspend the user from the **Team Directory**. This action will suspend
     all of the user's devices. If needed, the user can be unsuspended later.

## Appendix

**Replicated Native Scheduler**

- MySQL - 2911f1b7-f308-48db-960f-c3b4e1bab8ce_mysql_main
- RabbitMQ - 3.13.7
- Redis - 7.4.2
- OpenSearch - 1.3.20
- Traefik - v2.11.18

**Replicated KOTS**

- Ingress Nginx - chart version 4.12.0
- RabbitMQ - chart version 14.7.0
- Redis - chart version 20.6.3
- OpenSearch - chart version 1.35.1
- Cert Manager - chart version 1.16.3
- Cluster AutoScaler - chart version 9.46.0
- Metrics Server - chart version 3.12.2
- AWS Fluent Bit - chart version 0.1.34, app version 2.32.5
- AWS CloudWatch Metrics - chart version 0.0.11, app version 1.300051.0b992

## Change log

**Change log for 6.50 release and release notes**

| Change                | Description                                                 | Date              |
| --------------------- | ----------------------------------------------------------- | ----------------- |
| Final release         | Final notes with Replicated build number                    | February 11, 2025 |
| Infrastructure update | Updates to address vulnerability scan results and bug fixes | February 11, 2025 |
