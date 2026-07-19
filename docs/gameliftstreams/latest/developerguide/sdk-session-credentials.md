# AWS credentials for your application

To give your application access to AWS resources in your account — such as your Amazon S3 buckets,
DynamoDB tables, or other AWS services — provide an IAM role ARN when starting a stream session.
Amazon GameLift Streams assumes the role and makes credentials available to your application automatically.

To configure session credentials, pass the `--role-arn` parameter when calling
[StartStreamSession](../apireference/API_StartStreamSession.md "../apireference/API_StartStreamSession.md").
The following example shows a Windows launch script (`.bat` file) that downloads a
configuration file from Amazon S3 and then launches the application:

```
REM --- Configuration ---
SET "S3_CONFIG_PATH=s3://`my-app-bucket`/configs/app-config.json"
SET "LOCAL_CONFIG_DIR=%TEMP%\my-app-config"
SET "LOCAL_CONFIG_FILE=%LOCAL_CONFIG_DIR%\app-config.json"

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

You do not need to change your application code. Credentials are automatically
discovered through the [AWS SDK
credential provider chain](../../../sdkref/latest/guide/standardized-credentials.md#credentialProviderChain "../../../sdkref/latest/guide/standardized-credentials.md#credentialProviderChain") and refreshed for the lifetime of the session.

For the full setup guide, including IAM role creation, trust policies, and troubleshooting, see
[Provide AWS credentials to your streaming application](session-credentials.md "session-credentials.md").

###### Note

Do not pass AWS credentials through `AdditionalEnvironmentVariables` (such as
`AWS_ACCESS_KEY_ID` or `AWS_SECRET_ACCESS_KEY`). These take
precedence and prevent your application from using the IAM role credentials.
