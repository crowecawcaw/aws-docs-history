# Planning for Amazon Neptune major engine version life-span

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
  account and post the same message to your [AWS Health Dashboard](../../../health/latest/ug/aws-health-dashboard-status.md "../../../health/latest/ug/aws-health-dashboard-status.md").
  This will give you time to plan and prepare to upgrade.

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
