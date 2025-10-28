# Resource-level throttling

Some API operations are subject to resource-level throttling to prevent database hot key issues. While increasing API-level limits for these operations, they may still be throttled at the resource level.

The following API operations are subject to resource-level throttling:

- DescribeGameSessionPlacement
- DescribeGameSessions
- DescribeMatchmaking
- DescribePlayerSessions
  Resource-level throttling is enforced using specific throttle keys that include resource identifiers. For example, DescribeGameSessionPlacement uses the key "Operation:GameLift/DescribeGameSessionPlacement,aws-account-placement-id:" which enforces throttling per account and placement ID combination. This prevents customers from overwhelming the system with requests for specific resources.
