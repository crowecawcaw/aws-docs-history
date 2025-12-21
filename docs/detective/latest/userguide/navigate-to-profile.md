# Navigating directly to an entity profile or finding

overview

To navigate directly to an entity profile or finding overview in Amazon Detective, you can use one
of these options.

- From Amazon GuardDuty or AWS Security Hub CSPM, you can pivot from a GuardDuty finding to the corresponding Detective
  finding profile.
- You can assemble a Detective URL that identifies a finding or entity and sets the scope time to
  use.

## Pivoting to an entity profile or finding overview

from Amazon GuardDuty or AWS Security Hub CSPM

From the Amazon GuardDuty console, you can navigate to the entity profile for an entity that is
related to a finding.

From the GuardDuty and AWS Security Hub CSPM consoles, you can also navigate to a finding overview. This
also provides links to the entity profiles for the involved entities.

These links can help to streamline the investigation process. You can quickly use Detective to
see the associated entity activity and determine next steps. You can then archive a finding if it
is a false positive or explore further to determine the scope of the problem.

### How to pivot to the Amazon Detective console

The investigation links are available for all GuardDuty findings. GuardDuty also allows you to
choose whether to navigate to an entity profile or to the finding overview.

###### To pivot to Detective from the GuardDuty console

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").
2. If necessary, choose **Findings** in the left navigation pane.
3. On the GuardDuty **Findings** page, choose the finding.

The finding details pane displays to the right of the finding list. 4. On the finding details pane, choose **Investigate in Detective**.

GuardDuty displays a list of available items to investigate in Detective.

The list contains both the related entities, such as IP addresses or EC2 instances, and
the finding. 5. Choose an entity or the finding.

The Detective console opens in a new tab. The console opens to the entity or finding
profile.

If you have not enabled Detective, then the console opens to a landing page that provides an
overview of Detective. From there, you can choose to enable Detective.

###### To pivot to Detective from the Security Hub CSPM console

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").
2. If necessary, choose **Findings** in the left navigation pane.
3. On the Security Hub CSPM **Findings** page, choose a GuardDuty finding.
4. In the details pane, choose **Investigate in Detective** and then choose
   **Investigate finding**.

When you choose **Investigate finding**, the Detective console opens in a new
tab. The console opens to the finding overview.

The Detective console always opens to the Region where the finding originated, even if you
pivot from your aggregation Region. For more information about finding aggregation, see [Aggregating
findings across Regions](../../../securityhub/latest/userguide/finding-aggregation.md "../../../securityhub/latest/userguide/finding-aggregation.md") in the _AWS Security Hub User Guide_.

If you have not enabled Detective, the console opens to the Detective landing page. From there,
you can enable Detective.

### Troubleshooting the pivot

To use the pivot, one of the following must be true:

- Your account must be an administrator account for both Detective and the service you are pivoting
  from.
- You have assumed a cross-account role that grants you administrator account access to the
  behavior graph.

For more information about the recommendation to align administrator accounts, see [Recommended alignment with Amazon GuardDuty and AWS Security Hub CSPM](detective-setup.md#detective-recommendations "detective-setup.md#detective-recommendations").

If the pivot does not work, check the following.

- **Does the finding belong to an enabled member account in your
  behavior graph?** If the associated account was not invited to the behavior graph as
  a member account, then the behavior graph does not contain data for that account.

If an invited member account did not accept the invitation, then the behavior graph does
not contain data for that account.

- **Is the finding archived?** Detective does not receive archived
  findings from GuardDuty.
- **Did the finding occur before Detective began to ingest data into your
  behavior graph?** If the finding is not present in the data that Detective ingests, then
  the behavior graph does not contain data for it.
- **Is the finding from the correct Region?** Each behavior
  graph is specific to a Region. A behavior graph does not contain data from other
  Regions.

## Navigating to an entity profile or finding overview using

a URL

To navigate to an entity profile or finding overview in Amazon Detective, you can use a URL that
provides a direct link to it. The URL identifies the finding or entity. It can also specify the
scope time to use on the profile. Detective maintains up to a year of historical event data.

### Format of a profile URL

###### Note

If you are using the old URL format, Detective will automatically redirect to the new URL. The
old format of the URL was:

https://console.aws.amazon.com/detective/home?region=`Region`#`type`/`namespace`/`instanceID`?`parameters`

The new format of the profile URL is as follows:

- For entities -
  https://console.aws.amazon.com/detective/home?region=`Region`#`entities`/`namespace`/`instanceID`?`parameters`
- For findings -
  https://console.aws.amazon.com/detective/home?region=`Region`#`findings`/`instanceID`?`parameters`

The URL requires the following values.

**`Region`**

The Region that you want to use.

**`type`**

The type of item for the profile that you are navigating to.

- `entities` - Indicates that you are navigating to an entity profile
- `findings` - Indicates that you are navigating to a finding overview

**`namespace`**

For entities, the namespace is the name of the entity type.

- `AwsAccount`
- `AwsRole`
- `AwsRoleSession`
- `AwsUser`
- `Ec2Instance`
- `FederatedUser`
- `IpAddress`
- `S3Bucket`
- `UserAgent`
- `FindingGroup`
- `KubernetesSubject`
- `ContainerPod`
- `ContainerCluster`
- `ContainerImage`

**`instanceID`**

The instance identifier of the finding or entity.

- For a GuardDuty finding, the GuardDuty finding identifier.
- For an AWS account, the account ID.
- For AWS roles and users, the principal ID of the role or of the user.
- For federated users, the principal ID of the federated user. The principal ID is
  either
  ``<identityProvider>`:`<username>``
  or
  ``<identityProvider>`:`<audience>`:`<username>``.
- For IP addresses, the IP address.
- For user agents, the user agent name.
- For EC2 instances, the instance ID.
- For role sessions, the session identifier. The session identifier uses the format``<rolePrincipalID>`:`<sessionName>``.
- For S3 buckets, the bucket name.
- For FindingGroups, a UUID. for example,
  `ca6104bc-a315-4b15-bf88-1c1e60998f83`
- For EKS resources, use the following formats:
  - EKS cluster: `<clusterName>~<accountId>~EKS`
  - Kubernetes Pod:
    `<podUid>~<clusterName>~<accountId>~EKS`
  - Kubernetes Subject:
    `<subjectName>~<clusterName>~<accountId>`
  - Container image:
    `<registry>/<repository>:<tag>@<digest>`

The finding or entity must be associated with an enabled account in your behavior
graph.

The URL can also include the following optional parameters, which are used to set the scope
time. For more information about scope time and how it is used on profiles, see [Managing the scope time](scope-time-managing.md "scope-time-managing.md").

**`scopeStart`**

Start time for the scope time to use on the profile. Start time must be within the last
365 days.

The value is the epoch timestamp.

If you provide a start time but no end time, then the scope time ends at the current
time.

**`scopeEnd`**

End time for the scope time to use on the profile.

The value is the epoch timestamp.

If you provide an end time, but no start time, then the scope time includes all time
before the end time.

If you don't specify the scope time, then the default scope time is used.

- For findings, the default scope time uses the first and last times that the finding
  activity was observed.
- For entities, the default scope time is the previous 24 hours.

Here is an example of a Detective URL:

`https://console.aws.amazon.com/detective/home?region=us-east-1#entities/IpAddress/192.168.1.1?scopeStart=1552867200&scopeEnd=1552910400`

This example URL provides the following instructions.

- Display the entity profile for the IP address 192.168.1.
- Use a scope time that starts Monday, March 18, 2019 12:00:00 AM GMT and that ends Monday,
  March 18, 2019 12:00:00 PM GMT.

### Troubleshooting a URL

If the URL does not display the expected profile, first check that the URL uses the correct
format and that you have provided the correct values.

- Did you start with the correct URL (`findings` or `entities`)?
- Did you specify the correct namespace?
- Did you provide the correct identifier?

If the values are correct, then you can also check the following.

- **Does the finding or entity belong to an enabled member account in
  your behavior graph?** If the associated account was not invited to the behavior
  graph as a member account, then the behavior graph does not contain data for that
  account.

If an invited member account did not accept the invitation, then the behavior graph does
not contain data for that account.

- **For a finding, is the finding archived?** Detective does not
  receive archived findings from Amazon GuardDuty.
- **Did the finding or entity occur before Detective began to ingest data
  into your behavior graph?** If the finding or entity is not present in the data that
  Detective ingests, then the behavior graph does not contain data for it.
- **Is the finding or entity from the correct Region?** Each
  behavior graph is specific to a Region. A behavior graph does not contain data from other
  Regions.

## Adding Detective URLs for findings to Splunk

The Splunk Trumpet project allows you send data from AWS services to Splunk.

You can configure the Trumpet project to generate Detective URLs for Amazon GuardDuty findings. You can
then use these URLs to pivot directly from Splunk to the corresponding Detective finding
profiles.

The Trumpet project is available from GitHub at [https://github.com/splunk/splunk-aws-project-trumpet](https://github.com/splunk/splunk-aws-project-trumpet "https://github.com/splunk/splunk-aws-project-trumpet").

On the configuration page for the Trumpet project, from **AWS CloudWatch Events**,
choose **Detective GuardDuty URLs**.
