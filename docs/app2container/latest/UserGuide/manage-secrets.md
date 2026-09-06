

AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET is no longer open to new customers. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# Manage secrets for AWS App2Container
<a name="manage-secrets"></a>

App2Container uses AWS Secrets Manager to manage the credentials necessary to connect your worker machine to application servers and run remote commands. Secrets Manager encrypts your secrets for storage and provides an Amazon Resource Name (ARN) so that you can access the secret. When you run the **remote configure** command, you provide the secret ARN that App2Container uses to connect to your target server when you run the remote command.

For more information about Secrets Manager, see [What Is AWS Secrets Manager?](https://docs.aws.amazon.com/secretsmanager/latest/userguide/) For information specifically related to costs, see [Pricing for AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html#asm_pricing) in the *AWS Secrets Manager User Guide*.

## Create remote access secrets
<a name="ra-secrets"></a>

The secret that App2Container uses to connect to an application server varies with the application server's operating system (OS) platform. To create a remote access secret for your application server, choose the tab that matches your OS platform.

------
#### [ Linux ]

For Linux, you can store either the SSH private key or the Certificate and SSH private key in Secrets Manager. To create a secret in Secrets Manager so that you can access your application server remotely, follow the steps shown in the [Create a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html) page in the *AWS Secrets Manager User Guide*. Provide the information that App2Container needs to run remote commands as follows.

**Step 1 Choose secret type**
+ **Secret type** – To store a key that App2Container uses programmatically, through API calls, choose the **Other type of secrets** option.
+ Specify the following **Key/value pairs** to store in the secret. To add the next key/value pair, choose **\+ Add row**.

**Username key**
  + **Key name (box 1):** **username**
  + **Key value (box 2):** Enter the plaintext username value to use with SSH.

**SSH private key**
  + **Key name (box 1):** **key**
  + **Key value (box 2):** Copy the base64-encoded string that represents your private key file into the second box.
**Note**  
To base64-encode your key file, you can use the following command, where `.ssh/id_rsa` is the private key that encodes the file:  

    ```
    $ base64 {{.ssh/id_rsa}}
    ```

**SSH Certificate key (optional)**
  + **Key name (box 1):** **cert**
  + **Key value (box 2):** Copy the base64-encoded string that represents your signed certificate file into the second box.
**Note**  
To base64-encode your signed certificate file, you can use the following command, where `.ssh/id_rsa-cert.pub` is the private key that encodes the file:  

    ```
    $ base64 {{.ssh/id_rsa-cert.pub}}
    ```

**Step 2 Configure secret**
+ Enter a name for your secret in the **Secret name** box. You can also enter optional information to help identify your secret, such as **Description**, or you can enter tags in the **Tags** panel.

------
#### [ Windows ]

For Windows application servers, you can store the Username and Password for remote access. In most cases, the username and password translates to a set of credentials for a domain user with access to the application servers. [Create a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html) page in the *AWS Secrets Manager User Guide*

**Step 1 Choose secret type**
+ **Secret type** – To store a key that App2Container uses programmatically, through API calls, choose the **Other type of secrets** option.
+ Specify the following **Key/value pairs** to store in the secret. To add the next key/value pair, choose **\+ Add row**.

**Username key**
  + **Key name (box 1):** **username**
  + **Key value (box 2):** In the second box, enter the plaintext username value to use with the connection credentials for your application server.

**Password key**
  + **Key name (box 1):** **password**
  + **Key value (box 2):** In the second box, enter the password value.

**Step 2 Configure secret**
+ Enter a name for your secret in the **Secret name** box. You can also enter optional information to help identify your secret, such as **Description**, or you can enter tags in the **Tags** panel.

------

## Create secrets for Jenkins pipelines
<a name="jenkins-secrets"></a>

Integration with Jenkins requires secure authentication, both for the Git repository that Jenkins uses for automated container build pipelines, and for authentication to the Jenkins server itself. For secure authentication, App2Container uses Secrets Manager to store credentials, and provide access to the authentication secrets to Jenkins agent nodes.

**Topics**
+ [Authentication secret for Git](#jenkins-secrets-ssh)
+ [Authentication secret for Jenkins server](#jenkins-secrets-api-token)

### Authentication secret for Git
<a name="jenkins-secrets-ssh"></a>

App2Container uses SSH to authenticate to the Git source repository that the Jenkins agent uses to update your pipeline. In the `pipeline.json` file, you provide the ARN from the authentication secret you create, in the `sshKeyArn` parameter value.

To create a secret in Secrets Manager so that App2Container can authenticate to the Git repository for the Jenkins agent, follow the steps shown in the [Create a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html) page in the *AWS Secrets Manager User Guide*. Provide the information that App2Container needs to authenticate to the Git source repository as follows.

**Step 1 Choose secret type**
+ **Secret type** – To store a key that App2Container uses programmatically, through API calls, choose the **Other type of secrets** option.
+ Specify the following **Key/value pairs** to store in the secret. To add the next key/value pair, choose **\+ Add row**.

**Username key**
  + **Key name (box 1):** **username**
  + **Key value (box 2):** In the second box, enter the plaintext username value that App2Container uses with SSH to authenticate to the Git source repository for Jenkins.

**Username key**
  + **Key name (box 1):** **key**
  + **Key value (box 2):** In the second box, copy the base64-encoded string that represents your private key file.
**Note**  
To base64-encode your key file, you can use the following command, where `.ssh/id_rsa` is the private key that encodes the file:  

    ```
    $ base64 {{.ssh/id_rsa}}
    ```

**Step 2 Configure secret**
+ Enter a name for your secret in the **Secret name** box. You can also enter optional information to help identify your secret, such as **Description**, or you can enter tags in the **Tags** panel.

### Authentication secret for Jenkins server
<a name="jenkins-secrets-api-token"></a>

Just as App2Container needs credentials to interact with AWS services on your behalf, so it also needs credentials to interact with the Jenkins server that runs your pipelines. In the `pipeline.json` file, you provide the ARN from the authentication secret you create, in the `apiTokenArn` parameter value.

#### Generate a Jenkins authentication token
<a name="jenkins-secrets-api-token-generate"></a>

Before you store your Jenkins authentication secrets in Secrets Manager, generate an API token from your Jenkins server. To generate a Jenkins API authentication token, follow these steps:

1. Log in to your Jenkins server.

1. In the upper right corner of the interface, choose your name.

1. From the left side navigation menu, choose **Configure** .

1. In the **API Token** panel, choose **Add new Token**.

1. After Jenkins generates the token, give it a name. Keep track of the name. You will need it for the secret key you enter in Secrets Manager.

1. Choose the copy icon to copy the token value, or select and copy the value manually. You will need it for the secret value that you enter in Secrets Manager You can't see the value again after you log out of Jenkins.
**Note**  
Ensure that you revoke tokens that you no longer need.

#### Store your Jenkins authentication token in Secrets Manager
<a name="jenkins-secrets-api-token-store"></a>

To create a secret in Secrets Manager for the Jenkins authentication token, follow the steps shown in the [Create a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html) page in the *AWS Secrets Manager User Guide*. Provide the information that App2Container needs to authenticate to the Jenkins server that runs your pipelines as follows.

**Step 1 Choose secret type**
+ **Secret type** – To store a key that App2Container uses programmatically, through API calls, choose the **Other type of secrets** option.
+ Specify the following **Key/value pairs** to store in the secret. To add the next key/value pair, choose **\+ Add row**.

**Username key**
  + **Key name (box 1):** **username**
  + **Key value (box 2):** In the second box, enter the plaintext username value so that App2Container can log in to the Jenkins server.

**Username key**
  + **Key name (box 1):** **apitoken**
  + **Key value (box 2):** In the second box, copy the base64-encoded string that represents your Jenkins authentication token.
**Note**  
To base64-encode a string, you can use the following command:  

    ```
    $ echo {{string-to-encode}} | base64
    ```

**Step 2 Configure secret**
+ Enter a name for your secret in the **Secret name** box. You can also enter optional information to help identify your secret, such as **Description**, or you can enter tags in the **Tags** panel.

## Create secrets for Microsoft Azure DevOps pipelines
<a name="azure-devops-secrets"></a>

To integrate with Azure Repos Git repositories and Azure DevOps pipelines, App2Container uses secure authentication. App2Container authenticates with a Microsoft Azure Personal Access Token (PAT) that you store as a secret in Secrets Manager.

 In the `apiTokenArn` parameter value of the `pipeline.json` file, provide the ARN from the authentication secret that you create.

### Generate a Microsoft Azure Personal Access Token (PAT)
<a name="azure-devops-secrets-generate-pat"></a>

Before you generate a Personal Access Token (PAT), you first must have an active Microsoft Azure account, with an organization and project already defined. For more information about how to set up Azure DevOps, see [Prerequisites](a2c-integrations-azure-devops.md#integrations-azure-devops-prereq).

To generate a PAT for your Microsoft Azure account, sign in to your Azure organization and create a new token with a **Custom defined** scope. For instructions, see [Create a PAT](https://docs.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops#create-a-pat) in the *Azure DevOps Services* documentation on the Microsoft documentation website. Choose the settings for your custom scope as follows.
+ **Agent Pools:** Read and manage
+ **Build:** Read and execute
+ **Code:** Full
+ **Extensions:** Read and manage
+ **Release:** Read, write, execute, and manage
+ **Service Connections:** Read and query

**Note**  
If you don't see all of the settings, choose **Show all scopes** to show the complete list.

### Store your PAT in Secrets Manager
<a name="azure-devops-secrets-store-pat"></a>

To create a secret in Secrets Manager for the PAT, follow the procedure on the [Create a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html) page in the *AWS Secrets Manager User Guide*. To access the Azure Repos Git repository, and Azure DevOps, provide the information that App2Container needs to authenticate to Microsoft Azure, as follows.

**Step 1 Choose secret type**
+ **Secret type** – To store a key that App2Container uses programmatically, through API calls, choose the **Other type of secrets** option.
+ Specify the following **Key/value pair** to store in the secret.

**PAT key**
  + **Key name (box 1):** **azure-personal-access-token**
  + **Key value (box 2):** Paste a copy of the token string that the Azure DevOps service generated.

**Step 2 Configure secret**
+ Enter a name for your secret in the **Secret name** box. You can also enter optional information to help identify your secret, such as **Description**, or you can enter tags in the **Tags** panel.