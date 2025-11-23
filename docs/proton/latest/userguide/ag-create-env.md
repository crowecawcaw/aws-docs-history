End of support notice: On October 7, 2026, AWS will end support for AWS Proton. After October
7, 2026, you will no longer be able to access the AWS Proton console or AWS Proton resources. Your deployed infrastructure
will remain intact. For more information, see [AWS Proton Service Deprecation and Migration
Guide](proton-end-of-support.md "proton-end-of-support.md").

# Create an environment

Learn to create AWS Proton environments.

###### You can create an AWS Proton environment in one of two ways:

- Create, manage, and provision a standard environment by using a _standard
  environment template_. AWS Proton provisions infrastructure for your
  environment.
- Connect AWS Proton to customer-managed infrastructure by using a _customer-managed
  environment template_. You provision your own shared resources outside of
  AWS Proton, and then you provide provisioning outputs that AWS Proton can use.

###### You can choose one of several provisioning approaches when you create an

environment.

- _AWS managed provisioning_ – Create, manage, and provision
  an environment in a single account. AWS Proton provisions your environment.

This method only supports CloudFormation infrastructure code (IaC) templates.

- _AWS managed provisioning to another account_ – In a
  single management account, create and manage an environment that's provisioned in another
  account with environment account connections. AWS Proton provisions your environment in the
  other account. For more information, see [Create an environment in one account and
  provision in another account](#ag-create-env-deploy-other "#ag-create-env-deploy-other") and [Environment account connections](ag-env-account-connections.md "ag-env-account-connections.md").

This method only supports CloudFormation IaC templates.

- _Self-managed provisioning_ – AWS Proton submits provisioning
  pull requests to a linked repository with your own provisioning infrastructure.

This method only supports Terraform IaC templates.

- _CodeBuild provisioning_ – AWS Proton uses AWS CodeBuild to run
  shell commands that you provide. Your commands can read inputs that AWS Proton provides, and
  are responsible for provisioning or deprovisioning infrastructure and generating output
  values. A template bundle for this method includes your commands in a manifest file and
  any programs, scripts, or other files that these commands may need.

As an example to using CodeBuild provisioning, you can include code that uses the
AWS Cloud Development Kit (AWS CDK) to provision AWS resources, and a manifest that installs the CDK and
runs your CDK code.

For more information, see [CodeBuild provisioning template bundle](ag-infrastructure-tmp-files-codebuild.md "ag-infrastructure-tmp-files-codebuild.md").

###### Note

You can use CodeBuild provisioning with environments and services. At this time you can't provision components this way.
With AWS managed provisioning (both in the same account and to another account), AWS Proton
makes direct calls to provision your resources.

With self-managed provisioning, AWS Proton makes pull requests to provide compiled IaC files
that your IaC engine uses to provision resources.

For more information, see [How AWS Proton provisions infrastructure](ag-works-prov-methods.md "ag-works-prov-methods.md"), [Template bundles](ag-template-authoring.md#ag-template-bundles "ag-template-authoring.md#ag-template-bundles"), and [Schema requirements for environment template bundles](ag-schema.md#schema-req-env "ag-schema.md#schema-req-env").

###### Topics

- [Create and provision a standard environment in
  the same account](#ag-create-env-same-account "#ag-create-env-same-account")
- [Create an environment in one account and
  provision in another account](#ag-create-env-deploy-other "#ag-create-env-deploy-other")
- [Create and provision an environment using
  self-managed provisioning](#ag-create-env-pull-request "#ag-create-env-pull-request")

## Create and provision a standard environment in

the same account

Use the console or AWS CLI to create and provision an environment in a single account.
Provisioning is managed by AWS.

AWS Management Console

###### Use the console to create and provision an environment in a single

account

1. In the [AWS Proton console](https://console.aws.amazon.com//proton/ "https://console.aws.amazon.com//proton/"), choose
   **Environments**.
2. Choose **Create environment**.
3. In the **Choose an environment template** page, select a
   template and choose **Configure**.
4. In the **Configure environment** page, in the
   **Provisioning** section, choose **AWS managed
   provisioning**.
5. In the **Deployment account** section, choose **This
   AWS account**.
6. In the **Configure environment** page, in the
   **Environment settings** section, enter an
   **Environment name**.
7. (Optional) Enter a description for the environment.
8. In the **Environment roles** section, select the AWS Proton
   service role that you created as part of [Setting up AWS Proton service roles](ag-setting-up-iam.md#setting-up-cicd "ag-setting-up-iam.md#setting-up-cicd").
9. (Optional) In the **Component role** section, select a
   service role that enables directly defined components to run in the environment
   and scopes down the resources that they can provision. For more information, see
   [AWS Proton components](ag-components.md "ag-components.md").
10. (Optional) In the **Tags** section, choose **Add new
    tag** and enter a key and value to create a customer managed
    tag.
11. Choose **Next**.
12. In the **Configure environment custom settings** page, you
    must enter values for the `required` parameters. You can enter values
    for the `optional` parameters or use the defaults when given.
13. Choose **Next** and review your inputs.
14. Choose **Create**.

View the environment details and status, as well as the
AWS managed tags and customer managed tags for your environment. 15. In the navigation pane, choose **Environments**.

A new page displays a list of your environments along with the status and
other environment details.

AWS CLI
Use the AWS CLI to create and provision an environment in a
single account.

To create an environment, you specify the [AWS Proton
service role](security_iam_service-role-policy-examples.md#proton-svc-role "security_iam_service-role-policy-examples.md#proton-svc-role") ARN, path to your spec file, environment name, environment
template ARN, the major and minor versions, and description (optional).

The next examples shows a YAML formatted spec file that specifies
values for two inputs that are defined in the environment template schema file. You
can use the `get-environment-template-minor-version` command to view the
environment template schema.

```
proton: EnvironmentSpec
spec:
  my_sample_input: "the first"
  my_other_sample_input: "the second"

```

Create an environment by running the following command.

```
`$` `aws proton create-environment \
 --name "`MySimpleEnv`" \
 --template-name `simple-env` \
 --template-major-version `1` \
 --proton-service-role-arn "arn:aws:iam::`123456789012`:role/`AWSProtonServiceRole`" \
 --spec "`file://env-spec.yaml`"`
```

Response:

```
{
    "environment": {
        "arn": "arn:aws:proton:region-id:123456789012:environment/MySimpleEnv",
        "createdAt": "2020-11-11T23:03:05.405000+00:00",
        "deploymentStatus": "IN_PROGRESS",
        "lastDeploymentAttemptedAt": "2020-11-11T23:03:05.405000+00:00",
        "name": "MySimpleEnv",
        "protonServiceRoleArn": "arn:aws:iam::123456789012:role/ProtonServiceRole",
        "templateName": "simple-env"
    }
}
```

After you create a new environment, you can view a list of AWS and customer
managed tags as shown in the following example command. AWS Proton automatically generates
AWS managed tags for you. You can also modify and create customer managed tags using
the AWS CLI. For more information, see [AWS Proton resources and tagging](resources.md "resources.md").

Command:

```
`$` `aws proton list-tags-for-resource \
 --resource-arn "arn:aws:proton:`region-id`:`123456789012`:environment/`MySimpleEnv`"`
```

## Create an environment in one account and

provision in another account

Use the console or AWS CLI to create a standard environment in a management account that
provisions environment infrastructure in another account. Provisioning is managed by
AWS.

###### Before using the console or CLI, complete the following steps.

1. Identify the AWS account IDs for the management and environment account, and copy
   them for later use.
2. In the environment account, create an AWS Proton service role with minimum permissions
   for the environment to create. For more information, see [AWS Proton service role for provisioning using CloudFormation](security_iam_service-role-policy-examples.md#proton-svc-role "security_iam_service-role-policy-examples.md#proton-svc-role").

AWS Management Console

###### Use the console create an environment in one account and provision in

another.

1. ###### In the environment account, create an environment account connection, and use

   it to send a request to connect to the management account.
   1. In [AWS Proton console](https://console.aws.amazon.com//proton/ "https://console.aws.amazon.com//proton/"), choose
      **Environment account connections** in the navigation
      pane.
   2. In the **Environment account connections** page, choose
      **Request to connect**.

   ###### Note

   Verify that the account ID that's listed in the **Environment
   account connection** page heading matches your pre-identified
   environment account ID. 3. In the **Request to connect** page, in the
   **Environment role** section, select **Existing
   service role** and the name of the service role that you created
   for the environment. 4. In the **Connect to management account** section, enter
   the **Management account ID** and an **Environment
   name** for your AWS Proton environment. Copy the name for later
   use. 5. Choose **Request to connect** at the lower right corner
   of the page. 6. Your request shows as pending in the **Environment connections
   sent to a management account** table and a modal shows how to
   accept the request from the management account.

2. ###### In the management account, accept a request to connect from the environment

   account.
   1. Log in to your management account and choose **Environment account
      connections** in the AWS Proton console.
   2. In the **Environment account connections** page, in the
      **Environment account connection requests** table, select
      the environment account connection with the environment account ID that
      matches your pre-identified environment account ID.

   ###### Note

   Verify that the account ID that's listed in the **Environment
   account connection** page heading matches your pre-identified
   management account ID. 3. Choose **Accept**. The status changes from PENDING to
   CONNECTED.

3. ###### In the management account, create an environment.
   1. In the navigation pane, choose **Environment
      templates**.
   2. In the **Environment templates** page, choose
      **Create environment template**.
   3. In the **Choose an environment template** page, choose an
      environment template.
   4. In the **Configure environment** page, in the
      **Provisioning** section, choose **AWS managed
      provisioning**.
   5. In the **Deployment account** section, choose
      **Another AWS account;**.
   6. In the **Environment details** section, select your
      **Environment account connection** and
      **Environment name**.
   7. Choose **Next**.
   8. Fill out the forms and choose **Next** until you reach
      the **Review and Create** page.
   9. Review and choose **Create environment**.

AWS CLI
Use the AWS CLI to create an environment in one account and
provision in another.

In the environment account, create an environment account connection and request
to connect by running the following command.

```
`$` `aws proton create-environment-account-connection \
 --environment-name "`simple-env-connected`" \
 --role-arn "arn:aws:iam::`222222222222`:role/service-role/`env-account-proton-service-role`" \
 --management-account-id "`111111111111`"`
```

Response:

```
{
    "environmentAccountConnection": {
        "arn": "arn:aws:proton:region-id:222222222222:environment-account-connection/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "environmentAccountId": "222222222222",
        "environmentName": "simple-env-connected",
        "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "lastModifiedAt": "2021-04-28T23:13:50.847000+00:00",
        "managementAccountId": "111111111111",
        "requestedAt": "2021-04-28T23:13:50.847000+00:00",
        "roleArn": "arn:aws:iam::222222222222:role/service-role/env-account-proton-service-role",
        "status": "PENDING"
    }
}
```

In the management account, accept the environment account connection request by
running the following command.

```
`$` `aws proton accept-environment-account-connection \
 --id "`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`"`
```

Response:

```
{
    "environmentAccountConnection": {
        "arn": "arn:aws:proton:region-id:222222222222:environment-account-connection/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "environmentAccountId": "222222222222",
        "environmentName": "simple-env-connected",
        "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "lastModifiedAt": "2021-04-28T23:15:33.486000+00:00",
        "managementAccountId": "111111111111",
        "requestedAt": "2021-04-28T23:13:50.847000+00:00",
        "roleArn": "arn:aws:iam::222222222222:role/service-role/env-account-proton-service-role",
        "status": "CONNECTED"
    }
}
```

View your environment account connection by running the following command.

```
`$` `aws proton get-environment-account-connection \
 --id "`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`"`
```

Response:

```
{
    "environmentAccountConnection": {
        "arn": "arn:aws:proton:region-id:222222222222:environment-account-connection/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "environmentAccountId": "222222222222",
        "environmentName": "simple-env-connected",
        "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "lastModifiedAt": "2021-04-28T23:15:33.486000+00:00",
        "managementAccountId": "111111111111",
        "requestedAt": "2021-04-28T23:13:50.847000+00:00",
        "roleArn": "arn:aws:iam::222222222222:role/service-role/env-account-proton-service-role",
        "status": "CONNECTED"
    }
}
```

In the management account, create an environment by running the following
command.

```
`$` `aws proton create-environment \
 --name "`simple-env-connected`" \
 --template-name `simple-env-template` \
 --template-major-version "`1`" \
 --template-minor-version "`1`" \
 --spec "`file://simple-env-template/specs/original.yaml`" \
 --environment-account-connection-id "`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`"`
```

Response:

```
{
    "environment": {
        "arn": "arn:aws:proton:region-id:111111111111:environment/simple-env-connected",
        "createdAt": "2021-04-28T23:02:57.944000+00:00",
        "deploymentStatus": "IN_PROGRESS",
        "environmentAccountConnectionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "environmentAccountId": "222222222222",
        "lastDeploymentAttemptedAt": "2021-04-28T23:02:57.944000+00:00",
        "name": "simple-env-connected",
        "templateName": "simple-env-template"
    }
}
```

## Create and provision an environment using

self-managed provisioning

When you use self-managed provisioning, AWS Proton submits provisioning pull requests to a
linked repository with your own provisioning infrastructure. The pull requests start your
own workflow, which calls AWS services; to provision infrastructure.

###### Self-managed provisioning considerations:

- Before you create an environment, set up a repository resource directory for
  self-managed provisioning. For more information, see [AWS Proton infrastructure as code files](ag-infrastructure-tmp-files.md "ag-infrastructure-tmp-files.md").
- After you create the environment, AWS Proton waits to receive asynchronous notifications
  regarding the status of your infrastructure provisioning. Your provisioning code must
  use the AWS Proton `NotifyResourceStateChange` API to send these asynchronous
  notifications to AWS Proton.

You can use self-managed provisioning in the console or with the AWS CLI. The following
examples show how you can use self-managed provisioning with Terraform.

AWS Management Console

###### Use the console to create a Terraform environment using self-managed

provisioning.

1. In the [AWS Proton console](https://console.aws.amazon.com//proton/ "https://console.aws.amazon.com//proton/"), choose
   **Environments**.
2. Choose **Create environment**.
3. In the **Choose an environment template** page, select a
   Terraform template and choose **Configure**.
4. In the **Configure environment** page, in the
   **Provisioning** section, choose **Self-managed
   provisioning**.
5. In the **Provisioning repository details** section:
   1. If you haven't yet [linked your provisioning
      repository to AWS Proton](ag-create-repo.md "ag-create-repo.md"), choose **New repository**,
      choose one of the repository providers, and then, for **CodeStar
      connection**, choose one of your connections.

   ###### Note

   If you don't yet have a connection to the relevant repository provider
   account, choose **Add a new CodeStar connection**. Then,
   create a connection, and then choose the refresh button next to the
   **CodeStar connection** menu. You should now be able to
   choose your new connection in the menu.

   If you've already linked your repository to AWS Proton, choose
   **Existing repository**. 2. For **Repository name**, choose a repository. The
   drop-down menu shows linked repositories for **Existing
   repository** or the list of repositories in the provider account
   for **New repository**. 3. For **Branch name**, choose one of the repository
   branches.

6. In the **Environment settings** section, enter an
   **Environment name**.
7. (Optional) Enter a description for the environment.
8. (Optional) In the **Tags** section, choose **Add new
   tag** and enter a key and value to create a customer managed
   tag.
9. Choose **Next**.
10. In the **Configure environment custom settings** page, you
    must enter values for the `required` parameters. You can enter values
    for the `optional` parameters or use the defaults when given.
11. Choose **Next** and review your inputs.
12. Choose **Create** to send a pull request.
    - If you approve the pull request, the deployment is in progress.
    - If you reject the pull request, the environment creation is
      cancelled.
    - If the pull request times out, environment creation
      _isn't_ complete.

13. View the environment details and status, as well as the AWS managed tags and
    customer managed tags for your environment.
14. In the navigation pane, choose **Environments**.

A new page displays a list of your environments along with the status and
other environment details.

AWS CLI
When you create an environment using self-managed provisioning, you
_add_ the `provisioningRepository` parameter and omit
the `ProtonServiceRoleArn` and `environmentAccountConnectionId`
parameters.

###### Use the AWS CLI to create a Terraform environment with self-managed

provisioning.

1. Create an environment and send a pull request to the repository for review and
   approval.

The next examples shows a YAML formatted spec file that defines
the values for two inputs based on the environment template schema file. You can
use the `get-environment-template-minor-version` command to view the
environment template schema.

Spec:

```
proton: EnvironmentSpec
spec:
  ssm_parameter_value: "test"

```

Create an environment by running the following command.

```
`$` `aws proton create-environment \
 --name "`pr-environment`" \
 --template-name "`pr-env-template`" \
 --template-major-version "`1`" \
 --provisioning-repository="branch=`main`,name=`myrepos/env-repo`,provider=`GITHUB`" \
 --spec "`file://env-spec.yaml`"`
```

Response:>

```
{
    "environment": {
        "arn": "arn:aws:proton:region-id:123456789012:environment/pr-environment",
        "createdAt": "2021-11-18T17:06:58.679000+00:00",
        "deploymentStatus": "IN_PROGRESS",
        "lastDeploymentAttemptedAt": "2021-11-18T17:06:58.679000+00:00",
        "name": "pr-environment",
        "provisioningRepository": {
            "arn": "arn:aws:proton:region-id:123456789012:repository/github:myrepos/env-repo",
            "branch": "main",
            "name": "myrepos/env-repo",
            "provider": "GITHUB"
        },
        "templateName": "pr-env-template"
    }

```

2. Review the request.
   - If you approve the request, provisioning is in progress.
   - If you reject the request, the environment creation is cancelled.
   - If the pull request times out, environment creation
     _isn't_ complete.

3. Asynchronously provide provisioning status to AWS Proton. The following example
   notifies AWS Proton of a successful provisioning.

```
`$` `aws proton notify-resource-deployment-status-change \
 --resource-arn "arn:aws:proton:`region-id`:`123456789012`:environment/`pr-environment`" \
 --status "`SUCCEEDED`"`
```
