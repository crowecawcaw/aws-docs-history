# Getting a quick summary report about your graph

The Neptune graph summary API retrieves the following information about your
graph:

- For property (PG) graphs, the graph summary API returns a read-only
  list of node and edge labels and property keys, along with counts of nodes, edges,
  and properties.
- For resource description framework (RDF) graphs, the graph summary API
  returns a read-only list of classes and predicate keys, along with counts of quads,
  subjects, and predicates.

###### Note

The graph summary API was introduced in Neptune [engine release 1.2.1.0](engine-releases-1.2.1.md "engine-releases-1.2.1.md").

With the graph summary API, you can quickly gain a high-level understanding
of your graph data size and content. You can also use the API interactively within
a Neptune notebook using the [%summary](notebooks-magics.md#notebooks-line-magics-summary "notebooks-magics.md#notebooks-line-magics-summary")
Neptune Workbench magic. In a graph application, the API can be used to improve
search results by providing discovered node or edge labels as part of the search.

Graph summary data is drawn from the [DFE
statistics](neptune-dfe-statistics.md "neptune-dfe-statistics.md") computed by the [Neptune
DFE engine](neptune-dfe-engine.md "neptune-dfe-engine.md") during runtime, and is available whenever DFE statistics are
available. Statistics are enabled by default when you create a new Neptune DB
cluster.

###### Note

Statistics generation is disabled on `t3` and `t4`
instance types (that is, on `db.t3.medium` and `db.t4g.medium`
instance types) to conserve memory. As a result, graph summary data is not
available either on those instance types.

You can check the status of DFE statistics using the [statistics status API](neptune-dfe-statistics.md#neptune-dfe-statistics-status "neptune-dfe-statistics.md#neptune-dfe-statistics-status").
As long as auto-generation of statistics has not [been disabled](neptune-dfe-statistics.md#neptune-dfe-statistics-auto-disable "neptune-dfe-statistics.md#neptune-dfe-statistics-auto-disable"), statistics
are automatically updated periodically.

If you want to be sure that statistics are as up to date as possible when you request
a graph summary, you can [manually
trigger a statistics update](neptune-dfe-statistics.md#neptune-dfe-statistics-manual "neptune-dfe-statistics.md#neptune-dfe-statistics-manual") right before retrieving the summary. If the
graph is changing while the statistics are being computed, they will necessarily
lag slightly behind, but not by much.

## Using the graph summary API to retrieve graph summary information

For a property graph that you query using Gremlin or openCypher, you can retrieve
a graph summary from the property-graph summary endpoint. There is both a long and a
short URI for this endpoint:

- `https://`your-neptune-host`:`port`/propertygraph/statistics/summary`
- `https://`your-neptune-host`:`port`/pg/statistics/summary`

For an RDF graph that you query using SPARQL, you can retrieve a graph summary from
the RDF summary endpoint:

- `https://`your-neptune-host`:`port`/rdf/statistics/summary`

These endpoints are read-only, and only support an HTTP `GET` operation.
If $GRAPH_SUMMARY_ENDPOINT is set to the address of whichever endpoint you want
to query, you can retrieve the summary data using `curl` and HTTP `GET`
as follows:

```
curl -G "$GRAPH_SUMMARY_ENDPOINT"
```

If no statistics are available when you try to retrieve a graph summary, the
response looks like this:

```
{
  "detailedMessage": "Statistics are not available. Summary can only be generated after statistics are available.",
  "requestId": "48c1f788-f80b-b69c-d728-3f6df579a5f6",
  "code": "StatisticsNotAvailableException"
}
```

## The `mode` URL query parameter for the graph summary API

The graph summary API accepts a URL query parameter named `mode`,
which can take one of two values, namely `basic` (the default) and
`detailed`. For an RDF graph, the `detailed` mode graph summary
response contains an additional `subjectStructures` field. For a property
graph, the detailed graph summary response contains two additional fields, namely
`nodeStructures` and `edgeStructures`.

To request a `detailed` graph summary response, include the `mode`
parameter as follows:

```
curl -G "$GRAPH_SUMMARY_ENDPOINT?mode=detailed"
```

If the `mode` parameter isn't present, `basic` mode is used
by default, so while it is possible to specify `?mode=basic` explicitly,
this is not necessary.

## Graph summary response for a property graph (PG)

For an empty property graph, the detailed graph summary response looks like this:

```
{
  "status" : "200 OK",
  "payload" : {
    "version" : "v1",
    "lastStatisticsComputationTime" : "2023-01-10T07:58:47.972Z",
    "graphSummary" : {
      "numNodes" : 0,
      "numEdges" : 0,
      "numNodeLabels" : 0,
      "numEdgeLabels" : 0,
      "nodeLabels" : [ ],
      "edgeLabels" : [ ],
      "numNodeProperties" : 0,
      "numEdgeProperties" : 0,
      "nodeProperties" : [ ],
      "edgeProperties" : [ ],
      "totalNodePropertyValues" : 0,
      "totalEdgePropertyValues" : 0,
      "nodeStructures" : [ ],
      "edgeStructures" : [ ]
    }
  }
}
```

A property graph (PG) summary response has the following fields:

- **`status`**   –  
  the HTTP return code of the request. If the request succeeded, the code is

200.

See [Common graph summary errors](#neptune-graph-summary-errors "#neptune-graph-summary-errors") for a list of common errors.

- **`payload`**
  - **`version`**   –  
    The version of this graph summary response.
  - **`lastStatisticsComputationTime`**   –  
    The timestamp, in ISO 8601 format, of the time at which Neptune last
    computed [statistics](neptune-dfe-statistics.md "neptune-dfe-statistics.md").
  - **`graphSummary`**
    - **`numNodes`**   –  
      The number of nodes in the graph.
    - **`numEdges`**   –  
      The number of edges in the graph.
    - **`numNodeLabels`**   –  
      The number of distinct node labels in the graph.
    - **`numEdgeLabels`**   –  
      The number of distinct edge labels in the graph.
    - **`nodeLabels`**   –  
      List of distinct node labels in the graph.
    - **`edgeLabels`**   –  
      List of distinct edge labels in the graph.
    - **`numNodeProperties`**   –  
      The number of distinct node properties in the graph.
    - **`numEdgeProperties`**   –  
      The number of distinct edge properties in the graph.
    - **`nodeProperties`**   –  
      List of distinct node properties in the graph, along with the count of nodes
      where each property is used.
    - **`edgeProperties`**   –  
      List of distinct edge properties in the graph along with the count of edges
      where each property is used.
    - **`totalNodePropertyValues`**   –  
      Total number of usages of all node properties.
    - **`totalEdgePropertyValues`**   –  
      Total number of usages of all edge properties.
    - **`nodeStructures`**   –  
      _This field is only present when `mode=detailed`
      is specified in the request._ It contains a list of node
      structures, each of which contains the following fields:
      - **`count`**   –  
        Number of nodes that have this specific structure.
      - **`nodeProperties`**   –  
        List of node properties present in this specific structure.
      - **`distinctOutgoingEdgeLabels`**   –  
        List of distinct outgoing edge labels present in this specific structure.

    - **`edgeStructures`**   –  
      _This field is only present when `mode=detailed`
      is specified in the request._ It contains a list of edge
      structures, each of which contains the following fields:
      - **`count`**   –  
        Number of edges that have this specific structure.
      - **`edgeProperties`**   –  
        List of edge properties present in this specific structure.

## Graph summary response for an RDF graph

For an empty RDF graph, the detailed graph summary response looks like this:

```
{
  "status" : "200 OK",
  "payload" : {
    "version" : "v1",
    "lastStatisticsComputationTime" : "2023-01-10T07:58:47.972Z",
    "graphSummary" : {
      "numDistinctSubjects" : 0,
      "numDistinctPredicates" : 0,
      "numQuads" : 0,
      "numClasses" : 0,
      "classes" : [ ],
      "predicates" : [ ],
      "subjectStructures" : [ ]
    }
  }
}
```

An RDF graph summary response has the following fields:

- **`status`**   –  
  the HTTP return code of the request. If the request succeeded, the code is

200.

See [Common graph summary errors](#neptune-graph-summary-errors "#neptune-graph-summary-errors") for a list
of common errors.

- **`payload`**
  - **`version`**   –  
    The version of this graph summary response.
  - **`lastStatisticsComputationTime`**   –  
    The timestamp, in ISO 8601 format, of the time at which Neptune last
    computed [statistics](neptune-dfe-statistics.md "neptune-dfe-statistics.md").
  - **`graphSummary`**
    - **`numDistinctSubjects`**   –  
      The number of distinct subjects in the graph.
    - **`numDistinctPredicates`**   –  
      The number of distinct predicates in the graph.
    - **`numQuads`**   –  
      The number of quads in the graph.
    - **`numClasses`**   –  
      The number of classes in the graph.
    - **`classes`**   –  
      List of classes in the graph.
    - **`predicates`**   –  
      List of predicates in the graph, along with the predicate counts.
    - **`subjectStructures`**   –  
      _This field is only present when `mode=detailed`
      is specified in the request._ It contains a list of subject
      structures, each of which contains the following fields:
      - **`count`**   –  
        Number of occurrences of this specific structure.
      - **`predicates`**   –  
        List of predicates present in this specific structure.

## Sample property-graph (PG) summary response

Here is the detailed summary response for a property graph that contains the [sample
property-graph air routes dataset](https://github.com/aws/graph-notebook/tree/main/src/graph_notebook/seed/queries/propertygraph/gremlin/airports "https://github.com/aws/graph-notebook/tree/main/src/graph_notebook/seed/queries/propertygraph/gremlin/airports"):

```
{
  "status" : "200 OK",
  "payload" : {
    "version" : "v1",
    "lastStatisticsComputationTime" : "2023-03-01T14:35:03.804Z",
    "graphSummary" : {
      "numNodes" : 3748,
      "numEdges" : 51300,
      "numNodeLabels" : 4,
      "numEdgeLabels" : 2,
      "nodeLabels" : [
        "continent",
        "country",
        "version",
        "airport"
      ],
      "edgeLabels" : [
        "contains",
        "route"
      ],
      "numNodeProperties" : 14,
      "numEdgeProperties" : 1,
      "nodeProperties" : [
        {
          "desc" : 3748
        },
        {
          "code" : 3748
        },
        {
          "type" : 3748
        },
        {
          "country" : 3503
        },
        {
          "longest" : 3503
        },
        {
          "city" : 3503
        },
        {
          "lon" : 3503
        },
        {
          "elev" : 3503
        },
        {
          "icao" : 3503
        },
        {
          "region" : 3503
        },
        {
          "runways" : 3503
        },
        {
          "lat" : 3503
        },
        {
          "date" : 1
        },
        {
          "author" : 1
        }
      ],
      "edgeProperties" : [
        {
          "dist" : 50532
        }
      ],
      "totalNodePropertyValues" : 42773,
      "totalEdgePropertyValues" : 50532,
      "nodeStructures" : [
        {
          "count" : 3471,
          "nodeProperties" : [
            "city",
            "code",
            "country",
            "desc",
            "elev",
            "icao",
            "lat",
            "lon",
            "longest",
            "region",
            "runways",
            "type"
          ],
          "distinctOutgoingEdgeLabels" : [
            "route"
          ]
        },
        {
          "count" : 161,
          "nodeProperties" : [
            "code",
            "desc",
            "type"
          ],
          "distinctOutgoingEdgeLabels" : [
            "contains"
          ]
        },
        {
          "count" : 83,
          "nodeProperties" : [
            "code",
            "desc",
            "type"
          ],
          "distinctOutgoingEdgeLabels" : [ ]
        },
        {
          "count" : 32,
          "nodeProperties" : [
            "city",
            "code",
            "country",
            "desc",
            "elev",
            "icao",
            "lat",
            "lon",
            "longest",
            "region",
            "runways",
            "type"
          ],
          "distinctOutgoingEdgeLabels" : [ ]
        },
        {
          "count" : 1,
          "nodeProperties" : [
            "author",
            "code",
            "date",
            "desc",
            "type"
          ],
          "distinctOutgoingEdgeLabels" : [ ]
        }
      ],
      "edgeStructures" : [
        {
          "count" : 50532,
          "edgeProperties" : [
            "dist"
          ]
        }
      ]
    }
  }
}
```

## Sample RDF graph summary response

Here is the detailed summary response for an RDF graph that contains the [sample
RDF air routes dataset](https://github.com/aws/graph-notebook/tree/main/src/graph_notebook/seed/queries/rdf/sparql/airports "https://github.com/aws/graph-notebook/tree/main/src/graph_notebook/seed/queries/rdf/sparql/airports"):

```
{
  "status" : "200 OK",
  "payload" : {
    "version" : "v1",
    "lastStatisticsComputationTime" : "2023-03-01T14:54:13.903Z",
    "graphSummary" : {
      "numDistinctSubjects" : 54403,
      "numDistinctPredicates" : 19,
      "numQuads" : 158571,
      "numClasses" : 4,
      "classes" : [
        "http://kelvinlawrence.net/air-routes/class/Version",
        "http://kelvinlawrence.net/air-routes/class/Airport",
        "http://kelvinlawrence.net/air-routes/class/Continent",
        "http://kelvinlawrence.net/air-routes/class/Country"
      ],
      "predicates" : [
        {
          "http://kelvinlawrence.net/air-routes/objectProperty/route" : 50656
        },
        {
          "http://kelvinlawrence.net/air-routes/datatypeProperty/dist" : 50656
        },
        {
          "http://kelvinlawrence.net/air-routes/objectProperty/contains" : 7004
        },
        {
          "http://kelvinlawrence.net/air-routes/datatypeProperty/code" : 3747
        },
        {
          "http://www.w3.org/2000/01/rdf-schema#label" : 3747
        },
        {
          "http://kelvinlawrence.net/air-routes/datatypeProperty/type" : 3747
        },
        {
          "http://kelvinlawrence.net/air-routes/datatypeProperty/desc" : 3747
        },
        {
          "http://www.w3.org/1999/02/22-rdf-syntax-ns#type" : 3747
        },
        {
          "http://kelvinlawrence.net/air-routes/datatypeProperty/icao" : 3502
        },
        {
          "http://kelvinlawrence.net/air-routes/datatypeProperty/lat" : 3502
        },
        {
          "http://kelvinlawrence.net/air-routes/datatypeProperty/region" : 3502
        },
        {
          "http://kelvinlawrence.net/air-routes/datatypeProperty/runways" : 3502
        },
        {
          "http://kelvinlawrence.net/air-routes/datatypeProperty/longest" : 3502
        },
        {
          "http://kelvinlawrence.net/air-routes/datatypeProperty/elev" : 3502
        },
        {
          "http://kelvinlawrence.net/air-routes/datatypeProperty/lon" : 3502
        },
        {
          "http://kelvinlawrence.net/air-routes/datatypeProperty/country" : 3502
        },
        {
          "http://kelvinlawrence.net/air-routes/datatypeProperty/city" : 3502
        },
        {
          "http://kelvinlawrence.net/air-routes/datatypeProperty/author" : 1
        },
        {
          "http://kelvinlawrence.net/air-routes/datatypeProperty/date" : 1
        }
      ],
      "subjectStructures" : [
        {
          "count" : 50656,
          "predicates" : [
            "http://kelvinlawrence.net/air-routes/datatypeProperty/dist"
          ]
        },
        {
          "count" : 3471,
          "predicates" : [
            "http://kelvinlawrence.net/air-routes/datatypeProperty/city",
            "http://kelvinlawrence.net/air-routes/datatypeProperty/code",
            "http://kelvinlawrence.net/air-routes/datatypeProperty/country",
            "http://kelvinlawrence.net/air-routes/datatypeProperty/desc",
            "http://kelvinlawrence.net/air-routes/datatypeProperty/elev",
            "http://kelvinlawrence.net/air-routes/datatypeProperty/icao",
            "http://kelvinlawrence.net/air-routes/datatypeProperty/lat",
            "http://kelvinlawrence.net/air-routes/datatypeProperty/lon",
            "http://kelvinlawrence.net/air-routes/datatypeProperty/longest",
            "http://kelvinlawrence.net/air-routes/datatypeProperty/region",
            "http://kelvinlawrence.net/air-routes/datatypeProperty/runways",
            "http://kelvinlawrence.net/air-routes/datatypeProperty/type",
            "http://kelvinlawrence.net/air-routes/objectProperty/route",
            "http://www.w3.org/1999/02/22-rdf-syntax-ns#type",
            "http://www.w3.org/2000/01/rdf-schema#label"
          ]
        },
        {
          "count" : 238,
          "predicates" : [
            "http://kelvinlawrence.net/air-routes/datatypeProperty/code",
            "http://kelvinlawrence.net/air-routes/datatypeProperty/desc",
            "http://kelvinlawrence.net/air-routes/datatypeProperty/type",
            "http://kelvinlawrence.net/air-routes/objectProperty/contains",
            "http://www.w3.org/1999/02/22-rdf-syntax-ns#type",
            "http://www.w3.org/2000/01/rdf-schema#label"
          ]
        },
        {
          "count" : 31,
          "predicates" : [
            "http://kelvinlawrence.net/air-routes/datatypeProperty/city",
            "http://kelvinlawrence.net/air-routes/datatypeProperty/code",
            "http://kelvinlawrence.net/air-routes/datatypeProperty/country",
            "http://kelvinlawrence.net/air-routes/datatypeProperty/desc",
            "http://kelvinlawrence.net/air-routes/datatypeProperty/elev",
            "http://kelvinlawrence.net/air-routes/datatypeProperty/icao",
            "http://kelvinlawrence.net/air-routes/datatypeProperty/lat",
            "http://kelvinlawrence.net/air-routes/datatypeProperty/lon",
            "http://kelvinlawrence.net/air-routes/datatypeProperty/longest",
            "http://kelvinlawrence.net/air-routes/datatypeProperty/region",
            "http://kelvinlawrence.net/air-routes/datatypeProperty/runways",
            "http://kelvinlawrence.net/air-routes/datatypeProperty/type",
            "http://www.w3.org/1999/02/22-rdf-syntax-ns#type",
            "http://www.w3.org/2000/01/rdf-schema#label"
          ]
        },
        {
          "count" : 6,
          "predicates" : [
            "http://kelvinlawrence.net/air-routes/datatypeProperty/code",
            "http://kelvinlawrence.net/air-routes/datatypeProperty/desc",
            "http://kelvinlawrence.net/air-routes/datatypeProperty/type",
            "http://www.w3.org/1999/02/22-rdf-syntax-ns#type",
            "http://www.w3.org/2000/01/rdf-schema#label"
          ]
        },
        {
          "count" : 1,
          "predicates" : [
            "http://kelvinlawrence.net/air-routes/datatypeProperty/author",
            "http://kelvinlawrence.net/air-routes/datatypeProperty/code",
            "http://kelvinlawrence.net/air-routes/datatypeProperty/date",
            "http://kelvinlawrence.net/air-routes/datatypeProperty/desc",
            "http://kelvinlawrence.net/air-routes/datatypeProperty/type",
            "http://www.w3.org/1999/02/22-rdf-syntax-ns#type",
            "http://www.w3.org/2000/01/rdf-schema#label"
          ]
        }
      ]
    }
  }
}
```

## Using AWS Identity and Access Management (IAM) authentication with graph summary endpoints

You can access graph summary endpoints securely with IAM authentication by using
[awscurl](https://github.com/okigan/awscurl "https://github.com/okigan/awscurl") or any other tool
that works with HTTPS and IAM. See [Using awscurl with temporary
credentials to securely connect to a DB cluster with IAM authentication enabled](iam-auth-connect-command-line.md#iam-auth-connect-awscurl "iam-auth-connect-command-line.md#iam-auth-connect-awscurl") to see how to set up the proper
credentials. Once you have done that, you can then make requests like this:

```
awscurl "$GRAPH_SUMMARY_ENDPOINT" \
    --region `(your region)` \
    --service neptune-db
```

###### Important

The IAM identity or role that creates the temporary credentials
must have an IAM policy attached that allows the [GetGraphSummary](iam-dp-actions.md#getgraphsummary "iam-dp-actions.md#getgraphsummary") IAM action.

See [IAM Authentication Errors](errors-engine-codes.md#errors-iam-auth "errors-engine-codes.md#errors-iam-auth") for
a list of common IAM errors that you may encounter.

## Common error codes that a graph summary request may return

| Neptune service error code            | HTTP status                                                                                                   | Message                                                                                                                                                                                                        | Error Scenario                                                                                                        | Mitigation                                                                                                                                                                                                                                               |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`AccessDeniedException`**           | 403                                                                                                           | Missing Authentication Token.                                                                                                                                                                                  | Unsigned or incorrectly signed request was sent to<br>Neptune database with IAM enabled.                              | Sign the request with SigV4 before sending<br>(see [IAM and graph summaries](#neptune-graph-summary-iam "#neptune-graph-summary-iam")).                                                                                                                  |
| 403                                   | User: `(user ARN)` is not authorized<br>to perform: neptune-db:GetGraphSummary on resource: `(resource ARN)`. | IAM policy does not allow the action [GetGraphSummary](iam-dp-actions.md#getgraphsummary "iam-dp-actions.md#getgraphsummary") when the graph summary request<br>was sent to Neptune database with IAM enabled. | Make sure that the IAM policy attached to the user or role making the request<br>allows the `GetGraphSummary` action. |
| **`BadRequestException`**             | 400                                                                                                           | Statistics are disabled, so graph summary is also disabled.                                                                                                                                                    | Trying to fetch summary on burstable instance types<br>(`t3` or `t4g`) where statistics are disabled.                 | Use an instance type where statistics generation is enabled<br>(all supported instances except `t3` and `t4g`).                                                                                                                                          |
| 400                                   | Bad route: `/rdf/statistics/summarypathapi`                                                                   | Request sent to invalid path.                                                                                                                                                                                  | Use correct route for graph summary endpoint.                                                                         |
| **`InvalidParameterException`**       | 400                                                                                                           | Request contains unknown parameters: '`(unknown parameter or parameters)`'.                                                                                                                                    | When an invalid parameter is specified in the request.                                                                | Only use valid parameters (such as `mode`) in the request.                                                                                                                                                                                               |
| **`InvalidParameterException`**       | 400                                                                                                           | URI query parameter 'mode' has unsupported value '`(invalid value)`'.                                                                                                                                          | When the URL parameter 'mode' in the request is followed by an invalid value.                                         | Use valid values (such as `basic` or `detailed`) when<br>specifying the URL parameter 'mode'.                                                                                                                                                            |
| **`MethodNotAllowedException`**       | 405                                                                                                           | Method Not Allowed.                                                                                                                                                                                            | Calling summary endpoint with any HTTP method other than<br>`GET` (such as `POST` or `DELETE`).                       | Use HTTP `GET` method when calling summary endpoint.                                                                                                                                                                                                     |
| **`StatisticsNotAvailableException`** | 400                                                                                                           | Statistics are not computed yet, graph summary will be available<br>after statistics computation is complete.                                                                                                  | There are no statistics available when the request is<br>sent to the summary endpoint.                                | Wait until statistics generation is complete. You can check<br>the status of statistics generation using the [statistics status API](neptune-dfe-statistics.md#neptune-dfe-statistics-status "neptune-dfe-statistics.md#neptune-dfe-statistics-status"). |
| 400                                   | Statistics limit reached, thus graph summary is not available.                                                | Statistics generation has stopped because it reached [statistics size limits](neptune-dfe-statistics.md#neptune-dfe-statistics-limits "neptune-dfe-statistics.md#neptune-dfe-statistics-limits").              | Graph summary is not available on this graph.                                                                         |

For example, if you make a request to graph summary endpoint in a
Neptune database that has IAM authentication enabled, and the necessary
permissions are not present in the requestor’s IAM policy, then you would
get a response like the following:

```
{
  "detailedMessage": "User: arn:aws:iam::`(account ID)`:`(user or user name)` is not authorized to perform: neptune-db:GetGraphSummary on resource: arn:aws:neptune-db:`(region)`:`(account ID)`:`(cluster resource ID)`/*",
  "requestId": "7ac2b98e-b626-d239-1d05-74b4c88fce82",
  "code": "AccessDeniedException"
}
```
