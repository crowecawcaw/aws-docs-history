# Using Python to connect to a Neptune DB

instance

If you can, always use the latest version of the Apache TinkerPop Python Gremlin
client, [gremlinpython](https://pypi.org/project/gremlinpython/ "https://pypi.org/project/gremlinpython/"),
that your engine version supports. Newer versions contain numerous bug fixes that
improve the stability, performance and usability of the client. The
`gremlinpython` version to use will typically align with the TinkerPop
versions described in the [table
for the Java Gremlin client](access-graph-gremlin-client.md#best-practices-gremlin-java-latest "access-graph-gremlin-client.md#best-practices-gremlin-java-latest").

The following section walks you through the running of a Python sample that connects to an
Amazon Neptune DB instance and performs a Gremlin traversal.

You must follow these instructions from an Amazon EC2 instance in the same virtual private
cloud (VPC) as your Neptune DB instance.

Before you begin, do the following:

- Download and install Python 3.6 or later from the [Python.org website](https://www.python.org/downloads/ "https://www.python.org/downloads/").
- Verify that you have **pip** installed. If you don't have
  **pip** or you're not sure, see [Do I need to
  install pip?](https://pip.pypa.io/en/stable/installing/#do-i-need-to-install-pip "https://pip.pypa.io/en/stable/installing/#do-i-need-to-install-pip") in the **pip** documentation.
- If your Python installation does not already have it, download
  `futures` as follows: `pip install futures`

###### To connect to Neptune using Python

1. Enter the following to install the `gremlinpython` package:

```
pip install --user gremlinpython
```

2. Create a file named `gremlinexample.py`, and then open it in a text
   editor.
3. Copy the following into the `gremlinexample.py` file. Replace
   `your-neptune-endpoint` with the address of your Neptune DB cluster and
   `your-neptune-port` with the port of your Neptune DB cluster (default:8182).

For information about finding the address of your Neptune DB instance, see the [Connecting to Amazon Neptune Endpoints](feature-overview-endpoints.md "feature-overview-endpoints.md") section.

The example below demonstrates how to connect with Gremlin Python. For IAM connectivity, see
[Connecting to Amazon Neptune databases using IAM authentication with Gremlin Python](gremlin-python-iam-auth.md "gremlin-python-iam-auth.md").

```
import boto3
import os
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python.process.anonymous_traversal import traversal

database_url = "wss://your-neptune-endpoint:your-neptune-port/gremlin"

remoteConn = DriverRemoteConnection(database_url, "g")

g = traversal().withRemote(remoteConn)

print(g.inject(1).toList())
remoteConn.close()
```

4. Enter the following command to run the sample:

```
python gremlinexample.py
```

The Gremlin query at the end of this example returns the vertices
(`g.V().limit(2)`) in a list. This list is then printed with the standard
Python `print` function.

###### Note

The final part of the Gremlin query, `toList()`,
is required to submit the traversal to the server for evaluation.
If you don't include that method or another equivalent method,
the query is not submitted to the Neptune DB instance.

The following methods submit the query to the Neptune DB instance:

    * `toList()`
    * `toSet()`
    * `next()`
    * `nextTraverser()`
    * `iterate()`

The preceding example returns the first two vertices in the graph by using the
`g.V().limit(2).toList()` traversal. To query for something else, replace it
with another Gremlin traversal with one of the appropriate ending methods.
