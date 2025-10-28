# Neptune Public Endpoints

## Overview

Amazon Neptune clusters are typically deployed within your VPC and can only be accessed from within that VPC.
This requires configuring applications and development environments within the VPC or using proxy services to connect
to the VPC, which increases setup time and costs.

Public endpoints simplify this experience by allowing direct connections to Neptune over the internet, making
it easier to get started with graph databases without specialized networking knowledge.

## When to use public endpoints

Consider using public endpoints in the following scenarios:

- You want to quickly test Neptune in a development or test environment without complex network configuration
- You don't have specialized AWS networking knowledge
- Your application's security posture doesn't require a private VPC
- You need to connect to Neptune from your local development environment

## Security considerations

When using public endpoints, keep these security considerations in mind:

- IAM authentication is required for clusters with public endpoints enabled.
- Access to the database is controlled by the security group it uses.
- You can restrict which IP addresses can connect to your cluster.
- You can use IAM policies to control who can create or modify clusters with public access. See:
  [Restricting public access creation](#neptune-public-endpoints-restrict-access "#neptune-public-endpoints-restrict-access")

## Enabling public endpoints

By default, new Neptune databases are created with public endpoints disabled. You must explicitly enable
public access when creating or modifying a cluster.

Public endpoints are supported from Neptune engine release version 1.4.6.x. You need to upgrade existing clusters
to at least this version to use this feature.

Public endpoint setting is available on the Neptune instance and not the Neptune cluster. Hence, a Neptune
cluster can exist with some instances with public endpoints and some with not. However, we don't recommend having such
a setting. For more information on this refer to:
[How public endpoints work](#neptune-public-endpoints-how-they-work "#neptune-public-endpoints-how-they-work")

## Prerequisites

### IAM authentication setting on the Neptune cluster

Before enabling public endpoints on a Neptune instance, ensure your cluster supports IAM authentication.
If not, enable it using the following command:

```
aws neptune modify-db-cluster \
  --region us-west-2 \
  --engine graphdb \
  --engine-version 1.4.6.x \
  --db-cluster-identifier neptune-public-endpoint \
  --enable-iam-database-authentication
```

### Network settings

1. Ensure your VPC has subnets that enable public routing (has an entry for an internet gateway in the route
   table of the subnets). If you don't provide a `db-subnet-group-name` parameter while creating the
   cluster, the default subnet group is picked for the cluster creation.
2. Make sure the security group attached to the cluster allows inbound traffic for the allowed IP ranges and
   the allowed ports. For example, if you want to allow TCP traffic from all IPs to connect to the Neptune
   instance running on port 8182, the inbound rule should have:
   1. Type: All TCP
   2. Protocol: TCP
   3. Port range: 8182
   4. CIDR block: 0.0.0.0/0

###### Note

Although you can set the CIDR block range to 0.0.0.0/0, we recommend reducing this to a specific IP range of
your client application for a better security posture.

## Creating a new instance with public endpoints

You can create a new Neptune instance with public endpoints using the AWS Management Console, AWS CLI, or AWS
SDK.

Using the AWS CLI:

```
aws neptune create-db-instance \
  --region us-west-2 \
  --engine graphdb \
  --engine-version 1.4.6.x \
  --db-cluster-identifier neptune-public-endpoint \
  --publicly-accessible
```

## Modifying an existing instance for public access

To modify an existing Neptune instance to enable public access:

```
aws neptune modify-db-instance \
  --region us-west-2 \
  --engine graphdb \
  --engine-version 1.4.6.x \
  --db-instance-identifier neptune-public-endpoint \
  --publicly-accessible
```

###### Note

Public access is enabled at the instance level, not the cluster level. To ensure your cluster is always accessible
via public endpoints, all instances in the cluster must have public access enabled.

## Using the public endpoints

To check if your database is reachable, check the status using the AWS CLI `NeptuneData` API:

```
aws neptunedata get-engine-status \
  --endpoint-url https://my-cluster-name.cluster-abcdefgh1234.us-east-1.neptune.amazonaws.com:8182
```

If the database is accessible, the response is like:

```
{
    "status": "healthy",
    "startTime": "Sun Aug 10 06:54:15 UTC 2025",
    "dbEngineVersion": "1.4.6.0.R1",
    "role": "writer",
    "dfeQueryEngine": "viaQueryHint",
    "gremlin": {
        "version": "tinkerpop-3.7.1"
    },
    "sparql": {
        "version": "sparql-1.1"
    },
    "opencypher": {
        "version": "Neptune-9.0.20190305-1.0"
    },
    "labMode": {
        "ObjectIndex": "disabled",
        "ReadWriteConflictDetection": "enabled"
    },
    "features": {
        "SlowQueryLogs": "disabled",
        "InlineServerGeneratedEdgeId": "disabled",
        "ResultCache": {
            "status": "disabled"
        },
        "IAMAuthentication": "disabled",
        "Streams": "disabled",
        "AuditLog": "disabled"
    },
    "settings": {
        "StrictTimeoutValidation": "true",
        "clusterQueryTimeoutInMs": "120000",
        "SlowQueryLogsThreshold": "5000"
    }
}
```

## Examples of how to query the database

### AWS CLI

```
aws neptunedata execute-open-cypher-query \
--open-cypher-query "MATCH (n) RETURN n LIMIT 10" \
--endpoint-url https://my-cluster-name.cluster-abcdefgh1234.us-east-1.neptune.amazonaws.com:8182
```

### Python

```
import boto3
import json
from botocore.config import Config

# Configuration - Replace with your actual Neptune cluster details
cluster_endpoint = "my-cluster-name.cluster-abcdefgh1234.my-region.neptune.amazonaws.com"
port = 8182
region = "my-region"

# Configure Neptune client
# This disables retries and sets the client timeout to infinite
#     (relying on Neptune's query timeout)
endpoint_url = f"https://{cluster_endpoint}:{port}"
config = Config(
    region_name=region,
    retries={'max_attempts': 1},
    read_timeout=None
)

client = boto3.client("neptunedata", config=config, endpoint_url=endpoint_url)

cypher_query = "MATCH (n) RETURN n LIMIT 5"
try:
    response = client.execute_open_cypher_query(openCypherQuery=cypher_query)
    print("openCypher Results:")
    for item in response.get('results', []):
        print(f"  {item}")
except Exception as e:
    print(f"openCypher query failed: {e}")
```

### JavaScript

```
import {
    NeptunedataClient,
    GetPropertygraphSummaryCommand
} from "@aws-sdk/client-neptunedata";
import { inspect } from "util";
import { NodeHttpHandler } from "@smithy/node-http-handler";

/**
 * Main execution function
 */
async function main() {
    // Configuration - Replace with your actual Neptune cluster details
    const clusterEndpoint = 'my-cluster-name.cluster-abcdefgh1234.my-region.neptune.amazonaws.com';
    const port = 8182;
    const region = 'my-region';

    // Configure Neptune client
    // This disables retries and sets the client timeout to infinite
    //     (relying on Neptune's query timeout)
    const endpoint = `https://${clusterEndpoint}:${port}`;
    const clientConfig = {
        endpoint: endpoint,
        sslEnabled: true,
        region: region,
        maxAttempts: 1,  // do not retry
        requestHandler: new NodeHttpHandler({
            requestTimeout: 0  // no client timeout
        })
    };

    const client = new NeptunedataClient(clientConfig);
    try {
        try {
            const command = new GetPropertygraphSummaryCommand({ mode: "basic" });
            const response = await client.send(command);
            console.log("Graph Summary:", inspect(response.payload, { depth: null }));
        } catch (error) {
            console.log("Property graph summary failed:", error.message);
        }
    } catch (error) {
        console.error("Error in main execution:", error);
    }
}

// Run the main function
main().catch(console.error);
```

### Go

```
package main
import (
    "context"
    "fmt"
    "github.com/aws/aws-sdk-go-v2/aws"
    "github.com/aws/aws-sdk-go-v2/config"
    "github.com/aws/aws-sdk-go-v2/service/neptunedata"
    "os"
    "encoding/json"
    "net/http"
)

func main() {
    // Configuration - Replace with your actual Neptune cluster details
    clusterEndpoint := "my-cluster-name.cluster-abcdefgh1234.my-region.neptune.amazonaws.com"
    port := 8182
    region := "my-region"

    // Configure Neptune client
    // Configure HTTP client with no timeout
    //    (relying on Neptune's query timeout)
    endpoint := fmt.Sprintf("https://%s:%d", clusterEndpoint, port)
    // Load AWS SDK configuration
    sdkConfig, _ := config.LoadDefaultConfig(
        context.TODO(),
        config.WithRegion(region),
        config.WithHTTPClient(&http.Client{Timeout: 0}),
    )

    // Create Neptune client with custom endpoint
    client := neptunedata.NewFromConfig(sdkConfig, func(o *neptunedata.Options) {
        o.BaseEndpoint = aws.String(endpoint)
        o.Retryer = aws.NopRetryer{} // Do not retry calls if they fail
    })

    gremlinQuery := "g.addV('person').property('name','charlie').property(id,'charlie-1')"
    serializer := "application/vnd.gremlin-v1.0+json;types=false"

    gremlinInput := &neptunedata.ExecuteGremlinQueryInput{
        GremlinQuery: &gremlinQuery,
        Serializer:   &serializer,
    }
    gremlinResult, err := client.ExecuteGremlinQuery(context.TODO(), gremlinInput)
    if err != nil {
        fmt.Printf("Gremlin query failed: %v\n", err)
    } else {
        var resultMap map[string]interface{}
        err = gremlinResult.Result.UnmarshalSmithyDocument(&resultMap)
        if err != nil {
            fmt.Printf("Error unmarshaling Gremlin result: %v\n", err)
        } else {
            resultJSON, _ := json.MarshalIndent(resultMap, "", "  ")
            fmt.Printf("Gremlin Result: %s\n", string(resultJSON))
        }
    }
}
```

## How public endpoints work

When a Neptune instance is publicly accessible:

- Its DNS endpoint resolves to the private IP address from within the DB cluster's VPC.
- It resolves to the public IP address from outside of the cluster's VPC.
- Access is controlled by the security group assigned to the cluster.
- Only instances that are publicly accessible can be accessed via the internet.

### Reader endpoint behavior

- If all reader instances are publicly accessible, the reader endpoint will always resolve over the public
  internet.
- If only some reader instances are publicly accessible, the reader endpoint will resolve publicly only
  if it selects a publicly accessible instance to serve the read query.

### Cluster endpoint behavior

- The DB cluster endpoint always resolves to the instance endpoint of the writer.
- If public endpoint is enabled on the writer instance, the cluster endpoint will be publicly
  accessible, otherwise it won't be.

### Behavior after cluster failover

- A Neptune cluster can have instances on different public accessible setting.
- If a cluster has a public writer and a non-public reader, post a cluster failover, the new writer
  (previous reader) becomes non-public and the new reader (previous writer) becomes public.

## Network configuration requirements

For public endpoints to work properly:

1. The Neptune instances must be in public subnets within your VPC.
2. The route tables associated with these subnets must have a route to an internet gateway for 0.0.0.0/0.
3. The security group must allow access from the public IP addresses or CIDR ranges you want to grant access to.

## Restricting public access creation

You can use IAM policies to restrict who can create or modify Neptune clusters with public access. The
following example policy denies the creation of Neptune instances with public access:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [
 "rds:CreateDBInstance",
 "rds:ModifyDBInstance",
 "rds:RestoreDBInstanceFromDBSnapshot",
 "rds:RestoreDBInstanceToPointInTime"
 ],
 "Resource": "*",
 "Condition": {
 "Bool": {
 "rds:PubliclyAccessible": true
 }
 }
 }
 ]
}`

```

More about the `rds:PublicAccessEnabled` IAM condition key:
[Amazon RDS Service Authorization Reference](../../../service-authorization/latest/reference/list_amazonrds.md#amazonrds-rds_PubliclyAccessible "../../../service-authorization/latest/reference/list_amazonrds.md#amazonrds-rds_PubliclyAccessible")

## AWS CloudFormation support

You can use AWS CloudFormation to launch Neptune clusters with public endpoints enabled by specifying the
`PubliclyAccessible` parameter in your AWS CloudFormation template.

## Compatibility with Neptune features

A cluster with public endpoints enabled supports all Neptune features that a VPC-only cluster supports,
including:

- Neptune workbench
- Full text search integration
- Neptune Streams
- Custom endpoints
- Neptune Serverless
- Graph Explorer

## Pricing

Public endpoints are available at no additional cost beyond standard Neptune pricing. However, connecting from
your local environment to Neptune over a public IP might incur increased data transfer costs.
