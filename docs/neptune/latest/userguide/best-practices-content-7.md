# Avoid using the WITH clause when possible

The WITH clause in openCypher acts as a boundary where everything before it executes, and then the resulting values
are passed to the remaining portions of the query. The WITH clause is needed when you require interim aggregation
or want to limit the number of results, but aside from that you should try to avoid using the WITH clause. The
general guidance is to remove these simple WITH clauses (without aggregation, order by or limit) to enable the
query planner to work on the entire query to create a globally optimal plan. As an example, assume you wrote a query
to return all people living in `India`:

```
MATCH (person)-[:lives_in]->(city)
WITH person, city
MATCH (city)-[:part_of]->(country {name: 'India'})
RETURN collect(person) AS result
```

In the above version, the WITH clause restricts the placement of the pattern
`(city)-[:part_of]->(country {name: 'India'})` (which is more restrictive) before
`(person)-[:lives_in]->(city)`. This makes the plan sub-optimal. An optimization
on this query would be to remove the WITH clause and let the planner compute the best plan.

```
MATCH (person)-[:lives_in]->(city)
MATCH (city)-[:part_of]->(country {name: 'India'})
RETURN collect(person) AS result
```
