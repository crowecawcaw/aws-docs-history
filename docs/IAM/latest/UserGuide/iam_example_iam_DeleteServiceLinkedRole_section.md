# Use `DeleteServiceLinkedRole` with an AWS SDK or CLI

The following code examples show how to use `DeleteServiceLinkedRole`.

CLI

**AWS CLI**

**To delete a service-linked role**

The following `delete-service-linked-role` example deletes the specified service-linked role that you no longer need. The deletion happens asynchronously. You can check the status of the deletion and confirm when it is done by using the `get-service-linked-role-deletion-status` command.

```
`aws iam delete-service-linked-role \
 --role-name `AWSServiceRoleForLexBots``

```

Output:

```
{
    "DeletionTaskId": "task/aws-service-role/lex.amazonaws.com/AWSServiceRoleForLexBots/1a2b3c4d-1234-abcd-7890-abcdeEXAMPLE"
}
```

For more information, see [Using service-linked roles](using-service-linked-roles.md "using-service-linked-roles.md") in the _AWS IAM User Guide_.

- For API details, see
  [DeleteServiceLinkedRole](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-service-linked-role.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-service-linked-role.html")
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
	"log"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/service/iam"
	"github.com/aws/aws-sdk-go-v2/service/iam/types"
)

// RoleWrapper encapsulates AWS Identity and Access Management (IAM) role actions
// used in the examples.
// It contains an IAM service client that is used to perform role actions.
type RoleWrapper struct {
	IamClient *iam.Client
}



// DeleteServiceLinkedRole deletes a service-linked role.
func (wrapper RoleWrapper) DeleteServiceLinkedRole(ctx context.Context, roleName string) error {
	_, err := wrapper.IamClient.DeleteServiceLinkedRole(ctx, &iam.DeleteServiceLinkedRoleInput{
		RoleName: aws.String(roleName)},
	)
	if err != nil {
		log.Printf("Couldn't delete service-linked role %v. Here's why: %v\n", roleName, err)
	}
	return err
}



```

- For API details, see
  [DeleteServiceLinkedRole](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.DeleteServiceLinkedRole "https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.DeleteServiceLinkedRole")
  in _AWS SDK for Go API Reference_.

JavaScript

**SDK for JavaScript (v3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/iam#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/iam#code-examples").

```
import { DeleteServiceLinkedRoleCommand, IAMClient } from "@aws-sdk/client-iam";

const client = new IAMClient({});

/**
 *
 * @param {string} roleName
 */
export const deleteServiceLinkedRole = (roleName) => {
  const command = new DeleteServiceLinkedRoleCommand({ RoleName: roleName });
  return client.send(command);
};


```

- For API details, see
  [DeleteServiceLinkedRole](../../../AWSJavaScriptSDK/v3/latest/client/iam/command/DeleteServiceLinkedRoleCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/iam/command/DeleteServiceLinkedRoleCommand.md")
  in _AWS SDK for JavaScript API Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example deleted the service linked role. Please note that if the service is still using this role, then this command results in a failure.**

```
Remove-IAMServiceLinkedRole -RoleName AWSServiceRoleForAutoScaling_RoleNameEndsWithThis

```

- For API details, see
  [DeleteServiceLinkedRole](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example deleted the service linked role. Please note that if the service is still using this role, then this command results in a failure.**

```
Remove-IAMServiceLinkedRole -RoleName AWSServiceRoleForAutoScaling_RoleNameEndsWithThis

```

- For API details, see
  [DeleteServiceLinkedRole](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

Ruby

**SDK for Ruby**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/iam#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/iam#code-examples").

```
  # Deletes a service-linked role.
  #
  # @param role_name [String] The name of the role to delete.
  def delete_service_linked_role(role_name)
    response = @iam_client.delete_service_linked_role(role_name: role_name)
    task_id = response.deletion_task_id
    check_deletion_status(role_name, task_id)
  rescue Aws::Errors::ServiceError => e
    handle_deletion_error(e, role_name)
  end

  private

  # Checks the deletion status of a service-linked role
  #
  # @param role_name [String] The name of the role being deleted
  # @param task_id [String] The task ID for the deletion process
  def check_deletion_status(role_name, task_id)
    loop do
      response = @iam_client.get_service_linked_role_deletion_status(
        deletion_task_id: task_id
      )
      status = response.status
      @logger.info("Deletion of #{role_name} #{status}.")
      break if %w[SUCCEEDED FAILED].include?(status)

      sleep(3)
    end
  end

  # Handles deletion error
  #
  # @param e [Aws::Errors::ServiceError] The error encountered during deletion
  # @param role_name [String] The name of the role attempted to delete
  def handle_deletion_error(e, role_name)
    return if e.code == 'NoSuchEntity'

    @logger.error("Couldn't delete #{role_name}. Here's why:")
    @logger.error("\t#{e.code}: #{e.message}")
    raise
  end


```

- For API details, see
  [DeleteServiceLinkedRole](../../../goto/SdkForRubyV3/iam-2010-05-08/DeleteServiceLinkedRole.md "../../../goto/SdkForRubyV3/iam-2010-05-08/DeleteServiceLinkedRole.md")
  in _AWS SDK for Ruby API Reference_.

Rust

**SDK for Rust**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/iam#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/iam#code-examples").

```
pub async fn delete_service_linked_role(
    client: &iamClient,
    role_name: &str,
) -> Result<(), iamError> {
    client
        .delete_service_linked_role()
        .role_name(role_name)
        .send()
        .await?;

    Ok(())
}


```

- For API details, see
  [DeleteServiceLinkedRole](https://docs.rs/aws-sdk-iam/latest/aws_sdk_iam/client/struct.Client.html#method.delete_service_linked_role "https://docs.rs/aws-sdk-iam/latest/aws_sdk_iam/client/struct.Client.html#method.delete_service_linked_role")
  in _AWS SDK for Rust API reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
