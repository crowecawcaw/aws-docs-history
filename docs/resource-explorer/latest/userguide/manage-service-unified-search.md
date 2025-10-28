AWS Resource Explorer now provides immediate access to resource search and
discovery capabilities in a Region. With this launch, you no longer need to activate
Resource Explorer to discover your resources. [Learn more](manage-immediate-resource-discovery-experience.md "manage-immediate-resource-discovery-experience.md")

# Supporting Unified Search in the

AWS Management Console

The AWS Management Console has a search bar at the top of every console page. This provides a
[Unified Search](../../../awsconsolehelpdocs/latest/gsg/using-search.md "../../../awsconsolehelpdocs/latest/gsg/using-search.md") experience across all AWS services. Unified Search results can
include such things as:

- AWS service and feature console pages.
- AWS documentation pages.
- AWS blog and Knowledge Base articles
- Resources in your accounts — if you follow the steps below.
  To see your account's resources in your Unified Search results, you must perform the
  following steps. You can do this during initial setup of AWS Resource Explorer. It all happens
  automatically if you use the **Quick setup** option.

- You must [create an aggregator
  index](manage-aggregator-region-turn-on.md "manage-aggregator-region-turn-on.md") in one AWS Region for the AWS account.
- You must [create a default view in the
  AWS Region that contains the aggregator index](configure-views-set-default.md "configure-views-set-default.md").
- You must grant all principals that need to search for resources in the Unified
  Search bar [permission to search using
  that default view](configure-views-grant-access.md "configure-views-grant-access.md").
  Unified Search always uses the default view in the AWS Region that contains the
  aggregator index to perform all searches.
