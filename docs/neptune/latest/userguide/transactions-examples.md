# Examples of Neptune transaction semantics

The following examples illustrate different use cases for transaction semantics in
Amazon Neptune.

###### Topics

- [Conditional
  Insertion of a Property](#transactions-examples-conditional-insertion "#transactions-examples-conditional-insertion")
- [Property Value
  Uniqueness](#transactions-examples-unique-property "#transactions-examples-unique-property")
- [Conditional Property
  Change](#transactions-examples-conditional-edit "#transactions-examples-conditional-edit")
- [Replacing a Property](#transactions-examples-replace "#transactions-examples-replace")
- [Avoiding Dangling
  Elements](#transactions-examples-dangling "#transactions-examples-dangling")

## Example 1 – Inserting a

Property Only If It Does Not Exist

Suppose that you want to ensure that a property is set only once. For example, suppose
that multiple queries are trying to assign a person a credit score concurrently. You only want
one instance of the property to be inserted, and the other queries to fail because the
property has already been set.

```
# GREMLIN:
g.V('person1').hasLabel('Person').coalesce(has('creditScore'), property('creditScore', 'AAA+'))

# SPARQL:
INSERT { :person1 :creditScore "AAA+" .}
WHERE  { :person1 rdf:type :Person .
         FILTER NOT EXISTS { :person1 :creditScore ?o .} }
```

The Gremlin `property()` step inserts a property with the given
key and value. The `coalesce()` step executes the first argument
in the first step, and if it fails, then it executes the second step:

Before inserting the value for the `creditScore` property for a given
`person1` vertex, a transaction must try to read the possibly non-existent
`creditScore` value for `person1`. This attempted read locks the
`SP` range for `S=person1` and `P=creditScore` in the
`SPOG` index where the `creditScore` value either exists or will be
written.

Taking this range lock prevents any concurrent transaction from inserting a
`creditScore` value concurrently. When there are multiple parallel
transactions, at most one of them can update the value at a time. This rules
out the anomaly of more than one `creditScore` property being
created.

## Example 2 – Asserting That a

Property Value Is Globally Unique

Suppose that you want to insert a person with a Social Security number as a primary key.
You would want your mutation query to guarantee that, at a global level, no one else in the
database has that same Social Security number:

```
# GREMLIN:
g.V().has('ssn', 123456789).fold()
  .coalesce(__.unfold(),
            __.addV('Person').property('name', 'John Doe').property('ssn', 123456789'))

# SPARQL:
INSERT { :person1 rdf:type :Person .
         :person1 :name "John Doe" .
         :person1 :ssn 123456789 .}
WHERE  { FILTER NOT EXISTS { ?person :ssn 123456789 } }
```

This example is similar to the previous one. The main difference is that the range
lock is taken on the `POGS` index rather than the `SPOG` index.

The transaction executing the query must read the pattern, `?person :ssn 123456789`,
in which the `P` and `O` positions are bound. The range lock is
taken on the `POGS` index for `P=ssn` and `O=123456789`.

- If the pattern does exist, no action is taken.
- If it does not exist, the lock prevents any concurrent transaction from inserting that Social
  Security number also

## Example 3 – Changing a

Property If Another Property Has a Specified Value

Suppose that various events in a game move a person from level one to level two, and
assign them a new `level2Score` property set to zero. You need to be sure that
multiple concurrent instances of such a transaction could not create multiple instances of the
level-two score property. The queries in Gremlin and SPARQL might look like the
following.

```
# GREMLIN:
g.V('person1').hasLabel('Person').has('level', 1)
 .property('level2Score', 0)
 .property(Cardinality.single, 'level', 2)

# SPARQL:
DELETE { :person1 :level 1 .}
INSERT { :person1 :level2Score 0 .
         :person1 :level 2 .}
WHERE  { :person1 rdf:type :Person .
         :person1 :level 1 .}
```

In Gremlin, when `Cardinality.single` is specified, the
`property()` step either adds a new property or replaces an existing property
value with the new value that is specified.

Any update to a property value, such as increasing the `level` from 1 to 2,
is implemented as a deletion of the current record and insertion of a new record with the new
property value. In this case, the record with level number 1 is deleted and a record with
level number 2 is reinserted.

For the transaction to be able to add `level2Score` and update the
`level` from 1 to 2, it must first validate that the `level` value is
currently equal to 1. In doing so, it takes a range lock on the `SPO` prefix for
`S=person1`, `P=level`, and `O=1` in the `SPOG`
index. This lock prevents concurrent transactions from deleting the version 1 triple, and as a
result, no conflicting concurrent updates can happen.

## Example 4 – Replacing an Existing

Property

Certain events might update a person's credit score to a new value (here
`BBB`). But you want to be sure that concurrent events of that type can't create
multiple credit score properties for a person.

```
# GREMLIN:
g.V('person1').hasLabel('Person')
 .sideEffect(properties('creditScore').drop())
 .property('creditScore', 'BBB')

# SPARQL:
DELETE { :person1 :creditScore ?o .}
INSERT { :person1 :creditScore "BBB" .}
WHERE  { :person1 rdf:type :Person .
         :person1 :creditScore ?o .}
```

This case is similar to example 3, except that instead of locking the
`SPO` prefix, Neptune locks the `SP` prefix with
`S=person1` and `P=creditScore` only. This prevents
concurrent transactions from inserting or deleting any triples with the
`creditScore` property for the `person1` subject.

## Example 5 – Avoiding Dangling

Properties or Edges

The update on an entity should not leave a dangling element, that is,
a property or edge associated to an entity that is not typed. This is only
an issue in SPARQL, because Gremlin has built-in constraints to prevent
dangling elements.

```
# SPARQL:
tx1: INSERT { :person1 :age 23 } WHERE { :person1 rdf:type :Person }
tx2: DELETE { :person1 ?p ?o }
```

The `INSERT` query must read and lock the `SPO` prefix
with `S=person1`, `P=rdf:type`, and `O=Person` in
the `SPOG` index. The lock prevents the `DELETE` query from
succeeding in parallel.

In the race between the `DELETE` query trying to delete
the `:person1 rdf:type :Person` record and the `INSERT`
query reading the record and creating a range lock on its `SPO` in the
`SPOG` index, the following outcomes are possible:

- If the `INSERT` query commits before the `DELETE` query reads and
  deletes all records for `:person1`, `:person1` is removed entirely
  from the database, including the newly inserted record.
- If the `DELETE` query commits before the `INSERT` query tries to read
  the `:person1 rdf:type :Person` record, the read observes the committed change.
  That is, it does not find any `:person1 rdf:type :Person` record and hence
  becomes a no-op.
- If the `INSERT` query reads before the `DELETE` query does, the
  `:person1 rdf:type :Person` triple is locked and the `DELETE`
  query is blocked until the INSERT query commits, as in the first case previously.
- If the `DELETE` reads before the `INSERT` query, and the
  `INSERT` query tries to read and take a lock on the `SPO` prefix
  for the record, a conflict is detected. This is because the triple has been marked for
  removal, and the `INSERT` then fails.

In all these different possible sequences of events, no dangling edge is created.
