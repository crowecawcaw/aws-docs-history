

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


<table>
<thead>
  <tr><th>To view service revisions for this deployment type</th><th>Do this</th><th></th></tr>
</thead>
<tbody>
  <tr><td>Ongoing deployments</td><td>Under <b>Ongoing deployments</b>, do the following:<ul><li> To view the source service revision, under <b>Service revisions</b>, choose the service revision ID for the Source <b>Revision type</b>.  </li><li> To view the target service revision, under <b>Service revisions</b>, choose the service revision ID for the Target <b>Revision type</b>.  </li></ul></td><td></td></tr>
  <tr><td>Last deployment</td><td>Under <b>Last deployment</b>, choose the <b>Target service revision</b>. </td><td></td></tr>
  <tr><td>Completed deployments</td><td>Under <b>Service deployments</b>, do the following:<ul><li> Under <b>Target service revision</b>, choose the ID.  </li></ul></td><td></td></tr>
</tbody>
</table>


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