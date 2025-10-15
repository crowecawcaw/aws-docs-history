# View a timeline of a CloudFormation stack deployment

The stack deployment timeline graph provides a visual representation of a stack deployment 
 timeline. This view shows the deployment statuses for the stack and each of its resources, and the times that 
 each status changed. Stack deployment statuses are represented by a corresponding color.

###### Topics

* [Understanding the stack deployment timeline graph](#understanding-stack-deployment-timeline-graph "#understanding-stack-deployment-timeline-graph")
* [Viewing the stack deployment timeline graph (console)](#viewing-stack-deployment-timeline-graph "#viewing-stack-deployment-timeline-graph")

## Understanding the stack deployment timeline graph


The following image shows the timeline graph for a stack deployment that failed due to an Amazon EC2 
 instance resource that failed to launch.



![A stack deployment timeline graph for a failed stack deployment.](../../../images/AWSCloudFormation/latest/UserGuide/images/deployment-timeline-graph.PNG)

The names of the stack resources are found on the left side of the graph, and the date and time relative to the 
 deployment times are found at the top of the graph.


Each resource starts with the **In progress** status. The status bar changes to **Complete** for each successful deployment. The 
 status bar changes to **Failed** when a resource fails to deploy. When a resource fails to deploy and the stack deployment also fails, the 
 resource responsible for the stack deployment failure receives the **Likely root failure** status.


After the stack deployment operation failed, the successfully deployed resource begin rolling back and change to the **Rollback in progress** status. 
 The statuses change to **Rollback complete** after the resource finish rolling back.


Choosing each resource provides more granular detail on the deployment timeline:



![A stack deployment timeline graph popover showing deployment details for the chosen failed resource.](../../../images/AWSCloudFormation/latest/UserGuide/images/deployment-timeline-graph-root-cause.PNG)

Choosing a resource shows the **Type**, deployment **Start time**, deployment 
 **End time**, and **Total duration** of the deployment. You will also find the **Start time**, 
 **End time**, and **Duration** of each deployment status in the drop-down menus below. If the resource failed 
 to deploy, a **Failure reason** will be provided.


For more information on stack statuses, see [Stack status
 codes](view-stack-events.md#cfn-console-view-stack-data-resources-status-codes "view-stack-events.md#cfn-console-view-stack-data-resources-status-codes").


## Viewing the stack deployment timeline graph (console)


To view a stack deployment timeline graph:


1. Open the AWS CloudFormation console at
 [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. On the navigation bar at the top of the screen, choose the AWS Region you
 created the stack in.
3. On the **Stacks** page of the CloudFormation console, choose the
 stack name. CloudFormation displays the stack details for the selected stack.
4. Choose the **Events** tab to view the stack events CloudFormation
 has generated for your stack.
5. Choose the **Timeline graph** button to view the timeline graph 
 for your stack.
