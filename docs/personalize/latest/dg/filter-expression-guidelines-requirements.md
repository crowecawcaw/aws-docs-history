# Guidelines and requirements

When creating a filter expression, note the following guidelines and requirements:

- You can't use filters to include or exclude items based on unstructured textual item metadata such as product descriptions.
- If you are filtering based on item or action interactions data, you can only filter based on event type.
  You can't filter based on other interaction metadata, such as contextual metadata.
- Amazon Personalize ignores case only when matching event types.
- You can't use Item Interaction and Item datasets in one expression. To create a filter
  that filters by Interaction and then Item datasets (or the opposite), you must chain two
  or more expressions together. For more information, see [Combining multiple expressions](multiple-expression-example.md "multiple-expression-example.md").
- You can't use Item interaction and Action datasets in one expression. To create a filter
  that filters by Item interaction and then Action datasets (or the opposite), you must chain two
  or more expressions together. For more information, see [Combining multiple expressions](multiple-expression-example.md "multiple-expression-example.md").
- You can't use item interactions filters
  with the [Item-Attribute-Affinity recipe](item-attribute-affinity-recipe.md "item-attribute-affinity-recipe.md").
- You can't create filter expressions that filter using values with a boolean type in your schema.
  To filter based on boolean values, use a schema with a field of type _String_ and use the values `"True"` and `"False"`
  in your data. Or you can use type _int_ or _long_ and values `0` and `1`.
- The maximum number of distinct dataset fields for a filter, either in one expression or across multiple expressions chained together, is **10**. The maximum
  number of distinct dataset fields across all filters in a dataset group is **20**.
- You can apply a filter with the CurrentItem element only if your domain use case or custom recipe generates related items recommendations,
  such as the Similar-Items recipe or the _More Like X_ domain use case.
- You can't use placeholder parameters in a filter expression that uses the NOT_IN operator. Instead,
  use the IN operator and use the opposite Action. For example, use Include instead of Exclude (or the reverse).
- You can't create filters that filter based on `Action expiration timestamp` and
  `Repeat frequency` data. Amazon Personalize automatically filters action recommendations based on this data.
