AWS Application Discovery Service is no longer open to new customers. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](application-discovery-service-availability-change.md "application-discovery-service-availability-change.md").

# Managing the Discovery Agent process

This page covers how to manage the Discovery Agent on Linux and Microsoft Windows.

## Manage the Discovery Agent process on Linux

You can manage the behavior of the Discovery Agent at the system level using the
`systemd`, `Upstart`, or `System V init` tools.
The following tabs outline the commands for the supported tasks in each of the
respective tools.

systemd

| Management Commands for the Application Discovery Agent | Task                                                     | Command |
| ------------------------------------------------------- | -------------------------------------------------------- | ------- |
| Verify that an agent is running                         | `sudo systemctl status<br>aws-discovery-daemon.service`  |
| Start an agent                                          | `sudo systemctl start<br>aws-discovery-daemon.service`   |
| Stop an agent                                           | `sudo systemctl stop<br>aws-discovery-daemon.service`    |
| Restart an agent                                        | `sudo systemctl restart<br>aws-discovery-daemon.service` |

Upstart

| Management commands for the Application Discovery Agent | Task                                           | Command |
| ------------------------------------------------------- | ---------------------------------------------- | ------- |
| Verify that an agent is running                         | `sudo initctl status<br>aws-discovery-daemon`  |
| Start an agent                                          | `sudo initctl start<br>aws-discovery-daemon`   |
| Stop an agent                                           | `sudo initctl stop<br>aws-discovery-daemon`    |
| Restart an agent                                        | `sudo initctl restart<br>aws-discovery-daemon` |

System V init

| Management commands for the Application Discovery Agent | Task                                               | Command |
| ------------------------------------------------------- | -------------------------------------------------- | ------- |
| Verify that an agent is running                         | `sudo /etc/init.d/aws-discovery-daemon<br>status`  |
| Start an agent                                          | `sudo /etc/init.d/aws-discovery-daemon<br>start`   |
| Stop an agent                                           | `sudo /etc/init.d/aws-discovery-daemon<br>stop`    |
| Restart an agent                                        | `sudo /etc/init.d/aws-discovery-daemon<br>restart` |

## Manage the Discovery Agent process on Microsoft

Windows

You can manage the behavior of the Discovery Agent at the system level through the
Windows Server Manager Services console. The following table describes how.

| Task                            | Service Name                                 | Service Status/Action |
| ------------------------------- | -------------------------------------------- | --------------------- |
| Verify that an agent is running | AWS Discovery Agent<br>AWS Discovery Updater | Started               |
| Start an agent                  | AWS Discovery Agent<br>AWS Discovery Updater | Choose **Start**      |
| Stop an agent                   | AWS Discovery Agent<br>AWS Discovery Updater | Choose **Stop**       |
| Restart an agent                | AWS Discovery Agent<br>AWS Discovery Updater | Choose **Restart**    |
