AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Creating a custom migration journey

In this tutorial, you create a custom journey for the following migration scenario:
[Rehost on-premises workloads in the AWS Cloud: migration checklist](../../../prescriptive-guidance/latest/patterns/rehost-on-premises-workloads-in-the-aws-cloud-migration-checklist.md#rehost-on-premises-workloads-in-the-aws-cloud-migration-checklist-epics "../../../prescriptive-guidance/latest/patterns/rehost-on-premises-workloads-in-the-aws-cloud-migration-checklist.md#rehost-on-premises-workloads-in-the-aws-cloud-migration-checklist-epics").

###### Create the migration journey

1. Open the Migration Hub Journeys console. For information about how to access the console, see [Accessing AWS Migration Hub Journeys](setup.md "setup.md").
2. In the navigation pane, choose **Migration journeys**.
3. Choose **Create migration journey**.
4. In the **Journey creation method** section, choose
   **Create custom journey**.
5. In the **Journey details** section, under **Journey
   name** enter
   `custom-migration-journey`.
6. Under **Migration space**, choose **Create migration
   space**.
7. In the **Space name** field, enter
   `tutorial-two-space`.
8. In the **Create phases** section, enter `Planning
phase` in the **Phase name** field.
9. Choose **Add phase**, and then enter
   `Pre-discovery` in the **Phase name**
   field.
10. Repeat the previous step to add four more phases with the following names:
    `Discovery`, `Build`,
    `Test`, and `Cutover`.
11. Choose **Create migration journey**.

###### Add a module to each of the phases of the journey

In this procedure, you add a main module to contain the tasks that you will later
add to each phase.

1. In the navigation pane, choose **Migration journeys**.
2. Choose the name of the journey
   **custom-migration-journey**.
3. Choose the journey's **Modules** tab.
4. In the **Modules in the Pre-discovery phase** section, choose
   **Add module**.
5. In the **Title** field, enter `Main
module`.
6. For the **Phase** field, use the dropdown list to choose
   **Pre-discovery**.
7. Choose **Add module**.
8. Repeat the steps in this procedure to add a module to each of the phases of
   the journey.

###### Add tasks to the modules of the journey

1. In the journey's **Modules** tab, find the **Modules
   in the Pre-discovery phase** section, and choose **Main
   module**.
2. Choose **Create task**.
3. In the **Title** field, enter `Groom the
pre-discovery backlog.`.
4. For the **Module** field, choose **Pre-discovery main
   module** from the dropdown list.
5. For the task description, enter `Conduct the pre-discovery backlog
grooming working session with department leads and application
owners.`
6. Choose **Create task**.
7. Repeat the steps in this procedure to add to the journey all of the tasks that
   are listed under [Epics](../../../prescriptive-guidance/latest/patterns/rehost-on-premises-workloads-in-the-aws-cloud-migration-checklist.md#rehost-on-premises-workloads-in-the-aws-cloud-migration-checklist-epics "../../../prescriptive-guidance/latest/patterns/rehost-on-premises-workloads-in-the-aws-cloud-migration-checklist.md#rehost-on-premises-workloads-in-the-aws-cloud-migration-checklist-epics").
