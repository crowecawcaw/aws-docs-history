

# Create a Valkey serverless cache with a public endpoint
<a name="serverless-public-endpoints-chapter"></a>

With a public endpoint, you can connect to an ElastiCache Serverless cache directly over the internet without a VPC. Public endpoints are available on ElastiCache Serverless for Valkey 9.0 or later.

## Prerequisites
<a name="create-serverless-cache-public-endpoint-prerequisites"></a>
+ An AWS account with permissions to create ElastiCache resources.
+ Either `AdministratorAccess`, or IAM permissions that include `elasticache:CreateServerlessCache`. If you plan to create a custom user group instead of using the default, you also need `elasticache:CreateUser` and `elasticache:CreateUserGroup`.
+ Your IAM identity must have permission to create caches with a public endpoint. This permission can be restricted using the `elasticache:ConnectionType` condition key. For more information, see [Example Policies: Using Conditions for Fine-Grained Parameter Control](IAM.ConditionKeys.md#IAM.ExamplePolicies).
+ The AWS CLI version 2 installed and configured, for the CLI steps.

With ElastiCache, you can use the system-managed IAM user (`default.iam-user`) and user group (`default.iam-user-group`) to get started without creating custom users. To use a custom user group, first create a user group where all users use IAM authentication, then create the cache.

------
#### [ AWS Management Console ]

1. Open the ElastiCache console at [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/). If prompted, sign in.

1. Choose **Get started** to open the Create cache page.  
![The ElastiCache console home page with the Get started button.](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/images/create-pe-console-step2-get-started.png)

1. Under **Engine**, choose **Valkey**.  
![The Engine section of the Create cache page with Valkey selected.](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/images/create-pe-console-step3-engine-valkey.png)

1. Under **Deployment option**, choose **Serverless**.  
![The Deployment option section with Serverless selected.](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/images/create-pe-console-step4-deployment-serverless.png)

1. Under **Settings**, enter a **Name** for your cache. Optionally, enter a **Description**.  
![The Settings section showing the Name and Description fields.](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/images/create-pe-console-step5-settings-name.png)

1. Under **Engine version**, keep the default selected or choose **9** or later.  
![The Engine version control with version 9 selected.](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/images/create-pe-console-step6-engine-version.png)

1. For **Connection type**, choose **Public**.  
![The Connection type section with Public selected.](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/images/create-pe-console-step7-connection-type-public.png)

1. By default, ElastiCache uses recommended settings that work for most workloads. Choose **Customize default settings** if you need to change the network type, adjust cache usage limits, or select a different user group. The default user group is `default.iam-user-group`. All users in the group must use IAM authentication.  
![The Customize default settings area showing network type, security settings, and user group.](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/images/create-pe-console-step8-customize-settings.png)

1. (Optional) Under **Tags**, choose **Add new tag** and add tags to search and filter your caches, or track your AWS costs.  
![The Tags section with the Add new tag button.](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/images/create-pe-console-step9-tags.png)

1. Choose **Create**. After submission, you are redirected to the Cache details page, where the cache status is shown as **Creating**.  
![The Cache details page showing the cache status as Creating.](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/images/create-pe-console-step10-create.png)

1. Wait until the **Status** on the Cache details page changes from **Creating** to **Available** before connecting to the cache. The page refreshes automatically when the cache is ready.  
![The Cache details page showing the cache status changed to Available.](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/images/create-pe-console-step11-status-available.png)

------
#### [ AWS CLI ]

Run the following command to create a cache with a public endpoint using the system-managed default IAM user group:

```
aws elasticache create-serverless-cache \
    --serverless-cache-name my-public-cache \
    --engine valkey \
    --major-engine-version 9 \
    --connection-type public \
    --user-group-id default.iam-user-group
```

The command returns a response that includes the cache endpoint:

```
{
    "ServerlessCache": {
        "ServerlessCacheName": "my-public-cache",
        "Status": "creating",
        "Engine": "valkey",
        "MajorEngineVersion": "9",
        "ConnectionType": "public",
        "Endpoint": {
            "Address": "my-public-cache-x2e9hv.public.serverless.use1.cache.amazonaws.com",
            "Port": 6379
        },
        "UserGroupId": "default.iam-user-group"
    }
}
```

Note the `Endpoint.Address` value. You use this value to connect to your cache.

To use a custom user group instead of the default, replace `default.iam-user-group` with your user group ID. All users in the user group must use IAM authentication.

------
#### [ AWS SDK ]

The following examples create a cache with a public endpoint.

**Python (boto3)**

```
import boto3

client = boto3.client("elasticache", region_name="us-east-1")

response = client.create_serverless_cache(
    ServerlessCacheName="my-public-cache",
    Engine="valkey",
    MajorEngineVersion="9",
    ConnectionType="public",
    UserGroupId="default.iam-user-group",
)

print(response["ServerlessCache"]["Endpoint"]["Address"])
```

**JavaScript (AWS SDK v3)**

```
import {
  ElastiCacheClient,
  CreateServerlessCacheCommand
} from "@aws-sdk/client-elasticache";

const client = new ElastiCacheClient({ region: "us-east-1" });

const response = await client.send(new CreateServerlessCacheCommand({
  ServerlessCacheName: "my-public-cache",
  Engine: "valkey",
  MajorEngineVersion: "9",
  ConnectionType: "public",
  UserGroupId: "default.iam-user-group",
}));

console.log(response.ServerlessCache?.Endpoint?.Address);
```

**Java (AWS SDK v2)**

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.elasticache.ElastiCacheClient;
import software.amazon.awssdk.services.elasticache.model.CreateServerlessCacheRequest;
import software.amazon.awssdk.services.elasticache.model.CreateServerlessCacheResponse;

try (ElastiCacheClient client = ElastiCacheClient.builder()
        .region(Region.US_EAST_1)
        .build()) {
    CreateServerlessCacheResponse response = client.createServerlessCache(
        CreateServerlessCacheRequest.builder()
            .serverlessCacheName("my-public-cache")
            .engine("valkey")
            .majorEngineVersion("9")
            .connectionType("public")
            .userGroupId("default.iam-user-group")
            .build());
    System.out.println(response.serverlessCache().endpoint().address());
}
```

------

After your cache is available, see [Connect to a cache with a public endpoint](connecting-public-endpoint.md).