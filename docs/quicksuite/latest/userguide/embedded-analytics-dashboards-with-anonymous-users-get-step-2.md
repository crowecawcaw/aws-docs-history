# Step

2: Get the URL with the authentication code attached

###### Important

Amazon Quick Sight has new APIs for embedding analytics:
`GenerateEmbedUrlForAnonymousUser` and
`GenerateEmbedUrlForRegisteredUser`.

You can still use the `GetDashboardEmbedUrl` and
`GetSessionEmbedUrl` APIs to embed dashboards and the
Amazon Quick Sight console, but they do not contain the latest embedding
capabilities. For the latest up-to-date embedding experience, see [Embedding Amazon Quick Sight analytics into your
applications](../../../quicksight/latest/user/embedding-overview.md "../../../quicksight/latest/user/embedding-overview.md").

|                                            |
| ------------------------------------------ |
| \*_Applies<br>to:_<br>• Enterprise Edition |

|                                                     |
| --------------------------------------------------- |
| Intended audience:<br>Amazon Quick Suite developers |

In the following section, you can find how to authenticate on behalf of the
anonymous visitor and get the embeddable dashboard URL on your application server.

When a user accesses your app, the app assumes the IAM role on the user's
behalf. Then it adds the user to Amazon Quick Sight, if that user doesn't already
exist. Next, it passes an identifier as the unique role session ID.

The following examples perform the IAM authentication on the user's behalf. It
passes an identifier as the unique role session ID. This code runs on your app
server.

Java

```
import com.amazonaws.auth.AWSCredentials;
import com.amazonaws.auth.BasicAWSCredentials;
import com.amazonaws.auth.AWSCredentialsProvider;
import com.amazonaws.regions.Regions;
import com.amazonaws.services.quicksight.AmazonQuickSight;
import com.amazonaws.services.quicksight.AmazonQuickSightClientBuilder;
import com.amazonaws.services.quicksight.model.GetDashboardEmbedUrlRequest;
import com.amazonaws.services.quicksight.model.GetDashboardEmbedUrlResult;

/**
 * Class to call QuickSight AWS SDK to get url for dashboard embedding.
 */
public class GetQuicksightEmbedUrlNoAuth {

    private static String ANONYMOUS = "ANONYMOUS";

    private final AmazonQuickSight quickSightClient;

    public GetQuicksightEmbedUrlNoAuth() {
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
            final String dashboardId, // YOUR DASHBOARD ID TO EMBED
            final String addtionalDashboardIds, // ADDITIONAL DASHBOARD-1 ADDITIONAL DASHBOARD-2
            final boolean resetDisabled, // OPTIONAL PARAMETER TO ENABLE DISABLE RESET BUTTON IN EMBEDDED DASHBAORD
            final boolean undoRedoDisabled // OPTIONAL PARAMETER TO ENABLE DISABLE UNDO REDO BUTTONS IN EMBEDDED DASHBAORD
    ) throws Exception {
        GetDashboardEmbedUrlRequest getDashboardEmbedUrlRequest = new GetDashboardEmbedUrlRequest()
                .withDashboardId(dashboardId)
                .withAdditionalDashboardIds(addtionalDashboardIds)
                .withAwsAccountId(accountId)
                .withNamespace("default") // Anonymous embedding requires specifying a valid namespace for which you want the embedding url
                .withIdentityType(ANONYMOUS)
                .withResetDisabled(resetDisabled)
                .withUndoRedoDisabled(undoRedoDisabled);

        GetDashboardEmbedUrlResult dashboardEmbedUrl = quickSightClient.getDashboardEmbedUrl(getDashboardEmbedUrlRequest);

        return dashboardEmbedUrl.getEmbedUrl();
    }
}
```

JavaScript

```
global.fetch = require('node-fetch');
const AWS = require('aws-sdk');

function getDashboardEmbedURL(
    accountId, // YOUR AWS ACCOUNT ID
    dashboardId, // YOUR DASHBOARD ID TO EMBED
    additionalDashboardIds, // ADDITIONAL DASHBOARD-1 ADDITIONAL DASHBOARD-2
    quicksightNamespace, // VALID NAMESPACE WHERE YOU WANT TO DO NOAUTH EMBEDDING
    resetDisabled, // OPTIONAL PARAMETER TO ENABLE DISABLE RESET BUTTON IN EMBEDDED DASHBAORD
    undoRedoDisabled, // OPTIONAL PARAMETER TO ENABLE DISABLE UNDO REDO BUTTONS IN EMBEDDED DASHBAORD
    getEmbedUrlCallback, // GETEMBEDURL SUCCESS CALLBACK METHOD
    errorCallback // GETEMBEDURL ERROR CALLBACK METHOD
    ) {
    const getDashboardParams = {
        AwsAccountId: accountId,
        DashboardId: dashboardId,
        AdditionalDashboardIds: additionalDashboardIds,
        Namespace: quicksightNamespace,
        IdentityType: 'ANONYMOUS',
        ResetDisabled: resetDisabled,
        SessionLifetimeInMinutes: 600,
        UndoRedoDisabled: undoRedoDisabled
    };

    const quicksightGetDashboard = new AWS.QuickSight({
        region: process.env.AWS_REGION,
    });

    quicksightGetDashboard.getDashboardEmbedUrl(getDashboardParams, function(err, data) {
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
# dashboardId: YOUR DASHBOARD ID TO EMBED
# additionalDashboardIds: ADDITIONAL DASHBOARD-1 ADDITIONAL DASHBOARD-2 WITHOUT COMMAS
# quicksightNamespace: VALID NAMESPACE WHERE YOU WANT TO DO NOAUTH EMBEDDING
# resetDisabled: PARAMETER TO ENABLE DISABLE RESET BUTTON IN EMBEDDED DASHBAORD
# undoRedoDisabled: OPTIONAL PARAMETER TO ENABLE DISABLE UNDO REDO BUTTONS IN EMBEDDED DASHBAORD
def getDashboardURL(accountId, dashboardId, quicksightNamespace, resetDisabled, undoRedoDisabled):
    try:
        response = qs.get_dashboard_embed_url(
            AwsAccountId = accountId,
            DashboardId = dashboardId,
            AdditionalDashboardIds = additionalDashboardIds,
            Namespace = quicksightNamespace,
            IdentityType = 'ANONYMOUS',
            SessionLifetimeInMinutes = 600,
            UndoRedoDisabled = undoRedoDisabled,
            ResetDisabled = resetDisabled
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
on the app server to get the URL for the embedded dashboard. You can use
this URL in your website or app to display the dashboard.

###### Example

```
const AWS = require('aws-sdk');
            const https = require('https');

            var quicksight = new AWS.Service({
                apiConfig: require('./quicksight-2018-04-01.min.json'),
                region: 'us-east-1',
            });

            quicksight.getDashboardEmbedUrl({
                'AwsAccountId': '111122223333',
                'DashboardId': '`dashboard-id`',
                'AdditionalDashboardIds': '`added-dashboard-id-1 added-dashboard-id-2 added-dashboard-id-3`'
                'Namespace' : '`default`',
                'IdentityType': 'ANONYMOUS',
                'SessionLifetimeInMinutes': 100,
                'UndoRedoDisabled': false,
                'ResetDisabled': true

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
app server to get the URL for the embedded dashboard. You can use this
URL in your website or app to display the dashboard.

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
                    client.GetDashboardEmbedUrlAsync(new GetDashboardEmbedUrlRequest
                    {
                        AwsAccountId = “`111122223333`”,
                        DashboardId = `"dashboard-id"`,
                        AdditionalDashboardIds = `"added-dashboard-id-1 added-dashboard-id-2 added-dashboard-id-3"`,
                        Namespace = `default`,
                        IdentityType = IdentityType.ANONYMOUS,
                        SessionLifetimeInMinutes = 600,
                        UndoRedoDisabled = false,
                        ResetDisabled = true
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
  you are using Security Assertion Markup Language (SAML) to
  authenticate your users.

The following example shows the CLI command to set the IAM role. The
role needs to have permissions enabled for
`quicksight:GetDashboardEmbedURL`.

```
aws sts assume-role \
     --role-arn "`arn:aws:iam::`11112222333`:role/`QuickSightEmbeddingAnonymousPolicy``" \
     --role-session-name `anonymous caller`
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
`embedding_quicksight_dashboard_role/QuickSightEmbeddingAnonymousPolicy`.
The role session ID is made up of the role name from
`role-arn` and the `role-session-name` value.
Using the unique role session ID for each user ensures that appropriate
permissions are set for each visiting user. It also keeps each session
separate and distinct. If you're using an array of web servers, for
example for load balancing, and a session is reconnected to a different
server, a new session begins.

To get a signed URL for the dashboard, call
`get-dashboard-embed-url` from the app server. This
returns the embeddable dashboard URL. The following example shows how to
get the URL for an embedded dashboard using a server-side call for users
who are making anonymous visits to your web portal or app.

```
aws quicksight get-dashboard-embed-url \
     --aws-account-id `111122223333` \
     --dashboard-id `dashboard-id` \
     --additional-dashboard-ids `added-dashboard-id-1 added-dashboard-id-2 added-dashboard-id-3`
     --namespace `default-or-something-else` \
     --identity-type `ANONYMOUS` \
     --session-lifetime-in-minutes `30` \
     --undo-redo-disabled `true` \
     --reset-disabled `true` \
     --user-arn arn:aws:quicksight:`us-east-1`:`111122223333`:user/default/`QuickSightEmbeddingAnonymousPolicy`/embeddingsession
```

For more information on using this operation, see [GetDashboardEmbedUrl](../../../quicksight/latest/APIReference/API_GetDashboardEmbedUrl.md "../../../quicksight/latest/APIReference/API_GetDashboardEmbedUrl.md"). You can use this
and other API operations in your own code.
