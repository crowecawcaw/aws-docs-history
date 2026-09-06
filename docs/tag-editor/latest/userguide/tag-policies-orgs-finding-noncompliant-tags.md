

# Evaluating compliance for an account
<a name="tag-policies-orgs-finding-noncompliant-tags"></a>

You can evaluate the compliance of an account in your organization with its effective tag policy.

**Important**  
Untagged resources don't appear as noncompliant in results.  
To find untagged resources in your account, use AWS Resource Explorer with a query that uses **tag:none**. For more information, see [Search for untagged resources](https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-examples.html#example-1) in the *AWS Resource Explorer User Guide*.

The *[effective tag policy](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies-effective.html)* specifies the tagging rules that apply to an account. The effective tag policy is the aggregation of any tag policies that the account inherits, plus any tag policy directly attached to the account. When you attach a tag policy to the organization root, it applies to all accounts in your organization. When you attach a tag policy to an organizational unit (OU), it applies to all accounts and OUs that belong to the OU.

**Note**  
If you haven't yet created tag policies, see [Getting started with tag policies](https://docs.aws.amazon.com/organizations/latest/userguide/tag-policies-getting-started.html) in the *AWS Organizations User Guide*.

To find noncompliant tags, you must have the following permissions:
+ `organizations:DescribeEffectivePolicy`
+ `tag:GetResources`
+ `tag:TagResources`
+ `tag:UntagResources`

**To evaluate an account's compliance with its effective tag policy (console)**

1. While signed in to the account whose compliance you want to check, open the [Tag Policies console](https://console.aws.amazon.com/resource-groups/tag-policies/).

1. The **Effective tag policy** section shows when the policy was last updated and the defined tag keys. You can expand a tag key to see information about its values, case treatment, and whether the values are enforced for specific resources types.
**Note**  
If you're signed in to the management account, you need to choose an account to see its effective policy and view compliance information.

1. In the **Resources with noncompliant tags** section, specify which AWS Region to search for noncompliant tags. Optionally, you can also search by resource type. Then choose **Search resources**.

   Real-time results are shown in the **Search results** section. To change the number of results returned per page or the columns to display, choose the settings icon. 

1. In the search results, select a resource with noncompliant tags.

1. In the dialog box that lists the resource's tags, choose the hyperlink to open the AWS service where the resource was created. From that console, correct the noncompliant tag.
**Tip**  
If you're not sure which tags are noncompliant, go to the **Effective tag policy** section for the account in the Tag Policies console. You can expand a tag key to view its tagging rules. 

1. Repeat the process of finding and correcting tags until the account resources that you care about are compliant in each Region.

**To find noncompliant tags (AWS CLI, AWS API)**  
Use the following commands and operations to find noncompliant tags:
+ AWS Command Line Interface (AWS CLI):
  + [aws resourcegroupstaggingapi get-resources](https://docs.aws.amazon.com/cli/latest/reference/resourcegroupstaggingapi/get-resources.html)
  + [aws resourcegroupstaggingapi tag-resources](https://docs.aws.amazon.com/cli/latest/reference/resourcegroupstaggingapi/tag-resources.html)
  + [aws resourcegroupstaggingapi untag-resources](https://docs.aws.amazon.com/cli/latest/reference/resourcegroupstaggingapi/untag-resources.html)

  For the complete procedure for using tag policies in the AWS CLI, see [Using tag policies in the AWS CLI](https://docs.aws.amazon.com/organizations/latest/userguide/tag-policy-cli.html) in the *AWS Organizations User Guide*.
+ AWS Resource Groups Tagging API:
  + [GetResources](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetResources.html)
  + [TagResources](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_TagResources.html)
  + [UntagResources](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_UntagResources.html)

**Next steps**  
 We recommend that you repeat the process of finding and correcting compliance issues. Continue until the account's resources that you care about are compliant with the effective tag policy in each Region.

Finding and correcting noncompliant tags is an iterative process for multiple reasons, including the following:
+ Your organization's use of tag policies can evolve over time.
+ It takes time to effect change in your organization when creating resources.
+ Compliance can change anytime that a new resource is created or when new tags are assigned to a resource. 
+ An account's effective tag policy is updated whenever a tag policy is attached to or detached from it. The effective tag policy is also updated whenever changes occur to tag the policies that the account inherits.

If you're signed in as the management account in the organization, you can also generate a report. This report shows information about all tagged resources in your organization's accounts. For more information, see [Evaluating organization-wide compliance](tag-policies-orgs-evaluating-org-wide-compliance.md).