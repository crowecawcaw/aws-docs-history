# Use `AttachUserPolicy` with an AWS SDK or CLI

The following code examples show how to use `AttachUserPolicy`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
context in the following code example:

- [Create read-only and read-write users](iam_example_iam_Scenario_UserPolicies_section.md "iam_example_iam_Scenario_UserPolicies_section.md")

CLI

**AWS CLI**

**To attach a managed policy to an IAM user**

The following `attach-user-policy` command attaches the AWS managed policy named `AdministratorAccess` to the IAM user named `Alice`.

```
`aws iam attach-user-policy \
 --policy-arn `arn:aws:iam::aws:policy/AdministratorAccess` \
 --user-name `Alice``

```

This command produces no output.

For more information, see [Managed policies and inline policies](access_policies_managed-vs-inline.md "access_policies_managed-vs-inline.md") in the _AWS IAM User Guide_.

- For API details, see
  [AttachUserPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/attach-user-policy.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/attach-user-policy.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example attaches the AWS managed policy named `AmazonCognitoPowerUser` to the IAM user `Bob`. The user is immediately affected by the permissions defined in the latest version of that policy.**

```
Register-IAMUserPolicy -UserName Bob -PolicyArn arn:aws:iam::aws:policy/AmazonCognitoPowerUser

```

- For API details, see
  [AttachUserPolicy](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example attaches the AWS managed policy named `AmazonCognitoPowerUser` to the IAM user `Bob`. The user is immediately affected by the permissions defined in the latest version of that policy.**

```
Register-IAMUserPolicy -UserName Bob -PolicyArn arn:aws:iam::aws:policy/AmazonCognitoPowerUser

```

- For API details, see
  [AttachUserPolicy](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/iam#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/iam#code-examples").

```
def attach_policy(user_name, policy_arn):
    """
    Attaches a policy to a user.

    :param user_name: The name of the user.
    :param policy_arn: The Amazon Resource Name (ARN) of the policy.
    """
    try:
        iam.User(user_name).attach_policy(PolicyArn=policy_arn)
        logger.info("Attached policy %s to user %s.", policy_arn, user_name)
    except ClientError:
        logger.exception("Couldn't attach policy %s to user %s.", policy_arn, user_name)
        raise




```

- For API details, see
  [AttachUserPolicy](../../../goto/boto3/iam-2010-05-08/AttachUserPolicy.md "../../../goto/boto3/iam-2010-05-08/AttachUserPolicy.md")
  in _AWS SDK for Python (Boto3) API Reference_.

Ruby

**SDK for Ruby**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/iam#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/iam#code-examples").

```
  # Attaches a policy to a user
  #
  # @param user_name [String] The name of the user
  # @param policy_arn [String] The Amazon Resource Name (ARN) of the policy
  # @return [Boolean] true if successful, false otherwise
  def attach_policy_to_user(user_name, policy_arn)
    @iam_client.attach_user_policy(
      user_name: user_name,
      policy_arn: policy_arn
    )
    true
  rescue Aws::IAM::Errors::ServiceError => e
    @logger.error("Error attaching policy to user: #{e.message}")
    false
  end


```

- For API details, see
  [AttachUserPolicy](../../../goto/SdkForRubyV3/iam-2010-05-08/AttachUserPolicy.md "../../../goto/SdkForRubyV3/iam-2010-05-08/AttachUserPolicy.md")
  in _AWS SDK for Ruby API Reference_.

Rust

**SDK for Rust**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/iam#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/iam#code-examples").

```
pub async fn attach_user_policy(
    client: &iamClient,
    user_name: &str,
    policy_arn: &str,
) -> Result<(), iamError> {
    client
        .attach_user_policy()
        .user_name(user_name)
        .policy_arn(policy_arn)
        .send()
        .await?;

    Ok(())
}


```

- For API details, see
  [AttachUserPolicy](https://docs.rs/aws-sdk-iam/latest/aws_sdk_iam/client/struct.Client.html#method.attach_user_policy "https://docs.rs/aws-sdk-iam/latest/aws_sdk_iam/client/struct.Client.html#method.attach_user_policy")
  in _AWS SDK for Rust API reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
