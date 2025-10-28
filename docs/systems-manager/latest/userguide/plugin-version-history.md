# Session Manager plugin latest version and release

history

Your local machine must be running a supported version of the Session Manager plugin. The
current minimum supported version is 1.1.17.0. If you're running an
earlier version, your Session Manager operations might not succeed.

To see if you have the latest version, run the following command in the
AWS CLI.

###### Note

The command returns results only if the plugin is located in the default
installation directory for your operating system type. You can also check
the version in the contents of the `VERSION` file in the
directory where you have installed the plugin.

```
session-manager-plugin --version
```

The following table lists all releases of the Session Manager plugin and the features and
enhancements included with each version.

###### Important

We recommend you always run the latest version. The latest version
includes enhancements that improve the experience of using the
plugin.

| Version   | Release date       | Details                                                                                                                                                                                                   |
| --------- | ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1.2.707.0 | February 6, 2025   | **Enhancement**: Upgraded the Go version to 1.23 in the Dockerfile. Updated the version configuration step in the README.                                                                                 |
| 1.2.694.0 | November 20, 2024  | **Bug fix**: Rolled back change that added credentials to OpenDataChannel requests.                                                                                                                       |
| 1.2.688.0 | November 6, 2024   | **This version was deprecated on 11/20/2024.** **Enhancements**: <br>• Added credentials to OpenDataChannel requests. <br>• Upgraded the `testify` and `objx` dependent packages.                         |
| 1.2.677.0 | October 10, 2024   | **Enhancement**: Added support for passing the plugin version with OpenDataChannel requests.                                                                                                              |
| 1.2.650.0 | July 02, 2024      | **Enhancement**: Upgraded aws-sdk-go to 1.54.10.**Bug fix**: Reformated comments for gofmt check.                                                                                                         |
| 1.2.633.0 | May 30, 2024       | **Enhancement**: Updated the Dockerfile to use an Amazon Elastic Container Registry (Amazon ECR) image.                                                                                                   |
| 1.2.553.0 | January 10, 2024   | **Enhancement**: Upgraded aws-sdk-go and dependent Golang packages.                                                                                                                                       |
| 1.2.536.0 | December 4, 2023   | **Enhancement**: Added support for passing a [StartSession](../APIReference/API_StartSession.md "../APIReference/API_StartSession.md") API response as an environment variable to session-manager-plugin. |
| 1.2.497.0 | August 1, 2023     | **Enhancement**: Upgraded Go SDK to v1.44.302.                                                                                                                                                            |
| 1.2.463.0 | March 15, 2023     | **Enhancement**: Added Mac with Apple silicon support for Apple Mac (M1) in macOS bundle installer and signed installer.                                                                                  |
| 1.2.398.0 | October 14, 2022   | **Enhancement**: Support golang version 1.17. Update default session-manager-plugin runner for macOS to use python3. Update import path from SSMCLI to session-manager-plugin.                            |
| 1.2.339.0 | June 16, 2022      | **Bug fix**: Fix idle session timeout for port sessions.                                                                                                                                                  |
| 1.2.331.0 | May 27, 2022       | **Bug fix**: Fix port sessions closing prematurely when the local server doesn't connect before timeout.                                                                                                  |
| 1.2.323.0 | May 19, 2022       | **Bug fix**: Disable smux keep alive to use idle session timeout feature.                                                                                                                                 |
| 1.2.312.0 | March 31, 2022     | **Enhancement**: Supports more output message payload types.                                                                                                                                              |
| 1.2.295.0 | January 12, 2022   | **Bug fix**: Hung sessions caused by client resending stream data when agent becomes inactive, and incorrect logs for `start_publication` and `pause_publication` messages.                               |
| 1.2.279.0 | October 27, 2021   | **Enhancement**: Zip packaging for Windows platform.                                                                                                                                                      |
| 1.2.245.0 | August 19, 2021    | **Enhancement**: Upgrade `aws-sdk-go` to latest version (v1.40.17) to support AWS IAM Identity Center.                                                                                                    |
| 1.2.234.0 | July 26, 2021      | **Bug fix**: Handle session abruptly terminated scenario in interactive session type.                                                                                                                     |
| 1.2.205.0 | June 10, 2021      | **Enhancement**: Added support for signed macOS installer.                                                                                                                                                |
| 1.2.54.0  | January 29, 2021   | **Enhancement**: Added support for running sessions in NonInteractiveCommands execution mode.                                                                                                             |
| 1.2.30.0  | November 24, 2020  | **Enhancement**: (Port forwarding sessions only) Improved overall performance.                                                                                                                            |
| 1.2.7.0   | October 15, 2020   | **Enhancement**: (Port forwarding sessions only) Reduced latency and improved overall performance.                                                                                                        |
| 1.1.61.0  | April 17, 2020     | **Enhancement**: Added ARM support for Linux and Ubuntu Server.                                                                                                                                           |
| 1.1.54.0  | January 6, 2020    | **Bug fix**: Handle race condition scenario of packets being dropped when the Session Manager plugin isn't ready.                                                                                         |
| 1.1.50.0  | November 19, 2019  | **Enhancement**: Added support for forwarding a port to a local unix socket.                                                                                                                              |
| 1.1.35.0  | November 7, 2019   | **Enhancement**: (Port forwarding sessions only) Send a TerminateSession command to SSM Agent when the local user presses `Ctrl+C`.                                                                       |
| 1.1.33.0  | September 26, 2019 | **Enhancement**: (Port forwarding sessions only) Send a disconnect signal to the server when the client drops the TCP connection.                                                                         |
| 1.1.31.0  | September 6, 2019  | **Enhancement**: Update to keep port forwarding session open until remote server closes the connection.                                                                                                   |
| 1.1.26.0  | July 30, 2019      | **Enhancement**: Update to limit the rate of data transfer during a session.                                                                                                                              |
| 1.1.23.0  | July 9, 2019       | **Enhancement**: Added support for running SSH sessions using Session Manager.                                                                                                                            |
| 1.1.17.0  | April 4, 2019      | **Enhancement**: Added support for further encryption of session data using AWS Key Management Service (AWS KMS).                                                                                         |
| 1.0.37.0  | September 20, 2018 | **Enhancement**: Bug fix for Windows version.                                                                                                                                                             |
| 1.0.0.0   | September 11, 2018 | Initial release of the Session Manager plugin.                                                                                                                                                            |
