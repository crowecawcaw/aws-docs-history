# Creating user-owned indexes for enhanced

Resource Explorer functionality

AWS Resource Explorer automatically enables basic search functionality when you search with
appropriate permissions. However, you may need to manually complete setup in specific
scenarios, such as when you lack required permissions, have previously deleted an index in a
Region, or need to manage existing aggregator configurations. For enhanced functionality
like cross-Region search, you can use the **[Quick setup](getting-started-setting-up.md#getting-started-setting-up-quick "getting-started-setting-up.md#getting-started-setting-up-quick")** option or
one-click cross-Region banner to create indexes in all [AWS Regions that are turned on in your
AWS account](../../../general/latest/gr/rande-manage.md "../../../general/latest/gr/rande-manage.md"). When you use the Quick Setup option, Resource Explorer promotes the
specified Region to be the [aggregator index](manage-aggregator-region.md "manage-aggregator-region.md")
for the account. If you use the **[Advanced setup](getting-started-setting-up.md#getting-started-setting-up-advanced "getting-started-setting-up.md#getting-started-setting-up-advanced")**
option, you can specify the Regions in which to create indexes.

###### Topics

- [Create a Resource Explorer index in a Region](#manage-service-turn-on-region-region "#manage-service-turn-on-region-region")
- [Considerations for AWS opt-in
  Regions](opt-in-region-considerations.md "opt-in-region-considerations.md")
  When you complete setup for Resource Explorer in an AWS Region, the service performs the following
  actions:

- When the first user with appropriate permissions accesses Resource Explorer in the first
  Region in an AWS account, Resource Explorer automatically creates a [service-linked role in the account
  named AWSServiceRoleForResourceExplorer](security_iam_service-linked-roles.md "security_iam_service-linked-roles.md"). This role grants permissions for Resource Explorer to
  discover and index the resources in your account by using services such as AWS CloudTrail
  and the tagging service. Resource Explorer uses a service-linked channel to receive CloudTrail events
  on your behalf. Creation of the service-linked role happens only when you register
  the first AWS Region in the account. Resource Explorer uses the same service-linked role for
  all additional Regions that you add later.
- Resource Explorer automatically creates an index in the specified Region to store the details
  about that Region's resources. Once the service-linked role exists in the account,
  subsequent Regions are automatically enabled when users with search permissions
  invoke search operations in those Regions.
- Resource Explorer begins discovering the resources in the specified Region and adds the
  information it finds about them to that Region's index.
- If your account already contains [an
  aggregator index](manage-aggregator-region.md "manage-aggregator-region.md") in a different Region, Resource Explorer starts replicating the
  information from the new Region's index to the aggregator index to support
  cross-Region search.
  When those steps are complete, information about your resources is available to be
  discovered by users. They can search by using one of the [views](customer-views.md#configure-views "customer-views.md#configure-views") defined in either the same Region or the Region that contains the
  aggregator index.

## Create a Resource Explorer index in a Region

While Resource Explorer automatically enables basic search functionality, you may need to
manually create indexes in specific scenarios. The Resource Explorer console provides banner
notifications to guide you through setup completion, and you can access enhanced setup
options through the "Complete Setup" option in the left navigation or on the
**Settings** page.

Manual index creation is typically needed when:

- You lack the required `iam:CreateServiceLinkedRole` permission for
  automatic setup
- You previously deleted an index in a Region and want to restore full
  functionality
- You need to manage existing aggregator configurations or create cross-Region
  search capabilities
- You want enhanced control over index configuration and tagging

During manual setup, you may see indexing progress indicators in the console. A blue
banner displays "Completing AWS Resource Explorer setup" while indexing is in progress, which
changes to a green completion banner when setup is finished.

You can create a Resource Explorer index in an additional AWS Region by using the AWS Management Console, by
using commands in the AWS Command Line Interface (AWS CLI), or by using API operations in an AWS SDK. You
can create only one index in a Region.

**Minimum permissions**

To perform the steps in the following procedure, you must have the following
permissions:

- **Action**: `resource-explorer-2:*`
  – **Resource**: no specific resource
  (`*`)
- **Action**:
  `iam:CreateServiceLinkedRole` – **Resource**: no specific resource (`*`)

AWS Management Console

###### To create a Resource Explorer index in an AWS Region

1. **Primary method - Banner workflow:**
   If you see a **Complete setup and enable cross-Region
   search** banner, you can use these guided
   workflows:
   1. For cross-Region setup, choose **Enable
      cross-Region search in all Regions** in the
      banner

   -or-

   For customized setup, choose **Customize Region
   setup** to access enhanced configuration
   options.

2. **Alternative method - Settings
   page:** If banner workflows are not available or you
   need manual control:
   1. On the Resource Explorer **[Settings](https://console.aws.amazon.com/resource-explorer/home#/settings "https://console.aws.amazon.com/resource-explorer/home#/settings")** page.
   2. In the **Indexes** section, choose
      **Create indexes**.
   3. On the **Create indexes** page, select
      the check boxes next to the AWS Regions in which you want
      to create an index to support searching that Region's
      resources. Unavailable check boxes indicate Regions that
      already contain a user-owned index.
   4. (Optional) In the **Tags** section, you
      can specify tag key and value pairs to the index.
   5. Choose **Create indexes**.

   Resource Explorer displays a green banner at the top of the page to
   indicate success, or a red banner if there is an error
   creating an index in one or more of the selected
   Regions.

   ###### Note

   Tagged resources local to the index appear in search results
   within a few minutes. Untagged resources typically take less than two hours to appear, but can
   take longer when there is heavy demand. It can also can take up to an hour to complete the
   initial replication to a new aggregator index from all of the existing local indexes.

**Next step** – If you already [created an aggregator index](manage-aggregator-region.md "manage-aggregator-region.md"),
then the new Regions automatically begin to replicate their index
information to the aggregator index. If that is where your users do all of
their searching, then the resources in the new Region appear in those search
results and you're done.

However, if you want users to be able to search for resources in **_only_** the newly
indexed Region, then you can also create a view for users in that Region
and grant your users permissions to that view or users can search using the
service view in that Region.. For instructions on how to create a view, see
[Configuring a Resource Explorer view to provide access to
resource searches](customer-views.md#configure-views "customer-views.md#configure-views").

AWS CLI

###### To create a Resource Explorer index in an AWS Region

Run the following command for each AWS Region in which you want to
create an index to support searching that Region's resources. The
following example command registers Resource Explorer in the US East (N. Virginia)
(`us-east-1`).

```
`$` `aws resource-explorer-2 create-index \
 --region us-east-1`
`{
 "Arn": "arn:aws:resource-explorer-2:us-east-1:123456789012:index/1a2b3c4d-5d6e-7f8a-9b0c-abcd11111111",
 "CreatedAt": "2022-11-01T20:00:59.149Z",
 "State": "CREATING"
}`
```

Repeat this command for each Region in which you want to complete setup
for Resource Explorer, substituting the appropriate Region code for the
`--region` parameter.

Because Resource Explorer performs some of the index creation as asynchronous tasks
in the background, the response can be `CREATING`, which
indicates that the background processes are not yet complete.

###### Note

Tagged resources local to the index appear in search results
within a few minutes. Untagged resources typically take less than two hours to appear, but can
take longer when there is heavy demand. It can also can take up to an hour to complete the
initial replication to a new aggregator index from all of the existing local indexes.

You can check for final completion by running the following command, and
checking for the `ACTIVE` state.

```
`$` `aws resource-explorer-2 get-index \
 --region us-east-1``{
 "Arn": "arn:aws:resource-explorer-2:us-east-1:123456789012:index/1a2b3c4d-5d6e-7f8a-9b0c-abcd11111111",
 "CreatedAt": "2022-07-12T18:59:10.503000+00:00",
 "LastUpdatedAt": "2022-07-13T18:41:58.799000+00:00",
 "ReplicatingFrom": [],
 "State": "ACTIVE",
 "Tags": {},
 "Type": "LOCAL"
}`
```

**Next step** – If you already [created an aggregator index](manage-aggregator-region.md "manage-aggregator-region.md"),
then the new Regions automatically begin to replicate their index
information to the aggregator index. If that is where your users do all of
their searching, then the resources in the new Region appear in those search
results and you're done.

However, if you want users to be able to search for resources in **_only_** the newly
indexed Region, then you can also create a view for users in that Region
and grant your users permissions to that view or users can search using the
service view in that Region. For instructions on how to create a view, see
[Configuring a Resource Explorer view to provide access to
resource searches](customer-views.md#configure-views "customer-views.md#configure-views").
