# Use `GetSessionToken` with an AWS SDK or CLI

The following code examples show how to use `GetSessionToken`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
context in the following code example:

- [Get a session token that requires an MFA token](sts_example_sts_Scenario_SessionTokenMfa_section.md "sts_example_sts_Scenario_SessionTokenMfa_section.md")

CLI

**AWS CLI**

**To get a set of short term credentials for an IAM identity**

The following `get-session-token` command retrieves a set of short-term credentials for the IAM identity making the call. The resulting credentials can be used for requests where multi-factor authentication (MFA) is required by policy. The credentials expire 15 minutes after they are generated.

```
`aws sts get-session-token \
 --duration-seconds `900` \
 --serial-number `"YourMFADeviceSerialNumber"` \
 --token-code `123456``

```

Output:

```
{
    "Credentials": {
        "AccessKeyId": "ASIAIOSFODNN7EXAMPLE",
        "SecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYzEXAMPLEKEY",
        "SessionToken": "AQoEXAMPLEH4aoAH0gNCAPyJxz4BlCFFxWNE1OPTgk5TthT+FvwqnKwRcOIfrRh3c/LTo6UDdyJwOOvEVPvLXCrrrUtdnniCEXAMPLE/IvU1dYUg2RVAJBanLiHb4IgRmpRV3zrkuWJOgQs8IZZaIv2BXIa2R4OlgkBN9bkUDNCJiBeb/AXlzBBko7b15fjrBs2+cTQtpZ3CYWFXG8C5zqx37wnOE49mRl/+OtkIKGO7fAE",
        "Expiration": "2020-05-19T18:06:10+00:00"
    }
}
```

For more information, see [Requesting Temporary Security Credentials](id_credentials_temp_request.md#api_getsessiontoken "id_credentials_temp_request.md#api_getsessiontoken") in the _AWS IAM User Guide_.

- For API details, see
  [GetSessionToken](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sts/get-session-token.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sts/get-session-token.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: Returns an `Amazon.RuntimeAWSCredentials` instance containing temporary credentials valid for a set period of time. The credentials used to request temporary credentials are inferred from the current shell defaults. To specify other credentials, use the -ProfileName or -AccessKey/-SecretKey parameters.**

```
Get-STSSessionToken

```

**Output:**

```
AccessKeyId                             Expiration                              SecretAccessKey                        SessionToken
-----------                             ----------                              ---------------                        ------------
EXAMPLEACCESSKEYID                      2/16/2015 9:12:28 PM                    examplesecretaccesskey...              SamPleTokeN.....
```

**Example 2: Returns an `Amazon.RuntimeAWSCredentials` instance containing temporary credentials valid for one hour. The credentials used to make the request are obtained from the specified profile.**

```
Get-STSSessionToken -DurationInSeconds 3600 -ProfileName myprofile

```

**Output:**

```
AccessKeyId                             Expiration                              SecretAccessKey                        SessionToken
-----------                             ----------                              ---------------                        ------------
EXAMPLEACCESSKEYID                      2/16/2015 9:12:28 PM                    examplesecretaccesskey...              SamPleTokeN.....
```

**Example 3: Returns an `Amazon.RuntimeAWSCredentials` instance containing temporary credentials valid for one hour using the identification number of the MFA device associated with the account whose credentials are specified in the profile 'myprofilename' and the value provided by the device.**

```
Get-STSSessionToken -DurationInSeconds 3600 -ProfileName myprofile -SerialNumber YourMFADeviceSerialNumber -TokenCode 123456

```

**Output:**

```
AccessKeyId                             Expiration                              SecretAccessKey                        SessionToken
-----------                             ----------                              ---------------                        ------------
EXAMPLEACCESSKEYID                      2/16/2015 9:12:28 PM                    examplesecretaccesskey...              SamPleTokeN.....
```

- For API details, see
  [GetSessionToken](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: Returns an `Amazon.RuntimeAWSCredentials` instance containing temporary credentials valid for a set period of time. The credentials used to request temporary credentials are inferred from the current shell defaults. To specify other credentials, use the -ProfileName or -AccessKey/-SecretKey parameters.**

```
Get-STSSessionToken

```

**Output:**

```
AccessKeyId                             Expiration                              SecretAccessKey                        SessionToken
-----------                             ----------                              ---------------                        ------------
EXAMPLEACCESSKEYID                      2/16/2015 9:12:28 PM                    examplesecretaccesskey...              SamPleTokeN.....
```

**Example 2: Returns an `Amazon.RuntimeAWSCredentials` instance containing temporary credentials valid for one hour. The credentials used to make the request are obtained from the specified profile.**

```
Get-STSSessionToken -DurationInSeconds 3600 -ProfileName myprofile

```

**Output:**

```
AccessKeyId                             Expiration                              SecretAccessKey                        SessionToken
-----------                             ----------                              ---------------                        ------------
EXAMPLEACCESSKEYID                      2/16/2015 9:12:28 PM                    examplesecretaccesskey...              SamPleTokeN.....
```

**Example 3: Returns an `Amazon.RuntimeAWSCredentials` instance containing temporary credentials valid for one hour using the identification number of the MFA device associated with the account whose credentials are specified in the profile 'myprofilename' and the value provided by the device.**

```
Get-STSSessionToken -DurationInSeconds 3600 -ProfileName myprofile -SerialNumber YourMFADeviceSerialNumber -TokenCode 123456

```

**Output:**

```
AccessKeyId                             Expiration                              SecretAccessKey                        SessionToken
-----------                             ----------                              ---------------                        ------------
EXAMPLEACCESSKEYID                      2/16/2015 9:12:28 PM                    examplesecretaccesskey...              SamPleTokeN.....
```

- For API details, see
  [GetSessionToken](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/sts#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/sts#code-examples").

Get a session token by passing an MFA token and use it to list Amazon S3 buckets for the account.

```
def list_buckets_with_session_token_with_mfa(mfa_serial_number, mfa_totp, sts_client):
    """
    Gets a session token with MFA credentials and uses the temporary session
    credentials to list Amazon S3 buckets.

    Requires an MFA device serial number and token.

    :param mfa_serial_number: The serial number of the MFA device. For a virtual MFA
                              device, this is an Amazon Resource Name (ARN).
    :param mfa_totp: A time-based, one-time password issued by the MFA device.
    :param sts_client: A Boto3 STS instance that has permission to assume the role.
    """
    if mfa_serial_number is not None:
        response = sts_client.get_session_token(
            SerialNumber=mfa_serial_number, TokenCode=mfa_totp
        )
    else:
        response = sts_client.get_session_token()
    temp_credentials = response["Credentials"]

    s3_resource = boto3.resource(
        "s3",
        aws_access_key_id=temp_credentials["AccessKeyId"],
        aws_secret_access_key=temp_credentials["SecretAccessKey"],
        aws_session_token=temp_credentials["SessionToken"],
    )

    print(f"Buckets for the account:")
    for bucket in s3_resource.buckets.all():
        print(bucket.name)




```

- For API details, see
  [GetSessionToken](../../../goto/boto3/sts-2011-06-15/GetSessionToken.md "../../../goto/boto3/sts-2011-06-15/GetSessionToken.md")
  in _AWS SDK for Python (Boto3) API Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
