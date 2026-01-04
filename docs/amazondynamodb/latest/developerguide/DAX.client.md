# DAX SDK for Go

Follow this procedure to run the Amazon DynamoDB Accelerator (DAX) SDK for Go sample application
on your Amazon EC2 instance.

###### To run the SDK for Go sample for DAX

1. Set up the SDK for Go on your Amazon EC2 instance:
   1. Install the Go programming language (`Golang`).

   ```
   sudo yum install -y golang
   ```

   2. Test that Golang is installed and running correctly.

   ```
   go version
   ```

   A message like this should appear.

   ```
   go version go1.23.4 linux/amd64
   ```

2. Install the sample Golang application.

```
go get github.com/aws-samples/sample-aws-dax-go-v2
```

3. Run the following Golang programs. The first program creates a DynamoDB table
   named `TryDaxGoTable`. The second program writes data to
   the table.

```
go run ~/go/pkg/mod/github.com/aws-samples/sample-aws-dax-go-v2@v1.0.0/try_dax.go -service dynamodb -command create-table
```

```
go run ~/go/pkg/mod/github.com/aws-samples/sample-aws-dax-go-v2@v1.0.0/try_dax.go -service dynamodb -command put-item
```

4. Run the following Golang programs.

```
go run ~/go/pkg/mod/github.com/aws-samples/sample-aws-dax-go-v2@v1.0.0/try_dax.go -service dynamodb -command get-item
```

```
go run ~/go/pkg/mod/github.com/aws-samples/sample-aws-dax-go-v2@v1.0.0/try_dax.go -service dynamodb -command query
```

```
go run ~/go/pkg/mod/github.com/aws-samples/sample-aws-dax-go-v2@v1.0.0/try_dax.go -service dynamodb -command scan
```

Take note of the timing information—the number of milliseconds required
for the `GetItem`, `Query`, and `Scan`
tests. 5. In the previous step, you ran the programs against the DynamoDB endpoint.
Now, run the programs again, but this time, the `GetItem`,
`Query`, and `Scan` operations are processed by
your DAX cluster.

To determine the endpoint for your DAX cluster, choose one of the
following:

    * **Using the DynamoDB console** — Choose your
     DAX cluster. The cluster endpoint is shown on the console, as in
     the following example.



    ```
    dax://my-cluster.l6fzcv.dax-clusters.us-east-1.amazonaws.com
    ```
    * **Using the AWS CLI** — Enter the following
     command.



    ```
    aws dax describe-clusters --query "Clusters[*].ClusterDiscoveryEndpoint"
    ```

    The cluster endpoint is shown in the output, as in the following
     example.



    ```
    {
        "Address": "my-cluster.l6fzcv.dax-clusters.us-east-1.amazonaws.com",
        "Port": 8111,
        "URL": "dax://my-cluster.l6fzcv.dax-clusters.us-east-1.amazonaws.com"
    }
    ```

Now run the programs again, but this time, specify the cluster endpoint as
a command line parameter.

```
go run ~/go/pkg/mod/github.com/aws-samples/sample-aws-dax-go-v2@v1.0.0/try_dax.go -service dax -command get-item -endpoint my-cluster.l6fzcv.dax-clusters.us-east-1.amazonaws.com:8111
```

```
go run ~/go/pkg/mod/github.com/aws-samples/sample-aws-dax-go-v2@v1.0.0/try_dax.go -service dax -command query -endpoint my-cluster.l6fzcv.dax-clusters.us-east-1.amazonaws.com:8111
```

```
go run ~/go/pkg/mod/github.com/aws-samples/sample-aws-dax-go-v2@v1.0.0/try_dax.go -service dax -command scan -endpoint my-cluster.l6fzcv.dax-clusters.us-east-1.amazonaws.com:8111
```

```
go run ~/go/pkg/mod/github.com/aws-samples/sample-aws-dax-go-v2@v1.0.0/try_dax.go -service dax -command paginated-scan -endpoint my-cluster.l6fzcv.dax-clusters.us-east-1.amazonaws.com:8111
```

```
go run ~/go/pkg/mod/github.com/aws-samples/sample-aws-dax-go-v2@v1.0.0/try_dax.go -service dax -command paginated-query -endpoint my-cluster.l6fzcv.dax-clusters.us-east-1.amazonaws.com:8111
```

```
go run ~/go/pkg/mod/github.com/aws-samples/sample-aws-dax-go-v2@v1.0.0/try_dax.go -service dax -command paginated-batch-get -endpoint my-cluster.l6fzcv.dax-clusters.us-east-1.amazonaws.com:8111
```

Look at the rest of the output, and take note of the timing information.
The elapsed times for `GetItem`, `Query`, and
`Scan` should be significantly lower with DAX than with
DynamoDB. 6. Run the following Golang program to delete
`TryDaxGoTable`.

```
go run ~/go/pkg/mod/github.com/aws-samples/sample-aws-dax-go-v2@v1.0.0/try_dax.go -service dynamodb -command delete-table
```

## Features

not in parity with AWS SDK for Go V2

Middleware Stack – DAX Go V2 doesn’t support the use of Middleware
Stacks through APIoptions. For more information, see [Customizing the AWS SDK for Go v2 Client Requests with Middleware](../../../sdk-for-go/v2/developer-guide/middleware.md#:~:text=You%20can%20customize%20AWS%20SDK,step's%20input%20and%20output%20types "../../../sdk-for-go/v2/developer-guide/middleware.md#:~:text=You%20can%20customize%20AWS%20SDK,step's%20input%20and%20output%20types").

Example:

```
// Custom middleware implementation
type customSerializeMiddleware struct{}
// ID returns the identifier for the middleware
func (m *customSerializeMiddleware) ID() string {
    return "CustomMiddleware"
}
// HandleSerialize implements the serialize middleware handler
func (m *customSerializeMiddleware) HandleSerialize(
    ctx context.Context,
    in middleware.SerializeInput,
    next middleware.SerializeHandler,
) (
    out middleware.SerializeOutput,
    metadata middleware.Metadata,
    err error,
) {
    // Add your custom logic here before the request is serialized
    fmt.Printf("Executing custom middleware for request: %v\n", in)
    // Call the next handler in the middleware chain
    return next.HandleSerialize(ctx, in)
}

func executeGetItem(ctx context.Context) error {
    client, err := initItemClient(ctx)
    if err != nil {
        os.Stderr.WriteString(fmt.Sprintf("failed to initialize client: %v\n", err))
        return err
    }

    st := time.Now()
    for c := 0; c < iterations; c++ {
        for i := 0; i < pkMax; i++ {
            for j := 0; j < skMax; j++ {
                // Create key using attributevalue.Marshal for type safety
                pk, err := attributevalue.Marshal(fmt.Sprintf("%s_%d", keyPrefix, i))
                if err != nil {
                    return fmt.Errorf("error marshaling pk: %v", err)
                }
                sk, err := attributevalue.Marshal(fmt.Sprintf("%d", j))
                if err != nil {
                    return fmt.Errorf("error marshaling sk: %v", err)
                }
                key := map[string]types.AttributeValue{
                    "pk": pk,
                    "sk": sk,
                }
                in := &dynamodb.GetItemInput{
                    TableName: aws.String(table),
                    Key:       key,
                }

                // Custom middleware option
                customMiddleware := func(o *dynamodb.Options) {
                    o.APIOptions = append(o.APIOptions, func(stack *middleware.Stack) error {
                        // Add custom middleware to the stack
                        return stack.Serialize.Add(&customSerializeMiddleware{}, middleware.After)
                    })
                }

                // Apply options to the GetItem call
                out, err := client.GetItem(ctx, in, customMiddleware)
                if err != nil {
                    return err
                }
                writeVerbose(out)
            }
        }
    }
    d := time.Since(st)
    os.Stdout.WriteString(fmt.Sprintf("Total Time: %v, Avg Time: %v\n", d, d/iterations))
    return nil
}
```

Output:

```
failed to execute command: custom middleware through APIOptions is not supported in DAX client
exit status 1
```
