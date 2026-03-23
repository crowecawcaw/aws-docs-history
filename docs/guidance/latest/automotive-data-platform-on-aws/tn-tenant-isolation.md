# Tenant Isolation

Three Amazon Cognito user pool groups control access across all consumption layers:

| Role           | Data Scope   | Capabilities                                                                 |
| -------------- | ------------ | ---------------------------------------------------------------------------- |
| Platform Admin | All fleets   | Full system access, OEM connector management, user management                |
| Fleet Operator | Own fleet(s) | View vehicles, trips, telemetry; subscribe to real-time feed; manage drivers |
| Fleet Viewer   | Own fleet(s) | Read-only dashboard access                                                   |

The Fleet Management API Lambda extracts `cognito:groups` and `custom:fleetIds` from the JWT and filters every query. Lake Formation enforces the same boundaries on Athena queries. WebSocket connections are scoped by fleet at connect time.
