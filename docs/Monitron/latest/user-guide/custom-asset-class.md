

Amazon Monitron is no longer open to new customers. Existing customers can continue to use the service as normal. For capabilities similar to Amazon Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron).

# Creating asset classes
<a name="custom-asset-class"></a>

Amazon Monitron offers four [default machine classes based on ISO 20816 Standards](https://docs.aws.amazon.com/Monitron/latest/user-guide/assets-chapter.html). When you add an asset position, you can choose any of these four default classes as the machine class to use for detecting anomalies with your assets. Amazon Monitron then uses the assigned asset class to generate warnings and alarms on asset condition.

If your asset types don't align with the default machine classes offered by Amazon Monitron, you can create custom machine classes for your assets. Once created, these custom classes are available to be assigned to all asset positions in a project. 

**Important**  
Custom classes can only be created using the Amazon Monitron web app. Only the Amazon Monitron project admin can create, update, and delete custom asset classes.

**Topics**
+ [Creating a custom class](#create-custom-asset-class)
+ [Updating a custom class](#update-custom-asset-class)
+ [Deleting a custom class](#delete-custom-asset-class)

## Creating a custom class
<a name="create-custom-asset-class"></a>

**To create a custom class**

1. Open the Amazon Monitron console at [https://console.aws.amazon.com/monitron](https://console.aws.amazon.com/monitron/). 

1. Choose **Create project**.

1. If you're creating a project for the first time, follow the steps outlined in [Creating a project](https://docs.aws.amazon.com/Monitron/latest/user-guide/mp-creating-project.html).

   If you're choosing an existing project, from the left navigation menu, select **Projects**, and then select the project you want to create custom classes for.

1. From the project details page, choose **Open in Amazon Monitron web app**.  
![Amazon Monitron project setup steps: create project, add admin users, email instructions, manage directory.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/asset-class-1.png)

1. In the Amazon Monitron web app page, from the left navigation pane, choose **Settings**.  
![Settings page with language, measurements, and classes configuration options.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/asset-class-2.png)

1. Then, select from **Classes**, select **Create class**.  
![Form to create a custom class with fields for name, description, and measurement thresholds.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/asset-class-3.png)

1. On the **Create custom class** page, do the following:
   + In **Class details**, for **Class name** – A name for your custom class.
   + **Description** – A description for your custom machine class.
   + In **Measurement details**, for **Measurement thresholds** – Custom measurement thresholds for your assets.

1. Choose **Save**.

## Updating a custom class
<a name="update-custom-asset-class"></a>

**To update a custom class**

1. Open the Amazon Monitron console at [https://console.aws.amazon.com/monitron](https://console.aws.amazon.com/monitron/). 

1. Choose **Create project**.

1. If you're creating a project for the first time, follow the steps outlined in [Creating a project](https://docs.aws.amazon.com/Monitron/latest/user-guide/mp-creating-project.html).

   If you're choosing an existing project, from the left navigation menu, select **Projects**, and then select the project you want to create custom classes for.

1. From the project details page, choose **Open in Amazon Monitron web app**.  
![Amazon Monitron project setup steps: create project, add admin users, email instructions, manage directory.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/asset-class-1.png)

1. In the Amazon Monitron web app page, from the left navigation pane, choose **Settings**.  
![Settings page with language, measurements, and classes configuration options.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/asset-class-2.png)

1. Then, from **Classes**, select the class you would like to update, and select **Edit**.  
![Edit Custom name form with class details and measurement thresholds for warnings and alarms.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/asset-class-4.png)

1. On the **Edit class** page, do the following:
   + In **Class details**, for **Class name** – A name for your custom class.
   + **Description** – A description for your custom machine class.
   + In **Measurement details**, for **Measurement thresholds** – Custom measurement thresholds for your assets.

1. Choose **Save**.
**Note**  
The edited machine class will go into effect during the next Amazon Monitron measurement interval.

## Deleting a custom class
<a name="delete-custom-asset-class"></a>

**To delete a custom class**

1. Open the Amazon Monitron console at [https://console.aws.amazon.com/monitron](https://console.aws.amazon.com/monitron/). 

1. Choose **Create project**.

1. If you're creating a project for the first time, follow the steps outlined in [Creating a project](https://docs.aws.amazon.com/Monitron/latest/user-guide/mp-creating-project.html).

   If you're choosing an existing project, from the left navigation menu, select **Projects**, and then select the project you want to create custom classes for.

1. From the project details page, choose **Open in Amazon Monitron web app**.  
![Amazon Monitron project setup steps: create project, add admin users, email instructions, manage directory.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/asset-class-1.png)

1. In the Amazon Monitron web app page, from the left navigation pane, choose **Settings**.  
![Settings page with language, measurements, and classes configuration options.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/asset-class-2.png)

1. Then, from **Classes**, select the machine class you would like to delete, and select **Delete**.  
![Fan custom threshold details showing warning and alarm measurements, description, and position list.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/asset-class-5.png)
**Important**  
You can't delete custom machine classes that are currently in use by one or more positions. You will be prompted with a list of positions currently using the machine class and you will need to update these positions to a different machine class before deleting the machine class attached to these positions.

1. To confirm deletion, type **delete**, and then select **Save**.