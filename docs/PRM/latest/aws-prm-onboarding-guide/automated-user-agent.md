

# Automated User Agent
<a name="automated-user-agent"></a>

For partner solutions that make multiple regular AWS API/CLI calls, you can automate User Agent string inclusion using AWS SDK Application ID settings instead of instrumenting every call individually.

**Warning**  
Only configure User Agent strings for regular AWS API/CLI calls that are directly made by your partner solution. Do not configure User Agent strings for customer-initiated calls that are independent of your solution.

**Note**  
If an Application ID is already configured, you can append your Partner Revenue Measurement User Agent string using a space as a delimiter. For example: `EXISTING_APP_ID APN_1.1/pc_5ugbbrmu7ud3u5hsipfzug61p$`

## Shared AWS Config File
<a name="config-file-method"></a>

Configure the User Agent string in the AWS shared configuration file (`~/.aws/config`):

**Note**  
Replace `5ugbbrmu7ud3u5hsipfzug61p` with your product code. See [Product Code Retrieval](product-code-retrieval.md). The `$` is the required end delimiter.

```
[default]
sdk_ua_app_id=APN_1.1/pc_5ugbbrmu7ud3u5hsipfzug61p$
```

## Environment Variable
<a name="environment-variable-method"></a>

Set the User Agent string using environment variables for automated deployments:

**Note**  
Replace `5ugbbrmu7ud3u5hsipfzug61p` with your product code. The `$` is the required end delimiter.

Linux/macOS:

```
export AWS_SDK_UA_APP_ID=APN_1.1/pc_5ugbbrmu7ud3u5hsipfzug61p$
```

Windows:

```
setx AWS_SDK_UA_APP_ID APN_1.1/pc_5ugbbrmu7ud3u5hsipfzug61p$
```

Python:

```
import os
os.environ['AWS_SDK_UA_APP_ID'] = 'APN_1.1/pc_5ugbbrmu7ud3u5hsipfzug61p$'
```

Node.js:

```
process.env.AWS_SDK_UA_APP_ID = 'APN_1.1/pc_5ugbbrmu7ud3u5hsipfzug61p$';
```

## JVM System Property (Java/Kotlin)
<a name="jvm-system-property-method"></a>

For Java and Kotlin applications, configure the User Agent string using JVM system properties:

**Note**  
Replace `5ugbbrmu7ud3u5hsipfzug61p` with your product code. The `$` is the required end delimiter.

```
java -Dsdk.ua.appId="APN_1.1/pc_5ugbbrmu7ud3u5hsipfzug61p$" -jar your-application.jar
```

Or set it programmatically:

```
System.setProperty("sdk.ua.appId", "APN_1.1/pc_5ugbbrmu7ud3u5hsipfzug61p$");
```

## Support by AWS SDKs and Tools
<a name="sdk-tool-support"></a>

The Application ID configuration methods described above are supported by most AWS SDKs and tools. For a complete list, see [Application ID support by AWS SDKs and tools](https://docs.aws.amazon.com/sdkref/latest/guide/feature-appid.html#appid-sdk-compat). JVM system property settings are only supported by the AWS SDK for Java and the AWS SDK for Kotlin.

## Validation
<a name="automation-validation"></a>

After configuring automated User Agent settings, verify the configuration:

1. Make a test AWS API call from your application

1. Check AWS CloudTrail logs to verify the User Agent string appears in the `userAgent` field

1. Confirm the format matches exactly: `APN_1.1/pc_<YOUR-PRODUCT-CODE>$`