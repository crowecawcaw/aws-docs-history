AWS Resource Explorer now provides immediate access to resource search and
discovery capabilities in a Region. With this launch, you no longer need to activate
Resource Explorer to discover your resources. [Learn more](manage-immediate-resource-discovery-experience.md "manage-immediate-resource-discovery-experience.md")

# Setting a default view in an

AWS Region

In AWS Resource Explorer, you can define many views in an AWS Region, where each view addresses
different search requirements. We recommend that you set **_one_** view in each Region as the _default
view_ for that Region.

Resource Explorer automatically creates default user-owned views during setup that include Tags for
enhanced search functionality. If no user-owned view exists in a Region, Resource Explorer
automatically falls back to using a Resource Explorer-owned view to ensure search
functionality remains available. Resource Explorer-owned views are service-managed and
cannot be modified or deleted, and they do not include resource tags in search
results.

Resource Explorer uses the default view whenever a user performs a search and doesn't explicitly
specify which view to use. The [Unified Search](../../../awsconsolehelpdocs/latest/gsg/using-search.md "../../../awsconsolehelpdocs/latest/gsg/using-search.md") bar
at the top of every AWS Management Console page uses the default view in the aggregator Region if an
aggregator index exists, or the default view in the current Region if no aggregator is
configured. This provides regional search results without requiring cross-region
setup.

You can select only a view that exists in the Region to be that Region's default view. If
another Region has a view that you want to use, you must first create a copy of that view in
the Region in which you want to make it the default view.

###### Tip

There is no _copy view_ operation. You must create a
view in the target Region and then copy the settings from the existing view to the new
view.

You can specify a view as the default for its Region by using the AWS Management Console or by running AWS CLI commands or their equivalent API
operations in an AWS SDK.

AWS Management Console

###### To set a default view

1. On the Resource Explorer **[Views](https://console.aws.amazon.com/resource-explorer/home#/views "https://console.aws.amazon.com/resource-explorer/home#/views")** page, choose the option button next to the
   view that you want to make the default for its Region.
2. Choose **Actions**, then choose **Set as
   default** or set as default in
   the
   **Default** column.

AWS CLI

###### To set a default view

Run the following command to set the specified view as the default for its
Region. The following example sets the specified view to be the default for
all searches performed in the us-east-1 Region. That view must exist
in the Region in which you run the command.

```
`$` `aws resource-explorer-2 associate-default-view \
 --region us-east-1 \
 --view-arn arn:aws:resource-explorer-2:us-east-1:123456789012:view/MyViewName/1a2b3c4d-5d6e-7f8a-9b0c-abcd11111111``{
 "ViewArn": "arn:aws:resource-explorer-2:us-east-1:123456789012:view/MyViewName/1a2b3c4d-5d6e-7f8a-9b0c-abcd11111111"
}`
```
