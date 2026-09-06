

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Creating a provisioned fleet
<a name="projects-create-compute-resource"></a>

Use the following instructions to create a provisioned fleet.

**Note**  
Provisioned fleets will be deactivated after 2 weeks of inactivity. If used again, they will be re-activated automatically, but this re-activation may cause a latency to occur.

**To create a provisioned fleet**

1. In the navigation pane, choose **CI/CD**, and then choose **Compute**.

1. Choose **Create provisioned fleet**.

1. In the **Provisioned fleet name** text field, enter a name for your fleet.

1. From the **Operating system** drop-down menu, choose the operating system.

1. From the **Machine type** drop-down menu, choose the machine type for your machine.

1. In the **Capacity** text field, enter the maximum number of machines in the fleet.

1. From the **Scaling mode** drop-down menu, choose the desired overflow behavior. For more information about these fields, see [Provisioned fleet properties](workflows-working-compute.md#compute.provisioned-fleets).

1. Choose **Create**.

After creating the provisioned fleet, you are ready to assign it to an action. For more information, see [Assigning a fleet or compute to an action](workflows-assign-compute-resource.md).