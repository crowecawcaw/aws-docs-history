# Engine releases for Amazon Neptune

Amazon Neptune releases engine updates regularly.

You can determine which engine release version you currently have installed using
the [instance-status API](access-graph-status.md "access-graph-status.md") or the Neptune
console. The version number tells you whether you are running an original major
release, or a minor release, or a patch release.. For more information about release
numbering, see [Engine version numbers](cluster-maintenance.md#engine-version-numbers "cluster-maintenance.md#engine-version-numbers").

For more information about updates in general, see [Cluster maintenance](cluster-maintenance.md "cluster-maintenance.md").

From engine release 1.3.0.0 going forward, engine versions will have the structure
shown in the table below. The minor version number is the one that will be evaluated for
[AutoMinorVersionUpgrade](engine-maintenance-management.md#using-amvu "engine-maintenance-management.md#using-amvu") processing.

| Version                                                        | Product version | Major version | Minor version | Patch version | Status   | Released   | End of life | Upgrade to: |
| -------------------------------------------------------------- | --------------- | ------------- | ------------- | ------------- | -------- | ---------- | ----------- | ----------- |
| [1.4.6.3](engine-releases-1.4.6.md "engine-releases-1.4.6.md") | 1               | 4             | 6             | 3             | _active_ | 2025-12-18 | 2027-03-06  | N/A         |
| [1.4.6.2](engine-releases-1.4.6.md "engine-releases-1.4.6.md") | 1               | 4             | 6             | 2             | _active_ | 2025-11-18 | 2027-03-06  | 1.4.6.3     |
| [1.4.6.1](engine-releases-1.4.6.md "engine-releases-1.4.6.md") | 1               | 4             | 6             | 1             | _active_ | 2025-09-18 | 2027-03-06  | 1.4.6.3     |
| [1.4.6.0](engine-releases-1.4.6.md "engine-releases-1.4.6.md") | 1               | 4             | 6             | 0             | _active_ | 2025-09-02 | 2027-03-06  | 1.4.6.3     |
| [1.4.5.1](engine-releases-1.4.5.md "engine-releases-1.4.5.md") | 1               | 4             | 5             | 1             | _active_ | 2025-06-30 | 2027-03-06  | 1.4.6.0     |
| [1.4.5.0](engine-releases-1.4.5.md "engine-releases-1.4.5.md") | 1               | 4             | 5             | 0             | _active_ | 2025-04-09 | 2027-03-06  | 1.4.5.1     |
| [1.4.4.0](engine-releases-1.4.4.md "engine-releases-1.4.4.md") | 1               | 4             | 4             | 0             | _active_ | 2025-02-24 | 2027-03-06  | 1.4.5.0     |
| [1.4.3.0](engine-releases-1.4.3.md "engine-releases-1.4.3.md") | 1               | 4             | 3             | 0             | _active_ | 2025-01-21 | 2027-03-06  | 1.4.4.0     |
| [1.4.2.0](engine-releases-1.4.2.md "engine-releases-1.4.2.md") | 1               | 4             | 2             | 0             | _active_ | 2024-12-19 | 2027-03-06  | 1.4.3.0     |
| [1.4.1.0](engine-releases-1.4.1.md "engine-releases-1.4.1.md") | 1               | 4             | 1             | 0             | _active_ | 2024-11-21 | 2027-03-06  | 1.4.2.0     |
| [1.4.0.0](engine-releases-1.4.0.md "engine-releases-1.4.0.md") | 1               | 4             | 0             | 0             | _active_ | 2024-11-06 | 2027-03-06  | 1.4.1.0     |
| [1.3.4.0](engine-releases-1.3.4.md "engine-releases-1.3.4.md") | 1               | 3             | 4             | 0             | _active_ | 2024-10-01 | 2027-03-06  | 1.4.0.0     |
| [1.3.3.0](engine-releases-1.3.3.md "engine-releases-1.3.3.md") | 1               | 3             | 3             | 0             | _active_ | 2024-08-05 | 2027-03-06  | 1.3.4.0     |
| [1.3.2.1](engine-releases-1.3.2.md "engine-releases-1.3.2.md") | 1               | 3             | 2             | 1             | _active_ | 2024-06-20 | 2027-03-06  | 1.3.3.0     |
| [1.3.2.0](engine-releases-1.3.2.md "engine-releases-1.3.2.md") | 1               | 3             | 2             | 0             | _active_ | 2024-06-10 | 2027-03-06  | 1.3.2.1     |
| [1.3.1.0](engine-releases-1.3.1.md "engine-releases-1.3.1.md") | 1               | 3             | 1             | 0             | _active_ | 2024-03-06 | 2027-03-06  | 1.3.2.1     |
| [1.3.0.0](engine-releases-1.3.0.md "engine-releases-1.3.0.md") | 1               | 3             | 0             | 0             | _active_ | 2023-11-15 | 2027-03-06  | 1.3.2.1     |

The table below lists all the engine releases since 1.0.1.0, along with
information about version end-of-life. You can use the dates in this table
to plan your testing and upgrade cycles.

| Version                                                           | Major version | Minor version | Status       | Released              | End of life | Upgrade to: |
| ----------------------------------------------------------------- | ------------- | ------------- | ------------ | --------------------- | ----------- | ----------- |
| [1.2.1.2](engine-releases-1.2.1.md "engine-releases-1.2.1.md")    | 1.2           | 1.2           | _active_     | 2024-08-05            | 2026-06-30  | 1.3.0.0     |
| [1.2.1.1](engine-releases-1.2.1.md "engine-releases-1.2.1.md")    | 1.2           | 1.1           | _active_     | 2024-03-11            | 2026-06-30  | 1.3.0.0     |
| [1.2.1.0](engine-releases-1.2.1.md "engine-releases-1.2.1.md")    | 1.2           | 1.0           | _active_     | 2023-03-08            | 2026-06-30  | 1.3.0.0     |
| [1.2.0.2](engine-releases-1.2.0.md "engine-releases-1.2.0.md")    | 1.2           | 0.2           | _active_     | 2022-11-16            | 2026-06-30  | 1.3.0.0     |
| [1.2.0.1](engine-releases-1.2.0.md "engine-releases-1.2.0.md")    | 1.2           | 0.1           | _active_     | 2022-10-26            | 2026-06-30  | 1.3.0.0     |
| [1.2.0.0](engine-releases-1.2.0.md "engine-releases-1.2.0.md")    | 1.2           | 0.0           | _active_     | 2022-07-21            | 2026-06-30  | 1.3.0.0     |
| [1.1.1.0](engine-releases-1.1.1.md "engine-releases-1.1.1.md")    | 1.1           | 1.0           | _active_     | 2022-04-19            | 2026-06-30  | 1.2.1.0     |
| [1.1.0.0](engine-releases-1.1.0.md "engine-releases-1.1.0.md")    | 1.1           | 0.0           | _deprecated_ | 2021-11-19            | 2025-03-15  | 1.1.1.0     |
| [1.0.5.1](engine-releases-1.0.5.md "engine-releases-1.0.5.md")    | 1.0           | 5.1           | _deprecated_ | 2021-10-01            | 2023-01-30  | 1.1.0.0     |
| [1.0.5.0](engine-releases-1.0.5.md "engine-releases-1.0.5.md")    | 1.0           | 5.0           | _deprecated_ | 2021-07-27            | 2023-01-30  | 1.1.0.0     |
| [1.0.4.2](engine-releases-1.0.4.md "engine-releases-1.0.4.md")    | 1.0           | 4.2           | _deprecated_ | 2021-06-01            | 2023-01-30  | 1.1.0.0     |
| [1.0.4.1](engine-releases-1.0.4.md "engine-releases-1.0.4.md")    | 1.0           | 4.1           | _deprecated_ | 2020-12-08            | 2023-01-30  | 1.1.0.0     |
| [1.0.4.0](engine-releases-1.0.4.md "engine-releases-1.0.4.md")    | 1.0           | 4.0           | _deprecated_ | 2020-10-12            | 2023-01-30  | 1.1.0.0     |
| [1.0.3.0](engine-releases-1.0.3.md "engine-releases-1.0.3.md")    | 1.0           | 3.0           | _deprecated_ | 2020-08-03            | 2023-01-30  | 1.1.0.0     |
| [1.0.2.2](engine-releases-1.0.2.md "engine-releases-1.0.2.md")    | 1.0           | 2.2           | _deprecated_ | 2020-03-09            | 2022-07-29  | 1.0.3.0     |
| [1.0.2.1](engine-releases-1.0.2.md "engine-releases-1.0.2.md")    | 1.0           | 2.1           | _deprecated_ | 2019-11-22            | 2022-07-29  | 1.0.3.0     |
| [1.0.2.0](engine-releases-1.0.2.md "engine-releases-1.0.2.md")    | 1.0           | 2.0           | _deprecated_ | 2019-11-08            | 2020-05-19  | 1.0.3.0     |
| [1.0.1.2](engine-releases-1.0.1.md "engine-releases-1.0.1.md")    | 1.0           | 1.2           | _deprecated_ | 2019-10-15            | —           | —           |
| [1.0.1.1](engine-releases-1.0.1.md "engine-releases-1.0.1.md")    | 1.0           | 1.1           | _deprecated_ | 2019-08-13            | —           | —           |
| [1.0.1.0.\*](engine-releases-1.0.1.md "engine-releases-1.0.1.md") | 1.0           | 1.0.\*        | _deprecated_ | 2019-07-02 and before | —           | —           |

## Major engine version end-of-life planning

Neptune engine versions almost always reach their end of life at the end of a
calendar quarter. Exceptions occur only when important security or availability issues
arise.

When an engine version reaches its end of life, you will be required to upgrade
your Neptune database to a newer version.

In general, Neptune engine versions continue to be available as follows:

- **Minor engine versions:** Minor engine
  versions remain available for at least 6 months following their release.
- **Major engine versions:** Major engine
  versions remain available for at least 12 months following their release.

At least 3 months before an engine version reaches its end of life, AWS will
send an automated email notification to the email address associated with your AWS
account and post the same message to your [AWS
Health Dashboard](../../../health/latest/ug/aws-health-dashboard-status.md "../../../health/latest/ug/aws-health-dashboard-status.md"). This will give you time to plan and prepare to upgrade.

When an engine version reaches its end of life, you will no longer be able to
create new clusters or instances using that version, nor will autoscaling be able
to create instances using that version.

An engine version that actually reaches its end of life will automatically be
upgraded during a maintenance window. The message sent to you 3 months before the
engine version's end of life will contain details about what this automatic update
would involve, including the version to which you would be automatically upgraded,
the impact on your DB clusters, and actions that we recommend.

###### Important

You are responsible for keeping your database engine versions current.
AWS urges all customers to upgrade their databases to the latest engine version
in order to benefit from the most current security, privacy, and availability
safeguards. If you operate your database on an unsupported engine or software
past the deprecation date ("Legacy Engine"), you face a greater likelihood of
security, privacy, and operational risks, including downtime events.

Operation of your database on any engine is subject to the Agreement
governing your use of the AWS Services. Legacy Engines are not Generally
Available. AWS no longer provides support for the Legacy Engine, and AWS
may place limits on the access to or use of any Legacy Engine at any time,
if AWS determines the Legacy Engine poses a security or liability risk,
or a risk of harm, to the Services, AWS, its Affiliates, or any third party.
Your decision to continue running Your Content in a Legacy Engine could
result in Your Content becoming unavailable, corrupted, or unrecoverable.
Databases running on a Legacy Engine are subject to Service Level Agreement
(SLA) Exceptions.

DATABASES AND RELATED SOFTWARE RUNNING ON A LEGACY ENGINE CONTAIN BUGS,
ERRORS, DEFECTS, AND/OR HARMFUL COMPONENTS. ACCORDINGLY, AND NOTWITHSTANDING
ANYTHING TO THE CONTRARY IN THE AGREEMENT OR THE SERVICE TERMS, AWS IS
PROVIDING THE LEGACY ENGINE "AS IS."
