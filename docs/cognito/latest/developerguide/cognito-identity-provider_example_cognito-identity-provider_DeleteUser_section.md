

# Use `DeleteUser` with an AWS SDK or CLI
<a name="cognito-identity-provider_example_cognito-identity-provider_DeleteUser_section"></a>

The following code examples show how to use `DeleteUser`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code examples: 
+  [Automatically confirm known users with a Lambda function](cognito-identity-provider_example_cross_CognitoAutoConfirmUser_section.md) 
+  [Automatically migrate known users with a Lambda function](cognito-identity-provider_example_cross_CognitoAutoMigrateUser_section.md) 
+  [Write custom activity data with a Lambda function after Amazon Cognito user authentication](cognito-identity-provider_example_cross_CognitoCustomActivityLog_section.md) 

------
#### [ C\+\+ ]

**SDK for C\+\+**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/cognito#code-examples). 

```
        Aws::Client::ClientConfiguration clientConfig;
        // Optional: Set to the AWS Region (overrides config file).
        // clientConfig.region = "us-east-1";

    Aws::CognitoIdentityProvider::CognitoIdentityProviderClient client(clientConfig);

        Aws::CognitoIdentityProvider::Model::DeleteUserRequest request;
        request.SetAccessToken(accessToken);

        Aws::CognitoIdentityProvider::Model::DeleteUserOutcome outcome =
                client.DeleteUser(request);

        if (outcome.IsSuccess()) {
            std::cout << "The user " << userName << " was deleted."
                      << std::endl;
        }
        else {
            std::cerr << "Error with CognitoIdentityProvider::DeleteUser. "
                      << outcome.GetError().GetMessage()
                      << std::endl;
        }
```
+  For API details, see [DeleteUser](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/DeleteUser) in *AWS SDK for C\+\+ API Reference*. 

------
#### [ CLI ]

**AWS CLI**  
**To delete a user**  
This example deletes a user.  
Command:  

```
aws cognito-idp delete-user --access-token {{ACCESS_TOKEN}}
```
+  For API details, see [DeleteUser](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/delete-user.html) in *AWS CLI Command Reference*. 

------
#### [ Go ]

**SDK for Go V2**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/cognito#code-examples). 

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



// DeleteUser removes a user from the user pool.
func (actor CognitoActions) DeleteUser(ctx context.Context, userAccessToken string) error {
	_, err := actor.CognitoClient.DeleteUser(ctx, &cognitoidentityprovider.DeleteUserInput{
		AccessToken: aws.String(userAccessToken),
	})
	if err != nil {
		log.Printf("Couldn't delete user. Here's why: %v\n", err)
	}
	return err
}
```
+  For API details, see [DeleteUser](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/cognitoidentityprovider#Client.DeleteUser) in *AWS SDK for Go API Reference*. 

------
#### [ JavaScript ]

**SDK for JavaScript (v3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/cross-services/wkflw-pools-triggers#code-examples). 

```
/**
 * Delete the signed-in user. Useful for allowing a user to delete their
 * own profile.
 * @param {{ region: string, accessToken: string }} config
 * @returns {Promise<[import("@aws-sdk/client-cognito-identity-provider").DeleteUserCommandOutput | null, unknown]>}
 */
export const deleteUser = async ({ region, accessToken }) => {
  try {
    const client = new CognitoIdentityProviderClient({ region });
    const response = await client.send(
      new DeleteUserCommand({ AccessToken: accessToken }),
    );
    return [response, null];
  } catch (err) {
    return [null, err];
  }
};
```
+  For API details, see [DeleteUser](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/cognito-identity-provider/command/DeleteUserCommand) in *AWS SDK for JavaScript API Reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.