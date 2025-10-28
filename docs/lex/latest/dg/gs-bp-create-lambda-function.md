End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# Step 3: Create a

Lambda Function (Console)

Create a Lambda function (using the
**lex-order-flowers-python** blueprint) and
perform test invocation using sample event data in the AWS Lambda
console.

You return to the Amazon Lex console and add the Lambda function as
the code hook to fulfill the `OrderFlowers` intent in the
`OrderFlowersBot` that you created in the preceding
section.

###### To create the Lambda function (console)

1. Sign in to the AWS Management Console and open the AWS Lambda console at
   [https://console.aws.amazon.com/lambda/](https://console.aws.amazon.com/lambda/ "https://console.aws.amazon.com/lambda/").
2. Choose **Create function**.
3. On the **Create function** page, choose
   **Use a blueprint**. Type
   `lex-` in the filter text box and
   then press `Enter` to find the blueprint, choose
   the `lex-order-flowers-python` blueprint.

Lambda function blueprints are provided in both Node.js and
Python. For this exercise, use the Python-based
blueprint. 4. On the **Basic information** page, do the
following.

    * Type a Lambda function name
     (`OrderFlowersCodeHook`).
    * For the execution role, choose **Create a
     new role with basic Lambda
     permissions**.
    * Leave the other default values.

5. Choose **Create function**.
6. If you are using a locale other than English (US) (en-US),
   update the intent names as described in [Updating a Blueprint
   for a Specific Locale](lex-lambda-blueprints.md#blueprint-update-locale "lex-lambda-blueprints.md#blueprint-update-locale").
7. Test the Lambda function.
   1. Choose **Select a test event**,
      **Configure test
      events**.
   2. Choose **Amazon Lex Order
      Flowers** from the **Event
      template** list. This sample event
      matches the Amazon Lex request/response model (see
      [Using Lambda Functions](using-lambda.md "using-lambda.md")). Give the test
      event a name
      (`LexOrderFlowersTest`).
   3. Choose **Create**.
   4. Choose **Test** to test the code
      hook.
   5. Verify that the Lambda function ran successfully.
      The response in this case matches the Amazon Lex
      response model.

###### Next Step

[Step 4: Add the Lambda
Function as Code Hook (Console)](gs-bp-create-integrate.md "gs-bp-create-integrate.md")
