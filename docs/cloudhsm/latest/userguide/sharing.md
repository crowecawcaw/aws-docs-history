# Working with shared backups in AWS CloudHSM

CloudHSM integrates with AWS Resource Access Manager (AWS RAM) to enable resource sharing. AWS RAM is a
 service that enables you to share some CloudHSM resources with other AWS accounts or
 through AWS Organizations. With AWS RAM, you share resources that you own by creating a
 *resource share*. A resource share specifies the resources to share,
 and the consumers with whom to share them. Consumers can include:


* Specific AWS accounts inside or outside of its organization in AWS Organizations
* An organizational unit inside its organization in AWS Organizations
* An entire organization in AWS Organizations
For more information about AWS RAM, see the *[AWS RAM User Guide](https://docs.aws.amazon.com/ram/latest/userguide/ "https://docs.aws.amazon.com/ram/latest/userguide/")*.

This topic explains how to share resources that you own, and how to use resources that are
 shared with you.

###### Contents

* [Prerequisites for sharing backups](#sharing-prereqs "#sharing-prereqs")
* [Sharing a backup](#sharing-share "#sharing-share")
* [Unsharing a shared backup](#sharing-unshare "#sharing-unshare")
* [Identifying a shared backup](#sharing-identify "#sharing-identify")
* [Permissions for shared backups](#sharing-perms "#sharing-perms")
* [Billing and metering](#sharing-billing "#sharing-billing")

## Prerequisites for sharing backups



* To share a backup, you must own it in your AWS account. This means that
 the resource must be allocated or provisioned in your account. You cannot share
 a backup that has been shared with you.
* To share a backup, it must be in the *READY* state.
* To share a backup with your organization or an organizational unit in
 AWS Organizations, you must enable sharing with AWS Organizations. For more information, see
  [Enable Sharing with AWS Organizations](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-sharing.html#getting-started-sharing-orgs "https://docs.aws.amazon.com/ram/latest/userguide/getting-started-sharing.html#getting-started-sharing-orgs") in the
 *AWS RAM User Guide*.

## Sharing a backup


When you share a backup with other AWS accounts, you enable them to restore clusters from the backup which contain the keys and users stored 
 in the backup.
 


To share a backup, you must add it to a resource share. A resource share is an
 AWS RAM resource that lets you share your resources across AWS accounts. A resource
 share specifies the resources to share, and the consumers with whom they are shared.
 When you share a backup using the CloudHSM console, you add it to an existing
 resource share. To add the backup to a new resource share, you must first create the
 resource share using the [AWS RAM
 console](https://console.aws.amazon.com/ram "https://console.aws.amazon.com/ram").


If you are part of an organization in AWS Organizations and sharing within your organization is
 enabled, consumers in your organization are automatically granted access to the shared
 backup. Otherwise, consumers receive an invitation to join the resource share and
 are granted access to the shared backup after accepting the invitation.


You can share a backup that you own using the AWS RAM console or AWS CLI.


###### To share a backup that you own using the AWS RAM console


See [Creating a Resource Share](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing.html#working-with-sharing-create "https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing.html#working-with-sharing-create") in the
 *AWS RAM User Guide*.


###### To share a backup that you own (AWS RAM command)


Use the [create-resource-share](https://docs.aws.amazon.com/cli/latest/reference/ram/create-resource-share.html "https://docs.aws.amazon.com/cli/latest/reference/ram/create-resource-share.html") command.



**To share a backup that you own (CloudHSM command)**



###### Important

While you can share a backup using the CloudHSM PutResourcePolicy operation, we recommend using AWS Resource Access Manager
 (AWS RAM) instead. Using AWS RAM provides multiple benefits as it creates the policy for you, allows multiple resources to be shared at
 one time, and increases the discoverability of shared resources. If you use PutResourcePolicy and want consumers to be able to
 describe the backups you shared with them, you must promote the backup to a standard AWS RAM
 Resource Share using the AWS RAM PromoteResourceShareCreatedFromPolicy API operation.


Use the [put-resource-policy](https://docs.aws.amazon.com/cli/latest/reference/cloudhsmv2/put-resource-policy.html "https://docs.aws.amazon.com/cli/latest/reference/cloudhsmv2/put-resource-policy.html") command.


1. Create a file named `policy.json` and copy the following policy into it.



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement":[
 {
 "Effect":"Allow",
 "Principal": {
 "AWS":"`111122223333`"
 },
 "Action":[
 "cloudhsm:CreateCluster",
 "cloudhsm:DescribeBackups"
 ],
 "Resource":"`arn:aws:cloudhsm:us-west-2:111122223333:backup/backup-to-share`"
 }
 ]
}`

```
2. Update `policy.json` with the backup ARN and identifiers
 to share it with. The following example grants read-only access to the root user
 for the AWS account identified by 123456789012.



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement":[
 {
 "Effect":"Allow",
 "Principal": {
 "AWS": [
 "`123456789012`"
 ]
 },
 "Action": [
 "cloudhsm:CreateCluster",
 "cloudhsm:DescribeBackups"
 ],
 "Resource":"arn:aws:cloudhsm:us-west-2:123456789012:backup/backup-123"
 }
 ]
}`

```





###### Important

You can only grant permissions to DescribeBackups at the account level. When you share a backup with another customer,
 any principal that has DescribeBackups permission in that account can describe the backup.
3. Run the [put-resource-policy](https://docs.aws.amazon.com/cli/latest/reference/cloudhsmv2/put-resource-policy.html "https://docs.aws.amazon.com/cli/latest/reference/cloudhsmv2/put-resource-policy.html") command.



```
`$` `aws cloudhsmv2 put-resource-policy --resource-arn `<resource-arn>` --policy file://policy.json`
```

###### Note

 At this point, the consumer can use the backup but it will not show up in the DescribeBackups response with the shared parameter. 
 The next steps describe how to promote the AWS RAM resource share in order for the backup to be included in the response.
4. Get the AWS RAM resource share ARN.



```
`$` `aws ram list-resources --resource-owner SELF --resource-arns `<backup-arn>``
```

This returns a response similar to this:

 
```
{
  "resources": [
    {
      "arn": "`<project-arn>`",
      "type": "`<type>`",
      "resourceShareArn": "`<resource-share-arn>`",
      "creationTime": "`<creation-time>`",
      "lastUpdatedTime": "`<last-update-time>`"
    }
  ]
}
```

From the response, copy the `<resource-share-arn>` value to use in the next steps.
5. Run the AWS RAM [promote-resource-share-created-from-policy](https://docs.aws.amazon.com/cli/latest/reference/ram/promote-resource-share-created-from-policy.html "https://docs.aws.amazon.com/cli/latest/reference/ram/promote-resource-share-created-from-policy.html") command.



```
`$` `aws ram promote-resource-share-created-from-policy --resource-share-arn `<resource-share-arn>``
```
6. To validate that the resource share has been promoted, you can run the AWS RAM [get-resource-shares](https://docs.aws.amazon.com/cli/latest/reference/ram/get-resource-shares.html "https://docs.aws.amazon.com/cli/latest/reference/ram/get-resource-shares.html") command.



```
`$` `aws ram get-resource-shares --resource-owner SELF --resource-share-arns `<resource-share-arn>``
```

When the policy has been promoted, the `featureSet` listed in the response is `STANDARD`. This also 
means the backup can be described by the new accounts in the policy.

## Unsharing a shared backup


When you unshare a resource, the consumer may no longer use it to restore a cluster. Consumers will still be able to access 
 any clusters that they restored from the shared backup.


To unshare a shared backup that you own, you must remove it from the resource
 share. You can do this using the AWS RAM console or AWS CLI.


###### To unshare a shared backup that you own using the AWS RAM console


See [Updating a Resource Share](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing.html#working-with-sharing-update "https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing.html#working-with-sharing-update") in the *AWS RAM User Guide*.


###### To unshare a shared backup that you own (AWS RAM command)


Use the [disassociate-resource-share](https://docs.aws.amazon.com/cli/latest/reference/ram/disassociate-resource-share.html "https://docs.aws.amazon.com/cli/latest/reference/ram/disassociate-resource-share.html") command.



**To unshare a shared backup that you own (CloudHSM command)**


Use the [delete-resource-policy](https://docs.aws.amazon.com/cli/latest/reference/cloudhsmv2/delete-resource-policy.html "https://docs.aws.amazon.com/cli/latest/reference/cloudhsmv2/delete-resource-policy.html") command.



```
`$` `aws cloudhsmv2 delete-resource-policy --resource-arn `<resource-arn>``
```

## Identifying a shared backup


Consumers can identify a backup shared with them using the CloudHSM console and
 AWS CLI.


###### To identify backups shared with you using the CloudHSM console

1. Open the AWS CloudHSM console at
 [https://console.aws.amazon.com/cloudhsm/home](https://console.aws.amazon.com/cloudhsm/home "https://console.aws.amazon.com/cloudhsm/home").
2. To change the AWS Region, use the Region selector in the upper-right corner of the
 page.
3. In the navigation pane, choose **Backups**.
4. In the table, choose the **Shared backups** tab.

###### To identify backups shared with you using the AWS CLI


Use the [describe-backups](https://docs.aws.amazon.com/cli/latest/reference/cloudhsmv2/describe-backups.html "https://docs.aws.amazon.com/cli/latest/reference/cloudhsmv2/describe-backups.html") command with the `--shared` 
 parameter to return the backups that are shared with you.


## Permissions for shared backups


### Permissions for owners


Backup owners can describe and manage a shared backup as well as use it to restore a cluster.


### Permissions for consumers


Backup consumers cannot modify a shared backup, but they can describe it and use it to restore a cluster.


## Billing and metering


There are no additional charges for sharing backups.
