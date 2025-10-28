# Use `DeleteUserPolicy` with an AWS SDK or CLI

The following code examples show how to use `DeleteUserPolicy`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
context in the following code example:

- [Learn the basics](iam_example_iam_Scenario_CreateUserAssumeRole_section.md "iam_example_iam_Scenario_CreateUserAssumeRole_section.md")

.NET

**SDK for .NET**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/IAM#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/IAM#code-examples").

```
    /// <summary>
    /// Delete an IAM user policy.
    /// </summary>
    /// <param name="policyName">The name of the IAM policy to delete.</param>
    /// <param name="userName">The username of the IAM user.</param>
    /// <returns>A Boolean value indicating the success of the action.</returns>
    public async Task<bool> DeleteUserPolicyAsync(string policyName, string userName)
    {
        var response = await _IAMService.DeleteUserPolicyAsync(new DeleteUserPolicyRequest { PolicyName = policyName, UserName = userName });

        return response.HttpStatusCode == System.Net.HttpStatusCode.OK;
    }



```

- For API details, see
  [DeleteUserPolicy](../../../goto/DotNetSDKV3/iam-2010-05-08/DeleteUserPolicy.md "../../../goto/DotNetSDKV3/iam-2010-05-08/DeleteUserPolicy.md")
  in _AWS SDK for .NET API Reference_.

CLI

**AWS CLI**

**To remove a policy from an IAM user**

The following `delete-user-policy` command removes the specified policy from the IAM user named `Bob`.

```
`aws iam delete-user-policy \
 --user-name `Bob` \
 --policy-name `ExamplePolicy``

```

This command produces no output.

To get a list of policies for an IAM user, use the `list-user-policies` command.

For more information, see [Creating an IAM user in your AWS account](id_users_create.md "id_users_create.md") in the _AWS IAM User Guide_.

- For API details, see
  [DeleteUserPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-user-policy.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-user-policy.html")
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
	"encoding/json"
	"errors"
	"log"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/service/iam"
	"github.com/aws/aws-sdk-go-v2/service/iam/types"
	"github.com/aws/smithy-go"
)

// UserWrapper encapsulates user actions used in the examples.
// It contains an IAM service client that is used to perform user actions.
type UserWrapper struct {
	IamClient *iam.Client
}



// DeleteUserPolicy deletes an inline policy from a user.
func (wrapper UserWrapper) DeleteUserPolicy(ctx context.Context, userName string, policyName string) error {
	_, err := wrapper.IamClient.DeleteUserPolicy(ctx, &iam.DeleteUserPolicyInput{
		PolicyName: aws.String(policyName),
		UserName:   aws.String(userName),
	})
	if err != nil {
		log.Printf("Couldn't delete policy from user %v. Here's why: %v\n", userName, err)
	}
	return err
}



```

- For API details, see
  [DeleteUserPolicy](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.DeleteUserPolicy "https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.DeleteUserPolicy")
  in _AWS SDK for Go API Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example deletes the inline policy named `AccessToEC2Policy` that is embedded in the IAM user named `Bob`.**

```
Remove-IAMUserPolicy -PolicyName AccessToEC2Policy -UserName Bob

```

**Example 2: This example finds all of the inline polices that are embedded in the IAM user named `Theresa` and then deletes them.**

```
$inlinepols = Get-IAMUserPolicies -UserName Theresa
foreach ($pol in $inlinepols) { Remove-IAMUserPolicy -PolicyName $pol -UserName Theresa -Force}

```

- For API details, see
  [DeleteUserPolicy](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example deletes the inline policy named `AccessToEC2Policy` that is embedded in the IAM user named `Bob`.**

```
Remove-IAMUserPolicy -PolicyName AccessToEC2Policy -UserName Bob

```

**Example 2: This example finds all of the inline polices that are embedded in the IAM user named `Theresa` and then deletes them.**

```
$inlinepols = Get-IAMUserPolicies -UserName Theresa
foreach ($pol in $inlinepols) { Remove-IAMUserPolicy -PolicyName $pol -UserName Theresa -Force}

```

- For API details, see
  [DeleteUserPolicy](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

Ruby

**SDK for Ruby**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/iam#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/iam#code-examples").

```
  # Deletes a user and their associated resources
  #
  # @param user_name [String] The name of the user to delete
  def delete_user(user_name)
    user = @iam_client.list_access_keys(user_name: user_name).access_key_metadata
    user.each do |key|
      @iam_client.delete_access_key({ access_key_id: key.access_key_id, user_name: user_name })
      @logger.info("Deleted access key #{key.access_key_id} for user '#{user_name}'.")
    end

    @iam_client.delete_user(user_name: user_name)
    @logger.info("Deleted user '#{user_name}'.")
  rescue Aws::IAM::Errors::ServiceError => e
    @logger.error("Error deleting user '#{user_name}': #{e.message}")
  end


```

- For API details, see
  [DeleteUserPolicy](../../../goto/SdkForRubyV3/iam-2010-05-08/DeleteUserPolicy.md "../../../goto/SdkForRubyV3/iam-2010-05-08/DeleteUserPolicy.md")
  in _AWS SDK for Ruby API Reference_.

Rust

**SDK for Rust**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/iam#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/iam#code-examples").

```
pub async fn delete_user_policy(
    client: &iamClient,
    user: &User,
    policy_name: &str,
) -> Result<(), SdkError<DeleteUserPolicyError>> {
    client
        .delete_user_policy()
        .user_name(user.user_name())
        .policy_name(policy_name)
        .send()
        .await?;

    Ok(())
}


```

- For API details, see
  [DeleteUserPolicy](https://docs.rs/aws-sdk-iam/latest/aws_sdk_iam/client/struct.Client.html#method.delete_user_policy "https://docs.rs/aws-sdk-iam/latest/aws_sdk_iam/client/struct.Client.html#method.delete_user_policy")
  in _AWS SDK for Rust API reference_.

Swift

**SDK for Swift**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/iam#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/iam#code-examples").

```
import AWSIAM
import AWSS3


    func deleteUserPolicy(user: IAMClientTypes.User, policyName: String) async throws {
        let input = DeleteUserPolicyInput(
            policyName: policyName,
            userName: user.userName
        )
        do {
            _ = try await iamClient.deleteUserPolicy(input: input)
        } catch {
            print("ERROR: deleteUserPolicy:", dump(error))
            throw error
        }
    }



```

- For API details, see
  [DeleteUserPolicy](<https://sdk.amazonaws.com/swift/api/awsiam/latest/documentation/awsiam/iamclient/deleteuserpolicy(input:)> "https://sdk.amazonaws.com/swift/api/awsiam/latest/documentation/awsiam/iamclient/deleteuserpolicy(input:)")
  in _AWS SDK for Swift API reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
