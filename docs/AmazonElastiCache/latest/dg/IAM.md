# Using condition keys

You can specify conditions that determine how an IAM policy takes effect. In ElastiCache, you can use the `Condition` element of a JSON policy to compare keys in the request context with key values that you specify in your policy.
For more information, see [IAM JSON policy elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md").

To see a list of ElastiCache condition keys, see [Condition Keys for Amazon ElastiCache](../../../service-authorization/latest/reference/list_amazonelasticache.md#amazonelasticache-policy-keys "../../../service-authorization/latest/reference/list_amazonelasticache.md#amazonelasticache-policy-keys") in the
_Service Authorization Reference_.

For a list of global condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md").

**Using ElastiCache With AWS Global Condition Keys**

When using [AWS Global condition keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") that require ElastiCache's [Principal](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md#principal-services "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md#principal-services"), use an `OR` condition with _both_ Principals: `elasticache.amazonaws.com` and `ec.amazonaws.com`.

###### Note

If you do not add both Principals for ElastiCache, the intended “Allow” or “Deny” action will not be enforced correctly for any resource listed in your policy.

Example of policy with `aws:CalledVia` global condition key:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "ec2:*",
 "Resource": "*",
 "Condition": {
 "ForAnyValue:StringLike": {
 "aws:CalledVia": [
 "ec.amazonaws.com",
 "elasticache.amazonaws.com"
 ]
 }
 }
 }
 ]
}`

```

## Specifying Conditions: Using Condition Keys

To implement fine-grained control, you write an IAM permissions policy that specifies conditions to control a set of individual parameters on certain requests. You then apply the policy to IAM users, groups, or roles that you create using the IAM console.

To apply a condition, you add the condition information to the IAM policy statement. In the following example, you specify the condition that any node-based cluster created will be of node type `cache.r5.large`.

###### Note

- To construct `Condition` elements using condition keys of `String` type, use the case insensitive condition operators `StringEqualsIgnoreCase` or `StringNotEqualsIgnoreCase` to compare a key to a string value.
- ElastiCache processes the input arguments for `CacheNodeType` and `CacheParameterGroupName` in a case insensitive manner. For this reason, the string condition operators `StringEqualsIgnoreCase`, and `StringNotEqualsIgnoreCase` should be used in permissions policies that reference them.

The following shows an example of this permissions policy when using Valkey or Redis OSS.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "elasticache:CreateCacheCluster",
 "elasticache:CreateReplicationGroup"
 ],
 "Resource": [
 "arn:aws:elasticache:*:*:parametergroup:*",
 "arn:aws:elasticache:*:*:subnetgroup:*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "elasticache:CreateCacheCluster",
 "elasticache:CreateReplicationGroup"
 ],
 "Resource": [
 "arn:aws:elasticache:*:*:cluster:*",
 "arn:aws:elasticache:*:*:replicationgroup:*"
 ],
 "Condition": {
 "StringEquals": {
 "elasticache:CacheNodeType": [
 "cache.r5.large"
 ]
 }
 }
 }
 ]
}`

```

The following shows an example of this permissions policy when using Memcached.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "elasticache:CreateCacheCluster"
 ],
 "Resource": [
 "arn:aws:elasticache:*:*:parametergroup:*",
 "arn:aws:elasticache:*:*:subnetgroup:*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "elasticache:CreateCacheCluster"
 ],
 "Resource": [
 "arn:aws:elasticache:*:*:cluster:*"
 ],
 "Condition": {
 "StringEquals": {
 "elasticache:CacheNodeType": [
 "cache.r5.large"
 ]
 }
 }
 }
 ]
}`

```

For more information, see [Tagging your ElastiCache resources](Tagging-Resources.md "Tagging-Resources.md").

For more information on using policy condition operators, see [ElastiCache API permissions: Actions, resources, and conditions reference](IAM.md "IAM.md").

## Example Policies: Using Conditions for Fine-Grained Parameter Control

This section shows example policies for implementing fine-grained access control on the previously listed ElastiCache parameters.

1. **elasticache:MaximumDataStorage**:   Specify the maximum data storage of a serverless cache. Using the provided conditions, the customer can not create caches that can store more than a specific amount of data.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowDependentResources",
 "Effect": "Allow",
 "Action": [
 "elasticache:CreateServerlessCache"
 ],
 "Resource": [
 "arn:aws:elasticache:*:*:serverlesscachesnapshot:*",
 "arn:aws:elasticache:*:*:snapshot:*",
 "arn:aws:elasticache:*:*:usergroup:*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "elasticache:CreateServerlessCache"
 ],
 "Resource": [
 "arn:aws:elasticache:*:*:serverlesscache:*"
 ],
 "Condition": {
 "NumericLessThanEquals": {
 "elasticache:MaximumDataStorage": "30"
 },
 "StringEquals": {
 "elasticache:DataStorageUnit": "GB"
 }
 }
 }
 ]
}`

```

2. **elasticache:MaximumECPUPerSecond**:   Specify the maximum ECPU per second value of a serverless cache. Using the provided conditions, the customer can not create caches that can execute more than a specific number of ECPUs per second.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowDependentResources",
 "Effect": "Allow",
 "Action": [
 "elasticache:CreateServerlessCache"
 ],
 "Resource": [
 "arn:aws:elasticache:*:*:serverlesscachesnapshot:*",
 "arn:aws:elasticache:*:*:snapshot:*",
 "arn:aws:elasticache:*:*:usergroup:*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "elasticache:CreateServerlessCache"
 ],
 "Resource": [
 "arn:aws:elasticache:*:*:serverlesscache:*"
 ],
 "Condition": {
 "NumericLessThanEquals": {
 "elasticache:MaximumECPUPerSecond": "100000"
 }
 }
 }
 ]
}`

```

3. **elasticache:CacheNodeType**:   Specify which NodeType(s) a user can create. Using the provided conditions, the customer can specify a single or a range value for a node type.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "elasticache:CreateCacheCluster",
 "elasticache:CreateReplicationGroup"
 ],
 "Resource": [
 "arn:aws:elasticache:*:*:parametergroup:*",
 "arn:aws:elasticache:*:*:subnetgroup:*"
 ]
 },

 {
 "Effect": "Allow",
 "Action": [
 "elasticache:CreateCacheCluster",
 "elasticache:CreateReplicationGroup"
 ],
 "Resource": [
 "arn:aws:elasticache:*:*:cluster:*",
 "arn:aws:elasticache:*:*:replicationgroup:*"
 ],
 "Condition": {
 "StringEquals": {
 "elasticache:CacheNodeType": [
 "cache.t2.micro",
 "cache.t2.medium"
 ]
 }
 }
 }
 ]
}`

```

4. **elasticache:CacheNodeType**: With Memcached, specify which NodeType(s) a user can create. Using the provided conditions, the customer can specify a single or a range value for a node type.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "elasticache:CreateCacheCluster"
 ],
 "Resource": [
 "arn:aws:elasticache:*:*:parametergroup:*",
 "arn:aws:elasticache:*:*:subnetgroup:*"
 ]
 },

 {
 "Effect": "Allow",
 "Action": [
 "elasticache:CreateCacheCluster"
 ],
 "Resource": [
 "arn:aws:elasticache:*:*:cluster:*"
 ],
 "Condition": {
 "StringEquals": {
 "elasticache:CacheNodeType": [
 "cache.t2.micro",
 "cache.t2.medium"
 ]
 }
 }
 }
 ]
}`

```

5. **elasticache:NumNodeGroups**:   Create a replication group with fewer than 20 node groups.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "elasticache:CreateReplicationGroup"
 ],
 "Resource": [
 "arn:aws:elasticache:*:*:parametergroup:*",
 "arn:aws:elasticache:*:*:subnetgroup:*"
 ]
 },

 {
 "Effect": "Allow",
 "Action": [
 "elasticache:CreateReplicationGroup"
 ],
 "Resource": [
 "arn:aws:elasticache:*:*:replicationgroup:*"
 ],
 "Condition": {
 "NumericLessThanEquals": {
 "elasticache:NumNodeGroups": "20"
 }
 }
 }
 ]
}`

```

6. **elasticache:ReplicasPerNodeGroup**:   Specify the replicas per node between 5 and 10.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "elasticache:CreateReplicationGroup"
 ],
 "Resource": [
 "arn:aws:elasticache:*:*:parametergroup:*",
 "arn:aws:elasticache:*:*:subnetgroup:*"
 ]
 },

 {
 "Effect": "Allow",
 "Action": [
 "elasticache:CreateReplicationGroup"
 ],
 "Resource": [
 "arn:aws:elasticache:*:*:replicationgroup:*"
 ],
 "Condition": {
 "NumericGreaterThanEquals": {
 "elasticache:ReplicasPerNodeGroup": "5"
 },
 "NumericLessThanEquals": {
 "elasticache:ReplicasPerNodeGroup": "10"
 }
 }
 }
 ]
}`

```

7. **elasticache:EngineVersion**:   Specify usage of engine version 5.0.6.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "elasticache:CreateCacheCluster",
 "elasticache:CreateReplicationGroup"
 ],
 "Resource": [
 "arn:aws:elasticache:*:*:parametergroup:*",
 "arn:aws:elasticache:*:*:subnetgroup:*"
 ]
 },

 {
 "Effect": "Allow",
 "Action": [
 "elasticache:CreateCacheCluster",
 "elasticache:CreateReplicationGroup"
 ],
 "Resource": [
 "arn:aws:elasticache:*:*:cluster:*",
 "arn:aws:elasticache:*:*:replicationgroup:*"
 ],
 "Condition": {
 "StringEquals": {
 "elasticache:EngineVersion": "5.0.6"
 }
 }
 }
 ]
}`

```

8. **elasticache:EngineVersion**:   Specify usage of Memcached engine version 1.6.6

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "elasticache:CreateCacheCluster"
 ],
 "Resource": [
 "arn:aws:elasticache:*:*:parametergroup:*",
 "arn:aws:elasticache:*:*:subnetgroup:*"
 ]
 },

 {
 "Effect": "Allow",
 "Action": [
 "elasticache:CreateCacheCluster"
 ],
 "Resource": [
 "arn:aws:elasticache:*:*:cluster:*"
 ],
 "Condition": {
 "StringEquals": {
 "elasticache:EngineVersion": "1.6.6"
 }
 }
 }
 ]
}`

```

9. **elasticache:EngineType**:   Specify using a Valkey or Redis OSS engine only.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "elasticache:CreateCacheCluster",
 "elasticache:CreateReplicationGroup"
 ],
 "Resource": [
 "arn:aws:elasticache:*:*:parametergroup:*",
 "arn:aws:elasticache:*:*:subnetgroup:*"
 ]
 },

 {
 "Effect": "Allow",
 "Action": [
 "elasticache:CreateCacheCluster",
 "elasticache:CreateReplicationGroup"
 ],
 "Resource": [
 "arn:aws:elasticache:*:*:cluster:*",
 "arn:aws:elasticache:*:*:replicationgroup:*"
 ],
 "Condition": {
 "StringEquals": {
 "elasticache:EngineType": "redis"
 }
 }
 }
 ]
}`

```

10. **elasticache:AtRestEncryptionEnabled**:   Specify that replication groups would be created only with encryption enabled.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [

 {
 "Effect": "Allow",
 "Action": [
 "elasticache:CreateReplicationGroup"
 ],
 "Resource": [
 "arn:aws:elasticache:*:*:parametergroup:*",
 "arn:aws:elasticache:*:*:subnetgroup:*"
 ]
 },

 {
 "Effect": "Allow",
 "Action": [
 "elasticache:CreateReplicationGroup"
 ],
 "Resource": [
 "arn:aws:elasticache:*:*:replicationgroup:*"
 ],
 "Condition": {
 "Bool": {
 "elasticache:AtRestEncryptionEnabled": "true"
 }
 }
 }
 ]
}`

```

11. **elasticache:TransitEncryptionEnabled**
    1.  Set the `elasticache:TransitEncryptionEnabled` condition key
        to `false` for the [CreateReplicationGroup](../APIReference/API_CreateReplicationGroup.md "../APIReference/API_CreateReplicationGroup.md") action to specify that replication groups
        can only be created when TLS is not being used:

    JSON

    ```
    `{
     "Version":"2012-10-17",
     "Statement": [
     {
     "Effect": "Allow",
     "Action": [
     "elasticache:CreateReplicationGroup"
     ],
     "Resource": [
     "arn:aws:elasticache:*:*:parametergroup:*",
     "arn:aws:elasticache:*:*:subnetgroup:*"
     ]
     },

     {
     "Effect": "Allow",
     "Action": [
     "elasticache:CreateReplicationGroup"
     ],
     "Resource": [
     "arn:aws:elasticache:*:*:replicationgroup:*"
     ],
     "Condition": {
     "Bool": {
     "elasticache:TransitEncryptionEnabled": "false"
     }
     }
     }
     ]
    }`

    ```

    When the `elasticache:TransitEncryptionEnabled` condition key
    is set to `false` in a policy for the [CreateReplicationGroup](../APIReference/API_CreateReplicationGroup.md "../APIReference/API_CreateReplicationGroup.md")
    action, a `CreateReplicationGroup` request will be allowed only
    if TLS is not being used (that is, if the request does not include a
    `TransitEncryptionEnabled` parameter set to
    `true` or a `TransitEncryptionMode` parameter
    set to `required`. 2. Set the `elasticache:TransitEncryptionEnabled` conditon
    key to `true` for the [CreateReplicationGroup](../APIReference/API_CreateReplicationGroup.md "../APIReference/API_CreateReplicationGroup.md") action to specify that
    replication groups can only be created when TLS is being used:

    JSON

    ```
    `{
     "Version":"2012-10-17",
     "Statement": [
     {
     "Effect": "Allow",
     "Action": [
     "elasticache:CreateReplicationGroup"
     ],
     "Resource": [
     "arn:aws:elasticache:*:*:parametergroup:*",
     "arn:aws:elasticache:*:*:subnetgroup:*"
     ]
     },

     {
     "Effect": "Allow",
     "Action": [
     "elasticache:CreateReplicationGroup"
     ],
     "Resource": [
     "arn:aws:elasticache:*:*:replicationgroup:*"
     ],
     "Condition": {
     "Bool": {
     "elasticache:TransitEncryptionEnabled": "true"
     }
     }
     }
     ]
    }`

    ```

    When the `elasticache:TransitEncryptionEnabled` condition key
    is set to `true` in a policy for the [CreateReplicationGroup](../APIReference/API_CreateReplicationGroup.md "../APIReference/API_CreateReplicationGroup.md")
    action, a `CreateReplicationGroup` request will be allowed only
    if the request includes a `TransitEncryptionEnabled` parameter
    set to `true` and a `TransitEncryptionMode` parameter
    set to `required`. 3. Set `elasticache:TransitEncryptionEnabled` to `true`
    for the `ModifyReplicationGroup` action to specify that
    replication groups can only be modified when TLS is being used:

    JSON

    ```
    `{
     "Version":"2012-10-17",
     "Statement": [
     {
     "Effect": "Allow",
     "Action": [
     "elasticache:ModifyReplicationGroup"
     ],
     "Resource": [
     "arn:aws:elasticache:*:*:replicationgroup:*"
     ],
     "Condition": {
     "BoolIfExists": {
     "elasticache:TransitEncryptionEnabled": "true"
     }
     }
     }
     ]
    }`

    ```

    When the `elasticache:TransitEncryptionEnabled` condition key
    is set to `true` in a policy for the [ModifyReplicationGroup](../APIReference/API_ModifyReplicationGroup.md "../APIReference/API_ModifyReplicationGroup.md")
    action, a `ModifyReplicationGroup` request will be allowed only
    if the request includes a `TransitEncryptionMode` parameter
    set to `required`. The `TransitEncryptionEnabled` parameter
    set to `true` may optionally be included as well, but is
    not needed in this case to enable TLS.

12. **elasticache:AutomaticFailoverEnabled**:  
    Specify that replication groups would be created only with automatic failover enabled.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "elasticache:CreateReplicationGroup"
 ],
 "Resource": [
 "arn:aws:elasticache:*:*:parametergroup:*",
 "arn:aws:elasticache:*:*:subnetgroup:*"
 ]
 },

 {
 "Effect": "Allow",
 "Action": [
 "elasticache:CreateReplicationGroup"
 ],
 "Resource": [
 "arn:aws:elasticache:*:*:replicationgroup:*"
 ],
 "Condition": {
 "Bool": {
 "elasticache:AutomaticFailoverEnabled": "true"
 }
 }
 }
 ]
}`

```

13. **elasticache:MultiAZEnabled**:   Specify that replication groups cannot be created with Multi-AZ disabled.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "elasticache:CreateCacheCluster",
 "elasticache:CreateReplicationGroup"
 ],
 "Resource": [
 "arn:aws:elasticache:*:*:parametergroup:*",
 "arn:aws:elasticache:*:*:subnetgroup:*"
 ]
 },
 {
 "Effect": "Deny",
 "Action": [
 "elasticache:CreateCacheCluster",
 "elasticache:CreateReplicationGroup"
 ],
 "Resource": [
 "arn:aws:elasticache:*:*:cluster:*",
 "arn:aws:elasticache:*:*:replicationgroup:*"
 ],
 "Condition": {
 "Bool": {
 "elasticache:MultiAZEnabled": "false"
 }
 }
 }
 ]
}`

```

14. **elasticache:ClusterModeEnabled**:   Specify that replication groups can only be created with cluster mode enabled.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "elasticache:CreateReplicationGroup"
 ],
 "Resource": [
 "arn:aws:elasticache:*:*:parametergroup:*",
 "arn:aws:elasticache:*:*:subnetgroup:*"
 ]
 },

 {
 "Effect": "Allow",
 "Action": [
 "elasticache:CreateReplicationGroup"
 ],
 "Resource": [
 "arn:aws:elasticache:*:*:replicationgroup:*"
 ],
 "Condition": {
 "Bool": {
 "elasticache:ClusterModeEnabled": "true"
 }
 }
 }
 ]
}`

```

15. **elasticache:AuthTokenEnabled**:   Specify that replication groups can only be created with AUTH token enabled.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [

 {
 "Effect": "Allow",
 "Action": [
 "elasticache:CreateCacheCluster",
 "elasticache:CreateReplicationGroup"
 ],
 "Resource": [
 "arn:aws:elasticache:*:*:parametergroup:*",
 "arn:aws:elasticache:*:*:subnetgroup:*"
 ]
 },

 {
 "Effect": "Allow",
 "Action": [
 "elasticache:CreateCacheCluster",
 "elasticache:CreateReplicationGroup"
 ],
 "Resource": [
 "arn:aws:elasticache:*:*:cluster:*",
 "arn:aws:elasticache:*:*:replicationgroup:*"
 ],
 "Condition": {
 "Bool": {
 "elasticache:AuthTokenEnabled": "true"
 }
 }
 }
 ]
}`

```

16. **elasticache:SnapshotRetentionLimit**:   Specify the number of days (or min/max) to keep the snapshot. Below policy enforces storing backups for at least 30 days.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [

 {
 "Effect": "Allow",
 "Action": [
 "elasticache:CreateCacheCluster",
 "elasticache:CreateReplicationGroup"
 ],
 "Resource": [
 "arn:aws:elasticache:*:*:parametergroup:*",
 "arn:aws:elasticache:*:*:subnetgroup:*"
 ]
 },

 {
 "Effect": "Allow",
 "Action": [
 "elasticache:CreateCacheCluster",
 "elasticache:CreateReplicationGroup",
 "elasticache:CreateServerlessCache"
 ],
 "Resource": [
 "arn:aws:elasticache:*:*:cluster:*",
 "arn:aws:elasticache:*:*:replicationgroup:*",
 "arn:aws:elasticache:*:*:serverlesscache:*"
 ],
 "Condition": {
 "NumericGreaterThanEquals": {
 "elasticache:SnapshotRetentionLimit": "30"
 }
 }
 }
 ]
}`

```

17. **elasticache:KmsKeyId**:   Specify usage of customer managed AWS KMS keys.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowDependentResources",
 "Effect": "Allow",
 "Action": [
 "elasticache:CreateServerlessCache"
 ],
 "Resource": [
 "arn:aws:elasticache:*:*:serverlesscachesnapshot:*",
 "arn:aws:elasticache:*:*:snapshot:*",
 "arn:aws:elasticache:*:*:usergroup:*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "elasticache:CreateServerlessCache"
 ],
 "Resource": [
 "arn:aws:elasticache:*:*:serverlesscache:*"
 ],
 "Condition": {
 "StringEquals": {
 "elasticache:KmsKeyId": "my-key"
 }
 }
 }
 ]
}`

```

18. **elasticache:CacheParameterGroupName**:
      Specify a non default parameter group with specific parameters from an organization on your clusters. You could also specify a
    naming pattern for your parameter groups or block delete on a specific parameter group name. Following is an example constraining usage of only "my-org-param-group".

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [

 {
 "Effect": "Allow",
 "Action": [
 "elasticache:CreateCacheCluster",
 "elasticache:CreateReplicationGroup"
 ],
 "Resource": [
 "arn:aws:elasticache:*:*:parametergroup:*",
 "arn:aws:elasticache:*:*:subnetgroup:*"
 ]
 },

 {
 "Effect": "Allow",
 "Action": [
 "elasticache:CreateCacheCluster",
 "elasticache:CreateReplicationGroup"
 ],
 "Resource": [
 "arn:aws:elasticache:*:*:cluster:*",
 "arn:aws:elasticache:*:*:replicationgroup:*"
 ],
 "Condition": {
 "StringEquals": {
 "elasticache:CacheParameterGroupName": "my-org-param-group"
 }
 }
 }
 ]
}`

```

19. **elasticache:CacheParameterGroupName**:
      With Memcached, specify a non default parameter group with specific parameters from an organization on your clusters. You could also specify a
    naming pattern for your parameter groups or block delete on a specific parameter group name. Following is an example constraining usage of only "my-org-param-group".

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [

 {
 "Effect": "Allow",
 "Action": [
 "elasticache:CreateCacheCluster"
 ],
 "Resource": [
 "arn:aws:elasticache:*:*:parametergroup:*",
 "arn:aws:elasticache:*:*:subnetgroup:*"
 ]
 },

 {
 "Effect": "Allow",
 "Action": [
 "elasticache:CreateCacheCluster"
 ],
 "Resource": [
 "arn:aws:elasticache:*:*:cluster:*"
 ],
 "Condition": {
 "StringEquals": {
 "elasticache:CacheParameterGroupName": "my-org-param-group"
 }
 }
 }
 ]
}`

```

20. **elasticache:CreateCacheCluster**: Denying `CreateCacheCluster` action if the request tag `Project` is missing or is not equal to `Dev`, `QA` or `Prod`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "elasticache:CreateCacheCluster"
 ],
 "Resource": [
 "arn:aws:elasticache:*:*:parametergroup:*",
 "arn:aws:elasticache:*:*:subnetgroup:*",
 "arn:aws:elasticache:*:*:securitygroup:*",
 "arn:aws:elasticache:*:*:replicationgroup:*"
 ]
 },
 {
 "Effect": "Deny",
 "Action": [
 "elasticache:CreateCacheCluster"
 ],
 "Resource": [
 "arn:aws:elasticache:*:*:cluster:*"
 ],
 "Condition": {
 "Null": {
 "aws:RequestTag/Project": "true"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "elasticache:CreateCacheCluster",
 "elasticache:AddTagsToResource"
 ],
 "Resource": "arn:aws:elasticache:*:*:cluster:*",
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/Project": [
 "Dev",
 "Prod",
 "QA"
 ]
 }
 }
 }
 ]
}`

```

21. **elasticache:CacheNodeType**:
      Allowing `CreateCacheCluster` with `cacheNodeType` cache.r5.large or
    cache.r6g.4xlarge and tag `Project=XYZ`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "elasticache:CreateCacheCluster",
 "elasticache:CreateReplicationGroup"
 ],
 "Resource": [
 "arn:aws:elasticache:*:*:parametergroup:*",
 "arn:aws:elasticache:*:*:subnetgroup:*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "elasticache:CreateCacheCluster"
 ],
 "Resource": [
 "arn:aws:elasticache:*:*:cluster:*"
 ],
 "Condition": {
 "StringEqualsIfExists": {
 "elasticache:CacheNodeType": [
 "cache.r5.large",
 "cache.r6g.4xlarge"
 ]
 },
 "StringEquals": {
 "aws:RequestTag/Project": "XYZ"
 }
 }
 }
 ]
}`

```

22. **elasticache:CacheNodeType**:
      Allowing `CreateCacheCluster` with `cacheNodeType` cache.r5.large or
    cache.r6g.4xlarge and tag `Project=XYZ`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "elasticache:CreateCacheCluster"
 ],
 "Resource": [
 "arn:aws:elasticache:*:*:parametergroup:*",
 "arn:aws:elasticache:*:*:subnetgroup:*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "elasticache:CreateCacheCluster"
 ],
 "Resource": [
 "arn:aws:elasticache:*:*:cluster:*"
 ],
 "Condition": {
 "StringEqualsIfExists": {
 "elasticache:CacheNodeType": [
 "cache.r5.large",
 "cache.r6g.4xlarge"
 ]
 },
 "StringEquals": {
 "aws:RequestTag/Project": "XYZ"
 }
 }
 }
 ]
}`

```

###### Note

When creating polices to enforce tags and other condition keys together, the conditional `IfExists` may be required on condition key elements due to the extra `elasticache:AddTagsToResource`
policy requirements for creation requests with the `--tags` parameter.
