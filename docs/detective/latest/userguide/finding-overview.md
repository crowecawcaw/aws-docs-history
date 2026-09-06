

# Analyzing a finding overview in Detective
<a name="finding-overview"></a>

A Detective finding overview provides detailed information about the finding. It also displays a summary of the involved entities, with links to the associated entity profiles.

## Scope time used for the finding overview
<a name="finding-overview-scope-time"></a>

The scope time for a finding overview is set to the finding time window. The finding time window reflects the first and last time that the finding activity was observed.

## Finding details
<a name="finding-overview-finding-details"></a>

The panel at the right contains the details for the finding. These are the details provided by the finding provider.

From the finding details, you can also archive the finding. For more details, see [Archiving an Amazon GuardDuty finding](https://docs.aws.amazon.com/detective/latest/userguide/finding-update-status.html).

## Related entities
<a name="finding-overview-entities"></a>

The finding overview contains a list of entities that are involved in the finding. For each entity, the list provides overview information about the entity. This information reflects the information on the entity details profile panel on the corresponding entity profile.

You can filter the list based on entity type. You can also filter the list based on text in the entity identifier.

To pivot to the profile for an entity, choose **See profile**. When you pivot to the entity profile, the following occurs:
+ The scope time is set to the finding time window.
+ On the **Associated findings** panel for the entity, the finding is selected. The finding details remain displayed at the right of the entity profile.

## Troubleshooting 'Page not found'
<a name="finding-troubleshooting"></a>

When you navigate to an entity or a finding in Detective, you may see a **Page not found** error message. 

To resolve this, do one of the following: 
+ Make sure that the entity or finding belongs to one of your member accounts. For information on how to review member accounts, see [Viewing the list of accounts](https://docs.aws.amazon.com/detective/latest/userguide/accounts-view-list.html).
+ Make sure your administrator account is aligned with GuardDuty and/or Security Hub CSPM to pivot to Detective from these services. For the recommendations, see [Recommended alignment with GuardDuty and Security Hub CSPM](https://docs.aws.amazon.com/detective/latest/userguide/detective-setup.html#detective-recommendations).
+ Verify that the finding occurred after the member account accepted your invitation.
+ Verify the Detective behavior graph is ingesting data from an optional data source package. For more information about source data used in Detective behavior graphs, see [Source data used in a behavior graph](https://docs.aws.amazon.com/detective/latest/userguide/detective-source-data-about.html).
+ To allow Detective to ingest data from Security Hub CSPM and add that data to your behavior graph, you must enable Detective for AWS security findings as a data source package. For more information, see [AWS security findings](https://docs.aws.amazon.com/detective/latest/userguide/source-data-types-asff.html).
+ If you are navigating to an entity profile or finding overview in Detective, make sure that the URL is in the right format. For details on the formation of a profile URL, see [Navigating to an entity profile or finding overview using URL](https://docs.aws.amazon.com/detective/latest/userguide/profile-navigate-url.html).