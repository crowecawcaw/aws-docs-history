End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# Step 3: Create a Lambda

function

In this section you create a Lambda function using a blueprint
(**lex-book-trip-python**) provided in the AWS Lambda console. You
also test the Lambda function by invoking it using sample event data provided by the
console.

This Lambda function is written in Python.

1. Sign in to the AWS Management Console and open the AWS Lambda console at
   [https://console.aws.amazon.com/lambda/](https://console.aws.amazon.com/lambda/ "https://console.aws.amazon.com/lambda/").
2. Choose **Create function**.
3. Choose **Use a blueprint**. Type `lex`
   to find the blueprint, choose the `lex-book-trip-python`
   blueprint.
4. Choose **Configure** the Lambda function as follows.
   - Type a Lambda function name (`BookTripCodeHook`).
   - For the role, choose **Create a new role from
     template(s)** and then type a role name.
   - Leave the other default values.

5. Choose **Create function**.
6. If you are using a locale other than English (US) (en-US), update the intent
   names as described in [Updating a Blueprint
   for a Specific Locale](lex-lambda-blueprints.md#blueprint-update-locale "lex-lambda-blueprints.md#blueprint-update-locale").
7. Test the Lambda function. You invoke the Lambda function twice, using sample
   data for both booking a car and booking a hotel.
   1. Choose **Configure test event** from the
      **Select a test event** drop down.
   2. Choose **Amazon Lex Book Hotel** from the
      **Sample event template** list.

   This sample event matches the Amazon Lex request/response model. For
   more information, see [Using Lambda Functions](using-lambda.md "using-lambda.md"). 3. Choose **Save and test**. 4. Verify that the Lambda function ran successfully. The response in this
   case matches the Amazon Lex response model. 5. Repeat the step. This time you choose the **Amazon Lex Book
   Car** from the **Sample event template**
   list. The Lambda function processes the car reservation.

###### Next Step

[Step 4: Add the Lambda Function as a Code
Hook](ex-book-trip-create-integrate.md "ex-book-trip-create-integrate.md")
