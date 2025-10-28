# Interacting with your EMR Serverless application on the

AWS CLI

From the AWS CLI, create, describe, and delete individual applications. You can also
list all of your applications so that access them at a glance. This section describes
how to perform these actions. For more application operations, such as starting, stopping, and
application updates, refer to the [EMR Serverless API Reference](../../../emr-serverless/latest/APIReference/Welcome.md "../../../emr-serverless/latest/APIReference/Welcome.md").
For examples of how to use the EMR Serverless API using the AWS SDK for Java, refer to [Java
examples](https://github.com/aws-samples/emr-serverless-samples/tree/main/examples/java-api "https://github.com/aws-samples/emr-serverless-samples/tree/main/examples/java-api") in our GitHub repository. For examples of how to use the EMR Serverless
API using the AWS SDK for Python (Boto), refer to [Python examples](https://github.com/aws-samples/emr-serverless-samples/tree/main/examples/python-api "https://github.com/aws-samples/emr-serverless-samples/tree/main/examples/python-api") in our GitHub repository.

To create an application, use `create-application`. You must specify
`SPARK` or `HIVE` as the application `type`. This command
returns the application’s ARN, name, and ID.

```
aws emr-serverless create-application \
--name `my-application-name` \
--type '`application-type`' \
--release-label `release-version`
```

To describe an application, use `get-application` and provide its
`application-id`. This command returns the state and capacity-related
configurations for your application.

```
aws emr-serverless get-application \
--application-id `application-id`
```

To list all of your applications, call `list-applications`. This command
returns the same properties as `get-application` but includes all of your
applications.

```
aws emr-serverless list-applications
```

To delete your application, call `delete-application` and supply your
`application-id`.

```
aws emr-serverless delete-application \
--application-id `application-id`
```
