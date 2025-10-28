# Using Go to connect to a Neptune DB

instance

If you can, always use the latest version of the Apache TinkerPop Go Gremlin
client, [gremlingo](https://pkg.go.dev/github.com/apache/tinkerpop/gremlin-go/v3/driver "https://pkg.go.dev/github.com/apache/tinkerpop/gremlin-go/v3/driver"),
that your engine version supports. Newer versions contain numerous bug fixes that improve the
stability, performance and usability of the client.

The `gremlingo` version to use will typically align with the TinkerPop
versions described in the [table
for the Java Gremlin client](access-graph-gremlin-client.md#best-practices-gremlin-java-latest "access-graph-gremlin-client.md#best-practices-gremlin-java-latest").

###### Note

The gremlingo 3.5.x versions are backwards compatible with TinkerPop 3.4.x versions
as long as you only use 3.4.x features in the Gremlin queries you write.

The following section walks you through the running of a Go sample that connects to
an Amazon Neptune DB instance and performs a Gremlin traversal.

You must follow these instructions from an Amazon EC2 instance in the same virtual private
cloud (VPC) as your Neptune DB instance.

Before you begin, do the following:

- Download and install Go 1.17 or later from the [go.dev](https://go.dev/dl/ "https://go.dev/dl/") website.

###### To connect to Neptune using Go

1. Starting from an empty directory, initialize a new Go module:

```
go mod init example.com/gremlinExample
```

2. Add gremlin-go as a dependency of your new module:

```
go get github.com/apache/tinkerpop/gremlin-go/v3/driver
```

3. Create a file named `gremlinExample.go` and then open it in a text editor.
4. Copy the following into the `gremlinExample.go` file, replacing
   `(your neptune endpoint)` with the address
   of your Neptune DB instance:

```
package main

import (
  "fmt"
  gremlingo "github.com/apache/tinkerpop/gremlin-go/v3/driver"
)

func main() {
  // Creating the connection to the server.
  driverRemoteConnection, err := gremlingo.NewDriverRemoteConnection("wss://`(your neptune endpoint)`:8182/gremlin",
    func(settings *gremlingo.DriverRemoteConnectionSettings) {
      settings.TraversalSource = "g"
    })
  if err != nil {
    fmt.Println(err)
    return
  }
  // Cleanup
  defer driverRemoteConnection.Close()

  // Creating graph traversal
  g := gremlingo.Traversal_().WithRemote(driverRemoteConnection)

  // Perform traversal
  results, err := g.V().Limit(2).ToList()
  if err != nil {
    fmt.Println(err)
    return
  }
  // Print results
  for _, r := range results {
    fmt.Println(r.GetString())
  }
}

```

###### Note

The Neptune TLS certificate format is not currently supported on Go 1.18+ with
macOS, and may give a 509 error when trying to initiate a connection. For local testing,
this can be skipped by adding "crypto/tls" to the imports and modifying the
`DriverRemoteConnection` settings as follows:

```
// Creating the connection to the server.
driverRemoteConnection, err := gremlingo.NewDriverRemoteConnection("wss://your-neptune-endpoint:8182/gremlin",
  func(settings *gremlingo.DriverRemoteConnectionSettings) {
      settings.TraversalSource = "g"
      settings.TlsConfig = &tls.Config{InsecureSkipVerify: true}
  })
```

5. Enter the following command to run the sample:

```
go run gremlinExample.go
```

The Gremlin query at the end of this example returns the vertices
`(g.V().Limit(2))` in a slice. This slice is then iterated through
and printed with the standard `fmt.Println` function.

###### Note

The final part of the Gremlin query, `ToList()`, is required to submit the
traversal to the server for evaluation. If you don't include that method or another
equivalent method, the query is not submitted to the Neptune DB instance.

The following methods submit the query to the Neptune DB instance:

- `ToList()`
- `ToSet()`
- `Next()`
- `GetResultSet()`
- `Iterate()`
  The preceding example returns the first two vertices in the graph
  by using the `g.V().Limit(2).ToList()` traversal. To query
  for something else, replace it with another Gremlin traversal with one
  of the appropriate ending methods.
