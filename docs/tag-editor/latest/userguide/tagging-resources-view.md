# View and edit existing tags for a selected

resource

Tag Editor shows you the existing tags on selected resources that are in the results of
your **Find resources to tag** query.

If you enabled any **Tag** columns as described in the previous
section, you can see the current value of that tag for each resource in the search
results.

###### Note

This topic explains how to edit the tag for an _individual_ resource. You can also bulk edit tags for several
selected resources at the same time. For more information, see [Managing tags with Tag Editor](tagging-resources.md "tagging-resources.md").

###### To edit tags inline in the search results table

1. Choose the value for the tag on the resource that you want to edit.

###### Note

    * If the chosen resource currently does not have a tag with the
     chosen key, the value displays as **(not
     tagged)**.
    * If the chosen resource does have a tag with the chosen key but
     without a value, the value displays as
     '**–**'.

2. You can enter a new value or choose from any of the values already present on
   other resources with this tag. You can also delete the tag from this one
   resource by choosing **Remove tag**.

###### To view all tags for an individual resource

1. In the results of your **Find resources to tag** query,
   choose the number in the **Tags** column for any resource for
   which you want to view existing tags. Resources with a dash in the
   **Tags** column do not have existing tags.
2. View existing tags in **Resource tags**. You can also open
   this window by choosing **Manage tags of selected resources**,
   when you're changing or removing tags from the **Manage tags**
   page.

###### Note

If you don’t see a tag that you recently applied to a resource, try
refreshing your browser window.

## Export results to .csv file

You can export the results of a **Find resources to tag** query to a
comma-separated values (.csv) file. The .csv file includes the resource names, services,
Region, resource IDs, the total number of tags, and a column for each unique tag key in
the collection. The .csv file can help you develop a tagging strategy for resources in
your organization, or determine where there are overlaps or inconsistencies in tagging
across resources.

1. In the results of your **Find resources to tag** query,
   choose **Export resources to CSV**.
2. When you're prompted by your browser, choose to open the .csv file, or save it
   to a convenient location.
