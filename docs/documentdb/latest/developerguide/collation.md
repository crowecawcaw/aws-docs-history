# Using Collation in Amazon DocumentDB 8.0

Amazon DocumentDB 8.0 now supports collation. Collation allows you to configure language-specific rules for string comparison. With collation, you can specify rules for case-sensitive comparisons, or specify a language locale. Collation can be configured at the collection-level or index-level in DocumentDB 8.0.
When you use collation in DocumentDB, internally a collation document is created with the following parameters.

```

{
locale: string,
caseLevel: boolean,
caseFirst: string,
strength: int,
numericOrdering: boolean,
alternate: string,
maxVariable: string,
backwards: boolean,
normalization: boolean
}

```

## Limitations

Collation has following limitations in Amazon DocumentDB:

- Collation is compatible with planner v3 available in Amazon DocumentDB 8.0. Switching to plannerv2 or plannerv1 may cause inconsistent behaviors, including “Index not found“ errors.
- Due to inherent library differences, if a mongodb collection with collation is exported, you will need to update the metadata.bson files and change its version from 57.1 to 60.2 prior to migration.
- In rare cases, your collation settings may breach the internal limit on character count, causing the below error. "Error: Collation document has non-default attributes more than supported. Please reduce the number of options." In this case, try to reduce the options you provide in the collation document, or alternatively you could try and use default values wherever possible.
