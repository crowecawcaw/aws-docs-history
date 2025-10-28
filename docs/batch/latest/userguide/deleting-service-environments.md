# Delete a service environment in

AWS Batch

You can delete a service environment when it's no longer needed for your SageMaker Training
jobs. Deleting a service environment removes the configuration and prevents
further job submissions. Before deleting a service
environment, ensure that no active SageMaker Training jobs depend on it and that no job
queues are associated with the service environment.

###### Important

Service environment deletion is irreversible. Once deleted, you cannot recover the
service environment or its configuration. If you need similar functionality in the
future, you must create a new service environment with the required settings. Consider
disabling the service environment instead of deletion if you may need to reactivate it
later.

###### Note

Deleting all service environments in your account does not automatically remove the
service-linked role created for AWS Batch and SageMaker AI integration. The service-linked role
remains available for future service environment creation. If you want to remove the
service-linked role, you must delete it separately using IAM after ensuring no service
environments exist in your account.

## Deletion

prerequisites

Before you can delete a service environment you must disassociate any service job
queue and then disable the service environment.

**Before deleting a service environment:**

- **Check active jobs** - Ensure no SageMaker Training
  jobs are currently running through the service environment.
- **Review job queues** - Identify job queues
  associated with the service environment and either associate the job queue with
  a different service environment or disable and delete the job queue.

**Job queue management:** Job queues that were associated
with a deleted service environment can still exist but cannot process service jobs. You
should either delete unused job queues or associate them with a different service
environment before deleting the original service environment.

Delete a service environment (AWS
Console)
Use the AWS Batch console to delete a service environment through the web
interface.

**To delete a service environment**

1. Open the AWS Batch console at [https://console.aws.amazon.com/batch/](https://console.aws.amazon.com/batch/ "https://console.aws.amazon.com/batch/").
2. In the navigation pane, choose **Environments**.
3. Choose the **Service environment** tab and then choose a
   service environment.
4. If the service environment is enabled, choose **Actions** and then **Disable**.
5. Once the service environment is disabled, choose **Actions** and then **Delete**.
6. In the confirmation dialog, choose **Confirm**.

The service environment shows a `DELETING` state while deletion occurs.
Once deletion completes, the service environment disappears from the Environments
list.

Delete a service environment (AWS
CLI)
Use the `delete-service-environment` command to remove a service
environment with the AWS CLI.

**To delete a service environment**

1. Check for associated job queues with the service environment:

```
aws batch describe-job-queues
```

If there are any job queues associated with the service environment
you can either [disassociate the job queue](../APIReference/API_UpdateJobQueue.md "../APIReference/API_UpdateJobQueue.md") from the
service environment and associate it with a different service
environment, or delete the job queue. 2. Disable the service environment:

```
aws batch update-service-environment \
    --service-environment my-sagemaker-service-env \
    --state DISABLED
```

3. Delete the service environment:

```
aws batch delete-service-environment \
    --service-environment my-sagemaker-service-env
```

4. Monitor the deletion process:

```
aws batch describe-service-environments \
    --service-environment my-sagemaker-service-env
```

The service environment transitions to `DELETING` state during the deletion
process. Once deletion completes, the service environment is no longer listed in
describe operations. Associated job queues remain but cannot process service jobs until
associated with a different service environment.
