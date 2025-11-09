# Change management

| ADVREL04: How do you prevent regression<br>from changes in your application and infrastructure? |
| ----------------------------------------------------------------------------------------------- |
|                                                                                                 |

Changes to your advertising workload or its environment must be anticipated and accommodated to achieve reliable operation of the workload. Changes include those imposed on your workload such as spikes in demand, as well as those from within such as feature deployments and security patches.

Maintain reliability during application and infrastructure
changes. Implement comprehensive testing (like regression,
performance, and canary) in CI/CD pipelines to monitor impact on
critical metrics. Additionally, use phased deployment strategies
(like blue/green and rolling) to minimize service disruption and
quickly recover from issues.

###### Best practices

- [ADVREL04-BP01 Through your CI/CD pipeline, employ end-to-end regression, performance, and canary testing](advrel04-bp01.md "advrel04-bp01.md")
- [ADVREL04-BP02 Deploy new code or resources in staggered phases, separated by sufficient time, to verify that the changes are successful](advrel04-bp02.md "advrel04-bp02.md")
