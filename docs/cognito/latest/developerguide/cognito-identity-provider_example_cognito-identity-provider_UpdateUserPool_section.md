# Use `UpdateUserPool` with an AWS SDK or CLI

The following code examples show how to use `UpdateUserPool`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
context in the following code examples:

- [Automatically confirm known users with a Lambda function](cognito-identity-provider_example_cross_CognitoAutoConfirmUser_section.md "cognito-identity-provider_example_cross_CognitoAutoConfirmUser_section.md")
- [Automatically migrate known users with a Lambda function](cognito-identity-provider_example_cross_CognitoAutoMigrateUser_section.md "cognito-identity-provider_example_cross_CognitoAutoMigrateUser_section.md")
- [Write custom activity data with a Lambda function after Amazon Cognito user authentication](cognito-identity-provider_example_cross_CognitoCustomActivityLog_section.md "cognito-identity-provider_example_cross_CognitoCustomActivityLog_section.md")

CLI

**AWS CLI**

**To update a user pool**

The following `update-user-pool` example modifies a user pool with example syntax for each of the available configuration options. To update a user pool, you must specify all previously-configured options or they will reset to a default value.

```
`aws cognito-idp update-user-pool --user-pool-id `us-west-2_EXAMPLE` \
 --policies PasswordPolicy=\{MinimumLength=6,RequireUppercase=true,RequireLowercase=true,RequireNumbers=true,RequireSymbols=true,TemporaryPasswordValidityDays=7\} \
 --deletion-protection `ACTIVE` \
 --lambda-config PreSignUp="arn:aws:lambda:us-west-2:123456789012:function:cognito-test-presignup-function",PreTokenGeneration="arn:aws:lambda:us-west-2:123456789012:function:cognito-test-pretoken-function" \
 --auto-verified-attributes `"phone_number"` `"email"` \
 --verification-message-template \{\"SmsMessage\":\"`"Your code is {####}"`\",\"EmailMessage\":\""Your code is {####}"\",\"EmailSubject\":\""Your verification code"\",\"EmailMessageByLink\":\""Click {##here##} to verify your email address."\",\"EmailSubjectByLink\":\""Your verification link"\",\"DefaultEmailOption\":\"CONFIRM_WITH_LINK\"\} \
 --sms-authentication-message "Your code is {####}" \
 --user-attribute-update-settings AttributesRequireVerificationBeforeUpdate="email","phone_number" \
 --mfa-configuration `"OPTIONAL"` \
 --device-configuration `ChallengeRequiredOnNewDevice=true,DeviceOnlyRememberedOnUserPrompt=true` \
 --email-configuration SourceArn="arn:aws:ses:us-west-2:123456789012:identity/admin@example.com",ReplyToEmailAddress="amdin+noreply@example.com",EmailSendingAccount=DEVELOPER,From="admin@amazon.com",ConfigurationSet="test-configuration-set" \
 --sms-configuration SnsCallerArn="arn:aws:iam::123456789012:role/service-role/SNS-SMS-Role",ExternalId="12345",SnsRegion="us-west-2" \
 --admin-create-user-config AllowAdminCreateUserOnly=false,InviteMessageTemplate=\{SMSMessage=\""Welcome {username}. Your confirmation code is {####}"\",EmailMessage=\""Welcome {username}. Your confirmation code is {####}"\",EmailSubject=\""Welcome to MyMobileGame"\"\} \
 --user-pool-tags "Function"="MyMobileGame","Developers"="Berlin" \
 --admin-create-user-config AllowAdminCreateUserOnly=false,InviteMessageTemplate=\{SMSMessage=\""Welcome {username}. Your confirmation code is {####}"\",EmailMessage=\""Welcome {username}. Your confirmation code is {####}"\",EmailSubject=\""Welcome to MyMobileGame"\"\} \
 --user-pool-add-ons AdvancedSecurityMode="AUDIT" \
 --account-recovery-setting RecoveryMechanisms=\[\{Priority=1,Name="verified_email"\},\{Priority=2,Name="verified_phone_number"\}\]`

```

This command produces no output.

For more information, see [Updating user pool configuration](cognito-user-pool-updating.md "cognito-user-pool-updating.md") in the _Amazon Cognito Developer Guide_.

- For API details, see
  [UpdateUserPool](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/update-user-pool.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/update-user-pool.html")
  in _AWS CLI Command Reference_.

Go

**SDK for Go V2**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/cognito#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/cognito#code-examples").

```

import (
	"context"
	"errors"
	"log"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/service/cognitoidentityprovider"
	"github.com/aws/aws-sdk-go-v2/service/cognitoidentityprovider/types"
)

type CognitoActions struct {
	CognitoClient *cognitoidentityprovider.Client
}



// Trigger and TriggerInfo define typed data for updating an Amazon Cognito trigger.
type Trigger int

const (
	PreSignUp Trigger = iota
	UserMigration
	PostAuthentication
)

type TriggerInfo struct {
	Trigger    Trigger
	HandlerArn *string
}

// UpdateTriggers adds or removes Lambda triggers for a user pool. When a trigger is specified with a `nil` value,
// it is removed from the user pool.
func (actor CognitoActions) UpdateTriggers(ctx context.Context, userPoolId string, triggers ...TriggerInfo) error {
	output, err := actor.CognitoClient.DescribeUserPool(ctx, &cognitoidentityprovider.DescribeUserPoolInput{
		UserPoolId: aws.String(userPoolId),
	})
	if err != nil {
		log.Printf("Couldn't get info about user pool %v. Here's why: %v\n", userPoolId, err)
		return err
	}
	lambdaConfig := output.UserPool.LambdaConfig
	for _, trigger := range triggers {
		switch trigger.Trigger {
		case PreSignUp:
			lambdaConfig.PreSignUp = trigger.HandlerArn
		case UserMigration:
			lambdaConfig.UserMigration = trigger.HandlerArn
		case PostAuthentication:
			lambdaConfig.PostAuthentication = trigger.HandlerArn
		}
	}
	_, err = actor.CognitoClient.UpdateUserPool(ctx, &cognitoidentityprovider.UpdateUserPoolInput{
		UserPoolId:   aws.String(userPoolId),
		LambdaConfig: lambdaConfig,
	})
	if err != nil {
		log.Printf("Couldn't update user pool %v. Here's why: %v\n", userPoolId, err)
	}
	return err
}



```

- For API details, see
  [UpdateUserPool](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/cognitoidentityprovider#Client.UpdateUserPool "https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/cognitoidentityprovider#Client.UpdateUserPool")
  in _AWS SDK for Go API Reference_.

JavaScript

**SDK for JavaScript (v3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/cross-services/wkflw-pools-triggers#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/cross-services/wkflw-pools-triggers#code-examples").

```
/**
 * Connect a Lambda function to the PreSignUp trigger for a Cognito user pool
 * @param {{ region: string, userPoolId: string, handlerArn: string }} config
 * @returns {Promise<[import("@aws-sdk/client-cognito-identity-provider").UpdateUserPoolCommandOutput | null, unknown]>}
 */
export const addPreSignUpHandler = async ({
  region,
  userPoolId,
  handlerArn,
}) => {
  try {
    const cognitoClient = new CognitoIdentityProviderClient({
      region,
    });

    const command = new UpdateUserPoolCommand({
      UserPoolId: userPoolId,
      LambdaConfig: {
        PreSignUp: handlerArn,
      },
    });

    const response = await cognitoClient.send(command);
    return [response, null];
  } catch (err) {
    return [null, err];
  }
};


```

- For API details, see
  [UpdateUserPool](../../../AWSJavaScriptSDK/v3/latest/client/cognito-identity-provider/command/UpdateUserPoolCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/cognito-identity-provider/command/UpdateUserPoolCommand.md")
  in _AWS SDK for JavaScript API Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
