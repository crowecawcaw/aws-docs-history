

# Viewing Amazon ECS service deployments
<a name="view-service-deployment"></a>

You can see the most recent 90-day history for deployments created on or after October 25, 2024. The service deployments can be in any of the following states:
+ In-progress 
+ Pending
+ Completed

 You can use this information to determine if you need to update how the service is being deployed, or the service revision. For information about the included properties, see [Properties included in an Amazon ECS service deployment](service-deployment-property.md).

Before you begin, configure the required permissions for viewing service deployments. For more information, see [Permissions required for viewing Amazon ECS service deployments](service-deployment-permissions.md).

------
#### [ Amazon ECS Console ]

1. Open the console at [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2).

1. On the **Clusters** page, choose the cluster.

1. On the cluster details page, in the **Services** section, choose the service.

   The service details page displays.

1. On the service details page, choose **Deployments**.

1. Choose the service deployment to view.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/view-service-deployment.html)

   The service deployment details page appears.

1. (Optional) Compare service revisions to view the differences.

   Under **Service revisions**, choose **Compare revisions**, and then select 2 revisions to compare.

   The service revisions are displayed side-by-side with the differences highlighted.

------
#### [ AWS CLI ]

1. Run `list-service-deployments` to retrieve the service deployment ARN. 

   Replace the variables with your values.

   ```
   aws ecs list-service-deployments --cluster {{cluster-name}} --service {{service-name}}
   ```

   Note the serviceDeploymentArn for the deployment you want to view.

   ```
   {
       "serviceDeployments": [
           {
               "serviceDeploymentArn": "arn:aws:ecs:us-west-2:123456789012:service-deployment/example/sd-example/NCWGC2ZR-taawPAYrIaU5",
               "serviceArn": "arn:aws:ecs:us-west-2:123456789012:service/example/sd-example",
               "clusterArn": "arn:aws:ecs:us-west-2:123456789012:cluster/example",
               "targetServiceRevisionArn": "arn:aws:ecs:us-west-2:123456789012:service-revision/example/sd-example/4980306466373577095",
               "status": "SUCCESSFUL"
           }
       ]
   }
   ```

1. Run `describe-service-deployments`. Use the `serviceDeploymentArn` that was returned from `list-service-deployments`.

   Replace the variables with your values.

   ```
   aws ecs describe-service-deployments --service-deployment-arns arn:aws:ecs:{{region}}:{{123456789012}}:service-deployment/{{cluster-name}}/{{service-name}}/{{NCWGC2ZR-taawPAYrIaU5}}
   ```

------

## Next steps
<a name="view-service-deployment-next-step"></a>

You can view the details for service revisions in the deployment. For more information, see [Viewing Amazon ECS service revision details](view-service-revision.md)