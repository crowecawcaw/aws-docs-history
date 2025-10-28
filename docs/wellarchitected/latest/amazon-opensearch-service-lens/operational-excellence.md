# Operational excellence

The operational excellence pillar offers guidance on effectively
running and monitoring systems to deliver business value, while
continually improving supporting processes and procedures. This
involves maintaining high-quality Amazon OpenSearch Service domains, gaining
operational insights, and continually improving processes to achieve
organizational outcomes and values.

The subsequent questions and best practices complement those
outlined in the Operational Excellence Pillar whitepaper.

###### Focus areas

- [Design principles](#design-principles-ops "#design-principles-ops")
- [Operate](operate.md "operate.md")
- [Evolve](evolve.md "evolve.md")
- [Key AWS services](key-aws-services-ops.md "key-aws-services-ops.md")
- [Resources](resources-ops.md "resources-ops.md")

## Design principles

In addition to the AWS Well-Architected Framework whitepaper
principles, the following design principles can help achieve
operational excellence for your Amazon OpenSearch Service
workloads:

- **Implement monitoring and
  alerting:** Set up comprehensive monitoring and
  alerting within OpenSearch deployments, featuring log
  analysis, performance tracking, and notification systems that
  provide real-time alerts for slow queries, security events,
  and critical errors.
- **Optimize index management:**
  Employ efficient index management strategies, such as using
  Index templates and removing unused indexes, to maintain a
  clean and efficient index namespace.
- **Implement a regular
  snapshot:** Implement regular snapshots using Index
  State Management (ISM) to ensure consistent backups of
  OpenSearch data.
