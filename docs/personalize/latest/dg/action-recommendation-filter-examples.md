# Action recommendation filter expression examples

The following filter expression examples show how to filter actions based on action interactions data, action data.
and user data.
They are organized by data type.

###### Topics

- [Action interaction data](#action-interaction-filter-examples "#action-interaction-filter-examples")
- [Action data](#action-filter-examples "#action-filter-examples")
- [User data](#user-action-filter-examples "#user-action-filter-examples")

## Action interaction data

The following filter expression includes only actions in recommendations that the user has interacted with, when those interactions
have an event type that you specify when you get recommendations.

```
INCLUDE ActionID WHERE Action_Interactions.EVENT_TYPE IN ($EVENT_TYPE)
```

The following filter expression excludes actions that the user has not taken based on event type.

```
EXCLUDE ActionID WHERE Action_Interactions.EVENT_TYPE IN ("NOT_TAKEN")
```

## Action data

The following expression excludes actions based on a category or categories that you specify when you get
recommendations using the `$CATEGORY` parameter.

```
EXCLUDE ActionID WHERE Actions.CATEGORY IN ($CATEGORY)
```

The following expression includes only actions with a value greater than a value that you specify when you get
recommendations.

```
INCLUDE ActionID WHERE Actions.VALUE > ($VALUE)
```

## User data

The following expression includes only actions for premium members if the current user has a premium membership.

```
INCLUDE ActionID WHERE Action.MEMBERSHIP_LEVEL IN ("Premium") IF CurrentUser.MEMBERSHIP = $PREMIUM
```

The following expression excludes actions with a `VALUE` less than a value that you specify when you get recommendations
if the current user is a premium member.

```
EXCLUDE ActionID WHERE Actions.VALUE < ($VALUE) IF CurrentUser.MEMBERSHIP = $PREMIUM
```
