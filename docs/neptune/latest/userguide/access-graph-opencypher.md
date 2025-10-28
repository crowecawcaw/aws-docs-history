# Accessing the Neptune Graph with openCypher

Neptune supports building graph applications using openCypher, currently one
of the most popular query languages for developers working with graph databases.
Developers, business analysts, and data scientists like openCypher’s SQL-inspired
syntax because it provides a familiar structure to compose queries for graph
applications.

**openCypher** is a declarative query language
for property graphs that was originally developed by Neo4j, then open-sourced in 2015,
and contributed to the [openCypher](http://www.opencypher.org/ "http://www.opencypher.org/")
project under an Apache 2 open-source license. Its syntax is documented in the
[Cypher Query Language Reference, Version 9](https://s3.amazonaws.com/artifacts.opencypher.org/openCypher9.pdf "https://s3.amazonaws.com/artifacts.opencypher.org/openCypher9.pdf").

For the limitations and differences in Neptune support of the openCypher
specification, see [openCypher specification compliance in Amazon Neptune](feature-opencypher-compliance.md "feature-opencypher-compliance.md").

###### Note

The current Neo4j implementation of the Cypher query language has diverged
in some ways from the openCypher specification. If you are migrating current
Neo4j Cypher code to Neptune, see [Neptune compatibility with Neo4j](migration-compatibility.md "migration-compatibility.md") and [Rewriting Cypher queries to run in openCypher on Neptune](migration-opencypher-rewrites.md "migration-opencypher-rewrites.md") for help.

Starting with engine release 1.1.1.0, openCypher is available for production
use in Neptune.

## Gremlin vs. openCypher: similarities and differences

Gremlin and openCypher are both property-graph query languages, and they are
complementary in many ways.

Gremlin was designed to appeal to programmers and fit seamlessly
into code. As a result, Gremlin is imperative by design, whereas openCypher's declarative
syntax may feel more familiar for people with SQL or SPARQL experience. Gremlin might seem
more natural to a data scientist using Python in a Jupyter notebook, whereas openCypher
might seem more intuitive to a business user with some SQL background.

The nice thing is that **you don't have to choose**
between Gremlin and openCypher in Neptune. Queries in either language can operate
on the same graph regardless of which of the two language was used to enter that data.
You may find it more convenient to use Gremlin for some things and openCypher for others,
depending on what you're doing.

Gremlin uses an imperative syntax that lets you control how you move through
your graph in a series of steps, each of which takes in a stream of data, performs
some action on it (using a filter, map, and so forth), and then outputs the
results to the next step. A Gremlin query commonly takes the form, `g.V()`,
followed by additional steps.

In openCypher, you use a declarative syntax, inspired by SQL, that specifies a
pattern of nodes and relationships to find in your graph using a motif syntax
(like `()-[]->()`). An openCypher query often starts with a `MATCH`
clause, followed by other clauses such as `WHERE`, `WITH`, and
`RETURN`.
