

# Updating an Amazon ECS service to use a capacity provider
<a name="update-service-managed-instances"></a>

If you have an existing service that uses the Amazon EC2 or Fargate launchtype and you want to use Amazon ECS Managed Instances, you need to update the service to use your Amazon ECS Managed Instances capacity provider.

## Prerequisites
<a name="update-service-managed-instances-prerequisites"></a>

Create a capacity provider for your Amazon ECS Managed Instances. For more information, see [Creating a capacity provider for Amazon ECS Managed Instances](create-capacity-provider-managed-instances.md).

## Procedure
<a name="update-service-managed-instances-procedure"></a>

------
#### [ Console ]

1. Open the console at [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2).

1. On the **Clusters** page, choose the cluster.

1. On the cluster details page, in the **Services** section, select the check box next to the service, and then choose **Update**.

1. Select **Force new deployment**.

1. Under **Compute configuration**, choose the Capacity provider strategy. Then, choose one of the following:
   + When your Amazon ECS Managed Instances capacity provider is the default capacity provider, choose **Use cluster default**.
   + When your Amazon ECS Managed Instances capacity provider isn't the default capacity provider, choose **Use custom (Advanced)**. Choose your Amazon ECS Managed Instances capacity provider, and then for **Weight** choose 1.

1. Choose **Update**.

------
#### [ AWS CLI ]
+ Run `update-service`. For information about running the command, see [update-service](https://docs.aws.amazon.com/cli/latest/reference/ecs/update-service.html) in the AWS Command Line Interface Reference. 

  Replace the {{user-input}} with your values.

  ```
  aws ecs update-service \
      --cluster {{my-cluster}} \
      --service {{my-service}} \
      --capacity-provider-strategy capacityProvider={{my-managed-instance-capacity-provider}},weight=1 \
      --force-new-deployment
  ```

------