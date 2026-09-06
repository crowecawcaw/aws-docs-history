

# Cross-account cloning with AWS RAM and Amazon Aurora
<a name="Aurora.Managing.Clone.Cross-Account"></a>

By using AWS Resource Access Manager (AWS RAM) with Amazon Aurora, you can share Aurora DB clusters and clones that belong to your AWS account with another AWS account or organization. Such *cross-account cloning* is much faster than creating and restoring a database snapshot. You can create a clone of one of your Aurora DB clusters and share the clone. Or you can share your Aurora DB cluster with another AWS account and let the account holder create the clone. The approach that you choose depends on your use case.

For example, you might need to regularly share a clone of your financial database with your organization's internal auditing team. In this case, your auditing team has its own AWS account for the applications that it uses. You can give the auditing team's AWS account the permission to access your Aurora DB cluster and clone it as needed. 

On the other hand, if an outside vendor audits your financial data you might prefer to create the clone yourself. You then give the outside vendor access to the clone only.

You can also use cross-account cloning to support many of the same use cases for cloning within the same AWS account, such as development and testing. For example, your organization might use different AWS accounts for production, development, testing, and so on. For more information, see [Overview of Aurora cloning](Aurora.Managing.Clone.md#Aurora.Clone.Overview). 

Thus, you might want to share a clone with another AWS account or allow another AWS account to create clones of your Aurora DB clusters. In either case, start by using AWS RAM to create a share object. For complete information about sharing AWS resources between AWS accounts, see the [AWS RAM User Guide](https://docs.aws.amazon.com/ram/latest/userguide/). 

Creating a cross-account clone requires actions from the AWS account that owns the original cluster, and the AWS account that creates the clone. First, the original cluster owner modifies the cluster to allow one or more other accounts to clone it. If any of the accounts is in a different AWS organization, AWS generates a sharing invitation. The other account must accept the invitation before proceeding. Then each authorized account can clone the cluster. Throughout this process, the cluster is identified by its unique Amazon Resource Name (ARN). 

As with cloning within the same AWS account, additional storage space is used only if changes are made to the data by the source or the clone. Charges for storage are then applied at that time. If the source cluster is deleted, storage costs are distributed equally among remaining cloned clusters. 

**Topics**
+ [Limitations of cross-account cloning](#Aurora.Managing.Clone.CrossAccount.Limitations)
+ [Allowing other AWS accounts to clone your cluster](#Aurora.Managing.Clone.CrossAccount.yours)
+ [Cloning a cluster that is owned by another AWS account](#Aurora.Managing.Clone.CrossAccount.theirs)

## Limitations of cross-account cloning
<a name="Aurora.Managing.Clone.CrossAccount.Limitations"></a>

 Aurora cross-account cloning has the following limitations: 
+ You can't view or accept invitations to shared resources with the AWS Management Console. Use the AWS CLI, the Amazon RDS API, or the AWS RAM console to view and accept invitations to shared resources.
+ You can create only one new clone from a resource shared with your AWS account. This applies whether the shared resource is an original Aurora DB cluster or a previously created clone.
+ You can create only one new clone from a clone that's been shared with your AWS account.
+ You can't share resources (clones or Aurora DB clusters) that have been shared with your AWS account.
+ You can create a maximum of 15 cross-account clones from any single Aurora DB cluster. 
+  Each of the 15 cross-account clones must be owned by a different AWS account. That is, you can only create one cross-account clone of a cluster within any AWS account. 
+  After you clone a cluster, the original cluster and its clone are considered to be the same for purposes of enforcing limits on cross-account clones. You can't create cross-account clones of both the original cluster and the cloned cluster within the same AWS account. The total number of cross-account clones for the original cluster and any of its clones can't exceed 15. 
+ You can't share an Aurora DB cluster with other AWS accounts unless the cluster is in an `ACTIVE` state. 
+ You can't rename an Aurora DB cluster that's been shared with other AWS accounts. 
+  You can't create a cross-account clone of a cluster that is encrypted with the default RDS key. 
+ You can't create nonencrypted clones in one AWS account from encrypted Aurora DB clusters that have been shared by another AWS account. The cluster owner must grant permission to access the source cluster's AWS KMS key. However, you can use a different key when you create the clone. 

## Allowing other AWS accounts to clone your cluster
<a name="Aurora.Managing.Clone.CrossAccount.yours"></a>

 To allow other AWS accounts to clone a cluster that you own, use AWS RAM to set the sharing permission. Doing so also sends an invitation to each of the other accounts that's in a different AWS organization. 

 For the procedures to share resources owned by you in the AWS RAM console, see [Sharing resources owned by you](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing.html) in the *AWS RAM User Guide*. 

**Topics**
+ [Granting permission to other AWS accounts to clone your cluster](#Aurora.Managing.Clone.CrossAccount.granting)
+ [Checking if a cluster that you own is shared with other AWS accounts](#Aurora.Managing.Clone.CrossAccount.confirming)

### Granting permission to other AWS accounts to clone your cluster
<a name="Aurora.Managing.Clone.CrossAccount.granting"></a>

 If the cluster that you're sharing is encrypted, you also share the AWS KMS key for the cluster. You can allow AWS Identity and Access Management (IAM) users or roles in one AWS account to use a KMS key in a different account. 

To do this, you first add the external account (root user) to the KMS key's key policy through AWS KMS. You don't add the individual users or roles to the key policy, only the external account that owns them. You can only share a KMS key that you create, not the default RDS service key. For information about access control for KMS keys, see [Authentication and access control for AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/control-access.html). 

#### Console
<a name="Aurora.Managing.Clone.CrossAccount.granting.console"></a>

**To grant permission to clone your cluster**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1.  In the navigation pane, choose **Databases**. 

1.  Choose the DB cluster that you want to share to see its **Details** page, and choose the **Connectivity & security** tab. 

1.  In the **Share DB cluster with other AWS accounts** section, enter the numeric account ID for the AWS account that you want to allow to clone this cluster. For account IDs in the same organization, you can begin typing in the box and then choose from the menu. 
**Important**  
 In some cases, you might want an account that is not in the same AWS organization as your account to clone a cluster. In these cases, for security reasons the console doesn't report who owns that account ID or whether the account exists.   
Be careful entering account numbers that are not in the same AWS organization as your AWS account. Immediately verify that you shared with the intended account. 

1.  On the confirmation page, verify that the account ID that you specified is correct. Enter `share` in the confirmation box to confirm. 

    On the **Details** page, an entry appears that shows the specified AWS account ID under **Accounts that this DB cluster is shared with**. The **Status** column initially shows a status of **Pending**. 

1.  Contact the owner of the other AWS account, or sign in to that account if you own both of them. Instruct the owner of the other account to accept the sharing invitation and clone the DB cluster, as described following. 

#### AWS CLI
<a name="Aurora.Managing.Clone.CrossAccount.granting.cli"></a>

**To grant permission to clone your cluster**

1.  Gather the information for the required parameters. You need the ARN for your cluster and the numeric ID for the other AWS account. 

1.  Run the AWS RAM CLI command [`create-resource-share`](https://docs.aws.amazon.com/cli/latest/reference/ram/create-resource-share.html). 

   For Linux, macOS, or Unix:

   ```
   aws ram create-resource-share --name {{descriptive_name}} \
     --region {{region}} \
     --resource-arns {{cluster_arn}} \
     --principals {{other_account_ids}}
   ```

   For Windows:

   ```
   aws ram create-resource-share --name {{descriptive_name}} ^
     --region {{region}} ^
     --resource-arns {{cluster_arn}} ^
     --principals {{other_account_ids}}
   ```

    To include multiple account IDs for the `--principals` parameter, separate IDs from each other with spaces. To specify whether the permitted account IDs can be outside your AWS organization, include the `--allow-external-principals` or `--no-allow-external-principals` parameter for `create-resource-share`. 

#### AWS RAM API
<a name="Aurora.Managing.Clone.CrossAccount.granting.api"></a>

**To grant permission to clone your cluster**

1.  Gather the information for the required parameters. You need the ARN for your cluster and the numeric ID for the other AWS account. 

1.  Call the AWS RAM API operation [CreateResourceShare](https://docs.aws.amazon.com/ram/latest/APIReference/API_CreateResourceShare.html), and specify the following values: 
   +  Specify the account ID for one or more AWS accounts as the `principals` parameter. 
   +  Specify the ARN for one or more Aurora DB clusters as the `resourceArns` parameter. 
   +  Specify whether the permitted account IDs can be outside your AWS organization by including a Boolean value for the `allowExternalPrincipals` parameter. 

#### Recreating a cluster that uses the default RDS key
<a name="Aurora.Managing.Clone.CrossAccount.granting.defaultkey"></a>

If the encrypted cluster that you plan to share uses the default RDS key, make sure to recreate the cluster. To do this, create a manual snapshot of your DB cluster, use an AWS KMS key, and then restore the cluster to a new cluster. Then share the new cluster. To perform this process, take the following steps.

**To recreate an encrypted cluster that uses the default RDS key**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1.  Choose **Snapshots** from the navigation pane. 

1.  Choose your snapshot. 

1.  For **Actions**, choose **Copy Snapshot**, and then choose **Enable encryption**. 

1.  For **AWS KMS key**, choose the new encryption key that you want to use. 

1.  Restore the copied snapshot. To do so, follow the procedure in [Restoring from a DB cluster snapshot](aurora-restore-snapshot.md). The new DB instance uses your new encryption key. 

1.  (Optional) Delete the old DB cluster if you no longer need it. To do so, follow the procedure in [Deleting a DB cluster snapshot](aurora-delete-snapshot.md#DeleteDBClusterSnapshot). Before you do, confirm that your new cluster has all necessary data and that your application can access it successfully. 

### Checking if a cluster that you own is shared with other AWS accounts
<a name="Aurora.Managing.Clone.CrossAccount.confirming"></a>

 You can check if other users have permission to share a cluster. Doing so can help you understand whether the cluster is approaching the limit for the maximum number of cross-account clones. 

 For the procedures to share resources using the AWS RAM console, see [Sharing resources owned by you](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing.html) in the *AWS RAM User Guide*. 

#### AWS CLI
<a name="Aurora.Managing.Clone.CrossAccount.confirming.cli"></a>

**To find out if a cluster that you own is shared with other AWS accounts**
+  Call the AWS RAM CLI command [`list-principals`](https://docs.aws.amazon.com/cli/latest/reference/ram/list-principals.html), using your account ID as the resource owner and the ARN of your cluster as the resource ARN. You can see all shares with the following command. The results indicate which AWS accounts are allowed to clone the cluster. 

  ```
  aws ram list-principals \
      --resource-arns {{your_cluster_arn}} \
      --principals {{your_aws_id}}
  ```

#### AWS RAM API
<a name="Aurora.Managing.Clone.CrossAccount.confirming.api"></a>

**To find out if a cluster that you own is shared with other AWS accounts**
+  Call the AWS RAM API operation [ListPrincipals](https://docs.aws.amazon.com/ram/latest/APIReference/API_ListPrincipals.html). Use your account ID as the resource owner and the ARN of your cluster as the resource ARN. 

## Cloning a cluster that is owned by another AWS account
<a name="Aurora.Managing.Clone.CrossAccount.theirs"></a>

 To clone a cluster that's owned by another AWS account, use AWS RAM to get permission to make the clone. After you have the required permission, use the standard procedure for cloning an Aurora cluster. 

 You can also check whether a cluster that you own is a clone of a cluster owned by a different AWS account. 

 For the procedures to work with resources owned by others in the AWS RAM console, see [Accessing resources shared with you](https://docs.aws.amazon.com/ram/latest/userguide/working-with-shared.html) in the *AWS RAM User Guide.* 

**Topics**
+ [Viewing invitations to clone clusters that are owned by other AWS accounts](#Aurora.Managing.Clone.CrossAccount.viewing)
+ [Accepting invitations to share clusters owned by other AWS accounts](#Aurora.Managing.Clone.CrossAccount.accepting)
+ [Cloning an Aurora cluster that is owned by another AWS account](#Aurora.Managing.Clone.CrossAccount.cloning)
+ [Checking if a DB cluster is a cross-account clone](#Aurora.Managing.Clone.CrossAccount.checking)

### Viewing invitations to clone clusters that are owned by other AWS accounts
<a name="Aurora.Managing.Clone.CrossAccount.viewing"></a>

 To work with invitations to clone clusters owned by AWS accounts in other AWS organizations, use the AWS CLI, the AWS RAM console, or the AWS RAM API. Currently, you can't perform this procedure using the Amazon RDS console. 

 For the procedures to work with invitations in the AWS RAM console, see [Accessing resources shared with you](https://docs.aws.amazon.com/ram/latest/userguide/working-with-shared.html) in the *AWS RAM User Guide*. 

#### AWS CLI
<a name="Aurora.Managing.Clone.CrossAccount.viewing.cli"></a>

**To see invitations to clone clusters that are owned by other AWS accounts**

1.  Run the AWS RAM CLI command [`get-resource-share-invitations`](https://docs.aws.amazon.com/cli/latest/reference/ram/get-resource-share-invitations.html). 

   ```
   aws ram get-resource-share-invitations --region {{region_name}}
   ```

    The results from the preceding command show all invitations to clone clusters, including any that you already accepted or rejected. 

1.  (Optional) Filter the list so you see only the invitations that require action from you. To do so, add the parameter `--query 'resourceShareInvitations[?status==`PENDING`]'`. 

#### AWS RAM API
<a name="Aurora.Managing.Clone.CrossAccount.viewing.api"></a>

**To see invitations to clone clusters that are owned by other AWS accounts**

1.  Call the AWS RAM API operation [`GetResourceShareInvitations`](https://docs.aws.amazon.com/ram/latest/APIReference/API_GetResourceShareInvitations.html). This operation returns all such invitations, including any that you already accepted or rejected. 

1.  (Optional) Find only the invitations that require action from you by checking the `resourceShareAssociations` return field for a `status` value of `PENDING`. 

### Accepting invitations to share clusters owned by other AWS accounts
<a name="Aurora.Managing.Clone.CrossAccount.accepting"></a>

 You can accept invitations to share clusters owned by other AWS accounts that are in different AWS organizations. To work with these invitations, use the AWS CLI, the AWS RAM and RDS APIs, or the AWS RAM console. Currently, you can't perform this procedure using the RDS console. 

 For the procedures to work with invitations in the AWS RAM console, see [Accessing resources shared with you](https://docs.aws.amazon.com/ram/latest/userguide/working-with-shared.html) in the *AWS RAM User Guide*. 

#### AWS CLI
<a name="Aurora.Managing.Clone.CrossAccount.accepting.cli"></a>

**To accept an invitation to share a cluster from another AWS account**

1.  Find the invitation ARN by running the AWS RAM CLI command [`get-resource-share-invitations`](https://docs.aws.amazon.com/cli/latest/reference/ram/get-resource-share-invitations.html), as shown preceding. 

1.  Accept the invitation by calling the AWS RAM CLI command [`accept-resource-share-invitation`](https://docs.aws.amazon.com/cli/latest/reference/ram/accept-resource-share-invitation.html), as shown following. 

   For Linux, macOS, or Unix:

   ```
   aws ram accept-resource-share-invitation \
     --resource-share-invitation-arn {{invitation_arn}} \
     --region {{region}}
   ```

   For Windows:

   ```
   aws ram accept-resource-share-invitation ^
     --resource-share-invitation-arn {{invitation_arn}} ^
     --region {{region}}
   ```

#### AWS RAM and RDS API
<a name="Aurora.Managing.Clone.CrossAccount.accepting.api"></a>

**To accept invitations to share somebody's cluster**

1.  Find the invitation ARN by calling the AWS RAM API operation [`GetResourceShareInvitations`](https://docs.aws.amazon.com/ram/latest/APIReference/API_GetResourceShareInvitations.html), as shown preceding. 

1.  Pass that ARN as the `resourceShareInvitationArn` parameter to the RDS API operation [AcceptResourceShareInvitation](https://docs.aws.amazon.com/ram/latest/APIReference/API_AcceptResourceShareInvitation.html). 

### Cloning an Aurora cluster that is owned by another AWS account
<a name="Aurora.Managing.Clone.CrossAccount.cloning"></a>

 After you accept the invitation from the AWS account that owns the DB cluster, as shown preceding, you can clone the cluster. 

#### Console
<a name="Aurora.Managing.Clone.CrossAccount.cloning.console"></a>

**To clone an Aurora cluster that is owned by another AWS account**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1.  In the navigation pane, choose **Databases**. 

    At the top of the database list, you should see one or more items with a **Role** value of `Shared from account #{{account_id}}`. For security reasons, you can only see limited information about the original clusters. The properties that you can see are the ones such as database engine and version that must be the same in your cloned cluster. 

1.  Choose the cluster that you intend to clone. 

1.  For **Actions**, choose **Create clone**. 

1.  Follow the procedure in [Console](Aurora.Managing.Clone.md#Aurora.Managing.Clone.Console) to finish setting up the cloned cluster. 

1. As needed, enable encryption for the cloned cluster. If the cluster that you are cloning is encrypted, you must enable encryption for the cloned cluster. The AWS account that shared the cluster with you must also share the KMS key that was used to encrypt the cluster. You can use the same KMS key to encrypt the clone, or your own KMS key. You can't create a cross-account clone for a cluster that is encrypted with the default KMS key. 

    The account that owns the encryption key must grant permission to use the key to the destination account by using a key policy. This process is similar to how encrypted snapshots are shared, by using a key policy that grants permission to the destination account to use the key. 

#### AWS CLI
<a name="Aurora.Managing.Clone.CrossAccount.cloning.cli"></a>

**To clone an Aurora cluster owned by another AWS account**

1.  Accept the invitation from the AWS account that owns the DB cluster, as shown preceding. 

1.  Clone the cluster by specifying the full ARN of the source cluster in the `source-db-cluster-identifier` parameter of the RDS CLI command [`restore-db-cluster-to-point-in-time`](https://docs.aws.amazon.com/cli/latest/reference/rds/restore-db-cluster-to-point-in-time.html), as shown following. 

    If the ARN passed as the `source-db-cluster-identifier` hasn't been shared, the same error is returned as if the specified cluster doesn't exist. 

   For Linux, macOS, or Unix:

   ```
   aws rds restore-db-cluster-to-point-in-time \
     --source-db-cluster-identifier=arn:aws:rds:{{arn_details}} \
     --db-cluster-identifier={{new_cluster_id}} \
     --restore-type=copy-on-write \
     --use-latest-restorable-time
   ```

   For Windows:

   ```
   aws rds restore-db-cluster-to-point-in-time ^
     --source-db-cluster-identifier=arn:aws:rds:{{arn_details}} ^
     --db-cluster-identifier={{new_cluster_id}} ^
     --restore-type=copy-on-write ^
     --use-latest-restorable-time
   ```

1.  If the cluster that you are cloning is encrypted, encrypt your cloned cluster by including a `kms-key-id` parameter. This `kms-key-id` value can be the same one used to encrypt the original DB cluster, or your own KMS key. Your account must have permission to use that encryption key. 

   For Linux, macOS, or Unix:

   ```
   aws rds restore-db-cluster-to-point-in-time \
     --source-db-cluster-identifier=arn:aws:rds:{{arn_details}} \
     --db-cluster-identifier={{new_cluster_id}} \
     --restore-type=copy-on-write \
     --use-latest-restorable-time \
     --kms-key-id=arn:aws:kms:{{arn_details}}
   ```

   For Windows:

   ```
   aws rds restore-db-cluster-to-point-in-time ^
     --source-db-cluster-identifier=arn:aws:rds:{{arn_details}} ^
     --db-cluster-identifier={{new_cluster_id}} ^
     --restore-type=copy-on-write ^
     --use-latest-restorable-time ^
     --kms-key-id=arn:aws:kms:{{arn_details}}
   ```

    The account that owns the encryption key must grant permission to use the key to the destination account by using a key policy. This process is similar to how encrypted snapshots are shared, by using a key policy that grants permission to the destination account to use the key. An example of a key policy follows. 

------
#### [ JSON ]

****  

   ```
   {
       "Id": "key-policy-1",
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Sid": "Allow use of the key",
               "Effect": "Allow",
               "Principal": {
                   "AWS": [
                       "arn:aws:iam::{{111122223333}}:user/KeyUser",
                       "arn:aws:iam::{{111122223333}}:root"
                   ]
               },
               "Action": [
                   "kms:CreateGrant",
                   "kms:Encrypt",
                   "kms:Decrypt",
                   "kms:ReEncrypt*",
                   "kms:GenerateDataKey*",
                   "kms:DescribeKey"
               ],
               "Resource": "*"
           },
           {
               "Sid": "Allow attachment of persistent resources",
               "Effect": "Allow",
               "Principal": {
                   "AWS": [
                       "arn:aws:iam::{{111122223333}}:user/KeyUser",
                       "arn:aws:iam::{{111122223333}}:root"
                   ]
               },
               "Action": [
                   "kms:CreateGrant",
                   "kms:ListGrants",
                   "kms:RevokeGrant"
               ],
               "Resource": "*",
               "Condition": {
                   "Bool": {
                       "kms:GrantIsForAWSResource": true
                   }
               }
           }
       ]
   }
   ```

------

**Note**  
The [restore-db-cluster-to-point-in-time](https://docs.aws.amazon.com/cli/latest/reference/rds/restore-db-cluster-to-point-in-time.html) AWS CLI command restores only the DB cluster, not the DB instances for that DB cluster. To create DB instances for the restored DB cluster, invoke the [create-db-instance](https://docs.aws.amazon.com/cli/latest/reference/rds/create-db-instance.html) command. Specify the identifier of the restored DB cluster in `--db-cluster-identifier`.   
You can create DB instances only after the `restore-db-cluster-to-point-in-time` command has completed and the DB cluster is available.

#### RDS API
<a name="Aurora.Managing.Clone.CrossAccount.cloning.api"></a>

**To clone an Aurora cluster owned by another AWS account**

1.  Accept the invitation from the AWS account that owns the DB cluster, as shown preceding. 

1.  Clone the cluster by specifying the full ARN of the source cluster in the `SourceDBClusterIdentifier` parameter of the RDS API operation [`RestoreDBClusterToPointInTime`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RestoreDBClusterToPointInTime.html). 

    If the ARN passed as the `SourceDBClusterIdentifier` hasn't been shared, then the same error is returned as if the specified cluster doesn't exist. 

1.  If the cluster that you are cloning is encrypted, include a `KmsKeyId` parameter to encrypt your cloned cluster. This `kms-key-id` value can be the same one used to encrypt the original DB cluster, or your own KMS key. Your account must have permission to use that encryption key. 

    When you clone a volume, the destination account must have permission to use the encryption key used to encrypt the source cluster. Aurora encrypts the new cloned cluster with the encryption key specified in `KmsKeyId`. 

    The account that owns the encryption key must grant permission to use the key to the destination account by using a key policy. This process is similar to how encrypted snapshots are shared, by using a key policy that grants permission to the destination account to use the key. An example of a key policy follows. 

------
#### [ JSON ]

****  

   ```
   {
       "Id": "key-policy-1",
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Sid": "Allow use of the key",
               "Effect": "Allow",
               "Principal": {
                   "AWS": [
                       "arn:aws:iam::{{111122223333}}:user/KeyUser",
                       "arn:aws:iam::{{111122223333}}:root"
                   ]
               },
               "Action": [
                   "kms:CreateGrant",
                   "kms:Encrypt",
                   "kms:Decrypt",
                   "kms:ReEncrypt*",
                   "kms:GenerateDataKey*",
                   "kms:DescribeKey"
               ],
               "Resource": "*"
           },
           {
               "Sid": "Allow attachment of persistent resources",
               "Effect": "Allow",
               "Principal": {
                   "AWS": [
                       "arn:aws:iam::{{111122223333}}:user/KeyUser",
                       "arn:aws:iam::{{111122223333}}:root"
                   ]
               },
               "Action": [
                   "kms:CreateGrant",
                   "kms:ListGrants",
                   "kms:RevokeGrant"
               ],
               "Resource": "*",
               "Condition": {
                   "Bool": {
                       "kms:GrantIsForAWSResource": true
                   }
               }
           }
       ]
   }
   ```

------

**Note**  
The [RestoreDBClusterToPointInTime](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RestoreDBClusterToPointInTime.html) RDS API operation restores only the DB cluster, not the DB instances for that DB cluster. To create DB instances for the restored DB cluster, invoke the [CreateDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html) RDS API operation. Specify the identifier of the restored DB cluster in `DBClusterIdentifier`. You can create DB instances only after the `RestoreDBClusterToPointInTime` operation has completed and the DB cluster is available.

### Checking if a DB cluster is a cross-account clone
<a name="Aurora.Managing.Clone.CrossAccount.checking"></a>

 The `DBClusters` object identifies whether each cluster is a cross-account clone. You can see the clusters that you have permission to clone by using the `include-shared` option when you run the RDS CLI command [`describe-db-clusters`](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-clusters.html). However, you can't see most of the configuration details for such clusters. 

#### AWS CLI
<a name="Aurora.Managing.Clone.CrossAccount.checking.cli"></a>

**To check if a DB cluster is a cross-account clone**
+  Call the RDS CLI command [`describe-db-clusters`](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-clusters.html). 

   The following example shows how actual or potential cross-account clone DB clusters appear in `describe-db-clusters` output. For existing clusters owned by your AWS account, the `CrossAccountClone` field indicates whether the cluster is a clone of a DB cluster that is owned by another AWS account. 

   In some cases, an entry might have a different AWS account number than yours in the `DBClusterArn` field. In this case, that entry represents a cluster that is owned by a different AWS account and that you can clone. Such entries have few fields other than `DBClusterArn`. When creating the cloned cluster, specify the same `StorageEncrypted`, `Engine`, and `EngineVersion` values as in the original cluster. 

  ```
  $aws rds describe-db-clusters --include-shared --region us-east-1
  {
    "DBClusters": [
        {
            "EarliestRestorableTime": "2023-02-01T21:17:54.106Z",
            "Engine": "aurora-mysql",
            "EngineVersion": "8.0.mysql_aurora.3.02.0",
            "CrossAccountClone": false,
  ...
        },
        {
            "EarliestRestorableTime": "2023-02-09T16:01:07.398Z",
            "Engine": "aurora-mysql",
            "EngineVersion": "8.0.mysql_aurora.3.02.0",
            "CrossAccountClone": true,
  ...
        },
        {
            "StorageEncrypted": false,
            "DBClusterArn": "arn:aws:rds:us-east-1:12345678:cluster:cluster-abcdefgh",
            "Engine": "aurora-mysql",
            "EngineVersion": "8.0.mysql_aurora.3.02.0
    ]
  }
  ```

#### RDS API
<a name="Aurora.Managing.Clone.CrossAccount.checking.api"></a>

**To check if a DB cluster is a cross-account clone**
+  Call the RDS API operation [DescribeDBClusters](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBClusters.html). 

   For existing clusters owned by your AWS account, the `CrossAccountClone` field indicates whether the cluster is a clone of a DB cluster owned by another AWS account. Entries with a different AWS account number in the `DBClusterArn` field represent clusters that you can clone and that are owned by other AWS accounts. These entries have few fields other than `DBClusterArn`. When creating the cloned cluster, specify the same `StorageEncrypted`, `Engine`, and `EngineVersion` values as in the original cluster. 

   The following example shows a return value that demonstrates both actual and potential cloned clusters. 

  ```
  {
    "DBClusters": [
        {
            "EarliestRestorableTime": "2023-02-01T21:17:54.106Z",
            "Engine": "aurora-mysql",
            "EngineVersion": "8.0.mysql_aurora.3.02.0",
            "CrossAccountClone": false,
  ...
        },
        {
            "EarliestRestorableTime": "2023-02-09T16:01:07.398Z",
            "Engine": "aurora-mysql",
            "EngineVersion": "8.0.mysql_aurora.3.02.0",
            "CrossAccountClone": true,
  ...
        },
        {
            "StorageEncrypted": false,
            "DBClusterArn": "arn:aws:rds:us-east-1:12345678:cluster:cluster-abcdefgh",
            "Engine": "aurora-mysql",
            "EngineVersion": "8.0.mysql_aurora.3.02.0"
        }
    ]
  }
  ```