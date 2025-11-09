# Tagging Basics for Amazon WorkSpaces Applications

Tags consist of a key-value pair, similar to other AWS services tags. To tag a
resource, you specify a _key_ and a _value_ for
each tag. A key can be a general category, such as "project", "owner", or "environment",
with specific associated values, and you can share the same key and value across
multiple resources. You can tag an WorkSpaces Applications resource immediately after you create it or
later on. If you delete a resource, the tags are removed from that resource on deletion.
However, other WorkSpaces Applications and AWS resources that have the same tag key are not
impacted.

You can edit tag keys and values, and you can remove tags from a resource at any time. You can set the value of a tag to an empty string, but you can't set the name of a tag to null. If you add a tag that has the same key as an existing tag on that resource, the new value overwrites the old value. If you delete a resource, any tags for the resource are also deleted.

###### Note

If you plan to set up a monthly cost allocation report to track AWS costs for WorkSpaces Applications resources, keep in mind that tags added to existing WorkSpaces Applications resources appear in your cost allocation report on the first of the following month for resources that are renewed in that month.
