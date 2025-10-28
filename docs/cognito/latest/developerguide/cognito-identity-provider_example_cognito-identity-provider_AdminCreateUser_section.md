# Use `AdminCreateUser` with an AWS SDK or CLI

The following code examples show how to use `AdminCreateUser`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
context in the following code example:

- [Write custom activity data with a Lambda function after Amazon Cognito user authentication](cognito-identity-provider_example_cross_CognitoCustomActivityLog_section.md "cognito-identity-provider_example_cross_CognitoCustomActivityLog_section.md")

CLI

**AWS CLI**

**To create a user**

The following `admin-create-user` example creates a user with the specified settings email address and phone number.

```
`aws cognito-idp admin-create-user \
 --user-pool-id `us-west-2_aaaaaaaaa` \
 --username `diego` \
 --user-attributes `Name=email,Value=diego@example.com` Name=phone_number,Value="+15555551212" \
 --message-action `SUPPRESS``

```

Output:

```
{
    "User": {
        "Username": "diego",
        "Attributes": [
            {
                "Name": "sub",
                "Value": "7325c1de-b05b-4f84-b321-9adc6e61f4a2"
            },
            {
                "Name": "phone_number",
                "Value": "+15555551212"
            },
            {
                "Name": "email",
                "Value": "diego@example.com"
            }
        ],
        "UserCreateDate": 1548099495.428,
        "UserLastModifiedDate": 1548099495.428,
        "Enabled": true,
        "UserStatus": "FORCE_CHANGE_PASSWORD"
    }
}
```

- For API details, see
  [AdminCreateUser](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-create-user.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-create-user.html")
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



// AdminCreateUser uses administrator credentials to add a user to a user pool. This method leaves the user
// in a state that requires they enter a new password next time they sign in.
func (actor CognitoActions) AdminCreateUser(ctx context.Context, userPoolId string, userName string, userEmail string) error {
	_, err := actor.CognitoClient.AdminCreateUser(ctx, &cognitoidentityprovider.AdminCreateUserInput{
		UserPoolId:     aws.String(userPoolId),
		Username:       aws.String(userName),
		MessageAction:  types.MessageActionTypeSuppress,
		UserAttributes: []types.AttributeType{{Name: aws.String("email"), Value: aws.String(userEmail)}},
	})
	if err != nil {
		var userExists *types.UsernameExistsException
		if errors.As(err, &userExists) {
			log.Printf("User %v already exists in the user pool.", userName)
			err = nil
		} else {
			log.Printf("Couldn't create user %v. Here's why: %v\n", userName, err)
		}
	}
	return err
}



```

- For API details, see
  [AdminCreateUser](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/cognitoidentityprovider#Client.AdminCreateUser "https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/cognitoidentityprovider#Client.AdminCreateUser")
  in _AWS SDK for Go API Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
