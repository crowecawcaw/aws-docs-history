# Learn how to use AWS Cloud Map service discovery with
 custom attributes using the AWS CLI

This tutorial demonstrates how you can use AWS Cloud Map service discovery with custom
 attributes. You'll create a microservices application that uses AWS Cloud Map to discover resources
 dynamically using custom attributes. The application consists of two Lambda functions that
 write data to and read from a DynamoDB table, with all resources registered in AWS Cloud Map.

For an AWS Management Console version of the tutorial, see [Learn how to use AWS Cloud Map service discovery with custom
 attributes](tutorial-microservices.md "tutorial-microservices.md").


## Prerequisites


Before you begin this tutorial, complete the steps in [Set up to use AWS Cloud Map](setting-up-cloud-map.md "setting-up-cloud-map.md").


## Create an AWS Cloud Map namespace


A namespace is a construct used to group services for an application. In this step,
 you'll create a namespace that allows resources to be discoverable through AWS Cloud Map API
 calls.


1. Run the following command to create an HTTP namespace:



```
aws servicediscovery create-http-namespace \
  --name cloudmap-tutorial \
  --creator-request-id cloudmap-tutorial-request
```

The command returns an operation ID. You can check the status of the operation with
 the following command:



```
aws servicediscovery get-operation \
  --operation-id operation-id
```
2. Once the namespace is created, you can retrieve its ID for use in subsequent
 commands:



```
aws servicediscovery list-namespaces \
  --query "Namespaces[?Name=='cloudmap-tutorial'].Id" \
  --output text
```
3. Store the namespace ID in a variable for later use:



```
NAMESPACE_ID=$(aws servicediscovery list-namespaces \
  --query "Namespaces[?Name=='cloudmap-tutorial'].Id" \
  --output text)
```

## Create a DynamoDB table


Next, create a DynamoDB table that will store data for your application:


1. Run the following command to create the table:



```
aws dynamodb create-table \
  --table-name cloudmap \
  --attribute-definitions AttributeName=id,AttributeType=S \
  --key-schema AttributeName=id,KeyType=HASH \
  --billing-mode PAY_PER_REQUEST
```
2. Wait for the table to become active before proceeding:



```
aws dynamodb wait table-exists --table-name cloudmap
```

This command waits until the table is fully created and ready to use.

## Create an AWS Cloud Map data service and register the DynamoDB table


Now, create a service in your namespace to represent data storage resources:


1. Run the following command to create a AWS Cloud Map service for data storage resources:



```
aws servicediscovery create-service \
  --name data-service \
  --namespace-id $NAMESPACE_ID \
  --creator-request-id data-service-request
```
2. Get the service ID for the data service:



```
DATA_SERVICE_ID=$(aws servicediscovery list-services \
  --query "Services[?Name=='data-service'].Id" \
  --output text)
```
3. Register the DynamoDB table as a service instance with a custom attribute that specifies
 the table name:



```
aws servicediscovery register-instance \
  --service-id $DATA_SERVICE_ID \
  --instance-id data-instance \
  --attributes tablename=cloudmap
```

The custom attribute `tablename=cloudmap` allows other services to discover
 the DynamoDB table name dynamically.

## Create an IAM role for
 Lambda functions


Create an IAM role that the Lambda functions will use to access AWS
 resources:


1. Create the trust policy document for the IAM role using the following JSON:



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "lambda.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```
2. Run the following command to create the IAM role using the trust policy:



```
aws iam create-role \
  --role-name cloudmap-tutorial-role \
  --assume-role-policy-document file://lambda-trust-policy.json
```
3. Create a file for a custom IAM policy with least privilege permissions using the following JSON:



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogGroup",
 "logs:CreateLogStream",
 "logs:PutLogEvents"
 ],
 "Resource": "arn:aws:logs:*:*:*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "servicediscovery:DiscoverInstances"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "dynamodb:PutItem",
 "dynamodb:Scan"
 ],
 "Resource": "arn:aws:dynamodb:*:*:table/cloudmap"
 }
 ]
}`

```
4. Create and attach the policy to the IAM role:



```
aws iam create-policy \
  --policy-name CloudMapTutorialPolicy \
  --policy-document file://cloudmap-policy.json

POLICY_ARN=$(aws iam list-policies \
  --query "Policies[?PolicyName=='CloudMapTutorialPolicy'].Arn" \
  --output text)

aws iam attach-role-policy \
  --role-name cloudmap-tutorial-role \
  --policy-arn $POLICY_ARN

aws iam attach-role-policy \
  --role-name cloudmap-tutorial-role \
  --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
```

## Create the Lambda function to
 write data


To create a Lambda function that writes data to the DynamoDB
 table, follow these steps:


1. Create the Python file for the write function:



```
cat > writefunction.py << EOF
import json
import boto3
import random

def lambda_handler(event, context):
    try:
        serviceclient = boto3.client('servicediscovery')
        
        response = serviceclient.discover_instances(
            NamespaceName='cloudmap-tutorial',
            ServiceName='data-service')
        
        if not response.get("Instances"):
            return {
                'statusCode': 500,
                'body': json.dumps({"error": "No instances found"})
            }
            
        tablename = response["Instances"][0]["Attributes"].get("tablename")
        if not tablename:
            return {
                'statusCode': 500,
                'body': json.dumps({"error": "Table name attribute not found"})
            }
           
        dynamodbclient = boto3.resource('dynamodb')
           
        table = dynamodbclient.Table(tablename)
        
        # Validate input
        if not isinstance(event, str):
            return {
                'statusCode': 400,
                'body': json.dumps({"error": "Input must be a string"})
            }
           
        response = table.put_item(
            Item={ 'id': str(random.randint(1,100)), 'todo': event })
           
        return {
            'statusCode': 200,
            'body': json.dumps(response)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({"error": str(e)})
        }
EOF
```

This function uses AWS Cloud Map to discover the DynamoDB table name from the custom attribute,
 then writes data to the table.
2. Package and deploy the Lambda function:



```
zip writefunction.zip writefunction.py

ROLE_ARN=$(aws iam get-role --role-name cloudmap-tutorial-role \
  --query 'Role.Arn' --output text)

aws lambda create-function \
  --function-name writefunction \
  --runtime python3.12 \
  --role $ROLE_ARN \
  --handler writefunction.lambda_handler \
  --zip-file fileb://writefunction.zip \
  --architectures x86_64
```
3. Update the function timeout to avoid timeout errors:



```
aws lambda update-function-configuration \
  --function-name writefunction \
  --timeout 5
```

## Create an AWS Cloud Map app service and register the Lambda write function


To create another service in your namespace to represent application functions, follow these steps:


1. Create a service for application functions:



```
aws servicediscovery create-service \
  --name app-service \
  --namespace-id $NAMESPACE_ID \
  --creator-request-id app-service-request
```
2. Get the service ID for the app service:



```
APP_SERVICE_ID=$(aws servicediscovery list-services \
  --query "Services[?Name=='app-service'].Id" \
  --output text)
```
3. Register the Lambda write function as a service instance with custom
 attributes:



```
aws servicediscovery register-instance \
  --service-id $APP_SERVICE_ID \
  --instance-id write-instance \
  --attributes action=write,functionname=writefunction
```

The custom attributes `action=write` and
 `functionname=writefunction` allow clients to discover this function
 based on its purpose.

## Create the Lambda function to
 read data


To create a Lambda function that reads data from the DynamoDB
 table, follow these steps:


1. Create the Python file for the read function:



```
cat > readfunction.py << EOF
import json
import boto3

def lambda_handler(event, context):
    try:
        serviceclient = boto3.client('servicediscovery')

        response = serviceclient.discover_instances(
            NamespaceName='cloudmap-tutorial', 
            ServiceName='data-service')
        
        if not response.get("Instances"):
            return {
                'statusCode': 500,
                'body': json.dumps({"error": "No instances found"})
            }
            
        tablename = response["Instances"][0]["Attributes"].get("tablename")
        if not tablename:
            return {
                'statusCode': 500,
                'body': json.dumps({"error": "Table name attribute not found"})
            }
           
        dynamodbclient = boto3.resource('dynamodb')
           
        table = dynamodbclient.Table(tablename)
        
        # Use pagination for larger tables
        response = table.scan(
            Select='ALL_ATTRIBUTES',
            Limit=50  # Limit results for demonstration purposes
        )
        
        # For production, you would implement pagination like this:
        # items = []
        # while 'LastEvaluatedKey' in response:
        #     items.extend(response['Items'])
        #     response = table.scan(
        #         Select='ALL_ATTRIBUTES',
        #         ExclusiveStartKey=response['LastEvaluatedKey']
        #     )
        # items.extend(response['Items'])

        return {
            'statusCode': 200,
            'body': json.dumps(response)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({"error": str(e)})
        }
EOF
```

This function also uses AWS Cloud Map to discover the DynamoDB table name, then reads data from
 the table. It includes error handling and pagination comments.
2. Package and deploy the Lambda function:



```
zip readfunction.zip readfunction.py

aws lambda create-function \
  --function-name readfunction \
  --runtime python3.12 \
  --role $ROLE_ARN \
  --handler readfunction.lambda_handler \
  --zip-file fileb://readfunction.zip \
  --architectures x86_64
```
3. Update the function timeout:



```
aws lambda update-function-configuration \
  --function-name readfunction \
  --timeout 5
```

## Register the
 Lambda read function as a service instance


To register the Lambda read function as another service instance in the app
 service, follow this step:



```
aws servicediscovery register-instance \
  --service-id $APP_SERVICE_ID \
  --instance-id read-instance \
  --attributes action=read,functionname=readfunction
```

The custom attributes `action=read` and
 `functionname=readfunction` allow clients to discover this function based
 on its purpose.


## Create and run client
 applications


To create a Python client application that uses AWS Cloud Map to discover and invoke the write
 function, follow these steps:


1. Create a Python file for the write client application:



```
cat > writeclient.py << EOF
import boto3
import json

try:
    serviceclient = boto3.client('servicediscovery')

    print("Discovering write function...")
    response = serviceclient.discover_instances(
        NamespaceName='cloudmap-tutorial', 
        ServiceName='app-service', 
        QueryParameters={ 'action': 'write' }
    )

    if not response.get("Instances"):
        print("Error: No instances found")
        exit(1)
        
    functionname = response["Instances"][0]["Attributes"].get("functionname")
    if not functionname:
        print("Error: Function name attribute not found")
        exit(1)
        
    print(f"Found function: {functionname}")

    lambdaclient = boto3.client('lambda')

    print("Invoking Lambda function...")
    resp = lambdaclient.invoke(
        FunctionName=functionname, 
        Payload='"This is a test data"'
    )

    payload = resp["Payload"].read()
    print(f"Response: {payload.decode('utf-8')}")
    
except Exception as e:
    print(f"Error: {str(e)}")
EOF
```

This client uses the `QueryParameters` option to find service instances
 with the `action=write` attribute.
2. Create a Python file for the read client application:



```
cat > readclient.py << EOF
import boto3
import json

try:
    serviceclient = boto3.client('servicediscovery')

    print("Discovering read function...")
    response = serviceclient.discover_instances(
        NamespaceName='cloudmap-tutorial', 
        ServiceName='app-service', 
        QueryParameters={ 'action': 'read' }
    )

    if not response.get("Instances"):
        print("Error: No instances found")
        exit(1)
        
    functionname = response["Instances"][0]["Attributes"].get("functionname")
    if not functionname:
        print("Error: Function name attribute not found")
        exit(1)
        
    print(f"Found function: {functionname}")

    lambdaclient = boto3.client('lambda')

    print("Invoking Lambda function...")
    resp = lambdaclient.invoke(
        FunctionName=functionname, 
        InvocationType='RequestResponse'
    )

    payload = resp["Payload"].read()
    print(f"Response: {payload.decode('utf-8')}")
    
except Exception as e:
    print(f"Error: {str(e)}")
EOF
```
3. Run the write client to add data to the DynamoDB table:



```
python3 writeclient.py
```

The output should show a successful response with HTTP status code 200.
4. Run the read client to retrieve data from the DynamoDB table:



```
python3 readclient.py
```

The output should show the data that was written to the table, including the randomly
 generated ID and the "This is a test data" value.

## Clean up resources


When you're finished with the tutorial, clean up the resources to avoid incurring
 additional charges.


1. First, run the following command to deregister the service instances:



```
aws servicediscovery deregister-instance \
  --service-id $APP_SERVICE_ID \
  --instance-id read-instance

aws servicediscovery deregister-instance \
  --service-id $APP_SERVICE_ID \
  --instance-id write-instance

aws servicediscovery deregister-instance \
  --service-id $DATA_SERVICE_ID \
  --instance-id data-instance
```
2. Run the following command to delete the services:



```
aws servicediscovery delete-service \
  --id $APP_SERVICE_ID

aws servicediscovery delete-service \
  --id $DATA_SERVICE_ID
```
3. Run the following command to delete the namespace:



```
aws servicediscovery delete-namespace \
  --id $NAMESPACE_ID
```
4. Run the following command to delete the Lambda functions:



```
aws lambda delete-function --function-name writefunction
aws lambda delete-function --function-name readfunction
```
5. Run the following command to delete the IAM role and policy:



```
aws iam detach-role-policy \
  --role-name cloudmap-tutorial-role \
  --policy-arn $POLICY_ARN

aws iam detach-role-policy \
  --role-name cloudmap-tutorial-role \
  --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole

aws iam delete-policy \
  --policy-arn $POLICY_ARN

aws iam delete-role --role-name cloudmap-tutorial-role
```
6. Run the following command to delete the DynamoDB table:



```
aws dynamodb delete-table --table-name cloudmap
```
7. Run the following command to clean up temporary files:



```
rm -f lambda-trust-policy.json cloudmap-policy.json writefunction.py readfunction.py writefunction.zip readfunction.zip writeclient.py readclient.py
```
