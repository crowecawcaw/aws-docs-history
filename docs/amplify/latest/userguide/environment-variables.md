

# Using environment variables in an Amplify application
<a name="environment-variables"></a>

Environment variables are key-value pairs that you can add to your application's settings to make them available to Amplify Hosting. As a best practice, you can use environment variables to expose application configuration data. All environment variables that you add are encrypted to prevent rogue access.

Amplify enforces the following constraints on the environment variables that you create.
+ Amplify doesn't allow you to create environment variable names with an `AWS` prefix. This prefix is reserved for Amplify internal use only.
+ The value of an environment variable can't exceed 5500 characters.

**Important**  
Don't use environment variables to store secrets. For a Gen 2 app, use the **Secret management** feature in the Amplify console. For more information, see [Secrets and environment vars](https://docs.amplify.aws/react/deploy-and-host/fullstack-branching/secrets-and-vars/) in the *Amplify Documentation*. For a Gen 1 app, store secrets in an environment secret created using the AWS Systems Manager Parameter Store. For more information, see [Managing environment secrets](environment-secrets.md).

## Amplify environment variable reference
<a name="amplify-console-environment-variables"></a>

The following environment variables are accessible by default within the Amplify console.



| Variable name | Description | Example value | 
| --- | --- | --- | 
| \_BUILD\_TIMEOUT | The build timeout duration in minutes.<br />The minimum value is 5.<br />The maximum value is 120. | `30` | 
| \_LIVE\_UPDATES | The tool will be upgraded to the latest version. | `[{"name":"Amplify CLI","pkg":"@aws-amplify/cli","type":"npm","version":"latest"}]` | 
| USER\_DISABLE\_TESTS | The test step is skipped during a build. You can disable tests for all branches or specific branches in an app.<br />This environment variable is used for apps that perform tests during the build phase. For more information about setting this variable, see [Turning off tests for an Amplify application or branch](running-tests.md#disabling-tests). | `true` | 
| AWS\_APP\_ID | The app ID of the current build | `abcd1234` | 
| AWS\_BRANCH | The branch name of the current build | `main`, `develop`, `beta`, `v2.0` | 
| AWS\_BRANCH\_ARN | The branch Amazon Resource Name (ARN) of the current build | `aws:arn:amplify:us-west-2:123456789012:appname/branch/... ` | 
| AWS\_CLONE\_URL | The clone URL used to fetch the git repository contents |  `git@github.com:<user-name>/<repo-name>.git`  | 
| AWS\_COMMIT\_ID | The commit ID of the current build<br />“HEAD” for rebuilds | `abcd1234` | 
| AWS\_JOB\_ID | The job ID of the current build.<br />This includes some padding of ‘0’ so it always has the same length. | `0000000001` | 
| AWS\_PULL\_REQUEST\_ID | The pull request ID of pull request web preview build.<br />This environment variable is not available when using AWS CodeCommit as your repository provider. | `1` | 
| AWS\_PULL\_REQUEST\_SOURCE\_BRANCH | The name of the feature branch for a pull request preview being submitted to an application branch in the Amplify console. | `featureA` | 
| AWS\_PULL\_REQUEST\_DESTINATION\_BRANCH | The name of the application branch in the Amplify console that a feature branch pull request is being submitted to. | `main` | 
| AMPLIFY\_AMAZON\_CLIENT\_ID | The Amazon client ID | `123456` | 
| AMPLIFY\_AMAZON\_CLIENT\_SECRET | The Amazon client secret | `example123456` | 
| AMPLIFY\_FACEBOOK\_CLIENT\_ID | The Facebook client ID | `123456` | 
| AMPLIFY\_FACEBOOK\_CLIENT\_SECRET | The Facebook client secret | `example123456` | 
| AMPLIFY\_GOOGLE\_CLIENT\_ID | The Google client ID | `123456` | 
| AMPLIFY\_GOOGLE\_CLIENT\_SECRET | The Google client secret | `example123456` | 
| AMPLIFY\_DIFF\_DEPLOY | Enable or disable diff based frontend deployment. For more information, see [Configuring diff based frontend build and deploy](edit-build-settings.md#enable-diff-deploy). | `true` | 
| AMPLIFY\_DIFF\_DEPLOY\_ROOT | The path to use for diff based frontend deployment comparisons, relative to the root of your repository. | `dist` | 
| AMPLIFY\_DIFF\_BACKEND | Enable or disable diff based backend builds. This applies to Gen 1 apps only. For more information, see [Configuring diff based backend builds for a Gen 1 app](edit-build-settings.md#enable-diff-backend) | `true` | 
| AMPLIFY\_BACKEND\_PULL\_ONLY | Amplify manages this environment variable. This applies to Gen 1 apps only. For more information, see [Edit an existing frontend to point to a different backend](reuse-backends.md#reuse-backends-edit-existing) | `true` | 
| AMPLIFY\_BACKEND\_APP\_ID | Amplify manages this environment variable. This applies to Gen 1 apps only. For more information, see [Edit an existing frontend to point to a different backend](reuse-backends.md#reuse-backends-edit-existing) | `abcd1234` | 
| AMPLIFY\_SKIP\_BACKEND\_BUILD | If you do not have a backend section in your build specification and want to disable backend builds, set this environment variable to `true`. This applies to Gen 1 apps only. | `true` | 
| AMPLIFY\_ENABLE\_DEBUG\_OUTPUT | Set this variable to `true` to print a stack trace in the logs. This is helpful for debugging backend build errors. | `true` | 
| AMPLIFY\_MONOREPO\_APP\_ROOT | The path to use to specify the app root of a monorepo app, relative to the root of your repository. | `apps/react-app` | 
| AMPLIFY\_USERPOOL\_ID | The ID for the Amazon Cognito user pool imported for auth | `us-west-2_example` | 
| AMPLIFY\_WEBCLIENT\_ID | The ID for the app client to be used by web applications<br />The app client must be configured with access to the Amazon Cognito user pool specified by the AMPLIFY\_USERPOOL\_ID environment variable. | `123456` | 
| AMPLIFY\_NATIVECLIENT\_ID | The ID for the app client to be used by native applications<br />The app client must be configured with access to the Amazon Cognito user pool specified by the AMPLIFY\_USERPOOL\_ID environment variable. | `123456` | 
| AMPLIFY\_IDENTITYPOOL\_ID | The ID for the Amazon Cognito identity pool | `example-identitypool-id` | 
| AMPLIFY\_PERMISSIONS\_BOUNDARY\_ARN | The ARN for the IAM policy to use as a permissions boundary that applies to all IAM roles created by Amplify. | `arn:aws:iam::123456789012:policy/example-policy` | 
| AMPLIFY\_DESTRUCTIVE\_UPDATES | Set this environment variable to true to allow a GraphQL API to be updated with schema operations that can potentially cause data loss. | `true` | 

**Note**  
The `AMPLIFY_AMAZON_CLIENT_ID` and `AMPLIFY_AMAZON_CLIENT_SECRET` environment variables are OAuth tokens, not an AWS access key and secret key. 

## Frontend framework environment variables
<a name="frontend-framework-environment-variables"></a>

If you are developing your app with a frontend framework that supports its own environment variables, it is important to understand that these are not the same as the environment variables you configure in the Amplify console. For example, React (prefixed REACT\_APP) and Gatsby (prefixed GATSBY), enable you to create runtime environment variables that those frameworks automatically bundle into your frontend production build. To understand the effects of using these environment variables to store values, refer to the documentation for the frontend framework you are using.

Storing sensitive values, such as API keys, inside these frontend framework prefixed environment variables is not a best practice and is highly discouraged.