# Versions with ElastiCache Extended Support

Redis Open Source Software (OSS) versions 4 and 5 reached their community End of Life in 2020 and 2022, respectively. This means no further updates, bug fixes, or security patches are being released by the community. Standard support for ElastiCache Redis OSS versions 4 and 5 on ElastiCache will end on January 31, 2026. Continuing to use unsupported versions of Redis OSS could leave your data vulnerable to known [Common Vulnerabilities and Exposures](https://nvd.nist.gov/vuln-metrics/cvss "https://nvd.nist.gov/vuln-metrics/cvss") (CVEs).

Starting on February 1, 2026, ElastiCache caches still running on Redis OSS versions 4 and 5 will be automatically enrolled in Extended Support, to provide continuous availability and security. Although Extended Support offers flexibility, we recommend treating the end of standard support as a planning milestone for your production workloads. We strongly encourage you to upgrade your Redis OSS v4 and v5 caches to ElastiCache for Valkey or Redis OSS v6 or later, before the end of standard support.

The following table summarizes the Amazon ElastiCache end of standard support date and Extended Support dates.

**Extended support and End of Life schedule**

| Major Engine Version | End of Standard Support | Start of Extended Support Y1 Premium | Start of Extended Support Y2 Premium | Start of Extended Support Y3 Premium | End of Extended Support and version EOL |
| -------------------- | ----------------------- | ------------------------------------ | ------------------------------------ | ------------------------------------ | --------------------------------------- |
| Redis OSS v4         | 1/31/2026               | 2/1/2026                             | 2/1/2027                             | 2/1/2028                             | 1/31/2029                               |
| Redis OSS v5         | 1/31/2026               | 2/1/2026                             | 2/1/2027                             | 2/1/2028                             | 1/31/2029                               |
| Redis OSS v6         | 1/31/2027               | 2/1/2027                             | 2/1/2028                             | 2/1/2029                             | 1/31/2030                               |

Extended Support will only be offered for the latest supported patch version of each major Redis OSS version. When Extended Support begins on February 1, 2026, if your Redis OSS v4 and v5 clusters are not already on the latest patch versions, they will be automatically upgraded to v4.0.10 for Redis OSS v4, and v5.0.6 for Redis OSS v5, before being enrolled in Extended Support. This ensures that you receive security updates and bug fixes through Extended Support. You do not need to take any action to upgrade to these latest patch versions as part of the Extended Support transition.
