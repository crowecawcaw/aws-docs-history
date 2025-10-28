AWS Resource Explorer now provides immediate access to resource search and
discovery capabilities in a Region. With this launch, you no longer need to activate
Resource Explorer to discover your resources. [Learn more](manage-immediate-resource-discovery-experience.md "manage-immediate-resource-discovery-experience.md")

# Setting up and configuring Resource Explorer

AWS Resource Explorer is available immediately when you have the appropriate permissions. Users with,
at minimum, the permissions in the `AWSResourceExplorerReadOnlyAccess` managed policy can start searching
for resources right away without any setup. Users with the permissions in the `AWSResourceExplorerReadOnlyAccess` managed policy and
`iam:CreateServiceLinkedRole` permissions (included in the [AWSResourceExplorerFullAccess](../../../aws-managed-policy/latest/reference/AWSResourceExplorerFullAccess.md "../../../aws-managed-policy/latest/reference/AWSResourceExplorerFullAccess.md") managed policy) get complete search results with
automatic infrastructure creation on first search.

###### Note

After the service-linked role is created in your account when any user with the
`iam:CreateServiceLinkedRole` permission accesses Resource Explorer, subsequent
users need only, at minimum, the permissions in the `AWSResourceExplorerReadOnlyAccess` managed policy to create an
index and view for full results in a Region on first search.

Your search experience is automatically enabled based on your IAM permissions. For
enhanced functionality like cross-Region search, multi-account configurations, or more
control over your Resource Explorer configuration, you can use the manual setup options below.

Quick Setup and Advanced Setup options remain available for customers who want
cross-Region search or more control over their Resource Explorer configuration.

###### Note

Multi-account search requires that your account is part of an AWS Organizations organization.

There are two ways to enhance your Resource Explorer configuration:

- [Enable
  Cross-Region Search](#getting-started-setting-up-quick "#getting-started-setting-up-quick")
- [Enhanced
  Configuration Options](#getting-started-setting-up-advanced "#getting-started-setting-up-advanced")

###### Important

If you choose to create user-owned indexes using any option that says "all
AWS Regions", it creates indexes only in those AWS Regions that exist and that are
[enabled in the
AWS account](../../../general/latest/gr/rande-manage.md#rande-manage-enable "../../../general/latest/gr/rande-manage.md#rande-manage-enable")
_at the time you perform the procedure_. User-owned
indexes are **_not_**
automatically created in any AWS Regions that AWS adds in the future. When AWS
introduces a new Region, you can choose to create user-owned indexes in the Region
manually when it appears in the **[Settings](https://console.aws.amazon.com/resource-explorer/home#/settings "https://console.aws.amazon.com/resource-explorer/home#/settings")** page of the Resource Explorer console, or by calling
the [CreateIndex](../apireference/API_CreateIndex.md "../apireference/API_CreateIndex.md") operation.

###### Note

Configuring Resource Explorer can enhance the ability to search for resources using the
[Unified Search](../../../awsconsolehelpdocs/latest/gsg/using-search.md "../../../awsconsolehelpdocs/latest/gsg/using-search.md") bar on the AWS Management Console. Unified Search works with local Region
indexes and does not require an aggregator index. For cross-Region search capabilities,
you can optionally configure an aggregator index and default view. For more information,
see [Using Unified Search in the AWS Management Console](using-unified-search.md "using-unified-search.md").

## Enabling cross-Region search

To enable cross-Region search capabilities, you can complete setup to create
user-owned indexes and configure an aggregator index. This procedure does the
following:

- Creates user-owned indexes in every AWS Region in your AWS account for
  complete search results.
- Updates the index in the Region you specify to be the aggregator index for the
  account.
- Creates a default view in the aggregator index Region. This view has no filters so it
  returns all resources found in the index.

**Minimum permissions**

To perform the steps in the following procedure, you must have the following
permissions:

- **Action**: `resource-explorer-2:*`
  – **Resource**: no specific resource
  (`*`)
- **Action**:
  `iam:CreateServiceLinkedRole` – **Resource**: no specific resource (`*`)

AWS Management Console

###### To enable cross-Region search

1. Open the [AWS Resource Explorer console](https://console.aws.amazon.com/resource-explorer "https://console.aws.amazon.com/resource-explorer") at [https://console.aws.amazon.com/resource-explorer](https://console.aws.amazon.com/resource-explorer "https://console.aws.amazon.com/resource-explorer").
2. If you see the **Complete setup and enable cross-Region
   search** banner, proceed to the next step. Otherwise,
   navigate to **Settings** to access setup options.
   You can also access **Complete Setup** from the
   left navigation when available.
3. In the **Complete setup and enable cross-Region
   search** banner, select your preferred aggregator index
   from the list. Choose the Region that is appropriate for the
   geographic location of your users.
4. Choose **Enable cross-Region search in all
   Regions**. Alternatively, you can choose
   **Customize Region setup** for more granular
   control over which Regions to include.
5. Monitor the indexing progress.
6. Wait for the setup to complete. The indexing process creates
   user-owned indexes in all or selected Regions and configures the
   aggregator index in your selected Region.

After setup completes, you and your users can search for resources across
all Regions. The cross-Region search capability will be fully available
after indexing is complete.

###### Note

Tagged resources local to the index appear in search results
within a few minutes. Untagged resources typically take less than two hours to appear, but can
take longer when there is heavy demand. It can also can take up to an hour to complete the
initial replication to a new aggregator index from all of the existing local indexes.

**Next steps:** Before your users can search
with the default view you just created, you must grant them permissions to
search with it. For more information, see [Granting access to Resource Explorer views for
search](configure-views-grant-access.md "configure-views-grant-access.md").

AWS CLI
Setting up Resource Explorer in your AWS account by using the AWS CLI is, by
definition, equivalent to the **Advanced setup** option.
This is because the Resource Explorer CLI operations don't perform any of the steps for
you automatically like the Resource Explorer console does. See the AWS CLI tab on the
[Using enhanced configuration
options](#getting-started-setting-up-advanced "#getting-started-setting-up-advanced") to see what
commands are the equivalent of using the console.

## Using enhanced configuration

options

For more granular control over your Resource Explorer configuration, you can use Advanced setup
options to:

- Choose the AWS Regions in which to create user-owned indexes for complete
  search results.
- Choose whether to configure one Region with an [aggregator index](getting-started-terms-and-concepts.md#term-index "getting-started-terms-and-concepts.md#term-index"). If you do, you specify the AWS Region to place
  it in. This index allows you to create views that can include resources from all
  Regions in the account. For more information, see [Enabling cross-Region search by creating
  an aggregator index](manage-aggregator-region.md "manage-aggregator-region.md").
- Choose whether to create a default view. That view allows searching
  automatically for any AWS resource in the Regions where you have user-owned
  indexes. You must ensure that any principals who need to use the default view to
  search in Resource Explorer have permissions on the view. For more information, see [Granting access to Resource Explorer views for
  search](configure-views-grant-access.md "configure-views-grant-access.md").

**Minimum permissions**

To perform the steps in the following procedure, you must have the following
permissions:

- **Action**: `resource-explorer-2:*`
  – **Resource**: no specific resource
  (`*`)
- **Action**:
  `iam:CreateServiceLinkedRole` – **Resource**: no specific resource (`*`)

AWS Management Console

###### To configure Resource Explorer with enhanced options

1. Open the [AWS Resource Explorer console](https://console.aws.amazon.com/resource-explorer "https://console.aws.amazon.com/resource-explorer") at [https://console.aws.amazon.com/resource-explorer](https://console.aws.amazon.com/resource-explorer "https://console.aws.amazon.com/resource-explorer").
2. Navigate to **Settings** to access enhanced
   configuration options, or choose **Customize Region
   setup** from the cross-Region setup banner. You can
   also access **Complete Setup** from the left
   navigation when available.
3. Select the specific Regions where you want to create user-owned
   indexes, or configure custom view settings as needed.
4. If enabling cross-Region search, review the "Confirm cross-Region
   setup" modal that explains: "By enabling cross-Region search, AWS
   performs the following steps:" followed by details about creating
   indexes in all AWS Regions, creating the aggregator index, and
   creating default view with filter.
5. Choose **Cancel** to return to the previous
   screen, or **Confirm and enable** to proceed with
   the cross-Region setup.
6. Monitor the setup progress and wait for indexing to complete. To
   continue using Resource Explorer with partial results during this process,
   choose **Proceed to Resource Search**.

AWS CLI

###### To set up Resource Explorer using Advanced setup

The Resource Explorer console performs many API operation calls on your behalf
based on the choices you make. The following example AWS CLI commands
illustrate how to perform the same basic procedures outside of the
console using the AWS CLI.

###### Example Step 1: Create user-owned indexes in the desired

AWS Regions

Run the following command in each AWS Region in which you want to
activate Resource Explorer. The following example command enables Resource Explorer in the
AWS Region that is the default for the AWS CLI.

```
`$` `aws resource-explorer-2 create-index`
`{
 "Arn": "arn:aws:resource-explorer-2:us-east-1:123456789012:index/1a2b3c4d-5d6e-7f8a-9b0c-abcd11111111",
 "CreatedAt": "2022-07-27T16:17:12.130000+00:00",
 "State": "CREATING"
}`
```

###### Example Step 2: Update the index in one AWS Region to be the aggregator

index for the account

Run the following command in the AWS Region in which you want Resource Explorer
to update the local index to the aggregator index for the account. The
following example command updates the aggregator index in the
US East (N. Virginia) (`us-east-1`).

```
`$` `aws resource-explorer-2 update-index-type \
 --arn arn:aws:resource-explorer-2:us-east-1:123456789012:index/1a2b3c4d-5d6e-7f8a-9b0c-abcd11111111 \
 --type AGGREGATOR`
`{
 "Arn": "arn:aws:resource-explorer-2:us-east-1:123456789012:index/1a2b3c4d-5d6e-7f8a-9b0c-abcd11111111",
 "LastUpdatedAt": "2022-07-27T16:29:49.231000+00:00",
 "State": "UPDATING",
 "Type": "AGGREGATOR"
}`
```

###### Example Step 3: Create a view in the AWS Region that contains the

aggregator index

Run the following command in the AWS Region in which you created the
aggregator index. The following example command creates a view identical
to the one created by the Resource Explorer console setup process. This new view
includes tags attached to the resource as part of the indexed
information and supports searching for resources by tag key or value.

```
`$` `aws resource-explorer-2 create-view \
 --view-name My-New-View \
 --included-properties Name=tags``{
 "View": {
 "Filters": {
 "FilterString": ""
 },
 "IncludedProperties": [
 {
 "Name": "tags"
 }
 ],
 "LastUpdatedAt": "2022-07-27T16:34:14.960000+00:00",
 "Owner": "123456789012",
 "Scope": "arn:aws:iam::123456789012:root",
 "ViewArn": "arn:aws:resource-explorer-2:us-east-1:123456789012:view/My-New-View/1a2b3c4d-5d6e-7f8a-9b0c-abcd22222222"
 }
}`
```

###### Example Step 4: Set your new view as the default for its AWS Region

The following example sets the view you created in the previous step
as the default for the Region. You must run the following command in the
same AWS Region in which you created the default view.

```
`$` `aws resource-explorer-2 associate-default-view \
 --view-arn arn:aws:resource-explorer-2:us-east-1:123456789012:view/My-New-View/1a2b3c4d-5d6e-7f8a-9b0c-abcd11111111``{
 "ViewArn": "arn:aws:resource-explorer-2:us-east-1:123456789012:view/My-New-View/1a2b3c4d-5d6e-7f8a-9b0c-abcd11111111"
}`
```

Before your users can search with a view, you must grant them
permissions to use that view. For more information, see [Granting access to Resource Explorer views for
search](configure-views-grant-access.md "configure-views-grant-access.md").

After you run those commands, Resource Explorer is running in the specified Regions
in your AWS account. Resource Explorer builds and maintains an index in each Region
with details of the resources located there. Resource Explorer replicates each of the
individual Region indexes to the aggregator index in the specified Region.
That Region also contains a view that allows any IAM role or user in the
account to search for resources across all indexed Regions.

###### Note

Tagged resources local to the index appear in search results
within a few minutes. Untagged resources typically take less than two hours to appear, but can
take longer when there is heavy demand. It can also can take up to an hour to complete the
initial replication to a new aggregator index from all of the existing local indexes.
