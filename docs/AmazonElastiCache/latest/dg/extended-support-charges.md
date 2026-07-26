# ElastiCache Extended Support charges

You will incur charges for all engines enrolled in ElastiCache Extended Support beginning the day after the end of standard support. For the ElastiCache end of standard support date, see [Versions with ElastiCache Extended Support](extended-support-versions.md "extended-support-versions.md").

The additional charge for ElastiCache Extended Support automatically stops when you take one of the following actions:

- Upgrade to an engine version that's covered under standard support.
- Delete the cache that's running a major version past the ElastiCache end of standard support date.
  The charges will restart if your target engine version enters Extended Support in the future.

For example, let’s say ElastiCache version 4 for Redis OSS enters Extended Support on February 1, 2026, and you upgrade your caches on v4 to v6 on January 1, 2027. You will only be charged for 11 months of Extended Support, on ElastiCache version 4 for Redis OSS. If you continue running ElastiCache version 6 for Redis OSS past its end of standard support date of January 31, 2027, then those caches will again incur Extended Support charges starting on February 1, 2027.

You can avoid being charged for ElastiCache Extended Support by preventing ElastiCache from creating or restoring a cache past the ElastiCache end of standard support date.

## Extended Support charges and reserved nodes

ElastiCache reserved nodes or instances (RIs) pricing does not discount ElastiCache Extended Support charges. If you have a reserved node or instance, you are billed for:

- The standard ElastiCache node price with the RI discount applied.
- The ElastiCache Extended Support charge, calculated as a percentage of the standard on-demand node price. The RI discount does not apply to Extended Support charges.

For example, if you are running a cache.m5.large node on ElastiCache version 5 for Redis OSS in the US East (Ohio) Region, the on-demand price is $0.156/hr and the Extended Support premium for Year 1 is 80%. If your RI effective rate is $0.106/hr, you pay the RI-discounted rate of $0.106/hr plus the Extended Support charge of $0.1248/hr (80% of the $0.156/hr on-demand price), for a total of $0.2308/hr per node.

For more information, see [Amazon ElastiCache pricing](https://aws.amazon.com/elasticache/pricing/#Extended_support "https://aws.amazon.com/elasticache/pricing/#Extended_support").
