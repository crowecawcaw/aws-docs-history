# Data retention

| HCL_COST1. How do you define and<br>enforce data retention policies? |
| -------------------------------------------------------------------- |
|                                                                      |

**Determine applicable
regulatory frameworks and controls as it pertains to data
retention**

Healthcare organizations may be subject to regulatory and
company requirements dictating how long they must store both
health data as well as logs detailing access to that data. Over
time, storage requirements can reach petabyte scale for an
individual organization. New imaging modalities, such as digital
pathology, have the potential to push data volumes even higher.
Developing strategies for data retention is imperative to
maintain compliance while minimizing cost.

Healthcare organizations should establish a data retention
policy identifying the types and duration that data should be
retained in accordance with internal and external requirements.

**Implement data lifecycle
policies**

As healthcare data ages, its access frequency declines.
Implement lifecycle policies that transition
infrequently-accessed data to lower-cost storage tiers. When
designing your policies for each type of data, be sure to factor
the size of the data, the frequency of access, and expectations
for retrieval time; these are the three predominant
cost-drivers. For example, use Amazon S3 Lifecycle
configurations to archive infrequently accessed data after some
period of time, automatically reducing storage costs.
Alternatively, use Amazon S3 Intelligent-Tiering to shift the
archival policies to focus on time of last access instead of
time the object has been in Amazon S3.

**Centralize automated
policy enforcement**

Adopting infrastructure as code, as discussed in the operational
excellence pillar, enables you to define and test your data
retention policies before they make it into production. For
example, if regulatory requirements specify that you must retain
certain medical images for 10 years, you can verify that no Amazon S3
lifecycle policy expires an object before that time.
Additionally, consider AWS Backup for centralized backup
management, which enables you to back up application data in a
consistent and compliant manner.

**Validate lifecycle
policies are enforced**

Because the cloud is API-driven, you can monitor changes to your
environment as described in the operational excellence and
security tiers. Set up alerts for when an API action alters a
data retention policy so you can quickly review the change to
make sure it was authorized and operating correctly. If using
AWS Backup, use AWS Backup Audit Manager to automatically detect
when your AWS Backup policies violate your data retention
requirements.
