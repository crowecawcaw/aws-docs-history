# Creating, updating, and deleting recovery groups in ARC

A recovery group represents your application in Amazon Application Recovery Controller (ARC). It typically consists of two or
more _cells_ that are replicas of each other in terms of resources
and functionality, so that you can fail over from one to the other. Each cell includes
the Amazon Resource Names (ARNs) for the active resources for one AWS Region or Availability Zone.
The resources might be an Elastic Load Balancing load balancer, an Auto Scaling group, or other resources. A
corresponding cell representing another zone or Region has standby resources of the same type that
are in your active cell – a load balancer, Auto Scaling group, and so on.

A cell represents replicas of your application. Readiness checks in ARC help
you determine if your application is ready to fail over from one replica to another. However, you should make decisions
about whether to fail away from or to a replica based on your monitoring and health check systems, and consider
readiness checks as a complementary service to those systems.

Readiness checks audit resources to determine their readiness based on a set of pre-defined rules for that type of resource. After you create your
recovery group with the replicas, you add ARC readiness checks for the resources in your application, so ARC can help make sure that the
replicas have the same setup and configuration over time.

###### Topics

- [Creating recovery groups](#recovery-readiness.recovery-groups.create "#recovery-readiness.recovery-groups.create")
- [Updating and deleting recovery groups and cells](#recovery-readiness.recovery-groups.edit-delete "#recovery-readiness.recovery-groups.edit-delete")

## Creating recovery groups

The steps in this section explain how to create a recovery group on the ARC console. To learn about using recovery readiness API operations with
Amazon Application Recovery Controller (ARC), see [Readiness check API operations](actions.md "actions.md").

## To create a recovery group

1. Open the ARC console at [https://console.aws.amazon.com/route53recovery/home#/dashboard](https://console.aws.amazon.com/route53recovery/home#/dashboard "https://console.aws.amazon.com/route53recovery/home#/dashboard").
2. Choose **Readiness check**.
3. On the **Recovery readiness** page, choose **Create**, and then choose a
   **Recovery group**.
4. Enter a name for your recovery group, and then choose **Next**.
5. Choose **Create cells**, and then choose **Add cell**.
6. Enter a name for the cell. For example, if you have an application replica in US West (N. California), you could add a cell
   named `MyApp-us-west-1`.
7. Choose **Add cell**, and add a name for a second cell. For example, if you have a replica in US East (Ohio), you could
   add a cell named `MyApp-us-east-2`.
8. If you want to add nested cells (replicas in Availability Zones
   within Regions), choose **Action**, choose **Add
   nested cell**, and then enter a name.
9. When you've added all of the cells and nested cells for your application replicas, choose **Next**.
10. Review your recovery group, and then choose **Create recovery group**.

## Updating and deleting recovery groups and cells

The steps in this section explain how to update and delete a recovery group, and delete a cell on the ARC console. To learn about using recovery readiness API operations with
Amazon Application Recovery Controller (ARC), see [Readiness check API operations](actions.md "actions.md").

## To update or delete a recovery group, or delete a cell

1. Open the ARC console at [https://console.aws.amazon.com/route53recovery/home#/dashboard](https://console.aws.amazon.com/route53recovery/home#/dashboard "https://console.aws.amazon.com/route53recovery/home#/dashboard").
2. Choose **Readiness check**.
3. On the **Recovery readiness** page, choose a recovery group.
4. To work with a recovery group, choose **Action**, and then choose **Edit recovery group** or
   **Delete recovery group**.
5. When you edit a recovery group, you can add or remove cells or nested cells.
   - To add a cell, choose **Add cell**.
   - To remove a cell, under the **Action** label next to the cell, choose
     **Delete cell**.
