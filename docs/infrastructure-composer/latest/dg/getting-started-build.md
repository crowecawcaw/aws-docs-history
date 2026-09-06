

# Build your first application with Infrastructure Composer
<a name="getting-started-build"></a>

In this tutorial, you use AWS Infrastructure Composer to build a create, read, update, and delete (CRUD) serverless application that manages users in a database.

For this tutorial, we use Infrastructure Composer in the AWS Management Console. We recommend that you use Google Chrome or Microsoft Edge, and a full-screen browser window.

**Are you new to serverless?**  
We recommend a basic understanding of the following topics:  
[Event-driven architecture](what-is-concepts.md#what-is-concepts-terms-eda)
[Infrastructure as Code (IaC)](what-is-concepts.md#what-is-concepts-terms-iac)
[Serverless technologies](what-is-concepts.md#what-is-concepts-terms-serverless)
To learn more, see [Serverless concepts for AWS Infrastructure Composer](what-is-concepts.md).

**Topics**
+ [Resource properties reference](#getting-started-build-reference)
+ [Step 1: Create your project](#getting-started-build-start)
+ [Step 2: Add cards to the canvas](#getting-started-build-rest-cards)
+ [Step 3: Configure your API Gateway REST API](#getting-started-build-rest)
+ [Step 4: Configure your Lambda functions](#getting-started-build-functions)
+ [Step 5: Connect your cards](#getting-started-build-connect)
+ [Step 6: Organize the canvas](#getting-started-build-organize)
+ [Step 7: Add and connect a DynamoDB table](#getting-started-build-table)
+ [Step 8: Review your AWS CloudFormation template](#getting-started-build-template)
+ [Step 9: Integrate into your development workflows](#getting-started-build-integrate)
+ [Next steps](#getting-started-build-next)

## Resource properties reference
<a name="getting-started-build-reference"></a>

While building your application, use this table for reference to configure the properties of your Amazon API Gateway and AWS Lambda resources.


| Method | Path | Function name | 
| --- | --- | --- | 
| GET | /items | getItems | 
| GET | /items/{id} | getItem | 
| PUT | /items/{id} | updateItem | 
| POST | /item | addItem | 
| DELETE | /items/{id} | deleteItem | 

## Step 1: Create your project
<a name="getting-started-build-start"></a>

To get started with your CRUD serverless application, create a new project in Infrastructure Composer and activate **local sync**.

**To create a new blank project**

1. Sign in to the [Infrastructure Composer console](https://console.aws.amazon.com/composer/home).

1. On the **Home** page, choose **Create project**.

As shown in the following image, Infrastructure Composer opens the visual canvas and loads a starting (blank) application template.

![Infrastructure Composer with a blank visual canvas.](http://docs.aws.amazon.com/infrastructure-composer/latest/dg/images/aac_t2_01.png)


**To activate local sync**

1. From the Infrastructure Composer **menu**, select **Save** > **Activate local sync**.  
![An Infrastructure Composer menu with Activate local sync selected.](http://docs.aws.amazon.com/infrastructure-composer/latest/dg/images/aac_t2_09.png)

1. For **Project location**, press **Select folder** and choose a directory. This is where Infrastructure Composer will save and sync your template files and folders as you design. 

   The project location must not contain an existing application template.
**Note**  
**Local sync** requires a browser that supports the File System Access API. For more information, see [Data Infrastructure Composer gains access to](reference-fsa.md#reference-fsa-access).

1. When prompted to allow access, select **View files**.

1. Press **Activate** to turn on **local sync**. When prompted to save changes, select **Save changes**.

   When activated, the **Autosave** indicator will be displayed in the upper-left area of your canvas.

## Step 2: Add cards to the canvas
<a name="getting-started-build-rest-cards"></a>

Start to design your application architecture using enhanced component cards, beginning with an API Gateway REST API and five Lambda functions.

**To add API Gateway and Lambda cards to the canvas**

From the **Resources** palette, under the **Enhanced components** section, do the following:

1. Drag an **API Gateway** card onto the canvas.

1. Drag a **Lambda Function** card onto the canvas. Repeat until you've added five **Lambda Function** cards to the canvas.

![An Infrastructure Composer canvas view with one API Gateway and five Lambda Function cards.](http://docs.aws.amazon.com/infrastructure-composer/latest/dg/images/aac_t2_02.png)


## Step 3: Configure your API Gateway REST API
<a name="getting-started-build-rest"></a>

Next, add five routes within your API Gateway card.

**To add routes to the API Gateway card**

1. Open the **Resource properties** panel for the **API Gateway** card. To open the panel, double-click the card. Or, select the card, and then choose **Details**.

1. In the **Resource properties** panel, under **Routes**, do the following:
**Note**  
For each of the following routes, use the HTTP method and path values specified in the [resource properties reference table](#getting-started-build-reference).

   1. For **Method**, choose the specified HTTP method. For example, **GET**.

   1. For **Path**, enter the specified path. For example, **/items**.

   1. Choose **Add route**.

   1. Repeat the previous steps until you've added all five specified routes.

1. Choose **Save**.

![The Infrastructure Composer visual canvas with an API Gateway resource with five routes. The Resource properties panel shows selections for Method, Path, and Add route.](http://docs.aws.amazon.com/infrastructure-composer/latest/dg/images/aac_t2_03.png)


## Step 4: Configure your Lambda functions
<a name="getting-started-build-functions"></a>

Name each of the five Lambda functions as specified in the [resource properties reference table](#getting-started-build-reference).

**To name the Lambda functions**

1. Open the **Resource properties** panel of a **Lambda Function** card. To open the panel, double-click the card. Or, select the card, and then choose **Details**.

1. In the **Resource properties** panel, for **Logical ID**, enter a specified function name. For example, **getItems**.

1. Choose **Save**.

1. Repeat the previous steps until you've named all five functions.

![The Infrastructure Composer visual canvas with five named Lambda Function resource cards.](http://docs.aws.amazon.com/infrastructure-composer/latest/dg/images/aac_t2_04.png)


## Step 5: Connect your cards
<a name="getting-started-build-connect"></a>

Connect each route on your **API Gateway** card to its related **Lambda Function** card, as specified in the [resource properties reference table](#getting-started-build-reference).

**To connect your cards**

1. Click a right port on the **API Gateway** card and drag it to the left port of the specified **Lambda Function** card. For example, click the **GET /items** port and drag it to the left port of **getItems**.

1. Repeat the previous step until you've connected all five routes on the **API Gateway** card to corresponding **Lambda Function** cards.

![The Infrastructure Composer visual canvas with the REST API connected to five Lambda functions.](http://docs.aws.amazon.com/infrastructure-composer/latest/dg/images/aac_t2_05.png)


## Step 6: Organize the canvas
<a name="getting-started-build-organize"></a>

Organize the visual canvas by grouping together your Lambda functions and arranging all the cards.

**To group together your functions**

1. Press and hold **Shift**, then select each **Lambda Function** card on the canvas.

1. Choose **Group**.

**To name your group**

1. Double-click the top of the group, near the group name (**Group**).

   The **Group properties** panel opens.

1. On the **Group properties** panel, for **Group name**, enter **API**.

1. Choose **Save**.

**To arrange your cards**

On the canvas, above the main view area, choose **Arrange**.

Infrastructure Composer arranges and aligns all cards on the visual canvas, including your new group (**API**), as shown here:

![The Infrastructure Composer visual canvas arranged with all Lambda functions grouped together.](http://docs.aws.amazon.com/infrastructure-composer/latest/dg/images/aac_t2_06.png)


## Step 7: Add and connect a DynamoDB table
<a name="getting-started-build-table"></a>

Now, add a DynamoDB table to your application architecture and connect it to your Lambda functions.

**To add and connect a DynamoDB table**

1. From the resource palette (**Resources**), under the **Enhanced components** section, drag a **DynamoDB Table** card onto the canvas.

1. Click the right port on a **Lambda Function** card and drag it to the left port of the **DynamoDB Table** card.

1. Repeat the previous step until you've connected all five **Lambda Function** cards to the **DynamoDB Table** card.

1. (Optional) To reorganize and realign the cards on the canvas, choose **Arrange**.

![The Infrastructure Composer visual canvas with a DynamoDB table connected to the group API.](http://docs.aws.amazon.com/infrastructure-composer/latest/dg/images/aac_t2_07.png)


## Step 8: Review your AWS CloudFormation template
<a name="getting-started-build-template"></a>

Congratulations\! You've successfully designed a serverless application that's ready for deployment. Finally, choose **Template** to review the AWS CloudFormation template that Infrastructure Composer has automatically generated for you.

In the template, Infrastructure Composer has defined the following:
+ The `Transform` declaration, which specifies the template as an AWS Serverless Application Model (AWS SAM) template. For more information, see [AWS SAM template anatomy](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-template-anatomy.html) in the *AWS Serverless Application Model Developer Guide*.
+ An `AWS::Serverless::Api` resource, which specifies your API Gateway REST API with its five routes.
+ Five `AWS::Serverless::Function` resources, which specify your Lambda functions' configurations, including their environment variables and permissions policies.
+ An `AWS::DynamoDB::Table` resource, which specifies your DynamoDB table and its properties.
+ The `Metadata` section, which contains information about your resource group (**API**). For more information about this section, see [Metadata](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/metadata-section-structure.html) in the *AWS CloudFormation User Guide*.

![The Infrastructure Composer template view showing the application's template code.](http://docs.aws.amazon.com/infrastructure-composer/latest/dg/images/aac_t2_08.png)


## Step 9: Integrate into your development workflows
<a name="getting-started-build-integrate"></a>

Use the template file and project directories that Infrastructure Composer created for further testing and deployment.
+ With **local sync**, you can connect Infrastructure Composer to the IDE on your local machine to speed up development. To learn more, see [Connect the Infrastructure Composer console with your local IDE](other-services-ide.md).
+ With **local sync**, you can use the AWS Serverless Application Model Command Line Interface (AWS SAM CLI) on your local machine to test and deploy your application. To learn more, see [Deploy your Infrastructure Composer serverless application to the AWS Cloud](other-services-cfn.md).

## Next steps
<a name="getting-started-build-next"></a>

You're now ready to build your own applications with Infrastructure Composer. For in-depth details on using Infrastructure Composer, refer to [How to compose in AWS Infrastructure Composer](using-composer-basics.md). When you are ready to deploy your application, refer to [Deploy your Infrastructure Composer serverless application to the AWS Cloud](other-services-cfn.md).