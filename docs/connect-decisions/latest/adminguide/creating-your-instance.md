

# Creating Your Instance
<a name="creating-your-instance"></a>

You create an instance using one of two methods, Standard configuration or Advanced configuration. Standard configuration uses an automated process that creates your instance quickly using preset parameters. Advanced configuration allows you to customize your instance by setting your own parameters.

## Using standard configuration
<a name="creating-your-instance-standard-configuration"></a>

Standard configuration creates your Amazon Connect Decisions instance using default security and encryption settings. Instances operate in AWS geographic regions. For more information about regions, see [Regions and endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html) in the *IAM User Guide* and [Regional endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#regional-endpoints) in the *AWS General Reference*.

To create an Amazon Connect Decisions instance using a standard configuration of preset parameters, follow these steps.

1. Select **Create**.  
![](http://docs.aws.amazon.com/connect-decisions/latest/adminguide/images/creating-your-instance-standard-create.png)

1. Check your email for the following:
   + An email from the IdC team.
   + An email from Identity Management team.  
![](http://docs.aws.amazon.com/connect-decisions/latest/adminguide/images/creating-your-instance-email-invite.png)

1. Once you receive the invite email, log on to Amazon Connect Decisions. See [Log on to Amazon Connect Decisions web application](https://docs.aws.amazon.com/aws-supply-chain/latest/adminguide/viewing-homepage.html) .

## Using advanced configuration
<a name="creating-your-instance-advanced-configuration"></a>

Advanced configuration allows you to customize your instance by setting your own parameters. To create an Amazon Connect Decisions instance using an advanced configuration of preset parameters, follow these steps.

1. Select **Create in advanced setup**.

1. The **Instance properties** page will appear.  
![](http://docs.aws.amazon.com/connect-decisions/latest/adminguide/images/creating-your-instance-advanced-properties.png)

1. Enter the following on the **Instance properties** page:
   + **Name** – Enter an instance name.
   + **Description** – Enter a description of your Amazon Connect Decisions instance (e.g., production instance, test instance, etc.).
   + **Instance tags** – You can add tags to your instance that can be used for identification. For example, you can add a tag to define the type of instance you are creating (e.g., production, test, UAT, etc.).

1. Select **Create instance**.

## Deleting an instance
<a name="creating-your-instance-deleting"></a>

To delete an instance, follow these steps.

**Note**  
When you delete an instance, information from the Amazon S3 bucket is not automatically deleted.

1. Open the Amazon Connect Decisions console at [https://console.aws.amazon.com/scn/home](https://console.aws.amazon.com/scn/home).

1. On the Amazon Connect Decisions console dashboard, from the dropdown, select the instance that you want to delete.  
![](http://docs.aws.amazon.com/connect-decisions/latest/adminguide/images/creating-your-instance-delete-select.png)

1. Choose **Delete**.

1. On the **Delete Amazon Connect Decisions Instance** page, under **Confirmation**, type `delete` to confirm that you want to delete the instance.

1. Choose **Delete**. The instance deletion starts and once the instance is deleted, you will see a confirmation message.