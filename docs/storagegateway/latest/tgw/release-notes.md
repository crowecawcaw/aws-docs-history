# Release notes for Tape Gateway appliance

software

These release notes describe the new and updated features, improvements, and fixes that are
included with each version of the Tape Gateway appliance. Each software version is identified by its
release date and a unique version number.

You can determine a gateway's software version number by checking its
**Details** page in the Storage Gateway console, or by calling the [DescribeGatewayInformation](../APIReference/API_DescribeGatewayInformation.md "../APIReference/API_DescribeGatewayInformation.md") API action using an AWS CLI command similar to the
following:

```
aws storagegateway describe-gateway-information --gateway-arn "`arn:aws:storagegateway:us-west-2:123456789012:gateway/sgw-12A3456B`"
```

The version number is returned in the `SoftwareVersion` field of the API
response.

###### Note

A gateway won't report software version information under the following
circumstances:

- The gateway is offline.
- The gateway is running older software that doesn't support version reporting.
- The gateway type is FSx File Gateway.
  For more information about Tape Gateway updates, including how to modify the default automatic
  maintenance and update schedule for a gateway, see [Managing Gateway Updates
  Using the AWS Storage Gateway Console](MaintenanceManagingUpdate-common.md "MaintenanceManagingUpdate-common.md").

###### Amazon Linux 2023 (AL2023) based gateways

The following table lists the release notes for gateways based on AL2023.

###### Note

Gateway versions 2.x.x can't be updated to 3.x.x.

| Release Date | Software Version | Release Notes                                                                                                                                                                                                                     |
| ------------ | ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2025-11-06   | 3.0.5            | • Updated operating system and software elements to improve security and performance for new and existing gateways                                                                                                                |
| 2025-10-10   | 3.0.4            | • Updated operating system and software elements to improve security and performance for new and existing gateways                                                                                                                |
| 2025-09-12   | 3.0.3            | • Updated operating system and software elements to improve security and performance for new and existing gateways                                                                                                                |
| 2025-08-29   | 3.0.2            | • Updated operating system and software elements to improve security and performance for new and existing gateways<br>• Addressed issues with static IP configuration                                                             |
| 2025-08-18   | 3.0.1            | • Updated operating system and software elements to improve security and performance for new and existing gateways<br>• Added CloudWatch Logs event to help administrators monitor when virtual tapes enter `IRRECOVERABLE` state |
| 2025-07-16   | 3.0.0            | • Initial release of new operating system<br>• Added IPv6 support                                                                                                                                                                 |

###### Amazon Linux 2 (AL2) based gateways

The following table lists the release notes for gateways based on AL2.

| Release Date | Software Version | Release Notes                                                                                                                                                                                                                        |
| ------------ | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 2025-11-03   | 2.12.15          | • Updated operating system and software elements to improve security and performance for<br>new and existing gateways                                                                                                                |
| 2025-10-01   | 2.12.14          | • Updated operating system and software elements to improve security and performance for<br>new and existing gateways                                                                                                                |
| 2025-09-02   | 2.12.13          | • Updated operating system and software elements to improve security and performance for<br>new and existing gateways<br>• Added CloudWatch Logs event to help administrators monitor when virtual tapes enter `IRRECOVERABLE` state |
| 2025-07-31   | 2.12.12          | • Updated operating system and software elements to improve security and performance for<br>new and existing gateways                                                                                                                |
| 2025-07-01   | 2.12.11          | • Updated operating system and software elements to improve security and performance for<br>new and existing gateways                                                                                                                |
| 2025-06-02   | 2.12.10          | • Updated operating system and software elements to improve security and performance for<br>new and existing gateways                                                                                                                |
| 2025-05-01   | 2.12.9           | • Updated operating system and software elements to improve security and performance for<br>new and existing gateways                                                                                                                |
| 2025-05-01   | 2.12.8           | • Updated operating system and software elements to improve security and performance for<br>new and existing gateways                                                                                                                |
| 2025-04-01   | 2.12.7           | • Updated operating system and software elements to improve security and performance for<br>new and existing gateways                                                                                                                |
| 2025-03-04   | 2.12.6           | • Updated operating system and software elements to improve security and performance for<br>new and existing gateways                                                                                                                |
| 2025-02-04   | 2.12.5           | • Updated operating system and software elements to improve security and performance for<br>new and existing gateways<br>• Addressed an issue where gateways could get stuck in shutdown state after a software<br>update            |
| 2025-01-07   | 2.12.3           | • Updated operating system and software elements to improve security and performance for<br>new and existing gateways                                                                                                                |
| 2024-12-06   | 2.12.2           | • Updated operating system and software elements to improve security and performance for<br>new and existing gateways                                                                                                                |
| 2024-11-06   | 2.12.1           | • Updated operating system and software elements to improve security and performance for<br>new and existing gateways                                                                                                                |
| 2024-10-03   | 2.12.0           | • Updated operating system and software elements to improve security and performance for<br>new and existing gateways                                                                                                                |
| 2024-08-30   | 2.11.0           | • Updated operating system and software elements to improve security and performance for<br>new and existing gateways                                                                                                                |
| 2024-07-29   | 2.10.0           | • Updated operating system and software elements to improve security and performance for<br>new and existing gateways<br>• Miscellaneous bug fixes and enhancements                                                                  |
| 2024-06-17   | 2.9.2            | • Updated operating system and software elements to improve security and performance for<br>new and existing gateways                                                                                                                |
| 2024-05-28   | 2.9.0            | • Reduced gateway restart time during software updates<br>• Reduced the amount of data transferred for estimating network bandwidth                                                                                                  |
| 2024-05-08   | 2.8.3            | • Addressed cloud connectivity issue when using SOCKS5 proxy<br>• Addressed upload performance degradation issue under certain conditions (such as a<br>high number of tape erasure operations)                                      |
| 2024-04-10   | 2.8.1            | • Addressed a memory usage issue introduced in 2.8.0<br>• Security patch updates<br>• Improved software update process<br>• Addressed missing Network Time Protocol (NTP) component for new gateways                                 |
| 2024-03-06   | 2.8.0            | • Updated operating system and software elements to improve security and performance for<br>new gateways<br>• Security patch updates<br>• Improved performance for concurrent Backup and Restore workloads                           |
| 2023-12-19   | 2.7.0            | • Updated operating system and software elements to improve security and performance for<br>new gateways                                                                                                                             |
| 2023-12-14   | 2.6.6            | • Fixed an issue with relative positioning on larger than 5 TiB tapes                                                                                                                                                                |
| 2023-10-19   | 2.6.5            | • Added safeguards against tape overwrites by clients after a gateway restart                                                                                                                                                        |
