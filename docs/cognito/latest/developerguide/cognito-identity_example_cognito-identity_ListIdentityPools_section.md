# Use `ListIdentityPools` with an AWS SDK or CLI

The following code examples show how to use `ListIdentityPools`.

CLI

**AWS CLI**

**To list identity pools**

This example lists identity pools. There s a maximum of 20 identities listed.

Command:

```
`aws cognito-identity list-identity-pools --max-results `20``

```

Output:

```
{
  "IdentityPools": [
      {
          "IdentityPoolId": "us-west-2:11111111-1111-1111-1111-111111111111",
          "IdentityPoolName": "MyIdentityPool"
      },
      {
          "IdentityPoolId": "us-west-2:11111111-1111-1111-1111-111111111111",
          "IdentityPoolName": "AnotherIdentityPool"
      },
      {
          "IdentityPoolId": "us-west-2:11111111-1111-1111-1111-111111111111",
          "IdentityPoolName": "IdentityPoolRegionA"
      }
  ]
}
```

- For API details, see
  [ListIdentityPools](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/list-identity-pools.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/list-identity-pools.html")
  in _AWS CLI Command Reference_.

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/cognito#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/cognito#code-examples").

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.cognitoidentity.CognitoIdentityClient;
import software.amazon.awssdk.services.cognitoidentity.model.ListIdentityPoolsRequest;
import software.amazon.awssdk.services.cognitoidentity.model.ListIdentityPoolsResponse;
import software.amazon.awssdk.services.cognitoidentityprovider.model.CognitoIdentityProviderException;

/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */
public class ListIdentityPools {
    public static void main(String[] args) {
        CognitoIdentityClient cognitoClient = CognitoIdentityClient.builder()
                .region(Region.US_EAST_1)
                .build();

        listIdPools(cognitoClient);
        cognitoClient.close();
    }

    public static void listIdPools(CognitoIdentityClient cognitoClient) {
        try {
            ListIdentityPoolsRequest poolsRequest = ListIdentityPoolsRequest.builder()
                    .maxResults(15)
                    .build();

            ListIdentityPoolsResponse response = cognitoClient.listIdentityPools(poolsRequest);
            response.identityPools().forEach(pool -> {
                System.out.println("Pool ID: " + pool.identityPoolId());
                System.out.println("Pool name: " + pool.identityPoolName());
            });

        } catch (CognitoIdentityProviderException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
}


```

- For API details, see
  [ListIdentityPools](../../../goto/SdkForJavaV2/cognito-identity-2014-06-30/ListIdentityPools.md "../../../goto/SdkForJavaV2/cognito-identity-2014-06-30/ListIdentityPools.md")
  in _AWS SDK for Java 2.x API Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: Retrieves a list of existing Identity Pools.**

```
Get-CGIIdentityPoolList

```

**Output:**

```
IdentityPoolId                                                     IdentityPoolName
--------------                                                     ----------------
us-east-1:0de2af35-2988-4d0b-b22d-EXAMPLEGUID1                     CommonTests1
us-east-1:118d242d-204e-4b88-b803-EXAMPLEGUID2                     Tests2
us-east-1:15d49393-ab16-431a-b26e-EXAMPLEGUID3                     CommonTests13
```

- For API details, see
  [ListIdentityPools](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: Retrieves a list of existing Identity Pools.**

```
Get-CGIIdentityPoolList

```

**Output:**

```
IdentityPoolId                                                     IdentityPoolName
--------------                                                     ----------------
us-east-1:0de2af35-2988-4d0b-b22d-EXAMPLEGUID1                     CommonTests1
us-east-1:118d242d-204e-4b88-b803-EXAMPLEGUID2                     Tests2
us-east-1:15d49393-ab16-431a-b26e-EXAMPLEGUID3                     CommonTests13
```

- For API details, see
  [ListIdentityPools](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

Swift

**SDK for Swift**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/cognito-identity/FindOrCreateIdentityPool#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/cognito-identity/FindOrCreateIdentityPool#code-examples").

```
import AWSCognitoIdentity


    /// Return the ID of the identity pool with the specified name.
    ///
    /// - Parameters:
    ///   - name: The name of the identity pool whose ID should be returned.
    ///
    /// - Returns: A string containing the ID of the specified identity pool
    ///   or `nil` on error or if not found.
    ///
    func getIdentityPoolID(name: String) async throws -> String? {
        let listPoolsInput = ListIdentityPoolsInput(maxResults: 25)
        // Use "Paginated" to get all the objects.
        // This lets the SDK handle the 'nextToken' field in "ListIdentityPoolsOutput".
        let pages = cognitoIdentityClient.listIdentityPoolsPaginated(input: listPoolsInput)

        do {
            for try await page in pages {
                guard let identityPools = page.identityPools else {
                    print("ERROR: listIdentityPoolsPaginated returned nil contents.")
                    continue
                }

                /// Read pages of identity pools from Cognito until one is found
                /// whose name matches the one specified in the `name` parameter.
                /// Return the matching pool's ID.

                for pool in identityPools {
                    if pool.identityPoolName == name {
                        return pool.identityPoolId!
                    }
                }
            }
        } catch {
            print("ERROR: getIdentityPoolID:", dump(error))
            throw error
        }

        return nil
    }



```

Get the ID of an existing identity pool or create it if it doesn't already exist.

```
import AWSCognitoIdentity


    /// Return the ID of the identity pool with the specified name.
    ///
    /// - Parameters:
    ///   - name: The name of the identity pool whose ID should be returned
    ///
    /// - Returns: A string containing the ID of the specified identity pool.
    ///   Returns `nil` if there's an error or if the pool isn't found.
    ///
    public func getOrCreateIdentityPoolID(name: String) async throws -> String? {
        // See if the pool already exists. If it doesn't, create it.

        do {
            guard let poolId = try await getIdentityPoolID(name: name) else {
                return try await createIdentityPool(name: name)
            }

            return poolId
        } catch {
            print("ERROR: getOrCreateIdentityPoolID:", dump(error))
            throw error
        }
    }



```

- For more information, see [AWS SDK for Swift developer guide](../../../sdk-for-swift/latest/developer-guide/getting-started.md "../../../sdk-for-swift/latest/developer-guide/getting-started.md").
- For API details, see
  [ListIdentityPools](<https://sdk.amazonaws.com/swift/api/awscognitoidentity/latest/documentation/awscognitoidentity/cognitoidentityclient/listidentitypools(input:)> "https://sdk.amazonaws.com/swift/api/awscognitoidentity/latest/documentation/awscognitoidentity/cognitoidentityclient/listidentitypools(input:)")
  in _AWS SDK for Swift API reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
