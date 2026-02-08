# Receiving SaaS events from AWS Lambda function URLs in Amazon EventBridge

###### Note

In order for the Inbound Webhook to be accessible by our partners, we're creating an
Open Lambda in your AWS account that is secured at the Lambda application level by
verifying the authentication signature sent by the third-party partner. Please review
this configuration with your security team. For more information, see [Security and auth model for Lambda
function URLs](../../../lambda/latest/dg/urls-auth.md#urls-auth-none "../../../lambda/latest/dg/urls-auth.md#urls-auth-none").

Your Amazon EventBridge [event bus](eb-event-bus.md "eb-event-bus.md") can use an [AWS Lambda function URL](../../../lambda/latest/dg/lambda-urls.md "../../../lambda/latest/dg/lambda-urls.md") created by an CloudFormation
template to receive [events](eb-events.md "eb-events.md") from supported SaaS providers.
With function URLs, the event data is sent to a Lambda function. The function then converts
this data into an event that can be ingested by EventBridge and sent to an event bus for
processing. Once the event is on an event bus, you can use rules to filter the events, apply
any configured input transformations, and then route it to the correct target.

###### Note

Creating Lambda function URLs will increase your monthly costs. For more information,
see [AWS Lambda pricing](https://aws.amazon.com/lambda/pricing "https://aws.amazon.com/lambda/pricing").

To set up a connection to EventBridge, you first select the SaaS provider that you want to set up
a connection with. Then, you provide a _signing secret_ that you’ve
created with that provider, and select the EventBridge event bus to send events to. Finally, you
use an CloudFormation template and create the needed resources to complete the connection.

The following SaaS providers are currently available for use with EventBridge using Lambda function URLs:

- GitHub
- Twilio

###### Topics

- [Step 1: Create the CloudFormation stack](#create-gh-cfn-stack "#create-gh-cfn-stack")
- [Step 2: Create a GitHub webhook](#create-gh-webhook "#create-gh-webhook")
- [Set up a connection to a
  Twilio](#furls-connection-twilio "#furls-connection-twilio")
- [Update webhook secret or auth token](#furls-update-secret "#furls-update-secret")
- [Update Lambda function](#furls-update-function "#furls-update-function")
- [Available event types](#furls-event-types "#furls-event-types")
- [Quotas, error codes, and retrying delivery](#furls-quotas-errors "#furls-quotas-errors")

## Step 1: Create the CloudFormation stack

First, use the Amazon EventBridge console to create a CloudFormation stack:

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. From the navigation pane, choose **Quick starts**.
3. Under **Inbound webhooks using Lambda fURLs**, choose
   **Get started**.
4. Under **GitHub**, choose **Set
   up**.
5. Under **Step 1: Select an event bus**, select an event
   bus from the dropdown list. This event bus receives data from the Lambda
   function URL that you provide to GitHub. You can also create
   an event bus by selecting **New event bus**.
6. Under **Step 2: Set up using CloudFormation**, choose
   **New GitHub webhook**.
7. Select **I acknowledge that the Inbound Webhook I create will be
   publicly accessible.** and choose
   **Confirm**.
8. Enter a name for the stack.
9. Under parameters, verify that the correct event bus is listed, then specify
   a secure token for the **GitHubWebhookSecret**. For more information on creating a secure token, see [Setting your secret token](https://docs.github.com/en/developers/webhooks-and-events/webhooks/securing-your-webhooks#setting-your-secret-token "https://docs.github.com/en/developers/webhooks-and-events/webhooks/securing-your-webhooks#setting-your-secret-token") in the GitHub documentation.
10. Under **Capabilities and transforms**, select each of the
    following:
    - **I acknowledge that CloudFormation might create IAM
      resources.**
    - **I acknowledge that CloudFormation might create IAM resources
      with custom names.**
    - **I acknowledge that CloudFormation might require the following
      capability:
      `CAPABILITY_AUTO_EXPAND`**

11. Choose **Create stack**.

## Step 2: Create a GitHub webhook

Next, create the webhook on GitHub. You’ll need both the secure
token and the Lambda function URL you created in step 2 to complete this step. For
more information, see [Creating webhooks](https://docs.github.com/en/developers/webhooks-and-events/webhooks/creating-webhooks "https://docs.github.com/en/developers/webhooks-and-events/webhooks/creating-webhooks") in the GitHub documentation.

## Set up a connection to a

Twilio

### Step 1: Find your Twilio auth

token

To set up a connection between Twilio and EventBridge, first set up the
connection to Twilio with the auth token, or secret, for your
Twilio account. For more information, see [Auth Tokens and How To Change Them](https://support.twilio.com/hc/en-us/articles/223136027-Auth-Tokens-and-How-to-Change-Them "https://support.twilio.com/hc/en-us/articles/223136027-Auth-Tokens-and-How-to-Change-Them") in the Twilio
documentation.

### Step 2: Create the CloudFormation stack

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, choose **Quick starts**.
3. Under **Inbound webhooks using Lambda fURLs**, choose
   **Get started**.
4. Under **Twilio**, choose **Set
   up**.
5. Under **Step 1: Select and event bus**, sselect an event
   bus from the dropdown list. This event bus receives data from the Lambda
   function URL that you provide to Twilio. You can also create
   an event bus by selecting **New event bus**.
6. Under **Step 2: Set up using CloudFormation**, choose
   **New Twilio webhook**.
7. Select **I acknowledge that the Inbound Webhook I create will be
   publicly accessible.** and choose
   **Confirm**.
8. Enter a name for the stack.
9. Under parameters, verify that the correct event bus is listed, then enter
   the **TwilioWebhookSecret** that you created
   in Step 1.
10. Under **Capabilities and transforms**, select each of the
    following:
    - **I acknowledge that CloudFormation might create IAM
      resources.**
    - **I acknowledge that CloudFormation might create IAM resources
      with custom names.**
    - **I acknowledge that CloudFormation might require the following
      capability: CAPABILITY_AUTO_EXPAND**

11. Choose **Create stack**.

### Step 3: Create a Twilio

webhook

After you set up the Lambda function URL, you need to give it to Twilio so that
event data can be sent. For more information, see [Configure your public URL with Twilio](https://www.twilio.com/docs/usage/webhooks/getting-started-twilio-webhooks#configure-your-public-url-with-twilio "https://www.twilio.com/docs/usage/webhooks/getting-started-twilio-webhooks#configure-your-public-url-with-twilio") in the
Twilio documentation.

## Update webhook secret or auth token

### Update GitHub secret

###### Note

GitHub doesn’t support having two secrets at the same time. You
may experience resource downtime while the GitHub secret and the
secret in the CloudFormation stack are out of sync. GitHub messages sent
while the secrets are out of sync will fail becaue of incorrect signatures. Wait
until the GitHub and CloudFormation secrets are in sync, then try
again.

1. Create a new GitHub secret. For more information, see
   [Encrypted secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets "https://docs.github.com/en/actions/security-guides/encrypted-secrets") in the GitHub
   documentation.
2. Open the CloudFormation console at
   [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
3. From the navigation pane, choose **Stacks**.
4. Choose the stack for the webhook that includes the secret you want to update.
5. Choose **Update**.
6. Make sure **Use current template** is selected and choose **Next**.
7. Under **GitHubWebhookSecret**, clear **Use existing value**, enter the new GitHub
   secret you created in step 1, and choose **Next**.
8. Choose **Next**.
9. Choose **Update stack**.

It may take up to one hour for the secret to propagate. To reduce this downtime,
you can refresh the Lambda execution context.

### Update Twilio secret

###### Note

Twilio doesn’t support having two secrets at the same time. You
may experience resource downtime while the Twilio secret and the
secret in the CloudFormation stack are out of sync. Twilio messages sent
while the secrets are out of sync will fail because of incorrect signatures.
Wait until the Twilio and CloudFormation secrets are in sync, then
try again.

1. Create a new Twilio secret. For more information, see
   [Auth Tokens and How To Change Them](https://support.twilio.com/hc/en-us/articles/223136027-Auth-Tokens-and-How-to-Change-Them "https://support.twilio.com/hc/en-us/articles/223136027-Auth-Tokens-and-How-to-Change-Them") in the Twilio
   documentation.
2. Open the CloudFormation console at
   [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
3. From the navigation pane, choose **Stacks**.
4. Choose the stack for the webhook that includes the secret you want to update.
5. Choose **Update**.
6. Make sure **Use current template** is selected and choose **Next**.
7. Under **TwilioWebhookSecret**, clear **Use existing value**, enter the new Twilio
   secret you created in step 1, and choose **Next**.
8. Choose **Next**.
9. Choose **Update stack**.

It may take up to one hour for the secret to propagate. To reduce this downtime,
you can refresh the Lambda execution context.

## Update Lambda function

The Lambda function that's created by the CloudFormation stack creates the basic webhook. If you want to customize the Lambda function for a specific use case, such as
customized logging, use the CloudFormation console to access the function and then use the Lambda console to update the Lambda function code.

###### Access the Lambda function

1. Open the CloudFormation console at
   [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. From the navigation pane, choose **Stacks**.
3. Choose the stack for the webhook that includes the Lambda function you want to update.
4. Choose **Resources** tab.
5. To open the Lambda function in the Lambda console, under **Physical ID**, choose the ID of the Lambda function.

Now that you've accessed the Lambda function, use the Lambda console to update the function code.

###### Update the Lambda function code

1. Under **Actions**, choose **Export function**.
2. Choose **Download deployment package** and save the file to your computer.
3. Unzip the deployment package .zip file, update the `app.py` file, and zip the updated deployment package, making sure all the files in the
   original .zip file are included.
4. In the Lambda console, choose the **Code** tab.
5. Under **Code source**, choose **Upload from**.
6. Choose **.zip file**, and then choose **Upload**.
   1. In the file chooser, select the file you updated, choose **Open**, and then choose
      **Save**.

7. Under **Actions**, choose **Publish new version**.

## Available event types

The following event types are currently supported by CloudFormation event buses:

- GitHub – [All event types](https://docs.github.com/en/developers/webhooks-and-events/webhooks/webhook-events-and-payloads "https://docs.github.com/en/developers/webhooks-and-events/webhooks/webhook-events-and-payloads") are supported.
- Twilio – [Post-event
  webhooks](https://www.twilio.com/docs/chat/webhook-events "https://www.twilio.com/docs/chat/webhook-events") are supported.

## Quotas, error codes, and retrying delivery

### Quotas

The number of incoming requests to the webhook is capped by the underlying AWS services. The following table includes the relevant quotas.

| Service             | Quota                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AWS Lambda          | Default: 10 concurrent executions<br>For more information about quotas, including requesting quota increases,<br>see [Lambda quotas](../../../lambda/latest/dg/gettingstarted-limits.md "../../../lambda/latest/dg/gettingstarted-limits.md").                                                                                                                                                                                                                                                                                                             |
| AWS Secrets Manager | Default: 5,000 requests per second<br>For more information about quotas, including requesting quota increases,<br>see [AWS Secrets Manager quotas](../../../secretsmanager/latest/userguide/reference_limits.md "../../../secretsmanager/latest/userguide/reference_limits.md").<br>NoteThe number of requests per second is minimized using the [AWS Secrets Manager Python caching client](https://github.com/aws/aws-secretsmanager-caching-python#cache-configuration "https://github.com/aws/aws-secretsmanager-caching-python#cache-configuration"). |
| Amazon EventBridge  | 1 MB maximum entry size for PutEvents actions.<br>EventBridge enforces Region-based rate quotas. For more information, see [EventBridge event bus quotas](eb-quota.md#eb-limits "eb-quota.md#eb-limits").                                                                                                                                                                                                                                                                                                                                                  |

### Error codes

Each AWS service returns specific error codes when errors occur. The following table includes the relevant error codes.

| Service             | Error code                   | Description                                 |
| ------------------- | ---------------------------- | ------------------------------------------- |
| AWS Lambda          | 429 “TooManyRequestsExption” | The concurrent execution quota is exceeded. |
| AWS Secrets Manager | 500 “Internal Server Error”  | The requests per second quota is exceeded.  |
| Amazon EventBridge  | 500 “Internal Server Error”  | The rate quota is exceeded for the Region.  |

### Event redelivery

When errors happen you can retry delivery of the affected events. Each SaaS provider has different retry procedures.

#### GitHub

Use the GitHub webhooks API to check the deliver status of any webhook call and redeliver the event, if needed. For more information,
see the following GitHub documentation:

- Organization – [Redeliver a delivery for an organization webhook](https://docs.github.com/en/rest/orgs/webhooks#redeliver-a-delivery-for-an-organization-webhook "https://docs.github.com/en/rest/orgs/webhooks#redeliver-a-delivery-for-an-organization-webhook")
- Repository – [Redeliver a delivery for a repository webhook](https://docs.github.com/en/rest/webhooks/repo-deliveries#redeliver-a-delivery-for-a-repository-webhook "https://docs.github.com/en/rest/webhooks/repo-deliveries#redeliver-a-delivery-for-a-repository-webhook")
- App – [Redeliver a delivery for an app webhook](https://docs.github.com/en/rest/apps/webhooks#redeliver-a-delivery-for-an-app-webhook "https://docs.github.com/en/rest/apps/webhooks#redeliver-a-delivery-for-an-app-webhook")

#### Twilio

Twilio users can customize event retry options using connection overrides. For more information, see [Webhooks (HTTP callbacks): Connection Overrides](https://www.twilio.com/docs/usage/webhooks/webhooks-connection-overrides "https://www.twilio.com/docs/usage/webhooks/webhooks-connection-overrides") in the Twilio documentation.
