AWS Application Discovery Service will discontinue onboarding new customers starting November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](application-discovery-service-availability-change.md "application-discovery-service-availability-change.md").

# Managing the Discovery Agent process

This page covers how to manage the Discovery Agent on Linux and Microsoft Windows.

## Manage the Discovery Agent process on Linux

You can manage the behavior of the Discovery Agent at the system level using the
`systemd`, `Upstart`, or `System V init` tools.
The following tabs outline the commands for the supported tasks in each of the
respective tools.

systemd

| Management Commands for the Application Discovery Agent | Task                                                  | Command                                                                                                                                                                                                                   |
| ------------------------------------------------------- | ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ------- |
| Verify that an agent is running                         | `sudo systemctl status aws-discovery-daemon.service`  |
| Start an agent                                          | `sudo systemctl start aws-discovery-daemon.service`   |
| Stop an agent                                           | `sudo systemctl stop aws-discovery-daemon.service`    |
| Restart an agent                                        | `sudo systemctl restart aws-discovery-daemon.service` | Upstart Management commands for the Application Discovery Agent                                                                                                                                                           | Task | Command |
| ---                                                     | ---                                                   |
| Verify that an agent is running                         | `sudo initctl status aws-discovery-daemon`            |
| Start an agent                                          | `sudo initctl start aws-discovery-daemon`             |
| Stop an agent                                           | `sudo initctl stop aws-discovery-daemon`              |
| Restart an agent                                        | `sudo initctl restart aws-discovery-daemon`           | System V init Management commands for the Application Discovery Agent                                                                                                                                                     | Task | Command |
| ---                                                     | ---                                                   |
| Verify that an agent is running                         | `sudo /etc/init.d/aws-discovery-daemon status`        |
| Start an agent                                          | `sudo /etc/init.d/aws-discovery-daemon start`         |
| Stop an agent                                           | `sudo /etc/init.d/aws-discovery-daemon stop`          |
| Restart an agent                                        | `sudo /etc/init.d/aws-discovery-daemon restart`       | ## Manage the Discovery Agent process on Microsoft Windows You can manage the behavior of the Discovery Agent at the system level through the Windows Server Manager Services console. The following table describes how. |
| Task                                                    | Service Name                                          | Service Status/Action                                                                                                                                                                                                     |
| ---                                                     | ---                                                   | ---                                                                                                                                                                                                                       |
| Verify that an agent is running                         | AWS Discovery Agent AWS Discovery Updater             | Started                                                                                                                                                                                                                   |
| Start an agent                                          | AWS Discovery Agent AWS Discovery Updater             | Choose **Start**                                                                                                                                                                                                          |
| Stop an agent                                           | AWS Discovery Agent AWS Discovery Updater             | Choose **Stop**                                                                                                                                                                                                           |
| Restart an agent                                        | AWS Discovery Agent AWS Discovery Updater             | Choose **Restart**                                                                                                                                                                                                        |
