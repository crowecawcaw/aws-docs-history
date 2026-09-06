

# Security and access control
<a name="feature-store-security"></a>

 Amazon SageMaker Feature Store enables you to create two types of stores: an online store or offline store. The online store is used for low latency real-time inference use cases whereas the offline store is used for training and batch inference use cases. When you create a feature group for online or offline use you can provide a AWS Key Management Service customer managed key to encrypt all your data at rest. In case you do not provide a AWS KMS key then we ensure that your data is encrypted on the server side using an AWS owned AWS KMS key or AWS managed AWS KMS key. While creating a feature group, you can select storage type and optionally provide a AWS KMS key for encrypting data, then you can call various APIs for data management such as `PutRecord`, `GetRecord`, `DeleteRecord`, `ListRecords`, and `BatchWriteRecord`.

Feature Store allows you to grant or deny access to individuals at the feature group-level and enables cross-account access to Feature Store. For example, you can set up developer accounts to access the offline store for model training and exploration that do not have write access to production accounts. You can set up production accounts to access both online and offline stores. Feature Store uses unique customer AWS KMS keys for offline and online store data at-rest encryption. Access control is enabled through both API and AWS KMS key access. You can also create feature group-level access control. 

 For more information about customer managed key, see [customer managed keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys). For more information about AWS KMS, see [AWS KMS](https://aws.amazon.com/kms/). 

## Using AWS KMS permissions for Amazon SageMaker Feature Store
<a name="feature-store-kms-cmk-permissions"></a>

 Encryption at rest protects Feature Store under an AWS KMS customer managed key. By default, it uses an [AWS owned customer managed key for OnlineStore and AWS managed customer managed key for OfflineStore](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk). Feature Store supports an option to encrypt your online or offline store under [customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk). You can select the customer managed key for Feature Store when you create your online or offline store, and they can be different for each store. 

 Feature Store supports only [symmetric customer managed keys](https://docs.aws.amazon.com/kms/latest/developerguide/symm-asymm-concepts.html#symmetric-cmks). You cannot use an [asymmetric customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/symm-asymm-concepts.html#asymmetric-cmks) to encrypt your data in your online or offline store. For help determining whether a customer managed key is symmetric or asymmetric, see [Identifying symmetric and asymmetric customer managed keys](https://docs.aws.amazon.com/kms/latest/developerguide/find-symm-asymm.html).

When you use a customer managed key, you can take advantage of the following features: 
+  You create and manage the customer managed key, including setting the [key policies](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html), [IAM policies](https://docs.aws.amazon.com/kms/latest/developerguide/iam-policies.html) and [grants](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html) to control access to the customer managed key. You can [enable and disable](https://docs.aws.amazon.com/kms/latest/developerguide/enabling-keys.html) the customer managed key, enable and disable [automatic key rotation](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html), and [delete the customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys.html) when it is no longer in use. 
+  You can use a customer managed key with [imported key material](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html) or a customer managed key in a [custom key store](https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html) that you own and manage. 
+  You can audit the encryption and decryption of your online or offline store by examining the API calls to AWS KMS in [AWS CloudTrail logs](https://docs.aws.amazon.com/kms/latest/developerguide/services-dynamodb.html#dynamodb-cmk-trail). 

You do not pay a monthly fee for AWS owned customer managed keys. Customer managed keys will [ incur a charge](https://aws.amazon.com/kms/pricing/) for each API call and AWS Key Management Service quotas apply to each customer managed key.

## Authorizing use of a customer managed Key for your online store
<a name="feature-store-authorizing-cmk-online-store"></a>

 If you use a [customer managed key ](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk) to protect your online store, the policies on that customer managed key must give Feature Store permission to use it on your behalf. You have full control over the policies and grants on a customer managed key.

 Feature Store does not need additional authorization to use the default [AWS owned KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys) to protect your online or offline stores in your AWS account.

### Customer managed key policy
<a name="feature-store-customer-managed-cmk-policy"></a>

 When you select a [customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk) to protect your Online Store, Feature Store must have permission to use the customer managed key on behalf of the principal who makes the selection. That principal, a user or role, must have the permissions on the customer managed key that Feature Store requires. You can provide these permissions in a [key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html), an [IAM policy](https://docs.aws.amazon.com/kms/latest/developerguide/iam-policies.html), or a [grant](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html). At a minimum, Feature Store requires the following permissions on a customer managed key: 
+  "kms:Encrypt", "kms:Decrypt", "kms:DescribeKey", "kms:CreateGrant", "kms:RetireGrant", "kms:ReEncryptFrom", "kms:ReEncryptTo", "kms:GenerateDataKey", "kms:ListAliases", "kms:ListGrants", "kms:RevokeGrant" 

 For example, the following example key policy provides only the required permissions. The policy has the following effects: 
+  Allows Feature Store to use the customer managed key in cryptographic operations and create grants, but only when it is acting on behalf of principals in the account who have permission to use your Feature Store. If the principals specified in the policy statement don't have permission to use your Feature Store, the call fails, even when it comes from the Feature Store service. 
+  The [kms:ViaService](https://docs.aws.amazon.com/kms/latest/developerguide/policy-conditions.html#conditions-kms-via-service) condition key allows the permissions only when the request comes from FeatureStore on behalf of the principals listed in the policy statement. These principals can't call these operations directly. The value for `kms:ViaService` should be `sagemaker.*.amazonaws.com`. 
**Note**  
 The `kms:ViaService` condition key can only be used for the online store customer managed AWS KMS key, and cannot be used for the offline store. If you add this special condition to your customer managed key, and use the same AWS KMS key for both the online and offline store, then it will fail the `CreateFeatureGroup` API operation. 
+  Gives the customer managed key administrators read-only access to the customer managed key and permission to revoke grants, including the grants that Feature Store uses to protect your data. 

 Before using an example key policy, replace the example principals with actual principals from your AWS account. 

------
#### [ JSON ]

****  

```
{"Id": "key-policy-feature-store",
   "Version":"2012-10-17",		 	 	 
   "Statement": [
     {"Sid" : "Allow access through Amazon SageMaker AI Feature Store for all principals in the account that are authorized to use  Amazon SageMaker AI Feature Store ",
       "Effect": "Allow",
       "Principal": {"AWS": "arn:aws:iam::111122223333:user/featurestore-user"},
       "Action": [
         "kms:Encrypt",
         "kms:Decrypt",
         "kms:DescribeKey",
         "kms:CreateGrant",
         "kms:RetireGrant",
         "kms:ReEncryptFrom",
         "kms:ReEncryptTo",
         "kms:GenerateDataKey",
         "kms:ListGrants"
       ],
       "Resource": "*",      
       "Condition": {"StringLike": {"kms:ViaService" : "sagemaker.*.amazonaws.com"
          }
       }
     },
     {"Sid" : "Allow listing aliases",
       "Effect": "Allow",
       "Principal": {"AWS": "arn:aws:iam::111122223333:user/featurestore-user"},
       "Action": "kms:ListAliases",
       "Resource": "*"
     },
     {"Sid":  "Allow administrators to view the customer managed key and revoke grants",
       "Effect": "Allow",
       "Principal": {"AWS": "arn:aws:iam::111122223333:role/featurestore-admin"
        },
       "Action": [
         "kms:Describe*",
         "kms:Get*",
         "kms:List*",
         "kms:RevokeGrant"
       ],
       "Resource": "*"
     },
     {"Sid": "Enable IAM User Permissions",
       "Effect": "Allow",
       "Principal": {"AWS": "arn:aws:iam::111122223333:root"
        },
        "Action": "kms:*",
        "Resource": "*"
     }
   ]
 }
```

------

## Using grants to authorize Feature Store
<a name="feature-store-using-grants-authorize"></a>

 In addition to key policies, Feature Store uses grants to set permissions on the customer managed key. To view the grants on a customer managed key in your account, use the `[ListGrants](https://docs.aws.amazon.com/kms/latest/APIReference/API_ListGrants.html)` operation. Feature Store does not need grants, or any additional permissions, to use the [AWS owned customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk) to protect your online store. 

 Feature Store uses the grant permissions when it performs background system maintenance and continuous data protection tasks. 

 Each grant is specific to an online store. If the account includes multiple stores encrypted under the same customer managed key, there will be unique grants per `FeatureGroup` using the same customer managed key. 

 The key policy can also allow the account to [revoke the grant](https://docs.aws.amazon.com/kms/latest/APIReference/API_RevokeGrant.html) on the customer managed key. However, if you revoke the grant on an active encrypted online store, Feature Store won't be able to protect and maintain the store. 

## Monitoring Feature Store interaction with AWS KMS
<a name="feature-store-monitoring-kms-interaction"></a>

 If you use a [customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk) to protect your online or offline store, you can use AWS CloudTrail logs to track the requests that Feature Store sends to AWS KMS on your behalf.

## Accessing data in your online store
<a name="feature-store-accessing-data-online-store"></a>

 The **caller (either user or role)** to DataPlane operations must have the corresponding IAM action permissions on the target feature group resource. In addition, all DataPlane operations require `kms:Decrypt` on the customer managed key.
+ **PutRecord** – Requires `sagemaker:PutRecord`
+ **UpdateRecord** – Requires `sagemaker:PutRecord`. `UpdateRecord` does not have a separate IAM action. Instead, IAM authorizes `UpdateRecord` against the `sagemaker:PutRecord` action. Any policy that allows or denies `sagemaker:PutRecord` also applies to `UpdateRecord`. You don't need to update your existing policies.
+ **GetRecord** – Requires `sagemaker:GetRecord`
+ **DeleteRecord** – Requires `sagemaker:DeleteRecord`
+ **ListRecords** – Requires `sagemaker:ListRecords`
+ **BatchWriteRecord** – Requires `sagemaker:BatchWriteRecord` and `sagemaker:PutRecord`
+ **BatchGetRecord** – Requires `sagemaker:BatchGetRecord`

**Note**  
The `BatchWriteRecord` API requires the caller to have both `sagemaker:BatchWriteRecord` and `sagemaker:PutRecord` permissions on the target feature group. An explicit Deny on either action blocks the request.

### Condition keys for `UpdateRecord` access control
<a name="feature-store-updaterecord-condition-keys"></a>

IAM authorizes `UpdateRecord` against the `sagemaker:PutRecord` action. With these condition keys, you can write more granular policies. The keys let you distinguish partial record updates from full record writes:
+ `sagemaker:IsUpdateRecord` – Set to `true` when the request is an `UpdateRecord` call, and `false` when the request is a `PutRecord` call. This key is absent for other DataPlane operations, including the `PutRecord` check that `BatchWriteRecord` performs.
+ `sagemaker:UpdatableFeatures` – The list of feature names included in an `UpdateRecord` request. IAM omits this key when the request does not specify any features; the key is never present with an empty list. This prevents `ForAllValues` conditions from being evaluated against an empty set. This key is not present on `PutRecord` requests.

With these condition keys, you can build policies such as the following:
+ The following JSON IAM policy allows only `UpdateRecord` calls and blocks direct `PutRecord` calls on a feature group. This policy also blocks `BatchWriteRecord`. The `sagemaker:IsUpdateRecord` key is not present during the `sagemaker:PutRecord` authorization check that `BatchWriteRecord` performs. If you need to allow `BatchWriteRecord`, add a separate statement without the `IsUpdateRecord` condition:

  ```
  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": "sagemaker:PutRecord",
              "Resource": "arn:aws:sagemaker:us-east-1:111122223333:feature-group/test-fg",
              "Condition": {
                  "Bool": {
                      "sagemaker:IsUpdateRecord": "true"
                  }
              }
          }
      ]
  }
  ```
+ The following JSON IAM policy allows `PutRecord` calls and blocks `UpdateRecord` calls on a feature group. The `BoolIfExists` condition operator ensures the statement also matches the `sagemaker:PutRecord` check that `BatchWriteRecord` performs. For `BatchWriteRecord`, the authorization context does not include `sagemaker:IsUpdateRecord`:

  ```
  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": "sagemaker:PutRecord",
              "Resource": "arn:aws:sagemaker:us-east-1:111122223333:feature-group/test-fg",
              "Condition": {
                  "BoolIfExists": {
                      "sagemaker:IsUpdateRecord": "false"
                  }
              }
          }
      ]
  }
  ```
+ The following JSON IAM policy denies `UpdateRecord` calls that attempt to modify sensitive features, regardless of what other features are included in the request:

  ```
  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Deny",
              "Action": "sagemaker:PutRecord",
              "Resource": "arn:aws:sagemaker:us-east-1:111122223333:feature-group/test-fg",
              "Condition": {
                  "Bool": {
                      "sagemaker:IsUpdateRecord": "true"
                  },
                  "ForAnyValue:StringEquals": {
                      "sagemaker:UpdatableFeatures": ["ssn", "credit_score"]
                  }
              }
          }
      ]
  }
  ```
+ The following JSON IAM policy allows `UpdateRecord` calls only when all requested features are on an approved safe-to-update list. The `Null` condition requires `sagemaker:UpdatableFeatures` to exist, because the `ForAllValues` operator otherwise evaluates to `true` when the key is absent:

  ```
  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": "sagemaker:PutRecord",
              "Resource": "arn:aws:sagemaker:us-east-1:111122223333:feature-group/test-fg",
              "Condition": {
                  "Bool": {
                      "sagemaker:IsUpdateRecord": "true"
                  },
                  "Null": {
                      "sagemaker:UpdatableFeatures": "false"
                  },
                  "ForAllValues:StringEquals": {
                      "sagemaker:UpdatableFeatures": ["last_login", "click_count"]
                  }
              }
          }
      ]
  }
  ```

**Note**  
Policies that grant or deny `sagemaker:PutRecord` without any condition on `sagemaker:IsUpdateRecord` continue to apply to both `PutRecord` and `UpdateRecord` calls, so you don't need to change your policies unless you want to distinguish between the two operations.

For more information about using IAM condition keys, see [IAM JSON policy elements: Condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html) in the *IAM User Guide*.

## Authorizing use of a customer managed key for your offline store
<a name="feature-store-authorizing-use-cmk-offline-store"></a>

 The **roleArn** that is passed as a parameter to `createFeatureGroup` must have below permissions to the OfflineStore KmsKeyId: 

```
"kms:GenerateDataKey"
```

**Note**  
The key policy for the online store also works for the offline store, only when the `kms:ViaService` condition is not specified. 

**Important**  
You can specify a AWS KMS encryption key to encrypt the Amazon S3 location used for your offline feature store when you create a feature group. If AWS KMS encryption key is not specified, by default we encrypt all data at rest using AWS KMS key. By defining your [bucket-level key](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-key.html) for SSE, you can reduce AWS KMS requests costs by up to 99 percent. 