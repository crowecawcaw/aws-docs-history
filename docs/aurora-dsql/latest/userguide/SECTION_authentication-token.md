

# Generating an authentication token in Amazon Aurora DSQL
<a name="SECTION_authentication-token"></a>

To connect to Amazon Aurora DSQL with a SQL client, generate an authentication token to use as the password. This token is used only for authenticating the connection. After the connection is established, the connection remains valid even if the authentication token expires.

If you create an authentication token using the AWS console, the AWS CLI, or SDKs, the token automatically expires in 15 minutes by default. The maximum duration is 604,800 seconds, which is one week. To connect to Aurora DSQL from your client again, you can use the same authentication token if it hasn't expired, or you can generate a new one.

To get started with generating a token, [create an IAM policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) and [a cluster in Aurora DSQL](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/getting-started.html#getting-started-quickstart). Then use the AWS console , AWS CLI, or the AWS SDKs to generate a token.

At a minimum, you must have the IAM permissions listed in [Connecting to your cluster using IAM](authentication-authorization.md#authentication-authorization-iam-role-connect), depending on which database role you use to connect.

**Topics**
+ [Use the AWS console to generate an authentication token in Aurora DSQL](#authentication-token-console)
+ [Use AWS CloudShell to generate an authentication token in Aurora DSQL](#authentication-token-cloudshell)
+ [Use the AWS CLI to generate an authentication token in Aurora DSQL](#authentication-token-cli)
+ [Use the SDKs to generate a token in Aurora DSQL](#authentication-token-sdks)

## Use the AWS console to generate an authentication token in Aurora DSQL
<a name="authentication-token-console"></a>

Aurora DSQL authenticates users with a token rather than a password. You can generate the token from the console.

**To generate an authentication token**

1. Sign in to the AWS Management Console and open the Aurora DSQL console at [https://console.aws.amazon.com/dsql](https://console.aws.amazon.com/dsql).

1. Choose the cluster ID of the cluster for which you want to generate an authentication token. If you haven't yet created a cluster, follow the steps in [Step 1: Create an Aurora DSQL single-Region cluster](getting-started.md#getting-started-create-cluster) or [Step 4 (Optional): Create a multi-Region cluster](getting-started.md#getting-started-multi-region).

1. Choose **Connect** and then select **Get Token**.

1. Choose whether you want to connect as an `admin` or with a [custom database role](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/authentication-authorization.html#authentication-authorization-iam-role-connect).

1. Copy the generated authentication token and use it for [Access Aurora DSQL using SQL clients](accessing.md#accessing-sql-clients).

To learn more about custom database roles and IAM in Aurora DSQL, see [Authentication and authorization for Aurora DSQL](authentication-authorization.md).

## Use AWS CloudShell to generate an authentication token in Aurora DSQL
<a name="authentication-token-cloudshell"></a>

Before you can generate an authentication token using AWS CloudShell, make sure that you [Create an Aurora DSQL cluster](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/getting-started.html#getting-started-quickstart).

**To generate an authentication token using AWS CloudShell**

1. Sign in to the AWS Management Console and open the Aurora DSQL console at [https://console.aws.amazon.com/dsql](https://console.aws.amazon.com/dsql).

1. At the bottom left of the AWS console, choose AWS CloudShell.

1. Run the following command to generate an authentication token for the `admin` role. Replace {{us-east-1}} with your Region and {{your\_cluster\_endpoint}} with the endpoint of your own cluster. 
**Note**  
If you're not connecting as `admin`, use `generate-db-connect-auth-token` instead.

   ```
   aws dsql generate-db-connect-admin-auth-token \
     --expires-in 3600 \
     --region {{us-east-1}} \
     --hostname {{your_cluster_endpoint}}
   ```

   If you run into issues, see [Troubleshoot IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot.html) and [How can I troubleshoot access denied or unauthorized operation errors with an IAM policy?](https://repost.aws/knowledge-center/troubleshoot-iam-policy-issues).

1. Use the following command to use `psql` to start a connection to your cluster.

   ```
   PGSSLMODE=require \
   psql --dbname postgres \
     --username admin \
     --host cluster_endpoint
   ```

1. You should see a prompt to provide a password. Copy the token that you generated, and make sure you don't include any additional spaces or characters. Paste it into the following prompt from `psql`.

   ```
   Password for user admin: 
   ```

1. Press **Enter**. You should see a PostgreSQL prompt.

   ```
   postgres=>
   ```

   If you get an access denied error, make sure that your IAM identity has the `dsql:DbConnectAdmin` permission. If you have the permission and continue to get access deny errors, see [Troubleshoot IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot.html) and [How can I troubleshoot access denied or unauthorized operation errors with an IAM policy?](https://repost.aws/knowledge-center/troubleshoot-iam-policy-issues). 

To learn more about custom database roles and IAM in Aurora DSQL, see [Authentication and authorization for Aurora DSQL](authentication-authorization.md).

## Use the AWS CLI to generate an authentication token in Aurora DSQL
<a name="authentication-token-cli"></a>

When your cluster is `ACTIVE`, you can generate an authentication token on the CLI by using the `aws dsql` command. Use either of the following techniques:

**Note**  
Token generation is a local operation that signs the request using your current IAM credentials. It does not contact AWS to validate the credentials. If your credentials are expired or invalid, the token generation still succeeds, but the connection attempt fails. Ensure that your IAM credentials are valid before generating a token.
+ If you are connecting with the `admin` role, use the `generate-db-connect-admin-auth-token` option.
+ If you are connecting with a custom database role, use the `generate-db-connect-auth-token` option.

The following example uses the following attributes to generate an authentication token for the `admin` role.
+ {{your\_cluster\_endpoint}} – The endpoint of the cluster. It follows the format `{{your_cluster_identifier}}.dsql.{{region}}.on.aws`, as in the example `01abc2ldefg3hijklmnopqurstu.dsql.us-east-1.on.aws`.
+ {{region}} – The AWS Region, such as `us-east-2` or `us-east-1`.

The following examples set the expiration time for the token to expire in 3600 seconds (1 hour).

------
#### [ Linux and macOS ]

```
aws dsql generate-db-connect-admin-auth-token \
  --region {{region}} \
  --expires-in 3600 \
  --hostname {{your_cluster_endpoint}}
```

------
#### [ Windows ]

```
aws dsql generate-db-connect-admin-auth-token ^
  --region={{region}} ^
  --expires-in=3600 ^
  --hostname={{your_cluster_endpoint}}
```

------

## Use the SDKs to generate a token in Aurora DSQL
<a name="authentication-token-sdks"></a>

You can generate an authentication token for your cluster when it is in `ACTIVE` status. The SDK examples use the following attributes to generate an authentication token for the `admin` role:
+ {{your\_cluster\_endpoint}} (or {{yourClusterEndpoint}}) – The endpoint of your Aurora DSQL cluster. The naming format is `{{your_cluster_identifier}}.dsql.{{region}}.on.aws`, as in the example `01abc2ldefg3hijklmnopqurstu.dsql.us-east-1.on.aws`.
+ {{region}} (or {{RegionEndpoint}}) – The AWS Region in which your cluster is located, such as `us-east-2` or `us-east-1`.

------
#### [ Python SDK ]

**Tip**  
AWS recommends using the [Aurora DSQL Connector for Python](SECTION_program-with-dsql-connector-for-python.md), which handles token generation automatically.

You can generate the token in the following ways:
+ If you are connecting with the `admin` role, use `generate_db_connect_admin_auth_token`.
+ If you are connecting with a custom database role, use `generate_connect_auth_token`.

```
import boto3

def generate_token(your_cluster_endpoint, region):
    client = boto3.client("dsql", region_name=region)
    # use `generate_db_connect_auth_token` instead if you are not connecting as admin.
    token = client.generate_db_connect_admin_auth_token(your_cluster_endpoint, region)
    print(token)
    return token
```

------
#### [ C\+\+ SDK ]

You can generate the token in the following ways:
+ If you are connecting with the `admin` role, use `GenerateDBConnectAdminAuthToken`.
+ If you are connecting with a custom database role, use `GenerateDBConnectAuthToken`.

```
#include <aws/core/Aws.h>
#include <aws/dsql/DSQLClient.h>
#include <iostream>

using namespace Aws;
using namespace Aws::DSQL;

std::string generateToken(String yourClusterEndpoint, String region) {
    DSQLClientConfiguration clientConfig;
    clientConfig.region = region;
    DSQLClient client{clientConfig};
    std::string token = "";

    // If you are not using the admin role to connect, use GenerateDBConnectAuthToken instead
    const auto presignedString = client.GenerateDBConnectAdminAuthToken(yourClusterEndpoint, region);
    if (presignedString.IsSuccess()) {
        token = presignedString.GetResult();
    } else {
        std::cerr << "Token generation failed." << std::endl;
    }

    std::cout << token << std::endl;
    return token;
}

int main() {
    Aws::SDKOptions options;
    Aws::InitAPI(options);
    // Replace with your cluster endpoint and region
    std::string token = generateToken("your_cluster_endpoint.dsql.us-east-1.on.aws", "us-east-1");
    Aws::ShutdownAPI(options);
    return 0;
}
```

------
#### [ JavaScript SDK ]

**Tip**  
AWS recommends using the [Aurora DSQL Connectors for Node.js](SECTION_Node-js-connectors.md), which handle token generation automatically.

You can generate the token in the following ways:
+ If you are connecting with the `admin` role, use `getDbConnectAdminAuthToken`.
+ If you are connecting with a custom database role, use `getDbConnectAuthToken`.

```
import { DsqlSigner } from "@aws-sdk/dsql-signer";

async function generateToken(yourClusterEndpoint, region) {
  const signer = new DsqlSigner({
    hostname: yourClusterEndpoint,
    region,
  });
  try {
    // Use `getDbConnectAuthToken` if you are _not_ logging in as the `admin` user
    const token = await signer.getDbConnectAdminAuthToken();
    console.log(token);
    return token;
  } catch (error) {
      console.error("Failed to generate token: ", error);
      throw error;
  }
}
```

------
#### [ Java SDK ]

**Tip**  
AWS recommends using the [Aurora DSQL Connector for Java JDBC](SECTION_program-with-jdbc-connector.md), which handles token generation automatically.

You can generate the token in the following ways:
+ If you are connecting with the `admin` role, use `generateDbConnectAdminAuthToken`.
+ If you are connecting with a custom database role, use `generateDbConnectAuthToken`.

```
import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;
import software.amazon.awssdk.services.dsql.DsqlUtilities;
import software.amazon.awssdk.regions.Region;

public class GenerateAuthToken {
    public static String generateToken(String yourClusterEndpoint, Region region) {
        DsqlUtilities utilities = DsqlUtilities.builder()
                .region(region)
                .credentialsProvider(DefaultCredentialsProvider.builder().build())
                .build();

        // Use `generateDbConnectAuthToken` if you are _not_ logging in as `admin` user
        String token = utilities.generateDbConnectAdminAuthToken(builder -> {
            builder.hostname(yourClusterEndpoint)
                    .region(region);
        });

        System.out.println(token);
        return token;
    }
}
```

------
#### [ Rust SDK ]

**Tip**  
AWS recommends using the [Aurora DSQL Connector for Rust SQLx](SECTION_program-with-dsql-connector-for-rust-sqlx.md), which handles token generation automatically.

You can generate the token in the following ways:
+ If you are connecting with the `admin` role, use `db_connect_admin_auth_token`.
+ If you are connecting with a custom database role, use `db_connect_auth_token`.

```
use aws_config::{BehaviorVersion, Region};
use aws_sdk_dsql::auth_token::{AuthTokenGenerator, Config};

async fn generate_token(your_cluster_endpoint: String, region: String) -> String {
    let sdk_config = aws_config::load_defaults(BehaviorVersion::latest()).await;
    let signer = AuthTokenGenerator::new(
        Config::builder()
            .hostname(&your_cluster_endpoint)
            .region(Region::new(region))
            .build()
            .unwrap(),
    );

    // Use `db_connect_auth_token` if you are _not_ logging in as `admin` user
    let token = signer.db_connect_admin_auth_token(&sdk_config).await.unwrap();
    println!("{}", token);
    token.to_string()
}
```

------
#### [ Ruby SDK ]

**Tip**  
AWS recommends using the [Aurora DSQL Connector for Ruby pg](SECTION_program-with-dsql-connector-for-ruby-pg.md), which handles token generation automatically.

You can generate the token in the following ways:
+ If you are connecting with the `admin` role, use `generate_db_connect_admin_auth_token`.
+ If you are connecting with a custom database role, use `generate_db_connect_auth_token`.

```
require 'aws-sdk-dsql'

def generate_token(your_cluster_endpoint, region)
  credentials = Aws::CredentialProviderChain.new.resolve

  token_generator = Aws::DSQL::AuthTokenGenerator.new({
    :credentials => credentials
  })

  # if you're not using admin role, use generate_db_connect_auth_token instead
  token = token_generator.generate_db_connect_admin_auth_token({
    :endpoint => your_cluster_endpoint,
    :region => region
  })
end
```

------
#### [ PHP SDK ]

**Tip**  
AWS recommends using the [Aurora DSQL Connector for PHP `PDO_PGSQL`](SECTION_program-with-dsql-connector-for-php-pdo-pgsql.md), which handles token generation automatically.

You can generate the token in the following ways:
+ If you are connecting with the `admin` role, use `generateDbConnectAdminAuthToken`.
+ If you are connecting with a custom database role, use `generateDbConnectAuthToken`.

```
<?php
require 'vendor/autoload.php';

use Aws\DSQL\AuthTokenGenerator;
use Aws\Credentials\CredentialProvider;

function generateToken(string $yourClusterEndpoint, string $region): string {
    $provider = CredentialProvider::defaultProvider();
    $generator = new AuthTokenGenerator($provider);

    // Use generateDbConnectAuthToken if you are not connecting as admin
    $token = $generator->generateDbConnectAdminAuthToken($yourClusterEndpoint, $region);

    echo $token . PHP_EOL;
    return $token;
}
```

------
#### [ .NET ]

**Tip**  
AWS recommends using the [Aurora DSQL Connector for .NET Npgsql](SECTION_program-with-dsql-connector-for-dotnet-npgsql.md), which handles token generation automatically.

**Note**  
The official SDK for .NET doesn't include a built-in API call to generate an authentication token for Aurora DSQL. Instead, you must use `DSQLAuthTokenGenerator`, which is a utility class. The following code sample shows how to generate the authentication token for .NET. 

You can generate the token in the following ways:
+ If you are connecting with the `admin` role, use `DbConnectAdmin`.
+ If you are connecting with a custom database role, use `DbConnect`.

The following example uses the `DSQLAuthTokenGenerator` utility class to generate the authentication token for a user with the `admin` role. Replace {{insert-dsql-cluster-endpoint}} with your cluster endpoint.

```
using Amazon;
using Amazon.DSQL.Util;

var yourClusterEndpoint = "{{insert-dsql-cluster-endpoint}}";

// Use `DSQLAuthTokenGenerator.GenerateDbConnectAuthToken` if you are _not_ logging in as `admin` user
var token = DSQLAuthTokenGenerator.GenerateDbConnectAdminAuthToken(RegionEndpoint.USEast1, yourClusterEndpoint);

Console.WriteLine(token);
```

------
#### [ Go ]

**Tip**  
AWS recommends using the [Aurora DSQL Connector for Go pgx](SECTION_program-with-go-pgx-connector.md), which handles token generation automatically.

The AWS SDK for Go v2 provides a built-in method for generating authentication tokens in the [`github.com/aws/aws-sdk-go-v2/feature/dsql/auth`](https://github.com/aws/aws-sdk-go-v2/tree/main/feature/dsql/auth) package.
+ If you are connecting with the `admin` role, use `auth.GenerateDBConnectAdminAuthToken`.
+ If you are connecting with a custom database role, use `auth.GenerateDbConnectAuthToken`.

```
package main

import (
	"context"
	"fmt"

	"github.com/aws/aws-sdk-go-v2/config"
	"github.com/aws/aws-sdk-go-v2/feature/dsql/auth"
)

func main() {
	ctx := context.Background()

	cfg, err := config.LoadDefaultConfig(ctx, config.WithRegion("{{region}}"))
	if err != nil {
		panic(err)
	}

	// Use auth.GenerateDbConnectAuthToken for non-admin users
	token, err := auth.GenerateDBConnectAdminAuthToken(ctx, "{{yourClusterEndpoint}}", "{{region}}", cfg.Credentials)
	if err != nil {
		panic(err)
	}

	fmt.Println(token)
}
```

------