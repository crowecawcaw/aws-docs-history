

# Prerequisites for functions
<a name="functions-prerequisites"></a>

Before you create your first function, set up the following.
+ **A feed** – see [Step A: Create the feed in Elemental Inference](create-feed.md). You can attach a function to a feed that you create for the purpose, or to a feed that already has other features enabled.
+ **Model access in Amazon Bedrock** – if your function invokes a model, make sure that your account can invoke that model in the Region of the feed. The invocation runs in your account, so it is subject to your account's model access. Some models have prerequisites, such as a one-time use case submission for Anthropic models. The first invocation of a third-party model subscribes your account to it and needs AWS Marketplace permissions that the permissions policy in this topic doesn't grant, so invoke the model once from the Amazon Bedrock console before a function uses it. For more information, see [Request access to models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html) in the *Amazon Bedrock User Guide*. A passthrough function needs no model access.
+ **An access role on the feed** – if your function invokes a model, the feed must specify an `accessRoleArn` that Elemental Inference assumes to make the call. See [Setting up the access role](functions-prerequisites-access-role.md). A passthrough function needs no access role.
+ **A feature output on the feed** – a feed with an enabled function output must also have at least one enabled smart crop, event clipping, smart subtitles, or contextual metadata output. A function that reads `media.transcript` needs an enabled smart subtitles output on the same feed, a function that reads `media.contextual` needs an enabled contextual metadata output, and a function that reads `media.clip` needs an enabled event clipping output.
+ **Permissions to manage functions** – see [Permissions for managing functions](functions-prerequisites-caller-permissions.md).

**Topics**
+ [Setting up the access role](functions-prerequisites-access-role.md)
+ [Permissions for managing functions](functions-prerequisites-caller-permissions.md)