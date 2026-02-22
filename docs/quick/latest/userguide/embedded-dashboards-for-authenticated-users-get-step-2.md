# Step 2: Get

the URL with the authentication code attached

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
the embeddable dashboard URL on your application server.

When a user accesses your app, the app assumes the IAM role on the user's
behalf. Then it adds the user to Amazon Quick Sight, if that user doesn't already
exist. Next, it passes an identifier as the unique role session ID.

Performing the described steps ensures that each viewer of the dashboard is
uniquely provisioned in Amazon Quick Sight. It also enforces per-user settings, such
as the row-level security and dynamic defaults for parameters.

The following examples perform the IAM authentication on the user's behalf. This
code runs on your app server.

Java

```
import com.amazonaws.auth.AWSCredentials;
import com.amazonaws.auth.AWSStaticCredentialsProvider;
import com.amazonaws.auth.BasicSessionCredentials;
import com.amazonaws.auth.BasicAWSCredentials;
import com.amazonaws.auth.AWSCredentialsProvider;
import com.amazonaws.regions.Regions;
import com.amazonaws.services.quicksight.AmazonQuickSight;
import com.amazonaws.services.quicksight.AmazonQuickSightClientBuilder;
import com.amazonaws.services.quicksight.model.GetDashboardEmbedUrlRequest;
import com.amazonaws.services.quicksight.model.GetDashboardEmbedUrlResult;
import com.amazonaws.services.securitytoken.AWSSecurityTokenService;
import com.amazonaws.services.securitytoken.model.AssumeRoleRequest;
import com.amazonaws.services.securitytoken.model.AssumeRoleResult;

/**
 * Class to call QuickSight AWS SDK to get url for dashboard embedding.
 */
public class GetQuicksightEmbedUrlIAMAuth {

    private static String IAM = "IAM";

    private final AmazonQuickSight quickSightClient;

    private final AWSSecurityTokenService awsSecurityTokenService;

    public GetQuicksightEmbedUrlIAMAuth(final AWSSecurityTokenService awsSecurityTokenService) {
        this.quickSightClient = AmazonQuickSightClientBuilder
                .standard()
                .withRegion(Regions.`US_EAST_1`.getName())
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
        this.awsSecurityTokenService = awsSecurityTokenService;
    }

    public String getQuicksightEmbedUrl(
            final String accountId, // YOUR AWS ACCOUNT ID
            final String dashboardId, // YOUR DASHBOARD ID TO EMBED
            final String openIdToken, // TOKEN TO ASSUME ROLE WITH ROLEARN
            final String roleArn, // IAM USER ROLE TO USE FOR EMBEDDING
            final String sessionName, // SESSION NAME FOR THE ROLEARN ASSUME ROLE
            final boolean resetDisabled, // OPTIONAL PARAMETER TO ENABLE DISABLE RESET BUTTON IN EMBEDDED DASHBAORD
            final boolean undoRedoDisabled // OPTIONAL PARAMETER TO ENABLE DISABLE UNDO REDO BUTTONS IN EMBEDDED DASHBAORD
    ) throws Exception {
        AssumeRoleRequest request = new AssumeRoleRequest()
                .withRoleArn(roleArn)
                .withRoleSessionName(sessionName)
                .withTokenCode(openIdToken)
                .withDurationSeconds(3600);
        AssumeRoleResult assumeRoleResult = awsSecurityTokenService.assumeRole(request);

        AWSCredentials temporaryCredentials = new BasicSessionCredentials(
                assumeRoleResult.getCredentials().getAccessKeyId(),
                assumeRoleResult.getCredentials().getSecretAccessKey(),
                assumeRoleResult.getCredentials().getSessionToken());
        AWSStaticCredentialsProvider awsStaticCredentialsProvider = new AWSStaticCredentialsProvider(temporaryCredentials);

        GetDashboardEmbedUrlRequest getDashboardEmbedUrlRequest = new GetDashboardEmbedUrlRequest()
                .withDashboardId(dashboardId)
                .withAwsAccountId(accountId)
                .withIdentityType(IAM)
                .withResetDisabled(resetDisabled)
                .withUndoRedoDisabled(undoRedoDisabled)
                .withRequestCredentialsProvider(awsStaticCredentialsProvider);

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
    openIdToken, // TOKEN TO ASSUME ROLE WITH ROLEARN
    roleArn, // IAM USER ROLE TO USE FOR EMBEDDING
    sessionName, // SESSION NAME FOR THE ROLEARN ASSUME ROLE
    resetDisabled, // OPTIONAL PARAMETER TO ENABLE DISABLE RESET BUTTON IN EMBEDDED DASHBAORD
    undoRedoDisabled, // OPTIONAL PARAMETER TO ENABLE DISABLE UNDO REDO BUTTONS IN EMBEDDED DASHBAORD
    getEmbedUrlCallback, // GETEMBEDURL SUCCESS CALLBACK METHOD
    errorCallback // GETEMBEDURL ERROR CALLBACK METHOD
    ) {
    const stsClient = new AWS.STS();
    let stsParams = {
        RoleSessionName: sessionName,
        WebIdentityToken: openIdToken,
        RoleArn: roleArn
    }

    stsClient.assumeRoleWithWebIdentity(stsParams, function(err, data) {
        if (err) {
            console.log('Error assuming role');
            console.log(err, err.stack);
            errorCallback(err);
        } else {
            const getDashboardParams = {
                AwsAccountId: accountId,
                DashboardId: dashboardId,
                IdentityType: 'IAM',
                ResetDisabled: resetDisabled,
                SessionLifetimeInMinutes: 600,
                UndoRedoDisabled: undoRedoDisabled
            };

            const quicksightGetDashboard = new AWS.QuickSight({
                region: process.env.`AWS_REGION`,
                credentials: {
                    accessKeyId: data.Credentials.AccessKeyId,
                    secretAccessKey: data.Credentials.SecretAccessKey,
                    sessionToken: data.Credentials.SessionToken,
                    expiration: data.Credentials.Expiration
                }
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
    });
}
```

Python3

```
import json
import boto3
from botocore.exceptions import ClientError

# Create QuickSight and STS clients
qs = boto3.client('quicksight',region_name='us-east-1')
sts = boto3.client('sts')

# Function to generate embedded URL
# accountId: YOUR AWS ACCOUNT ID
# dashboardId: YOUR DASHBOARD ID TO EMBED
# openIdToken: TOKEN TO ASSUME ROLE WITH ROLEARN
# roleArn: IAM USER ROLE TO USE FOR EMBEDDING
# sessionName: SESSION NAME FOR THE ROLEARN ASSUME ROLE
# resetDisabled: PARAMETER TO ENABLE DISABLE RESET BUTTON IN EMBEDDED DASHBAORD
# undoRedoDisabled: PARAMETER TO ENABLE DISABLE UNDO REDO BUTTONS IN EMBEDDED DASHBAORD
def getDashboardURL(accountId, dashboardId, openIdToken, roleArn, sessionName, resetDisabled, undoRedoDisabled):
    try:
        assumedRole = sts.assume_role(
            RoleArn = roleArn,
            RoleSessionName = sessionName,
            WebIdentityToken = openIdToken
        )
    except ClientError as e:
        return "Error assuming role: " + str(e)
    else:
        assumedRoleSession = boto3.Session(
            aws_access_key_id = assumedRole['Credentials']['AccessKeyId'],
            aws_secret_access_key = assumedRole['Credentials']['SecretAccessKey'],
            aws_session_token = assumedRole['Credentials']['SessionToken'],
        )
        try:
            quickSight = assumedRoleSession.client('quicksight',region_name='`us-east-1`')

            response = quickSight.get_dashboard_embed_url(
                 AwsAccountId = accountId,
                 DashboardId = dashboardId,
                 IdentityType = 'IAM',
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
                'DashboardId': '1c1fe111-e2d2-3b30-44ef-a0e111111cde',
                'IdentityType': 'IAM',
                'ResetDisabled': true,
                'SessionLifetimeInMinutes': 100,
                'UndoRedoDisabled': false,
                'StatePersistenceEnabled': true

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
                        DashboardId = `"1c1fe111-e2d2-3b30-44ef-a0e111111cde"`,
                        IdentityType = EmbeddingIdentityType.IAM,
                        ResetDisabled = true,
                        SessionLifetimeInMinutes = 100,
                        UndoRedoDisabled = false,
                        StatePersistenceEnabled = true
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
`quicksight:GetDashboardEmbedURL`. If you are taking a
just-in-time approach to add users when they first open a dashboard, the
role also needs permissions enabled for
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
`embedding_quicksight_dashboard_role/john.doe@example.com`.
The role session ID is made up of the role name from
`role-arn` and the `role-session-name` value.
Using the unique role session ID for each user ensures that appropriate
permissions are set for each user. It also prevents any throttling of
user access. _Throttling_ is a security
feature that prevents the same user from accessing Amazon Quick Sight
from multiple locations.

The role session ID also becomes the user name in Amazon Quick Sight.
You can use this pattern to provision your users in Amazon Quick Sight
ahead of time, or to provision them the first time they access the
dashboard.

The following example shows the CLI command that you can use to
provision a user. For more information about [RegisterUser](../../../quicksight/latest/APIReference/API_RegisterUser.md "../../../quicksight/latest/APIReference/API_RegisterUser.md"), [DescribeUser](../../../quicksight/latest/APIReference/API_DescribeUser.md "../../../quicksight/latest/APIReference/API_DescribeUser.md"), and other Amazon Quick Sight API operations,
see the [Amazon Quick Sight API reference](../../../quicksight/latest/APIReference/Welcome.md "../../../quicksight/latest/APIReference/Welcome.md").

```
aws quicksight register-user \
     --aws-account-id `111122223333` \
     --namespace default \
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
this user to the group that the dashboard is shared with. The following
example shows the CLI command to add a user to a group.

```
aws quicksight create-group-membership \
     --aws-account-id=`111122223333` \
     --namespace=default \
     --group-name=`financeusers` \
     --member-name="`embedding_quicksight_dashboard_role/john.doe@example.com`"
```

You now have a user of your app who is also a user of
Amazon Quick Sight, and who has access to the dashboard.

Finally, to get a signed URL for the dashboard, call
`get-dashboard-embed-url` from the app server. This
returns the embeddable dashboard URL. The following example shows how to
get the URL for an embedded dashboard using a server-side call for users
authenticated through AWS Managed Microsoft AD or IAM Identity Center.

```
aws quicksight get-dashboard-embed-url \
     --aws-account-id `111122223333` \
     --dashboard-id `1a1ac2b2-3fc3-4b44-5e5d-c6db6778df89` \
     --identity-type `IAM` \
     --session-lifetime-in-minutes `30` \
     --undo-redo-disabled `true` \
     --reset-disabled `true` \
     --state-persistence-enabled `true` \
     --user-arn arn:aws:quicksight:us-east-1:111122223333:user/default/embedding_quicksight_dashboard_role/embeddingsession
```

For more information on using this operation, see [GetDashboardEmbedUrl](../../../quicksight/latest/APIReference/API_GetDashboardEmbedUrl.md "../../../quicksight/latest/APIReference/API_GetDashboardEmbedUrl.md"). You can use this
and other API operations in your own code.
