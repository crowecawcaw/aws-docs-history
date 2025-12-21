# X-Ray SDK and Daemon Support timeline

The following table lists the dates and the level of support for X-Ray SDKs and Daemon.

| SDK and daemon phase | Start date          | End date            | Support provided                                                                                                                         |
| -------------------- | ------------------- | ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| General availability | NA                  | February 25th, 2026 | X-Ray SDKs and Daemon are fully supported. AWS provides regular SDK and daemon releases that include bug and security fixes.             |
| Maintenance mode     | February 25th, 2026 | N/A                 | AWS will limit X-Ray SDK and Daemon releases to address security issues only. The SDKs/Daemon will not receive new feature enhancements. |

We recommend that you migrate to OpenTelemetry solutions for instrumenting your application and sending traces to AWS X-Ray. For more information on migrating to OpenTelemetry, see [Migrating from X-Ray instrumentation to OpenTelemetry instrumentation](xray-sdk-migration.md "xray-sdk-migration.md") .
