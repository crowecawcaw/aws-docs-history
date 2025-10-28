# ElastiCache Extended Support

With ElastiCache Extended Support, you can continue running your cache on a major engine version past the end of standard support date for an additional cost. If you don't upgrade after the end of standard support date, you will be charged.

Extended Support provides the following updates and technical support:

- Security updates for critical and high CVEs for your cache and cache engine
- Bug fixes and patches for critical issues
- The ability to open support cases and receive troubleshooting help within the standard ElastiCache service level agreement
  This paid offering gives you more time to upgrade to a supported major engine version.

For example, the ElastiCache end of standard support date for Redis OSS 4.0.10 is January 31, 2026. If you aren't ready to manually upgrade to Valkey or to Redis OSS 6 or later by that date, ElastiCache will automatically enroll your caches in Extended Support and you can continue to run Redis OSS 4.0.10. Starting the first day of the month after the standard support ends, February 1, 2026, ElastiCache automatically charges you for Extended Support.

Extended Support is available for up to 3 years past the end of standard support date for a major engine version. For Elasticache for Redis OSS versions 4 and 5, that will be January 31, 2029. After this date, any caches still running Redis OSS versions 4 and 5 will be automatically upgraded to the latest version of Valkey.

Once an engine’s support period ends, caches that continue to run that old version will automatically transition to Extended Support. You will be notified before the Extended Support pricing start date so you may upgrade your instance instead. You also can explicitly opt out at any time by upgrading to supported versions.

For more information about the end of standard support dates and
the end of Extended Support dates, see [ElastiCache versions for Redis OSS end of life schedule](engine-versions.md#deprecated-engine-versions "engine-versions.md#deprecated-engine-versions") for Valkey, Memcached or Redis OSS.

###### Topics

- [ElastiCache Extended Support charges](extended-support-charges.md "extended-support-charges.md")
- [Versions with ElastiCache Extended Support](extended-support-versions.md "extended-support-versions.md")
- [ElastiCache and customer
  responsibilities with ElastiCache Extended Support](extended-support-responsibilities.md "extended-support-responsibilities.md")
