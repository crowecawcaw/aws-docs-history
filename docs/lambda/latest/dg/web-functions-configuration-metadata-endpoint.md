

# Using the metadata endpoint
<a name="web-functions-configuration-metadata-endpoint"></a>

The Lambda metadata endpoint is a local HTTP API within the execution environment. It returns metadata in a simple JSON format, including the Availability Zone (AZ) ID where the environment is running. Use it to route to same-AZ resources such as Amazon ElastiCache and Amazon RDS for lower latency. You can also use it to implement AZ-aware resilience patterns.

**Note**  
A Web Function runs a persistent web server rather than a per-invocation handler. Read the metadata endpoint once at application startup and cache the value, or read it per request if you need it in request context. Don't assume a fresh per-invocation handler. For a multi-Region Web Function, the endpoint reports the AZ within the AWS Region that is serving the request.

**Topics**
+ [Getting started](#web-functions-metadata-endpoint-getting-started)

## Getting started
<a name="web-functions-metadata-endpoint-getting-started"></a>

Powertools for AWS Lambda provides a utility for accessing the Lambda metadata endpoint. The utility caches the response after the first call. For more information, see [Metadata](https://docs.aws.amazon.com/powertools/typescript/latest/features/metadata/) in the *Powertools for AWS Lambda (TypeScript)* documentation.

Because Web Functions run on Node.js, the following example uses the Powertools for AWS Lambda metadata utility to read the AZ ID once at server startup and cache it for the life of the process. Run the following npm command to install the Powertools package and Express:

```
npm install @aws-lambda-powertools/commons express
```

The following example uses Express for illustration. The same approach works with any Node.js web framework; see [Supported web frameworks](web-functions-runtimes.md#web-functions-runtimes-frameworks). Read the AZ ID at startup and reuse the cached value when handling requests:

**Example Retrieving AZ ID with Powertools at startup (TypeScript)**  

```
import express from 'express';
import { getMetadata } from '@aws-lambda-powertools/commons/utils/metadata';

const app = express();

// Read the AZ ID once at startup and cache it for the life of the server.
const { AvailabilityZoneID: azId } = await getMetadata();

// Lambda provides the address to bind in AWS_LAMBDA_HTTP_ENDPOINT ("host:port").
// The fallback applies only when running locally.
const [host, port] = (process.env.AWS_LAMBDA_HTTP_ENDPOINT || 'localhost:3000').split(':');

app.get('/', (req, res) => {
  res.json({ azId });
});

app.listen(port, host, () => {
  console.log(`Server listening on ${host}:${port}, AZ: ${azId}`);
});
```

You can also call the metadata endpoint directly. Lambda automatically sets the `AWS_LAMBDA_METADATA_API` and `AWS_LAMBDA_METADATA_TOKEN` environment variables in every execution environment, and you include the token with the Bearer scheme in the `Authorization` header. For the endpoint URL, request and response formats, and error responses, see [Using the Lambda metadata endpoint](configuration-metadata-endpoint.md).

For example, read the metadata server address from `AWS_LAMBDA_METADATA_API` and send an authenticated GET request:

```
METADATA_ENDPOINT="http://${AWS_LAMBDA_METADATA_API}/2026-01-15/metadata/execution-environment"
RESPONSE=$(curl -s -H "Authorization: Bearer ${AWS_LAMBDA_METADATA_TOKEN}" "$METADATA_ENDPOINT")
AZ_ID=$(echo "$RESPONSE" | jq -r '.AvailabilityZoneID')
```

The endpoint returns `application/json`. For example: `{"AvailabilityZoneID": "use1-az1"}`.