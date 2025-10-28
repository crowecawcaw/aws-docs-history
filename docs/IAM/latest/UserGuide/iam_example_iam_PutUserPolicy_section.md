# Use `PutUserPolicy` with an AWS SDK or CLI

The following code examples show how to use `PutUserPolicy`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
context in the following code example:

- [Learn the basics](iam_example_iam_Scenario_CreateUserAssumeRole_section.md "iam_example_iam_Scenario_CreateUserAssumeRole_section.md")

CLI

**AWS CLI**

**To attach a policy to an IAM user**

The following `put-user-policy` command attaches a policy to the IAM user named `Bob`.

```
`aws iam put-user-policy \
 --user-name `Bob` \
 --policy-name `ExamplePolicy` \
 --policy-document `file://AdminPolicy.json``

```

This command produces no output.

The policy is defined as a JSON document in the _AdminPolicy.json_ file. (The file name and extension do not have significance.)

For more information, see [Adding and removing IAM identity permissions](access_policies_manage-attach-detach.md "access_policies_manage-attach-detach.md") in the _AWS IAM User Guide_.

- For API details, see
  [PutUserPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/put-user-policy.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/put-user-policy.html")
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



// CreateUserPolicy adds an inline policy to a user. This example creates a policy that
// grants a list of actions on a specified role.
// PolicyDocument shows how to work with a policy document as a data structure and
// serialize it to JSON by using Go's JSON marshaler.
func (wrapper UserWrapper) CreateUserPolicy(ctx context.Context, userName string, policyName string, actions []string,
	roleArn string) error {
	policyDoc := PolicyDocument{
		Version: "2012-10-17",
		Statement: []PolicyStatement{{
			Effect:   "Allow",
			Action:   actions,
			Resource: aws.String(roleArn),
		}},
	}
	policyBytes, err := json.Marshal(policyDoc)
	if err != nil {
		log.Printf("Couldn't create policy document for %v. Here's why: %v\n", roleArn, err)
		return err
	}
	_, err = wrapper.IamClient.PutUserPolicy(ctx, &iam.PutUserPolicyInput{
		PolicyDocument: aws.String(string(policyBytes)),
		PolicyName:     aws.String(policyName),
		UserName:       aws.String(userName),
	})
	if err != nil {
		log.Printf("Couldn't create policy for user %v. Here's why: %v\n", userName, err)
	}
	return err
}



```

- For API details, see
  [PutUserPolicy](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.PutUserPolicy "https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.PutUserPolicy")
  in _AWS SDK for Go API Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example creates an inline policy named `EC2AccessPolicy` and embeds it in the IAM user `Bob`. If an inline policy with the same name already exists, then it is overwritten. The JSON policy content comes from the file `EC2AccessPolicy.json`. Note that you must use the `-Raw` parameter to successfully process the content of the JSON file.**

```
Write-IAMUserPolicy -UserName Bob -PolicyName EC2AccessPolicy -PolicyDocument (Get-Content -Raw EC2AccessPolicy.json)

```

- For API details, see
  [PutUserPolicy](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example creates an inline policy named `EC2AccessPolicy` and embeds it in the IAM user `Bob`. If an inline policy with the same name already exists, then it is overwritten. The JSON policy content comes from the file `EC2AccessPolicy.json`. Note that you must use the `-Raw` parameter to successfully process the content of the JSON file.**

```
Write-IAMUserPolicy -UserName Bob -PolicyName EC2AccessPolicy -PolicyDocument (Get-Content -Raw EC2AccessPolicy.json)

```

- For API details, see
  [PutUserPolicy](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

Ruby

**SDK for Ruby**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/iam#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/iam#code-examples").

```
  # Creates an inline policy for a specified user.
  # @param username [String] The name of the IAM user.
  # @param policy_name [String] The name of the policy to create.
  # @param policy_document [String] The JSON policy document.
  # @return [Boolean]
  def create_user_policy(username, policy_name, policy_document)
    @iam_client.put_user_policy({
                                  user_name: username,
                                  policy_name: policy_name,
                                  policy_document: policy_document
                                })
    @logger.info("Policy #{policy_name} created for user #{username}.")
    true
  rescue Aws::IAM::Errors::ServiceError => e
    @logger.error("Couldn't create policy #{policy_name} for user #{username}. Here's why:")
    @logger.error("\t#{e.code}: #{e.message}")
    false
  end


```

- For API details, see
  [PutUserPolicy](../../../goto/SdkForRubyV3/iam-2010-05-08/PutUserPolicy.md "../../../goto/SdkForRubyV3/iam-2010-05-08/PutUserPolicy.md")
  in _AWS SDK for Ruby API Reference_.

Swift

**SDK for Swift**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/iam#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/iam#code-examples").

```
import AWSIAM
import AWSS3


    func putUserPolicy(policyDocument: String, policyName: String, user: IAMClientTypes.User) async throws {
        let input = PutUserPolicyInput(
            policyDocument: policyDocument,
            policyName: policyName,
            userName: user.userName
        )
        do {
            _ = try await iamClient.putUserPolicy(input: input)
        } catch {
            print("ERROR: putUserPolicy:", dump(error))
            throw error
        }
    }



```

- For API details, see
  [PutUserPolicy](<https://sdk.amazonaws.com/swift/api/awsiam/latest/documentation/awsiam/iamclient/putuserpolicy(input:)> "https://sdk.amazonaws.com/swift/api/awsiam/latest/documentation/awsiam/iamclient/putuserpolicy(input:)")
  in _AWS SDK for Swift API reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
