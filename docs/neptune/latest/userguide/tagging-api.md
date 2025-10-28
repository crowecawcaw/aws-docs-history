# Tagging in Neptune using the API

You can add, list, or remove tags for a DB instance using the Neptune API.

- To add a tag to a Neptune resource, use the [`AddTagsToResource`](API_AddTagsToResource.md "API_AddTagsToResource.md") operation.
- To list tags that are assigned to a Neptune resource, use the [`ListTagsForResource`](API_ListTagsForResource.md "API_ListTagsForResource.md").
- To remove tags from a Neptune resource, use the [`RemoveTagsFromResource`](API_RemoveTagsFromResource.md "API_RemoveTagsFromResource.md") operation.
  To learn more about how to construct the required ARN, see [Constructing an ARN for Neptune](tagging-arns-constructing.md "tagging-arns-constructing.md").

When working with XML using the Neptune API, tags use the following schema:

```
<Tagging>
    <TagSet>
        <Tag>
            <Key>Project</Key>
            <Value>Trinity</Value>
        </Tag>
        <Tag>
            <Key>User</Key>
            <Value>Jones</Value>
        </Tag>
    </TagSet>
</Tagging>
```

The following table provides a list of the allowed XML tags and their characteristics.
Values for `Key` and `Value` are case-dependent. For example,
`project=Trinity` and `PROJECT=Trinity` are two distinct tags.

| Tagging Element | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `TagSet`        | A tag set is a container for all tags that are assigned to a Neptune resource. There can be only one tag set per resource. You work with a `TagSet` only through the Neptune API.                                                                                                                                                                                                                                                                                                                                   |
| `Tag`           | A tag is a user-defined key-value pair. There can be from 1 to 50 tags in a tag set.                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `Key`           | A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and cannot be prefixed with "`rds:`" or "`aws:`". The string can contain only the set of Unicode letters, digits, white space, '\_', '.', '/', '=', '+', '-' (Java regex: "`^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$`"). Keys must be unique to a tag set. For example, you can't have a key-pair in a tag set with the key the same but with different values, such as `project/Trinity` and `project/Xanadu`. |
| Value           | A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and cannot be prefixed with "`rds:`" or "`aws:`". The string can contain only the set of Unicode letters, digits, white space, '\_', '.', '/', '=', '+', '-' (Java regex: "`^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$`"). Values don't have to be unique in a tag set and can be null. For example, you can have a key-value pair in a tag set of `project/Trinity` and `cost-center/Trinity`.                |
