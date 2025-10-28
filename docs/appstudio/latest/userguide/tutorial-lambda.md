# Invoking Lambda functions in an App Studio app

This tutorial shows you how to connect App Studio to Lambda and invoke Lambda functions from your apps.

## Prerequisites

This guide assumes you have completed the following prerequisites:

1. Created an App Studio app. If you do not have one, you can create an empty app to use in the tutorial. For more information, see [Creating an application](applications-create.md "applications-create.md").

###### Note

While you don't need a Lambda function to follow this tutorial and learn how to configure it, it may be helpful to have one for ensuring
you have correctly configured the app. This tutorial does not contain information about creating Lambda functions. for more information, see the
[AWS Lambda Developer Guide](../../../lambda/latest/dg.md "../../../lambda/latest/dg.md").

## Create a Lambda connector

To use Lambda functions in your App Studio app, you must use a connector to connect App Studio to Lambda to provide access to your functions. You
must be an Administrator to create connectors in App Studio. For more information about creating Lambda connectors, including the steps to create one, see
[Connect to AWS Lambda](connectors-lambda.md "connectors-lambda.md").

## Create and configure an automation

Automations are used to define the logic of your application and are made up of actions. To invoke a Lambda function in your app, you first add and configure
an _Invoke Lambda_ action to an automation. Use the following steps to create an automation and add the _Invoke Lambda_ action
to it.

1. While editing your app, choose the **Automations** tab.
2. Choose **+ Add automation**.
3. In the right-hand **Actions** menu, choose **Invoke Lambda** to add the step to your automation.
4. Choose the new Lambda step in the canvas to view and configure its properties.
5. In the right-hand **Properties** menu, configure the step by performing the following steps:
   1. In **Connector**, select the connector that was created to connect App Studio to your Lambda functions.
   2. In **Function name**, enter the name of your Lambda function.
   3. In **Function event**, enter the event to be passed to the Lambda function. Some common use case examples are provided in the following list:
      - Passing an automation parameter's value, such as a file name or other string:
        ``varName`: params.`paramName``
      - Passing the result of a previous action: ``varName`: results.`actionName1`.data[0].`fieldName``
      - If you add an _Invoke Lambda_ action inside a _Loop_ action, you can send fields from each iterated item similar to parameters: `varName: `currentItem`.`fieldName``

   4. The **Mocked output** field can be used for providing mock output to test the app while previewing, where connectors are not active.

## Configure a UI element to run the automation

Now that you have an automation that is configured with an action to invoke your Lambda function, you can configure a UI element to run the
automation. In this tutorial, you will create a button that runs the automation when clicked.

###### Tip

You can also run automations from other automations with the _Invoke automation_ action.

###### To run your automation from a button

1. While editing your app, choose the **Pages** tab.
2. In the right-hand menu, choose the **Button** component to add a button to the page.
3. Choose the new button to configure it.
4. In the right-hand **Properties** menu, in **Triggers**, choose **+ Add** and choose
   **Invoke automation**.
5. Choose the new automation invoke trigger to configure it.
6. In **Invoke automation**, select the automation that invokes your Lambda function and configure any parameters that you
   want to send to the automation.

Now, any user that chooses this button in your app will cause the configured automation to run.

## Next steps: Preview and publish the application for testing

Your application is now ready for testing. When previewing your app in the Development environment, connectors are not active, so you cannot
test the automation while previewing as it uses a connector to connect to AWS Lambda. To test your app's functionality that depends on connectors, you must
publish the app to the Testing environment. For more information about previewing and publishing applications, see
[Previewing, publishing, and sharing applications](applications-preview-publish-share.md "applications-preview-publish-share.md").
