

# Use `DescribeUserPoolClient` with an AWS SDK or CLI
<a name="cognito-identity-provider_example_cognito-identity-provider_DescribeUserPoolClient_section"></a>

The following code examples show how to use `DescribeUserPoolClient`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code examples: 
+  [Client token and Terms discovery](cognito-identity-provider_example_cognito-identity-provider_Scenario_ClientTokenAndTerms_section.md) 
+  [Getting started with user pools](cognito-identity-provider_example_cognito_identity_provider_GettingStarted_066_section.md) 

------
#### [ CLI ]

**AWS CLI**  
**To describe a user pool client**  
This example describes a user pool client.  
Command:  

```
aws cognito-idp describe-user-pool-client --user-pool-id {{us-west-2_aaaaaaaaa}} --client-id {{38fjsnc484p94kpqsnet7mpld0}}
```
Output:  

```
{
  "UserPoolClient": {
      "UserPoolId": "us-west-2_aaaaaaaaa",
      "ClientName": "MyApp",
      "ClientId": "38fjsnc484p94kpqsnet7mpld0",
      "ClientSecret": "CLIENT_SECRET",
      "LastModifiedDate": 1548108676.163,
      "CreationDate": 1548108676.163,
      "RefreshTokenValidity": 30,
      "ReadAttributes": [
          "address",
          "birthdate",
          "custom:CustomAttr1",
          "custom:CustomAttr2",
          "email",
          "email_verified",
          "family_name",
          "gender",
          "given_name",
          "locale",
          "middle_name",
          "name",
          "nickname",
          "phone_number",
          "phone_number_verified",
          "picture",
          "preferred_username",
          "profile",
          "updated_at",
          "website",
          "zoneinfo"
      ],
      "WriteAttributes": [
          "address",
          "birthdate",
          "custom:CustomAttr1",
          "custom:CustomAttr2",
          "email",
          "family_name",
          "gender",
          "given_name",
          "locale",
          "middle_name",
          "name",
          "nickname",
          "phone_number",
          "picture",
          "preferred_username",
          "profile",
          "updated_at",
          "website",
          "zoneinfo"
      ],
      "ExplicitAuthFlows": [
          "ADMIN_NO_SRP_AUTH",
          "USER_PASSWORD_AUTH"
      ],
      "AllowedOAuthFlowsUserPoolClient": false
  }
}
```
+  For API details, see [DescribeUserPoolClient](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/describe-user-pool-client.html) in *AWS CLI Command Reference*. 

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/cognito/scenarios/client_token#code-examples). 

```
    def describe_user_pool_client(
        self, user_pool_id: str, client_id: str
    ) -> dict[str, Any]:
        """
        Describes an app client in a user pool, including the client secret.

        :param user_pool_id: The ID of the user pool that contains the app client.
        :param client_id: The ID of the app client to describe.
        :return: A dictionary with the app client configuration.
        """
        try:
            response = self.cognito_idp_client.describe_user_pool_client(
                UserPoolId=user_pool_id, ClientId=client_id
            )
            client_info = response.get("UserPoolClient", dict())
            logger.info(
                "Described app client %s in user pool %s.",
                client_id,
                user_pool_id,
            )
            return client_info
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.error(
                    "The user pool %s or client %s does not exist. "
                    "Verify the stack deployed successfully and the outputs are correct.",
                    user_pool_id,
                    client_id,
                )
            raise
```
+  For API details, see [DescribeUserPoolClient](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/DescribeUserPoolClient) in *AWS SDK for Python (Boto3) API Reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.