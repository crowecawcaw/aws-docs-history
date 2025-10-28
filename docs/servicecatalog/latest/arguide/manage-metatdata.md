# Viewing attribute group metadata

An attribute group is an open JSON object
where you define the metadata
for a resource.
Metadata is data
that describes other data.
For more information,
see [Attribute groups](overview-appreg.md#attr-groups "overview-appreg.md#attr-groups") on [Overview of AWS Service Catalog AppRegistry](overview-appreg.md "overview-appreg.md").

###### To view attribute group metadata

1. Open the AWS Service Catalog console
   at [https://console.aws.amazon.com/servicecatalog/](https://console.aws.amazon.com/servicecatalog/ "https://console.aws.amazon.com/servicecatalog/")
2. From the navigation pane,
   choose **AppRegistry**,
   and then choose **Attribute groups**.
   You're directed
   to the **Attribute groups** screen
   where you can view all
   of your attribute groups.
3. On **Attribute groups**,
   choose the name
   of the attribute groups
   that you want
   to view.
   Or select the attribute group
   that you want
   to edit,
   and then choose **View**.
   You're directed
   to the **Attribute group details** screen.
4. On **Attribute group details**,
   choose **Metadata**.

**Example: Attribute group metadata**

```
{
 "Team" : "WebTeam",
 "Department": "10006",
 "ParentDept": "Research",
 "ContactAlias": "research@team.com"
}
```
