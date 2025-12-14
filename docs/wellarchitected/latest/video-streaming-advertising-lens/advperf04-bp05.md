# ADVPERF04-BP05 Manage high volume user profile

data

The user profile database is typically large, ranging from
100-200 million to 5 billion user profiles and contains a wide
range of data about users' online activities and interactions.
Hence this should be retained for a short time in the range of
30 days -1-year max, to manage data storage costs and data query
latency SLO’s.

## Implementation guidance

Use an in-memory database with a data cache strategy using
Amazon MemoryDB.

Avoid replicating user profile data across multiple Regions due
to high latency and data transfer costs. We recommend storing user profiles
local to the user.

In the event of multi-Region architecture, implement
synchronization between periodically (for example, once or twice a day)
rather than in real-time, as users are unlikely to be in two
locations at once. Advertisers also often use geotargeting, so a
user's profile may only be accessed from the Region the user is
located in for a particular ad campaign.

## Key AWS services

- Amazon MemoryDB

## Resources

- [Observability best practices for Amazon Memory DB for Valke](https://aws.amazon.com/blogs/database/monitor-server-side-latency-for-amazon-memorydb-for-valkey/ "https://aws.amazon.com/blogs/database/monitor-server-side-latency-for-amazon-memorydb-for-valkey/")y
