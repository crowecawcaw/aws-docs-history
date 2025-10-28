# Specify edge labels where possible

It is recommended to provide an edge label where possible when specifying an edge in a pattern. Consider the
following example query, which is used to link all of the people living in a city with all of the people who
visited that city.

```
MATCH (person)-->(city {country: "US"})-->(anotherPerson)
RETURN person, anotherPerson
```

If your graph model links people to nodes other than just cities using multiple edge labels, by not specifying
the end label, Neptune will need to evaluate additional paths that will later be discarded. In the above query,
as an edge label was not given, the engine does more work first and then filters out values to obtain the correct
result. A better version of above query might be:

```
MATCH (person)-[:livesIn]->(city {country: "US"})-[:visitedBy]->(anotherPerson)
RETURN person, anotherPerson
```

This not only helps in evaluation, but enables the query planner to create better plans. You could even combine this
best practice with redundant node label checks to remove the city label check and write the query as:

```
MATCH (person)-[:livesIn]->({country: "US"})-[:visitedBy]->(anotherPerson)
RETURN person, anotherPerson
```
