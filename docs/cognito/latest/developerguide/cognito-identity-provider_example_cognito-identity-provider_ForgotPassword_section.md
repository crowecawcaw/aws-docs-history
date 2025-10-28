# Use `ForgotPassword` with an AWS SDK or CLI

The following code examples show how to use `ForgotPassword`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
context in the following code example:

- [Automatically migrate known users with a Lambda function](cognito-identity-provider_example_cross_CognitoAutoMigrateUser_section.md "cognito-identity-provider_example_cross_CognitoAutoMigrateUser_section.md")

CLI

**AWS CLI**

**To force a password change**

The following `forgot-password` example sends a message to jane@example.com to change their password.

```
`aws cognito-idp forgot-password --client-id `38fjsnc484p94kpqsnet7mpld0` --username `jane@example.com``

```

Output:

```
{
    "CodeDeliveryDetails": {
        "Destination": "j***@e***.com",
        "DeliveryMedium": "EMAIL",
        "AttributeName": "email"
    }
}
```

- For API details, see
  [ForgotPassword](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/forgot-password.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/forgot-password.html")
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



// ForgotPassword starts a password recovery flow for a user. This flow typically sends a confirmation code
// to the user's configured notification destination, such as email.
func (actor CognitoActions) ForgotPassword(ctx context.Context, clientId string, userName string) (*types.CodeDeliveryDetailsType, error) {
	output, err := actor.CognitoClient.ForgotPassword(ctx, &cognitoidentityprovider.ForgotPasswordInput{
		ClientId: aws.String(clientId),
		Username: aws.String(userName),
	})
	if err != nil {
		log.Printf("Couldn't start password reset for user '%v'. Here;s why: %v\n", userName, err)
	}
	return output.CodeDeliveryDetails, err
}



```

- For API details, see
  [ForgotPassword](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/cognitoidentityprovider#Client.ForgotPassword "https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/cognitoidentityprovider#Client.ForgotPassword")
  in _AWS SDK for Go API Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
