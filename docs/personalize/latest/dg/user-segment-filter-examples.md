# User segment filter expressions

The following filter expressions show how to filter user segments based on item interactions data and user metadata. They
are organized by data type.

**User data**

The following filter expression includes only users with a membership status equal to the value that you specify
when you get user segments.

```
INCLUDE UserID WHERE Users.MEMBERSHIP_STATUS IN ($MEMBERSHIP)
```

The following filter expression excludes users with an `AGE` less than a value you specify when you get
user segments.

```
EXCLUDE UserID WHERE Users.AGE < $AGE
```

**Item interaction data**

The following filter expression includes only users who have clicked or rated items.

```
INCLUDE UserID WHERE Interactions.EVENT_TYPE IN ("click", "rating")
```

The following filter expression excludes users from user segments who have item interactions with an event type you
specify when you get user segments.

```
EXCLUDE UserID WHERE Interactions.EVENT_TYPE IN ($EVENT_TYPE)
```
