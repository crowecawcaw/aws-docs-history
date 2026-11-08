

# Adding and editing resource-based policies for clusters
<a name="rbp-attach-policy"></a>

When you attach a policy or create a cluster with one, the policy must meet these requirements:
+ It's no longer than 20,480 characters.
+ It doesn't include service principals (the `Service` key in a `Principal` element).
+ Each of its statements includes a `Principal` element and a `Resource` element. Aurora DSQL doesn't support `NotPrincipal` or `NotResource`.
+ It doesn't grant public access. For more information, see [Blocking public access with resource-based policies in Aurora DSQL](rbp-block-public-access.md).
+ It doesn't deny you both `dsql:PutClusterPolicy` and `dsql:DeleteClusterPolicy`.

The last requirement makes sure that you can still change or remove the policy after you attach it. To attach a policy that denies you both actions anyway, set `bypassPolicyLockoutSafetyCheck` to `true`, or pass `--bypass-policy-lockout-safety-check` in the AWS CLI.

## AWS Management Console
<a name="rbp-attach-console"></a>

**To add a resource-based policy to an existing cluster**

1. Sign in to the AWS Management Console and open the Aurora DSQL console at [https://console.aws.amazon.com/dsql/](https://console.aws.amazon.com/dsql).

1. Choose your cluster from the cluster list to open the cluster details page.

1. Choose the **Permissions** tab.

1. In the **Resource-based policy** section, choose **Add policy**.

1. Enter your policy document in the JSON editor. You can use **Edit statement** or **Add new statement** to build your policy.

1. Choose **Add policy**.

**To edit an existing resource-based policy**

1. Sign in to the AWS Management Console and open the Aurora DSQL console at [https://console.aws.amazon.com/dsql/](https://console.aws.amazon.com/dsql).

1. Choose your cluster from the cluster list to open the cluster details page.

1. Choose the **Permissions** tab.

1. In the **Resource-based policy** section, choose **Edit**.

1. Modify the policy document in the JSON editor. You can use **Edit statement** or **Add new statement** to update your policy.

1. Choose **Save changes**.

## AWS CLI
<a name="rbp-attach-cli"></a>

Use the `put-cluster-policy` command to attach a new policy or update an existing policy on a cluster:

```
aws dsql put-cluster-policy --identifier your_cluster_id --policy '{
    "Version": "2012-10-17",		 	 	 
    "Statement": [{
        "Effect": "Deny",
        "Principal": {"AWS": "*"},
        "Resource": "*",
        "Action": ["dsql:DbConnect", "dsql:DbConnectAdmin"],
        "Condition": {
            "Null": { "aws:SourceVpc": "true" }
        }
    }]
}'
```

To avoid overwriting a change that someone else made after you read the policy, pass the `policyVersion` value from `get-cluster-policy` in `--expected-policy-version`. If the policy changed after you read it, the command fails with a `ConflictException`.

## AWS SDKs
<a name="rbp-attach-sdk"></a>

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
            "Null": {"aws:SourceVpc": "true"}
        }
    }]
}

response = client.put_cluster_policy(
    identifier='your_cluster_id',
    policy=json.dumps(policy)
)
```

------
#### [ Java ]

```
import software.amazon.awssdk.services.dsql.DsqlClient;
import software.amazon.awssdk.services.dsql.model.PutClusterPolicyRequest;

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
      "Null": {"aws:SourceVpc": "true"}
    }
  }]
}
""";

PutClusterPolicyRequest request = PutClusterPolicyRequest.builder()
    .identifier("your_cluster_id")
    .policy(policy)
    .build();

client.putClusterPolicy(request);
```

------