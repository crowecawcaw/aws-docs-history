# Use `GetAccountPasswordPolicy` with an AWS SDK or CLI

The following code examples show how to use `GetAccountPasswordPolicy`.

.NET

**SDK for .NET**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/IAM#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/IAM#code-examples").

```
    /// <summary>
    /// Gets the IAM password policy for an AWS account.
    /// </summary>
    /// <returns>The PasswordPolicy for the AWS account.</returns>
    public async Task<PasswordPolicy> GetAccountPasswordPolicyAsync()
    {
        var response = await _IAMService.GetAccountPasswordPolicyAsync(new GetAccountPasswordPolicyRequest());
        return response.PasswordPolicy;
    }



```

- For API details, see
  [GetAccountPasswordPolicy](../../../goto/DotNetSDKV3/iam-2010-05-08/GetAccountPasswordPolicy.md "../../../goto/DotNetSDKV3/iam-2010-05-08/GetAccountPasswordPolicy.md")
  in _AWS SDK for .NET API Reference_.

CLI

**AWS CLI**

**To see the current account password policy**

The following `get-account-password-policy` command displays details about the password policy for the current account.

```
`aws iam get-account-password-policy`

```

Output:

```
{
    "PasswordPolicy": {
        "AllowUsersToChangePassword": false,
        "RequireLowercaseCharacters": false,
        "RequireUppercaseCharacters": false,
        "MinimumPasswordLength": 8,
        "RequireNumbers": true,
        "RequireSymbols": true
    }
}
```

If no password policy is defined for the account, the command returns a `NoSuchEntity` error.

For more information, see [Setting an account password policy for IAM users](id_credentials_passwords_account-policy.md "id_credentials_passwords_account-policy.md") in the _AWS IAM User Guide_.

- For API details, see
  [GetAccountPasswordPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-account-password-policy.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-account-password-policy.html")
  in _AWS CLI Command Reference_.

Go

**SDK for Go V2**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/iam#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/iam#code-examples").

```

import (
	"context"
	"log"

	"github.com/aws/aws-sdk-go-v2/service/iam"
	"github.com/aws/aws-sdk-go-v2/service/iam/types"
)

// AccountWrapper encapsulates AWS Identity and Access Management (IAM) account actions
// used in the examples.
// It contains an IAM service client that is used to perform account actions.
type AccountWrapper struct {
	IamClient *iam.Client
}



// GetAccountPasswordPolicy gets the account password policy for the current account.
// If no policy has been set, a NoSuchEntityException is error is returned.
func (wrapper AccountWrapper) GetAccountPasswordPolicy(ctx context.Context) (*types.PasswordPolicy, error) {
	var pwPolicy *types.PasswordPolicy
	result, err := wrapper.IamClient.GetAccountPasswordPolicy(ctx,
		&iam.GetAccountPasswordPolicyInput{})
	if err != nil {
		log.Printf("Couldn't get account password policy. Here's why: %v\n", err)
	} else {
		pwPolicy = result.PasswordPolicy
	}
	return pwPolicy, err
}



```

- For API details, see
  [GetAccountPasswordPolicy](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.GetAccountPasswordPolicy "https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.GetAccountPasswordPolicy")
  in _AWS SDK for Go API Reference_.

JavaScript

**SDK for JavaScript (v3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/iam#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/iam#code-examples").

Get the account password policy.

```
import {
  GetAccountPasswordPolicyCommand,
  IAMClient,
} from "@aws-sdk/client-iam";

const client = new IAMClient({});

export const getAccountPasswordPolicy = async () => {
  const command = new GetAccountPasswordPolicyCommand({});

  const response = await client.send(command);
  console.log(response.PasswordPolicy);
  return response;
};


```

- For API details, see
  [GetAccountPasswordPolicy](../../../AWSJavaScriptSDK/v3/latest/client/iam/command/GetAccountPasswordPolicyCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/iam/command/GetAccountPasswordPolicyCommand.md")
  in _AWS SDK for JavaScript API Reference_.

PHP

**SDK for PHP**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/php/example_code/iam#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/php/example_code/iam#code-examples").

```
$uuid = uniqid();
$service = new IAMService();

    public function getAccountPasswordPolicy()
    {
        return $this->iamClient->getAccountPasswordPolicy();
    }


```

- For API details, see
  [GetAccountPasswordPolicy](../../../goto/SdkForPHPV3/iam-2010-05-08/GetAccountPasswordPolicy.md "../../../goto/SdkForPHPV3/iam-2010-05-08/GetAccountPasswordPolicy.md")
  in _AWS SDK for PHP API Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example returns details about the password policy for the current account. If no password policy is defined for the account, the command returns a `NoSuchEntity` error.**

```
Get-IAMAccountPasswordPolicy

```

**Output:**

```
AllowUsersToChangePassword : True
ExpirePasswords            : True
HardExpiry                 : False
MaxPasswordAge             : 90
MinimumPasswordLength      : 8
PasswordReusePrevention    : 20
RequireLowercaseCharacters : True
RequireNumbers             : True
RequireSymbols             : False
RequireUppercaseCharacters : True
```

- For API details, see
  [GetAccountPasswordPolicy](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example returns details about the password policy for the current account. If no password policy is defined for the account, the command returns a `NoSuchEntity` error.**

```
Get-IAMAccountPasswordPolicy

```

**Output:**

```
AllowUsersToChangePassword : True
ExpirePasswords            : True
HardExpiry                 : False
MaxPasswordAge             : 90
MinimumPasswordLength      : 8
PasswordReusePrevention    : 20
RequireLowercaseCharacters : True
RequireNumbers             : True
RequireSymbols             : False
RequireUppercaseCharacters : True
```

- For API details, see
  [GetAccountPasswordPolicy](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/iam#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/iam#code-examples").

```
def print_password_policy():
    """
    Prints the password policy for the account.
    """
    try:
        pw_policy = iam.AccountPasswordPolicy()
        print("Current account password policy:")
        print(
            f"\tallow_users_to_change_password: {pw_policy.allow_users_to_change_password}"
        )
        print(f"\texpire_passwords: {pw_policy.expire_passwords}")
        print(f"\thard_expiry: {pw_policy.hard_expiry}")
        print(f"\tmax_password_age: {pw_policy.max_password_age}")
        print(f"\tminimum_password_length: {pw_policy.minimum_password_length}")
        print(f"\tpassword_reuse_prevention: {pw_policy.password_reuse_prevention}")
        print(
            f"\trequire_lowercase_characters: {pw_policy.require_lowercase_characters}"
        )
        print(f"\trequire_numbers: {pw_policy.require_numbers}")
        print(f"\trequire_symbols: {pw_policy.require_symbols}")
        print(
            f"\trequire_uppercase_characters: {pw_policy.require_uppercase_characters}"
        )
        printed = True
    except ClientError as error:
        if error.response["Error"]["Code"] == "NoSuchEntity":
            print("The account does not have a password policy set.")
        else:
            logger.exception("Couldn't get account password policy.")
            raise
    else:
        return printed




```

- For API details, see
  [GetAccountPasswordPolicy](../../../goto/boto3/iam-2010-05-08/GetAccountPasswordPolicy.md "../../../goto/boto3/iam-2010-05-08/GetAccountPasswordPolicy.md")
  in _AWS SDK for Python (Boto3) API Reference_.

Ruby

**SDK for Ruby**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/iam#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/iam#code-examples").

```
# Class to manage IAM account password policies
class PasswordPolicyManager
  attr_accessor :iam_client, :logger

  def initialize(iam_client, logger: Logger.new($stdout))
    @iam_client = iam_client
    @logger = logger
    @logger.progname = 'IAMPolicyManager'
  end

  # Retrieves and logs the account password policy
  def print_account_password_policy
    response = @iam_client.get_account_password_policy
    @logger.info("The account password policy is: #{response.password_policy.to_h}")
  rescue Aws::IAM::Errors::NoSuchEntity
    @logger.info('The account does not have a password policy.')
  rescue Aws::Errors::ServiceError => e
    @logger.error("Couldn't print the account password policy. Error: #{e.code} - #{e.message}")
    raise
  end
end


```

- For API details, see
  [GetAccountPasswordPolicy](../../../goto/SdkForRubyV3/iam-2010-05-08/GetAccountPasswordPolicy.md "../../../goto/SdkForRubyV3/iam-2010-05-08/GetAccountPasswordPolicy.md")
  in _AWS SDK for Ruby API Reference_.

Rust

**SDK for Rust**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/iam#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/iam#code-examples").

```
pub async fn get_account_password_policy(
    client: &iamClient,
) -> Result<GetAccountPasswordPolicyOutput, SdkError<GetAccountPasswordPolicyError>> {
    let response = client.get_account_password_policy().send().await?;

    Ok(response)
}


```

- For API details, see
  [GetAccountPasswordPolicy](https://docs.rs/aws-sdk-iam/latest/aws_sdk_iam/client/struct.Client.html#method.get_account_password_policy "https://docs.rs/aws-sdk-iam/latest/aws_sdk_iam/client/struct.Client.html#method.get_account_password_policy")
  in _AWS SDK for Rust API reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
