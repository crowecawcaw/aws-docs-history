End of support notice: On June 30, 2027, AWS
will end support for AMS Advanced. After June 30, 2027, you will
no longer be able to access the AMS Advanced console or AMS Advanced resources.
For more information, see [AMS Advanced end of support](SunsetPlan.md "SunsetPlan.md").

# Single-Account Landing Zone proactive monitoring of Active Directory Trust in AMS

AMS single-account landing zone (SALZ) monitors the status of the one-way trust(s) between the
Managed Active Directory (AD) in your AMS managed account and your company domain.
The one-way trust with Managed AD is critical for access requests and instance logon requests.
With this new monitoring, AMS now proactively responds to trust related issues, and
reduces the mean time to detect access related incidents.

This feature is automatically enabled in your AWS Managed Services (AMS) accounts.

There is a small cost impact. The feature uses four AWS CloudWatch metrics, and two AWS CloudWatch
alarms for one trust.
