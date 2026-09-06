

# Locally invoke Lambda functions with AWS SAM
<a name="serverless-sam-cli-using-invoke"></a>

Locally invoking a Lambda function before testing or deploying in the cloud can have a variety of benefits. It allows you to test the logic of your function faster. Testing locally first reduces the likelihood of identifying issues when testing in the cloud or during deployment, which can help you avoid unnecessary costs. Additionally, local testing makes debugging easier to do.

You can invoke your Lambda function locally by using the [sam local invoke](sam-cli-command-reference-sam-local-invoke.md) command and providing the function's logical ID and an event file. **sam local invoke** also accepts `stdin` as an event. For more information about events, see [Event](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-concepts.html#gettingstarted-concepts-event) in the *AWS Lambda Developer Guide*. For information about event message formats from different AWS services, see [Using AWS Lambda with other services](https://docs.aws.amazon.com/lambda/latest/dg/lambda-services.html) in the *AWS Lambda Developer Guide*.

**Note**  
It's not recommended to use SAM CLI's local invoke capabilities in untrusted code. To have complete isolation from your local environment, execute the code in the Lambda service directly.

**Note**  
The **sam local invoke** command corresponds to the AWS Command Line Interface (AWS CLI) command [`aws lambda invoke`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/invoke.html). You can use either command to invoke a Lambda function.

You must run the **sam local invoke** command in the project directory that contains the function that you want to invoke.

 Examples:

```
# Invoking function with event file
$ sam local invoke "Ratings" -e event.json

# Invoking function with event via stdin
$ echo '{"message": "Hey, are you there?" }' | sam local invoke --event - "Ratings"

# For more options
$ sam local invoke --help
```

## Environment variable file
<a name="serverless-sam-cli-using-invoke-environment-file"></a>

To declare environment variables locally that override values defined in your templates, do the following:

1. Create a JSON or `.env` file that contains the environment variables to override.

1. Use the `--env-vars` argument to override values defined in your templates.

The `--env-vars` option supports two file formats. The file format is automatically detected based on the file content.

### Declaring environment variables with JSON
<a name="serverless-sam-cli-using-invoke-environment-file-declaring"></a>

To declare environment variables that apply globally to all resources, specify a `Parameters` object like the following:

```
{
    "Parameters": {
        "TABLE_NAME": "localtable",
        "BUCKET_NAME": "amzn-s3-demo-bucket",
        "STAGE": "dev"
    }
}
```

To declare different environment variables for each resource, specify objects for each resource like the following:

```
{
    "MyFunction1": {
        "TABLE_NAME": "localtable",
        "BUCKET_NAME": "amzn-s3-demo-bucket",
    },
    "MyFunction2": {
        "TABLE_NAME": "localtable",
        "STAGE": "dev"
    }
}
```

When specifying objects for each resource, you can use the following identifiers, listed in order of highest to lowest precedence:

1. `logical_id`

1. `function_id`

1. `function_name`

1. Full path identifier

You can use both of the preceding methods of declaring environment variables together in a single file. When doing so, environment variables that you provided for specific resources take precedence over global environment variables.

Save your environment variables in a JSON file, such as `env.json`.

### Declaring environment variables with .env files
<a name="serverless-sam-cli-using-invoke-environment-file-dotenv"></a>

You can also use a `.env` file to declare environment variables. Variables declared in a `.env` file apply globally to all functions, equivalent to the `Parameters` object in JSON format.

```
TABLE_NAME=localtable
BUCKET_NAME=amzn-s3-demo-bucket
STAGE=dev
```

The `.env` format supports comments (lines starting with `#`) and quoted values.

**Note**  
The `.env` format only supports global environment variables. To declare function-specific environment variables, use the JSON format.

### Overriding environment variable values
<a name="serverless-sam-cli-using-invoke-environment-file-override"></a>

To override environment variables with those defined in your environment variable file, use the `--env-vars` argument with the **invoke** or **start-api** commands. For example:

```
# Using a JSON file
sam local invoke --env-vars env.json

# Using a .env file
sam local invoke --env-vars .env
```

## Layers
<a name="serverless-sam-cli-using-invoke-layers"></a>

If your application includes layers, for information about how to debug issues with layers on your local host, see [Increase efficiency using Lambda layers with AWS SAM](serverless-sam-cli-layers.md).

## Learn more
<a name="serverless-sam-cli-using-invoke-learn"></a>

For a hands-on example of invoking functions locally, see [ Module 2 - Run locally](https://s12d.com/sam-ws-en-local) in *The Complete AWS SAM Workshop*.