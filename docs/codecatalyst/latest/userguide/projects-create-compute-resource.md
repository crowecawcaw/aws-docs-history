Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Creating a provisioned fleet

Use the following instructions to create a provisioned fleet.

###### Note

Provisioned fleets will be deactivated after 2 weeks of inactivity. If used again,
they will be re-activated automatically, but this re-activation may cause a latency
to occur.

###### To create a provisioned fleet

1. In the navigation pane, choose **CI/CD**, and then choose **Compute**.
2. Choose **Create provisioned fleet**.
3. In the **Provisioned fleet name** text field, enter a name
   for your fleet.
4. From the **Operating system** drop-down menu, choose the
   operating system.
5. From the **Machine type** drop-down menu, choose the machine
   type for your machine.
6. In the **Capacity** text field, enter the maximum number of
   machines in the fleet.
7. From the **Scaling mode** drop-down menu, choose the desired
   overflow behavior. For more information about these fields, see [Provisioned fleet properties](workflows-working-compute.md#compute.provisioned-fleets "workflows-working-compute.md#compute.provisioned-fleets").
8. Choose **Create**.
   After creating the provisioned fleet, you are ready to assign it to an action. For
   more information, see [Assigning a fleet or compute to an
   action](workflows-assign-compute-resource.md "workflows-assign-compute-resource.md").
