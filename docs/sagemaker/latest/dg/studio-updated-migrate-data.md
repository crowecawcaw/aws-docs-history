# (Optional) Migrate data from

Studio Classic to Studio

Studio Classic and Studio use two different types of storage volumes. Studio Classic uses a
single Amazon Elastic File System (Amazon EFS) volume to store data across all users and shared spaces in the
domain. In Studio, each space gets its own Amazon Elastic Block Store (Amazon EBS) volume. When you update
the default experience of an existing domain, SageMaker AI automatically mounts a folder in an Amazon EFS
volume for each user in a domain. As a result, users are able to access files from
Studio Classic in their Studio applications. For more information, see [Amazon EFS auto-mounting in Studio](studio-updated-automount.md "studio-updated-automount.md").

You can also opt out of Amazon EFS auto-mounting and manually migrate the data to give users
access to files from Studio Classic in Studio applications. To accomplish this, you must
transfer the files from the user home directories to the Amazon EBS volumes associated with those
spaces. The following section gives information about this workflow. For more information
about opting out of Amazon EFS auto-mounting, see [Opt out of Amazon EFS auto-mounting](studio-updated-automount-optout.md "studio-updated-automount-optout.md").

## Manually migrate all of your data from

Studio Classic

The following section describes how to migrate all of the data from your Studio Classic storage
volume to the new Studio experience.

When manually migrating a user's data, code, and artifacts from Studio Classic to
Studio, we recommend one of the following approaches:

1. Using a custom Amazon EFS volume
2. Using Amazon Simple Storage Service (Amazon S3)

If you used Amazon SageMaker Data Wrangler in Studio Classic and want to migrate your data flow files, then
choose one of the following options for migration:

- If you want to migrate all of the data from your Studio Classic storage volume,
  including your data flow files, go to Manually migrate all of your data from
  Studio Classic and complete the section
  **Use Amazon S3 to migrate data**. Then, skip to the
  [Import the flow files into Canvas](#studio-updated-migrate-flows-import "#studio-updated-migrate-flows-import") section.
- If you only want to migrate your data flow files and no other data from your
  Studio Classic storage volume, skip to the [Migrate data flows from Data Wrangler](#studio-updated-migrate-flows "#studio-updated-migrate-flows") section.

### Prerequisites

Before running these steps, complete the prerequisites in [Complete prerequisites to migrate the
Studio experience](studio-updated-migrate-prereq.md "studio-updated-migrate-prereq.md"). You must also complete the steps in [Migrate the UI from Studio Classic to
Studio](studio-updated-migrate-ui.md "studio-updated-migrate-ui.md").

### Choosing an approach

Consider the following when choosing an approach to migrate your Studio Classic
data.

Pros and cons of using a custom Amazon EFS volume

In this approach, you use an Amazon EFS-to-Amazon EFS AWS DataSync task (one time or
cadence) to copy data, then mount the target Amazon EFS volume to a user’s spaces. This gives
users access to data from Studio Classic in their Studio compute environments.

Pros:

- Only the user’s home directory data is visible in the user's spaces. There is
  no data cross-pollination.
- Syncing from the source Amazon EFS volume to a target Amazon EFS volume is safer than
  directly mounting the source Amazon EFS volume managed by SageMaker AI into spaces. This
  avoids the potential to impact home directory user files.
- Users have the flexibility to continue working in Studio Classic and Studio
  applications, while having their data available in both applications if
  AWS DataSync is set up on a regular cadence.
- No need for repeated push and pull with Amazon S3.

Cons:

- No write access to the target Amazon EFS volume mounted to user's spaces. To get
  write access to the target Amazon EFS volume, customers would need to mount the
  target Amazon EFS volume to an Amazon Elastic Compute Cloud instance and provide appropriate permissions
  for users to write to the Amazon EFS prefix.
- Requires modification to the security groups managed by SageMaker AI to allow network
  file system (NFS) inbound and outbound flow.
- Costs more than using Amazon S3.
- If [migrating data flows
  from Data Wrangler in Studio Classic](#studio-updated-migrate-flows "#studio-updated-migrate-flows"), you must follow the steps for manually
  exporting flow files.

Pros and cons of using Amazon S3

In this approach, you use an Amazon EFS-to-Amazon S3 AWS DataSync task (one time or
cadence) to copy data, then create a lifecycle configuration to copy the user’s data
from Amazon S3 to their private space’s Amazon EBS volume.

Pros:

- If the LCC is attached to the domain, users can choose to use the LCC to copy
  data to their space or to run the space with no LCC script. This gives users the
  choice to copy their files only to the spaces they need.
- If an AWS DataSync task is set up on a cadence, users can restart
  their Studio application to get the latest files.
- Because the data is copied over to Amazon EBS, users have write permissions on the
  files.
- Amazon S3 storage is cheaper than Amazon EFS.
- If [migrating data flows
  from Data Wrangler in Studio Classic](#studio-updated-migrate-flows "#studio-updated-migrate-flows"), you can skip the manual export steps and
  directly import the data flows into SageMaker Canvas from Amazon S3.

Cons:

- If administrators need to prevent cross-pollination, they must create
  AWS Identity and Access Management policies at the user level to ensure users can only access the Amazon S3
  prefix that contains their files.

In this approach, you use an Amazon EFS-to-Amazon EFS AWS DataSync to copy the contents of a
Studio Classic Amazon EFS volume to a target Amazon EFS volume once or in a regular cadence, then
mount the target Amazon EFS volume to a user’s spaces. This gives users access to data
from Studio Classic in their Studio compute environments.

1. Create a target Amazon EFS volume. You will transfer data into this Amazon EFS volume
   and mount it to a corresponding user's space using prefix-level
   mounting.

```
export SOURCE_DOMAIN_ID="`domain-id`"
export AWS_REGION="`region`"

export TARGET_EFS=$(aws efs create-file-system --performance-mode generalPurpose --throughput-mode bursting --encrypted --region $REGION | jq -r '.FileSystemId')

echo "Target EFS volume Created: $TARGET_EFS"
```

2. Add variables for the source Amazon EFS volume currently attached to the domain and
   used by all users. The domain's Amazon Virtual Private Cloud information is required to ensure
   the target Amazon EFS is created in the same Amazon VPC and subnet, with the same
   security group configuration.

```
export SOURCE_EFS=$(aws sagemaker describe-domain --domain-id $SOURCE_DOMAIN_ID | jq -r '.HomeEfsFileSystemId')
export VPC_ID=$(aws sagemaker describe-domain --domain-id $SOURCE_DOMAIN_ID | jq -r '.VpcId')

echo "EFS managed by SageMaker: $SOURCE_EFS | VPC: $VPC_ID"
```

3. Create an Amazon EFS mount target in the same Amazon VPC and subnet as the source Amazon EFS
   volume, with the same security group configuration. The mount target takes a
   few minutes to be available.

```
export EFS_VPC_ID=$(aws efs describe-mount-targets --file-system-id $SOURCE_EFS | jq -r ".MountTargets[0].VpcId")
export EFS_AZ_NAME=$(aws efs describe-mount-targets --file-system-id $SOURCE_EFS | jq -r ".MountTargets[0].AvailabilityZoneName")
export EFS_AZ_ID=$(aws efs describe-mount-targets --file-system-id $SOURCE_EFS | jq -r ".MountTargets[0].AvailabilityZoneId")
export EFS_SUBNET_ID=$(aws efs describe-mount-targets --file-system-id $SOURCE_EFS | jq -r ".MountTargets[0].SubnetId")
export EFS_MOUNT_TARG_ID=$(aws efs describe-mount-targets --file-system-id $SOURCE_EFS | jq -r ".MountTargets[0].MountTargetId")
export EFS_SG_IDS=$(aws efs describe-mount-target-security-groups --mount-target-id $EFS_MOUNT_TARG_ID | jq -r '.SecurityGroups[]')

aws efs create-mount-target \
--file-system-id $TARGET_EFS \
--subnet-id $EFS_SUBNET_ID \
--security-groups $EFS_SG_IDS
```

4. Create Amazon EFS source and destination locations for the AWS DataSync task.

```
export SOURCE_EFS_ARN=$(aws efs describe-file-systems --file-system-id $SOURCE_EFS | jq -r ".FileSystems[0].FileSystemArn")
export TARGET_EFS_ARN=$(aws efs describe-file-systems --file-system-id $TARGET_EFS | jq -r ".FileSystems[0].FileSystemArn")
export EFS_SUBNET_ID_ARN=$(aws ec2 describe-subnets --subnet-ids $EFS_SUBNET_ID | jq -r ".Subnets[0].SubnetArn")
export ACCOUNT_ID=$(aws ec2 describe-security-groups --group-id $EFS_SG_IDS | jq -r ".SecurityGroups[0].OwnerId")
export EFS_SG_ID_ARN=arn:aws:ec2:$REGION:$ACCOUNT_ID:security-group/$EFS_SG_IDS

export SOURCE_LOCATION_ARN=$(aws datasync create-location-efs --subdirectory "/" --efs-filesystem-arn $SOURCE_EFS_ARN --ec2-config SubnetArn=$EFS_SUBNET_ID_ARN,SecurityGroupArns=$EFS_SG_ID_ARN --region $REGION | jq -r ".LocationArn")
export DESTINATION_LOCATION_ARN=$(aws datasync create-location-efs --subdirectory "/" --efs-filesystem-arn $TARGET_EFS_ARN --ec2-config SubnetArn=$EFS_SUBNET_ID_ARN,SecurityGroupArns=$EFS_SG_ID_ARN --region $REGION | jq -r ".LocationArn")
```

5.  Allow traffic between the source and target network file system (NFS) mounts.
    When a new domain is created, SageMaker AI creates 2 security groups.

        * NFS inbound security group with only inbound traffic.
        * NFS outbound security group with only outbound traffic.

    The source and target NFS are placed inside the same security groups. You can
    allow traffic between these mounts from the AWS Management Console or AWS CLI.

        * Allow traffic from the AWS Management Console



        	1. Sign in to the AWS Management Console and open the Amazon VPC console at
        	 [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
        	2. Choose **Security Groups**.
        	3. Search for the existing domain's ID on the **Security
        	 Groups** page.



        	```
        	d-`xxxxxxx`
        	```

        	The results should return two security groups that include the domain ID in the name.




        		+ `security-group-for-inbound-nfs-`domain-id``
        		+ `security-group-for-outbound-nfs-`domain-id``
        	4. Select the inbound security group ID. This opens a new page with details about the security group.
        	5. Select the **Outbound Rules** tab.
        	6. Select **Edit outbound rules**.
        	7. Update the existing outbound rules or add a new outbound rule with the following values:




        		+ Type: NFS
        		+ Protocol: TCP
        		+ Port range: 2049
        		+ Destination:
        		 security-group-for-outbound-nfs-`domain-id`

    | `security-group-id` 8. Choose **Save rules**. 9. Select the **Inbound Rules** tab. 10. Select **Edit inbound rules**. 11. Update the existing inbound rules or add a new outbound rule with the following values: + Type: NFS + Protocol: TCP + Port range: 2049 + Destination: security-group-for-outbound-nfs-`domain-id`
    | `security-group-id` 12. Choose **Save rules**. <br>• Allow traffic from the AWS CLI 1. Update the security group inbound and outbound rules with the following values: + Protocol: TCP + Port range: 2049 + Group ID: Inbound security group ID or outbound security group ID `export INBOUND_SG_ID=$(aws ec2 describe-security-groups --filters "Name=group-name,Values=security-group-for-inbound-nfs-$SOURCE_DOMAIN_ID" | jq -r ".SecurityGroups[0].GroupId") export OUTBOUND_SG_ID=$(aws ec2 describe-security-groups --filters "Name=group-name,Values=security-group-for-outbound-nfs-$SOURCE_DOMAIN_ID" | jq -r ".SecurityGroups[0].GroupId") echo "Outbound SG ID: $OUTBOUND_SG_ID | Inbound SG ID: $INBOUND_SG_ID" aws ec2 authorize-security-group-egress \ --group-id $INBOUND_SG_ID \ --protocol tcp --port 2049 \ --source-group $OUTBOUND_SG_ID aws ec2 authorize-security-group-ingress \ --group-id $OUTBOUND_SG_ID \ --protocol tcp --port 2049 \ --source-group $INBOUND_SG_ID` 2. Add both the inbound and outbound security groups to the source and target Amazon EFS mount targets. This allows traffic between the 2 Amazon EFS mounts. `export SOURCE_EFS_MOUNT_TARGET=$(aws efs describe-mount-targets --file-system-id $SOURCE_EFS | jq -r ".MountTargets[0].MountTargetId") export TARGET_EFS_MOUNT_TARGET=$(aws efs describe-mount-targets --file-system-id $TARGET_EFS | jq -r ".MountTargets[0].MountTargetId") aws efs modify-mount-target-security-groups \ --mount-target-id $SOURCE_EFS_MOUNT_TARGET \ --security-groups $INBOUND_SG_ID $OUTBOUND_SG_ID aws efs modify-mount-target-security-groups \ --mount-target-id $TARGET_EFS_MOUNT_TARGET \ --security-groups $INBOUND_SG_ID $OUTBOUND_SG_ID` 6. Create a AWS DataSync task. This returns a task ARN that can be used to run the task on-demand or as part of a regular cadence. `export EXTRA_XFER_OPTIONS='VerifyMode=ONLY_FILES_TRANSFERRED,OverwriteMode=ALWAYS,Atime=NONE,Mtime=NONE,Uid=NONE,Gid=NONE,PreserveDeletedFiles=REMOVE,PreserveDevices=NONE,PosixPermissions=NONE,TaskQueueing=ENABLED,TransferMode=CHANGED,SecurityDescriptorCopyFlags=NONE,ObjectTags=NONE' export DATASYNC_TASK_ARN=$(aws datasync create-task --source-location-arn $SOURCE_LOCATION_ARN --destination-location-arn $DESTINATION_LOCATION_ARN --name "SMEFS_to_CustomEFS_Sync" --region $REGION --options $EXTRA_XFER_OPTIONS | jq -r ".TaskArn")` 7. Start a AWS DataSync task to automatically copy data from the source Amazon EFS to the target Amazon EFS mount. This does not retain the file's POSIX permissions, which allows users to read from the target Amazon EFS mount, but not write to it. `aws datasync start-task-execution --task-arn $DATASYNC_TASK_ARN` 8. Mount the target Amazon EFS volume on the domain at the root level. `aws sagemaker update-domain --domain-id $SOURCE_DOMAIN_ID \ --default-user-settings '{"CustomFileSystemConfigs": [{"EFSFileSystemConfig": {"FileSystemId": "'"$TARGET_EFS"'", "FileSystemPath": "/"}}]}'` 9. Overwrite every user profile with a `FileSystemPath` prefix. The prefix includes the user’s UID, which is created by SageMaker AI. This ensure user’s only have access to their data and prevents cross-pollination. When a space is created in the domain and the target Amazon EFS volume is mounted to the application, the user’s prefix overwrites the domain prefix. As a result, SageMaker AI only mounts the `/user-id` directory on the user's application. `aws sagemaker list-user-profiles --domain-id $SOURCE_DOMAIN_ID | jq -r '.UserProfiles[] | "\(.UserProfileName)"' | while read user; do export uid=$(aws sagemaker describe-user-profile --domain-id $SOURCE_DOMAIN_ID --user-profile-name $user | jq -r ".HomeEfsFileSystemUid") echo "$user $uid" aws sagemaker update-user-profile --domain-id $SOURCE_DOMAIN_ID --user-profile-name $user --user-settings '{"CustomFileSystemConfigs": [{"EFSFileSystemConfig":{"FileSystemId": "'"$TARGET_EFS"'", "FileSystemPath": "'"/$uid/"'"}}]}' done` 10. Users can then select the custom Amazon EFS filesystem when launching an application. For more information, see [JupyterLab user guide](studio-updated-jl-user-guide.md "studio-updated-jl-user-guide.md") or [Launch a Code Editor application in Studio](code-editor-use-studio.md "code-editor-use-studio.md"). In this approach, you use an Amazon EFS-to-Amazon S3 AWS DataSync task to copy the contents of a Studio Classic Amazon EFS volume to an Amazon S3 bucket once or in a regular cadence, then create a lifecycle configuration to copy the user’s data from Amazon S3 to their private space’s Amazon EBS volume. ###### Note This approach only works for domains that have internet access. 1. Set the source Amazon EFS volume ID from the domain containing the data that you are migrating. ``timestamp=$(date +%Y%m%d%H%M%S) export SOURCE_DOMAIN_ID="`domain-id`" export AWS_REGION="`region`" export ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text) export EFS_ID=$(aws sagemaker describe-domain --domain-id $SOURCE_DOMAIN_ID | jq -r '.HomeEfsFileSystemId')`` 2. Set the target Amazon S3 bucket name. For information about creating an Amazon S3 bucket, see [Creating a bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md"). The bucket used must have a CORS policy as described in [(Optional) Update your CORS policy to access Amazon S3 buckets](studio-updated-migrate-ui.md#studio-updated-migrate-cors "studio-updated-migrate-ui.md#studio-updated-migrate-cors"). Users in the domain must also have permissions to access the Amazon S3 bucket. In this example, we are copying files to a prefix named `studio-new`. If you are using a single Amazon S3 bucket to migrate multiple domains, use the `studio-new/<domain-id>` prefix to restrict permissions to the files using IAM. ``export BUCKET_NAME=`s3-bucket-name` export S3_DESTINATION_PATH=studio-new`` 3. Create a trust policy that gives AWS DataSync permissions to assume the execution role of your account. `export TRUST_POLICY=$(cat <<EOF { "Version": "2012-10-17", "Statement": [ { "Effect": "Allow", "Principal": { "Service": "datasync.amazonaws.com" }, "Action": "sts:AssumeRole", "Condition": { "StringEquals": { "aws:SourceAccount": "$ACCOUNT_ID" }, "ArnLike": { "aws:SourceArn": "arn:aws:datasync:$REGION:$ACCOUNT_ID:*" } } } ] } EOF )` 4. Create an IAM role and attach the trust policy. `export timestamp=$(date +%Y%m%d%H%M%S) export ROLE_NAME="DataSyncS3Role-$timestamp" aws iam create-role --role-name $ROLE_NAME --assume-role-policy-document "$TRUST_POLICY" aws iam attach-role-policy --role-name $ROLE_NAME --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess echo "Attached IAM Policy AmazonS3FullAccess" aws iam attach-role-policy --role-name $ROLE_NAME --policy-arn arn:aws:iam::aws:policy/AmazonSageMakerFullAccess echo "Attached IAM Policy AmazonSageMakerFullAccess" export ROLE_ARN=$(aws iam get-role --role-name $ROLE_NAME --query 'Role.Arn' --output text) echo "Created IAM Role $ROLE_ARN"` 5. Create a security group to give access to the Amazon EFS location. `export EFS_ARN=$(aws efs describe-file-systems --file-system-id $EFS_ID | jq -r '.FileSystems[0].FileSystemArn' ) export EFS_SUBNET_ID=$(aws efs describe-mount-targets --file-system-id $EFS_ID | jq -r '.MountTargets[0].SubnetId') export EFS_VPC_ID=$(aws efs describe-mount-targets --file-system-id $EFS_ID | jq -r '.MountTargets[0].VpcId') export MOUNT_TARGET_ID=$(aws efs describe-mount-targets --file-system-id $EFS_ID | jq -r '.MountTargets[0].MountTargetId ') export EFS_SECURITY_GROUP_ID=$(aws efs describe-mount-target-security-groups --mount-target-id $MOUNT_TARGET_ID | jq -r '.SecurityGroups[0]') export EFS_SUBNET_ARN=$(aws ec2 describe-subnets --subnet-ids $EFS_SUBNET_ID | jq -r '.Subnets[0].SubnetArn') echo "Subnet ID: $EFS_SUBNET_ID" echo "Security Group ID: $EFS_SECURITY_GROUP_ID" echo "Subnet ARN: $EFS_SUBNET_ARN" timestamp=$(date +%Y%m%d%H%M%S) sg_name="datasync-sg-$timestamp" export DATASYNC_SG_ID=$(aws ec2 create-security-group --vpc-id $EFS_VPC_ID --group-name $sg_name --description "DataSync SG" --output text --query 'GroupId') aws ec2 authorize-security-group-egress --group-id $DATASYNC_SG_ID --protocol tcp --port 2049 --source-group $EFS_SECURITY_GROUP_ID aws ec2 authorize-security-group-ingress --group-id $EFS_SECURITY_GROUP_ID --protocol tcp --port 2049 --source-group $DATASYNC_SG_ID export DATASYNC_SG_ARN="arn:aws:ec2:$REGION:$ACCOUNT_ID:security-group/$DATASYNC_SG_ID" echo "Security Group ARN: $DATASYNC_SG_ARN"` 6. Create a source Amazon EFS location for the AWS DataSync task. `export SOURCE_ARN=$(aws datasync create-location-efs --efs-filesystem-arn $EFS_ARN --ec2-config "{\"SubnetArn\": \"$EFS_SUBNET_ARN\", \"SecurityGroupArns\": [\"$DATASYNC_SG_ARN\"]}" | jq -r '.LocationArn') echo "Source Location ARN: $SOURCE_ARN"` 7. Create a target Amazon S3 location for the AWS DataSync task. `export BUCKET_ARN="arn:aws:s3:::$BUCKET_NAME" export DESTINATION_ARN=$(aws datasync create-location-s3 --s3-bucket-arn $BUCKET_ARN --s3-config "{\"BucketAccessRoleArn\": \"$ROLE_ARN\"}" --subdirectory $S3_DESTINATION_PATH | jq -r '.LocationArn') echo "Destination Location ARN: $DESTINATION_ARN"` 8. Create a AWS DataSync task. `export TASK_ARN=$(aws datasync create-task --source-location-arn $SOURCE_ARN --destination-location-arn $DESTINATION_ARN | jq -r '.TaskArn') echo "DataSync Task: $TASK_ARN"` 9. Start the AWS DataSync task. This task automatically copies data from the source Amazon EFS volume to the target Amazon S3 bucket. Wait for the task to be complete. `aws datasync start-task-execution --task-arn $TASK_ARN` 10. Check the status of the AWS DataSync task to verify that it is complete. Pass the ARN returned in the previous step. ``export TASK_EXEC_ARN=`datasync-task-arn` echo "Task execution ARN: $TASK_EXEC_ARN" export STATUS=$(aws datasync describe-task-execution --task-execution-arn $TASK_EXEC_ARN | jq -r '.Status') echo "Execution status: $STATUS" while [ "$STATUS" = "QUEUED" ] || [ "$STATUS" = "LAUNCHING" ] || [ "$STATUS" = "PREPARING" ] || [ "$STATUS" = "TRANSFERRING" ] || [ "$STATUS" = "VERIFYING" ]; do STATUS=$(aws datasync describe-task-execution --task-execution-arn $TASK_EXEC_ARN | jq -r '.Status') if [ $? -ne 0 ]; then echo "Error Running DataSync Task" exit 1 fi echo "Execution status: $STATUS" sleep 30 done`` 11. After the AWS DataSync task is complete, clean up the previously created resources. `aws datasync delete-task --task-arn $TASK_ARN echo "Deleted task $TASK_ARN" aws datasync delete-location --location-arn $SOURCE_ARN echo "Deleted location source $SOURCE_ARN" aws datasync delete-location --location-arn $DESTINATION_ARN echo "Deleted location source $DESTINATION_ARN" aws iam detach-role-policy --role-name $ROLE_NAME --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess aws iam detach-role-policy --role-name $ROLE_NAME --policy-arn arn:aws:iam::aws:policy/AmazonSageMakerFullAccess aws iam delete-role --role-name $ROLE_NAME echo "Deleted IAM Role $ROLE_NAME" echo "Wait 5 minutes for the elastic network interface to detach..." start_time=$(date +%s) while [[ $(($(date +%s) - start_time)) -lt 300 ]]; do sleep 1 done aws ec2 revoke-security-group-ingress --group-id $EFS_SECURITY_GROUP_ID --protocol tcp --port 2049 --source-group $DATASYNC_SG_ID echo "Revoked Ingress from $EFS_SECURITY_GROUP_ID" aws ec2 revoke-security-group-egress --group-id $DATASYNC_SG_ID --protocol tcp --port 2049 --source-group $EFS_SECURITY_GROUP_ID echo "Revoked Egress from $DATASYNC_SG_ID" aws ec2 delete-security-group --group-id $DATASYNC_SG_ID echo "Deleted DataSync SG $DATASYNC_SG_ID"` 12. From your local machine, create a file named `on-start.sh` with the following content. This script copies the user’s Amazon EFS home directory in Amazon S3 to the user’s Amazon EBS volume in Studio and creates a prefix for each user profile. ``#!/bin/bash set -eo pipefail sudo apt-get install -y jq # Studio Variables DOMAIN_ID=$(cat /opt/ml/metadata/resource-metadata.json | jq -r '.DomainId') SPACE_NAME=$(cat /opt/ml/metadata/resource-metadata.json | jq -r '.SpaceName') USER_PROFILE_NAME=$(aws sagemaker describe-space --domain-id=$DOMAIN_ID --space-name=$SPACE_NAME | jq -r '.OwnershipSettings.OwnerUserProfileName') # S3 bucket to copy from BUCKET=`s3-bucket-name` # Subfolder in bucket to copy PREFIX=studio-new # Getting HomeEfsFileSystemUid for the current user-profile EFS_FOLDER_ID=$(aws sagemaker describe-user-profile --domain-id $DOMAIN_ID --user-profile-name $USER_PROFILE_NAME | jq -r '.HomeEfsFileSystemUid') # Local destination directory DEST=./studio-classic-efs-backup mkdir -p $DEST echo "Bucket: s3://$BUCKET/$PREFIX/$EFS_FOLDER_ID/" echo "Destination $DEST/" echo "Excluding .*" echo "Excluding .*/*" aws s3 cp s3://$BUCKET/$PREFIX/$EFS_FOLDER_ID/ $DEST/ \ --exclude ".*" \ --exclude "**/.*" \ --recursive`` 13. Convert your script into base64 format. This requirement prevents errors that occur from spacing and line break encoding. The script type can be either `JupyterLab` or `CodeEditor`. `` export LCC_SCRIPT_NAME='studio-classic-sync' export SCRIPT_FILE_NAME='on-start.sh' export SCRIPT_TYPE='`JupyterLab-or-CodeEditor`' LCC_CONTENT=`openssl base64 -A -in ${SCRIPT_FILE_NAME}` `` 14. Verify the following before you use the script: <br>• The Amazon EBS volume is large enough to store the objects that you're exporting. <br>• You aren't migrating hidden files and folders, such as `.bashrc` and `.condarc` if you aren't intending to do so. <br>• The AWS Identity and Access Management (IAM) execution role that's associated with Studio user profiles has the policies configured to access only the respective home directory in Amazon S3. 15. Create a lifecycle configuration using your script. `aws sagemaker create-studio-lifecycle-config \ --studio-lifecycle-config-name $LCC_SCRIPT_NAME \ --studio-lifecycle-config-content $LCC_CONTENT \ --studio-lifecycle-config-app-type $SCRIPT_TYPE` 16. Attach the LCC to your domain. ``aws sagemaker update-domain \ --domain-id $SOURCE_DOMAIN_ID \ --default-user-settings ' {"JupyterLabAppSettings": {"LifecycleConfigArns": [ "`lifecycle-config-arn`" ] } }'`` 17. Users can then select the LCC script when launching an application. For more information, see [JupyterLab user guide](studio-updated-jl-user-guide.md "studio-updated-jl-user-guide.md") or [Launch a Code Editor application in Studio](code-editor-use-studio.md "code-editor-use-studio.md"). This automatically syncs the files from Amazon S3 to the Amazon EBS storage for the user's space. ## Migrate data flows from Data Wrangler If you have previously used Amazon SageMaker Data Wrangler in Amazon SageMaker Studio Classic for data preparation tasks, you can migrate to the new Amazon SageMaker Studio and access the latest version of Data Wrangler in Amazon SageMaker Canvas. Data Wrangler in SageMaker Canvas provides you with an enhanced user experience and access to the latest features, such as a natural language interface and faster performance. You can onboard to SageMaker Canvas at any time to begin using the new Data Wrangler experience. For more information, see [Getting started with using Amazon SageMaker Canvas](canvas-getting-started.md "canvas-getting-started.md"). If you have data flow files saved in Studio Classic that you were previously working on, you can onboard to Studio and then import the flow files into Canvas. You have the following options for migration: <br>• One-click migration: When you sign in to Canvas, you can use a one-time import option that migrates all of your flow files on your behalf. <br>• Manual migration: You can manually import your flow files into Canvas. From Studio Classic, either export the files to Amazon S3 or download them to your local machine. Then, you sign in to the SageMaker Canvas application, import the flow files, and continue your data preparation tasks. The following guide describes the prerequisites to migration and how to migrate your data flow files using either the one-click or manual option. ### Prerequisites Review the following prerequisites before you begin migrating your flow files. **Step 1. Migrate the domain and grant permissions** Before migrating data flow files, you need to follow specific steps of the [Migration from Amazon SageMaker Studio Classic](studio-updated-migrate.md "studio-updated-migrate.md") guide to ensure that your user profile's AWS IAM execution role has the required permissions. Follow the [Prerequisites](studio-updated-migrate-prereq.md "studio-updated-migrate-prereq.md") and [Migrate the UI from Studio Classic to Studio](studio-updated-migrate-ui.md "studio-updated-migrate-ui.md") before proceeding, which describe how to grant the required permissions, configure Studio as the new experience, and migrate your existing domain. Specifically, you must have permissions to create a SageMaker Canvas application and use the SageMaker Canvas data preparation features. To obtain these permissions, you can either: <br>• Add the [AmazonSageMakerCanvasDataPrepFullAccess](../../../aws-managed-policy/latest/reference/AmazonSageMakerCanvasDataPrepFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonSageMakerCanvasDataPrepFullAccess.md") policy to your IAM role, or <br>• Attach a least-permissions policy, as shown in the **(Optional) Migrate from Data Wrangler in Studio Classic to SageMaker Canvas** section of the page [Migrate the UI from Studio Classic to Studio](studio-updated-migrate-ui.md "studio-updated-migrate-ui.md"). Make sure to use the same user profile for both Studio and SageMaker Canvas. After completing the prerequisites outlined in the migration guide, you should have a new domain with the required permissions to access SageMaker Canvas through Studio. **Step 2. (Optional) Prepare an Amazon S3 location** If you are doing a manual migration and plan to use Amazon S3 to transfer your flow files instead of using the local download option, you should have an Amazon S3 bucket in your account that you'd like to use for storing the flow files. ### One-click migration method SageMaker Canvas offers a one-time import option for migrating your data flows from Data Wrangler in Studio Classic to Data Wrangler in SageMaker Canvas. As long as your Studio Classic and Canvas applications share the same Amazon EFS storage volume, you can migrate in one click from Canvas. This streamlined process eliminates the need for manual export and import steps, and you can import all of your flows at once. Use the following procedure to migrate all of your flow files: 1. Open your latest version of Studio. 2. In Studio, in the left navigation pane, choose the **Data** dropdown menu. 3. From the navigation options, choose **Data Wrangler**. 4. On the **Data Wrangler** page, choose **Run in Canvas**. If you have successfully set up the permissions, this creates a Canvas application for you. The Canvas application may take a few minutes before it's ready. 5. When Canvas is ready, choose **Open in Canvas.** 6. Canvas opens to the **Data Wrangler** page, and a banner at the top of the page appears that says **`Import your data flows from Data Wrangler in Studio Classic to Canvas. This is a one time import. Learn more.`** In the banner, choose **Import All**. ###### Warning If you close the banner notification, you won't be able to re-open it or use the one-click migration method anymore. A pop-up notification appears, indicating that Canvas is importing your flow files from Studio Classic. If the import is fully successful, you receive another notification that `X` number of flow files were imported, and you can see your flow files on the **Data Wrangler** page of the Canvas application. Any imported flow files that have the same name as existing data flows in your Canvas application are renamed with a postfix. You can open a data flow to verify that it looks as expected. In case any of your flow files don't import successfully, you receive a notification that the import was either partially successful or failed. Choose **View errors** on the notification message to check the individual error messages for guidance on how to reformat any incorrectly formatted flow files. After importing your flow files, you should now be able to continue using Data Wrangler to prepare data in SageMaker Canvas. ### Manual migration method The following sections describe how to manually import your flow files into Canvas in case the one-click migration method didn't work. #### Export the flow files from Studio Classic ###### Note If you've already migrated your Studio Classic data to Amazon S3 by following the instructions in [(Optional) Migrate data from Studio Classic to Studio](studio-updated-migrate-data.md "studio-updated-migrate-data.md"), you can skip this step and go straight to the [Import the flow files into Canvas](#studio-updated-migrate-flows-import "#studio-updated-migrate-flows-import") section in which you import your flow files from the Amazon S3 location where your Studio Classic data is stored. You can export your flow files by either saving them to Amazon S3 or downloading them to your local machine. When you import your flow files into SageMaker Canvas in the next step, if you choose the local upload option, then you can only upload 20 flow files at a time. If you have a large number of flow files to import, we recommend that you use Amazon S3 instead. Follow the instructions in either [Method 1: Use Amazon S3 to transfer flow files](#studio-updated-migrate-flows-export-s3 "#studio-updated-migrate-flows-export-s3") or [Method 2: Use your local machine to transfer flow files](#studio-updated-migrate-flows-export-local "#studio-updated-migrate-flows-export-local") to proceed. ##### Method 1: Use Amazon S3 to transfer flow files With this method, you use Amazon S3 as the intermediary between Data Wrangler in Studio Classic and Data Wrangler in SageMaker Canvas (accessed through the latest version of Studio). You export the flow files from Studio Classic to Amazon S3, and then in the next step, you access Canvas through Studio and import the flow files from Amazon S3. Make sure that you have an Amazon S3 bucket prepared as the storage location for the flow files. Use the following procedure to export your flow files from Studio Classic to Amazon S3: 1. Open Studio Classic. 2. Open a new terminal by doing the following: 1. On the top navigation bar, choose **File**. 2. In the context menu, hover over **New**, and then select **Terminal**. 3. By default, the terminal should open in your home directory. Navigate to the folder that contains all of the flow files that you want to migrate. 4. Use the following command to synchronize all of the flow files to the specified Amazon S3 location. Replace `{bucket-name}` and `{folder}` with the path to your desired Amazon S3 location. For more information about the command and parameters, see the [sync](../../../cli/latest/reference/s3/sync.md "../../../cli/latest/reference/s3/sync.md") command in the AWS AWS CLI Command Reference. ``aws s3 sync . s3://`{bucket-name}`/`{folder}`/ --exclude "*.*" --include "*.flow"`` If you are using your own AWS KMS key, then use the following command instead to synchronize the files, and specify your KMS key ID. Make sure that the user's IAM execution role (which should be the same role used in **Step 1. Migrate the domain and grant permissions** of the preceding [Prerequisites](#studio-updated-migrate-flows-prereqs "#studio-updated-migrate-flows-prereqs")) has been granted access to use the KMS key. `` aws s3 sync . s3://`{bucket-name}`/`{folder}`/ --exclude "*.*" --include "*.flow" --sse-kms-key-id `{your-key-id}` `` Your flow files should now be exported. You can check your Amazon S3 bucket to make sure that the flow files synchronized successfully. To import these files in the latest version of Data Wrangler, follow the steps in [Import the flow files into Canvas](#studio-updated-migrate-flows-import "#studio-updated-migrate-flows-import"). ##### Method 2: Use your local machine to transfer flow files With this method, you download the flow files from Studio Classic to your local machine. You can download the files directly, or you can compress them as a zip archive. Then, you unpack the zip file locally (if applicable), sign in to Canvas, and import the flow files by uploading them from your local machine. Use the following procedure to download your flow files from Studio Classic: 1. Open Studio Classic. 2. (Optional) If you want to compress multiple flow files into a zip archive and download them all at once, then do the following: 1. On the top navigation bar of Studio Classic, choose **File**. 2. In the context menu, hover over **New**, and then select **Terminal**. 3. By default, the terminal opens in your home directory. Navigate to the folder that contains all of the flow files that you want to migrate. 4. Use the following command to pack the flow files in the current directory as a zip. The command excludes any hidden files: `find . -not -path "*/.*" -name "*.flow" -print0 | xargs -0 zip my_archive.zip` 3. Download the zip archive or individual flow files to your local machine by doing the following: 1. In the left navigation pane of Studio Classic, choose **File Browser**. 2. Find the file you want to download in the file browser. 3. Right click the file, and in the context menu, select **Download**. The file should download to your local machine. If you packed them as a zip archive, extract the files locally. After the files are extracted, to import these files in the latest version of Data Wrangler, follow the steps in [Import the flow files into Canvas](#studio-updated-migrate-flows-import "#studio-updated-migrate-flows-import"). #### Import the flow files into Canvas After exporting your flow files, access Canvas through Studio and import the files. Use the following procedure to import flow files into Canvas: 1. Open your latest version of Studio. 2. In Studio, in the left navigation pane, choose the **Data** dropdown menu. 3. From the navigation options, choose **Data Wrangler**. 4. On the **Data Wrangler** page, choose **Run in Canvas**. If you have successfully set up the permissions, this creates a Canvas application for you. The Canvas application may take a few minutes before it's ready. 5. When Canvas is ready, choose **Open in Canvas.** 6. Canvas opens to the **Data Wrangler** page. In the top pane, choose **Import data flows**. 7. For **Data source**, choose either **Amazon S3** or **Local upload**. 8. Select your flow files from your Amazon S3 bucket, or upload the files from your local machine. ###### Note For local upload, you can upload a maximum of 20 flow files at a time. For larger imports, use Amazon S3. If you select a folder to import, any flow files in sub-folders are also imported. 9. Choose **Import data**. If the import was successful, you receive a notification that `X` number of flow files were successfully imported. In case your flow files don't import successfully, you receive a notification in the SageMaker Canvas application. Choose **View errors** on the notification message to check the individual error messages for guidance on how to reformat any incorrectly formatted flow files. After your flow files are done importing, go to the **Data Wrangler** page of the SageMaker Canvas application to view your data flows. You can try opening a data flow to verify that it looks as expected.
