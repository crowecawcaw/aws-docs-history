

# Creating clusters with resource-based policies
<a name="rbp-create-cluster"></a>

You can attach resource-based policies when creating a new cluster to ensure access controls are in place from the start. Each cluster can have a single inline policy attached directly to the cluster.

## AWS Management Console
<a name="rbp-create-cluster-console"></a>

**To add a resource-based policy during cluster creation**

1. Sign in to the AWS Management Console and open the Aurora DSQL console at [https://console.aws.amazon.com/dsql/](https://console.aws.amazon.com/dsql).

1. Choose **Create cluster**.

1. Configure your cluster name, tags, and multi-region settings as needed.

1. In the **Cluster settings** section, locate the **Resource-based policy** option.

1. Turn on **Add resource-based policy**.

1. Enter your policy document in the JSON editor. For example, to block public internet access:

   ```
   {
     "Version": "2012-10-17",		 	 	 
     "Statement": [
       {
         "Effect": "Deny",
         "Principal": {
           "AWS": "*"
         },
         "Resource": "*",
         "Action": [
           "dsql:DbConnect",
           "dsql:DbConnectAdmin"
         ],
         "Condition": {
           "Null": {
             "aws:SourceVpc": "true"
           }
         }
       }
     ]
   }
   ```

1. You can use **Edit statement** or **Add new statement** to build your policy.

1. Complete the remaining cluster configuration and choose **Create cluster**.

## AWS CLI
<a name="rbp-create-cluster-cli"></a>

Use the `--policy` parameter when creating a cluster to attach an inline policy:

```
aws dsql create-cluster --policy '{
    "Version": "2012-10-17",		 	 	 
    "Statement": [{
        "Effect": "Deny",
        "Principal": {"AWS": "*"},
        "Resource": "*",
        "Action": ["dsql:DbConnect", "dsql:DbConnectAdmin"],
        "Condition": {
            "StringNotEquals": { "aws:SourceVpc": "vpc-1a2b3c4d5e6f7a8b9" }
        }
    }]
}'
```

## AWS SDKs
<a name="rbp-create-cluster-sdk"></a>

------
#### [ Python ]

```
import boto3
import json

client = boto3.client('dsql')

policy = {
    "Version": "2012-10-17",		 	 	 
    "Statement": [{
        "Effect": "Deny",
        "Principal": {"AWS": "*"},
        "Resource": "*",
        "Action": ["dsql:DbConnect", "dsql:DbConnectAdmin"],
        "Condition": {
            "StringNotEquals": { "aws:SourceVpc": "vpc-1a2b3c4d5e6f7a8b9" }
        }
    }]
}

response = client.create_cluster(
    policy=json.dumps(policy)
)

print(f"Cluster created: {response['identifier']}")
```

------
#### [ Java ]

```
import software.amazon.awssdk.services.dsql.DsqlClient;
import software.amazon.awssdk.services.dsql.model.CreateClusterRequest;
import software.amazon.awssdk.services.dsql.model.CreateClusterResponse;

DsqlClient client = DsqlClient.create();

String policy = """
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [{
    "Effect": "Deny",
    "Principal": {"AWS": "*"},
    "Resource": "*",
    "Action": ["dsql:DbConnect", "dsql:DbConnectAdmin"],
    "Condition": {
      "StringNotEquals": { "aws:SourceVpc": "vpc-1a2b3c4d5e6f7a8b9" }
    }
  }]
}
""";

CreateClusterRequest request = CreateClusterRequest.builder()
    .policy(policy)
    .build();

CreateClusterResponse response = client.createCluster(request);
System.out.println("Cluster created: " + response.identifier());
```

------