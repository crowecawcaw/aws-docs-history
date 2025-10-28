End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# Step 2: Create a Lambda

Function

In this section, you create a Lambda function using a blueprint
(lex-make-appointment-python) that is provided in the Lambda console. You also test
the Lambda function by invoking it using sample Amazon Lex event data that is provided
by the console.

1. Sign in to the AWS Management Console and open the AWS Lambda console at
   [https://console.aws.amazon.com/lambda/](https://console.aws.amazon.com/lambda/ "https://console.aws.amazon.com/lambda/").
2. Choose **Create a Lambda function**.
3. For **Select blueprint**, type `lex`
   to find the blueprint, and then choose the
   **lex-make-appointment-python** blueprint.
4. Configure the Lambda function as follows.
   - Type the Lambda function name
     (`MakeAppointmentCodeHook`).
   - For the role, choose **Create a new role from
     template(s)**, and then type a role name.
   - Leave other default values.

5. Choose **Create Function**.
6. If you are using a locale other than English (US) (en-US), update the
   intent names as described in [Updating a Blueprint
   for a Specific Locale](lex-lambda-blueprints.md#blueprint-update-locale "lex-lambda-blueprints.md#blueprint-update-locale").
7. Test the Lambda function.
   1. Choose **Actions**, and then
      choose**Configure test event**.
   2. From the **Sample event template** list, choose
      **Lex-Make Appointment (preview)**. This sample
      event uses the Amazon Lex request/response model, with values set to
      match a request from your Amazon Lex bot. For information about the Amazon Lex
      request/response model, see [Using Lambda Functions](using-lambda.md "using-lambda.md").
   3. Choose **Save and test**.
   4. Verify that the Lambda function ran successfully. The response in
      this case matches the Amazon Lex response model.

###### Next Step

[Step 3: Update the Intent: Configure
a Code Hook](ex1-sch-appt-create-integrate.md "ex1-sch-appt-create-integrate.md")
