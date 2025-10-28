# Use `AdminSetUserPassword` with an AWS SDK or CLI

The following code examples show how to use `AdminSetUserPassword`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
context in the following code example:

- [Write custom activity data with a Lambda function after Amazon Cognito user authentication](cognito-identity-provider_example_cross_CognitoCustomActivityLog_section.md "cognito-identity-provider_example_cross_CognitoCustomActivityLog_section.md")

CLI

**AWS CLI**

**To set a user password as an admin**

The following `admin-set-user-password` example permanently sets the password for diego@example.com.

```
`aws cognito-idp admin-set-user-password \
 --user-pool-id `us-west-2_EXAMPLE` \
 --username `diego@example.com` \
 --password `MyExamplePassword1!` \
 --permanent`

```

This command produces no output.

For more information, see [Passwords, password recovery, and password policies](managing-users-passwords.md "managing-users-passwords.md") in the _Amazon Cognito Developer Guide_.

- For API details, see
  [AdminSetUserPassword](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-set-user-password.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-set-user-password.html")
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



// AdminSetUserPassword uses administrator credentials to set a password for a user without requiring a
// temporary password.
func (actor CognitoActions) AdminSetUserPassword(ctx context.Context, userPoolId string, userName string, password string) error {
	_, err := actor.CognitoClient.AdminSetUserPassword(ctx, &cognitoidentityprovider.AdminSetUserPasswordInput{
		Password:   aws.String(password),
		UserPoolId: aws.String(userPoolId),
		Username:   aws.String(userName),
		Permanent:  true,
	})
	if err != nil {
		var invalidPassword *types.InvalidPasswordException
		if errors.As(err, &invalidPassword) {
			log.Println(*invalidPassword.Message)
		} else {
			log.Printf("Couldn't set password for user %v. Here's why: %v\n", userName, err)
		}
	}
	return err
}



```

- For API details, see
  [AdminSetUserPassword](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/cognitoidentityprovider#Client.AdminSetUserPassword "https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/cognitoidentityprovider#Client.AdminSetUserPassword")
  in _AWS SDK for Go API Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
