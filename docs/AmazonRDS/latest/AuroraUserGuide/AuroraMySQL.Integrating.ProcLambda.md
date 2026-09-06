

# Invoking a Lambda function with an Aurora MySQL stored procedure (deprecated)
<a name="AuroraMySQL.Integrating.ProcLambda"></a>

You can invoke an AWS Lambda function from an Aurora MySQL DB cluster by calling the `mysql.lambda_async` procedure. This approach can be useful when you want to integrate your database running on Aurora MySQL with other AWS services. For example, you might want to send a notification using Amazon Simple Notification Service (Amazon SNS) whenever a row is inserted into a specific table in your database. 

**Contents**
+ [Aurora MySQL version considerations](#AuroraMySQL.Integrating.ProcLambda.caveats)
+ [Working with the mysql.lambda\_async procedure to invoke a Lambda function (deprecated)](#AuroraMySQL.Integrating.Lambda.mysql_lambda_async)
  + [Syntax](#AuroraMySQL.Integrating.Lambda.mysql_lambda_async.Syntax)
  + [Parameters](#AuroraMySQL.Integrating.Lambda.mysql_lambda_async.Parameters)
  + [Examples](#AuroraMySQL.Integrating.Lambda.mysql_lambda_async.Examples)

## Aurora MySQL version considerations
<a name="AuroraMySQL.Integrating.ProcLambda.caveats"></a>

Starting in Aurora MySQL version 2, you can use the native function method instead of these stored procedures to invoke a Lambda function. For more information about the native functions, see [Working with native functions to invoke a Lambda function](AuroraMySQL.Integrating.NativeLambda.md#AuroraMySQL.Integrating.NativeLambda.lambda_functions).

In Aurora MySQL version 2, the stored procedure `mysql.lambda_async` is no longer supported. We strongly recommend that you work with native Lambda functions instead.

In Aurora MySQL version 3, the stored procedure isn't available.

## Working with the mysql.lambda\_async procedure to invoke a Lambda function (deprecated)
<a name="AuroraMySQL.Integrating.Lambda.mysql_lambda_async"></a>

The `mysql.lambda_async` procedure is a built-in stored procedure that invokes a Lambda function asynchronously. To use this procedure, your database user must have `EXECUTE` privilege on the `mysql.lambda_async` stored procedure.

### Syntax
<a name="AuroraMySQL.Integrating.Lambda.mysql_lambda_async.Syntax"></a>

The `mysql.lambda_async` procedure has the following syntax.

```
CALL mysql.lambda_async (
  {{lambda_function_ARN}},
  {{lambda_function_input}}
)
```

### Parameters
<a name="AuroraMySQL.Integrating.Lambda.mysql_lambda_async.Parameters"></a>

The `mysql.lambda_async` procedure has the following parameters.

* lambda\_function\_ARN *  
The Amazon Resource Name (ARN) of the Lambda function to invoke.

* lambda\_function\_input *  
The input string, in JSON format, for the invoked Lambda function.

### Examples
<a name="AuroraMySQL.Integrating.Lambda.mysql_lambda_async.Examples"></a>

As a best practice, we recommend that you wrap calls to the `mysql.lambda_async` procedure in a stored procedure that can be called from different sources such as triggers or client code. This approach can help to avoid impedance mismatch issues and make it easier to invoke Lambda functions. 

**Note**  
Be careful when invoking an AWS Lambda function from triggers on tables that experience high write traffic. `INSERT`, `UPDATE`, and `DELETE` triggers are activated per row. A write-heavy workload on a table with `INSERT`, `UPDATE`, or `DELETE` triggers results in a large number of calls to your AWS Lambda function.   
Although calls to the `mysql.lambda_async` procedure are asynchronous, triggers are synchronous. A statement that results in a large number of trigger activations doesn't wait for the call to the AWS Lambda function to complete, but it does wait for the triggers to complete before returning control to the client.

**Example: Invoke an AWS Lambda function to send email**  
The following example creates a stored procedure that you can call in your database code to send an email using a Lambda function.  
**AWS Lambda Function**  

```
import boto3

ses = boto3.client('ses')

def SES_send_email(event, context):

    return ses.send_email(
        Source=event['email_from'],
        Destination={
            'ToAddresses': [
            event['email_to'],
            ]
        },

        Message={
            'Subject': {
            'Data': event['email_subject']
            },
            'Body': {
                'Text': {
                    'Data': event['email_body']
                }
            }
        }
    )
```
**Stored Procedure**  

```
DROP PROCEDURE IF EXISTS SES_send_email;
DELIMITER ;;
  CREATE PROCEDURE SES_send_email(IN email_from VARCHAR(255),
                                  IN email_to VARCHAR(255),
                                  IN subject VARCHAR(255),
                                  IN body TEXT) LANGUAGE SQL
  BEGIN
    CALL mysql.lambda_async(
         'arn:aws:lambda:us-west-2:123456789012:function:SES_send_email',
         CONCAT('{"email_to" : "', email_to,
             '", "email_from" : "', email_from,
             '", "email_subject" : "', subject,
             '", "email_body" : "', body, '"}')
     );
  END
  ;;
DELIMITER ;
```
**Call the Stored Procedure to Invoke the AWS Lambda Function**  

```
mysql> call SES_send_email('example_from@amazon.com', 'example_to@amazon.com', 'Email subject', 'Email content');
```

**Example: Invoke an AWS Lambda function to publish an event from a trigger**  
The following example creates a stored procedure that publishes an event by using Amazon SNS. The code calls the procedure from a trigger when a row is added to a table.  
**AWS Lambda Function**  

```
import boto3

sns = boto3.client('sns')

def SNS_publish_message(event, context):

    return sns.publish(
        TopicArn='arn:aws:sns:us-west-2:123456789012:Sample_Topic',
        Message=event['message'],
        Subject=event['subject'],
        MessageStructure='string'
    )
```
**Stored Procedure**  

```
DROP PROCEDURE IF EXISTS SNS_Publish_Message;
DELIMITER ;;
CREATE PROCEDURE SNS_Publish_Message (IN subject VARCHAR(255),
                                      IN message TEXT) LANGUAGE SQL
BEGIN
  CALL mysql.lambda_async('arn:aws:lambda:us-west-2:123456789012:function:SNS_publish_message',
     CONCAT('{ "subject" : "', subject,
            '", "message" : "', message, '" }')
     );
END
;;
DELIMITER ;
```
**Table**  

```
CREATE TABLE 'Customer_Feedback' (
  'id' int(11) NOT NULL AUTO_INCREMENT,
  'customer_name' varchar(255) NOT NULL,
  'customer_feedback' varchar(1024) NOT NULL,
  PRIMARY KEY ('id')
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```
**Trigger**  

```
DELIMITER ;;
CREATE TRIGGER TR_Customer_Feedback_AI
  AFTER INSERT ON Customer_Feedback
  FOR EACH ROW
BEGIN
  SELECT CONCAT('New customer feedback from ', NEW.customer_name), NEW.customer_feedback INTO @subject, @feedback;
  CALL SNS_Publish_Message(@subject, @feedback);
END
;;
DELIMITER ;
```
**Insert a Row into the Table to Trigger the Notification**  

```
mysql> insert into Customer_Feedback (customer_name, customer_feedback) VALUES ('Sample Customer', 'Good job guys!');
```