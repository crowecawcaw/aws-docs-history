# Amazon GameLift Servers release notes

The Amazon GameLift Servers release notes provide details about new features, updates, and fixes related to
the service.

## SDK versions

The following tables list all Amazon GameLift Servers releases with SDK version information. There is no
requirement to use comparable SDKs for your game server and client integrations.
However, earlier versions of one SDK may not fully support the latest features in
another.

Amazon GameLift Servers SDKs and plugins are open source. See [Get Amazon GameLift Servers development tools](gamelift-supported.md "gamelift-supported.md"). To get the latest versions, see the [Amazon GameLift Servers
GitHub organization.](https://github.com/amazon-gamelift/ "https://github.com/amazon-gamelift/")

**Current version**

| Service release                                                 | AWS SDK                                                                                                                                  | Server SDK | Plugin for Unreal | Plugin for Unity | Realtime client SDK |
| --------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ----------------- | ---------------- | ------------------- | ----- | ----- | ----- | ----- |
|                                                                 | C++                                                                                                                                      | C#         | Unity (C#)        | C++              | Unreal (C++)        | Go    |       |       |       |
| [2025-10-28](#release-notes-10282025 "#release-notes-10282025") | [1.11.595](https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.595 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.595") or later | 5.4.0      | 5.4.0             | 5.4.0            | 5.4.0               | 5.4.0 | 3.1.0 | 3.2.0 | 1.1.0 |

| Service release                                                                                                                                                       | AWS SDK                                                                                                                                  | Server SDK            | Plugin for Unreal | Plugin for Unity | Realtime client SDK |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | --------------------- | ----------------- | ---------------- | ------------------- | ----- | ----- | ----- | ----- |
|                                                                                                                                                                       | C++                                                                                                                                      | C#                    | C# Unity          | C++              | C++ Unreal          | Go    |       |       |       |
| 2025-10-03                                                                                                                                                            | [1.11.595](https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.595 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.595") or later | 5.3.0                 | 5.3.0             | 5.3.0            | 5.3.2               | 5.3.0 | 3.0.2 | 3.1.0 | 1.2.0 |
| [2025-08-12](#release-notes-08122025 "#release-notes-08122025")                                                                                                       | [1.11.595](https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.595 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.595") or later | 5.3.0                 | 5.3.0             | 5.3.0            | 5.3.1               | 5.3.0 | 3.0.1 | 3.1.0 | 1.2.0 |
| [2025-06-24](#release-notes-06242025-2 "#release-notes-06242025-2")                                                                                                   | [1.11.595](https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.595 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.595") or later | 5.3.0                 | 5.3.0             | 5.3.0            | 5.3.0               | 5.3.0 | 3.0.0 | 3.1.0 | 1.2.0 |
| [2025-05-29](#release-notes-05292025 "#release-notes-05292025")                                                                                                       | [1.11.535](https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.535 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.535") or later | 5.3.0                 | 5.3.0             | 5.3.0            | 5.3.0               | 5.3.0 | 3.0.0 | 3.1.0 | 1.2.0 |
| [2025-04-24](#release-notes-04242025 "#release-notes-04242025")                                                                                                       | [1.11.535](https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.535 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.535") or later | 5.2.1 (.NET 8)        | 5.2.0             | 5.2.0            | 5.2.0               | 5.2.0 | 2.0.0 | 3.0.1 | 1.2.0 |
| [2025-03-27](#release-notes-03272025 "#release-notes-03272025")                                                                                                       | [1.11.535](https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.535 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.535") or later | 5.2.0                 | 5.2.0             | 5.2.0            | 5.2.0               | 5.2.0 | 2.0.0 | 3.0.1 | 1.2.0 |
| 2025-03-13                                                                                                                                                            | [1.11.485](https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.485 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.485") or later | 5.2.0                 | 5.2.0             | 5.2.0            | 5.2.0               | 5.2.0 | 2.0.0 | 3.0.1 | 1.2.0 |
| [2025-01-14](#release-notes-01022025 "#release-notes-01022025")                                                                                                       | [1.11.485](https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.485 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.485") or later | 5.2.0                 | 5.2.0             | 5.2.0            | 5.2.0               | 5.2.0 | 2.0.0 | 3.0.0 | 1.2.0 |
| [2025-01-02](#release-notes-01022025 "#release-notes-01022025")                                                                                                       | [1.11.477](https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.477 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.477") or later | 5.2.0                 | 5.2.0             | 5.2.0            | 5.2.0               | 5.2.0 | 2.0.0 | 3.0.0 | 1.2.0 |
| [2024-12-19](#release-notes-12192024 "#release-notes-12192024")                                                                                                       | [1.11.445](https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.445 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.445") or later | 5.2.0                 | 5.2.0             | 5.2.0            | 5.2.0               | 5.2.0 | 2.0.0 | 3.0.0 | 1.2.0 |
| [2024-11-12](#release-notes-11122024 "#release-notes-11122024")                                                                                                       | [1.11.445](https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.445 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.445") or later | 5.2.0                 | 5.2.0             | 5.2.0            | 5.2.0               | 5.2.0 | 1.1.2 | 2.1.0 | 1.2.0 |
| [2024-09-19](#release-notes-09192024 "#release-notes-09192024")                                                                                                       | [1.11.225](https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.225 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.225") or later | 5.1.2                 | 5.1.2             | 5.1.3            | 5.1.2               | 5.1.0 | 1.1.2 | 2.1.0 | 1.2.0 |
| [2024-02-13](#release-notes-02132024 "#release-notes-02132024")                                                                                                       | [1.11.225](https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.225 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.225") or later | 5.1.2                 | 5.1.2             | 5.1.2            | 5.1.1               | 5.1.0 | 1.1.0 | 2.1.0 | 1.2.0 |
| [2023-12-14](#release-notes-12142023 "#release-notes-12142023")                                                                                                       | [1.11.225](https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.225 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.225") or later | 5.1.1                 | 5.1.0             | 5.1.1            | 5.1.0               | 5.0.0 | 1.1.0 | 2.0.0 | 1.2.0 |
| [2023-11-16](#release-notes-11162023 "#release-notes-11162023")                                                                                                       | [1.11.193](https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.193 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.193") or later | 5.1.1                 | 5.1.0             | 5.1.1            | 5.1.0               | 5.0.0 | 1.1.0 | 2.0.0 | 1.2.0 |
| [2023-11-02](#release-notes-11022023 "#release-notes-11022023")                                                                                                       | [1.11.193](https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.193 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.193") or later | 5.1.1                 | 5.1.0             | 5.1.1            | 5.1.0               | 5.0.0 | 1.1.0 | 1.3.1 | 1.2.0 |
| [2023-09-28](#release-notes-09282023 "#release-notes-09282023")                                                                                                       | [1.11.144](https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.144 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.144") or later | 5.1.1                 | 5.1.0             | 5.1.1            | 5.1.0               | 5.0.0 | 1.0.0 | 1.3.1 | 1.2.0 |
| [2023-08-17](#release-notes-08172023 "#release-notes-08172023")                                                                                                       | [1.11.144](https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.144 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.144") or later | 5.1.1                 | 5.1.0             | 5.1.1            | 5.1.0               | 5.0.0 |       | 1.3.1 | 1.2.0 |
| [2023-07-27](#release-notes-07272023 "#release-notes-07272023")                                                                                                       | [1.11.111](https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.111 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.111") or later | 5.1.0                 | 5.1.0             | 5.1.0            | 5.0.2               | 5.0.0 |       | 1.3.1 | 1.2.0 |
| [2023-06-29](#release-notes-06292023 "#release-notes-06292023")                                                                                                       | [1.11.111](https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.111 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.111") or later | 5.0.0                 |                   | 5.0.4            | 5.0.2               | 5.0.0 |       | 1.3.0 | 1.2.0 |
| 2023-06-15                                                                                                                                                            | [1.11.87](https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.87 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.87") or later    | 5.0.0                 |                   | 5.0.4            | 5.0.2               | 5.0.0 |       | 1.3.0 | 1.2.0 |
| [2023-05-25](#release-notes-05252023 "#release-notes-05252023")                                                                                                       | [1.11.87](https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.87 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.87") or later    | 5.0.0                 |                   | 5.0.3            | 5.0.2               | 5.0.0 |       | 1.3.0 | 1.2.0 |
| [2023-04-20](#release-notes-04202023 "#release-notes-04202023")                                                                                                       | [1.11.63](https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.63 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.63") or later    | 5.0.0                 |                   | 5.0.3            | 5.0.2               | 5.0.0 |       | 1.3.0 | 1.2.0 |
| [2023-04-13](#release-notes-04132023 "#release-notes-04132023")                                                                                                       | [1.10.21](https://github.com/aws/aws-sdk-cpp/releases/tag/1.10.21 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.10.21") or later    | 5.0.0                 |                   | 5.0.0            | 5.0.0               | 5.0.0 |       | 1.2.1 | 1.2.0 |
| [2023-02-09](#release-notes-02092023 "#release-notes-02092023")                                                                                                       | [1.10.21](https://github.com/aws/aws-sdk-cpp/releases/tag/1.10.21 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.10.21") or later    | 5.0.0                 |                   | 5.0.0            | 3.4.0               | 5.0.0 |       | 1.2.1 | 1.2.0 |
| [2023-01-31](#release-notes-01312023 "#release-notes-01312023")                                                                                                       | [1.10.21](https://github.com/aws/aws-sdk-cpp/releases/tag/1.10.21 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.10.21") or later    |                       | 5.0.0             |                  | 3.4.0               | 5.0.0 |       | 1.2.1 | 1.2.0 |
| [2022-12-01](#release-notes-12012022 "#release-notes-12012022")                                                                                                       | [1.10.21](https://github.com/aws/aws-sdk-cpp/releases/tag/1.10.21 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.10.21") or later    | 5.0.0 (.NET 4 .NET 6) |                   | 5.0.0            | 3.4.0               |       |       | 1.2.1 | 1.2.0 |
| [2022-08-25](#release-notes-08252022 "#release-notes-08252022")                                                                                                       | [1.9.333](https://github.com/aws/aws-sdk-cpp/releases/tag/1.9.333 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.9.333") or later    | 4.0.2                 |                   | 3.4.2            | 3.4.0               |       |       | 1.2.0 | 1.2.0 |
| [2021-10-28](#release-notes-10282021 "#release-notes-10282021")                                                                                                       | [1.9.133](https://github.com/aws/aws-sdk-cpp/releases/tag/1.9.133 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.9.133") or later    | 4.0.2                 |                   | 3.4.2            | 3.4.0               |       |       | 1.2.0 | 1.2.0 |
| [2021-06-03](#release-notes-06032021 "#release-notes-06032021")                                                                                                       | [1.8.168](https://github.com/aws/aws-sdk-cpp/releases/tag/1.8.168 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.8.168") or later    | 4.0.2                 |                   | 3.4.2            | 3.4.0               |       |       |       | 1.2.0 |
| [2021-03-23](#release-notes-03232021 "#release-notes-03232021")                                                                                                       | [1.8.168](https://github.com/aws/aws-sdk-cpp/releases/tag/1.8.168 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.8.168") or later    | 4.0.2                 |                   | 3.4.1            | 3.3.3               |       |       |       | 1.1.0 |
| [2021-03-16](#release-notes-03162021 "#release-notes-03162021")                                                                                                       | [1.8.163](https://github.com/aws/aws-sdk-cpp/releases/tag/1.8.163 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.8.163") or later    | 4.0.2                 |                   | 3.4.1            | 3.3.3               |       |       |       | 1.1.0 |
| [2021-02-09](#release-notes-02092021 "#release-notes-02092021")                                                                                                       | [1.8.139](https://github.com/aws/aws-sdk-cpp/releases/tag/1.8.139 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.8.139") or later    | 4.0.2                 |                   | 3.4.1            | 3.3.3               |       |       |       | 1.1.0 |
| [2020-12-22](#release-notes-12222020 "#release-notes-12222020")                                                                                                       | [1.8.95](https://github.com/aws/aws-sdk-cpp/releases/tag/1.8.95 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.8.95") or later       | 4.0.2                 |                   | 3.4.1            | 3.3.3               |       |       |       | 1.1.0 |
| [2020-11-24](#release-notes-11242020 "#release-notes-11242020")                                                                                                       | [1.8.95](https://github.com/aws/aws-sdk-cpp/releases/tag/1.8.95 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.8.95") or later       | 4.0.2                 |                   | 3.4.1            | 3.3.2               |       |       |       | 1.1.0 |
| [2020-11-11](#release-notes-11112020 "#release-notes-11112020")                                                                                                       | [1.8.36](https://github.com/aws/aws-sdk-cpp/releases/tag/1.8.36 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.8.36") or later       | 4.0.2                 |                   | 3.4.1            | 3.3.2               |       |       |       | 1.1.0 |
| [2020-09-17](#release-notes-09172020 "#release-notes-09172020")                                                                                                       | [1.8.36](https://github.com/aws/aws-sdk-cpp/releases/tag/1.8.36 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.8.36") or later       | 4.0.1                 |                   | 3.4.1            | 3.3.2               |       |       |       | 1.1.0 |
| [2020-08-27](#release-notes-04162020 "#release-notes-04162020")                                                                                                       | [1.7.310](https://github.com/aws/aws-sdk-cpp/releases/tag/1.7.310 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.7.310") or later    | 4.0.0                 |                   | 3.4.0            | 3.3.1               |       |       |       | 1.1.0 |
| [2020-04-16](#release-notes-04162020 "#release-notes-04162020")                                                                                                       | [1.7.310](https://github.com/aws/aws-sdk-cpp/releases/tag/1.7.310 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.7.310") or later    | 4.0.0                 |                   | 3.4.0            | 3.3.1               |       |       |       | 1.1.0 |
| [2020-04-02](#release-notes-04022020 "#release-notes-04022020")                                                                                                       | [1.7.310](https://github.com/aws/aws-sdk-cpp/releases/tag/1.7.310 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.7.310") or later    | 3.4.0                 |                   | 3.4.0            |                     |       |       |       | 1.1.0 |
| [2019-12-19](#release-notes-12192019 "#release-notes-12192019")                                                                                                       | [1.7.249](https://github.com/aws/aws-sdk-cpp/releases/tag/1.7.249 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.7.249") or later    | 3.4.0                 |                   | 3.4.0            |                     |       |       |       | 1.1.0 |
| [2019-11-14](#release-notes-11142019 "#release-notes-11142019")                                                                                                       | [1.7.210](https://github.com/aws/aws-sdk-cpp/releases/tag/1.7.210 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.7.210") or later    | 3.4.0                 |                   | 3.4.0            |                     |       |       |       | 1.1.0 |
| [2019-10-24](https://aws.amazon.com/releasenotes/release-amazon-gamelift-on-2019-10-24/ "https://aws.amazon.com/releasenotes/release-amazon-gamelift-on-2019-10-24/") | [1.7.210](https://github.com/aws/aws-sdk-cpp/releases/tag/1.7.210 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.7.210") or later    | 3.4.0                 |                   | 3.4.0            |                     |       |       |       | 1.1.0 |
| [2019-09-03](https://aws.amazon.com/releasenotes/release-amazon-gamelift-on-2019-09-03/ "https://aws.amazon.com/releasenotes/release-amazon-gamelift-on-2019-09-03/") | [1.7.175](https://github.com/aws/aws-sdk-cpp/releases/tag/1.7.175 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.7.175") or later    | 3.4.0                 |                   | 3.4.0            |                     |       |       |       | 1.1.0 |
| [2019-07-09](https://aws.amazon.com/releasenotes/release-amazon-gamelift-on-2019-07-09/ "https://aws.amazon.com/releasenotes/release-amazon-gamelift-on-2019-07-09/") | [1.7.140](https://github.com/aws/aws-sdk-cpp/releases/tag/1.7.140 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.7.140") or later    | 3.3.0                 |                   | 3.3.0            |                     |       |       |       | 1.0.0 |
| [2019-04-25](https://aws.amazon.com/releasenotes/release-amazon-gamelift-on-2019-04-25/ "https://aws.amazon.com/releasenotes/release-amazon-gamelift-on-2019-04-25/") | [1.7.91](https://github.com/aws/aws-sdk-cpp/releases/tag/1.7.91 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.7.91") or later       | 3.3.0                 |                   | 3.3.0            |                     |       |       |       | 1.0.0 |
| [2019-03-07](https://aws.amazon.com/releasenotes/release-amazon-gamelift-on-2019-03-07/ "https://aws.amazon.com/releasenotes/release-amazon-gamelift-on-2019-03-07/") | [1.7.65](https://github.com/aws/aws-sdk-cpp/releases/tag/1.7.65 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.7.65") or later       | 3.3.0                 |                   | 3.3.0            |                     |       |       |       |       |
| [2019-02-07](https://aws.amazon.com/releasenotes/release-amazon-gamelift-on-2019-02-07/ "https://aws.amazon.com/releasenotes/release-amazon-gamelift-on-2019-02-07/") | [1.7.45](https://github.com/aws/aws-sdk-cpp/releases/tag/1.7.45 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.7.45") or later       | 3.3.0                 |                   | 3.3.0            |                     |       |       |       |       |
| [2018-12-14](https://aws.amazon.com/releasenotes/release-amazon-gamelift-on-2018-12-14/ "https://aws.amazon.com/releasenotes/release-amazon-gamelift-on-2018-12-14/") | [1.6.20](https://github.com/aws/aws-sdk-cpp/releases/tag/1.6.20 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.6.20") or later       | 3.3.0                 |                   | 3.3.0            |                     |       |       |       |       |
| [2018-09-27](https://aws.amazon.com/releasenotes/release-amazon-gamelift-on-2018-09-27/ "https://aws.amazon.com/releasenotes/release-amazon-gamelift-on-2018-09-27/") | [1.6.20](https://github.com/aws/aws-sdk-cpp/releases/tag/1.6.20 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.6.20") or later       | 3.2.1                 |                   | 3.2.1            |                     |       |       |       |       |
| [2018-06-14](https://aws.amazon.com/releasenotes/release-amazon-gamelift-on-2018-06-14/ "https://aws.amazon.com/releasenotes/release-amazon-gamelift-on-2018-06-14/") | [1.4.47](https://github.com/aws/aws-sdk-cpp/releases/tag/1.4.47 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.4.47") or later       | 3.2.1                 |                   | 3.2.1            |                     |       |       |       |       |
| [2018-05-10](https://aws.amazon.com/releasenotes/release-amazon-gamelift-on-2018-05-10/ "https://aws.amazon.com/releasenotes/release-amazon-gamelift-on-2018-05-10/") | [1.4.47](https://github.com/aws/aws-sdk-cpp/releases/tag/1.4.47 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.4.47") or later       | 3.2.1                 |                   | 3.2.1            |                     |       |       |       |       |
| [2018-02-15](https://aws.amazon.com/releasenotes/release-amazon-gamelift-on-2018-02-15/ "https://aws.amazon.com/releasenotes/release-amazon-gamelift-on-2018-02-15/") | [1.3.58](https://github.com/aws/aws-sdk-cpp/releases/tag/1.3.58 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.3.58") or later       | 3.2.1                 |                   | 3.2.1            |                     |       |       |       |       |
| [2018-02-08](https://aws.amazon.com/releasenotes/release-amazon-gamelift-on-2018-02-08/ "https://aws.amazon.com/releasenotes/release-amazon-gamelift-on-2018-02-08/") | [1.3.52](https://github.com/aws/aws-sdk-cpp/releases/tag/1.3.52 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.3.52") or later       | 3.2.0                 |                   | 3.2.0            |                     |       |       |       |       |
| [2017-09-01](https://aws.amazon.com/releasenotes/release-amazon-gamelift-on-2017-08-31/ "https://aws.amazon.com/releasenotes/release-amazon-gamelift-on-2017-08-31/") | [1.1.43](https://github.com/aws/aws-sdk-cpp/releases/tag/1.1.43 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.1.43") or later       | 3.1.7                 |                   | 3.1.7            |                     |       |       |       |       |
| [2017-08-16](https://aws.amazon.com/releasenotes/release-amazon-gamelift-on-2017-08-16/ "https://aws.amazon.com/releasenotes/release-amazon-gamelift-on-2017-08-16/") | [1.1.31](https://github.com/aws/aws-sdk-cpp/releases/tag/1.1.31 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.1.31") or later       | 3.1.7                 |                   | 3.1.7            |                     |       |       |       |       |
| [2017-05-16](https://aws.amazon.com/releasenotes/release-amazon-gamelift-on-2017-05-16/ "https://aws.amazon.com/releasenotes/release-amazon-gamelift-on-2017-05-16/") | [1.0.122](https://github.com/aws/aws-sdk-cpp/releases/tag/1.0.122 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.0.122") or later    | 3.1.5                 |                   | 3.1.5            |                     |       |       |       |       |
| [2017-04-11](https://aws.amazon.com/releasenotes/release-amazon-gamelift-on-2017-04-11/ "https://aws.amazon.com/releasenotes/release-amazon-gamelift-on-2017-04-11/") | [1.0.103](https://github.com/aws/aws-sdk-cpp/releases/tag/1.0.103 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.0.103") or later    | 3.1.5                 |                   | 3.1.5            |                     |       |       |       |       |
| [2017-02-21](https://aws.amazon.com/releasenotes/release-amazon-gamelift-on-2017-02-21/ "https://aws.amazon.com/releasenotes/release-amazon-gamelift-on-2017-02-21/") | [1.0.72](https://github.com/aws/aws-sdk-cpp/releases/tag/1.0.72 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.0.72") or later       | 3.1.5                 |                   | 3.1.5            |                     |       |       |       |       |
| [2016-11-18](https://aws.amazon.com/releasenotes/release-amazon-gamelift-on-2016-11-18/ "https://aws.amazon.com/releasenotes/release-amazon-gamelift-on-2016-11-18/") | [1.0.31](https://github.com/aws/aws-sdk-cpp/releases/tag/1.0.31 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.0.31") or later       |                       |                   | 3.1.0            |                     |       |       |       |       |
| [2016-10-13](https://aws.amazon.com/releasenotes/release-amazon-gamelift-on-2016-10-13/ "https://aws.amazon.com/releasenotes/release-amazon-gamelift-on-2016-10-13/") | [1.0.17](https://github.com/aws/aws-sdk-cpp/releases/tag/1.0.17 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.0.17") or later       |                       |                   | 3.1.0            |                     |       |       |       |       |
| [2016-09-01](https://aws.amazon.com/releasenotes/release-amazon-gamelift-on-2016-09-01/ "https://aws.amazon.com/releasenotes/release-amazon-gamelift-on-2016-09-01/") | [0.14.9](https://github.com/aws/aws-sdk-cpp/releases/tag/0.14.9 "https://github.com/aws/aws-sdk-cpp/releases/tag/0.14.9") or later       |                       |                   | 3.1.0            |                     |       |       |       |       |
| [2016-08-04](https://aws.amazon.com/releasenotes/release-amazon-gamelift-on-2016-08-04/ "https://aws.amazon.com/releasenotes/release-amazon-gamelift-on-2016-08-04/") | [0.12.16](https://github.com/aws/aws-sdk-cpp/releases/tag/0.12.16 "https://github.com/aws/aws-sdk-cpp/releases/tag/0.12.16") or later    |                       |                   | 3.0.7            |                     |       |       |       |       |

## Release notes

The following release notes are in chronological order, with the latest updates listed
first. Amazon GameLift Servers was first released in 2016. For release notes dated earlier than those
listed here, see the release date links in [SDK versions](#release-notes-history "#release-notes-history").

Amazon GameLift Servers customers can now use the Windows Server 2022 operating system to host their game servers. Windows Server 2022 offers several improvements over Windows Server 2016 including security. This operating system is available in all AWS Regions with the exception of the China Regions.

Customers can use the newer Windows operating systems and continue to receive critical security updates when support ends for Windows Server 2016 in January 2027. Support for Windows Server 2022 continues through October 13, 2031.

Amazon GameLift Servers API Reference links:

- [AWS SDK
  action `CreateBuild`](../apireference/API_CreateBuild.md "../apireference/API_CreateBuild.md")
- [CLI command
  `upload-build`](../../../cli/latest/reference/gamelift/upload-build.md "../../../cli/latest/reference/gamelift/upload-build.md")
- [CLI command
  `create-build`](../../../cli/latest/reference/gamelift/create-build.md "../../../cli/latest/reference/gamelift/create-build.md")
  Amazon GameLift Servers now includes built-in OpenTelemetry (OTel) metrics collection in all server SDKs and plugins, providing standardized observability for game server performance monitoring. This integration brings industry-standard telemetry capabilities directly to your game servers, enabling comprehensive monitoring and troubleshooting without requiring additional instrumentation or configuration.

With OpenTelemetry integration, you can now:

- Automatically capture essential game server metrics, logs, and traces using standardized protocols
- Integrate seamlessly with existing monitoring platforms and observability tools
- Monitor game server performance and health in real-time across all fleet instances
- Troubleshoot issues faster with telemetry data that works across different monitoring solutions
  OpenTelemetry is an open-source observability framework that provides a standardized way to collect, process, and export telemetry data.

###### **Learn more:**

- [Monitor with server telemetry metrics](monitoring-gamelift-servers-metrics.md "monitoring-gamelift-servers-metrics.md"), _Amazon GameLift Servers Developer Guide_
  Amazon GameLift Servers now provides direct remote access to managed EC2 and container fleet instances through the Amazon GameLift Servers console, eliminating the need for authentication management. This new feature uses Amazon EC2 Systems Manager (SSM) to provide secure, browser-based terminal access without requiring additional setup or credential management.

With console-based remote access, you can now:

- Troubleshoot game server integration issues in real-time
- Monitor game server activity and access log files during active game sessions
- Run diagnostics and benchmarking tools using actual player traffic
  This feature is available for fleets running server SDK version 5.x. For fleets running earlier SDK versions, you can continue to use the existing AWS CLI method for remote access.

To remotely connect to a fleet instance, open the Amazon GameLift Servers console and find the managed EC2 or container fleet you want to access. In the fleet's details, open the **Instances** tab, select an instance from the list, and choose **Connect**.

###### **Learn more:**

- [Remotely connect to Amazon GameLift Servers fleet instances](fleets-remote-access.md "fleets-remote-access.md"), _Amazon GameLift Servers Developer Guide_
  With Amazon GameLift Servers managed hosting, you can now deploy game server resources in a new
  Dallas, TX, Local Zone (`us-east-1-dfw-2`). Local Zones give you the ability to
  place your game servers geographically closer to your players to reduce latency
  and significantly improve gameplay. In this new Local Zone, you can use the following
  EC2 instance types: C6gn, C6i, C6in, M6g, M6i, M6in, M8g, and R6i. For detailed
  descriptions of each instance type, see [AWS EC2 instance types](https://aws.amazon.com/ec2/instance-types/ "https://aws.amazon.com/ec2/instance-types/").

To start hosting game sessions in the new Dallas Local Zone, first opt in to the Local Zone for your
AWS account. Then you can add it
as a remote location to a new or existing multi-location fleet. If
your game uses Amazon GameLift Servers FlexMatch, update any of the fleets in your matchmaking queue to include
the new Local Zone. With multi-location fleets, you can directly manage hosting
capacity in each location.

The parent AWS Region for the new Dallas, TX, Local Zone is
`us-east-1` (Virginia). The original Dallas, TX, Local Zone
(`us-east-1-dfw-1`) is no longer accepting new opt-in
requests.

###### **Learn more:**

- [Getting started
  with AWS Local Zones](../../../local-zones/latest/ug/getting-started.md "../../../local-zones/latest/ug/getting-started.md"), _AWS Local Zones User
  Guide_
- [Amazon GameLift Servers service locations](gamelift-regions.md "gamelift-regions.md"), _Amazon GameLift Servers Developer
  Guide_
- [Update fleet locations](fleets-update-locations.md "fleets-update-locations.md"),
  _Amazon GameLift Servers Developer Guide_
  **Updated plugin version:**

- [Plugin for
  Unreal](https://github.com/amazon-gamelift/amazon-gamelift-plugin-unreal "https://github.com/amazon-gamelift/amazon-gamelift-plugin-unreal"), version 3.0.1 (includes the server SDK for Unreal,
  version 5.3.1)
  Amazon GameLift Servers releases new versions of the plugin for Unreal Engine and the server SDK for Unreal Engine. These latest versions include the following updates:

- They now support use with Unreal Engine 5.6.
- Compilation issues when packaging Android client targets are resolved.

###### **Learn more:**

- [Integrating
  games with the Amazon GameLift Servers plugin for Unreal Engine](unreal-plugin.md "unreal-plugin.md"), _Amazon GameLift Servers Developer
  Guide_
- [Integrate
  Amazon GameLift Servers into an Unreal Engine project](integration-engines-setup-unreal.md "integration-engines-setup-unreal.md"), _Amazon GameLift Servers Developer Guide_
  **Updated SDK versions:**

- AWS SDK 1.11.595
  Amazon GameLift Servers releases for general availability a set of fixed endpoints called UDP
  ping beacons to help you accurately measure latency between player devices and
  game server locations. The UDP ping beacon endpoints are available in all AWS
  Global Regions and Local Zones supported by Amazon GameLift Servers, with the exception of the
  AWS China Regions.

Most multiplayer games use UDP (User Datagram Protocol) as their primary
packet transmission protocol due to its performance benefits for real-time
gaming. Understanding and optimizing network latency is crucial for delivering
the best possible player experience. UDP ping beacons provide a consistent and
reliable way to measure actual UDP packet latency between players and game
servers, helping you make better decisions about player-to-server matching and
game session placement.

The [ListLocations](../apireference/API_ListLocations.md "../apireference/API_ListLocations.md") API has been extended to include endpoint domain and
port information as part of the list of locations it returns, making it easy to
programmatically access the endpoints.

Your game client can send UDP messages to these endpoints and receive
asynchronous responses with the same data, giving you latency measurements that
better represent actual game traffic conditions between a player's device and
potential hosting locations. These endpoints are permanent and remain available
as long as Amazon GameLift Servers supports game hosting in that location.

**Learn more:**

- [UDP ping beacons](reference-udp-ping-beacons.md "reference-udp-ping-beacons.md"), _Amazon GameLift Servers Developer Guide_
- [ListLocations](../apireference/API_ListLocations.md "../apireference/API_ListLocations.md"), _Amazon GameLift Servers API Reference_
  With Amazon GameLift Servers managed hosting, you can now deploy game server resources in
  Bangkok, Thailand, and Kuala Lumpur, Malaysia, extending the reach of your games
  to players throughout Southeast Asia. These new Regions help reduce latency and
  improve gameplay experience for players in those areas.

The following AWS Regions are available as remote locations for
multi-location fleets. To begin hosting game sessions in these locations, add
them as remote locations to a new or existing multi-location fleet. With
multi-location fleets, you can directly manage hosting capacity in each
location.

- Asia Pacific (Thailand) (`ap-southeast-7`)
- Asia Pacific (Malaysia) (`ap-southeast-5`)
  These AWS Regions are not enabled by default for an AWS account. You mut
  opt in to each Region before you can deploy Amazon GameLift Servers resources there.

###### **Learn more:**

- [Amazon GameLift Servers service locations](gamelift-regions.md "gamelift-regions.md"),
  _Amazon GameLift Servers Hosting Developer Guide_
- [Update fleet locations](fleets-update-locations.md "fleets-update-locations.md"), _Amazon GameLift Servers Hosting
  Developer Guide_
- [Enable or
  disable AWS Regions in your account](../../../accounts/latest/reference/manage-acct-regions.md "../../../accounts/latest/reference/manage-acct-regions.md"), _AWS
  Account Management Reference Guide_.
  **Updated SDK versions:**

- [C++ server SDK](https://github.com/amazon-gamelift/amazon-gamelift-servers-cpp-server-sdk "https://github.com/amazon-gamelift/amazon-gamelift-servers-cpp-server-sdk"), version 5.3.0
- [C# server SDK](https://github.com/amazon-gamelift/amazon-gamelift-servers-csharp-server-sdk "https://github.com/amazon-gamelift/amazon-gamelift-servers-csharp-server-sdk"), version 5.3.0
- [Go server SDK](https://github.com/amazon-gamelift/amazon-gamelift-servers-go-server-sdk "https://github.com/amazon-gamelift/amazon-gamelift-servers-go-server-sdk"), version 5.3.0
- [Server SDK for Unreal](https://github.com/amazon-gamelift/amazon-gamelift-plugin-unreal "https://github.com/amazon-gamelift/amazon-gamelift-plugin-unreal"), version 5.3.0
- [Server SDK for Unity](https://github.com/amazon-gamelift/amazon-gamelift-plugin-unity "https://github.com/amazon-gamelift/amazon-gamelift-plugin-unity"), version 5.3.0
  **Updated plugin versions:**

- [Plugin for Unreal](https://github.com/amazon-gamelift/amazon-gamelift-plugin-unreal "https://github.com/amazon-gamelift/amazon-gamelift-plugin-unreal"), version 3.0.0
- [Plugin for Unity](https://github.com/amazon-gamelift/amazon-gamelift-plugin-unity "https://github.com/amazon-gamelift/amazon-gamelift-plugin-unity"), version 3.1.0
  New versions of the server SDK for C++, C#, Go, Unreal and Unity, as well as
  new plugin versions for Unreal Engine and Unity, are now open source. They are
  all available in the [Amazon GameLift Servers
  GitHub organization](https://github.com/amazon-gamelift "https://github.com/amazon-gamelift"). For detailed update information, see the
  release notes and readmes in each repository.

**Key server SDK updates:**

- Improved client-side validation and error responses in all server SDKs.
- The [OnProcessTerminate](integration-server-sdk5-cpp-datatypes.md#integration-server-sdk5-cpp-dataypes-process "integration-server-sdk5-cpp-datatypes.md#integration-server-sdk5-cpp-dataypes-process")
  callback function now has default logic to end the game server
  process.
- The function [InitSDK()](integration-server-sdk5-cpp-actions.md#integration-server-sdk5-cpp-initsdk "integration-server-sdk5-cpp-actions.md#integration-server-sdk5-cpp-initsdk") now uses an idempotency token to support multiple retries.
- The [OnUpdateGameSession](integration-server-sdk5-cpp-datatypes.md#integration-server-sdk5-cpp-dataypes-process "integration-server-sdk5-cpp-datatypes.md#integration-server-sdk5-cpp-dataypes-process") callback can now pass data for autoBackfillMode.
  **Key plugin updates:**

- The plugin for Unreal Engine now has a more streamlined install and setup process, with more
  automation and fewer prerequisites (CMake, OpenSSL, and the Unreal
  cross-compile tool chain).
- The plugin for Unreal Engine has improved UI experience
  for the Managed EC2 workflow, including support for spaces in the game
  client and server build paths. In addition, you can now add command-line
  arguments when launching a game client from the Editor.
- The plugin for Unreal Engine now supports ARM server builds in UE5.
  **Learn more:**

- [Amazon GameLift Servers plugin for Unreal Engine](unreal-plugin.md "unreal-plugin.md"), _Amazon GameLift Servers Developer Guide_
- [Amazon GameLift Servers plugin for Unity (server SDK 5.x)](unity-plug-in.md "unity-plug-in.md"), _Amazon GameLift Servers Developer Guide_
- [Server SDK 5.x for Amazon GameLift Servers](reference-serversdk.md "reference-serversdk.md"), _Amazon GameLift Servers Developer Guide_
- [Integrate Amazon GameLift Servers into an Unreal Engine
  project](integration-engines-setup-unreal.md "integration-engines-setup-unreal.md"), _Amazon GameLift Servers Developer Guide_
- [Integrate Amazon GameLift Servers into a Unity
  project](integration-engines-unity-using.md "integration-engines-unity-using.md"), _Amazon GameLift Servers Developer Guide_
  **Updated SDK versions:**

- C# Server SDK, version 5.2.1
  For game developers using C#, you can now use .NET 8 as a target framework for
  your Amazon GameLift Servers projects. With .NET 8, you can take advantage of performance
  improvements, including improved just-in-time (JIT) compilation, memory usage
  optimization, and faster startup times. If you're currently using .NET 6, we
  recommend that you plan a migration to .NET 8, including updating your C# server
  SDK to the latest version. Microsoft announced .NET 8 support, with security
  patches and technical updates, through November 2026.

**[Download the latest
version of the C# server SDK for Amazon GameLift Servers](https://aws.amazon.com/gamelift/servers/getting-started/#custom "https://aws.amazon.com/gamelift/servers/getting-started/#custom")**

**Learn more:**

- [Get Amazon GameLift Servers development tools](gamelift-supported.md "gamelift-supported.md"), _Amazon GameLift Servers Developer Guide_
  **Updated SDK versions:**

- AWS SDK 1.11.535
  You can now fine-tune your game server hosting with Amazon GameLift Servers by selecting from a
  larger selection of Amazon EC2 instances across the 5th through 8th generation
  instance families. Each new EC2 generation offers advancements in EC2 compute,
  memory and networking, with the 8th generation instances delivering cutting-edge
  AWS Graviton4 and Intel Xeon-based instances. Next generation instances are
  available in the following instance families:

- [General purpose](https://aws.amazon.com/ec2/instance-types/#General_Purpose "https://aws.amazon.com/ec2/instance-types/#General_Purpose") (M-series)
- [Compute optimized](https://aws.amazon.com/ec2/instance-types/#Compute_Optimized "https://aws.amazon.com/ec2/instance-types/#Compute_Optimized") (C-series)
- [Memory optimized](https://aws.amazon.com/ec2/instance-types/#Memory_Optimized "https://aws.amazon.com/ec2/instance-types/#Memory_Optimized") (R-series)
  You can also choose variants that offer local storage (d), enhanced
  networking (n), and specific processor architectures (Intel/AMD/Graviton
  – i/a/g). The next-generation instances are available in all
  AWS Regions that are supported by Amazon GameLift Servers, with the exception of the AWS China
  Regions. For more details, see [Amazon GameLift Servers service locations](gamelift-regions.md "gamelift-regions.md").

Use these new instance types with Amazon GameLift Servers managed EC2 fleets and managed
container fleets. When switching your existing game hosting to a new instance
type (same architecture), simply deploy new fleets with all configuration
settings unchanged except the instance type.

**Learn more:**

- [Amazon GameLift Servers Instance Pricing](https://aws.amazon.com/gamelift/pricing/instance-pricing/ "https://aws.amazon.com/gamelift/pricing/instance-pricing/")
- [CreateFleet](../apireference/API_CreateFleet.md "../apireference/API_CreateFleet.md")
  _Amazon GameLift Servers API Reference_
- [CreateContainerFleet](../apireference/API_CreateContainerFleet.md "../apireference/API_CreateContainerFleet.md"),
  _Amazon GameLift Servers API Reference_
  The new game server wrapper for Amazon GameLift Servers significantly reduces the time required
  to get a game server hosted on Amazon GameLift Servers. With no code changes required, you can use
  the wrapper to add basic game session management functionality to your game and
  deploy it to an Amazon GameLift Servers Anywhere fleet, managed EC2 fleet, or managed container
  fleet. This tool is ideal for doing a hands-on evaluation of Amazon GameLift Servers features,
  using your own game server or one from a sample game. It is also useful for
  quickly deploying game server iterations, such as for rapid prototyping or
  testing.

With the basic game session management features, your game server can
initialize a connection with the Amazon GameLift Servers service, respond to prompts to start and
stop game sessions, and shut down when a game session is complete.

**[Download the game server wrapper from GitHub.](https://github.com/amazon-gamelift/amazon-gamelift-servers-game-server-wrapper "https://github.com/amazon-gamelift/amazon-gamelift-servers-game-server-wrapper")** See
the readme on GitHub for how to install and use the wrapper with your game
projects.

Amazon GameLift is a fully-managed service that's dedicated to helping developers
build, scale, and deliver the world's most demanding games. With the general
availability release of Amazon GameLift Streams, Amazon GameLift now offers both
high-scaling game server and smooth-gameplay streaming capabilities.

**[Amazon GameLift Servers](../../../gamelift.md "../../../gamelift.md")** gives game developers the capability to
deploy, operate, and scale dedicated game servers. You can deploy
high-performance game servers in the cloud in minutes and scale up and down to
meet player demand. Built on AWS proven computing environment, Amazon GameLift Servers supports
100 million concurrent players in a single game, 100 thousand player adds per
second, and 9 thousand new compute instances per minute. And with
enterprise-grade security, matchmaking for the largest crowds, and pay-as-you-go
flexibility, it helps you get started whether you’re working on a new game idea
or running a game with millions of players.

**[Amazon GameLift Streams](../../../gameliftstreams.md "../../../gameliftstreams.md")** helps game developers deliver
game streaming experiences at up to 1080p resolution and 60 frames-per-second
(fps) with no perceivable lag across devices including iOS, Android, FireOS, and
PCs for gamers. Using a single AWS offering, publishers can deploy their game
content in minutes, without modifications, onto fully-managed cloud-based GPU
instances and deliver them through the AWS Network Backbone directly to any
end-player device with a web browser. Players can start gaming in just a few
seconds, without waiting for a download or an install and it delivers a gameplay
experience that is nearly indistinguishable from playing the game locally on a
PC or gaming console.

**Updated SDK versions:**

- AWS SDK 1.11.485
  In response to customer feedback, we're releasing new functionality that lets you prioritize
  locations for individual game session placement requests. For your queues that are configured to
  prioritize placement by location, you can now provide a customized list of priority locations
  with each placement request.

This new feature lets customers dynamically change location priorities for each placement request as needed.
The additional flexibility means that you can better respond to changing conditions,
such as player locations, fleet load, or server health. It can also support customers who want to
further customize how placement locations are selected.

###### **Learn more:**

- [Prioritize game session placement](queues-design-priority.md "queues-design-priority.md"), _Amazon GameLift Servers Developer Guide_
- [StartGameSessionPlacement](../apireference/API_StartGameSessionPlacement.md "../apireference/API_StartGameSessionPlacement.md"), _Amazon GameLift Servers API Reference_
  **Updated SDK versions:**

- AWS SDK 1.11.477
  In response to customer feedback, we're releasing new functionality that lets you more easily
  terminate individual game sessions. With this release, you can now terminate a game session directly in
  the Amazon GameLift Servers console or by using the AWS CLI or AWS SDK for Amazon GameLift Servers.

This new feature addresses the need to resolve game sessions that remain active but in a
bad state, which prevents compute resources from hosting new game sessions. Previously, customers
were required to remotely access the compute to manually terminate a game session.

You have two termination methods to choose from. The first method attempts to gracefully terminate
a game session using its custom shutdown sequence, which might include actions to notify players and resolve game data.
The second method forces the server process to stop, which terminates the game session immediately. This second method
ensures that the game session ends even when the server process is not responding.

###### **Learn more:**

- [Shut down a game session using the Amazon GameLift Servers console](terminate-sessions.md "terminate-sessions.md"), _Amazon GameLift Servers Developer Guide_
- [TerminateGameSession](../apireference/API_TerminateGameSession.md "../apireference/API_TerminateGameSession.md"), _Amazon GameLift Servers API Reference_
  **Updated plugin versions:**

Amazon GameLift Servers plugin for Unreal Engine, version 2.0.0

- Upgraded to support C++ server SDK 5.2.0 with managed containers
  support.
- Added support for Unreal Engine 5.4 and 5.5.
  Amazon GameLift Servers plugin for Unity, version 3.0.0

- Upgraded to support C++ server SDK 5.2.0 with managed containers
  support.
- Support for Unity 2021.3 LTS and 2022.3 LTS for Windows and Mac
  OS.
  The Amazon GameLift Servers plugin for the Unreal and Unity game engines provides tools and
  workflows that streamline your steps to getting a game up and running with
  Amazon GameLift Servers. Amazon GameLift Servers is a fully managed cloud hosting service that game developers can
  use to manage and scale dedicated game servers for session-based multiplayer
  games.

The latest plugin versions offer the following enhancements:

- **Guided workflow for hosting with Managed
  Containers.** This workflow walks you through the steps to
  set up a container image with your game server software, and deploy a
  cloud-based hosting solution for your game server. The workflow offers
  two different deployment scenarios: a simple deployment and a more
  complete deployment with a game session placement queue and a FlexMatch
  matchmaker. Each scenario generates Amazon GameLift Servers container fleets and
  supporting AWS resources.
- **Improved process for setting up AWS user
  profiles and managing AWS access credentials for plugin
  use.** You can maintain multiple profiles to work with
  different AWS accounts, account users, and regions.
- **Additional functionality to update existing
  container fleets.** You can deploy new container images
  (such as for game server version updates) and change fleet configuration
  settings without having to start from the beginning.
- **Improved workflows for hosting with Amazon GameLift Servers
  Anywhere fleets and Managed EC2.** Improvements based on
  customer feedback include better guidance with tips and links to helpful
  resources.
  The deployment scenarios for Managed Containers and Managed EC2 solutions use
  AWS CloudFormation templates to create and deploy the AWS resources for each
  scenario. These templates are included in the Amazon GameLift Servers plugin download and are
  editable. You can use them as is or modify them for your game.

###### **Learn more:**

- [Plugin for Unreal: Deploy your game to a
  managed container fleet](unreal-plugin-container.md "unreal-plugin-container.md"), _Amazon GameLift Servers Developer Guide_
- [Plugin for Unity: Deploy your game to a
  managed container fleet](unity-plug-in-container.md "unity-plug-in-container.md"), _Amazon GameLift Servers Developer Guide_
- [Download the plugin for
  Unreal from GitHub](https://github.com/aws/amazon-gamelift-plugin-unreal "https://github.com/aws/amazon-gamelift-plugin-unreal")
- [Download the plugin for
  Unity from GitHub](https://github.com/aws/amazon-gamelift-plugin-unity "https://github.com/aws/amazon-gamelift-plugin-unity")
- [Game hosting with Amazon GameLift Servers](https://aws.amazon.com/gamelift/servers/ "https://aws.amazon.com/gamelift/servers/")
- [Amazon GameLift Servers forum](https://forums.awsgametech.com/c/amazon-gamelift/ "https://forums.awsgametech.com/c/amazon-gamelift/")
  **Updated SDK versions:**

- AWS SDK 1.11.445
- Server SDK, version 5.2.0 (all languages)
  Amazon GameLift Servers releases for general availability a new hosting solution for
  containerized game server workloads. With this release, game developers can now
  take advantage of the benefits of containerization including consistent, secure
  environments, a simplified deployment process, and optimized resource
  utilization.

Managed container fleets use Amazon EC2 instances that are managed by Amazon GameLift Servers on your
behalf and based on your configurations. You build a custom container
architecture for your game and provide container images by storing them in a
Amazon Elastic Container Registry (Amazon ECR) repository. Container fleets are available for Linux-based
game servers only. Game servers must be integrated with Server SDK 5.2.0 or
greater.

With managed container fleets, you get the same benefits as with managed EC2
fleets. This includes support for On-Demand and Spot instance types, intelligent
capacity scaling, game session placement with queues, and matchmaking. You also
get the same metrics as other fleet types along with some new ones for
containers. Other features for container fleets include:

- **Alignment with serverless experience for
  containerized workloads.** Run one game server process
  per container and pack many containers onto each fleet instance for
  optimal resource usage. If you prefer to have containers with
  multiple game server processes, you can use the Amazon GameLift Servers Agent for
  automated host management.
- **Streamlined fleet creation.**
  Container fleets are designed to require minimal deployment
  configuration settings, with sensible suggested/default values. You
  can quickly deploy a working fleet, and then customize individual
  settings as needed.

- **Versioning tools for container
  architecture.** You can now update a container group
  definition (which is similar to a container "task"), maintain multiple
  versions, and specify which version to deploy to a fleet.
- **Fleet update tools.** With container
  fleets, you no longer need to create a new fleet when you want to
  release a game server version update. Instead, you can now update your
  container image and deploy the updates to existing fleets.
  You can build Amazon GameLift Servers container fleets in any AWS Region where Amazon GameLift Servers supports
  multi-location fleets, and you can deploy container fleet instances to any
  supported remote location. For more details, see [Amazon GameLift Servers service locations](gamelift-regions.md "gamelift-regions.md"). Managed containers is not currently
  available in AWS China Regions.

###### **Learn more:**

- Blog post: [Leverage fully managed containers to host multiplayer games at global scale on Amazon GameLift Servers](https://aws.amazon.com/blogs/gametech/leverage-fully-managed-containers-to-host-multiplayer-games-at-global-scale-on-amazon-gamelift/ "https://aws.amazon.com/blogs/gametech/leverage-fully-managed-containers-to-host-multiplayer-games-at-global-scale-on-amazon-gamelift/")
- [Managed containers](gamelift-intro-flavors.md#gamelift-intro-flavors-hosting-managed-containers "gamelift-intro-flavors.md#gamelift-intro-flavors-hosting-managed-containers")
  overview, _Amazon GameLift Servers Developer
  Guide_
- [How containers work in Amazon GameLift Servers](containers-howitworks.md "containers-howitworks.md"), _Amazon GameLift Servers Developer Guide_
- [Development roadmap for hosting with Amazon GameLift Servers managed
  containers](gamelift-roadmap-containers.md "gamelift-roadmap-containers.md"),
  _Amazon GameLift Servers Developer Guide_
- [CreateContainerFleet](../apireference/API_CreateContainerFleet.md "../apireference/API_CreateContainerFleet.md"), _Amazon GameLift Servers API Reference_
  **Updated SDK versions:**

C++ Server SDK, version 5.1.3

- New logging capabilities. You can now access SDK request logs.
- Improved SDK message transmission reliability. The SDK now uses more
  robust reconnection mechanisms to recover in the event of network
  interruptions or random message drops.
  **Updated plugin versions:**

Amazon GameLift Servers plugin for Unreal Engine, version 1.1.2

- Upgraded to support the latest version of the C++ server SDK
  5.1.3.
- In the Amazon GameLift Servers plugin for Unreal Engine, when browsing for a server build executable for
  a fleet, you now have the option to browse **All
  Files**.
  C++ Server SDK Plugin for Unreal, version 5.1.2

- Upgraded to support the latest version of the C++ server SDK
  5.1.3.

###### **Learn more:**

- [Integrating
  games with the Amazon GameLift Servers plugin for Unreal Engine](unreal-plugin.md "unreal-plugin.md"), _Amazon GameLift Servers Developer
  Guide_
- [Amazon GameLift Servers plugin and SDK downloads](https://aws.amazon.com/gamelift/servers/getting-started/#Amazon_GameLift_Plugins_for_Game_Engines "https://aws.amazon.com/gamelift/servers/getting-started/#Amazon_GameLift_Plugins_for_Game_Engines")
  Based on customer feedback, we've clarified the Amazon GameLift Servers workflow for creating a
  managed EC2 fleet and getting it ready to host game sessions. Improvements
  include:

- We've provided more specific and accurate descriptions of each phase
  of the fleet creation process. This improved visibility makes it easier
  to pinpoint and resolve issues faster.
- The Building and Activating phases better separate instance deployment
  tasks (building) from tasks to start game server processes and connect
  to the Amazon GameLift Servers service (activating). This change makes it easier to
  recognize the likely cause of issues. In addition, you can now remotely
  connect to fleets when they're in the Activating phase.
- Two new fleet creation events communicate the success or failure of
  game server install scripts. If you're game server build includes an
  install script, Amazon GameLift Servers attempts to run the script and emits one of the
  following new events:
  - `FLEET_CREATION_COMPLETED_INSTALLER`
  - `FLEET_CREATION_FAILED_INSTALLER`

###### **Learn more:**

- [Debug Amazon GameLift Servers fleet issues](fleets-creating-debug.md "fleets-creating-debug.md"), _Amazon GameLift Servers Developer
  Guide_
- [Event data type](../apireference/API_Event.md "../apireference/API_Event.md"), _Amazon GameLift Servers API Reference_
  Based on customer feedback, we've made the following updates to the
  [Amazon GameLift Servers console](https://console.aws.amazon.com/gamelift "https://console.aws.amazon.com/gamelift") experience:

- Your display preferences for pages are now automatically saved to your AWS account user and
  applied whenever you return to the page. Display preferences let you
  choose what information to include in a table display, such as on the
  Fleets listing page. Customize your display preferences by using the
  ![Gear icon representing settings or configuration options.](images/settings.png)
  icon in the upper right corner of a table.
- The Create Fleet workflow for managed EC2 fleets has been streamlined to combine the selection
  of fleet locations and instance types. We've made it easier for you to
  find the right instance type for your fleet, even when you change your
  locations selections.

###### **Learn more:**

- [Create an Amazon GameLift Servers managed EC2 fleet](fleets-creating.md "fleets-creating.md"), _Amazon GameLift Servers Developer
  Guide_
  With Amazon GameLift Servers managed hosting, you can now deploy game server resources in
  Nigeria, West Africa, and extend the reach of your games to players throughout
  Africa. Use AWS Local Zones to place game servers geographically closer to
  your players to reduce latency and significantly improve gameplay.

To immediately begin hosting game sessions in Nigeria, add the new Nigeria
Local Zone as a remote location to a new or existing multi-location fleet. If
your game uses Amazon GameLift Servers FlexMatch, update fleets in your matchmaking queue to include
the new Local Zone. With multi-location fleets, you can directly manage hosting
capacity in each location.

The parent AWS Region for the Lagos, Nigeria Local Zone is the Africa (Cape Town) Region (`af-south-1`),
which Amazon GameLift Servers also supports as a remote location. The Nigeria Local Zone name is `af-south-1-los-1`.

###### **Learn more:**

- [Amazon GameLift Servers service locations](gamelift-regions.md "gamelift-regions.md"), _Amazon GameLift Servers Developer
  Guide_
- [Update fleet locations](fleets-update-locations.md "fleets-update-locations.md"),
  _Amazon GameLift Servers Developer Guide_
  The Amazon GameLift Servers console now offers a player session lookup tool that lets you
  retrieve player session information by game session ID, player session ID, or
  player ID. Games that use FlexMatch matchmaking automatically generate player
  sessions for every matched player. For all other games, player sessions are an
  optional feature.

You can find the player session lookup tool in the main navigation for the
Amazon GameLift Servers console. View individual player sessions or compare data across multiple
player sessions. You can also open player session data when viewing a game
session detail page.

###### **Learn more:**

- [Game and player sessions in
  the Amazon GameLift Servers console](gamelift-console-game-player-sessions-metrics.md "gamelift-console-game-player-sessions-metrics.md"),
  _Amazon GameLift Servers Developer Guide_
  Amazon GameLift Servers is now offering a preview of container fleets, which give you improved portability, scalability, fault tolerance, and agility.

In container fleets, Amazon EC2 instances host one or more of your containers.
These containers include your game server along with whatever it requires, including dependencies and configurations.
Examples of dependencies include SDKs and software packages.
After you upload your container to your private Amazon Elastic Container Registry, Amazon GameLift Servers populates your fleet with the container.

To function in a container fleet, your game server must run in Linux and be integrated with Server SDK 5.x.
In a container fleet, you have fine-tuned control of hosting resources so that you can optimize consumption of resources such as CPU units and memory.
You can also host multiple game servers in a container to reduce the use of resources.

In a container fleet you get many of the same benefits that other types of fleets have such as On-Demand instance types, scaling (automatic and manual), queues, and matchmaking.
You also get the same metrics as other fleet types along with some new ones for containers. Container fleets give you global reach to players in these locations regions:

- ap-northeast-1
- ap-northeast-2
- ap-southeast-2
- eu-central-1
- eu-west-1
- us-east-1
- us-west-2
  To reach even more regions and local zones, create multi-location containers fleets.

###### **Learn more:**

- [Managing hosting with Amazon GameLift Servers containers](containers-intro.md "containers-intro.md"), _Amazon GameLift Servers Developer Guide_
- [CreateContainerGroupDefinition](../apireference/API_CreateContainerGroupDefinition.md "../apireference/API_CreateContainerGroupDefinition.md"), _Amazon GameLift Servers API Reference_
  **Updated SDK versions:**

- Go Server SDK, version 5.1.0
- C# Server SDK, version 5.1.2
- C++ Server SDK, version 5.1.2
  We made the following improvements:

- Improved the reliability of the SDK by adding automatic reconnection in the event of network interruption.
- [Go] You can now call `InitSDK()` with or without server parameters.
  Game servers that run on Amazon GameLift Servers managed EC2 fleets read the server parameters directly from environment variables.
  Game servers on Amazon GameLift Servers Anywhere fleets must call `InitSDK()` with server parameters.
  **Updated plugin versions:**

- Amazon GameLift Servers plugin for Unreal Engine, version 1.1.0
- Amazon GameLift Servers plugin for Unity, version 2.1.0
- C++ Server SDK Plugin for Unreal, version 5.1.1
- C# Server SDK Plugin for Unity, version 5.1.2
  We made the following improvements:

- [Amazon GameLift Servers plugin for Unreal Engine] Updated the installation instructions and simplified the packaging.
  This plugin now includes the latest version of the C++ Server SDK for Unreal.
- Upgraded the plugins to support the latest version of the server SDK for Amazon GameLift Servers.

###### **Learn more:**

- [Integrating games with the Amazon GameLift Servers plugin for Unreal Engine](unreal-plugin.md "unreal-plugin.md"), _Amazon GameLift Servers Developer Guide_
- [Amazon GameLift Servers plugin and SDK downloads](https://aws.amazon.com/gamelift/servers/getting-started/#Amazon_GameLift_Plugins_for_Game_Engines "https://aws.amazon.com/gamelift/servers/getting-started/#Amazon_GameLift_Plugins_for_Game_Engines")
  You've already been able to set game properties when creating game sessions, and to search game sessions for specified properties.
  Now you can also add and update these properties in an active game session.

For example, your players vote on a map that they want to play on.
Your game client calls `UpdateGameSession` to modify a `GameProperty` value to `{"Key": "map", "Value":"jungle"}`.
Your game then implements the new map for the players in the game session.

Game administrators can also retrieve useful data from game properties by using the `SearchGameSessions` operation.
For example, administrators can list game sessions that have a `Status` value of `ACTIVE` and this game property: `{"Key": "map", "Value":"desert"}`.

###### **Learn more:**

- [Integrate Amazon GameLift Servers game client functionality](gamelift-sdk-client-api.md "gamelift-sdk-client-api.md"), _Amazon GameLift Servers Developer Guide_
- [GameProperty](../apireference/API_GameProperty.md "../apireference/API_GameProperty.md"), _Amazon GameLift Servers API Reference_
- [UpdateGameSession](../apireference/API_UpdateGameSession.md "../apireference/API_UpdateGameSession.md"), _Amazon GameLift Servers API Reference_
- [SearchGameSessions](../apireference/API_SearchGameSessions.md "../apireference/API_SearchGameSessions.md"), _Amazon GameLift Servers API Reference_

You can now manage your entire Amazon GameLift Servers resource stack using Infrastructure as Code (IaC) tools. These tools include AWS CloudFormation, and also third-party tools such as Terraform and Pulumi. With this added support, you can now focus on building your game, and leverage DevOps strategies to take care of resource management, CI/CD, and deployment to your customers.

You can also now provision and configure all Amazon GameLift Servers resources types by using the AWS Cloud Control API. You can continue to work with resources using the Amazon GameLift Servers APIs or the AWS CloudFormation templates for Amazon GameLift Servers.

For details about the Amazon GameLift Servers resources available through IaC, see the [Amazon GameLift Servers resource type reference](../../../AWSCloudFormation/latest/UserGuide/AWS_GameLift.md "../../../AWSCloudFormation/latest/UserGuide/AWS_GameLift.md") Amazon GameLift Servers resource type reference.

In addition, you can now automatically scale your fleets using AWS CloudFormation templates or the AWS Cloud Control API by using the new [Fleet](../../../AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.md") property: `ScalingPolicies`.

The Cloud Control API gives developers a standard set of APIs to create, read, update, delete, and list resources (CRUDL) across hundreds of AWS services and multiple third-party tools like Terraform and Pulumi.

###### **Learn more:**

- [AWS CloudFormation](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md")
- [AWS Cloud Control API](../../../cloudcontrolapi/latest/userguide/what-is-cloudcontrolapi.md "../../../cloudcontrolapi/latest/userguide/what-is-cloudcontrolapi.md")
- [AWS CC Terraform Provider](https://registry.terraform.io/providers/hashicorp/awscc/latest "https://registry.terraform.io/providers/hashicorp/awscc/latest")
- [Pulumi](https://www.pulumi.com/ "https://www.pulumi.com/")
  **Updated SDK versions:** Amazon GameLift Servers plugin for Unity, version 2.0.0

The Amazon GameLift Servers plugin for Unity provides tools and workflows that
streamline the steps to getting your Unity game up and running for cloud
hosting with Amazon GameLift Servers. Amazon GameLift Servers is a fully managed service that lets game developers manage and
scale dedicated game servers for session-based multiplayer games.

With this version, the plugin for Unity is updated to use the latest Amazon GameLift Servers features,
including server SDK version 5.x and support for local testing with Amazon GameLift Servers Anywhere.
The plugin is compatible with Unity versions Unity 2021.3 LTS and 2022.3 LTS.

Key plugin features include:

- Guided UI workflows in the Unity editor for the following scenarios:
  - Test your game integration with Amazon GameLift Servers using your local
    workstation as a host. This workflow helps you set up an Amazon GameLift Servers
    Anywhere fleet for your local machine, launch instances of your
    game server and client, request a game session through Amazon GameLift Servers,
    and join the game.
  - Deploy cloud hosting solution for your integrated
    game server with Amazon GameLift Servers managed EC2 and supporting AWS resources.
    This workflow helps you configure your game for
    cloud hosting, and provides three deployment
    scenarios:
    - Deploy the game server to a single fleet.
    - Deploy the game server to a set of low-cost Spot fleets in multiple AWS Regions.
    - Deploy the game server with a FlexMatch matchmaker.

- Ability to set up user profiles that link to an AWS account user
  and set a default AWS Region. You can maintain multiple
  profiles to work in different AWS accounts, account users, and
  regions.
- Special conveniences that help streamline the Amazon GameLift Servers integration
  and deployment processes, including:
  - Each hosting solution includes supporting AWS resources,
    including an Amazon Cognito user pool that provides unique player IDs and
    player validation. The solutions also include an Amazon S3 bucket for
    storage, Amazon SNS event notification, AWS Lambda functions, and
    other resources.
  - For the Anywhere workflow, the plugin automates the required
    server parameter settings.
  - For the Amazon EC2 workflow, each deployment solution provides a
    built-in client backend service using Lambda functions. The
    backend service sits between the game client and the Amazon GameLift Servers
    service and manages all direct calls to the Amazon GameLift Servers
    service.

- Content for integration testing, including assets and code for a simple sample multiplayer game to illustrate game server and game client integration.
- Plugin documentation with detailed integration guidance and sample
  code.
  All deployment scenarios, including for Anywhere and Amazon EC2 fleets, use
  AWS CloudFormation templates to describe and deploy the AWS resources for your game's
  solution. These templates are included in the Amazon GameLift Servers plugin download. You can use
  them as is or customize them for your game.

###### **Learn more:**

- [Amazon GameLift Servers plugin for Unity (server SDK 5.x)](unity-plug-in.md "unity-plug-in.md"), _Amazon GameLift Servers Developer Guide_
- [Download the plugin from GitHub](https://github.com/aws/amazon-gamelift-plugin-unity "https://github.com/aws/amazon-gamelift-plugin-unity")
- [About Amazon GameLift Servers hosting](https://aws.amazon.com/gamelift/servers/ "https://aws.amazon.com/gamelift/servers/")
- [Amazon GameLift Servers forum](https://forums.awsgametech.com/c/amazon-gamelift/ "https://forums.awsgametech.com/c/amazon-gamelift/")
  **Updated SDK versions:** AWS SDK 1.11.193

The new Amazon GameLift Servers shared credentials feature allows applications that are
deployed on managed EC2 fleets to interact with other AWS resources. This
update affects applications that you bundle and deploy along with game server
binaries integrated with server SDK version 5.x or later. (Game server
executables can already request credentials using the server SDK 5.x
`GetFleetRoleCredentials()` action.)

For example, if you want to deploy your game server build with an Amazon CloudWatch agent to collect EC2 instance metrics and other data,
the agent needs permission to interact with your CloudWatch resources. To do this, you must first set up an AWS Identity and Access Management IAM) role with
permissions to use the CloudWatch resources, and then configure a fleet with the IAM role and shared credentials enabled.
When Amazon GameLift Servers deploys your game server build to each EC2 instance, it generates a shared credentials file and stores it on the instance.
All applications on the instance can use the shared credentials.
Amazon GameLift Servers automatically refreshes the temporary credentials throughout the life of the instance.

You can enable shared credentials when you create a managed EC2 fleet using the following methods:

- In the Amazon GameLift Servers console fleet creation workflow.
- When calling the service API operation `CreateFleet` using the new parameter `InstanceRoleCredentialsProvider`.
- When calling the AWS CLI operation `aws gamelift create-fleet` with the parameter `instance-role-credentials-provider`.

###### **Learn more:**

- [Communicate with other AWS resources from your fleets](gamelift-sdk-server-resources.md "gamelift-sdk-server-resources.md"), _Amazon GameLift Servers Developer Guide_
- [CreateFleet, InstanceRoleCredentialsProvider](../apireference/API_CreateFleet.md#gamelift-CreateFleet-request-InstanceRoleCredentialsProvider "../apireference/API_CreateFleet.md#gamelift-CreateFleet-request-InstanceRoleCredentialsProvider"), _Amazon GameLift Servers API Reference_
- [Set up an IAM service role](setting-up-role.md "setting-up-role.md"), _Amazon GameLift Servers Developer Guide_
  **Updated SDK versions:** Amazon GameLift Servers plugin for Unreal Engine version 1.0.0

The Amazon GameLift Servers plugin for Unreal Engine provides tools and workflows that
streamline your steps to getting a game up and running with Amazon GameLift Servers for cloud
hosting. Amazon GameLift Servers is a fully managed service that lets game developers manage and
scale dedicated game servers for session-based multiplayer games. The plugin
supports UE versions 5.0, 5.1, and 5.2. Key features include:

- Guided UI workflows in the Unreal editor ]step through the
  following paths:
  - Test your game integration with Amazon GameLift Servers using your local
    workstation as a host. This workflow helps you set up an Amazon GameLift Servers
    Anywhere fleet for your local machine, launch instances of your
    game server and client, request a game session through Amazon GameLift Servers,
    and get connection information for the new game session.
  - Deploy an Amazon EC2 cloud hosting solution for your integrated
    game server. This workflow helps you configure your game for
    cloud hosting, and provides three different deployment
    scenarios: deploy to a single fleet, deploy to a set of spot
    fleets in multiple regions, or deploy to a set of fleets with a
    FlexMatch matchmaker. The solution for each deployment scenario
    includes Amazon GameLift Servers resources and supporting AWS resources.

- Ability to set up user profiles that link to an AWS account user
  and define a default AWS Region. You can maintain multiple
  profiles to work in different AWS accounts, account users, and
  regions.
- Special conveniences that help streamline the Amazon GameLift Servers integration
  and deployment processes, including:
  - Each hosting solution includes supporting AWS resources,
    including a basic Amazon Cognito user pool that provides unique player
    IDs, an Amazon S3 bucket for storage, Amazon SNS event notification, and
    AWS Lambda functions.
  - For the Anywhere workflow, the plugin automates the required
    server parameter settings using command line arguments.
  - For the Amazon EC2 workflow, each deployment solution provides a
    built-in client backend service using Lambda functions. The
    backend service receives requests from game clients and passes
    them on to the Amazon GameLift Servers service.

- Content for integration testing, including a starter game map and
  two testing maps with basic blueprints and UI elements.
- Plugin documentation with detailed integration guidance and sample
  code.
  All deployment scenarios, including for Anywhere and Amazon EC2 fleets, use AWS
  CloudFormation templates to describe the solutions. The plugin uses these
  templates when deploying Amazon GameLift Servers resources for your game. These templates are
  included in the Amazon GameLift Servers plugin download and are editable. You can use them as is
  or modify them for your game.

###### **Learn more:**

- [Amazon GameLift Servers plugin for Unreal Engine](unreal-plugin.md "unreal-plugin.md"), _Amazon GameLift Servers Developer Guide_
- [Download the plugin from GitHub](https://github.com/aws/amazon-gamelift-plugin-unreal "https://github.com/aws/amazon-gamelift-plugin-unreal")
- [About Amazon GameLift Servers hosting](https://aws.amazon.com/gamelift/servers/ "https://aws.amazon.com/gamelift/servers/")
- [Amazon GameLift Servers forum](https://forums.awsgametech.com/c/amazon-gamelift/ "https://forums.awsgametech.com/c/amazon-gamelift/")
  **Updated SDK versions:** AWS SDK
  1.11.144

With Amazon GameLift Servers you can now host your games in the cloud using EC2 instances with AWS Graviton processors.
Designed by AWS with Arm64-based processors, Graviton instances
deliver the best price performance for cloud workloads using EC2, with up to 40% improvement over
comparable x86-based instances. The latest Graviton3 processors offer up to 25% better compute performance over
earlier versions.

With Amazon GameLift Servers, you can now select from these new instances in the AWS Graviton
family:

- Graviton2-based instances: c6g, c6gn, r6g, m6g, g5g
- Graviton3-based instances: c7g, r7g, m7g

###### **Learn more:**

- [AWS Graviton Processor](https://aws.amazon.com/ec2/graviton/ "https://aws.amazon.com/ec2/graviton/"): Learn about the benefits and practical uses of Graviton-based EC2 instances.
- [Getting started with
  Graviton](https://aws.amazon.com/ec2/graviton/getting-started/ "https://aws.amazon.com/ec2/graviton/getting-started/"): Get an overview of the Graviton-based instances
  and insights on how applications run on them depending on their
  operating system, languages, and run times.

###### Note

Graviton Arm instances require a server build for a Linux AMI.
Server SDK 5.1.1 or newer is required for C++ and C#. Server SDK 5.0 or newer is required for Go.
These instances do not provide out-of-the-box support for Mono installation on Amazon Linux 2023 (AL2023) or Amazon Linux 2 (AL2).

**Updated SDK versions:** Server SDK for C++,
C#/Unity, Unreal 5.1.0

The newest release of the Amazon GameLift Servers server SDK delivers updates for C++, C#, and
the Unreal plugin, and a new plugin for use with the Unity game engine. Game
developers integrate the Amazon GameLift Servers server SDK into game servers that they deploy for
hosting on Amazon GameLift Servers.

The latest server SDK version contains the following updates, which include a
number of customer requests:

- **Download language-specific SDK
  packages** – The updated [Amazon GameLift Servers
  download site](https://aws.amazon.com/gamelift/servers/getting-started/#Amazon_GameLift_Server_SDKs "https://aws.amazon.com/gamelift/servers/getting-started/#Amazon_GameLift_Server_SDKs") contains SDK packages for each language. You
  can download current or previous versions.
- **New C# server SDK plugin for Unity**
  – The new server SDK package for Unity contains built C#
  libraries that you can install using the package manager in Unity Editor
  (see the new [Unity
  integration guide](integration-engines-unity-using.md "integration-engines-unity-using.md")). These libraries include the required
  dependencies through UnityNuGet. You can use this plugin with Unity
  2020.3 LTS, 2021.3 LTS and 2022.3 LTS for Windows and Mac OS. It
  supports Unity's .NET Framework and .NET Standard profiles, with .NET
  Standard 2.1 and .NET 4.x.
- **Consolidated .NET solution for C#**
  – The server SDK for C# now supports .NET Framework 4.6.2
  (upgraded from 4.6.1) and .NET 6.0 in a single solution. .NET Standard
  2.1 is available with the Unity-built libraries.
- **Server SDK 5.1.0 updates**
  - [C++, C#, Unreal] You can now call `InitSDK()` with
    or without server parameters. Game servers that run on Amazon GameLift Servers
    managed EC2 fleets read the server parameters directly from
    environment variables. Game servers on Amazon GameLift Servers Anywhere fleets
    must call `InitSDK()` with server parameters.
  - [C++, C#, Unreal] Server SDK calls have improved error
    messaging.
  - [C++ SDK] To improve Server SDK build times, the build flag
    `-DRUN_CLANG_FORMAT` is disabled by default. You
    can enable it with `-DRUN_CLANG_FORMAT=1`.
  - [C++ SDK] When building the libraries without the standard
    libraries (`-DGAMELIFT_USE_STD=0`),
    `InitSDK()` no longer uses `std::`
    data types.

- **Expanded server SDK 5.x documentation**
  - Updated server SDK reference guides for C++, C#/Unity, and
    Unreal including expanded coverage of all data types.
    - [C# server SDK 5.x for Amazon GameLift Servers --
      Actions](integration-server-sdk5-csharp-actions.md "integration-server-sdk5-csharp-actions.md")
    - [C++ server SDK 5.x for Amazon GameLift Servers --
      Actions](integration-server-sdk5-cpp-actions.md "integration-server-sdk5-cpp-actions.md")
    - [C++ (Unreal) server SDK 5.x for
      Amazon GameLift Servers -- Actions](integration-server-sdk5-unreal-actions.md "integration-server-sdk5-unreal-actions.md")

  - New versions of the server SDK 5 integration guides for Unity
    and Unreal plugins
    - [Integrate Amazon GameLift Servers into a Unity
      project](integration-engines-unity-using.md "integration-engines-unity-using.md")
    - [Integrate Amazon GameLift Servers into an Unreal Engine
      project](integration-engines-setup-unreal.md "integration-engines-setup-unreal.md")

- **Additional documentation
  updates**

      + Revised documentation for Amazon GameLift Servers service API operations [GetComputeAccess](../apireference/API_GetComputeAccess.md "../apireference/API_GetComputeAccess.md") and [GetInstanceAccess](../apireference/API_GetInstanceAccess.md "../apireference/API_GetInstanceAccess.md") to clarify remote access
       procedures based on the Amazon GameLift Servers server SDK version in use.
      + Revised descriptions for [GameSessionPlacement](../apireference/API_GameSessionPlacement.md "../apireference/API_GameSessionPlacement.md") to document how game session
       information is transient when a placement is in "pending"
       status.

  You can now track hardware performance metrics for your Amazon GameLift Servers managed EC2
  fleets. Metrics include EC2 instance metrics for CPU utilization, network
  traffic volume, and disk read/write activity. For Amazon GameLift Servers, these metrics describe
  all active instances in a fleet location. You can view these fleet hardware metrics
  using an Amazon CloudWatch dashboard in the AWS Management Console. You can also view them in the Amazon GameLift Servers
  console in fleet details.

###### Learn more:

- [Monitor Amazon GameLift Servers with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md") (Metrics for
  fleets), _Amazon GameLift Servers Developer Guide_
  **Updated SDK versions:** AWS SDK
  1.11.111

Amazon GameLift Servers customers can now use the Amazon Linux 2023 operating system to host
their game servers. AL2023 offers several improvements over AL2 including
security. This operating system is available in all AWS Regions with the
exception of the China Regions.

Customers can use the newer Linux operating systems and continue to receive
critical security updates when support ends for Amazon Linux (AL1) in December 2023. Support for Amazon Linux 2 continues through June 30, 2025.

###### Learn more:

- [Amazon GameLift Servers Linux Server FAQ](https://aws.amazon.com/gamelift/servers/faq/al1/ "https://aws.amazon.com/gamelift/servers/faq/al1/")
- [Comparing Amazon Linux 2 and Amazon Linux 2023](../../../linux/al2023/ug/compare-with-al2.md "../../../linux/al2023/ug/compare-with-al2.md")
- Amazon GameLift Servers API Reference links:

      + [AWS SDK
       action `CreateBuild`](../apireference/API_CreateBuild.md "../apireference/API_CreateBuild.md")
      + [CLI command
       `upload-build`](../../../cli/latest/reference/gamelift/upload-build.md "../../../cli/latest/reference/gamelift/upload-build.md")
      + [CLI command
       `create-build`](../../../cli/latest/reference/gamelift/create-build.md "../../../cli/latest/reference/gamelift/create-build.md")

  **Updated SDK versions:** AWS SDK 1.11.87

If you use Amazon GameLift Servers FleetIQ for game hosting, you can now prevent game session
placements on instances that are currently draining. Draining instances are
flagged for shutdown, but they can still be selected to host new game sessions
if no other hosting resources are available. With this new feature, you can
exclude the use of draining instances entirely.

Use this feature when calling `ClaimGameServer` to find available
game servers. Add the new `FilterOption` parameter and set allowed
instance statuses to ACTIVE only. In response, Amazon GameLift Servers FleetIQ looks only at active
instances when searching for and claiming an available game server.

###### **Learn more:**

- [ClaimGameServer](../apireference/API_ClaimGameServer.md "../apireference/API_ClaimGameServer.md") in the _Amazon GameLift Servers API
  Reference_
- [How FleetIQ works](../fleetiqguide/gsg-howitworks.md "../fleetiqguide/gsg-howitworks.md") in the _Amazon GameLift Servers FleetIQ
  Developer Guide_
  Amazon GameLift Servers customers can now use AWS Billing cost allocation tags to organize
  their game hosting costs. You can assign cost allocation tags to individual
  Amazon GameLift Servers EC2 fleet resources to track how your fleets are contributing to the
  overall hosting costs.

###### **Learn more:**

- [Resource cost and utilization tools](gamelift-pricing-cost-optimization.md#gamelift-pricing-cost-optimization-tools "gamelift-pricing-cost-optimization.md#gamelift-pricing-cost-optimization-tools")
- [Using
  AWS cost allocation tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md"), _AWS Billing User Guide_
  **Updated SDK versions:** AWS SDK 1.11.63

Amazon GameLift Servers customers can now use the Windows Server 2016 operating system to host their game servers.
This operating system is available in all AWS Regions. Customers can use the newer Windows
operating system and continue to receive critical security updates as Microsoft ends its support
for Windows Server 2012 in October 2023.

Starting today, new customers who require a Windows runtime environment
must specify Windows Server 2016 when creating new game server builds for
hosting. Existing customers can continue to create new builds and fleets with
Windows Server 2012 but must complete migration with Windows Server 2016 before
the Microsoft end of support date on October 10, 2023.

This update includes the following service changes:

- When creating a game server build using Amazon GameLift Servers SDK or CLI commands, you must now explicitly set
  the operating system. There is no longer a default value. To deploy your
  game server on Windows Server 2016, use the value
  `WINDOWS_2016`.
- When creating a game server build using the Amazon GameLift Servers console, you must select an operating system
  from the available values. If you're an existing customer with active
  Windows Server 2012 fleets, you can choose either
  `WINDOWS_2012` or `WINDOWS_2016`.

###### **Learn more:**

- Amazon GameLift Servers API Reference links:
  - [CLI command
    `upload-build`](../../../cli/latest/reference/gamelift/upload-build.md "../../../cli/latest/reference/gamelift/upload-build.md")
  - [CLI command
    `create-build`](../../../cli/latest/reference/gamelift/create-build.md "../../../cli/latest/reference/gamelift/create-build.md")
  - [AWS SDK
    action `CreateBuild`](../apireference/API_CreateBuild.md "../apireference/API_CreateBuild.md")

- [Amazon GameLift Servers FAQ for Windows 2012](https://aws.amazon.com/gamelift/servers/faq/win2012/ "https://aws.amazon.com/gamelift/servers/faq/win2012/")
  **Updated SDK versions:** Server SDK 5.0.0 for
  Unreal

The latest version of the Amazon GameLift Servers lightweight plugin for Unreal Engine is now
based on the Amazon GameLift Servers server SDK 5.x. To start integrating your Unreal Engine
environment with Amazon GameLift Servers see the following links.

###### **Learn more:**

- [Integrate Amazon GameLift Servers into an Unreal Engine
  project](integration-engines-setup-unreal.md "integration-engines-setup-unreal.md")
- [Add Amazon GameLift Servers to your game server with the server
  SDK](gamelift-sdk-server-api.md "gamelift-sdk-server-api.md")
- [C++ server SDK 5.x for Amazon GameLift Servers --
  Actions](integration-server-sdk5-cpp-actions.md "integration-server-sdk5-cpp-actions.md")
  The new Amazon GameLift Servers console includes these improvements:

- **Improved navigation** – The new
  navigation pane facilitates navigation between Amazon GameLift Servers resources.
- **Amazon GameLift Servers landing page** – The new
  landing page provides links to helpful documentation, displays a
  high-level overview of Amazon GameLift Servers, and provides support through links to
  documentation, frequently asked questions, and AWS re:Post.
- **Improved Amazon CloudWatch metrics** –
  Amazon GameLift Servers metrics are now available in both the Amazon GameLift Servers console and your CloudWatch
  dashboards. This update also includes new metrics for performance,
  utilization, and player sessions.

###### **Learn more:**

- [Manage game hosting resources with Amazon GameLift Servers](gamelift-console-intro.md "gamelift-console-intro.md")
- [Building
  a FlexMatch matchmaker](../flexmatchguide/matchmaker-build.md "../flexmatchguide/matchmaker-build.md")
  **Server Side Encryption ((SSE)) for SNS topics**
  encrypts your sensitive data at rest. SSE uses AWS Key Management Service (AWS KMS) keys to protect
  the contents of your SNS topics.

**Learn more:**

- [Set up event notification for game session
  placement](queue-notification.md "queue-notification.md")
- [FlexMatch
  matchmaking events](../flexmatchguide/match-notification.md "../flexmatchguide/match-notification.md")
- [Encryption at rest](../../../sns/latest/dg/sns-server-side-encryption.md "../../../sns/latest/dg/sns-server-side-encryption.md")
  **Updated SDK versions:** Server SDK 5.0.0 for
  .NET 6. No SDK updates are required.

If you use the Unity Real-Time Development Platform, continue to use the Amazon GameLift Servers
server SDK 5.0.0 with .NET 4.6. Unity doesn't support .NET 6.

###### **Learn more:**

- Download the latest version of the Amazon GameLift Servers server SDK at [Amazon GameLift Servers getting
  started](https://aws.amazon.com/gamelift/getting-started "https://aws.amazon.com/gamelift/getting-started")
- [C# server SDK 5.x for Amazon GameLift Servers --
  Actions](integration-server-sdk5-csharp-actions.md "integration-server-sdk5-csharp-actions.md")
  **Updated SDK versions:** Server SDK 5.0.0 for
  Go

###### **Learn more:**

- Download the latest version of the Amazon GameLift Servers server SDK at [Amazon GameLift Servers getting
  started](https://aws.amazon.com/gamelift/getting-started "https://aws.amazon.com/gamelift/getting-started")
- [Go server SDK for Amazon GameLift Servers --
  Actions](integration-server-sdk-go-actions.md "integration-server-sdk-go-actions.md")
  **Updated SDK versions:** AWS SDK 1.10.21,
  Server SDK 5.0.0 for C++ and C#

**Amazon GameLift Servers Anywhere** uses your game server
resources to host Amazon GameLift Servers game servers. You can use Amazon GameLift Servers Anywhere to integrate
your own compute resources with Amazon GameLift Servers managed EC2 compute to distribute your
game servers across multiple compute types. You can also use Amazon GameLift Servers Anywhere to
iteratively test your game servers without uploading the build to Amazon GameLift Servers for
every iteration.

Highlights:

- New Amazon GameLift Servers Anywhere fleet and compute types
- Amazon GameLift Servers Anywhere compute resource registration
- Improved testing iteration cycle
  **Amazon GameLift Servers Server SDK 5.0.0** introduces
  improvements to the existing server SDK and a new resource type, compute. Server
  SDK 5.0.0 supports Amazon GameLift Servers Anywhere and the use of your own compute resources for
  game server hosting.

###### **Learn more:**

- [Server SDK 5.x for Amazon GameLift Servers](reference-serversdk.md "reference-serversdk.md")
- [Geographic locations](gamelift-compute.md#gamelift-compute-location "gamelift-compute.md#gamelift-compute-location")
- [Choose compute resources for a managed fleet](gamelift-compute.md "gamelift-compute.md")
- [Create an Amazon GameLift Servers Anywhere fleet](fleets-creating-anywhere.md "fleets-creating-anywhere.md")
  **Updated SDK versions:** AWS SDK
  1.9.333

Amazon GameLift Servers is now available in eight Local Zones in the United States, so you can
deploy your fleets closer to players. You can use all managed Amazon GameLift Servers features
with Local Zones by adding the Local Zones to your fleets.

Local Zones extend AWS resources and services to the edge of the cloud, near
large population, industry, and information technology (IT) centers. This means
that you can deploy applications that require single-digit millisecond latency
closer to end users or to on-premises data centers.

###### **Learn more:**

- Amazon GameLift Servers local zones
- [Geographic locations](gamelift-compute.md#gamelift-compute-location "gamelift-compute.md#gamelift-compute-location")
- [Create an Amazon GameLift Servers managed EC2 fleet](fleets-creating.md "fleets-creating.md")
  The new Amazon GameLift Servers console includes these improvements:

- **Improved navigation** – The new
  navigation pane facilitates navigation between Amazon GameLift Servers resources.
- **Amazon GameLift Servers landing page** – The new
  landing page provides links to helpful documentation, displays a
  high-level overview of Amazon GameLift Servers, and provides support through links to
  documentation, frequently asked questions, and AWS re:Post.
- **Improved Amazon CloudWatch metrics** –
  Amazon GameLift Servers metrics are now available in both the Amazon GameLift Servers console and your CloudWatch
  dashboards. This update also includes new metrics for performance,
  utilization, and player sessions.

###### **Learn more:**

- [Manage game hosting resources with Amazon GameLift Servers](gamelift-console-intro.md "gamelift-console-intro.md")
- [Building
  a FlexMatch matchmaker](../flexmatchguide/matchmaker-build.md "../flexmatchguide/matchmaker-build.md")
  FlexMatch users now have access to the following features:

- **Compound rule** – Added support
  for compound matchmaking rules for matches of 40 or fewer players. You
  can now use logical statements to create a compound rule to form a
  match. Without a compound rule in your rule set, to form a match, all
  the rules in the rule set must be true. With compound rules, you can
  choose which rules to apply using the following logical operators:
  `and`, `or`, `not`, and
  `xor`.
- **Flexible team selection** –
  Updated matchmaking property expressions to support selecting a subset
  of all available teams.
- **Longer string lists** –
  Increased the maximum number of strings from 10 to 100 in a list of
  strings of player attribute values.

**Learn more:**

- [Amazon GameLift Servers FlexMatch
  developer guide](../flexmatchguide.md "../flexmatchguide.md"):
  - [FlexMatch rule types](../flexmatchguide/match-rules-reference-ruletype.md "../flexmatchguide/match-rules-reference-ruletype.md")
  - [FlexMatch property expressions](../flexmatchguide/match-rules-reference-property-expression.md "../flexmatchguide/match-rules-reference-property-expression.md")

- [AttributeValue: SL](../apireference/API_AttributeValue.md#gamelift-Type-AttributeValue-SL "../apireference/API_AttributeValue.md#gamelift-Type-AttributeValue-SL")
  **Updated SDK versions:** AWS SDK [1.9.133](https://github.com/aws/aws-sdk-cpp/releases/tag/1.9.133 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.9.133")

Amazon GameLift Servers is now available in the Asia Pacific (Osaka) Region. Game developers can now
deploy instances in Osaka using GameLift multi-Region fleet.

You can now use Graviton2-hosted game servers, based on the Arm-based
processor architecture, to achieve increased performance at a lower cost when
compared to the equivalent Intel-based compute options.

###### Highlights:

- Amazon GameLift Servers is now available in the Asia Pacific (Osaka) Region.
- Amazon GameLift Servers FleetIQ game server groups can now be configured to manage the
  Graviton2 instance families c6g, m6g, and r6g.
  **Learn more:**

- [Amazon GameLift Servers multi-Region fleet](https://aws.amazon.com/blogs/gametech/amazon-gamelift-is-now-easier-to-manage-fleets-across-regions "https://aws.amazon.com/blogs/gametech/amazon-gamelift-is-now-easier-to-manage-fleets-across-regions")
- [CreateGameServerGroup](../../../gamelift/latest/apireference/API_CreateGameServerGroup.md "../../../gamelift/latest/apireference/API_CreateGameServerGroup.md")
- [AWS graviton
  processor](https://aws.amazon.com/ec2/graviton/ "https://aws.amazon.com/ec2/graviton/")
  The Amazon GameLift Servers plugin for Unity version 1.0.0 contains libraries and native UI that makes it easier to
  access Amazon GameLift Servers resources and integrate Amazon GameLift Servers into your Unity game. You can use the
  Amazon GameLift Servers plugin for Unity to access Amazon GameLift Servers APIs and deploy AWS CloudFormation templates for common gaming
  scenarios. The plugin also includes a sample game that works with the sample
  scenarios. You can use Amazon GameLift Servers Local to see messages passed between the game
  client and the game server to learn how a typical game interacts with
  Amazon GameLift Servers.

The plugin for Unity supports Unity 2019.4 LTS and 2020.3 LTS.

Highlights:

- Build, run, and modify a sample game with different scenarios, or
  create your own.
- Deploy sample AWS CloudFormation scenarios for typical game scenarios including
  auth only, single-Region fleet, multi-Region fleets with queue and
  custom matchmaker, Spot Fleets with queue and custom matchmaker, and
  FlexMatch.
  **Learn more:**

- [Integrating games with the
  Amazon GameLift Servers plugin for Unity](../../../gamelift/latest/developerguide/unity-plugin.md "../../../gamelift/latest/developerguide/unity-plugin.md")
  You can use the batchDistance rule type to specify a string or numeric
  attribute, bringing a host of benefits to each segment.

Highlights:

- For large matches (>40 players), instead of evenly balancing players
  by skill only, you can now get that same balance based on skill, modes,
  and maps. Ensure that everyone in the match is in a skill band, band
  multiple numeric attributes such as league or play style, and group
  according to string attributes such as map or game mode. You can also
  create expansions over time. For example, you can create an expansion to
  allow a greater skill level range to enter the match the longer the
  player is waiting.

For matches under 40 players, you can use a new simplified rules
expression.
**Updated SDK versions:** Realtime Client SDK
1.2.0, Server SDK 3.4.0 for Unreal

With this latest SDK update, you can now integrate IL2CPP into your mobile
applications that use the RTS Client SDK and follow best practices with
frameworks. You can also now build the Amazon GameLift Servers Server SDK for Unreal Version
4.26. This update contains components that integrate with your Windows or Linux
game server, including C++ and C# versions of the Amazon GameLift Servers Server SDK, Amazon GameLift Servers
Local, and an Unreal Engine plugin.

Highlights:

- Added support for IL2CPP in the RTS Client SDK and for building the
  native libraries as frameworks, so you can build RTS clients for the
  latest mobile devices.
- You can use [DescribePlayerSessions()](integration-server-sdk-unreal-ref-actions.md#integration-server-sdk-unreal-ref-describeplayersessions "integration-server-sdk-unreal-ref-actions.md#integration-server-sdk-unreal-ref-describeplayersessions") to get information for a single player session, for all player
  sessions in a game session, or for all player sessions associated with a
  single player ID.
- You can use [GetInstanceCertificate()](integration-server-sdk-unreal-ref-actions.md#integration-server-sdk-unreal-ref-getinstancecertificate "integration-server-sdk-unreal-ref-actions.md#integration-server-sdk-unreal-ref-getinstancecertificate") to retrieve the file location of a PEM-encoded TLS certificate that
  is associated with the fleet and its instances.
- Created Server SDK support for Unreal version 4.26.
- The existing C# SDK, version 4.0.2, has been verified compatible with
  Unity 2020.3. No SDK updates were required.
  **Learn more:**

- [Amazon GameLift Servers Developer Guide](../../../gamelift/latest/developerguide.md "../../../gamelift/latest/developerguide.md"):

      + [DescribePlayerSessions()](integration-server-sdk-unreal-ref-actions.md#integration-server-sdk-unreal-ref-describeplayersessions "integration-server-sdk-unreal-ref-actions.md#integration-server-sdk-unreal-ref-describeplayersessions")
      + [GetInstanceCertificate()](integration-server-sdk-unreal-ref-actions.md#integration-server-sdk-unreal-ref-getinstancecertificate "integration-server-sdk-unreal-ref-actions.md#integration-server-sdk-unreal-ref-getinstancecertificate")

  **Updated SDK versions:** AWS SDK [1.8.168](https://github.com/aws/aws-sdk-cpp/releases/tag/1.8.168 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.8.168")

You can now use events to monitor game session placement activity for a game
session queue. Create an Amazon Simple Notification Service (Amazon SNS) topic to publish event notifications,
or set up event tracking using CloudWatch Events.

Highlights:

- For each queue, you can set a custom text string to be included in all
  event messaging.
- When using an Amazon SNS topic, you can set additional access conditions
  that limit publishing to specific queues.
  **Learn more:**

- Amazon GameLift Servers Developer Guide:
  - [Set up event notification for game session
    placement](queue-notification.md "queue-notification.md") (new)
  - [Game session placement events](queue-events.md "queue-events.md")
    (new)

- [API reference (AWS
  SDK)](../../../gamelift/latest/developerguide.md "../../../gamelift/latest/developerguide.md")
  - New game session queue parameters
    `NotificationTarget` and
    `CustomEventData`: [GameSessionQueue](../../../gamelift/latest/apireference/API_GameSessionQueue.md "../../../gamelift/latest/apireference/API_GameSessionQueue.md"), [CreateGameSessionQueue](../../../gamelift/latest/apireference/API_CreateGameSessionQueue.md "../../../gamelift/latest/apireference/API_CreateGameSessionQueue.md"), [UpdateGameSessionQueue](../../../gamelift/latest/apireference/API_UpdateGameSessionQueue.md "../../../gamelift/latest/apireference/API_UpdateGameSessionQueue.md")

- [Amazon GameLift Servers
  forum](https://forums.awsgametech.com/c/amazon-gamelift/7 "https://forums.awsgametech.com/c/amazon-gamelift/7")
  **Updated SDK versions:** AWS SDK [1.8.163](https://github.com/aws/aws-sdk-cpp/releases/tag/1.8.163 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.8.163")

Amazon GameLift Servers managed hosting is now available in 21 AWS Regions. The new Regions
are Cape Town (`af-south-1`), Bahrain (`me-south-1`), Hong
Kong (`ap-east-1`), Milan (`eu-south-1`), Paris
(`eu-west-3`), and Stockholm (`eu-north-1`).

With the new Amazon GameLift Servers multi-location fleets feature, you can now set up a single
fleet to host your game servers in any or all of 20 Amazon GameLift Servers-supported Regions
(Beijing Region excepted). This feature aims to significantly reduce the work
required to set up and maintain Amazon GameLift Servers hosting resources globally. Multi-location
fleets can be created in the following AWS Regions: `us-east-1` (N.
Virginia), `us-west-2` (Oregon), `eu-central-1`
(Frankfurt), `eu-west-1` (Ireland), `ap-southeast-2`
(Sydney), `ap-northeast-1` (Tokyo), and `ap-northeast-2`
(Seoul). In all other Regions, you can continue to set up single-location fleets
as needed. All fleets that were created before this release are single-location
fleets. Using multi-location fleets does not affect your hosting costs. Amazon GameLift Servers
pricing is based on the type, location, and volume of instances that you use.
(For more information, see [Amazon GameLift Servers
pricing](https://aws.amazon.com/gamelift/servers/pricing/ "https://aws.amazon.com/gamelift/servers/pricing/").) AWS CloudFormation support for multi-location fleets will be available
soon.

###### Note

Multi-location fleets are not available in the China Regions. Amazon GameLift Servers
resources that reside in China Regions cannot interact with or be used by
resources in other Amazon GameLift Servers Regions.

Highlights:

- With a multi-location fleet, explicitly add a list of remote
  locations. Amazon GameLift Servers deploys instances of the same type and configuration,
  including the build and runtime configuration, to the fleet's home
  Region and all added locations.
- Adjust capacity settings and scaling for each location independently.
  Auto scaling policies apply to an entire fleet, but you can turn them on
  or off by location.
- Start new game sessions at specific fleet locations. When using game
  session queues or matchmaking to place game sessions, you can now
  prioritize where new game sessions start by location, hosting cost, and
  player latency.
- Get hosting metrics in the Amazon GameLift Servers console, aggregated for all locations
  in a fleet or broken out by each fleet location.
  **Learn more:**

- [Amazon game tech
  blog](https://aws.amazon.com/blogs/gametech/ "https://aws.amazon.com/blogs/gametech/")
- [API reference (AWS
  SDK)](../../../gamelift/latest/developerguide.md "../../../gamelift/latest/developerguide.md")
  - New fleet location operations: [CreateFleetLocations](../../../gamelift/latest/apireference/API_CreateFleetLocations.md "../../../gamelift/latest/apireference/API_CreateFleetLocations.md"), [DescribeFleetLocationAttributes](../../../gamelift/latest/apireference/API_DescribeFleetLocationAttributes.md "../../../gamelift/latest/apireference/API_DescribeFleetLocationAttributes.md"), [DescribeFleetLocationCapacity](../../../gamelift/latest/apireference/API_DescribeFleetLocationCapacity.md "../../../gamelift/latest/apireference/API_DescribeFleetLocationCapacity.md"), [DescribeFleetLocationUtilization](../../../gamelift/latest/apireference/API_DescribeFleetLocationUtilization.md "../../../gamelift/latest/apireference/API_DescribeFleetLocationUtilization.md"), [DeleteFleetLocations](../../../gamelift/latest/apireference/API_DeleteFleetLocations.md "../../../gamelift/latest/apireference/API_DeleteFleetLocations.md")
  - Updated fleet operations, with new multi-location support:
    [CreateFleet](../../../gamelift/latest/apireference/API_CreateFleet.md "../../../gamelift/latest/apireference/API_CreateFleet.md"), [UpdateFleetCapacity](../../../gamelift/latest/apireference/API_UpdateFleetCapacity.md "../../../gamelift/latest/apireference/API_UpdateFleetCapacity.md"), [DescribeEC2InstanceLimits](../../../gamelift/latest/apireference/API_DescribeEC2InstanceLimits.md "../../../gamelift/latest/apireference/API_DescribeEC2InstanceLimits.md"), [DescribeInstances](../../../gamelift/latest/apireference/API_DescribeInstances.md "../../../gamelift/latest/apireference/API_DescribeInstances.md"), [StopFleetActions](../../../gamelift/latest/apireference/API_StopFleetActions.md "../../../gamelift/latest/apireference/API_StopFleetActions.md"), [StartFleetActions](../../../gamelift/latest/apireference/API_StartFleetActions.md "../../../gamelift/latest/apireference/API_StartFleetActions.md")
  - Updated game session placement operations, with new priority
    and filtering capability: [CreateGameSessionQueue](../../../gamelift/latest/apireference/API_CreateGameSessionQueue.md "../../../gamelift/latest/apireference/API_CreateGameSessionQueue.md"), [DescribeGameSessionQueues](../../../gamelift/latest/apireference/API_DescribeGameSessionQueues.md "../../../gamelift/latest/apireference/API_DescribeGameSessionQueues.md"), [UpdateGameSessionQueue](../../../gamelift/latest/apireference/API_UpdateGameSessionQueue.md "../../../gamelift/latest/apireference/API_UpdateGameSessionQueue.md")
  - Updated game session creation operations, with new location
    support: [CreateGameSession](../../../gamelift/latest/apireference/API_CreateGameSession.md "../../../gamelift/latest/apireference/API_CreateGameSession.md"), [DescribeGameSessions](../../../gamelift/latest/apireference/API_DescribeGameSessions.md "../../../gamelift/latest/apireference/API_DescribeGameSessions.md"), [DescribeGameSessionDetails](../../../gamelift/latest/apireference/API_DescribeGameSessionDetails.md "../../../gamelift/latest/apireference/API_DescribeGameSessionDetails.md"), [SearchGameSessions](../../../gamelift/latest/apireference/API_SearchGameSessions.md "../../../gamelift/latest/apireference/API_SearchGameSessions.md")

- [Amazon GameLift Servers Developer Guide](../../../gamelift/latest/developerguide.md "../../../gamelift/latest/developerguide.md"):
  - [Amazon GameLift Servers service locations](gamelift-regions.md "gamelift-regions.md") (updated)
  - [Hosting resource customizations](fleets-design.md "fleets-design.md")
    (new)

  [Scaling game hosting capacity with Amazon GameLift Servers](fleets-manage-capacity.md "fleets-manage-capacity.md") (updated)
  - [Customize a game session queue](queues-design.md "queues-design.md")
    (new)
  - [Fleet details in the Amazon GameLift Servers console](gamelift-console-fleets-metrics.md "gamelift-console-fleets-metrics.md") (updated)

- [Amazon GameLift Servers
  forum](https://forums.awsgametech.com/c/amazon-gamelift/7 "https://forums.awsgametech.com/c/amazon-gamelift/7")
  **Updated SDK versions:** AWS SDK [1.8.139](https://github.com/aws/aws-sdk-cpp/releases/tag/1.8.139 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.8.139")

This release includes the following updates:

- Amazon GameLift Servers FleetIQ game server groups can now be configured to manage the
  AMD instance families C5a, M5a, and R5a. The supported Amazon EC2 instance
  types, as listed for the GameServerGroup [InstanceDefinition](../../../gamelift/latest/apireference/API_InstanceDefinition.md "../../../gamelift/latest/apireference/API_InstanceDefinition.md"), now include the following:

      + c5a.large, c5a.xlarge, c5a.2xlarge, c5a.4xlarge, c5a.8xlarge,
       c5a.12xlarge, c5a.16xlarge, c5a.24xlarge
      + m5a.large, m5a.xlarge, m5a.2xlarge, m5a.4xlarge, m5a.8xlarge,
       m5a.12xlarge, m5a.16xlarge, m5a.24xlarge
      + r5a.large, r5a.xlarge, r5a.2xlarge, r5a.4xlarge, r5a.8xlarge,
       r5a.12xlarge, r5a.16xlarge, r5a.24xlarge

  Note: AMD instances for FleetIQ are currently not available for use in
  the China (Beijing) AWS Region. See [Feature availability and implementation differences](https://docs.amazonaws.cn/en_us/aws/latest/userguide/gamelift.html "https://docs.amazonaws.cn/en_us/aws/latest/userguide/gamelift.html") in
  China.

- Amazon GameLift Servers managed game hosting now supports AMD instances in the China
  (Beijing) Region, operated by Sinnet. The new AMD instance families
  include M5a and R5a. Supported EC2 instance types, as listed for fleet
  [InstanceType](../../../gamelift/latest/apireference/API_FleetAttributes.md "../../../gamelift/latest/apireference/API_FleetAttributes.md"), now include the following:
  - m5a.large, m5a.xlarge, m5a.2xlarge, m5a.4xlarge, m5a.8xlarge,
    m5a.12xlarge, m5a.16xlarge, m5a.24xlarge
  - r5a.large, r5a.xlarge, r5a.2xlarge, r5a.4xlarge, r5a.8xlarge,
    r5a.12xlarge, r5a.16xlarge, r5a.24xlarge

- Amazon GameLift Servers FlexMatch can now be used as a standalone matchmaking solution in
  the China (Beijing) Region, operated by Sinnet. Customers can create a
  FlexMatch matchmaker in the Beijing Region and configure the [FlexMatchMode](../../../gamelift/latest/apireference/API_CreateMatchmakingConfiguration.md#gamelift-CreateMatchmakingConfiguration-request-FlexMatchMode "../../../gamelift/latest/apireference/API_CreateMatchmakingConfiguration.md#gamelift-CreateMatchmakingConfiguration-request-FlexMatchMode") parameter to STANDALONE. For more information
  about FlexMatch, either with Amazon GameLift Servers managed hosting or with a non-Amazon GameLift Servers
  hosting solution, in the [Amazon GameLift Servers FlexMatch Developer Guide](https://docs.amazonaws.cn/en_us/gameliftservers/latest/flexmatchguide/match-intro.html "https://docs.amazonaws.cn/en_us/gameliftservers/latest/flexmatchguide/match-intro.html").
- When setting up event notifications for Amazon GameLift Servers FlexMatch, you can now
  designate an Amazon SNS FIFO topic as the notification target. For more
  information, see:

      + [MatchmakingConfiguration NotificationTarget](../../../gamelift/latest/apireference/API_MatchmakingConfiguration.md "../../../gamelift/latest/apireference/API_MatchmakingConfiguration.md"),
       *Amazon GameLift Servers API Reference*
      + [Set up FlexMatch event notification](../flexmatchguide/match-notification.md "../flexmatchguide/match-notification.md") , *Amazon GameLift Servers FlexMatch Developer Guide*
      + [Introducing Amazon SNS FIFO – First-in-first-out
       Pub/Sub messaging](https://aws.amazon.com/blogs/aws/introducing-amazon-sns-fifo-first-in-first-out-pub-sub-messaging/ "https://aws.amazon.com/blogs/aws/introducing-amazon-sns-fifo-first-in-first-out-pub-sub-messaging/"), *AWS
       News Blog*

  **Updated SDK versions:** Amazon GameLift Servers Server SDK 4.0.2,
  Unreal plugin version 3.3.3

The latest version of the Amazon GameLift Servers Server SDK contains the following
components:

- The updated Unreal plugin has been updated for compatibility with
  Unreal Engine 4.25. The API was not changed.
- The existing C# SDK, version 4.0.2, has been verified compatible with
  Unity 2020. No SDK updates were required.
  Download the latest version of the Amazon GameLift Servers Server SDK at [Amazon GameLift Servers getting
  started](https://aws.amazon.com/gamelift/getting-started "https://aws.amazon.com/gamelift/getting-started").

**Updated SDK versions:** AWS SDK [1.8.95](https://github.com/aws/aws-sdk-cpp/releases/tag/1.8.95 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.8.95")

Amazon GameLift Servers FlexMatch is a customizable matchmaking service for multiplayer games.
Initially designed for users of Amazon GameLift Servers managed hosting, FlexMatch can now be
integrated into games that use other hosting systems, including peer-to-peer,
proprietary on-premises computing, and cloud compute primitive types. Games that
use Amazon GameLift Servers FleetIQ for game hosting on Amazon EC2 can now implement matchmaking with
FlexMatch.

FlexMatch provides a robust matchmaking algorithm and rules language that gives
you wide latitude to customize the matchmaking process so that players are
matched together based on key player characteristics and reported latency. In
addition, FlexMatch offers a matchmaking request workflow that supports features
such as player parties, player acceptance, and match backfill. When you use
FlexMatch with Amazon GameLift Servers managed hosting or Amazon GameLift Servers Realtime, the matchmaker automatically uses
Amazon GameLift Servers to find hosting resources and start a new game session for newly formed
matches. When using FlexMatch as a standalone service, the matchmaker delivers
match results back to your game, which can then start a new game session using
your hosting solution.

API operations for FlexMatch are part of the Amazon GameLift Servers service API, which is included
in the AWS SDK and the AWS Command Line Interface (AWS CLI). This release includes these updates
to support standalone matchmaking:

- The API resource `MatchmakingConfiguration` has the
  following changes:
  - New property, `FlexMatchMode` indicates whether the
    matchmaker is being used with Amazon GameLift Servers managed hosting or as
    standalone matchmaking.
  - Property `GameSessionQueueArns` is not required
    when `FlexMatchMode` is set to standalone.
  - These properties are not used with standalone matchmaking:
    `AdditionalPlayerCount`,
    `BackfillMode`, `GameProperties`,
    `GameSessionData`.

- The automatic backfill feature is not available with standalone
  matchmaking.
  **Updated SDK versions:** AWS SDK [1.8.95](https://github.com/aws/aws-sdk-cpp/releases/tag/1.8.95 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.8.95")

The list of Amazon EC2 instance types supported by Amazon GameLift Servers now includes three new
instance families: C5a, M5a, and R5a. These families consist of AMD
compute-optimized instances that are powered by AMD EPYC processors running at
frequencies up to 3.3. GHz. The AMD instances are x86 compatible; games that are
currently running on Amazon GameLift Servers can be deployed to AMD instance types without
alteration. The new instances are available in the following AWS Regions: US
East (N. Virginia and Ohio), US West (Oregon and N. California), Central Canada
(Montreal), South America (Sao Paulo), EU Central (Frankfurt), EU West (London
and Ireland), Asia Pacific South (Mumbai), Asia Pacific Northeast (Seoul and
Tokyo), and Asia Pacific Southeast (Singapore and Sydney).

The new AMD instances include:

- c5a.large, c5a.xlarge, c5a.2xlarge, c5a.4xlarge, c5a.8xlarge,
  c5a.12xlarge, c5a.16xlarge, c5a.24xlarge
- m5a.large, m5a.xlarge, m5a.2xlarge, m5a.4xlarge, m5a.8xlarge,
  m5a.12xlarge, m5a.16xlarge, m5a.24xlarge
- r5a.large, r5a.xlarge, r5a.2xlarge, r5a.4xlarge, r5a.8xlarge,
  r5a.12xlarge, r5a.16xlarge, r5a.24xlarge
  **Learn more:**

- [Amazon game tech
  blog](https://aws.amazon.com/blogs/gametech/ "https://aws.amazon.com/blogs/gametech/")
- [Amazon GameLift Servers instance
  pricing](https://aws.amazon.com/gamelift/servers/pricing "https://aws.amazon.com/gamelift/servers/pricing")
- [Amazon EC2 instances featuring AMD
  EPYC processors](https://aws.amazon.com/ec2/amd/ "https://aws.amazon.com/ec2/amd/")
- [Amazon GameLift Servers
  forum](https://forums.awsgametech.com/c/amazon-gamelift/7 "https://forums.awsgametech.com/c/amazon-gamelift/7")
  **Updated SDK versions:** Amazon GameLift Servers Server SDK
  4.0.2

The new Server SDK version 4.0.2 fixes a known issue with the API operation
`StartMatchBackfill()`. This operation now returns a correct
response to a match backfill request.

The issue did not affect the match backfill process, and there is no change to
how this feature works. The issue may have impacted log messaging and error
handling for match backfill requests.

Download the latest version of the Amazon GameLift Servers Server SDK at [Amazon GameLift Servers getting
started](https://aws.amazon.com/gamelift/getting-started "https://aws.amazon.com/gamelift/getting-started").

FlexMatch users can now adjust the following default behaviors for the
matchmaking process. These customizations are set in a matchmaking rule set.
There are no changes to the Amazon GameLift Servers SDKs.

- Prioritize backfill tickets: You can choose to raise or lower how
  match backfill tickets are prioritized when searching for acceptable
  matches. Prioritizing backfill tickets is useful when the auto-backfill
  feature is enabled. Use the algorithm property
  `backfillPriority`.
- Pre-sort to optimize match consistency and efficiency: Configure your
  matchmaker to pre-sort the ticket pool before batching tickets for
  evaluation. By pre-sorting tickets based on key player attributes, your
  resulting matches tend to have players who are more similar in those
  attributes. You can also boost efficiency in the evaluation process by
  pre-sorting on the same attributes that are used in match rules. Use the
  algorithm property `sortByAttributes` with the
  `strategy` property set to "sorted".
- Adjust how expansion wait times are triggered: Choose between
  triggering expansions based on the age of the newest (default) or oldest
  ticket in an incomplete match. Triggering on the oldest ticket tends to
  complete matches faster, while triggering on the newest ticket leads to
  higher match quality. Use the algorithm property
  `expansionAgeSelection`.
  **Updated SDK versions:** Amazon GameLift Servers Server SDK
  4.0.1

The new Server SDK contains the following updates:

- C# API version 4.0.1
  - The API operation [TerminateGameSession()](integration-server-sdk-csharp-ref-actions.md#integration-server-sdk-csharp-ref-terminategamesession "integration-server-sdk-csharp-ref-actions.md#integration-server-sdk-csharp-ref-terminategamesession") is no longer supported. Replace with a call to [ProcessEnding()](integration-server-sdk-csharp-ref-actions.md#integration-server-sdk-csharp-ref-processending "integration-server-sdk-csharp-ref-actions.md#integration-server-sdk-csharp-ref-processending") to end both a game session and the server process.
  - A known issue with the operation [GetInstanceCertificate()](integration-server-sdk-csharp-ref-actions.md#integration-server-sdk-csharp-ref-getinstancecertificate "integration-server-sdk-csharp-ref-actions.md#integration-server-sdk-csharp-ref-getinstancecertificate") is fixed.
  - The operation [GetTerminationTime()](integration-server-sdk-csharp-ref-actions.md#integration-server-sdk-csharp-ref-getterm "integration-server-sdk-csharp-ref-actions.md#integration-server-sdk-csharp-ref-getterm")
    now returns a value of data type AwsDateTimeOutcome.

- C++ API version 3.4.1
  - The operation [TerminateGameSession()](integration-server-sdk-cpp-ref-actions.md#integration-server-sdk-cpp-ref-terminategamesession "integration-server-sdk-cpp-ref-actions.md#integration-server-sdk-cpp-ref-terminategamesession") is no longer supported. Replace it with a call to [ProcessEnding()](integration-server-sdk-cpp-ref-actions.md#integration-server-sdk-cpp-ref-processending "integration-server-sdk-cpp-ref-actions.md#integration-server-sdk-cpp-ref-processending") to end both a game session and the server process.

- Unreal Engine plugin version 3.3.2

      + The operation [TerminateGameSession()](integration-server-sdk-unreal-ref-actions.md#integration-server-sdk-unreal-ref-terminategamesession "integration-server-sdk-unreal-ref-actions.md#integration-server-sdk-unreal-ref-terminategamesession") is no longer supported. Replace it with a call to [ProcessEnding()](integration-server-sdk-unreal-ref-actions.md#integration-server-sdk-unreal-ref-processending "integration-server-sdk-unreal-ref-actions.md#integration-server-sdk-unreal-ref-processending") to end both a game session and the server process.
      + The callback operation `OnUpdateGameSession` is
       added to [FProcessParameters](integration-server-sdk-unreal-ref-datatypes.md#integration-server-sdk-unreal-ref-dataypes-process "integration-server-sdk-unreal-ref-datatypes.md#integration-server-sdk-unreal-ref-dataypes-process") to support match backfill.

  Download the latest version of the Amazon GameLift Servers Server SDK at [Amazon GameLift Servers getting
  started](https://aws.amazon.com/gamelift/getting-started "https://aws.amazon.com/gamelift/getting-started").

**Updated SDK versions:** AWS SDK [1.8.36](https://github.com/aws/aws-sdk-cpp/releases/tag/1.8.36 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.8.36")

The Amazon GameLift Servers FleetIQ solution for low-cost, cloud-based game hosting on Amazon EC2 is
now generally available. Amazon GameLift Servers FleetIQ gives developers the ability to host game
servers directly on Amazon EC2 Spot Instances by optimizing their viability for game
hosting. Game developers can use Amazon GameLift Servers FleetIQ with new games or to supplement
capacity for existing games. This solution supports the use of containers or
other AWS services such as AWS Shield and Amazon Elastic Container Service (Amazon ECS).

This general availability release includes the following updates to the Amazon GameLift Servers
FleetIQ solution:

- New API operation `DescribeGameServerInstances` returns
  information, including status, on all active instances for a Amazon GameLift Servers FleetIQ
  game server group.
- New balancing strategy, `ON_DEMAND_ONLY`, configures a game
  server group to use On-Demand Instances only. You can update a game
  server group's balancing strategy at any time, making it possible to
  switch between using Spot Instances and On-Demand Instances as
  needed.
- The following preview elements have been dropped for general
  availability:

      + Use of custom sort keys for game server resources. Game
       servers can be sorted based on registration timestamp.
      + Tagging for game server resources.

  **Updated SDK versions:** Amazon GameLift Servers Server SDK 4.0.0,
  Amazon GameLift Servers Local 1.0.5

The latest version of the Amazon GameLift Servers Server SDK contains the following updated
components:

- C# SDK version 4.0.0 updated for Unity 2019.
- Unreal plugin version 3.3.1 updated for Unreal Engine versions 4.22,
  4.23, and 4.24.
- Amazon GameLift Servers Local version 1.0.5 updated to test integrations that use the C#
  server SDK version 4.0.0.
  Download the latest version of the Amazon GameLift Servers Server SDK at [Amazon GameLift Servers getting
  started](https://aws.amazon.com/gamelift/getting-started "https://aws.amazon.com/gamelift/getting-started").

**Updated SDK versions:** AWS SDK [1.7.310](https://github.com/aws/aws-sdk-cpp/releases/tag/1.7.310 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.7.310")

The Amazon GameLift Servers FleetIQ feature optimizes the viability of low-cost Spot Instances for
use with game hosting. This feature is now extended for customers who want to
manage their hosting resources directly rather than through the managed Amazon GameLift Servers
service. This solution supports the use of containers or other AWS services
such as AWS Shield and Amazon Elastic Container Service (Amazon ECS).

**Learn more:**

[GameTech blog post](https://aws.amazon.com/blogs/gametech/gamelift-in-2020-major-update-now-available-in-preview/ "https://aws.amazon.com/blogs/gametech/gamelift-in-2020-major-update-now-available-in-preview/") on Amazon GameLift Servers FleetIQ

**Updated SDK versions:** AWS SDK [1.7.249](https://github.com/aws/aws-sdk-cpp/releases/tag/1.7.249 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.7.249")

You can now take advantage of AWS resource management tools with Amazon GameLift Servers
resources. In particular, all key Amazon GameLift Servers resources—builds, scripts,
fleets, game session queues, matchmaking configurations, and matchmaking rule
sets—are now assigned Amazon Resource Name (ARN) values. A resource ARN
provides a consistent identifier that is unique across all AWS Regions. They
can be used to create resource-specific AWS Identity and Access Management (IAM) permissions policies.
Resources are now assigned an ARN and also the pre-existing resource identifier,
which is not Region-specific.

In addition, Amazon GameLift Servers resources now support tagging. You can use tags to organize
resources, create IAM permissions policies to manage access to groups of
resources, customize AWS cost breakdowns, etc. When managing tags for Amazon GameLift Servers
resources, use the Amazon GameLift Servers API actions `TagResource()`,
`UntagResource()`, and `ListTagsForResource()`.

**Learn more:**

- [TagResource](../../../gamelift/latest/apireference/API_TagResource.md "../../../gamelift/latest/apireference/API_TagResource.md") in
  the _Amazon GameLift Servers API Reference_
- [Tagging AWS
  resources](../../../general/latest/gr/aws_tagging.md "../../../general/latest/gr/aws_tagging.md") in the _AWS General
  Reference_
- [Amazon
  resource names](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md") in the _AWS General
  Reference_
  **Updated SDK versions:** AWS SDK [1.7.210](https://github.com/aws/aws-sdk-cpp/releases/tag/1.7.210 "https://github.com/aws/aws-sdk-cpp/releases/tag/1.7.210")

AWS CloudFormation templates for Amazon GameLift Servers

Amazon GameLift Servers resources can now be created and managed through AWS CloudFormation. The existing
AWS CloudFormation build and fleet templates have been updated to align with the current
resources, and new templates are now available for scripts, queues, matchmaking
configurations, and matchmaking rule sets. AWS CloudFormation templates greatly simplify the
task of managing groups of related AWS resources, particularly when deploying
games across multiple Regions.

**Learn more:**

- [Amazon GameLift Servers resource type
  reference](../../../AWSCloudFormation/latest/UserGuide/AWS_GameLift.md "../../../AWSCloudFormation/latest/UserGuide/AWS_GameLift.md") in the _AWS CloudFormation User Guide_
- [Manage Amazon GameLift Servers hosting resources using AWS CloudFormation](resources-cloudformation.md "resources-cloudformation.md") in the _Amazon GameLift Servers Developer Guide_
