

# Viewing Amazon ECS service revision details
<a name="view-service-revision"></a>

You can view information about the following service revision types that were created on or after October 25, 2024:
+ Source -The currently deployed workload configuration
+ Target - The workload configuration being deployed

------
#### [ Amazon ECS Console ]

1. Open the console at [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2).

1. On the **Clusters** page, choose the cluster.

1. On the cluster details page, in the **Services** section, choose the service.

   The service details page displays.

1. On the service details page, choose **Deployments**.

1. Choose the service revision to view.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/view-service-revision.html)

------
#### [ AWS CLI ]

1. Run `describe-service-deployments` to retrieve the service revision ARN. 

   Replace the variables with your values.

   ```
   aws ecs describe-service-deployments --service-deployment-arns arn:aws:ecs:{{region}}{{:account-id}}:service/{{cluster-name}}/{{service-name}}/{{NCWGC2ZR-taawPAYrIaU5}}
   ```

   Note the `arn` for the `sourceServiceRevisions` or the `targetServiceRevisions`.

   ```
   {
       "serviceDeployments": [
           {
               "serviceDeploymentArn": "arn:aws:ecs:us-west-2:123456789012:service-deployment/example/sd-example/NCWGC2ZR-taawPAYrIaU5",
               "serviceArn": "arn:aws:ecs:us-west-2:123456789012:service/example/sd-example",
               "clusterArn": "arn:aws:ecs:us-west-2:123456789012:cluster/example",
               "updatedAt": "2024-09-10T16:49:35.572000+00:00",
               "sourceServiceRevision": {
                   "arn": "arn:aws:ecs:us-west-2:123456789012:service-revision/example/sd-example/4980306466373578954",
                   "requestedTaskCount": 0,
                   "runningTaskCount": 0,
                   "pendingTaskCount": 0
               },
               "targetServiceRevision": {
                   "arn": "arn:aws:ecs:us-west-2:123456789012:service-revision/example/sd-example/4980306466373577095",
                   "requestedTaskCount": 0,
                   "runningTaskCount": 0,
                   "pendingTaskCount": 0
               },
               "status": "IN_PROGRESS",
               "deploymentConfiguration": {
                   "deploymentCircuitBreaker": {
                       "enable": false,
                       "rollback": false
                   },
                   "maximumPercent": 200,
                   "minimumHealthyPercent": 100
               }
           }
       ],
       "failures": []
   }
   ```

1. Run `describe-service-revisions`. Use the `arn` that was returned from `describe-service-deployments`.

   Replace the variables with your values.

   ```
   aws ecs describe-service-revisions --service-revision-arns arn:aws:ecs:{{region}}:{{123456789012}}:service-revision/{{cluster-name}}/{{service-name}}/{{4980306466373577095}}
   ```

------