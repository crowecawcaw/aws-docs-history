

# Learn how to use AWS Cloud Map service discovery with custom attributes
<a name="tutorial-microservices"></a>

The following tutorial demonstrates how you can use AWS Cloud Map service discovery with custom attributes that are discoverable using the AWS Cloud Map API. The tutorial walks you through creating and running client applications using AWS CloudShell. The applications use two Lambda functions to write data to a DynamoDB table and then read from the table. The Lambda functions and DynamoDB table are registered in AWS Cloud Map as service instances. The code in the client applications and Lambda functions uses AWS Cloud Map custom attributes to discover the resources needed to perform the job.

For an AWS CLI-based version of this tutorial, see [Learn how to use AWS Cloud Map service discovery with custom attributes using the AWS CLI](tutorial-microservices-cli.md).

**Important**  
You will create AWS resources during the workshop which will incur a cost in your AWS account. It is recommended to clean-up the resources as soon as you finish the workshop to minimize the cost.

## Prerequisites
<a name="tutorial-customattributes-prerequisites"></a>

Before you begin, complete the steps in [Set up to use AWS Cloud Map](setting-up-cloud-map.md).

## Step 1: Create an AWS Cloud Map namespace
<a name="tutorial-customattributes-step1"></a>

In this step, you create an AWS Cloud Map namespace. A namespace is a construct used to group services for an application. When you create the namespace, you specify how the resources will be discoverable. The resources created in the namespace created in this step will be discoverable with AWS Cloud Map API calls using custom attributes.

1. Sign in to the AWS Management Console and open the AWS Cloud Map console at [https://console.aws.amazon.com/cloudmap/](https://console.aws.amazon.com/cloudmap/).

1. Choose **Create namespace**.

1. For **Namespace name**, specify `cloudmap-tutorial`.

1. (Optional) For **Namespace description**, specify a description for what you intend to use the namespace for.

1. For **Instance discovery**, select **API calls**.

1. Leave the rest of the default values and choose **Create namespace**.

## Step 2: Create a DynamoDB table
<a name="tutorial-customattributes-step2"></a>

In this step, you create a DynamoDB table. The table is used to store and retrieve data for the sample application that you will create in the following steps.

For information about how to create an DynamoDB, see [Step 1: Create a table in DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/getting-started-step-1.html) in the *DynamoDB Developer Guide* and use the following table to determine what options to specify.


| Option | Value | 
| --- | --- | 
| Table name | cloudmap | 
| Partition key | id | 

Keep the default values for the rest of the settings and create the table.

## Step 3: Create an AWS Cloud Map data service and register DynamoDB table as an instance
<a name="tutorial-customattributes-step3"></a>

In this step, you create a AWS Cloud Map service and then register the DynamoDB table created in the last step as a service instance.

1. Open the AWS Cloud Map console at [https://console.aws.amazon.com/cloudmap/](https://console.aws.amazon.com/cloudmap/)

1. From the list of namespaces, select the `cloudmap-tutorial` namespace and choose **View details**.

1. In the **Services** section, choose **Create service** and do the following.

   1. For **Service name**, enter `data-service`.

   1. Leave the rest of the default values and choose **Create service**.

1. In the **Services** section, select the `data-service` service and choose **View details**.

1. In the **Service instances** section, choose **Register service instance**.

1. On the **Register service instance** page, do the following.

   1. For **Instance type**, select **Identifying information for another resource**.

   1. For **Service instance id**, specify `data-instance`.

   1. In the **Custom attributes** section, specify the following key-value pair: **key** = `tablename`, **value** = `cloudmap`.

## Step 4: Create an AWS Lambda execution role
<a name="tutorial-customattributes-step4"></a>

In this step, you create an IAM role that the AWS Lambda function in the next step uses. You can name the IAM role `cloudmap-tutorial-role` and omit the permissions boundary because the role is only used for this tutorial, and you can delete it afterwards.

**To create the service role for Lambda (IAM console)**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane of the IAM console, choose **Roles**, and then choose **Create role**.

1. For **Trusted entity type**, choose **AWS service**.

1. For **Service or use case**, choose **Lambda**, and then choose the **Lambda** use case.

1. Choose **Next**.

1. Search for, and select the box next to, the `PowerUserAccess` policy and then choose **Next**.

1. Choose **Next**.

1. For **Role name**, specify `cloudmap-tutorial-role`.

1. Review the role, and then choose **Create role**.

## Step 5: Create the Lambda function to write data
<a name="tutorial-customattributes-step5"></a>

In this step, you create a Lambda function authored from scratch that writes data to the DynamoDB table by using the AWS Cloud Map API to query the AWS Cloud Map service you created.

For information about creating a Lambda function, see [Create a Lambda function with the console](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html#getting-started-create-function) in the *AWS Lambda Developer Guide* and use the following table to determine what options to specify or choose.


| Option | Value | 
| --- | --- | 
| Function name | writefunction | 
| Runtime | Python 3.12 | 
| Architecture | x86\_64 | 
| Permissions | Use an existing role | 
| Existing role | cloudmap-tutorial-role | 

After you create the function, update the example code to reflect the following Python code, and then deploy the function. Note that you're specifying the `datatable` custom attribute you associated with the AWS Cloud Map service instance you created for the DynamoDB table. The function generates a key that is a random number between 1 and 100 and associates it with a value that is passed to the function when it is called.

```
import json
import boto3
import random

def lambda_handler(event, context):
       
    serviceclient = boto3.client('servicediscovery')
    
    response = serviceclient.discover_instances(
        NamespaceName='cloudmap-tutorial',
        ServiceName='data-service')
       
    tablename = response["Instances"][0]["Attributes"]["tablename"]
       
    dynamodbclient = boto3.resource('dynamodb')
       
    table = dynamodbclient.Table(tablename)
       
    response = table.put_item(
        Item={ 'id': str(random.randint(1,100)), 'todo': event })
       
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
```

After deploying the function, to avoid timeout errors, update the function timeout to 5 seconds. For more information, see [Configure Lambda function timeout](https://docs.aws.amazon.com/lambda/latest/dg/configuration-timeout.html) in the *AWS Lambda Developer Guide*.

## Step 6: Create an AWS Cloud Map app service and register the Lambda write function as an instance
<a name="tutorial-customattributes-step6"></a>

In this step, you create an AWS Cloud Map service and then register the Lambda write function as a service instance.

1. Open the AWS Cloud Map console at [https://console.aws.amazon.com/cloudmap/](https://console.aws.amazon.com/cloudmap/)

1. In the left navigation, choose **Namespaces**.

1. From the list of namespaces, select the `cloudmap-tutorial` namespace and choose **View details**.

1. In the **Services** section, choose **Create service** and do the following.

   1. For **Service name**, enter `app-service`.

   1. Leave the rest of the default values and choose **Create service**.

1. In the **Services** section, select the `app-service` service and choose **View details**.

1. In the **Service instances** section, choose **Register service instance**.

1. On the **Register service instance** page, do the following.

   1. For **Instance type**, select **Identifying information for another resource**.

   1. For **Service instance id**, specify `write-instance`.

   1. In the **Custom attributes** section, specify the following key-value pairs.
      + **key** = `action`, **value** = `write`
      + **key** = `functionname`, **value** = `writefunction`

## Step 7: Create the Lambda function to read data
<a name="tutorial-customattributes-step7"></a>

In this step, you create a Lambda function authored from scratch that writes data to the DynamoDB table you created.

For information about creating a Lambda function, see [Create a Lambda function with the console](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html#getting-started-create-function) in the *AWS Lambda Developer Guide* and use the following table to determine what options to specify or choose.


| Option | Value | 
| --- | --- | 
| Function name | readfunction | 
| Runtime | Python 3.12 | 
| Architecture | x86\_64 | 
| Permissions | Use an existing role | 
| Existing role | cloudmap-tutorial-role | 

After you create the function, update the example code to reflect the following Python code, and then deploy the function. The function scans the table amd returns all items.

```
import json
import boto3

def lambda_handler(event, context):
    serviceclient = boto3.client('servicediscovery')

    response = serviceclient.discover_instances(NamespaceName='cloudmap-tutorial', ServiceName='data-service')
       
    tablename = response["Instances"][0]["Attributes"]["tablename"]
       
    dynamodbclient = boto3.resource('dynamodb')
       
    table = dynamodbclient.Table(tablename)
       
    response = table.scan(Select='ALL_ATTRIBUTES')

    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
```

After deploying the function, to avoid timeout errors, update the function timeout to 5 seconds. For more information, see [Configure Lambda function timeout](https://docs.aws.amazon.com/lambda/latest/dg/configuration-timeout.html) in the *AWS Lambda Developer Guide*.

## Step 8: Register the Lambda read function as an AWS Cloud Map service instance
<a name="tutorial-customattributes-step8"></a>

In this step, you register the Lambda read function as a service instance in the `app-service` service you previously created.

1. Open the AWS Cloud Map console at [https://console.aws.amazon.com/cloudmap/](https://console.aws.amazon.com/cloudmap/)

1. In the left navigation, choose **Namespaces**.

1. From the list of namespaces, select the `cloudmap-tutorial` namespace and choose **View details**.

1. In the **Services** section, select the `app-service` service and choose **View details**.

1. In the **Service instances** section, choose **Register service instance**.

1. On the **Register service instance** page, do the following.

   1. For **Instance type**, select **Identifying information for another resource**.

   1. For **Service instance id**, specify `read-instance`.

   1. In the **Custom attributes** section, specify the following key-value pairs.
      + **key** = `action`, **value** = `read`
      + **key** = `functionname`, **value** = `readfunction`

## Step 9: Create and run read and write clients on AWS CloudShell
<a name="tutorial-customattributes-step10"></a>

You can create and run client applications in AWS CloudShell that use code to discover the services you configured in AWS Cloud Map and make calls to these services.

1. Open the AWS CloudShell console at [https://console.aws.amazon.com/cloudshell/](https://console.aws.amazon.com/cloudshell/)

1. Use the following command to create a file called `writefunction.py`.

   ```
   vim writeclient.py
   ```

1. In the `writeclient.py` file, enter insert mode by pressing the `i` button. Then, copy and paste the following code. This code discovers the Lambda function to write data by searching for the custom attribute `name=writeservice` in the `app-service` service. The name of the Lambda function responsible for writing data to the DynamoDB table is returned. Then the Lambda function is invoked, passing a sample payload that is written to the table as a value.

   ```
   import boto3
   
   serviceclient = boto3.client('servicediscovery')
   
   response = serviceclient.discover_instances(NamespaceName='cloudmap-tutorial', ServiceName='app-service', QueryParameters={ 'action': 'write' })
   
   functionname = response["Instances"][0]["Attributes"]["functionname"]
   
   lambdaclient = boto3.client('lambda')
   
   resp = lambdaclient.invoke(FunctionName=functionname, Payload='"This is a test data"')
   
   print(resp["Payload"].read())
   ```

1. Press the escape key, type `:wq`, and press the enter key to save the file and exit.

1. Use the following command to run the Python code.

   ```
   python3 writeclient.py
   ```

   The output should be a `200` response, similar to the following.

   ```
   b'{"statusCode": 200, "body": "{\\"ResponseMetadata\\": {\\"RequestId\\": \\"Q0M038IT0BPBVBJK8OCKK6I6M7VV4KQNSO5AEMVJF66Q9ASUAAJG\\", \\"HTTPStatusCode\\": 200, \\"HTTPHeaders\\": {\\"server\\": \\"Server\\", \\"date\\": \\"Wed, 06 Mar 2024 22:46:09 GMT\\", \\"content-type\\": \\"application/x-amz-json-1.0\\", \\"content-length\\": \\"2\\", \\"connection\\": \\"keep-alive\\", \\"x-amzn-requestid\\": \\"Q0M038IT0BPBVBJK8OCKK6I6M7VV4KQNSO5AEMVJF66Q9ASUAAJG\\", \\"x-amz-crc32\\": \\"2745614147\\"}, \\"RetryAttempts\\": 0}}"}'
   ```

1. To verify the write was successful in the previous step, create a read client.

   1. Use the following command to create a file called `readfunction.py`.

      ```
      vim readclient.py
      ```

   1. In the `readclient.py` file, press the `i` button to enter insert mode. Then, copy and paste the following code. This code scans the table and will return the value that you wrote to the table in the previous step.

      ```
      import boto3
      
      serviceclient = boto3.client('servicediscovery')
      
      response = serviceclient.discover_instances(NamespaceName='cloudmap-tutorial', ServiceName='app-service', QueryParameters={ 'action': 'read' })
      
      functionname = response["Instances"][0]["Attributes"]["functionname"]
      
      lambdaclient = boto3.client('lambda')
      
      resp = lambdaclient.invoke(FunctionName=functionname, InvocationType='RequestResponse')
      
      print(resp["Payload"].read())
      ```

   1. Press the escape key, type `:wq`, and press the enter key to save the file and exit.

   1. Use the following command to run the Python code.

      ```
      python3 readclient.py
      ```

      The output should look similar to the following, listing the value written to the table by running `writefunction.py` and the random key generated in the Lambda write function.

      ```
        b'{"statusCode": 200, "body": "{\\"Items\\": [{\\"id\\": \\"45\\", \\"todo\\": \\"This is a test data\\"}], \\"Count\\": 1, \\"ScannedCount\\": 1, \\"ResponseMetadata\\": {\\"RequestId\\": \\"9JF8J6SFQCKR6IDT5JG5NOM3CNVV4KQNSO5AEMVJF66Q9ASUAAJG\\", \\"HTTPStatusCode\\": 200, \\"HTTPHeaders\\": {\\"server\\": \\"Server\\", \\"date\\": \\"Thu, 25 Jul 2024 20:43:33 GMT\\", \\"content-type\\": \\"application/x-amz-json-1.0\\", \\"content-length\\": \\"91\\", \\"connection\\": \\"keep-alive\\", \\"x-amzn-requestid\\": \\"9JF8J6SFQCKR6IDT5JG5NOM3CNVV4KQNSO5AEMVJF66Q9ASUAAJG\\", \\"x-amz-crc32\\": \\"1163081893\\"}, \\"RetryAttempts\\": 0}}"}'
      ```

## Step 10: Clean up the resources
<a name="tutorial-customattributes-step11"></a>

After you have completed the tutorial, delete the resources to avoid incurring additional charges. AWS Cloud Map requires that you clean them up in reverse order, the service instances first, then the services, and finally the namespace. The following steps walk you through cleaning up the AWS Cloud Map resources used in the tutorial.

**To delete the AWS Cloud Map resources**

1. Sign in to the AWS Management Console and open the AWS Cloud Map console at [https://console.aws.amazon.com/cloudmap/](https://console.aws.amazon.com/cloudmap/).

1. From the list of namespaces, select the `cloudmap-tutorial` namespace and choose **View details**.

1. On the namespace details page, from the list of services, select the `data-service` service and choose **View details**.

1. In the **Service instances** section, select the `data-instance` instance and choose **Deregister**.

1. Using the breadcrumb at the top of the page, select **cloudmap-tutorial.com** to navigate back to the namespace detail page.

1. On the namespace details page, from the list of services, select the **data-service** service and choose **Delete**.

1. Repeat steps 3-6 for the `app-service` service and the `write-instance` and `read-instance` service instances.

1. In the left navigation, choose **Namespaces**.

1. Select the `cloudmap-tutorial` namespace and choose **Delete**.

The following table lists procedures that you can follow to delete the other resources used in the tutorial.


| Resource | Steps | 
| --- | --- | 
| DynamoDB table | [Step 6: (Optional) Delete your DynamoDB table to clean up resources](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/getting-started-step-6.html) in the Amazon DynamoDB Developer Guide | 
| Lambda functions and associated IAM execution role | [Clean up](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html#gettingstarted-cleanup) in the *AWS Lambda Developer Guide* | 