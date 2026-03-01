# Managing ElastiCache cluster maintenance

Every cluster has a weekly maintenance window during which any system changes are
applied. With Valkey and Redis OSS, replication groups have this same weekly maintenance window.
If you don't specify a preferred maintenance window when you create or modify a
cluster or replication group, ElastiCache assigns a 60-minute maintenance window within your region's maintenance window
on a randomly chosen day of the week.

The 60-minute maintenance window is chosen at random from an 8-hour block of time
per region. The following table lists the time blocks for each region from which the
default maintenance windows are assigned.
You may choose a preferred maintenance window outside the region's maintenance window block.

| Region Code      | Region Name                      | Region Maintenance Window |
| ---------------- | -------------------------------- | ------------------------- |
| `af-south-1`     | Africa (Cape Town) Region        | 13:00–21:00 UTC           |
| `ap-east-1`      | Asia Pacific (Hong Kong) Region  | 13:00–21:00 UTC           |
| `ap-east-2`      | Asia Pacific (Taipei) Region     | 09:00–17:00 UTC           |
| `ap-northeast-1` | Asia Pacific (Tokyo) Region      | 13:00–21:00 UTC           |
| `ap-northeast-2` | Asia Pacific (Seoul) Region      | 12:00–20:00 UTC           |
| `ap-northeast-3` | Asia Pacific (Osaka) Region      | 12:00–20:00 UTC           |
| `ap-south-1`     | Asia Pacific (Mumbai) Region     | 17:30–1:30 UTC            |
| `ap-south-2`     | Asia Pacific (Hyderabad) Region  | 06:30–14:30 UTC           |
| `ap-southeast-1` | Asia Pacific (Singapore) Region  | 14:00–22:00 UTC           |
| `ap-southeast-2` | Asia Pacific (Sydney) Region     | 12:00–20:00 UTC           |
| `ap-southeast-3` | Asia Pacific (Jakarta) Region    | 14:00–22:00 UTC           |
| `ap-southeast-4` | Asia Pacific (Melbourne) Region  | 11:00–19:00 UTC           |
| `ap-southeast-5` | Asia Pacific (Malaysia) Region   | 09:00–17:00 UTC           |
| `ap-southeast-7` | Asia Pacific (Thailand) Region   | 08:00–16:00 UTC           |
| `ca-central-1`   | Canada (Central) Region          | 03:00–11:00 UTC           |
| `ca-west-1`      | Canada West (Calgary) Region     | 18:00–02:00 UTC           |
| `cn-north-1`     | China (Beijing) Region           | 14:00–22:00 UTC           |
| `cn-northwest-1` | China (Ningxia) Region           | 14:00–22:00 UTC           |
| `eu-central-1`   | Europe (Frankfurt) Region        | 23:00–07:00 UTC           |
| `eu-central-2`   | Europe (Zurich) Region           | 02:00–10:00 UTC           |
| `eu-north-1`     | Europe (Stockholm) Region        | 23:00–07:00 UTC           |
| `eu-south-1`     | Europe (Milan) Region            | 21:00–05:00 UTC           |
| `eu-south-2`     | Europe (Spain) Region            | 02:00–10:00 UTC           |
| `eu-west-1`      | Europe (Ireland) Region          | 22:00–06:00 UTC           |
| `eu-west-2`      | Europe (London) Region           | 23:00–07:00 UTC           |
| `eu-west-3`      | EU (Paris) Region                | 23:59–07:29 UTC           |
| `il-central-1`   | Israel (Tel Aviv) Region         | 03:00–11:00 UTC           |
| `me-central-1`   | Middle East (UAE) Region         | 13:00–21:00 UTC           |
| `me-south-1`     | Middle East (Bahrain) Region     | 13:00–21:00 UTC           |
| `mx-central-1`   | Mexico (Central) Region          | 19:00–03:00 UTC           |
| `sa-east-1`      | South America (São Paulo) Region | 01:00–09:00 UTC           |
| `us-east-1`      | US East (N. Virginia) Region     | 03:00–11:00 UTC           |
| `us-east-2`      | US East (Ohio) Region            | 04:00–12:00 UTC           |
| `us-gov-east-1`  | AWS GovCloud (US-East)           | 17:00–01:00 UTC           |
| `us-gov-west-1`  | AWS GovCloud (US) region         | 06:00–14:00 UTC           |
| `us-west-1`      | US West (N. California) Region   | 06:00–14:00 UTC           |
| `us-west-2`      | US West (Oregon) Region          | 06:00–14:00 UTC           |

###### Changing your cluster's or replication group's maintenance window

The maintenance window should fall at the time of lowest usage and thus might need
modification from time to time. You can modify your cluster or replication group
to specify a time range of up to 24 hours in duration during which any maintenance
activities you have requested should occur. Any deferred or pending cluster modifications
you requested occur during this time.

###### Note

If you want to apply node type modifications and/or engine upgrades immediately using the AWS Management Console select the **Apply now** box. Otherwise these modifications will be applied during your next scheduled maintenance window.
To the use the API, see [modify-replication-group](../../../cli/latest/reference/elasticache/modify-replication-group.md "../../../cli/latest/reference/elasticache/modify-replication-group.md") or
[modify-cache-cluster](../../../cli/latest/reference/elasticache/modify-cache-cluster.md "../../../cli/latest/reference/elasticache/modify-cache-cluster.md").

###### More information

For information on your maintenance window and node replacement, see the following:

- [ElastiCache Maintenance](https://aws.amazon.com/elasticache/elasticache-maintenance/ "https://aws.amazon.com/elasticache/elasticache-maintenance/")—FAQ on maintenance and node replacement
- [Replacing nodes (Memcached)](CacheNodes.md "CacheNodes.md")—Managing node replacement for Memcached
- [Modifying an ElastiCache cluster](Clusters.md "Clusters.md")—Changing a cluster's maintenance window
- [Replacing nodes (Valkey and Redis OSS)](CacheNodes.md "CacheNodes.md")—Managing node replacement
- [Modifying a replication group](Replication.md "Replication.md")—Changing a replication group's maintenance window
