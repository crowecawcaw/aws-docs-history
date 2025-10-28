# Monitor, update and delete Amazon EMR Studio resources

This section includes instructions to help you monitor, update, or delete an
EMR Studio resource. For information about assigning users or updating user permissions,
see [Assign and manage EMR Studio users](emr-studio-manage-users.md "emr-studio-manage-users.md").

## View Studio details

Console

###### \*\*To view details about an EMR Studio with the new

console\*\*

1. Open the Amazon EMR console at [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr "https://console.aws.amazon.com/emr").
2. Under **EMR Studio** on the left navigation, choose
   **Studios**.
3. Select the Studio from the **Studios** list
   to open the Studio detail page. The Studio detail page includes
   **Studio setting** information, such as the
   Studio **Description**, **VPC**, and
   **Subnets**.

CLI
**To retrieve details for an EMR Studio by Studio
ID using the AWS CLI**

Use the following `describe-studio` AWS CLI command to fetch detailed
information about a particular EMR Studio. For more information, see the [_AWS CLI Command Reference_](../../../cli/latest/reference/emr/describe-studio.md "../../../cli/latest/reference/emr/describe-studio.md").

```
aws emr describe-studio \
 --studio-id `<id-of-studio-to-describe>` \
```

**To retrieve a list of EMR Studios using the
AWS CLI**

Use the following `list-studios` AWS CLI command. For more information,
see the [_AWS CLI Command Reference_](../../../cli/latest/reference/emr/list-studios.md "../../../cli/latest/reference/emr/list-studios.md").

```
aws emr list-studios
```

The following is an example return value for the `list-studios` command
in JSON format.

```
{
    "Studios": [
        {
            "AuthMode": "IAM",
            "VpcId": "vpc-b21XXXXX",
            "Name": "example-studio-name",
            "Url": "https://es-7HWP74SNGDXXXXXXXXXXXXXXX.emrstudio-prod.us-east-1.amazonaws.com",
            "CreationTime": 1605672582.781,
            "StudioId": "es-7HWP74SNGDXXXXXXXXXXXXXXX",
            "Description": "example studio description"
        }
    ]
}
```

## Monitor Amazon EMR Studio actions

### View EMR Studio and API

activity

EMR Studio is integrated with AWS CloudTrail, a service that provides a record of
actions taken by a user, by an IAM role, or by another AWS service in EMR Studio.
CloudTrail captures API calls for EMR Studio as events. You can view events using the CloudTrail
console at [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/ "https://console.aws.amazon.com/cloudtrail/").

EMR Studio events provide information such as which Studio or IAM user
makes a request, and what kind of request it is.

###### Note

On-cluster actions such as running notebook jobs do not emit AWS CloudTrail.

You can also create a trail for continuous delivery of EMR Studio CloudTrail events to
an Amazon S3 bucket. For more information, see the _[AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md")_.

**Example CloudTrail Event: a user Calls the DescribeStudio
API**

The following is an example AWS CloudTrail event that is created when a user,
`admin`, calls the [DescribeStudio](../APIReference/API_DescribeStudio.md "../APIReference/API_DescribeStudio.md") API. CloudTrail records the user name as
`admin`.

###### Note

To protect Studio details, the EMR Studio API event for
DescribeStudio excludes a value for `responseElements`.

```
{
   "eventVersion":"1.08",
   "userIdentity":{
      "type":"IAMUser",
      "principalId":"AIDXXXXXXXXXXXXXXXXXX",
      "arn":"arn:aws:iam::653XXXXXXXXX:user/`admin`",
      "accountId":"653XXXXXXXXX",
      "accessKeyId":"AKIAIOSFODNN7EXAMPLE",
      "userName":"`admin`"
   },
   "eventTime":"2021-01-07T19:13:58Z",
   "eventSource":"elasticmapreduce.amazonaws.com",
   "eventName":"DescribeStudio",
   "awsRegion":"us-east-1",
   "sourceIPAddress":"72.XX.XXX.XX",
   "userAgent":"aws-cli/1.18.188 Python/3.8.5 Darwin/18.7.0 botocore/1.19.28",
   "requestParameters":{
      "studioId":"es-9O5XXXXXXXXXXXXXXXXXXXXXX"
   },
   **"responseElements":null**,
   "requestID":"0fxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
   "eventID":"b0xxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
   "readOnly":true,
   "eventType":"AwsApiCall",
   "managementEvent":true,
   "eventCategory":"Management",
   "recipientAccountId":"653XXXXXXXXX"
}
```

### View Spark user and job

activity

To view Spark job activity by Amazon EMR Studio users, you can configure user impersonation
on a cluster. With user impersonation, each Spark job that is submitted from a
Workspace is associated with the Studio user who ran the code.

When user impersonation is enabled, Amazon EMR creates an HDFS user directory on the
cluster's primary node for each user that runs code in the Workspace. For example,
if user `studio-user-1@example.com` runs code, you can connect to the primary
node and see that `hadoop fs -ls /user` has a directory for
`studio-user-1@example.com`.

To set up Spark user impersonation, set the following properties in the following
configuration classifications:

- `core-site`
- `livy-conf`

```
[
    {
        "Classification": "core-site",
        "Properties": {
          "hadoop.proxyuser.livy.groups": "*",
          "hadoop.proxyuser.livy.hosts": "*"
        }
    },
    {
        "Classification": "livy-conf",
        "Properties": {
          "livy.impersonation.enabled": "true"
        }
    }
]
```

To view history server pages, see [Debug applications and jobs with EMR Studio](emr-studio-debug.md "emr-studio-debug.md"). You can also connect to the primary node of the
cluster using SSH to view application web interfaces. For more information, see [View web interfaces hosted on Amazon EMR
clusters](emr-web-interfaces.md "emr-web-interfaces.md").

## Update an Amazon EMR Studio

After you create an EMR Studio, you can update the following attributes using the
AWS CLI:

- Name
- Description
- Default S3 location
- Subnets

**To update an EMR Studio using the AWS CLI**

Use the `update-studio` AWS CLI command to update an EMR Studio. For more
information, see the [_AWS CLI Command
Reference_](../../../cli/latest/reference/emr/update-studio.md "../../../cli/latest/reference/emr/update-studio.md").

###### Note

You can associated a Studio with a maximum of 5 subnets. These subnets must
belong to the same VPC as the Studio. The list of subnet IDs that you submit to
the `update-studio` command can include new subnet IDs, but must also include
all of the subnet IDs that you already associated with the Studio. You can't
remove subnets from a Studio.

```
aws emr update-studio \
 --studio-id `<example-studio-id-to-update>` \
 --name `<example-new-studio-name>` \
 --subnet-ids `<old-subnet-id-1 old-subnet-id-2 old-subnet-id-3 new-subnet-id>` \
```

To verify the changes, use the `describe-studio` AWS CLI command and specify
your Studio ID. For more information, see the [_AWS CLI Command
Reference_](../../../cli/latest/reference/emr/describe-studio.md "../../../cli/latest/reference/emr/describe-studio.md").

```
aws emr describe-studio \
 --studio-id `<id-of-updated-studio>` \
```

## Delete an Amazon EMR Studio and

Workspaces

When you delete a Studio, EMR Studio deletes all of the IAM Identity Center user and group
assignments that are associated with the Studio.

###### Note

When you delete a Studio, Amazon EMR does _not_
delete the Workspaces associated with that Studio. You must delete the
Workspaces in your Studio separately.

**Delete Workspaces**

Console
Since each EMR Studio Workspace is an EMR notebook instance,
you can use the Amazon EMR management console to delete Workspaces. You can delete
Workspaces using the Amazon EMR console before or after you delete your
Studio

###### To delete a Workspace using the Amazon EMR console

1. Navigate to the new Amazon EMR console and select **Switch to the old console** from the side navigation. For more information on what to expect when you switch to the old console, see [Using the old console](whats-new-in-console.md#console-opt-in "whats-new-in-console.md#console-opt-in").
2. Choose **Notebooks**.
3. Select the Workspace(s) that you want to delete.
4. Choose **Delete**, then choose **Delete**
   again to confirm.
5. Follow the instructions for [Deleting objects](../../../AmazonS3/latest/user-guide/delete-objects.md "../../../AmazonS3/latest/user-guide/delete-objects.md") in
   the _Amazon Simple Storage Service_
   _Console User Guide_ to remove the notebook files
   associated with the deleted Workspace from Amazon S3.

EMR Studio UI
From the Workspace UIFrom the Workspaces listFrom the Workspace UI###### Delete a Workspace and its associated backup files from
EMR Studio

1. Log in to your EMR Studio with your Studio access URL and
   choose **Workspaces** from the left
   navigation.
2. Find your Workspace in the list, then select the check box next
   to its name. You can select multiple Workspaces to delete at the
   same time.
3. Choose **Delete** in the upper right of the
   **Workspaces** list and confirm that you want
   to delete the selected Workspaces. Choose
   **Delete** to confirm.
4. If you want to remove the notebook files that were associated with the
   deleted Workspace from Amazon S3, follow the instructions for [Deleting
   objects](../../../AmazonS3/latest/user-guide/delete-objects.md "../../../AmazonS3/latest/user-guide/delete-objects.md") in the _Amazon Simple Storage Service_
   _Console User Guide_. If you did not create
   the Studio, consult your Studio administrator to determine
   the Amazon S3 backup location for the deleted Workspace.
   From the Workspaces list###### Delete a Workspace and its associated backup files from the
   Workspaces list

5. Navigate to the **Workspace**s list in the
   console.
6. Select the Workspace that you want to delete from the list and
   then choose **Actions**.
7. Choose **Delete**.
8. If you want to remove the notebook files that were associated with the
   deleted Workspace from Amazon S3, follow the instructions for [Deleting
   objects](../../../AmazonS3/latest/user-guide/delete-objects.md "../../../AmazonS3/latest/user-guide/delete-objects.md") in the _Amazon Simple Storage Service_
   _Console User Guide_. If you did not create
   the Studio, consult your Studio administrator to determine
   the Amazon S3 backup location for the deleted Workspace.

**Delete an EMR Studio**

Console

###### \*\*To delete an EMR Studio with the new

console\*\*

1. Open the Amazon EMR console at [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr "https://console.aws.amazon.com/emr").
2. Under **EMR Studio** on the left navigation, choose
   **Studios**.
3. Select the Studio from the **Studios** list
   with the toggle to the left of the Studio name . Choose
   **Delete**.

Old console

###### \*\*To delete an EMR Studio with the old

console\*\*

1. Open the Amazon EMR console at [https://console.aws.amazon.com/elasticmapreduce/home](https://console.aws.amazon.com/elasticmapreduce/home "https://console.aws.amazon.com/elasticmapreduce/home").
2. Choose **EMR Studio** from the left navigation.
3. Select the Studio from the **Studios** list
   and choose **Delete**.

CLI
**To delete an EMR Studio with the AWS CLI**

Use the `delete-studio` AWS CLI command to delete an EMR Studio. For
more information, see the [_AWS CLI Command
Reference_](../../../cli/latest/reference/emr/delete-studio.md "../../../cli/latest/reference/emr/delete-studio.md").

```
aws emr delete-studio --studio-id `<id-of-studio-to-delete>`
```
