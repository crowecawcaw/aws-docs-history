# Create a service environment in

AWS Batch

Before you can run SageMaker Training jobs in AWS Batch, you need to create a service
environment. You can create a service environment that contains the configuration parameters
required for AWS Batch to integrate with SageMaker AI services and submit SageMaker Training jobs on your
behalf.

## Prerequisites

Before creating a service environment, ensure you have:

- **IAM permissions** – Permissions to create and manage service environments. For more information, see
  [AWS Batch IAM policies, roles, and permissions](IAM_policies.md "IAM_policies.md").

Create a service environment (AWS Console)
Use the AWS Batch console to create a service environment through the web
interface.

**To create a service environment**

1. Open the AWS Batch console at [https://console.aws.amazon.com/batch/](https://console.aws.amazon.com/batch/ "https://console.aws.amazon.com/batch/").
2. In the navigation pane, choose **Environments**.
3. Choose **Create environment**, select
   **Service environment**.
4. For **Service environment configuration**
   choose SageMaker AI.
5. For **Name**, enter a unique name for
   your service environment. Valid characters are a-z, A-Z, 0-9, hyphens
   (-), and underscores (\_).
6. For **Max number of instances** enter the
   maximum number of concurrent training instances
7. (Optional) Add tags by choosing **Add
   tag** and entering key-value pairs.
8. Choose **Next**.
9. Review the details of the new service environment and choose **Create service environment**.

Create a service environment (AWS CLI)
Use the `create-service-environment` command to create a service
environment with the AWS CLI.

**To create a service environment**

1. Create a service environment with the basic required
   parameters:

```
aws batch create-service-environment \
    --service-environment-name my-sagemaker-service-env \
    --service-environment-type SAGEMAKER_TRAINING \
    --capacity-limits capacityUnit=NUM_INSTANCES,maxCapacity=10
```

2. (Optional) Create a service environment with tags:

```
aws batch create-service-environment \
    --service-environment-name my-sagemaker-service-env \
    --service-environment-type SAGEMAKER_TRAINING \
    --capacity-limits capacityUnit=NUM_INSTANCES,maxCapacity=10 \
    --tags team=data-science,project=ml-training
```

3. Verify the service environment was created successfully:

```
aws batch describe-service-environments \
    --service-environment my-sagemaker-service-env
```

The service environment appears in the Environments list with a
`CREATING` state. When creation completes successfully, the state
changes to `VALID` and the service environment is ready to have a
service job queue added to it so the service environment can start processing
jobs.
