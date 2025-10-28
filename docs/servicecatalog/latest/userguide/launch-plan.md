# Creating a launch plan

Before you provision a product, AWS Service Catalog enables you to create a launch plan.
The plan is a list of resource changes AWS Service Catalog will apply to the provisioned
product. You can view planned resource changes and execute them when the plan is complete. You
can delete, modify, or execute a launch plan.

Creating a plan to provision a product is optional. Once you create a plan, you won't be
able to execute any actions until the plan is complete.

###### To create a launch plan

1. In the left navigation menu, choose **Product**.
2. In **Products**, choose a product and then **Launch product**.
3. In **Provisioned product name**, enter or generate a name.
4. In **Product versions**, choose a version of the product.
5. Choose or enter information in the required fields.

Optionally, you can create and manage tags to track resources, and send notifications
to an Amazon SNS topic:

    * In **Manage tags**, enter values in the **Key** and **Value** fields to
     create custom tags. Then choose **Add new item**. To
     remove tags, choose **Remove**.
    * In **Enable event notifications**, choose the
     **Enable** box under **Event
     notifications**. To create an Amazon SNS topic, choose one of the
     following:




    	+ **Create a topic**. Enter a name for the
    	 topic.
    	+ **Choose a topic from your account**. In
    	 **Topic name**, choose a name.
    	+ **Choose a topic from another account**. In
    	 **Topic**
    	**ARN**, enter the ARN for the topic.

6. Choose **Create plan**.

###### Note

You can choose to cancel and not create a plan. If you proceed, you see a list of
changes AWS Service Catalog will apply to the provisioned product. You’ll be able to
review the changes before you execute them. To create the plan, confirm your choice and
choose **Create plan** again. 7. After the plan is complete, you see **Planned resource
changes**. It contains the list of changes to apply to the provisioned product.
From here you can delete, modify, or execute the plan.

    * When you delete the plan, a deletion box appears. Enter
     `delete` and choose **Delete**.
    * When you modify the plan, the **Modify plan** page
     appears. You can change the product version and any of the required or optional
     parameters. Then choose **Update**. You can see your
     updated changes in **Planned resource changes**.
    * When you execute the plan, AWS Service Catalog executes the provisioned product
     with the planned resource changes.

###### Note

If your plan fails to create, you can delete or modify the plan and create it again. When you
delete a plan, it deletes any provisioned product that has yet to be fully provisioned.
This deletion does not terminate any previously provisioned products.
