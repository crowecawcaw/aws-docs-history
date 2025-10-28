AWS Resource Explorer now provides immediate access to resource search and
discovery capabilities in a Region. With this launch, you no longer need to activate
Resource Explorer to discover your resources. [Learn more](manage-immediate-resource-discovery-experience.md "manage-immediate-resource-discovery-experience.md")

# Getting started with Resource Explorer

Use the topics in this section to get a basic understanding of the concepts and terms used
by AWS Resource Explorer. Learn how Resource Explorer is automatically enabled based on your permissions and how
to access enhanced features for your AWS account.

## Accessing Resource Explorer

Resource Explorer is automatically enabled when you access the service through any of the
following methods, with your experience determined by your IAM permissions:

- **Full Experience:** Users with, at minimum,
  the permissions in the `AWSResourceExplorerReadOnlyAccess` managed policy and
  the `iam:CreateServiceLinkedRole` permission (included in the
  [AWSResourceExplorerFullAccess](../../../aws-managed-policy/latest/reference/AWSResourceExplorerFullAccess.md "../../../aws-managed-policy/latest/reference/AWSResourceExplorerFullAccess.md") managed policy) get complete
  search results with automatic infrastructure creation on a
  Regional
  basis for indexes and views.
- **Enhanced Experience:** Users with only the
  permissions in the `AWSResourceExplorerReadOnlyAccess` managed policy get
  immediate access to partial results (all tagged resources and supported
  untagged resources created after the [immediate resource discovery](manage-immediate-resource-discovery-experience.md "manage-immediate-resource-discovery-experience.md") release).
- **No Access:** Users without the permissions
  in the `AWSResourceExplorerReadOnlyAccess` managed policy
  receive access denied errors, respecting IAM boundaries.

You can interact with Resource Explorer in the following ways:

**Resource Explorer console**

Resource Explorer provides a web-based user interface, the Resource Explorer console. Simply
navigating to or accessing the Resource Explorer console automatically triggers the
setup process based on your permissions. You can access the Resource Explorer console
by signing into the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") and
searching for it by name or choosing **View all services**
and selecting **Resource Explorer** from the list.

You can also navigate in your browser directly to the **[Resource Explorer home
page](https://console.aws.amazon.com/resource-explorer/home#/home "https://console.aws.amazon.com/resource-explorer/home#/home")**, or to the **[Resource search](https://console.aws.amazon.com/resource-explorer/home#/search "https://console.aws.amazon.com/resource-explorer/home#/search")** page. If you aren't
already signed in, then you're asked to do so before the console
appears.

###### Note

The Resource Explorer console is a _global_
console, meaning that you don't have to select an AWS Region to work
in. However, when you use Resource Explorer to create an index or a view, you need
to specify which Region the index or view is stored in. When you use
Resource Explorer to search, you can choose any view you have access to. The
results automatically come from the Region associated with the selected
view. If the view is from the Region that contains the aggregator index,
the results include resources from all Regions where you created Resource Explorer
indexes.

**AWS Management Console [Unified Search](../../../awsconsolehelpdocs/latest/gsg/using-search.md "../../../awsconsolehelpdocs/latest/gsg/using-search.md")**

At the top of every page in the AWS Management Console, there is a search bar. Resource Explorer
returns resource search results in Unified Search when you have the
appropriate permissions. You can use [Resource Explorer search query syntax](using-search-query-syntax.md "using-search-query-syntax.md") in
the Unified Search text box, and see matching resources in those search
results. You can search for resources from the console of any AWS service
without having to first switch to the Resource Explorer console.

###### Important

Unified Search uses the default view in the aggregator Region if
configured, or the default view in the current Region for regional
results.

**Resource Explorer commands in the AWS CLI and Tools for Windows PowerShell**

The AWS CLI and Tools for PowerShell provide direct access to the Resource Explorer public API
operations and automatically trigger setup based on your permissions when
you invoke search operations. These tools work on Windows, macOS, and Linux.
For more information about getting started, see the [AWS Command Line Interface User Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md"), or the [AWS Tools for Windows PowerShell User Guide](../../../powershell/latest/userguide.md "../../../powershell/latest/userguide.md"). For more information
about the commands for Resource Explorer, see the [AWS CLI Command
Reference](../../../cli/latest/reference/resource-explorer-2.md "../../../cli/latest/reference/resource-explorer-2.md") or the [AWS Tools for Windows PowerShell Cmdlet Reference](../../../powershell/latest/reference/index.md "../../../powershell/latest/reference/index.md").

**Resource Explorer operations in the AWS SDKs**

AWS provides API commands for a broad set of programming languages that
automatically enable Resource Explorer functionality when you have appropriate
permissions. For more information about getting started, see [Using AWS Resource Explorer with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").

**Query API**

If you don't use one of the supported programming languages, the Resource Explorer
HTTPS Query API gives you programmatic access to Resource Explorer. With the Resource Explorer
API, you can issue HTTPS requests directly to the service. When you use the
Resource Explorer API, you must include code that can digitally sign your requests
using your AWS credentials. For more information, see the [AWS Resource Explorer API Reference](../apireference.md "../apireference.md").

## Getting started immediately

You can start using Resource Explorer immediately with just the permissions in the `AWSResourceExplorerReadOnlyAccess` managed policy. This provides
instant access to search functionality with partial results while automatic setup
completes in the background.

###### Note

Automatic setup can complete only if you have the necessary permissions. You must
have, at minimum, the permissions in the `AWSResourceExplorerFullAccess` managed policy.

###### To start searching immediately

1. Ensure you have, at minimum, the permissions in the `AWSResourceExplorerReadOnlyAccess` managed policy. This
   permission is included in the `ResourceExplorerFullAccess` managed
   policy.
2. Navigate to the Resource Explorer console or use [Unified Search](../../../awsconsolehelpdocs/latest/gsg/using-search.md "../../../awsconsolehelpdocs/latest/gsg/using-search.md") from any AWS
   console page.
3. Begin searching immediately. You'll receive partial results (all tagged
   resources and supported untagged resources created after the [immediate resource discovery](manage-immediate-resource-discovery-experience.md "manage-immediate-resource-discovery-experience.md")
   release) while indexing completes.
4. (Optional) For complete results, obtain the
   `iam:CreateServiceLinkedRole` permission (included in the [AWSResourceExplorerFullAccess](../../../aws-managed-policy/latest/reference/AWSResourceExplorerFullAccess.md "../../../aws-managed-policy/latest/reference/AWSResourceExplorerFullAccess.md") managed policy). Once any user in
   your account creates the service-linked role, all users with search permission
   searching in a new Region can create an index and a view for full
   results.

## Enhanced setup for cross-Region search

While Resource Explorer provides immediate regional search functionality, you can optionally
configure enhanced features like cross-Region search and custom views.

- **Cross-Region search:** Create an aggregator
  index to search across all Regions from a single location.
- **Custom views:** Create filtered views for
  specific resource types or access control requirements.
- **Multi-account search:** Configure
  organization-wide resource discovery (requires management account or delegated
  administrator permissions).

For detailed setup instructions, see [Setting up and configuring Resource Explorer](getting-started-setting-up.md "getting-started-setting-up.md").
