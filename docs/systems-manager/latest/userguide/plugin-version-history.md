• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

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

| Version   | Release date       | Details                                                                                                                                                                                                         |
| --------- | ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1.2.779.0 | February 12, 2026  | **Enhancement**: Update Go<br>version to 1.25 in Dockerfile.<br>**Bug fix**: Add shebang<br>lines to debian packaging scripts.                                                                                  |
| 1.2.764.0 | November 19, 2025  | **Enhancement**: Added<br>support for signing OpenDataChannel request.<br>**Bug fix**: Fix checkstyle<br>issues to support newer Go version.                                                                    |
| 1.2.707.0 | February 6, 2025   | **Enhancement**: Upgraded<br>the Go version to 1.23 in the Dockerfile. Updated the<br>version configuration step in the README.                                                                                 |
| 1.2.694.0 | November 20, 2024  | **Bug fix**: Rolled back<br>change that added credentials to OpenDataChannel<br>requests.                                                                                                                       |
| 1.2.688.0 | November 6, 2024   | **This version was deprecated on<br>11/20/2024.**<br>**Enhancements**:<br>• Added credentials to OpenDataChannel<br>requests.<br>• Upgraded the `testify` and<br>`objx` dependent packages.                     |
| 1.2.677.0 | October 10, 2024   | **Enhancement**: Added<br>support for passing the plugin version with OpenDataChannel<br>requests.                                                                                                              |
| 1.2.650.0 | July 02, 2024      | **Enhancement**: Upgraded<br>aws-sdk-go to 1.54.10.**Bug<br>fix**: Reformated comments for gofmt<br>check.                                                                                                      |
| 1.2.633.0 | May 30, 2024       | **Enhancement**: Updated the<br>Dockerfile to use an Amazon Elastic Container Registry (Amazon ECR) image.                                                                                                      |
| 1.2.553.0 | January 10, 2024   | **Enhancement**: Upgraded<br>aws-sdk-go and dependent Golang packages.                                                                                                                                          |
| 1.2.536.0 | December 4, 2023   | **Enhancement**: Added support<br>for passing a [StartSession](../APIReference/API_StartSession.md "../APIReference/API_StartSession.md") API response as an environment<br>variable to session-manager-plugin. |
| 1.2.497.0 | August 1, 2023     | **Enhancement**: Upgraded Go SDK<br>to v1.44.302.                                                                                                                                                               |
| 1.2.463.0 | March 15, 2023     | **Enhancement**: Added<br>Mac with Apple silicon support for Apple Mac (M1) in macOS bundle<br>installer and signed installer.                                                                                  |
| 1.2.398.0 | October 14, 2022   | **Enhancement**: Support golang<br>version 1.17. Update default session-manager-plugin runner for<br>macOS to use python3. Update import path from SSMCLI to<br>session-manager-plugin.                         |
| 1.2.339.0 | June 16, 2022      | **Bug fix**: Fix idle session<br>timeout for port sessions.                                                                                                                                                     |
| 1.2.331.0 | May 27, 2022       | **Bug fix**: Fix port sessions<br>closing prematurely when the local server doesn't connect before<br>timeout.                                                                                                  |
| 1.2.323.0 | May 19, 2022       | **Bug fix**: Disable smux keep<br>alive to use idle session timeout feature.                                                                                                                                    |
| 1.2.312.0 | March 31, 2022     | **Enhancement**: Supports more<br>output message payload types.                                                                                                                                                 |
| 1.2.295.0 | January 12, 2022   | **Bug fix**: Hung sessions<br>caused by client resending stream data when agent becomes<br>inactive, and incorrect logs for `start_publication`<br>and `pause_publication` messages.                            |
| 1.2.279.0 | October 27, 2021   | **Enhancement**: Zip packaging<br>for Windows platform.                                                                                                                                                         |
| 1.2.245.0 | August 19, 2021    | **Enhancement**: Upgrade<br>`aws-sdk-go` to latest version (v1.40.17) to<br>support AWS IAM Identity Center.                                                                                                    |
| 1.2.234.0 | July 26, 2021      | **Bug fix**: Handle session<br>abruptly terminated scenario in interactive session<br>type.                                                                                                                     |
| 1.2.205.0 | June 10, 2021      | **Enhancement**: Added support<br>for signed macOS installer.                                                                                                                                                   |
| 1.2.54.0  | January 29, 2021   | **Enhancement**: Added support<br>for running sessions in NonInteractiveCommands execution<br>mode.                                                                                                             |
| 1.2.30.0  | November 24, 2020  | **Enhancement**: (Port<br>forwarding sessions only) Improved overall<br>performance.                                                                                                                            |
| 1.2.7.0   | October 15, 2020   | **Enhancement**: (Port<br>forwarding sessions only) Reduced latency and improved<br>overall performance.                                                                                                        |
| 1.1.61.0  | April 17, 2020     | **Enhancement**: Added ARM<br>support for Linux and Ubuntu Server.                                                                                                                                              |
| 1.1.54.0  | January 6, 2020    | **Bug fix**: Handle race<br>condition scenario of packets being dropped when the<br>Session Manager plugin isn't ready.                                                                                         |
| 1.1.50.0  | November 19, 2019  | **Enhancement**: Added<br>support for forwarding a port to a local unix socket.                                                                                                                                 |
| 1.1.35.0  | November 7, 2019   | **Enhancement**: (Port<br>forwarding sessions only) Send a TerminateSession command to<br>SSM Agent when the local user presses<br>`Ctrl+C`.                                                                    |
| 1.1.33.0  | September 26, 2019 | **Enhancement**: (Port<br>forwarding sessions only) Send a disconnect signal to the server<br>when the client drops the TCP connection.                                                                         |
| 1.1.31.0  | September 6, 2019  | **Enhancement**: Update to keep<br>port forwarding session open until remote server closes the<br>connection.                                                                                                   |
| 1.1.26.0  | July 30, 2019      | **Enhancement**: Update to<br>limit the rate of data transfer during a session.                                                                                                                                 |
| 1.1.23.0  | July 9, 2019       | **Enhancement**: Added<br>support for running SSH sessions using Session Manager.                                                                                                                               |
| 1.1.17.0  | April 4, 2019      | **Enhancement**: Added<br>support for further encryption of session data using<br>AWS Key Management Service (AWS KMS).                                                                                         |
| 1.0.37.0  | September 20, 2018 | **Enhancement**: Bug fix for<br>Windows version.                                                                                                                                                                |
| 1.0.0.0   | September 11, 2018 | Initial release of the Session Manager plugin.                                                                                                                                                                  |
