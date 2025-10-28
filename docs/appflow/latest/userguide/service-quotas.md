# Quotas for Amazon AppFlow

Your AWS account has default quotas, formerly referred to as limits, for each AWS
service. Unless otherwise noted, each quota is Region-specific. You can request increases
for some quotas, and other quotas cannot be increased.

###### Flows

Your AWS account has the following quotas related to Amazon AppFlow.

- Number of flows per account: 1,000
- Number of flow runs per month: 10 million
- Number of concurrent flow runs at any time: 1000

###### Flow runs

The maximum time that a flow can run is 48 hours.

The following source applications place quotas on the amount of data they can
process:

- Amplitude: 25 MB of data per flow run.
- Marketo:
  - Data import from Marketo: 1 GB per flow run. To transfer over 1 GB of data, you
    can split your workload into multiple flows by applying the appropriate filters for
    each flow.
  - Data export to Marketo: You can insert up to 500 MB of records into Marketo in a
    single flow run. If your source is Amazon S3, each CSV file cannot exceed 125 MB in size.
    However, you can drop multiple CSV files (each less than 125 MB) into the source
    bucket or folder, and Amazon AppFlow will transfer all the data to Marketo in a single
    flow run.

- Salesforce:
  - Events from Salesforce: Amazon AppFlow currently uses a third-party library,
    which is allocated a fixed buffer size of 10 MB. If a surge of events on a
    single event channel (such as `AccountChangeEvent`) exceeds the
    buffer size, then events might be dropped. You can request a larger buffer
    by filing a support case in the AWS Management Console. When you create
    the case, choose the **Technical support** case type. For
    **Description**, provide the ARN of your flow and the
    buffer size that you request. For more information, see [Creating a support case](../../../awssupport/latest/user/case-management.md#creating-a-support-case "../../../awssupport/latest/user/case-management.md#creating-a-support-case").

  To determine a suitable buffer size, calculate the maximum volume of burst
  data that you anticipate. To do that, multiply the average event size with
  the maximum number of burst events that can occur in a 5-second
  window.
  - Data export to Salesforce: You can insert, update, or upsert up to 500 MB of
    records into Salesforce in a single flow run. If your source is Amazon S3, each CSV file
    cannot exceed 125 MB in size. However, you can drop multiple CSV files (each less
    than 125 MB) into the source bucket or folder, and Amazon AppFlow will transfer all the
    data to Salesforce in a single flow run.

- ServiceNow: 100,000 records per flow run.
- Google Analytics: 9 dimensions and 10 metrics per flow run
- Amazon EventBridge: Events are limited to 256 KB. If your event exceeds this size, Amazon AppFlow publishes a summary event with a pointer to the S3 bucket where you can get the full event.

###### Flow frequency

Amazon AppFlow can run schedule-triggered flows up to once per minute. However, the
following source applications place quotas on how frequently you can run a
schedule-triggered flow:

- Amazon S3: Maximum frequency of one flow run per minute
- Amplitude: Maximum frequency of one flow run per day
- Datadog: Maximum frequency of one flow run per minute
- Dynatrace: Maximum frequency of one flow run per minute
- Google Analytics: Maximum frequency of one flow run per day
- Infor Nexus: Maximum frequency of one flow run per minute
- Marketo: Maximum frequency of one flow run per hour
- Salesforce: Maximum frequency of one flow run per minute
- Salesforce Pardot: Maximum frequency of one flow run per minute
- ServiceNow: Maximum frequency of one flow run per minute
- Singular: Maximum frequency of one flow run per hour
- Slack: Maximum frequency of one flow run per minute
- Trend Micro: Maximum frequency of one flow run per hour
- Veeva: Maximum frequency of one flow run per minute
- Zendesk: Maximum frequency of one flow run per minute

###### Source and destination API limits

The API calls that Amazon AppFlow makes to data sources and destinations count against any
API limits for that application. For example, if you set up an hourly flow that pulls
five pages of data from Salesforce, Amazon AppFlow will make a total of 120 daily API calls
(24x5=120). This will count against your 24-hour Salesforce API limit. The exact
SalesForce API limit in this example would vary depending on your edition and number of
licenses.

###### Amazon AppFlow API limits

There is a soft quota of 100 connector profiles per AWS account. If you need more connector profiles than this quota allows, you can submit a request to the Amazon AppFlow team through the Amazon AppFlow support channel.
