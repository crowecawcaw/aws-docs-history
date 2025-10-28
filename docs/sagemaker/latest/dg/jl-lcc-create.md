# Lifecycle configuration creation

This topic includes instructions for creating and associating a lifecycle configuration
with JupyterLab. You use the AWS Command Line Interface (AWS CLI) or the AWS Management Console to automate customization for your
JupyterLab environment.

Lifecycle configurations are shell scripts triggered by JupyterLab lifecycle events, such
as starting a new JupyterLab notebook. For more information about lifecycle configurations,
see [Lifecycle configurations with JupyterLab](jl-lcc.md "jl-lcc.md").

## Create a lifecycle configuration (AWS CLI)

Learn how to create a lifecycle configuration using the AWS Command Line Interface (AWS CLI) to automate
customization for your Studio environment.

### Prerequisites

Before you begin, complete the following prerequisites:

- Update the AWS CLI by following the steps in [Installing the current AWS CLI Version](../../../cli/latest/userguide/install-cliv1.md#install-tool-bundled "../../../cli/latest/userguide/install-cliv1.md#install-tool-bundled").
- From your local machine, run `aws configure` and provide your AWS
  credentials. For information about AWS credentials, see [Understanding and getting your AWS credentials](../../../general/latest/gr/aws-sec-cred-types.md "../../../general/latest/gr/aws-sec-cred-types.md").
- Onboard to Amazon SageMaker AI domain. For conceptual information, see [Amazon SageMaker AI domain overview](gs-studio-onboard.md "gs-studio-onboard.md"). For a
  quickstart guide, see [Use quick setup for Amazon SageMaker AI](onboard-quick-start.md "onboard-quick-start.md").

### Step 1: Create a lifecycle

configuration

The following procedure shows how to create a lifecycle configuration script that
prints `Hello World`.

###### Note

Each script can have up to **16,384
characters**.

1. From your local machine, create a file named `my-script.sh` with
   the following content:

```
#!/bin/bash
set -eux
echo 'Hello World!'
```

2. Use the following to convert your `my-script.sh` file into base64
   format. This requirement prevents errors that occur from spacing and line break
   encoding.

```
LCC_CONTENT=`openssl base64 -A -in my-script.sh`
```

3. Create a lifecycle configuration for use with Studio. The following
   command creates a lifecycle configuration that runs when you launch an
   associated `JupyterLab` application:

```
aws sagemaker create-studio-lifecycle-config \
--region `region` \
--studio-lifecycle-config-name `my-jl-lcc` \
--studio-lifecycle-config-content $LCC_CONTENT \
--studio-lifecycle-config-app-type JupyterLab
```

Note the ARN of the newly created lifecycle configuration that is returned.
This ARN is required to attach the lifecycle configuration to your
application.

### Step 2: Attach the lifecycle configuration

to your Amazon SageMaker AI domain (domain) and user profile

To attach the lifecycle configuration, you must update the `UserSettings`
for your domain or user profile. Lifecycle configuration scripts that are associated at the domain level are inherited by
all users. However, scripts that are associated at the user profile level are scoped to
a specific user.

You can create a new user profile, domain, or space with a lifecycle
configuration attached by using the following commands:

- [create-user-profile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-user-profile.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-user-profile.html")
- [create-domain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-domain.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-domain.html")
- [create-space](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-space.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-space.html")

The following command creates a user profile with a lifecycle configuration. Add the lifecycle configuration ARN from the preceding step to the
`JupyterLabAppSettings` of the user. You can add multiple lifecycle
configurations at the same time by passing a list of them. When a
user launches a JupyterLab application with the AWS CLI, they can specify a lifecycle configuration instead of using the default one.
The lifecycle configuration that the user
passes must belong to the list of lifecycle configurations in
`JupyterLabAppSettings`.

```
# Create a new UserProfile
aws sagemaker create-user-profile --domain-id `domain-id` \
--user-profile-name `user-profile-name` \
--region `region` \
--user-settings '{
"JupyterLabAppSettings": {
  "LifecycleConfigArns":
    [`lifecycle-configuration-arn-list`]
  }
}'
```

## Create a lifecycle configuration (Console)

Learn how to create a lifecycle configuration using the AWS Management Console to automate
customization for your Studio environment.

### Step 1: Create a lifecycle

configuration

Use the following procedure to create a lifecycle configuration script that
prints `Hello World`.

###### To create a lifecycle configuration

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. On the left navigation pane, choose **Admin configurations**.
3. Under **Admin configurations**, choose **Lifecycle configurations**.
4. Choose the **JupyterLab** tab.
5. Choose **Create configuration**.
6. For **Name**, specify the name of the lifecycle configuration.
7. For the text box under **Scripts**, specify the following lifecycle configuration:

```

#!/bin/bash
set -eux
echo 'Hello World!'

```

8. Choose **Create configuration**.

### Step 2: Attach the lifecycle configuration

to your Amazon SageMaker AI domain (domain) and user profile

Lifecycle configuration scripts associated at the domain level are inherited by all users.
However, scripts that are associated at the user profile level are scoped to a specific user.

You can attach multiple lifecycle configurations to a domain or user profile for JupyterLab.

Use the following procedure to attach a lifecycle configuration to a domain.

###### To attach a lifecycle configuration to a domain

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. On the left navigation pane, choose **Admin configurations**.
3. Under **Admin configurations**, choose **domains**.
4. From the list of domains, select the domain to attach the
   lifecycle configuration to.
5. From the **Domain details**, choose the
   **Environment** tab.
6. Under **Lifecycle configurations for personal Studio
   apps**, choose **Attach**.
7. Under **Source**, choose **Existing
   configuration**.
8. Under **Studio lifecycle configurations**, select the
   lifecycle configuration that you created in the previous step.
9. Select **Attach to domain**.

Use the following procedure to attach a lifecycle configuration to a user profile.

###### To attach a lifecycle configuration to a user profile

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. On the left navigation pane, choose **Admin configurations**.
3. Under **Admin configurations**, choose **domains**.
4. From the list of domains, select the domain that contains the user
   profile to attach the lifecycle configuration to.
5. Under **User profiles**, select the user profile.
6. From the **User Details** page, choose
   **Edit**.
7. On the left navigation, choose **Studio
   settings**.
8. Under **Lifecycle configurations attached to user**,
   choose **Attach**.
9. Under **Source**, choose **Existing
   configuration**.
10. Under **Studio lifecycle configurations**, select the
    lifecycle configuration that you created in the previous step.
11. Choose **Attach to user profile**.
