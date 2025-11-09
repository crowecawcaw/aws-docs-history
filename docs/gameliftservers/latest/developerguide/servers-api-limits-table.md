# Amazon GameLift Servers SDK API limits

The following table lists the default rate limits for Amazon GameLift Servers SDK API operations. These limits optimize performance and prevent resource contention in game server environments. Understanding these limits is important for efficient server-side integration with Amazon GameLift Servers.

Server SDK limits are enforced using specific throttling keys that include account and process identifiers. Some limits are per-player to prevent abuse from individual players.

###### Note

This table is subject to change. The authoritative source for current limits is the internal SDC configuration. Contact AWS Support for the most up-to-date information if needed.

| Server SDK API limits reference   | API action | Burst limit | Rate limit                               | Throttling key                                                                              | Notes |
| --------------------------------- | ---------- | ----------- | ---------------------------------------- | ------------------------------------------------------------------------------------------- | ----- |
| AcceptPlayerSession               | 3          | 1           | aws-account-and-process-id-and-player-id | Limit is per player and per process. Should never need a limit increase as it's per-player. |
| RemovePlayerSession               | 3          | 1           | aws-account-and-process-id-and-player-id | Limit is per player and per process. Should never need a limit increase as it's per-player. |
| ActivateGameSession               | 3          | 1           | aws-account-and-process-id               | Limit is per server process. Should never need a limit increase as it's per-process.        |
| ActivateHostProcessV2             | 3          | 1           | aws-account-and-process-id               | Limit is per server process. Should never need a limit increase as it's per-process.        |
| StartMatchBackfill                | 3          | 1           | aws-account-and-process-id               | Limit is per server process. Should never need a limit increase as it's per-process.        |
| DescribePlayerSessions            | 10         | 5           | aws-account-and-process-id               | Limit is per server process. Should never need a limit increase as it's per-process.        |
| GetComputeCertificate             | 3          | 0.1         | aws-account-and-process-id               | Limit is per server process. Should never need a limit increase as it's per-process.        |
| GetCustomerRoleCredentials        | 3          | 0.1         | aws-account-and-process-id               | Limit is per server process. Should never need a limit increase as it's per-process.        |
| InitSDK                           | 3          | 0.1         | aws-account-and-process-id               | Limit is per server process. Should never need a limit increase as it's per-process.        |
| RefreshHostProcess                | 3          | 0.1         | aws-account-and-process-id               | Limit is per server process. Should never need a limit increase as it's per-process.        |
| StopMatchmaking                   | 3          | 1           | aws-account-and-process-id               | Limit is per server process. Should never need a limit increase as it's per-process.        |
| ProcessEnding                     | 3          | 1           | aws-account-and-process-id               | Limit is per server process. Should never need a limit increase as it's per-process.        |
| ProcessReady                      | 3          | 1           | aws-account-and-process-id               | Limit is per server process. Should never need a limit increase as it's per-process.        |
| UpdateGameSession                 | 3          | 1           | aws-account-and-process-id               | Limit is per server process. Should never need a limit increase as it's per-process.        |
| UpdateHostProcess                 | 3          | 1           | aws-account-and-process-id               | Limit is per server process. Should never need a limit increase as it's per-process.        |
| GetGameSessionId                  | 10         | 5           | aws-account-and-process-id               | Limit is per server process. Should never need a limit increase as it's per-process.        |
| GetTerminationTime                | 3          | 1           | aws-account-and-process-id               | Limit is per server process. Should never need a limit increase as it's per-process.        |
| UpdatePlayerSessionCreationPolicy | 3          | 1           | aws-account-and-process-id               | Limit is per server process. Should never need a limit increase as it's per-process.        |

###### Note

These are the default limits. If you're experiencing throttling on these APIs, it may be due to account-level throttling. To request a limit increase, contact AWS Support.

Per-process and per-player limits are designed to accommodate normal usage patterns and should rarely need adjustment. If you're experiencing throttling with these APIs, review your implementation for potential optimization opportunities before requesting limit increases.

Account-level throttling may also apply through these additional rules:

- SdkWebSocket/AccountLevelHighUsage,aws-account
- SdkWebSocket/AccountLevelThrottle,aws-account
