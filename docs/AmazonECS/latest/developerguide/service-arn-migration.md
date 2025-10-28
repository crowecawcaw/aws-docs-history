# Migrate an Amazon ECS short service ARN to a long ARN

Amazon ECS assigns a unique Amazon Resource Name (ARN) to each service. Services that were created before 2021
have a short ARN format:

`arn:aws:ecs:`region`:`aws_account_id`:service/`service-name``

Amazon ECS changed the ARN format to include the cluster name. This is a long ARN
format:

`arn:aws:ecs:`region`:`aws_account_id`:service/`cluster-name`/`service-name``

Your service must have the long ARN format in order to tag your service.

You can migrate a service with a short ARN format to the long ARN format without having
to recreate the service. You can use the API, CLI, or the console. You can't undo the
migration operation.

The migration process is seamless and ensures zero downtime for your service. During migration:

- **Service availability**: Your service continues to run normally with no interruption to traffic or functionality.
- **Running tasks**: Existing tasks continue to run without disruption. New tasks launched after migration will use the long ARN format if the `taskLongArnFormat` account setting is enabled.
- **Container instances**: Container instances are not affected by the service ARN migration and continue to operate normally.
- **Service configuration**: All service settings, including task definition, networking, and load balancer configurations, remain unchanged.
  If you want to use AWS CloudFormation to tag a service with short ARN format, you must migrate the
  service using the API, CLI, or console. After the migration completes you can use AWS CloudFormation to
  tag the service.

If you want to use Terraform to tag a service with short ARN format, you must migrate
the service using the API, CLI, or console. After the migration completes you can use
Terraform to tag the service.

After the migration is complete, the service has the following changes:

- The long ARN format

`arn:aws:ecs:`region`:`aws_account_id`:service/`cluster-name`/`service-name``

- When you migrate using the console, Amazon ECS adds a tag to the service with the key
  set to "ecs:serviceArnMigratedAt" and the value set to the migration timestamp (UTC
  format).

This tag counts toward your tag quota.

- When the `PhysicalResourceId` in a AWS CloudFormation stack represents a service
  ARN, the value does not change and will continue to be the short service ARN.

## Prerequisites

Perform the following operations before you migrate the service ARN.

1. To see if you have a short service ARN, view the service details in the Amazon ECS console (you
   see a warning when the service has the short ARN format), or the
   `serviceARN` return parameter from
   `describe-services`. When the ARN does not include the cluster
   name, you have a short ARN. The following is the format of a short
   ARN:

`arn:aws:ecs:`region`:`aws_account_id`:service/`service-name`` 2. Note the created at date. 3. If you have IAM policies that use the short ARN format, update it to the long ARN
format.

Replace each `user input placeholder` with your own
information.

`arn:aws:ecs:`region`:`aws_account_id`:service/`cluster-name`/`service-name``

For more information, see [Editing IAM
policies](../../../IAM/latest/UserGuide/access_policies_manage-edit.md "../../../IAM/latest/UserGuide/access_policies_manage-edit.md") in the _AWS Identity and Access Management User
Guide_. 4. If you have tools that use the short ARN format, update it to the long ARN format.

Replace each `user input placeholder` with your own
information.

`arn:aws:ecs:`region`:`aws_account_id`:service/`cluster-name`/`service-name``5. Enable the service long ARN format. Run
`put-account-setting`with the
`serviceLongArnFormat`option set to
`enabled`. For more information, see, [put-account-setting](../../../cli/latest/reference/ecs/put-account-setting.md "../../../cli/latest/reference/ecs/put-account-setting.md") in the _Amazon Elastic Container Service API Reference_.

Run the command as the root user when your service has an unknown
`createdAt` date.

```
aws ecs put-account-setting --name serviceLongArnFormat --value enabled
```

Example output

```
{
    "setting": {
        "name": "serviceLongArnFormat",
        "value": "enabled",
        "principalArn": "arn:aws:iam::`123456789012:role/your-role`",
        "type": user
    }
}
```

6. Enable the task long ARN format. This account setting controls the ARN format for new tasks that are launched after the service migration is complete. Run `put-account-setting`
   with the `taskLongArnFormat` option set to `enabled`. For
   more information, see, [put-account-setting](../../../cli/latest/reference/ecs/put-account-setting.md "../../../cli/latest/reference/ecs/put-account-setting.md") in the _Amazon Elastic Container Service API Reference_.

Run the command as the root user when your service has an unknown
`createdAt` date.

```
aws ecs put-account-setting --name taskLongArnFormat --value enabled
```

Example output

```
{
    "setting": {
        "name": "taskLongArnFormat",
        "value": "enabled",
        "principalArn": "arn:aws:iam::`123456789012:role/your-role`",
        "type": user
    }
}
```

###### Note

The `taskLongArnFormat` setting does not directly migrate existing tasks. It only affects the ARN format of new tasks that are created after the setting is enabled. Existing running tasks retain their current ARN format until they are replaced through normal service operations (such as deployments or scaling activities).

## Procedure

Use the following to migrate your service ARN.

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. On the **Clusters** page, choose the cluster.
3. In the **Services** section, choose a service that
   has a warning in the ARN column.

The service details page appears. 4. Choose **Migrate to long ARN**.

The Migrate service dialog box appears. 5. Choose **Migrate**.
After you complete the prerequisites, you can tag your service. Run the
following command:

Amazon ECS considers passing the long ARN format in a `tag-resource`
API request for a service with a short ARN as a signal to migrate the service
to use the long ARN format.

```
aws ecs tag-resource \
    --resource-arn arn:aws:ecs:`region`:`aws_account_id`:service/`cluster-name`/`service-name`
    --tags key=`key1`,value=`value1`
```

The following example tags MyService with a tag that has a key set to
"TestService" and a value set to "WebServers:

```
aws ecs tag-resource \
    --resource-arn arn:aws:ecs:us-east-1:123456789012:service/MyCluster/MyService
    --tags key=TestService1,value=WebServers
```

After you complete the prerequisites, you can tag your service. Create an
`aws_ecs_service` resource and set the `tags`
reference. For more information, see [Resource: aws_ecs_service](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ecs_service "https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ecs_service") in the Terraform documentation.

```
resource "aws_ecs_service" "MyService" {
  name    = "example"
  cluster = aws_ecs_cluster.MyService.id

 tags = {
 "Name"  =  "MyService"
 "Environment"  =  "Production"
 "Department"  =  "QualityAssurance"
  }
}

```

### Next steps

You can add tags to the service. For more information, see [Adding tags to Amazon ECS resources](tag-resources-console.md "tag-resources-console.md").

If you want Amazon ECS to propagate the tags from the task definition or the service to the
task, run `update-service` with the `propagateTags` parameter.
For more information, see [update-service](../../../cli/latest/reference/ecs/update-service.md "../../../cli/latest/reference/ecs/update-service.md") in the _AWS Command Line Interface
Reference_.

## Troubleshooting

Some users might encounter the following error when they migrate from the short ARN
format to the long ARN format.

`There was an error while migrating the ARN of service
 `service-name`. The specified account does not have
 serviceLongArnFormat or taskLongArnFormat account settings enabled. Add account
 settings in order to enable tagging.`

If you have already enabled the `serviceLongArnFormat` account setting but
still encounter this error, it might be because the account settings for the long ARN
format hasn't been enabled for the specific IAM principal that originally created the
service.

1. Identify the principal that created the service.
   1. In the console, the information is available in the **Created by** field in
      the **Configuration and networking** tab on the Service
      details page in the Amazon ECS console.
   2. For the AWS CLI, run the following command:

   Replace the `user-input` with your
   values.

   ```
   aws ecs describe-services --cluster `cluster-name` --services `service-name` --query 'services[0].{createdBy: createdBy}'
   ```

2. Enable the required account settings for that specific principal. You can do
   this in one of the following ways:
   1. Assume the IAM user or role for that principal. Then run
      `put-account-setting`.
   2. Use the root user to run the command while specifying the creating
      principal with the `principal-arn`.

   Example.

   Replace the `principal-arn` with the value
   from Step 1.

   ```
   aws ecs put-account-setting --name serviceLongArnFormat --value enabled --principal-arn `arn:aws:iam::123456789012:role/jdoe`
   ```

Both methods enable the required `serviceLongArnFormat` account setting
on the principal that created the service, which allows the ARN migration to proceed.
