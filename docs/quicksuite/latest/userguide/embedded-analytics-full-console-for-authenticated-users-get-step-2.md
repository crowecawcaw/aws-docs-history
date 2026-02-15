# Step 2: Get the URL with the authentication code attached

###### Important

Amazon Quick Sight has new APIs for embedding analytics:
`GenerateEmbedUrlForAnonymousUser` and
`GenerateEmbedUrlForRegisteredUser`.

You can still use the `GetDashboardEmbedUrl` and
`GetSessionEmbedUrl` APIs to embed dashboards and the
Amazon Quick Sight console, but they do not contain the latest embedding
capabilities. For the latest up-to-date embedding experience, see [Embedding Amazon Quick Sight analytics into your
applications](../../../quicksight/latest/user/embedding-overview.md "../../../quicksight/latest/user/embedding-overview.md").

In the following section, you can find out how to authenticate your user and get
the embeddable console session URL on your application server.

When a user accesses your app, the app assumes the IAM role on the user's
behalf. Then it adds the user to Amazon Quick Sight, if that user doesn't already
exist. Next, it passes an identifier as the unique role session ID.

Performing the described steps ensures that each viewer of the console session is
uniquely provisioned in Amazon Quick Sight. It also enforces per-user settings, such
as the row-level security and dynamic defaults for parameters.

The following examples perform the IAM authentication on the user's behalf. This
code runs on your app server.

Java

```
import com.amazonaws.auth.AWSCredentials;
import com.amazonaws.auth.BasicAWSCredentials;
import com.amazonaws.auth.AWSCredentialsProvider;
import com.amazonaws.regions.Regions;
import com.amazonaws.services.quicksight.AmazonQuickSight;
import com.amazonaws.services.quicksight.AmazonQuickSightClientBuilder;
import com.amazonaws.services.quicksight.model.GetSessionEmbedUrlRequest;
import com.amazonaws.services.quicksight.model.GetSessionEmbedUrlResult;

/**
 * Class to call QuickSight AWS SDK to get url for session embedding.
 */
public class GetSessionEmbedUrlQSAuth {

    private final AmazonQuickSight quickSightClient;

    public GetSessionEmbedUrlQSAuth() {
        this.quickSightClient = AmazonQuickSightClientBuilder
                .standard()
                .withRegion(Regions.US_EAST_1.getName())
                .withCredentials(new AWSCredentialsProvider() {
                                     @Override
                                     public AWSCredentials getCredentials() {
                                         // provide actual IAM access key and secret key here
                                         return new BasicAWSCredentials("access-key", "secret-key");
                                     }

                                     @Override
                                     public void refresh() {}
                                 }
                )
                .build();
    }

    public String getQuicksightEmbedUrl(
            final String accountId, // YOUR AWS ACCOUNT ID
            final String userArn // REGISTERED USER ARN TO USE FOR EMBEDDING. REFER TO GETEMBEDURL SECTION IN DEV PORTAL TO FIND OUT HOW TO GET USER ARN FOR A QUICKSIGHT USER
    ) throws Exception {
        GetSessionEmbedUrlRequest getSessionEmbedUrlRequest = new GetSessionEmbedUrlRequest()
                .withAwsAccountId(accountId)
                .withEntryPoint("/start")
                .withUserArn(userArn);

        GetSessionEmbedUrlResult sessionEmbedUrl = quickSightClient.getSessionEmbedUrl(getSessionEmbedUrlRequest);

        return sessionEmbedUrl.getEmbedUrl();
    }
}
```

JavaScript

```
global.fetch = require('node-fetch');
const AWS = require('aws-sdk');

function getSessionEmbedURL(
    accountId, // YOUR AWS ACCOUNT ID
    userArn, // REGISTERED USER ARN TO USE FOR EMBEDDING. REFER TO GETEMBEDURL SECTION IN DEV PORTAL TO FIND OUT HOW TO GET USER ARN FOR A QUICKSIGHT USER
    getEmbedUrlCallback, // GETEMBEDURL SUCCESS CALLBACK METHOD
    errorCallback // GETEMBEDURL ERROR CALLBACK METHOD
    ) {
    const getSessionParams = {
        AwsAccountId: accountId,
        EntryPoint: "/start",
        UserArn: userArn,
        SessionLifetimeInMinutes: 600,
    };

    const quicksightGetSession = new AWS.QuickSight({
        region: process.env.AWS_REGION,
    });

    quicksightGetSession.getSessionEmbedUrl(getSessionParams, function(err, data) {
        if (err) {
            console.log(err, err.stack);
            errorCallback(err);
        } else {
            const result = {
                "statusCode": 200,
                "headers": {
                    "Access-Control-Allow-Origin": "*", // USE YOUR WEBSITE DOMAIN TO SECURE ACCESS TO GETEMBEDURL API
                    "Access-Control-Allow-Headers": "Content-Type"
                },
                "body": JSON.stringify(data),
                "isBase64Encoded": false
            }
            getEmbedUrlCallback(result);
        }
    });
}
```

Python3

```
import json
import boto3
from botocore.exceptions import ClientError
import time

# Create QuickSight and STS clients
qs = boto3.client('quicksight',region_name='us-east-1')
sts = boto3.client('sts')

# Function to generate embedded URL
# accountId: YOUR AWS ACCOUNT ID
# userArn: REGISTERED USER ARN TO USE FOR EMBEDDING. REFER TO GETEMBEDURL SECTION IN DEV PORTAL TO FIND OUT HOW TO GET USER ARN FOR A QUICKSIGHT USER
def getSessionEmbedURL(accountId, userArn):
    try:
        response = qs.get_session_embed_url(
            AwsAccountId = accountId,
            EntryPoint = "/start",
            UserArn = userArn,
            SessionLifetimeInMinutes = 600
        )

        return {
            'statusCode': 200,
            'headers': {"Access-Control-Allow-Origin": "*", "Access-Control-Allow-Headers": "Content-Type"},
            'body': json.dumps(response),
            'isBase64Encoded':  bool('false')
        }
    except ClientError as e:
        print(e)
        return "Error generating embeddedURL: " + str(e)
```

Node.js
The following example shows the JavaScript (Node.js) that you can use
on the app server to get the URL for the embedded console session. You
can use this URL in your website or app to display the console session.

###### Example

```
const AWS = require('aws-sdk');
            const https = require('https');

            var quicksight = new AWS.Service({
                apiConfig: require('./quicksight-2018-04-01.min.json'),
                region: 'us-east-1',
            });

            quicksight.GetSessionEmbedUrl({
                'AwsAccountId': '`111122223333`',
                'EntryPoint': '`https://url-for-console-page-to-open`',
                'SessionLifetimeInMinutes': `600`,
                'UserArn': '`USER_ARN`'

            }, function(err, data) {
                console.log('Errors: ');
                console.log(err);
                console.log('Response: ');
                console.log(data);
            });
```

###### Example

```
//The URL returned is over 900 characters. For this example, we've shortened the string for
            //readability and added ellipsis to indicate that it's incomplete.
                                { Status: 200,
              EmbedUrl: 'https://dashboards.example.com/embed/620bef10822743fab329fb3751187d2d…
              RequestId: '7bee030e-f191-45c4-97fe-d9faf0e03713' }
```

.NET/C#
The following example shows the .NET/C# code that you can use on the
app server to get the URL for the embedded console session. You can use
this URL in your website or app to display the console.

###### Example

```

            var client = new AmazonQuickSightClient(
                AccessKey,
                SecretAccessKey,
                sessionToken,
                Amazon.RegionEndpoint.USEast1);
            try
            {
                Console.WriteLine(
                    client.GetSessionEmbedUrlAsync(new GetSessionEmbedUrlRequest
                    {
                'AwsAccountId': '`111122223333`',
                'EntryPoint': '`https://url-for-console-page-to-open`',
                'SessionLifetimeInMinutes': 600,
                'UserArn': '`USER_ARN`'
                        AwsAccountId = `111122223333`,
                        EntryPoint = `https://url-for-console-page-to-open`,
                        SessionLifetimeInMinutes = `600`,
                        UserArn = '`USER_ARN`'
                    }).Result.EmbedUrl
                );
            } catch (Exception ex) {
                Console.WriteLine(ex.Message);
            }
```

AWS CLI
To assume the role, choose one of the following AWS Security Token Service (AWS STS) API
operations:

- [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") – Use this operation when you are
  using an IAM identity to assume the role.
- [AssumeRoleWithWebIdentity](../../../STS/latest/APIReference/API_AssumeRoleWithWebIdentity.md "../../../STS/latest/APIReference/API_AssumeRoleWithWebIdentity.md") – Use this
  operation when you are using a web identity provider to
  authenticate your user.
- [AssumeRoleWithSaml](../../../STS/latest/APIReference/API_AssumeRoleWithSAML.md "../../../STS/latest/APIReference/API_AssumeRoleWithSAML.md") – Use this operation when
  you are using SAML to authenticate your users.

The following example shows the CLI command to set the IAM role. The
role needs to have permissions enabled for
`quicksight:GetSessionEmbedUrl`. If you are taking a
just-in-time approach to add users when they first open
Amazon Quick Sight, the role also needs permissions enabled for
`quicksight:RegisterUser`.

```
aws sts assume-role \
     --role-arn "`arn:aws:iam::111122223333:role/embedding_quicksight_dashboard_role`" \
     --role-session-name `john.doe@example.com`
```

The `assume-role` operation returns three output
parameters: the access key, the secret key, and the session token.

###### Note

If you get an `ExpiredToken` error when calling the
`AssumeRole` operation, this is probably because the
previous `SESSION TOKEN` is still in the environment
variables. Clear this by setting the following variables:

- _AWS_ACCESS_KEY_ID_
- _AWS_SECRET_ACCESS_KEY_
- _AWS_SESSION_TOKEN_

The following example shows how to set these three parameters in the
CLI. If you are using a Microsoft Windows machine, use `set`
instead of `export`.

```
export AWS_ACCESS_KEY_ID     = "`access_key_from_assume_role`"
export AWS_SECRET_ACCESS_KEY = "`secret_key_from_assume_role`"
export AWS_SESSION_TOKEN     = "`session_token_from_assume_role`"
```

Running these commands sets the role session ID of the user visiting
your website to
`embedding_quicksight_console_session_role/john.doe@example.com`.
The role session ID is made up of the role name from
`role-arn` and the `role-session-name` value.
Using the unique role session ID for each user ensures that appropriate
permissions are set for each user. It also prevents any throttling of
user access. Throttling is a security feature that prevents the same
user from accessing Amazon Quick Sight from multiple locations.

The role session ID also becomes the user name in Amazon Quick Sight.
You can use this pattern to provision your users in Amazon Quick Sight
ahead of time, or to provision them the first time they access a console
session.

The following example shows the CLI command that you can use to
provision a user. For more information about [RegisterUser](../../../quicksight/latest/APIReference/API_RegisterUser.md "../../../quicksight/latest/APIReference/API_RegisterUser.md"), [DescribeUser](../../../quicksight/latest/APIReference/API_DescribeUser.md "../../../quicksight/latest/APIReference/API_DescribeUser.md"), and other Amazon Quick Sight API operations,
see the [Amazon Quick Sight API reference](../../../quicksight/latest/APIReference/Welcome.md "../../../quicksight/latest/APIReference/Welcome.md").

```
aws quicksight register-user \
     --aws-account-id `111122223333` \
     --namespace `default` \
     --identity-type `IAM` \
     --iam-arn "`arn:aws:iam::111122223333:role/embedding_quicksight_dashboard_role`" \
     --user-role `READER` \
     --user-name `jhnd` \
     --session-name "`john.doe@example.com`" \
     --email `john.doe@example.com` \
     --region `us-east-1` \
     --custom-permissions-name `TeamA1`
```

If the user is authenticated through Microsoft AD, you don't need to
use `RegisterUser` to set them up. Instead, they should be
automatically subscribed the first time they access Amazon Quick Sight.
For Microsoft AD users, you can use `DescribeUser` to get the
user ARN.

The first time a user accesses Amazon Quick Sight, you can also add
this user to the appropriate group. The following example shows the CLI
command to add a user to a group.

```
aws quicksight create-group-membership \
     --aws-account-id=`111122223333` \
     --namespace=`default` \
     --group-name=`financeusers` \
     --member-name="`embedding_quicksight_dashboard_role/john.doe@example.com`"
```

You now have a user of your app who is also a user of
Amazon Quick Sight, and who has access to the Amazon Quick Sight console
session.

Finally, to get a signed URL for the console session, call
`get-session-embed-url` from the app server. This returns
the embeddable console session URL. The following example shows how to
get the URL for an embedded console session using a server-side call for
users authenticated through AWS Managed Microsoft AD or Single Sign-on
(IAM Identity Center).

```
aws quicksight get-dashboard-embed-url \
     --aws-account-id `111122223333` \
     --entry-point `the-url-for--the-console-session` \
     --session-lifetime-in-minutes `600` \
     --user-arn arn:aws:quicksight:`us-east-1`:`111122223333`:user/default/`embedding_quicksight_dashboard_role`/embeddingsession
```

For more information on using this operation, see [GetSessionEmbedUrl](../../../quicksight/latest/APIReference/API_GetSessionEmbedUrl.md "../../../quicksight/latest/APIReference/API_GetSessionEmbedUrl.md"). You can use this and
other API operations in your own code.
