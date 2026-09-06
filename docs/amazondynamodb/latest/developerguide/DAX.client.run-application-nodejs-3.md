

# Node.js and DAX
<a name="DAX.client.run-application-nodejs-3"></a>

The DAX SDK for Node.js v3.x is compatible with [AWS SDK for Node.js v3.x](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/introduction/). The DAX SDK for Node.js v3.x supports the use of [aggregated](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/introduction/#high-level-concepts) clients. Note that DAX doesn't support the creation of bare-bones clients. For more information about unsupported features, see [Features not in parity with AWS SDK V3](#DAX.client.run-application-nodejs-3-not-in-parity).

Follow these steps to run the Node.js sample application on your Amazon EC2 instance.

**To run the Node.js sample for DAX**

1. Set up Node.js on your Amazon EC2 instance, as follows:

   1. Install node version manager (`nvm`).

      ```
      curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
      ```

   1. Use nvm to install Node.js.

      ```
      nvm install 18
      ```

   1. Use nvm to use Node 18

      ```
      nvm use 18
      ```

   1. Test that Node.js is installed and running correctly.

      ```
      node -e "console.log('Running Node.js ' + process.version)"
      ```

      This should display the following message.

      `Running Node.js v18.x.x`

1. Install the DaxDocument Node.js client using the node package manager (`npm`).

   ```
   npm install @amazon-dax-sdk/lib-dax
   ```

## TryDax sample code
<a name="DAX.client.run-application-nodejs-3-TryDax-sample-code"></a>

To evaluate the performance benefits of DynamoDB Accelerator (DAX), follow these steps to run a sample test that compares read operation times between standard DynamoDB and a DAX cluster.

1. After you've set up your workspace and installed the `lib-dax` as a dependency, copy [TryDax.js](DAX.client.tutorial-TryDax.md) into your project.

1. Run the program against your DAX cluster. To determine the endpoint for your DAX cluster, choose one of the following: 
   +  **Using the DynamoDB console** — Choose your DAX cluster. The cluster endpoint is shown on the console, as in the following example.

     ```
     dax://my-cluster.l6fzcv.dax-clusters.us-east-1.amazonaws.com
     ```
   + **Using the AWS CLI** — Enter the following command.

     ```
     aws dax describe-clusters --query "Clusters[*].ClusterDiscoveryEndpoint"
     ```

     The cluster endpoint is shown in the output, as in the following example.

     ```
     {
         "Address": "my-cluster.l6fzcv.dax-clusters.us-east-1.amazonaws.com",
         "Port": 8111,
         "URL": "dax://my-cluster.l6fzcv.dax-clusters.us-east-1.amazonaws.com"
     }
     ```

1. Now run the program by specifying the cluster endpoint as a command line parameter.

   ```
   node TryDax.js dax://my-cluster.l6fzcv.dax-clusters.us-east-1.amazonaws.com
   ```

   You should see output similar to the following:

   ```
   Attempting to create table; please wait...
   Successfully created table. Table status: ACTIVE
   Writing data to the table...
   Writing 20 items for partition key:  1
   Writing 20 items for partition key:  2
   Writing 20 items for partition key:  3
   ...
   Running GetItem Test
           Total time: 153555.10 µs - Avg time: 383.89 µs
           Total time: 44679.96 µs - Avg time: 111.70 µs
           Total time: 36885.86 µs - Avg time: 92.21 µs
           Total time: 32467.25 µs - Avg time: 81.17 µs
           Total time: 32202.60 µs - Avg time: 80.51 µs
   Running Query Test
           Total time: 14869.25 µs - Avg time: 2973.85 µs
           Total time: 3036.31 µs - Avg time: 607.26 µs
           Total time: 2468.92 µs - Avg time: 493.78 µs
           Total time: 2062.53 µs - Avg time: 412.51 µs
           Total time: 2178.22 µs - Avg time: 435.64 µs
   Running Scan Test
           Total time: 2395.88 µs - Avg time: 479.18 µs
           Total time: 2207.16 µs - Avg time: 441.43 µs
           Total time: 2443.14 µs - Avg time: 488.63 µs
           Total time: 2038.24 µs - Avg time: 407.65 µs
           Total time: 1972.17 µs - Avg time: 394.43 µs
   Running Pagination Test
   Scan Pagination
   [
     { pk: 1, sk: 1, someData: 'XXXXXXXXXX' },
     { pk: 1, sk: 2, someData: 'XXXXXXXXXX' },
     { pk: 1, sk: 3, someData: 'XXXXXXXXXX' }
   ]
   [
     { pk: 1, sk: 4, someData: 'XXXXXXXXXX' },
     { pk: 1, sk: 5, someData: 'XXXXXXXXXX' },
     { pk: 1, sk: 6, someData: 'XXXXXXXXXX' }
   ]
   ...
   Query Pagination
   [
     { pk: 1, sk: 1, someData: 'XXXXXXXXXX' },
     { pk: 1, sk: 2, someData: 'XXXXXXXXXX' },
     { pk: 1, sk: 3, someData: 'XXXXXXXXXX' }
   ]
   [
     { pk: 1, sk: 4, someData: 'XXXXXXXXXX' },
     { pk: 1, sk: 5, someData: 'XXXXXXXXXX' },
     { pk: 1, sk: 6, someData: 'XXXXXXXXXX' }
   ]
   ...
   Attempting to delete table; please wait...
   Successfully deleted table.
   ```

   Take note of the timing information. The number of microseconds required for the `GetItem`,`Query`,`Scan` tests.

1. In this case, you ran the programs against the DAX cluster. Now, you'll run the program again, this time against DynamoDB.

1. Now run the program again, but this time, without the cluster endpoint URL as a command line parameter.

   ```
   node TryDax.js
   ```

   Look at the output and take note of the timing information. The elapsed times for `GetItem`, `Query`, and `Scan` should be significantly lower with DAX as compared to DynamoDB.

## Features not in parity with AWS SDK V3
<a name="DAX.client.run-application-nodejs-3-not-in-parity"></a>
+ [Bare-bones](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/introduction/#high-level-concepts) clients – Dax Node.js V3 doesn’t support bare-bones clients. 

  ```
  const dynamoDBClient = new DynamoDBClient({ region: 'us-west-2' });
  const regularParams = {
      TableName: 'TryDaxTable',
      Key: {
          pk: 1,
          sk: 1
      }
  };
  // The DynamoDB client supports the send operation.
  const dynamoResult = await dynamoDBClient.send(new GetCommand(regularParams));
  
  // However, the DaxDocument client does not support the send operation.
  const daxClient = new DaxDocument({
      endpoints: ['your-dax-endpoint'],
      region: 'us-west-2',
  });
  
  const params = {
      TableName: 'TryDaxTable',
      Key: {
          pk: 1,
          sk: 1
      }
  };
  
  // This will throw an error - send operation is not supported for DAX. Please refer to documentation.
  const result = await daxClient.send(new GetCommand(params));
  console.log(result);
  ```
+ [Middleware Stack](https://aws.amazon.com/blogs/developer/middleware-stack-modular-aws-sdk-js/) – Dax Node.js V3 doesn’t support using Middleware functions.

  ```
  const dynamoDBClient = new DynamoDBClient({ region: 'us-west-2' });
  // The DynamoDB client supports the middlewareStack.
  dynamoDBClient.middlewareStack.add(
    (next, context) =>> async (args) => {
      console.log("Before operation:", args);
      const result = await next(args);
      console.log("After operation:", result);
      return result;
    },
    {
      step: "initialize", // or "build", "finalizeRequest", "deserialize"
      name: "loggingMiddleware",
    }
  );
  
  // However, the DaxDocument client does not support the middlewareStack.
  const daxClient = new DaxDocument({
      endpoints: ['your-dax-endpoint'],
      region: 'us-west-2',
  });
  
  // This will throw an error - custom middleware and middlewareStacks are not supported for DAX. Please refer to documentation.
  daxClient.middlewareStack.add(
    (next, context) => async (args) => {
      console.log("Before operation:", args);
      const result = await next(args);
      console.log("After operation:", result);
      return result;
    },
    {
      step: "initialize", // or "build", "finalizeRequest", "deserialize"
      name: "loggingMiddleware",
    }
  );
  ```