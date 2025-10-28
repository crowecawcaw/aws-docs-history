# Use `ConfirmForgotPassword` with an AWS SDK or CLI

The following code examples show how to use `ConfirmForgotPassword`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
context in the following code example:

- [Automatically migrate known users with a Lambda function](cognito-identity-provider_example_cross_CognitoAutoMigrateUser_section.md "cognito-identity-provider_example_cross_CognitoAutoMigrateUser_section.md")

CLI

**AWS CLI**

**To confirm a forgotten password**

This example confirms a forgotten password for username diego@example.com.

Command:

```
`aws cognito-idp confirm-forgot-password --client-id `3n4b5urk1ft4fl3mg5e62d9ado` --username=diego@example.com --password `PASSWORD` --confirmation-code `CONF_CODE``

```

- For API details, see
  [ConfirmForgotPassword](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/confirm-forgot-password.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/confirm-forgot-password.html")
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



// ConfirmForgotPassword confirms a user with a confirmation code and a new password.
func (actor CognitoActions) ConfirmForgotPassword(ctx context.Context, clientId string, code string, userName string, password string) error {
	_, err := actor.CognitoClient.ConfirmForgotPassword(ctx, &cognitoidentityprovider.ConfirmForgotPasswordInput{
		ClientId:         aws.String(clientId),
		ConfirmationCode: aws.String(code),
		Password:         aws.String(password),
		Username:         aws.String(userName),
	})
	if err != nil {
		var invalidPassword *types.InvalidPasswordException
		if errors.As(err, &invalidPassword) {
			log.Println(*invalidPassword.Message)
		} else {
			log.Printf("Couldn't confirm user %v. Here's why: %v", userName, err)
		}
	}
	return err
}



```

- For API details, see
  [ConfirmForgotPassword](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/cognitoidentityprovider#Client.ConfirmForgotPassword "https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/cognitoidentityprovider#Client.ConfirmForgotPassword")
  in _AWS SDK for Go API Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
