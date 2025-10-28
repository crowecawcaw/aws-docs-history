# Item recommendation filter expression examples

The following filter expressions show how to filter item recommendations based on item interactions, item metadata, and
user metadata. They are organized by data type.

###### Topics

- [Item interaction data](#item-interaction-filter-examples "#item-interaction-filter-examples")
- [Item
  data](#item-filter-examples "#item-filter-examples")
- [User data](#user-filter-examples "#user-filter-examples")

## Item interaction data

The following expression excludes items based on an event type (such as click) or event types that you specify
when you get recommendations using the `$EVENT_TYPE` parameter.

```
EXCLUDE ItemID WHERE Interactions.EVENT_TYPE IN ($EVENT_TYPE)
```

The following expression excludes items that a user clicked or streamed.

```
EXCLUDE ItemID WHERE Interactions.EVENT_TYPE IN ("click", "stream")
```

The following expression includes only items that the user has clicked.

```
INCLUDE ItemID WHERE Interactions.EVENT_TYPE IN ("click")
```

## Item

data

The following expression excludes items based on a category or categories that you specify when you get
recommendations using the `$CATEGORY` parameter.

```
EXCLUDE ItemID WHERE Items.CATEGORY IN ($CATEGORY)
```

The following expression includes only items that are cheaper than the current item (the item you specify in the
request for related items recommendations), and created by the same studio as the current item. You can apply a filter
with the CurrentItem element only if your domain use case or custom recipe generates related items
recommendations.

```
INCLUDE ItemID WHERE Items.PRICE < CurrentItem.PRICE AND Items.GENRE IN CurrentItem.GENRE
```

The following expression excludes items based on multiple levels of categorical fields. It excludes items with a
CATEGORY_L1 value of `shoe` that _do not_ have a CATEGORY_L2 value of `boot`.

```
EXCLUDE ItemID WHERE Items.CATEGORY_L1 IN ("shoe") AND Items.CATEGORY_L2 NOT IN ("boot")
```

The following expression includes only items with a price less than or equal to the price that you specify when
you get recommendations using the `$PRICE` parameter.

```
INCLUDE ItemID WHERE Items.PRICE <= $PRICE
```

The following expression includes only items that have been created earlier than a timestamp (in Unix epoch time)
that you specify when you get recommendations.

```
INCLUDE ItemID WHERE Items.CREATION_TIMESTAMP < $DATE
```

The following expression includes only items with a genre or genres that you specify when you get recommendations
using the `$GENRE` parameter.

```
INCLUDE ItemID WHERE Items.GENRE IN ($GENRE)
```

The following expression includes only items that are more expensive than the current item
_and_ created more recently than a timestamp (in Unix epoch time) that you specify. You might use
this filter if you are getting related item recommendations, and want to apply some specific business rules based on
price and a varying creation date.

```
INCLUDE ItemID WHERE Items.PRICE < CurrentItem.PRICE AND Items.CREATION_TIMESTAMP > $DATE
```

## User data

The following expression excludes items with a genre or genres that you specify when you get recommendations using
the `$GENRE` parameter, but only if the current user's age is equal to the value that you specify when you
get recommendations using the `$AGE` parameter.

```
EXCLUDE ItemID WHERE Items.GENRE IN ($GENRE) IF CurrentUser.AGE = $AGE
```

The following expression includes only items with `watch` for CATEGORY_L1 and `luxury` for
CATEGORY_L2, if the current user's age is over `18`.

```
INCLUDE ItemID WHERE Items.CATEGORY_L1 IN ("watch") AND Items.CATEGORY_L2 IN ("luxury") IF CurrentUser.AGE > 18
```
