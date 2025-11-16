# Release notes and document history for

Amazon DCV Session Manager

This page provides the release notes and document history for Amazon DCV Session Manager.

###### Topics

- [Release Notes](#release-notes "#release-notes")
- [Document history](#doc-history "#doc-history")

## Amazon DCV Session Manager release notes

This section provides an overview of the major updates, feature releases, and bug fixes for
Amazon DCV Session Manager. All the updates are organized by release date. We update the documentation
frequently to address the feedback that you send us.

###### Topics

- [2025.0-539— October 22, 2025](#sm-2025.0-539 "#sm-2025.0-539")
- [2024.0-531— June 17, 2025](#sm-2024.0-531 "#sm-2024.0-531")
- [2024.0-504— March 31, 2025](#sm-2024.0-504 "#sm-2024.0-504")
- [2024.0-493— January 15, 2025](#sm-2024.0-493 "#sm-2024.0-493")
- [2024.0-457— October 1, 2024](#sm-2024.0-457 "#sm-2024.0-457")
- [2023.1-17652— August 1, 2024](#sm-2023.1-17652 "#sm-2023.1-17652")
- [2023.1-16388— June 26, 2024](#sm-2023.1-16388 "#sm-2023.1-16388")
- [2023.1— November 9, 2023](#sm-2023.1 "#sm-2023.1")
- [2023.0-15065— May 4, 2023](#sm-2023.0-15065 "#sm-2023.0-15065")
- [2023.0-14852— March 28, 2023](#sm-2023.0-14852 "#sm-2023.0-14852")
- [2022.2-13907— November 11, 2022](#sm-2022.2-13907 "#sm-2022.2-13907")
- [2022.1-13067— June 29, 2022](#sm-2022.1-13067 "#sm-2022.1-13067")
- [2022.0-11952— February 23, 2022](#sm-2022.0-11952 "#sm-2022.0-11952")
- [2021.3-11591— December 20, 2021](#sm-2021.3-11591 "#sm-2021.3-11591")
- [2021.2-11445— November 18, 2021](#sm-2021.2-11445 "#sm-2021.2-11445")
- [2021.2-11190— October 11, 2021](#sm-2021.2-11190 "#sm-2021.2-11190")
- [2021.2-11042— September 01, 2021](#sm-2021.2-11042 "#sm-2021.2-11042")
- [2021.1-10557— May 31, 2021](#sm-2021.1-10557 "#sm-2021.1-10557")
- [2021.0-10242— April 12, 2021](#sm-2021.0-10242 "#sm-2021.0-10242")
- [2020.2-9662— December 04, 2020](#sm-2020.2-9662 "#sm-2020.2-9662")
- [2020.2-9508— November 11, 2020](#sm-2020.2-9508 "#sm-2020.2-9508")

### 2025.0-539— October 22, 2025

| Build numbers                               | Changes and bug fixes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • Broker: 539<br>• Agent: 886<br>• CLI: 159 | • Added enable_query_logged_in_users configuration parameter to the Agent configuration file to<br>specify logged users query behavior on Windows systems.<br>• Replaced PowerShell commands with native Windows APIs (WMI and Windows Registry) for improved<br>performance and reliability when retrieving system information.<br>• Fixed DNS name resolution on Windows Amazon EC2 instances by improving Amazon EC2 detection with<br>fallback to AWS metadata service when UUID-based detection fails.<br>• Updated version to 2025. |

### 2024.0-531— June 17, 2025

| Build numbers                               | Changes and bug fixes                                                                                       |
| ------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| • Broker: 531<br>• Agent: 852<br>• CLI: 154 | • Added feature to renew certificates before expiry.<br>• Rebranded NICE DCV to Amazon DCV.<br>• Bug fixes. |

### 2024.0-504— March 31, 2025

| Build numbers                               | Changes and bug fixes                                                    |
| ------------------------------------------- | ------------------------------------------------------------------------ |
| • Broker: 504<br>• Agent: 817<br>• CLI: 154 | • Added support for AL2023.<br>• Bug fixes and performance improvements. |

### 2024.0-493— January 15, 2025

| Build numbers                               | Changes and bug fixes                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • Broker: 493<br>• Agent: 801<br>• CLI: 152 | • Added parameters to the `GetSessionScreenshot` request to specify the maximum height and width of the screenshot.<br>• Added parameter to the Broker configuration file that specifies the number of seconds after which session on an unreachable Amazon DCV server are deleted from the system.<br>• Fixed an issue where the `seconds-before-deleting-unreachable-dcv-server` parameter in the Broker configuration file was not being honored.<br>• Bug fixes and performance improvements. |

### 2024.0-457— October 1, 2024

| Build numbers                               | Changes and bug fixes                                                    |
| ------------------------------------------- | ------------------------------------------------------------------------ |
| • Broker: 457<br>• Agent: 748<br>• CLI: 140 | • Rebranded NICE DCV to Amazon DCV.<br>• Added support for Ubuntu 24.04. |

### 2023.1-17652— August 1, 2024

| Build numbers                               | Changes and bug fixes                     |
| ------------------------------------------- | ----------------------------------------- |
| • Broker: 426<br>• Agent: 748<br>• CLI: 140 | • Bug fixes and performance improvements. |

### 2023.1-16388— June 26, 2024

| Build numbers                               | Changes and bug fixes                                                                                    |
| ------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| • Broker: 417<br>• Agent: 748<br>• CLI: 140 | • Fixed a bug that showed memory incorrectly as TB, not GB.<br>• Bug fixes and performance improvements. |

### 2023.1— November 9, 2023

| Build numbers                               | Changes and bug fixes                    |
| ------------------------------------------- | ---------------------------------------- |
| • Broker: 410<br>• Agent: 732<br>• CLI: 140 | • Bug fixes and performance improvements |

### 2023.0-15065— May 4, 2023

| Build numbers                               | Changes and bug fixes                                                                                |
| ------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| • Broker: 392<br>• Agent: 675<br>• CLI: 132 | • Added support for Red Hat Enterprise Linux 9, Rocky Linux 9, and CentOS Stream 9 on ARM platforms. |

### 2023.0-14852— March 28, 2023

| Build numbers                               | Changes and bug fixes                                                               |
| ------------------------------------------- | ----------------------------------------------------------------------------------- |
| • Broker: 392<br>• Agent: 642<br>• CLI: 132 | • Added support for Red Hat Enterprise Linux 9, Rocky Linux 9, and CentOS Stream 9. |

### 2022.2-13907— November 11, 2022

| Build numbers                               | Changes and bug fixes                                                                                                                                                  |
| ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • Broker: 382<br>• Agent: 612<br>• CLI: 123 | • Added a `Substate` field in `DescribeSessions` response.<br>• Fixed a problem that could cause the CLI to fail to connect to the broker depending on the URL in use. |

### 2022.1-13067— June 29, 2022

| Build numbers                               | Changes and bug fixes                                                                                              |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| • Broker: 355<br>• Agent: 592<br>• CLI: 114 | • Added support to run the broker on AWS Graviton instances.<br>• Added agent and broker support for Ubuntu 22.04. |

### 2022.0-11952— February 23, 2022

| Build numbers                               | Changes and bug fixes                                                                                                                                                                                                |
| ------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • Broker: 341<br>• Agent: 520<br>• CLI: 112 | • Added log rotation capability to the Agent.<br>• Added configuration parameter to set Java home in the Broker.<br>• Improved data flushing from cache to disk in the Broker.<br>• Fixed URL validation in the CLI. |

### 2021.3-11591— December 20, 2021

| Build numbers                              | New features                                                                                                                         |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| • Broker: 307<br>• Agent: 453<br>• CLI: 92 | • Added support for integrating with the Amazon DCV Connection Gateway.<br>• Added Broker support for Ubuntu 18.04 and Ubuntu 20.04. |

### 2021.2-11445— November 18, 2021

| Build numbers                              | Changes and bug fixes                                                                |
| ------------------------------------------ | ------------------------------------------------------------------------------------ |
| • Broker: 288<br>• Agent: 413<br>• CLI: 54 | • Fixed a problem with the validation of login names which include a Windows domain. |

### 2021.2-11190— October 11, 2021

| Build numbers                              | Changes and bug fixes                                                                               |
| ------------------------------------------ | --------------------------------------------------------------------------------------------------- |
| • Broker: 254<br>• Agent: 413<br>• CLI: 54 | • Fixed a problem in the command line interface which prevented from launching<br>Windows sessions. |

### 2021.2-11042— September 01, 2021

| Build numbers                              | New features                                                                                                                                                                                                                                                                                                                                                                   | Changes and bug fixes                                                                                                                                                                                                                          |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • Broker: 254<br>• Agent: 413<br>• CLI: 37 | • Amazon DCV Session Manager now offers command line interface (CLI) support. You can create and manage Amazon DCV sessions<br>in the CLI, instead of calling APIs.<br>• Amazon DCV Session Manager introduced Broker data persistence. For higher availability,<br>brokers can persist server state information on an external data store and<br>restore the data at startup. | • When registering an external authorization server, you can now specify the algorithm that the<br>authorization server uses to sign JSON-formatted Web Tokens. With this change,<br>you can use Azure AD as an external authorization server. |

### 2021.1-10557— May 31, 2021

| Build numbers                 | New features                                                                                                                                                                                                                                             | Changes and bug fixes                                  |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| • Broker: 214<br>• Agent: 365 | • Amazon DCV Session Manager added support for input parameters passed to the autorun file on<br>Linux.<br>• Server properties can now be passed as requirements to the [CreateSessions](../sm-dev/CreateSessions.md "../sm-dev/CreateSessions.md") API. | • We fixed a problem with the autorun file on Windows. |

### 2021.0-10242— April 12, 2021

| Build numbers                 | Changes and bug fixes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • Broker: 183<br>• Agent: 318 | • Amazon DCV Session Manager introduced the following new APIs:<br>+ [OpenServers](../sm-dev/OpenServers.md "../sm-dev/OpenServers.md")<br>+ [CloseServers](../sm-dev/CloseServers.md "../sm-dev/CloseServers.md")<br>+ [DescribeServers](../sm-dev/DescribeServers.md "../sm-dev/DescribeServers.md")<br>+ [GetSessionScreenshots](../sm-dev/GetSessionScreenshots.md "../sm-dev/GetSessionScreenshots.md")<br>• It also introduced the following new configuration parameters:<br>+ [Broker parameters](broker-file.md "broker-file.md"):<br>`session-screenshot-max-width`, `session-screenshot-max-height`,<br>`session-screenshot-format`, `create-sessions-queue-max-size`,<br>and `create-sessions-queue-max-time-seconds`.<br>+ [Agent parameters](agent-file.md "agent-file.md"):<br>`agent.autorun_folder`, `max_virtual_sessions`, and `max_concurrent_sessions_per_user`.<br>[Agent parameters](agent-file.md "agent-file.md"):<br>`agent.autorun_folder`,`max_virtual_sessions`, and<br>`max_concurrent_sessions_per_user`.<br>[Agent parameters](agent-file.md "agent-file.md"):<br>`agent.autorun_folder`,`max_virtual_sessions`, and<br>`max_concurrent_sessions_per_user`. |

### 2020.2-9662— December 04, 2020

| Build numbers                 | Changes and bug fixes                                                                                     |
| ----------------------------- | --------------------------------------------------------------------------------------------------------- |
| • Broker: 114<br>• Agent: 211 | • We fixed a problem with the auto-generated TLS certificates that prevented the Broker from<br>starting. |

### 2020.2-9508— November 11, 2020

| Build numbers                | Changes and bug fixes                                |
| ---------------------------- | ---------------------------------------------------- |
| • Broker: 78<br>• Agent: 183 | • The initial release of Amazon DCV Session Manager. |

## Document history

The following table describes the documentation for this release of Amazon DCV Session Manager.

| Change                                        | Description                                                                                                                                                                | Date               |
| --------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| Amazon DCV Version 2024.0-531                 | Amazon DCV Session Manager has been updated for Amazon DCV 2024.0-531. For more information, see<br>[2024.0-531— June 17, 2025](#sm-2024.0-531 "#sm-2024.0-531").          | June 17, 2025      |
| Amazon DCV Version 2024.0-504                 | Amazon DCV Session Manager has been updated for Amazon DCV 2024.0-504. For more information, see<br>[2024.0-504— March 31, 2025](#sm-2024.0-504 "#sm-2024.0-504").         | March 31, 2025     |
| Amazon DCV Version 2024.0-493                 | Amazon DCV Session Manager has been updated for Amazon DCV 2024.0-493. For more information, see<br>[2024.0-493— January 15, 2025](#sm-2024.0-493 "#sm-2024.0-493").       | January 15, 2025   |
| Amazon DCV Version 2024.0-457                 | Amazon DCV Session Manager has been updated for Amazon DCV 2024.0-457. For more information, see<br>[2024.0-457— October 1, 2024](#sm-2024.0-457 "#sm-2024.0-457").        | September 30, 2024 |
| Amazon DCV Version 2023.1-17652               | Amazon DCV Session Manager has been updated for Amazon DCV 2023.1-17652. For more information, see<br>[2023.1-17652— August 1, 2024](#sm-2023.1-17652 "#sm-2023.1-17652"). | August 1, 2024     |
| Amazon DCV Version 2023.1-16388               | Amazon DCV Session Manager has been updated for Amazon DCV 2023.1-16388. For more information, see<br>[2023.1-16388— June 26, 2024](#sm-2023.1-16388 "#sm-2023.1-16388").  | June 26, 2024      |
| Amazon DCV Version 2023.1                     | Amazon DCV Session Manager has been updated for Amazon DCV 2023.1. For more information, see<br>[2023.1— November 9, 2023](#sm-2023.1 "#sm-2023.1").                       | November 9, 2023   |
| Amazon DCV Version 2023.0                     | Amazon DCV Session Manager has been updated for Amazon DCV 2023.0. For more information, see<br>[2023.0-14852— March 28, 2023](#sm-2023.0-14852 "#sm-2023.0-14852").       | March 28, 2023     |
| Amazon DCV Version 2022.2                     | Amazon DCV Session Manager has been updated for Amazon DCV 2022.2. For more information, see<br>[2022.2-13907— November 11, 2022](#sm-2022.2-13907 "#sm-2022.2-13907").    | November 11, 2022  |
| Amazon DCV Version 2022.1                     | Amazon DCV Session Manager has been updated for Amazon DCV 2022.1. For more information, see<br>[2022.1-13067— June 29, 2022](#sm-2022.1-13067 "#sm-2022.1-13067").        | June 29, 2022      |
| Amazon DCV Version 2022.0                     | Amazon DCV Session Manager has been updated for Amazon DCV 2022.0. For more information, see<br>[2022.0-11952— February 23, 2022](#sm-2022.0-11952 "#sm-2022.0-11952").    | February 23, 2022  |
| Amazon DCV Version 2021.3                     | Amazon DCV Session Manager has been updated for Amazon DCV 2021.3. For more information, see<br>[2021.3-11591— December 20, 2021](#sm-2021.3-11591 "#sm-2021.3-11591").    | December 20, 2021  |
| Amazon DCV Version 2021.2                     | Amazon DCV Session Manager has been updated for Amazon DCV 2021.2. For more information, see<br>[2021.2-11042— September 01, 2021](#sm-2021.2-11042 "#sm-2021.2-11042").   | September 01, 2021 |
| Amazon DCV Version 2021.1                     | Amazon DCV Session Manager has been updated for Amazon DCV 2021.1. For more information, see<br>[2021.1-10557— May 31, 2021](#sm-2021.1-10557 "#sm-2021.1-10557").         | May 31, 2021       |
| Amazon DCV Version 2021.0                     | Amazon DCV Session Manager has been updated for Amazon DCV 2021.0. For more information, see<br>[2021.0-10242— April 12, 2021](#sm-2021.0-10242 "#sm-2021.0-10242").       | April 12, 2021     |
| Initial release of Amazon DCV Session Manager | The first publication of this content.                                                                                                                                     | November 11, 2020  |
