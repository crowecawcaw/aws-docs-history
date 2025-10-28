# ElastiCache Extended Support charges

You will incur charges for all engines enrolled in ElastiCache Extended Support beginning the day after the end of standard support. For the ElastiCache end of standard support date, see [Versions with ElastiCache Extended Support](extended-support-versions.md "extended-support-versions.md").

The additional charge for ElastiCache Extended Support automatically stops when you take one of the following actions:

- Upgrade to an engine version that's covered under standard support.
- Delete the cache that's running a major version past the ElastiCache end of standard support date.
  The charges will restart if your target engine version enters Extended Support in the future.

For example, let’s say ElastiCache version 4 for Redis OSS enters Extended Support on February 1, 2026, and you upgrade your caches on v4 to v6 on January 1, 2027. You will only be charged for 11 months of Extended Support, on ElastiCache version 4 for Redis OSS. If you continue running ElastiCache version 6 for Redis OSS past its end of standard support date of January 31, 2027, then those caches will again incur Extended Support charges starting on February 1, 2027.

You can avoid being charged for ElastiCacheExtended Support by preventing ElastiCache from creating or restoring a cache past the ElastiCache end of standard support date.

For more information, see [Amazon ElastiCache pricing](https://aws.amazon.com/elasticache/pricing/ "https://aws.amazon.com/elasticache/pricing/").
