# Accessing the graph

Once you’ve created a graph and set up the prerequisites for connecting to that graph, you can proceed with
accessing your graph to load and query data. This section contains an explanation of ways you can communicate
with your graph along with some example queries. For details on how to load data, see the
[loading data](loading-data.md "loading-data.md") section
in the Neptune Analytics user guide.

## Using a notebook

You can access to your Neptune Analytics graph through a Neptune workbench, which provides visualization tools on
top of Neptune Analytics which can help with interpreting query results. For more information on how to set up and use
a graph notebook, see the
[notebooks](notebooks.md "notebooks.md") section
in the Neptune Analytics user guide.

**Example**

The cell magic below submits an openCypher query that returns a single node.

```
%%oc
MATCH (n) RETURN n LIMIT 1
```

## Using the AWS SDK

With the AWS SDK, you can access your graph using a programming language of your choice, which provides
clean integration between Neptune Analytics and your applications. With the Neptune Analytics SDK (service name Neptune graph),
you can perform data operations like querying and summarization in addition to control plane operations
such as graph creation, deletion, and modification. For a list of the supported programming languages and
directions for setting up the SDK in each language, see the
[AWS developer tools](https://aws.amazon.com/developer/tools/ "https://aws.amazon.com/developer/tools/") documentation.

Direct links to the API reference documentation for the Neptune Analytics service in each SDK language can be found below:

| Programming language | Neptune graph API reference                                                                                                                                                                                                                                                                                                              |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| C++                  | [https://sdk.amazonaws.com/cpp/api/LATEST/aws-cpp-sdk-neptune-graph/html/annotated.html](https://sdk.amazonaws.com/cpp/api/LATEST/aws-cpp-sdk-neptune-graph/html/annotated.html "https://sdk.amazonaws.com/cpp/api/LATEST/aws-cpp-sdk-neptune-graph/html/annotated.html")                                                                |
| Go                   | [https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/neptunegraph](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/neptunegraph "https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/neptunegraph")                                                                                                                      |
| Java                 | [https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/neptunegraph/package-summary.html](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/neptunegraph/package-summary.html "https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/neptunegraph/package-summary.html") |
| JavaScript           | [https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-aws-sdk-client-neptune-graph/](../../../AWSJavaScriptSDK/v3/latest/Package/-aws-sdk-client-neptune-graph.md "../../../AWSJavaScriptSDK/v3/latest/Package/-aws-sdk-client-neptune-graph.md")                                                                             |
| Kotlin               | [https://sdk.amazonaws.com/kotlin/api/latest/neptunegraph/index.html](https://sdk.amazonaws.com/kotlin/api/latest/neptunegraph/index.html "https://sdk.amazonaws.com/kotlin/api/latest/neptunegraph/index.html")                                                                                                                         |
| .NET                 | [https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/NeptuneGraph/NNeptuneGraph.html](../../../sdkfornet/v3/apidocs/items/NeptuneGraph/NNeptuneGraph.md "../../../sdkfornet/v3/apidocs/items/NeptuneGraph/NNeptuneGraph.md")                                                                                                          |
| PHP                  | [https://docs.aws.amazon.com/aws-sdk-php/v3/api/namespace-Aws.NeptuneGraph.html](../../../aws-sdk-php/v3/api/namespace-Aws.md "../../../aws-sdk-php/v3/api/namespace-Aws.md")                                                                                                                                                            |
| Python               | [https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html")                                           |
| CLI                  | [https://docs.aws.amazon.com/cli/latest/reference/neptune-graph/](../../../cli/latest/reference/neptune-graph.md "../../../cli/latest/reference/neptune-graph.md")                                                                                                                                                                       |
| Ruby                 | [https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/NeptuneGraph.html](../../../sdk-for-ruby/v3/api/Aws/NeptuneGraph.md "../../../sdk-for-ruby/v3/api/Aws/NeptuneGraph.md")                                                                                                                                                             |
| Rust                 | [https://crates.io/crates/aws-sdk-neptunegraph](https://crates.io/crates/aws-sdk-neptunegraph "https://crates.io/crates/aws-sdk-neptunegraph")                                                                                                                                                                                           |
| Swift                | [https://sdk.amazonaws.com/swift/api/awsneptunegraph/0.37.0/documentation/awsneptunegraph](https://sdk.amazonaws.com/swift/api/awsneptunegraph/0.37.0/documentation/awsneptunegraph "https://sdk.amazonaws.com/swift/api/awsneptunegraph/0.37.0/documentation/awsneptunegraph")                                                          |

## Examples

The following examples outline how to interact with an Amazon Neptune graph database using different
programming languages and tools. It covers the steps to set up an SDK client, execute an OpenCypher
query, and print the results, for Python as well as other languages. Additionally, it demonstrates
how to use the AWS Command Line Interface (CLI) and the AWSCURL tool to submit queries directly
to the Neptune graph endpoint.

Python

The code sample below uses the Python SDK to submit a query that returns a single node and prints the result.

1. Follow the
   [installation instructions](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html "https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html") to install Boto3. If you are using a SageMaker AI hosted
   Jupyter notebook, Boto3 will be pre-installed, but you may need to update it.
2. Configure your Boto3 credentials by following the
   [configuring credentials](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html#configuring-credentials "https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html#configuring-credentials") guide.
3. Create a file named `queryExample.py`.
4. In that file, paste the following code. It will set up a Neptune graph client, execute
   an openCypher query request, and print the result. Replace the graph identifier and
   query string as needed.

```
import boto3

// Set up the Neptune Graph client.
client = boto3.client('neptune-graph')

// Execute a query.
response = client.execute_query(
    graphIdentifier='g-0123456789',
    queryString='MATCH (n) RETURN n LIMIT 1',
    language='OPEN_CYPHER'
)

// Print the response.
print(response['payload'].read().decode('utf-8'))
```

5. Run the sample code by entering `python queryExample.py`.

Go

The code sample below uses the Go SDK to submit a query that returns a single node and prints the result.

1. Follow the
   [installation instructions](https://aws.github.io/aws-sdk-go-v2/docs/getting-started/ "https://aws.github.io/aws-sdk-go-v2/docs/getting-started/") to install Go and the AWS SDK for Go.
2. Create a file named `queryExample.go`.
3. In that file, paste the following code. It will set up a Neptune graph client, execute
   an openCypher query request, and print the result. Replace the graph identifier and
   query string as needed.

```
package main

import (
        "context"
        "log"
        "github.com/aws/aws-sdk-go-v2/aws"
        "github.com/aws/aws-sdk-go-v2/config"
        "github.com/aws/aws-sdk-go-v2/service/neptunegraph"
        "io"
)

func main() {
        // Load the Shared AWS Configuration (~/.aws/config)
        cfg, err := config.LoadDefaultConfig(context.TODO())
        if err != nil {
                log.Fatal(err)
        }

        // Create an Amazon Neptune Analytics service client
        client := neptunegraph.NewFromConfig(cfg)

        // Execute a query
        output, err := client.ExecuteQuery(context.TODO(), &neptunegraph.ExecuteQueryInput{
                GraphIdentifier: aws.String("g-0123456789"),
                Language: "OPEN_CYPHER",
                QueryString: aws.String("MATCH (n) RETURN n LIMIT 1"),
        })
        if err != nil {
                log.Fatal(err)
        }

        // Print the results
        bytes, err := io.ReadAll(output.Payload)
        log.Println(string(bytes))
}
```

4. Run the sample code by entering `go run queryExample.go`.

Node.js

The Node.js code sample below uses the JavaScript SDK to submit a query that returns a single node and prints the result.

1. Follow the [installation instructions](../../../sdk-for-javascript/v3/developer-guide/getting-started-nodejs.md "../../../sdk-for-javascript/v3/developer-guide/getting-started-nodejs.md") to install Node.js and set up your package structure. For this example,
   install the Neptune graph client package instead of the Amazon S3 client package:
   `npm install @aws-sdk/client-neptune-graph`.
2. Create a file in that directory structure named `queryExample.js`.
3. In that file, paste the following code. It will set up a Neptune graph client, execute
   an openCypher query request, and print the result. Replace the graph identifier and
   query string as needed.

```
import { NeptuneGraphClient, ExecuteQueryCommand } from "@aws-sdk/client-neptune-graph";

// Set up the client.
const neptuneGraphClient = new NeptuneGraphClient({});

// Send the query request.
const output = await neptuneGraphClient.send(
    new ExecuteQueryCommand({
        graphIdentifier: "g-0123456789",
        language: "OPEN_CYPHER",
        queryString: "MATCH (n) RETURN n LIMIT 1"
    })
);

// Print the result.
console.log(await output.payload.transformToString('utf-8'));
```

4. Run the sample code by entering `node queryExample.js`.

Java

The tutorial below sets up a project that uses the Java SDK to submit a query that returns a single node and prints the result.

1. To get started with the Java SDK, follow the
   [installation instructions](../../../sdk-for-java/latest/developer-guide/setup.md#setup-envtools "../../../sdk-for-java/latest/developer-guide/setup.md#setup-envtools") to install Java and set up a build tool that supports Maven central.
   This example will use [Apache Maven](https://maven.apache.org/ "https://maven.apache.org/").
2. Follow the
   [steps](../../../sdk-for-java/latest/developer-guide/get-started.md#get-started-projectsetup "../../../sdk-for-java/latest/developer-guide/get-started.md#get-started-projectsetup")
   to create a project using Maven based on the quickstart template. When executing these
   steps, please make the following modifications:

###### Note

When generating the project from the template, specify a version of the Java SDK that
includes the Neptune graph service APIs. For this example, use 2.25.7 as your
archetype version.

```
mvn archetype:generate \
  -DarchetypeGroupId=software.amazon.awssdk \
  -DarchetypeArtifactId=archetype-app-quickstart \
  -DarchetypeVersion=2.25.7
```

Running the command above will present you with several prompts. When asked to provide a
'service' (i.e., the service whose client and APIs you plan to use for this tutorial),
please enter `neptunegraph` as the service name. An updated table of prompts
and values can be found below:

| Prompt                                            | Value to enter  |
| ------------------------------------------------- | --------------- |
| Define value for property 'service':              | neptunegraph    |
| Define value for property 'httpClient':           | apache-client   |
| Define value for property 'nativeImage':          | false           |
| Define value for property 'credentialProvider':   | identity-center |
| Define value for property 'groupId':              | org.example     |
| Define value for property 'artifactId':           | getstarted      |
| Define value for property 'version' 1.0-SNAPSHOT: | <Enter>         |
| Define value for property 'package' org.example:  | <Enter>         |

3. After generating the project structure, you should see three Maven-generated classes
   defined in the `getstarted/src/main/java/org/example/` directory:
   `App.java`, `DependencyFactory.java`, and `Handler.java`.
   For details on each of these classes, see step 3 in the
   [SDK for Java](../../../sdk-for-java/latest/developer-guide/get-started.md#get-started-code "../../../sdk-for-java/latest/developer-guide/get-started.md#get-started-code") guide. Since this example uses the `neptunegraph` service, the
   Maven-generated code in the DependencyFactor and Handler classes will be using a
   different client than the code samples provided there. Refer to the Neptune
   graph-specific equivalents of the auto-generated classes below:
   1. Maven-generated `App.java` - this file is the same regardless of the
      service used.

   ```
   package org.example;
   import org.slf4j.Logger;
   import org.slf4j.LoggerFactory;

   public class App {
       private static final Logger logger = LoggerFactory.getLogger(App.class);

       public static void main(String... args) {
           logger.info("Application starts");

           Handler handler = new Handler();
           handler.sendRequest();

           logger.info("Application ends");
       }
   }
   ```

   2. Maven-generated `DependencyFactory.java` - This file uses the client
      class `NeptuneGraphClient` because `neptunegraph` was
      chosen as the service during the project setup.

   ```
   package org.example;

   import software.amazon.awssdk.http.apache.ApacheHttpClient;
   import software.amazon.awssdk.services.neptunegraph.NeptuneGraphClient;

   /**
    * The module containing all dependencies required by the {@link Handler}.
    */
   public class DependencyFactory {

       private DependencyFactory() {}

       /**
        * @return an instance of NeptuneGraphClient
        */
       public static NeptuneGraphClient neptuneGraphClient() {
           return NeptuneGraphClient.builder()
                          .httpClientBuilder(ApacheHttpClient.builder())
                          .build();
       }
   }
   ```

   3. Maven-generated `Handler.java` - This file uses the client
      class `NeptuneGraphClient` because `neptunegraph` was
      chosen as the service during the project setup.

   ```
   package org.example;

   import software.amazon.awssdk.services.neptunegraph.NeptuneGraphClient;


   public class Handler {
       private final NeptuneGraphClient neptuneGraphClient;

       public Handler() {
           neptuneGraphClient = DependencyFactory.neptuneGraphClient();
       }

       public void sendRequest() {
           // TODO: invoking the api calls using neptuneGraphClient.
       }
   }
   ```

4. Make changes to the Maven-generated handler class to fill in the missing logic in
   `sendRequest` to use the `NeptuneGraphClient` to execute a query,
   then print the result. Copy the completed code below, which replaces the TODO with code
   and adds the necessary imports. Replace the graph identifier and query string as needed.

```
package org.example;

import software.amazon.awssdk.core.ResponseInputStream;
import software.amazon.awssdk.services.neptunegraph.NeptuneGraphClient;
import software.amazon.awssdk.services.neptunegraph.model.ExecuteQueryRequest;
import software.amazon.awssdk.services.neptunegraph.model.ExecuteQueryResponse;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;


public class Handler {
    private final NeptuneGraphClient neptuneGraphClient;

    public Handler() {
        neptuneGraphClient = DependencyFactory.neptuneGraphClient();
    }

    public void sendRequest() {
        String graphIdentifier = "g-0123456789";
        String queryString = "MATCH (n) RETURN n LIMIT 1";

        ExecuteQueryRequest request = ExecuteQueryRequest.builder()
                .graphIdentifier(graphIdentifier)
                .queryString(queryString)
                .build();

        System.out.println("Executing query: " + queryString);

        ResponseInputStream<ExecuteQueryResponse> response = neptuneGraphClient.executeQuery(request);
        BufferedReader reader = new BufferedReader(new InputStreamReader(response));

        try {
                System.out.println("Printing query result:");
                String line;
                while ((line = reader.readLine()) != null) {
                        System.out.println(line);
                }
        } catch (IOException e) {
                System.out.println("Error occurred while printing result.");
        }
    }
}
```

5. Navigate to your project directory `getStarted`.
6. Build your project: `mvn clean package`
7. Run the application: `mvn exec:java -Dexec.mainClass="org.example.App"`.

## Using the AWS CLI

You can connect to your graph using the AWS command-line interface. Specify the neptune-graph service name
to use Neptune Analytics APIs. For information on AWS CLI installation and usage, see the
[AWS CLI documentation](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/"). To set up credentials, refer to
the [AWS CLI user guide](../../../cli/latest/userguide/cli-chap-configure.md "../../../cli/latest/userguide/cli-chap-configure.md").

The example command below uses the AWS CLI to submit a query that returns a single node.

```
aws neptune-graph execute-query \
--graph-identifier g-0123456789 \
--region us-east-2 \
--query-string "MATCH (n) RETURN n LIMIT 1" \
--language open_cypher \
out.txt
```

## Using AWSCURL

You can connect to your graph using the `awscurl` command-line tool. This allows you to directly
make requests using HTTPS against a graph endpoint. You can find the correct endpoint to use in the AWS
console (under the “Connectivity & Security” section of a Neptune Analytics graph page) and in the response of any
`GetGraph` API request. To set up credentials, refer to
the [AWS CLI user guide](../../../cli/latest/userguide/cli-chap-configure.md "../../../cli/latest/userguide/cli-chap-configure.md").

For `awscurl` installation and setup instructions, see
[AWSCURL](https://github.com/okigan/awscurl "https://github.com/okigan/awscurl") github repository.

The following command uses `awscurl` to submit a query that returns a single node.

```
awscurl -X POST "https://g-0123456789.us-east-2.neptune-graph.amazonaws.com/queries" \
-H "Content-Type: application/x-www-form-urlencoded" \
--region us-east-2 \
--service neptune-graph \
-d "query=MATCH (n) RETURN n LIMIT 1"
```
