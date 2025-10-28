# Starting the AWS AppConfig

agent for Amazon ECS integration

The AWS AppConfig Agent sidecar container is automatically available in your Amazon ECS
environment. To use it, you must start it, as described in the following procedure.

###### To start Amazon ECS (console)

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. In the navigation pane, choose **Task definitions**.
3. Choose the task definition for your application, and then select the latest
   revision.
4. Choose **Create new revision**, **Create new
   revision**.
5. Choose **Add more containers**.
6. For **Name**, enter a unique name for the AWS AppConfig Agent
   container.
7. For **Image URI**, enter:
   `public.ecr.aws/aws-appconfig/aws-appconfig-agent:2.x`
8. For **Essential container**, choose
   **Yes**.
9. In the **Port mappings** section, choose **Add port
   mapping**.
10. For **Container port**, enter `2772`.

###### Note

AWS AppConfig Agent runs on port 2772, by default. You can specify a different
port. 11. Choose **Create**. Amazon ECS creates a new container revision and
displays the details. 12. In the navigation pane, choose **Clusters**, and then choose your
application cluster in the list. 13. On the **Services** tab, select the service for your
application. 14. Choose **Update**. 15. Under **Deployment configuration**, for
**Revision**, choose the latest revision. 16. Choose **Update**. Amazon ECS deploys the latest task
definition. 17. After the deployment finishes, you can verify that AWS AppConfig Agent is running on the
**Configuration and tasks** tab. On the **Tasks**
tab, choose the running task. 18. In the **Containers** section, verify that the AWS AppConfig Agent
container is listed. 19. To verify that AWS AppConfig Agent started, choose the **Logs** tab.
Locate a statement like the following for the AWS AppConfig Agent container:
`[appconfig agent] 1970/01/01 00:00:00 INFO serving on
 localhost:2772`

###### Note

Note the following information.

- AWS AppConfig Agent is a long-running process. As a best practice for Amazon ECS containers,
  configure health checks for your containers, specifically setting the container
  dependency to the HEALTHY condition. For more information, see [ContainerDependency](../../../AmazonECS/latest/APIReference/API_ContainerDependency.md "../../../AmazonECS/latest/APIReference/API_ContainerDependency.md") in the _Amazon Elastic Container Service API Reference_.
- You can adjust the default behavior of AWS AppConfig Agent by entering or changing
  environment variables. For information about the available environment variables,
  see [(Optional) Using
  environment variables to configure AWS AppConfig Agent for Amazon ECS and Amazon EKS](appconfig-integration-containers-agent-configuring.md "appconfig-integration-containers-agent-configuring.md"). For
  information about how to change environment variables in Amazon ECS, see [Passing environment variables to a container](../../../AmazonECS/latest/developerguide/taskdef-envfiles.md "../../../AmazonECS/latest/developerguide/taskdef-envfiles.md") in the _Amazon Elastic Container Service Developer Guide_.
