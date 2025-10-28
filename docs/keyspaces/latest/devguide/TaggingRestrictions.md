# Restrictions for using tags to label resources in Amazon Keyspaces

Each tag consists of a key and a value, both of which you define. The following restrictions apply:

- Each Amazon Keyspaces keyspace, table, or stream can have only one tag with the same key. If you try
  to add an existing tag (same key), the existing tag value is updated to the new
  value.
- Tags applied to a keyspace don't automatically apply to tables within that keyspace.
  To apply the same tag to a keyspace and all its tables, each resource must be individually tagged.
- Tags applied to a table don't automatically apply to the stream of that table.
  To apply the same tags to a table and the stream during table creation, you can use the `PropagateTagsOnEnable` flag when you
  create the table. Using this flag, Amazon Keyspaces applies the tags of the table to the stream during stream creation. When the stream is active,
  changes to the table tags don't apply to the stream.
- When you create a multi-Region keyspace or table, any tags that you define during the creation process
  are automatically applied to all keyspaces and tables in all Regions. When you change existing tags
  using `ALTER KEYSPACE` or `ALTER TABLE`, the update is
  only applied to the keyspace or table in the Region where you're making the change.
- A value acts as a descriptor within a tag category (key). In Amazon Keyspaces the value cannot be empty or null.
- Tag keys and values are case sensitive.
- The maximum key length is 128 Unicode characters.
- The maximum value length is 256 Unicode characters.
- The allowed characters are letters, white space, and numbers, plus the following special
  characters: `+ - = . _ : /`
- The maximum number of tags per resource is 50.
- AWS-assigned tag names and values are automatically assigned the `aws:`
  prefix, which you can't assign. AWS-assigned tag names don't count toward the tag
  limit of 50. User-assigned tag names have the prefix `user:` in the cost
  allocation report.
- You can't backdate the application of a tag.
