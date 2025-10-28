# Generate sample event

payloads with AWS SAM

To test your Lambda functions, you can generate and customize sample event payloads that imitate the data
your Lambda functions will receive when triggered by other AWS services. This includes services like API Gateway,
AWS CloudFormation, Amazon S3, and more.

Generating sample event payloads helps you test the behavior of your Lambda function with a variety of different
inputs without needing to work in a live environment. This approach also saves time when compared to manually
creating AWS service event samples to test functions.

For the full list of services that you can generate sample event payloads for, use
this command:

```
sam local generate-event --help
```

For the list of options you can use for a particular service, use this command:

```
sam local generate-event [SERVICE] --help
```

Examples:

```
#Generates the event from S3 when a new object is created
sam local generate-event s3 put

# Generates the event from S3 when an object is deleted
sam local generate-event s3 delete

```
