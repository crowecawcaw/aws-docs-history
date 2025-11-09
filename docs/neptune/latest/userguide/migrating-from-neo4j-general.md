# General information about migrating from Neo4j to Neptune

With Neptune [support for the
openCypher query language](feature-opencypher-compliance.md "feature-opencypher-compliance.md"), you can move most Neo4j workloads that use the Bolt
protocol or HTTPS to Neptune. However, openCypher is an open-source specification
that contains most but not all of the functionality supported by other databases such
as Neo4j.

In spite of being compatible in many ways, Neptune is not a drop-in replacement for
Neo4j. Neptune is a fully managed graph database service with enterprise features like
high availability and high durability that is architecturally different from Neo4j.
Neptune is instance-based, with a single primary writer instance and up to 15 read
replica instances that let you scale read capacity horizontally. Using [Neptune Serverless](neptune-serverless.md "neptune-serverless.md"), you can automatically scale
your compute capacity up and down depending on query volume. This is independent of
Neptune storage, which scales automatically as you add data.

Neptune supports the open-source [openCypher
standard specification, version 9](https://s3.amazonaws.com/artifacts.opencypher.org/openCypher9.pdf "https://s3.amazonaws.com/artifacts.opencypher.org/openCypher9.pdf"). At AWS, we believe that open source
is good for everyone and we are committed both to bringing the value of open source
to our customers, and to bringing the operational excellence of AWS to open source
communities.

However, many applications running on Neo4j also use proprietary features that
are not open-sourced and that Neptune doesn't support. For example, Neptune doesn't
support APOC procedures, some Cypher-specific clauses and functions, and `Char`,
`Date`, or `Duration` data types. Neptune does auto-cast
the missing data types to [data
types that are supported](bulk-load-tutorial-format-opencypher.md#bulk-load-tutorial-format-opencypher-data-types "bulk-load-tutorial-format-opencypher.md#bulk-load-tutorial-format-opencypher-data-types").

In addition to openCypher, Neptune also supports the [Apache
TinkerPop Gremlin](https://tinkerpop.apache.org/docs/current/reference/#traversal "https://tinkerpop.apache.org/docs/current/reference/#traversal") query language for property graphs (as well as SPARQL for RDF
data). Gremlin can interoperate with openCypher on the same property graph, and in many
cases you can use Gremlin to supply functionality that openCypher does not provide.
Below is a quick comparison of the two languages:

|               | openCypher                                                                                | Gremlin                                                                                            |
| ------------- | ----------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| Style         | Declarative                                                                               | Imperative                                                                                         |
| Syntax        | Pattern matching<br>`<br>Match p=(a)-[:route]->(d)<br>WHERE a.code='ANC'<br>RETURN p<br>` | Traversal based<br>`<br>g.V().has('code', 'ANC').<br>out('route').path().<br>by(elementMap())<br>` |
| Ease of use   | SQL-inspired, readable by non-programmers                                                 | Steeper learning curve, similar to programming languages like Java                                 |
| Flexibility   | Low                                                                                       | High                                                                                               |
| Query support | String-based queries                                                                      | String-based queries or in-line code supported by client libraries                                 |
| Clients       | HTTPS and Bolt                                                                            | HTTPS and Websockets                                                                               |

In general, it isn't necessary to change your data model to migrate from Neo4j to
Neptune, because both Neo4j and Neptune support labeled property graph (LPG) data.
However, Neptune has some architectural and data model differences that you can take
advantage of to optimize performance. For example:

- Neptune IDs are treated as first-class citizens.
- Neptune uses [AWS Identity and Access Management (IAM) policies](iam-auth.md "iam-auth.md") to secure access
  to your graph data in flexible and granular ways.
- Neptune provides several ways to [use Jupyter notebooks](graph-notebooks.md "graph-notebooks.md")
  to run queries and [visualize the results](notebooks-visualization.md "notebooks-visualization.md"). Neptune
  also works with [third-party visualization tools](visualization-tools.md "visualization-tools.md").
- > Although Neptune has no drop-in replacement for the Neo4j Graph Data Science (GDS) library,
  > Neptune supports graph analytics today through a variety of solutions. For example, several [sample
  > notebooks](https://github.com/aws/graph-notebook/tree/main/src/graph_notebook/notebooks/05-Data-Science "https://github.com/aws/graph-notebook/tree/main/src/graph_notebook/notebooks/05-Data-Science") demonstrate how to leverage the Neptune
  > [integration with
  > the AWS Pandas SDK](https://github.com/amazon-archives/fully-automated-neo4j-to-neptune "https://github.com/amazon-archives/fully-automated-neo4j-to-neptune") within Python environments to run analytics on graph data.
  > Please reach out to AWS support or engage your AWS account team if you have questions.
  > We use your feedback to prioritize new features that will meet your needs.
