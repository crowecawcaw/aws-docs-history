# Specify an Amazon S3 Files volume in your Amazon ECS task definition

You can configure S3 Files volumes in your Amazon ECS task definitions using the Amazon ECS
console, the AWS CLI, or the AWS API.

## Using the Amazon ECS console

1. Open the Amazon ECS console at [https://console.aws.amazon.com/ecs/](https://console.aws.amazon.com/ecs/ "https://console.aws.amazon.com/ecs/").
2. In the navigation pane, choose **Task
   definitions**.
3. Choose **Create new task definition** or select an
   existing task definition and create a new revision.
4. In the **Infrastructure** section, ensure you have a
   Task IAM Role configured with the required permissions.
5. In the **Storage** section, choose **Add
   volume**.
6. For **Volume type**, select **S3
   Files**.
7. For **File system ARN**, enter the full ARN of your
   S3 file system. The ARN format is:

```
arn:`{partition}`:s3files:`{region}`:`{account-id}`:file-system/`fs-xxxxx`
```

8. (Optional) For **Root directory**, enter the path
   within the file system to mount as the root. If not specified, the root
   of the file system (`/`) is used.
9. (Optional) For **Transit encryption port**, enter the
   port number for sending encrypted data between the Amazon ECS host and the
   S3 file system. If you don't specify a transit encryption port, it uses the port selection
   strategy that the Amazon EFS mount helper uses.
10. (Optional) For **Access point ARN**, select the S3 Files access point to use from the dropdown list.
11. In the **Container mount points** section, select the
    container and specify the local mount path in your container where the
    volume should be mounted inside the container.
12. Choose **Create** to create the task
    definition.

## Using the AWS CLI

To specify an S3 Files volume in a task definition using the AWS CLI, use the
`register-task-definition` command with the
`s3filesVolumeConfiguration` parameter in the volume
definition.

The following is an example task definition JSON snippet that defines an S3
Files volume and mounts it to a container:

```
{
  "family": "s3files-task-example",
  "taskRoleArn": "arn:aws:iam::`123456789012`:role/`ecsTaskRole`",
  "containerDefinitions": [
    {
      "name": "my-container",
      "image": "`my-image:latest`",
      "essential": true,
      "mountPoints": [
        {
          "containerPath": "/mnt/s3data",
          "sourceVolume": "my-s3files-volume"
        }
      ]
    }
  ],
  "volumes": [
    {
      "name": "my-s3files-volume",
      "s3filesVolumeConfiguration": {
        "fileSystemArn": "arn:aws:s3files:`us-east-1`:`123456789012`:file-system/`fs-0123456789abcdef0`",
        "rootDirectory": "/",
        "transitEncryptionPort": `2999`
      }
    }
  ]
}
```

Register the task definition:

```
`aws ecs register-task-definition --cli-input-json file://s3files-task-def.json`
```

To use an access point, include the `accessPointArn`
parameter:

```
{
  "name": "my-s3files-volume",
  "s3filesVolumeConfiguration": {
    "fileSystemArn": "arn:aws:s3files:`us-east-1`:`123456789012`:file-system/`fs-0123456789abcdef0`",
    "rootDirectory": "/",
    "transitEncryptionPort": `2999`,
    "accessPointArn": "arn:aws:s3files:`us-east-1`:`123456789012`:file-system/`fs-0123456789abcdef0`/access-point/`fsap-0123456789abcdef0`"
  }
}
```
