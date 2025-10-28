# Filter expressions

To configure filters, you must use a properly formatted _filter expression_. Filter expressions are
composed of dataset and field identifiers in
`dataset`.`field` format, along with logical
operators, keywords, and values. For values, you can specify fixed values
or add placeholder parameters set the filter criteria when you get
recommendations.

You can use filter expressions to filter items, users, or actions from recommendations
based on data from the following datasets:

- **Item interactions**: You can use filter expressions to include or exclude items or users
  based on interactions data. For example, you can exclude items that a user has already clicked (for item recommendations), or include
  only users who have rated items (for the Item-Affinity recipe). For all recipe types, you
  can filter only based on event type. You can't filter based on other interaction metadata, such as contextual metadata. You can't use item interactions filters
  with the [Item-Attribute-Affinity recipe](item-attribute-affinity-recipe.md "item-attribute-affinity-recipe.md").

Amazon Personalize considers up to 100 of the most recent interactions per user per event type. This
is an adjustable quota. You can request a quota increase using the [Service
Quotas console](https://console.aws.amazon.com/servicequotas/ "https://console.aws.amazon.com/servicequotas/"). If you don't import item interactions for a user for three months, your filters no longer
consider the user's historical data. To consider this data, you must import the user's entire event history again.

- **Action interactions**: Use filter
  expressions to include or exclude actions that a user has interacted
  with based on event type. For example, you might exclude actions that a user has already taken. You can't filter based on
  other action interaction metadata.

Amazon Personalize considers up to 300
of the most recent action interactions per user per event type.
This is an adjustable quota.
You can request a quota increase using the [Service Quotas console](https://console.aws.amazon.com/servicequotas/ "https://console.aws.amazon.com/servicequotas/").

- **Items**: Use filter expressions to include or exclude items based on specific item
  conditions. You can't use filters to include or exclude items based on unstructured textual item metadata such as
  product descriptions. If your domain use case or custom recipe generates related items recommendations,
  such as the Similar-Items recipe or the _More Like X_ domain use case,
  you can use filter expressions to include or exclude items based on the properties of the item you specify in your recommendation request.
- **Users**: For _item_ and _action_ recommendations,
  if you have a Users dataset, you can exclude or include items or actions based on a `CurrentUser`. For
  personalized recommendations, popular items, and action recommendations, this is the user you are getting
  recommendations for. For related items, this an optional user you can specify in your recommendation request.

For _user segments_, you can use filter expressions to include or exclude users from user
segments based on attributes, such as `Users.MEMBERSHIP_STATUS`.

- **Actions**: Use filter expressions to include or exclude actions based on specific action
  conditions. Amazon Personalize automatically excludes actions based on `Action expiration timestamp` and
  `Repeat frequency` data. You can't create additional custom filters that filter based on this data.
  For a complete list of filter expression elements, see [Filter expression elements](creating-filter-expressions.md#filter-expression-elements "creating-filter-expressions.md#filter-expression-elements"). For examples of filter
  expressions, see [Filter expression examples](filter-expression-examples.md "filter-expression-examples.md").

###### Topics

- [Guidelines and requirements](filter-expression-guidelines-requirements.md "filter-expression-guidelines-requirements.md")
- [Filter expression structure and elements](creating-filter-expressions.md "creating-filter-expressions.md")
- [Filter expression examples](filter-expression-examples.md "filter-expression-examples.md")
