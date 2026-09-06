

# AWS credentials for your application
<a name="sdk-session-credentials"></a>

To give your application access to AWS resources in your account — such as your Amazon S3 buckets, DynamoDB tables, or other AWS services — provide an IAM role ARN when starting a stream session. Amazon GameLift Streams assumes the role and makes credentials available to your application automatically.

To configure session credentials, pass the `--role-arn` parameter when calling [StartStreamSession](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_StartStreamSession.html). The following example shows a Windows launch script (`.bat` file) that downloads a configuration file from Amazon S3 and then launches the application:

```
REM --- Configuration ---
SET "S3_CONFIG_PATH=s3://{{my-app-bucket}}/configs/app-config.json"
SET "LOCAL_CONFIG_DIR=%TEMP%\my-app-config"
SET "LOCAL_CONFIG_FILE=%LOCAL_CONFIG_DIR%\app-config.json"

REM --- Add AWS CLI to PATH (required for Proton runtime) ---
SET "PATH=%PATH%;C:\Program Files\Amazon\AWSCLIV2"

REM --- Create local directory if it doesn't exist ---
IF NOT EXIST "%LOCAL_CONFIG_DIR%" (mkdir "%LOCAL_CONFIG_DIR%")

REM --- Download configuration file from S3 ---
echo Downloading configuration from %S3_CONFIG_PATH%...
aws s3 cp "%S3_CONFIG_PATH%" "%LOCAL_CONFIG_FILE%"
IF %ERRORLEVEL% NEQ 0 (
    echo ERROR: Failed to download configuration file from S3.
    exit /b 1
)
echo Configuration downloaded to %LOCAL_CONFIG_FILE%.

REM --- Launch the application with config file ---
echo Starting application...
my-app.exe --config "%LOCAL_CONFIG_FILE%" %*
exit /b %ERRORLEVEL%
```

You do not need to change your application code. The AWS CLI and all AWS SDKs automatically discover and use the credentials through the [AWS SDK credential provider chain](https://docs.aws.amazon.com/sdkref/latest/guide/standardized-credentials.html#credentialProviderChain).

The AWS CLI version 2.35.11 is available on all Amazon GameLift Streams runtime environments (Windows, Ubuntu, and Proton). The AWS CLI and all AWS SDKs automatically refresh credentials for the lifetime of the session.

For the full setup guide, including IAM role creation, trust policies, and troubleshooting, see [Provide AWS credentials to your streaming application](session-credentials.md).

**Note**  
Do not pass AWS credentials through `AdditionalEnvironmentVariables` (such as `AWS_ACCESS_KEY_ID` or `AWS_SECRET_ACCESS_KEY`). These take precedence and prevent your application from using the IAM role credentials.