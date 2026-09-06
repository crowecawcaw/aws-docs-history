

# Migrating to DAX Node.js SDK V3
<a name="DAX.client.run-application-nodejs-3-migrating"></a>

This migration guide will help you transition your existing DAX Node.js applications. The new SDK requires Node.js 18 or higher and introduces several important changes in how you'll structure your DynamoDB Accelerator code. This guide will walk you through the key differences, including syntax changes, new import methods, and updated asynchronous programming patterns.

## V2 Node.js DAX usage
<a name="DAX.client.run-application-nodejs-3-migrating-V2-usage"></a>

```
const AmazonDaxClient = require('amazon-dax-client');
const AWS = require('aws-sdk');

var region = "us-west-2";

AWS.config.update({
  region: region,
});

var client = new AWS.DynamoDB.DocumentClient();

if (process.argv.length > 2) {
  var dax = new AmazonDaxClient({
    endpoints: [process.argv[2]],
    region: region,
  });
  client = new AWS.DynamoDB.DocumentClient({ service: dax });
}

// Make Get Call using Dax
var params = {
    TableName: 'TryDaxTable',
    pk: 1,
    sk: 1
}
client.get(params, function (err, data) {
    if (err) {
        console.error(
            "Unable to read item. Error JSON:",
            JSON.stringify(err, null, 2)
          );
    } else {
        console.log(data);
    }
});
```

## V3 Node.js DAX usage
<a name="DAX.client.run-application-nodejs-3-migrating-V3-dax-usage"></a>

For Using DAX Node.js V3 Node version 18 or above is the preferred version. To move to Node 18, use the following:

```
import { DaxDocument } from '@amazon-dax-sdk/lib-dax';
import { DynamoDBDocument } from '@aws-sdk/lib-dynamodb';
import { DynamoDBClient } from '@aws-sdk/client-dynamodb';

let client: DynamoDBDocument | DaxDocument = DynamoDBDocument.from(
  new DynamoDBClient({ region: 'us-west-2' })
);

if (process.argv.length > 2) {
  client = new DaxDocument({
    endpoints: [process.argv[2]],
    region: 'us-west-2',
  });
}

const params = {
  TableName: 'TryDaxTable',
  Key: { pk: 1, sk: 1 },
};

try {
  const results = await client.get(params);
  console.log(results);
} catch (err) {
  console.error(err);
}
```