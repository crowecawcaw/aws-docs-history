Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Tutorial: Deploy an application to Amazon EKS

In this tutorial, you learn how to deploy a containerized application into Amazon Elastic Kubernetes Service using
an Amazon CodeCatalyst workflow, Amazon EKS, and a few other AWS services. The deployed application is a
simple 'Hello, World!' website built on an Apache web server Docker image. The tutorial walks
you through the required preparation work such as setting up a development machine and an Amazon EKS
cluster, and then describes how to create a workflow to build the application and deploy it into
the cluster.

After the initial deployment is complete, the tutorial instructs you to make a change to
your application source. This change causes a new Docker image to be built and pushed to your
Docker image repository with new revision information. The new revision of the Docker image is
then deployed into Amazon EKS.

###### Tip

Instead of working your way through this tutorial, you can use a blueprint that does a
complete Amazon EKS setup for you. You'll need to use the **EKS App Deployment**
blueprint. For more information, see [Creating a project with a
blueprint](projects-create.md#projects-create-console-template "projects-create.md#projects-create-console-template").

###### Topics

- [Prerequisites](#deploy-tut-eks-prereqs "#deploy-tut-eks-prereqs")
- [Step 1: Set up your development
  machine](#deploy-tut-eks-dev-env-create "#deploy-tut-eks-dev-env-create")
- [Step 2: Create an Amazon EKS cluster](#deploy-tut-eks-cluster "#deploy-tut-eks-cluster")
- [Step 3: Create an Amazon ECR image repository](#deploy-tut-eks-ecr "#deploy-tut-eks-ecr")
- [Step 4: Add source files](#deploy-tut-eks-source-files "#deploy-tut-eks-source-files")
- [Step 5: Create AWS roles](#deploy-tut-eks-roles "#deploy-tut-eks-roles")
- [Step 6: Add AWS roles to CodeCatalyst](#deploy-tut-eks-import-roles "#deploy-tut-eks-import-roles")
- [Step 7: Update the ConfigMap](#deploy-tut-eks-configmap "#deploy-tut-eks-configmap")
- [Step 8: Create and run a workflow](#deploy-tut-eks-workflow "#deploy-tut-eks-workflow")
- [Step 9: Make a change to your source files](#deploy-tut-eks-change "#deploy-tut-eks-change")
- [Clean up](#deploy-tut-eks-cleanup "#deploy-tut-eks-cleanup")

## Prerequisites

Before you begin this tutorial:

- You need an Amazon CodeCatalyst **space** with a connected AWS account.
  For more information, see [Creating a space](spaces-create.md "spaces-create.md").
- In your space, you need an empty project called:

```
codecatalyst-eks-project
```

Use the **Start from scratch** option to create this project.

For more information, see [Creating an empty project in Amazon CodeCatalyst](projects-create.md#projects-create-empty "projects-create.md#projects-create-empty").

- In your project, you need an empty CodeCatalyst **source repository**
  called:

```
codecatalyst-eks-source-repository
```

For more information, see [Store and collaborate on code with source repositories in CodeCatalyst](source.md "source.md").

- In your project, you need a CodeCatalyst CI/CD **environment** (not a
  Dev Environment) called:

```
codecatalyst-eks-environment
```

Configure this environment as follows:

    + Choose any type, such as **Non-production**.
    + Connect your AWS account to it.
    + For the **Default IAM role**, choose any role. You'll specify a
     different role later.

For more information, see [Deploying into AWS accounts and VPCs](deploy-environments.md "deploy-environments.md").

## Step 1: Set up your development

machine

The first step in this tutorial is to configure a development machine with a few tools
that you'll use throughout this tutorial. These tools are:

- the `eksctl` utility – for cluster creation
- the `kubectl` utility – a prerequisite for
  `eksctl`
- the AWS CLI – also a prerequisite for `eksctl`

You can install these tools on your existing development machine if you have one, or you
can use a CodeCatalyst Dev Environment, which is Cloud-based. The benefit of a CodeCatalyst Dev Environment is
that it's easy to spin up and take down, and is integrated with other CodeCatalyst services,
allowing you to work through this tutorial in fewer steps.

This tutorial assumes you'll be using a CodeCatalyst Dev Environment.

The following instructions describe a quick way to launch a CodeCatalyst Dev Environment and
configure it with the required tools, but if you want detailed instructions, see:

- [Creating a Dev Environment](devenvironment-create.md "devenvironment-create.md") in this
  guide.
- [Installing
  kubectl](../../../eks/latest/userguide/install-kubectl.md "../../../eks/latest/userguide/install-kubectl.md") in the **Amazon EKS User Guide**.
- [Installing or
  upgrading eksctl](../../../eks/latest/userguide/eksctl.md "../../../eks/latest/userguide/eksctl.md") in the **Amazon EKS User Guide**.
- [Installing or updating the latest version of the AWS CLI](../../../cli/latest/userguide/cli-chap-install.md "../../../cli/latest/userguide/cli-chap-install.md") in the
  _AWS Command Line Interface User Guide_.

###### To launch a Dev Environment

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to your project, `codecatalyst-eks-project`.
3. In the navigation pane, choose **Code**, and then choose
   **Source repositories**.
4. Choose the name of your source repository,
   `codecatalyst-eks-source-repository`.
5. Near the top choose **Create Dev Environment**, and then choose
   **AWS Cloud9 (in browser)**.
6. Make sure that **Work in existing branch** and
   **main** are selected, and then choose
   **Create**.

Your Dev Environment launches in a new browser tab, and your repository
(`codecatalyst-eks-source-repository`) is cloned into it.

###### To install and configure kubectl

1. In the Dev Environment terminal, enter:

```
curl -o kubectl https://amazon-eks.s3.us-west-2.amazonaws.com/1.18.9/2020-11-02/bin/linux/amd64/kubectl
```

2. Enter:

```
chmod +x ./kubectl
```

3. Enter:

```
mkdir -p $HOME/bin && cp ./kubectl $HOME/bin/kubectl && export PATH=$PATH:$HOME/bin
```

4. Enter:

```
echo 'export PATH=$PATH:$HOME/bin' >> ~/.bashrc
```

5. Enter:

```
kubectl version --short --client
```

6. Check that a version appears.

You have now installed `kubectl`.

###### To install and configure eksctl

###### Note

`eksctl` is not strictly required because you can use `kubectl`
instead. However, `eksctl` has the benefit of automating much of the cluster
configuration, and is therefore the tool recommended for this tutorial.

1. In the Dev Environment terminal, enter:

```
curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
```

2. Enter:

```
sudo cp /tmp/eksctl /usr/bin
```

3. Enter:

```
eksctl version
```

4. Check that a version appears.

You have now installed `eksctl`.

###### To verify that the AWS CLI is installed

1. In the Dev Environment terminal, enter:

```
aws --version
```

2. Check that a version appears to verify that the AWS CLI is installed.

Complete the remaining procedures to configure the AWS CLI with the necessary
permissions to access AWS.

**To configure the AWS CLI**

You must configure the AWS CLI with access keys and a session token to give it access to
AWS services. The following instructions provide a quick way to configure the keys and
token, but if you want detailed instructions, see [Configuring the AWS CLI](../../../cli/latest/userguide/cli-chap-configure.md "../../../cli/latest/userguide/cli-chap-configure.md") in the
_AWS Command Line Interface User Guide_.

1.  Create an IAM Identity Center user, as follows:
    1. Sign in to the AWS Management Console and open the AWS IAM Identity Center console at [https://console.aws.amazon.com/singlesignon/](https://console.aws.amazon.com/singlesignon/ "https://console.aws.amazon.com/singlesignon/").

    (You might need to choose **Enable** if you've never signed in to
    IAM Identity Center before.)

    ###### Note

    Make sure you sign in using the AWS account that is connected to your CodeCatalyst
    space. You can verify which account is connected by navigating to your
    space and choosing the **AWS accounts** tab. For more
    information, see [Creating a space](spaces-create.md "spaces-create.md"). 2. In the navigation pane, choose **Users**, and then choose
    **Add user**. 3. In **Username**, enter:

    ```
    `codecatalyst-eks-user`
    ```

    4. Under **Password**, choose **Generate a one-time password
       that you can share with this user**.
    5. In **Email address** and **Confirm email
       address**, enter an email address that doesn't already exist in
       IAM Identity Center.
    6. In **First name**, enter:

    ```
    `codecatalyst-eks-user`
    ```

    7. In **Last name**, enter:

    ```
    `codecatalyst-eks-user`
    ```

    8. In **Display name**, keep:

    ```
    `codecatalyst-eks-user codecatalyst-eks-user`
    ```

    9. Choose **Next**.
    10. On the **Add user to groups** page, choose
        **Next**.
    11. On the **Review and add user** page, review the information and
        choose **Add user**.

    A **One-time password** dialog box appears. 12. Choose **Copy** and then paste the sign-in information to a text
    file. The sign-in information consists of the AWS access portal URL, a user name,
    and a one-time password. 13. Choose **Close**.

2.  Create a permission set, as follows:
    1. In the navigation pane, choose **Permission sets**, and then
       choose **Create permission set**.
    2. Choose **Predefined permission set** and then select
       **AdministratorAccess**. This policy provides full permissions to
       all AWS services.
    3. Choose **Next**.
    4. In **Permission set name**, remove
       `AdministratorAccess` and enter:

    ```
    `codecatalyst-eks-permission-set`
    ```

    5. Choose **Next**.
    6. On the **Review and create** page, review the information and
       choose **Create**.

3.  Assign the permission set to `codecatalyst-eks-user`, as follows:
    1. In the navigation pane, choose **AWS accounts**, and then
       select the check box next to the AWS account that you're currently signed in
       to.
    2. Choose **Assign users or groups**.
    3. Choose the **Users** tab.
    4. Select the check box next to `codecatalyst-eks-user`.
    5. Choose **Next**.
    6. Select the check box next to
       `codecatalyst-eks-permission-set`.
    7. Choose **Next**.
    8. Review the information and choose **Submit**.

    You have now assigned `codecatalyst-eks-user` and
    `codecatalyst-eks-permission-set` to your AWS account, binding them
    together.

4.  Obtain `codecatalyst-eks-user`'s access keys and session token, as
    follows:
    1. Make sure you have the AWS access portal URL and the username and one-time
       password for `codecatalyst-eks-user`. You should have copied this
       information to a text editor earlier.

    ###### Note

    If you do not have this information, go to the
    `codecatalyst-eks-user` details page in IAM Identity Center, choose
    **Reset password**, **Generate a one-time password
    [...]**, and **Reset password** again to display the
    information on the screen. 2. Sign out of AWS. 3. Paste the AWS access portal URL into your browser's address bar. 4. Sign in with:

        * **Username**:



        ```
        `codecatalyst-eks-user`
        ```
        * **Password**:


        `one-time-password`

    5. In **Set new password**, enter a new password and choose
       **Set new password**.

    An **AWS account** box appears on the screen. 6. Choose **AWS account**, and then choose the name of the
    AWS account to which you assigned the `codecatalyst-eks-user` user and
    permission set. 7. Next to `codecatalyst-eks-permission-set`, choose **Command
    line or programmatic access**. 8. Copy the commands in the middle of the page. They look similar to the
    following:

    ```
    export AWS_ACCESS_KEY_ID="AKIAIOSFODNN7EXAMPLE"
    export AWS_SECRET_ACCESS_KEY="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
    export AWS_SESSION_TOKEN="`session-token`"
    ```

    ...where `session-token` is a long random string.

5.  Add the access keys and session token to the AWS CLI, as follows:
    1. Return to your CodeCatalyst Dev Environment.
    2. At the terminal prompt, paste the commands you copied. Press Enter.

    You have now configured the AWS CLI with access keys and a session token. You can
    now use AWS CLI to complete the tasks required by this tutorial.

    ###### Important

    If at any time during this tutorial you see messages similar to:

    `Unable to locate credentials. You can configure credentials by running
 "aws configure".`

    Or:

    `ExpiredToken: The security token included in the request is
 expired`

    ...it's because your AWS CLI session has expired. In this case, do
    _not_ run the `aws configure` command. Instead, use
    the instructions in step 4 of this procedure that starts with `Obtain
 codecatalyst-eks-user's access key and session token` to refresh your
    session.

## Step 2: Create an Amazon EKS cluster

In this section, you create a cluster in Amazon EKS. The instructions below describe a quick
way to create the cluster using `eksctl`, but if you want detailed instructions,
see:

- [Getting started with eksctl](../../../eks/latest/userguide/getting-started-eksctl.md "../../../eks/latest/userguide/getting-started-eksctl.md") in the **Amazon EKS User Guide**

or

- [Getting started with the console and AWS CLI](../../../eks/latest/userguide/getting-started-console.md "../../../eks/latest/userguide/getting-started-console.md") in the
  **Amazon EKS User Guide** (this topic provides `kubectl`
  instructions for creating the cluster)

###### Note

[Private
clusters](../../../eks/latest/userguide/private-clusters.md "../../../eks/latest/userguide/private-clusters.md") are not supported by the CodeCatalyst integration with Amazon EKS.

**Before you begin**

Make sure you have completed the following tasks on your development machine:

- Installed the `eksctl` utility.
- Installed the `kubectl` utility.
- Installed the AWS CLI and configured it with access keys and a session token.

For information on how to complete these tasks, see [Step 1: Set up your development
machine](#deploy-tut-eks-dev-env-create "#deploy-tut-eks-dev-env-create").

###### To create a cluster

###### Important

Do not use the Amazon EKS service's user interface to create the cluster because the
cluster won't be configured correctly. Use the `eksctl` utility, as described
in the following steps.

1. Go to your Dev Environment.
2. Create a cluster and nodes:

```
eksctl create cluster --name `codecatalyst-eks-cluster` --region `us-west-2`
```

Where:

    * `codecatalyst-eks-cluster` is replaced with the name
     you want to give your cluster.
    * `us-west-2` is replaced with your Region.

After 10-20 minutes, a message similar to the following appears:

`EKS cluster "codecatalyst-eks-cluster" in "us-west-2" region is
 ready`

###### Note

You will see multiple `waiting for CloudFormation stack` messages while AWS
creates your cluster. This is expected. 3. Verify that your cluster was created successfully:

```
kubectl cluster-info
```

You will see a message similar to the following, indicating a sucessful cluster
creation:

```
Kubernetes master is running at https://`long-string`.gr7.us-west-2.eks.amazonaws.com
CoreDNS is running at https://`long-string`.gr7.us-west-2.eks.amazonaws.com/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy
```

## Step 3: Create an Amazon ECR image repository

In this section, you create a private image repository in Amazon Elastic Container Registry (Amazon ECR). This
repository stores the Docker image for the tutorial.

For more information about Amazon ECR, see the _Amazon Elastic Container Registry User Guide_.

###### To create an image repository in Amazon ECR

1. Go to your Dev Environment.
2. Create an empty repository in Amazon ECR:

```
aws ecr create-repository --repository-name `codecatalyst-eks-image-repo`
```

Replace `codecatalyst-eks-image-repo` with the name you
want to give the Amazon ECR repository.

This tutorial assumes you named your repository
`codecatalyst-eks-image-repo`. 3. Display the Amazon ECR repository’s details:

```
aws ecr describe-repositories \
      --repository-names codecatalyst-eks-image-repo

```

4. Note the `“repositoryUri”:` value, for example,
   `111122223333.dkr.ecr.us-west-2.amazonaws.com/codecatalyst-eks-image-repo`.

You need it later when adding the repository to your workflow.

## Step 4: Add source files

In this section, you add application source files to your source repository
(`codecatalyst-eks-source-repository`). They consist of:

- An `index.html` file – Displays a 'Hello, World!' message in
  the browser.
- A Dockerfile – Describes the base image to use for your Docker image and the
  Docker commands to apply to it.
- A `deployment.yaml` file – The Kubernetes manifest that
  defines the Kubernetes service and deployment.

The folder structure is as follows:

```
|— codecatalyst-eks-source-repository
   |— Kubernetes
      |— deployment.yaml
   |— public-html
   |  |— index.html
   |— Dockerfile

```

###### Topics

- [index.html](#deploy-tut-eks-source-files-index "#deploy-tut-eks-source-files-index")
- [Dockerfile](#deploy-tut-eks-source-files-dockerfile "#deploy-tut-eks-source-files-dockerfile")
- [deployment.yaml](#deploy-tut-eks-source-files-deployment-yml "#deploy-tut-eks-source-files-deployment-yml")

### index.html

The `index.html` file displays a 'Hello, World!' message in the
browser.

###### To add the index.html file

1. Go to your Dev Environment.
2. In `codecatalyst-eks-source-repository`, create a folder called
   `public-html`.
3. In `/public-html`, create a file called
   `index.html` with the following contents:

```
<html>
  <head>
    <title>Hello World</title>
    <style>
      body {
      background-color: black;
      text-align: center;
      color: white;
      font-family: Arial, Helvetica, sans-serif;
      }
    </style>
  </head>
  <body>
    <h1>Hello, World!</h1>
  </body>
</html>
```

4. At the terminal prompt, enter:

```
cd /projects/codecatalyst-eks-source-repository
```

5. Add, commit, and push:

```
git add .
git commit -m "add public-html/index.html"
git push
```

The `index.html` is added to your repository in a
`public-html` folder.

### Dockerfile

The Dockerfile describes the base Docker image to use and the Docker commands to apply
to it. For more information about the Dockerfile, see the [Dockerfile
Reference](https://docs.docker.com/engine/reference/builder/ "https://docs.docker.com/engine/reference/builder/").

The Dockerfile specified here indicates to use the Apache 2.4 base image
(`httpd`). It also includes instructions for copying a source file called
`index.html` to a folder on the Apache server that serves webpages. The
`EXPOSE` instruction in the Dockerfile tells Docker that the container is
listening on port 80.

###### To add the Dockerfile

1. In `codecatalyst-eks-source-repository`, create a file called
   `Dockerfile` with the following contents:

```
FROM httpd:2.4
COPY ./public-html/index.html /usr/local/apache2/htdocs/index.html
EXPOSE 80
```

Do not include a file extension.

###### Important

The Dockerfile must reside in your repository’s root folder. The workflow’s
`Docker build` command expects it to be there. 2. Add, commit, and push:

```
git add .
git commit -m "add Dockerfile"
git push
```

The Dockerfile is added to your repository.

### deployment.yaml

In this section, you add a `deployment.yaml` file to your repository.
The `deployment.yaml` file is a Kubernetes manifest that defines two Kubernetes
resources types or _kinds_ to run: a 'service' and a
'deployment'.

- The 'service' deploys a load balancer into Amazon EC2. The load balancer provides you
  with an Internet-facing public URL and standard port (port 80) that you can use to
  browse to the 'Hello, World!' application.
- The 'deployment' deploys three pods, and each pod will contain a Docker container
  with the 'Hello, World!' application. The three pods are deployed onto the nodes that
  were created when you created the cluster.

The manifest in this tutorial is short; however, a manifest can include any number of
Kubernetes resource types, such as pods, jobs, ingresses, and network policies. Further, you can
use multiple manifest files if your deployment is complex.

###### To add a deployment.yaml file

1. In `codecatalyst-eks-source-repository`, create a folder called
   `Kubernetes`.
2. In `/Kubernetes`, create a file called
   `deployment.yaml` with the following contents:

```
apiVersion: v1
kind: Service
metadata:
  name: my-service
  labels:
    app: my-app
spec:
  type: LoadBalancer
  selector:
    app: my-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-deployment
  labels:
    app: my-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: codecatalyst-eks-container
        # The $REPOSITORY_URI and $IMAGE_TAG placeholders will be replaced by actual values supplied by the build action in your workflow
        image: $REPOSITORY_URI:$IMAGE_TAG
        ports:
        - containerPort: 80
```

3. Add, commit, and push:

```
git add .
git commit -m "add Kubernetes/deployment.yaml"
git push
```

The `deployment.yaml` file is added to your repository in a
folder called `Kubernetes`.

You have now added all your source files.

Take a moment to double-check your work and make sure you placed all the files in the
correct folders. The folder structure is as follows:

```
|— codecatalyst-eks-source-repository
   |— Kubernetes
      |— deployment.yaml
   |— public-html
   |  |— index.html
   |— Dockerfile

```

## Step 5: Create AWS roles

In this section, you create AWS IAM roles that your CodeCatalyst workflow will need in order
to function. These roles are:

- **Build role** – Grants the CodeCatalyst build action
  (in the workflow) permission to access your AWS account and write to Amazon ECR and
  Amazon EC2.
- **Deploy role** – Grants the CodeCatalyst **Deploy to Kubernetes cluster** action (in the workflow) permission to
  access your AWS account and Amazon EKS.

For more information about IAM roles, see [IAM roles](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") in the _AWS Identity and Access Management User
Guide_.

###### Note

To save time, you can create a single role, called the `CodeCatalystWorkflowDevelopmentRole-`spaceName`` role, instead of
 the two roles listed previously. For more information, see [Creating the CodeCatalystWorkflowDevelopmentRole-spaceName role for your account
 and space](ipa-iam-roles.md#ipa-iam-roles-service-create "ipa-iam-roles.md#ipa-iam-roles-service-create").
 Understand that the `CodeCatalystWorkflowDevelopmentRole-`spaceName`` role has very broad permissions which may pose a security
risk. We recommend that you only use this role in tutorials and scenarios where security is
less of a concern. This tutorial assumes you are creating the two roles listed
previously.

To create the build and deploy roles, complete the following series of procedures.

###### 1. To create a trust policy for both roles

1. Go to your Dev Environment.
2. In the `Cloud9-`long-string``directory,
create a file called`codecatalyst-eks-trust-policy.json` with the
   following contents:

###### 2. To create the build policy for the build role

- In the `Cloud9-`long-string``directory,
create a file called`codecatalyst-eks-build-policy.json` with the
  following contents:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ecr:*",
 "ec2:*"
 ],
 "Resource": "*"
 }
 ]
}`

```

###### Note

The first time the role is used to run workflow actions, use the wildcard in the
resource policy statement and then scope down the policy with the resource name after it
is available.

```
"Resource": "*"
```

###### 3. To create the deploy policy for the deploy role

- In the `Cloud9-`long-string``directory,
create a file called`codecatalyst-eks-deploy-policy.json` with the
  following contents:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "eks:DescribeCluster",
 "eks:ListClusters"
 ],
 "Resource": "*"
 }
 ]
}`

```

###### Note

The first time the role is used to run workflow actions, use the wildcard in the
resource policy statement and then scope down the policy with the resource name after it
is available.

```
"Resource": "*"
```

You have now added three policy documents to your Dev Environment. Your directory structure
now looks like this:

```
|— Cloud9-`long-string`
   |— .c9
   |— codecatalyst-eks-source-repository
      |— Kubernetes
      |— public-html
      |— Dockerfile
   codecatalyst-eks-build-policy.json
   codecatalyst-eks-deploy-policy.json
   codecatalyst-eks-trust-policy.json

```

###### 4. To add the build policy to AWS

1. In the Dev Environment terminal, enter:

```
cd /projects
```

2. Enter:

```
aws iam create-policy \
    --policy-name codecatalyst-eks-build-policy \
    --policy-document file://codecatalyst-eks-build-policy.json
```

3. Press **Enter**.
4. In the command output, note the `"arn":` value, for example,
   `arn:aws:iam::111122223333:policy/codecatalyst-eks-build-policy`.
   You need this ARN later.

###### 5. To add the deploy policy to AWS

1. Enter:

```
aws iam create-policy \
    --policy-name codecatalyst-eks-deploy-policy \
    --policy-document file://codecatalyst-eks-deploy-policy.json
```

2. Press **Enter**.
3. In the command output, note the deploy policy's `"arn":` value, for
   example,
   `arn:aws:iam::111122223333:policy/codecatalyst-eks-deploy-policy`.
   You need this ARN later.

###### 6. To create the build role

1. Enter:

```
aws iam create-role \
      --role-name codecatalyst-eks-build-role \
      --assume-role-policy-document file://codecatalyst-eks-trust-policy.json
```

2. Press **Enter**.
3. Enter:

```
aws iam attach-role-policy \
      --role-name codecatalyst-eks-build-role \
      --policy-arn `arn:aws:iam::111122223333:policy/codecatalyst-eks-build-policy`
```

Where
`arn:aws:iam::111122223333:policy/codecatalyst-eks-build-policy`
is replaced with the ARN of the build policy you noted earlier. 4. Press **Enter**. 5. At the terminal prompt, enter:

```
aws iam get-role \
      --role-name codecatalyst-eks-build-role
```

6. Press **Enter**.
7. Note the role's `"Arn":` value, for example,
   `arn:aws:iam::111122223333:role/codecatalyst-eks-build-role`.
   You need this ARN later.

###### 7. To create the deploy role

1. Enter:

```
aws iam create-role \
      --role-name codecatalyst-eks-deploy-role \
      --assume-role-policy-document file://codecatalyst-eks-trust-policy.json
```

2. Press **Enter**.
3. Enter:

```
aws iam attach-role-policy \
      --role-name codecatalyst-eks-deploy-role \
      --policy-arn `arn:aws:iam::111122223333:policy/codecatalyst-eks-deploy-policy`
```

Where
`arn:aws:iam::111122223333:policy/codecatalyst-eks-deploy-policy`
is replaced with the ARN of the deploy policy you noted earlier. 4. Press **Enter**. 5. Enter:

```
aws iam get-role \
      --role-name codecatalyst-eks-deploy-role
```

6. Press **Enter**.
7. Note the role's `"Arn":` value, for example,
   `arn:aws:iam::111122223333:role/codecatalyst-eks-deploy-role`.
   You need this ARN later.

You have now created build and deploy roles and noted their ARNs.

## Step 6: Add AWS roles to CodeCatalyst

In this step, you add the build role (`codecatalyst-eks-build-role`) and
deploy role (`codecatalyst-eks-deploy-role`) to the AWS account that you
connected to your space. This makes the roles available for use in your workflow.

###### To add build and deploy roles to your AWS account

1. In the CodeCatalyst console, navigate to your space.
2. At the top, choose **Settings**.
3. In the navigation pane, choose **AWS accounts**. A list of accounts
   appears.
4. In the **Amazon CodeCatalyst display name** column, copy the display name of
   the AWS account where you created your build and deploy roles. (It might be a number.)
   You'll need this value later, when creating your workflow.
5. Choose the display name.
6. Choose **Manage roles from AWS management console**.

The **Add IAM role to Amazon CodeCatalyst space** page appears. You
might need to sign in to access the page. 7. Select **Add an existing role you have created in IAM**.

A drop-down list appears. The list displays the build and deploy roles, and any other
IAM roles with a trust policy that includes the
`codecatalyst-runner.amazonaws.com` and
`codecatalyst.amazonaws.com` service principals. 8. From the drop-down list, add:

    * `codecatalyst-eks-build-role`
    * `codecatalyst-eks-deploy-role`

###### Note

If you see `The security token included in the request is invalid`, it
might be because you do not have the right permissions. To fix this issue, sign out of
AWS as sign back in with the AWS account that you used when you created your CodeCatalyst
space. 9. Return to the CodeCatalyst console and refresh the page.

The build and deploy roles should now appear under **IAM
roles**.

These roles are now available for use in CodeCatalyst workflows.

## Step 7: Update the ConfigMap

You must add the deploy role that you created in [Step 5: Create AWS roles](#deploy-tut-eks-roles "#deploy-tut-eks-roles") to the Kubernetes `ConfigMap` file to
give the **Deploy to Kubernetes cluster** action (in your workflow) the ability to
access and interact with your cluster. You can use `eksctl` or `kubectl`
to perform this task.

###### To configure the Kubernetes ConfigMap file using eksctl

- In the Dev Environment terminal, enter:

```
eksctl create iamidentitymapping --cluster `codecatalyst-eks-cluster` --arn `arn:aws:iam::111122223333:role/codecatalyst-eks-deploy-role` --group system:masters --username `codecatalyst-eks-deploy-role` --region `us-west-2`
```

Where:

    + `codecatalyst-eks-cluster` is replaced with the
     cluster name of the Amazon EKS cluster.
    + `arn:aws:iam::111122223333:role/codecatalyst-eks-deploy-role`
     is replaced with the ARN of the deploy role that you created in [Step 5: Create AWS roles](#deploy-tut-eks-roles "#deploy-tut-eks-roles").
    + `codecatalyst-eks-deploy-role` (next to
     `--username`) is replaced with the name of the deploy role that you
     created in [Step 5: Create AWS roles](#deploy-tut-eks-roles "#deploy-tut-eks-roles").


    ###### Note

    If you decided not to create a deploy role, replace
     `codecatalyst-eks-deploy-role` with the name of the
     `CodeCatalystWorkflowDevelopmentRole-`spaceName`` role. For more information about this role, see [Step 5: Create AWS roles](#deploy-tut-eks-roles "#deploy-tut-eks-roles").
    + `us-west-2` is replaced with your Region.

For details on this command, see [Manage IAM users and
roles](https://eksctl.io/usage/iam-identity-mappings/ "https://eksctl.io/usage/iam-identity-mappings/").

A message similar to the following appears:

```
2023-06-09 00:58:29 [ℹ]  checking arn arn:aws:iam::111122223333:role/codecatalyst-eks-deploy-role against entries in the auth ConfigMap
2023-06-09 00:58:29 [ℹ]  adding identity "arn:aws:iam::111122223333:role/codecatalyst-eks-deploy-role" to auth ConfigMap
```

###### To configure the Kubernetes ConfigMap file using kubectl

1. In the Dev Environment terminal, enter:

```
kubectl edit configmap -n kube-system aws-auth
```

The ConfigMap file appears on the screen. 2. Add the text in red italics:

```
# Please edit the object below. Lines beginning with a '#' will be ignored,
# and an empty file will abort the edit. If an error occurs while saving this file will be
# reopened with the relevant failures.
#
apiVersion: v1
data:
  mapRoles: |
    - groups:
      - system:bootstrappers
      - system:nodes
      rolearn: arn:aws:iam::111122223333:role/eksctl-codecatalyst-eks-cluster-n-NodeInstanceRole-16BC456ME6YR5
      username: system:node:{{EC2PrivateDNSName}}
    - groups:
      - system:masters
      rolearn: arn:aws:iam::111122223333:role/codecatalyst-eks-deploy-role
      username: codecatalyst-eks-deploy-role
  mapUsers: |
    []
kind: ConfigMap
metadata:
  creationTimestamp: "2023-06-08T19:04:39Z"
  managedFields:
  ...
```

Where:

    * `arn:aws:iam::111122223333:role/codecatalyst-eks-deploy-role`
     is replaced with the ARN of the deploy role that you created in [Step 5: Create AWS roles](#deploy-tut-eks-roles "#deploy-tut-eks-roles").
    * `codecatalyst-eks-deploy-role` (next to
     `username:`)is replaced with the name of the deploy role that you created
     in [Step 5: Create AWS roles](#deploy-tut-eks-roles "#deploy-tut-eks-roles").


    ###### Note

    If you decided not to create a deploy role, replace
     `codecatalyst-eks-deploy-role` with the name of the
     `CodeCatalystWorkflowDevelopmentRole-`spaceName`` role. For more information about this role, see [Step 5: Create AWS roles](#deploy-tut-eks-roles "#deploy-tut-eks-roles").

For details, see [Enabling IAM principal access to your
cluster](../../../eks/latest/userguide/add-user-role.md "../../../eks/latest/userguide/add-user-role.md") in the **Amazon EKS User Guide**.

You have now given the deploy role, and by extension the **Deploy to
Amazon EKS** action, `system:masters` permissions to your Kubernetes
cluster.

## Step 8: Create and run a workflow

In this step, you create a workflow that takes your source files, builds them into a
Docker image, and then deploys the image into tree pods in your Amazon EKS cluster.

The workflow consists of the following building blocks that run sequentially:

- A trigger – This trigger starts the workflow run automatically when you push a
  change to your source repository. For more information about triggers, see [Starting a workflow run automatically using
  triggers](workflows-add-trigger.md "workflows-add-trigger.md").
- A build action (`BuildBackend`) – On trigger, the action builds the
  Docker image using the Dockerfile and pushes the image to Amazon ECR. The build action also
  updates the `$REPOSITORY_URI` and `$IMAGE_TAG` variables in the
  `deployment.yaml` file with the correct values, and then creates an output
  artifact of this file and any others in the `Kubernetes` folder. In this
  tutorial, the only file in the `Kubernetes` folder is
  `deployment.yaml` but you could include more files. The artifact is
  used as the input for the deploy action, which is next.

For more information about the build action, see [Building with workflows](build-workflow-actions.md "build-workflow-actions.md").

- A deploy action (`DeployToEKS`) – On completion of the build action,
  the deploy action looks for the output artifact generated by the build action
  (`Manifests`), and finds the `deployment.yaml` file inside
  of it. The action then follows the instructions in the
  `deployment.yaml` file to run three pods—each containing a single
  'Hello, World!' Docker container—inside your Amazon EKS cluster.

###### To create a workflow

1. Go to the CodeCatalyst console.
2. Navigate to your project (`codecatalyst-eks-project`).
3. In the navigation pane, choose **CI/CD**, and then choose
   **Workflows**.
4. Choose **Create workflow**.
5. For **Source repository**, choose
   `codecatalyst-eks-source-repository`.
6. For **Branch**, choose `main`.
7. Choose **Create**.
8. Delete the YAML sample code.
9. Add the following YAML code to create a new workflow definition file:

###### Note

For more information about the workflow definition file, see [Workflow YAML definition](workflow-reference.md "workflow-reference.md").

###### Note

In the YAML code that follows, you can omit the `Connections:` sections
if you want. If you omit these sections, you must ensure that the role specified in the
**Default IAM role** field in your environment includes the
permissions and trust policies of both roles described in [Step 6: Add AWS roles to CodeCatalyst](#deploy-tut-eks-import-roles "#deploy-tut-eks-import-roles").
For more information about setting up an environment with a default IAM role, see
[Creating an environment](deploy-environments-creating-environment.md "deploy-environments-creating-environment.md").

```
Name: codecatalyst-eks-workflow
SchemaVersion: 1.0

Triggers:
  - Type: PUSH
    Branches:
      - main
Actions:
  BuildBackend:
    Identifier: aws/build@v1
    Environment:
      Name: `codecatalyst-eks-environment`
      Connections:
        - Name: `codecatalyst-account-connection`
          Role: `codecatalyst-eks-build-role`
    Inputs:
      Sources:
        - WorkflowSource
      Variables:
        - Name: REPOSITORY_URI
          Value: `111122223333.dkr.ecr.us-west-2.amazonaws.com/codecatalyst-eks-image-repo`
        - Name: IMAGE_TAG
          Value: ${WorkflowSource.CommitId}
    Configuration:
      Steps:
        #pre_build:
        - Run: echo Logging in to Amazon ECR...
        - Run: aws --version
        - Run: aws ecr get-login-password --region `us-west-2` | docker login --username AWS --password-stdin `111122223333.dkr.ecr.us-west-2.amazonaws.com`
        #build:
        - Run: echo Build started on `date`
        - Run: echo Building the Docker image...
        - Run: docker build -t $REPOSITORY_URI:latest .
        - Run: docker tag $REPOSITORY_URI:latest $REPOSITORY_URI:$IMAGE_TAG
        #post_build:
        - Run: echo Build completed on `date`
        - Run: echo Pushing the Docker images...
        - Run: docker push $REPOSITORY_URI:latest
        - Run: docker push $REPOSITORY_URI:$IMAGE_TAG
        # Replace the variables in deployment.yaml
        - Run: find Kubernetes/ -type f | xargs sed -i "s|\$REPOSITORY_URI|$REPOSITORY_URI|g"
        - Run: find Kubernetes/ -type f | xargs sed -i "s|\$IMAGE_TAG|$IMAGE_TAG|g"
        - Run: cat Kubernetes/*
        # The output artifact will be a zip file that contains Kubernetes manifest files.
    Outputs:
      Artifacts:
        - Name: Manifests
          Files:
            - "Kubernetes/*"
  DeployToEKS:
    DependsOn:
      - BuildBackend
    Identifier: aws/kubernetes-deploy@v1
    Environment:
      Name: `codecatalyst-eks-environment`
      Connections:
        - Name: `codecatalyst-account-connection`
          Role: `codecatalyst-eks-deploy-role`
    Inputs:
      Artifacts:
        - Manifests
    Configuration:
      Namespace: default
      Region: `us-west-2`
      Cluster: codecatalyst-eks-cluster
      Manifests: Kubernetes/
```

In the preceding code, replace:

    * Both instances of `codecatalyst-eks-environment` with
     the name of the environment you created in [Prerequisites](#deploy-tut-eks-prereqs "#deploy-tut-eks-prereqs").
    * Both instances of `codecatalyst-account-connection`
     with the display name of your account connection. The display name might be a number.
     For more information, see [Step 6: Add AWS roles to CodeCatalyst](#deploy-tut-eks-import-roles "#deploy-tut-eks-import-roles").
    * `codecatalyst-eks-build-role` with the name of the
     build role you created in [Step 5: Create AWS roles](#deploy-tut-eks-roles "#deploy-tut-eks-roles").
    * `111122223333.dkr.ecr.us-west-2.amazonaws.com/codecatalyst-eks-image-repo`
     (in the `Value:` property) with the URI of the Amazon ECR repository you created
     in [Step 3: Create an Amazon ECR image repository](#deploy-tut-eks-ecr "#deploy-tut-eks-ecr").
    * `111122223333.dkr.ecr.us-west-2.amazonaws.com`
     (in the `Run: aws ecr` command) with the URI of the Amazon ECR repository
     without the image suffix (`/codecatalyst-eks-image-repo`).
    * `codecatalyst-eks-deploy-role` with the name of the
     deploy role you created in [Step 5: Create AWS roles](#deploy-tut-eks-roles "#deploy-tut-eks-roles").
    * Both instances of `us-west-2` with your AWS Region
     code. For a list of Region codes, see [Regional endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md") in the
     *AWS General Reference*.

###### Note

If you decided not to create build and deploy roles, replace
`codecatalyst-eks-build-role` and
`codecatalyst-eks-deploy-role` with the name of the
`CodeCatalystWorkflowDevelopmentRole-`spaceName`` role. For more information about this role, see [Step 5: Create AWS roles](#deploy-tut-eks-roles "#deploy-tut-eks-roles"). 10. (Optional) Choose **Validate** to make sure that the YAML code is
valid before committing. 11. Choose **Commit**. 12. In the **Commit workflow** dialog box, enter the following:

    1. For **Commit message**, remove the text and enter:



    ```
    `Add first workflow`
    ```
    2. For **Repository**, choose
     `codecatalyst-eks-source-repository`.
    3. For **Branch name**, choose main.
    4. Choose **Commit**.You have now created a workflow. A workflow run starts automatically because of the

trigger defined at the top of the workflow. Specifically, when you committed (and pushed)
the `workflow.yaml` file to your source repository, the trigger started
the workflow run.

###### To view the workflow run progress

1. In the navigation pane of the CodeCatalyst console, choose **CI/CD**, and
   then choose **Workflows**.
2. Choose the workflow you just created,
   `codecatalyst-eks-workflow`.
3. Choose **BuildBackend** to see the build progress.
4. Choose **DeployToEKS** to see the deployment progress.

For more information about viewing run details, see [Viewing workflow run status and details](workflows-view-run.md "workflows-view-run.md").

###### To verify the deployment

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the left, near the bottom, choose **Load Balancers**.
3. Select the load balancer that was created as part of your Kubernetes deployment. If you're
   not sure which load balancer to choose, look for the following tags under the
   **Tags** tab:
   - `kubernetes.io/service-name`
   - `kubernetes.io/cluster/ekstutorialcluster`

4. With the correct load balancer selected, choose the **Description**
   tab.
5. Copy and paste the **DNS name** value into your browser's address
   bar.

The 'Hello, World!' webpage appears in your browser, indicating that you successfully
deployed your application.

## Step 9: Make a change to your source files

In this section, you make a change to the `index.html` file in your
source repository. This change causes the workflow to build a new Docker image, tag it with a
commit ID, push it to Amazon ECR, and deploy it to Amazon ECS.

###### To change the index.html

1. Go to your Dev Environment.
2. At the terminal prompt, change to your source repository:

```
cd /projects/codecatalyst-eks-source-repository
```

3. Pull the latest workflow changes:

```
git pull
```

4. Open
   `codecatalyst-eks-source-repository/public-html/index.html`.
5. On line 14, change the `Hello, World!` text to `Tutorial
complete!`.
6. Add, commit, and push:

```
git add .
git commit -m "update index.html title"
git push
```

A workflow run starts automatically. 7. (Optional) Enter:

```
git show HEAD
```

Note the commit ID for the `index.html` change. This commit ID will
be tagged to the Docker image that will be deployed by the workflow run that you just
started. 8. Watch the deployment progress:

    1. In the CodeCatalyst console, in the navigation pane, choose **CI/CD**,
     and then choose **Workflows**.
    2. Choose `codecatalyst-eks-workflow` to view the latest run.
    3. Choose **BuildBackend**, and **DeployToEKS** to
     see the workflow run progress.

9. Verify that your application was updated, as follows:
   1. Open the Amazon EC2 console at
      [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
   2. On the left, near the bottom, choose **Load Balancers**.
   3. Select the load balancer that was created as part of your Kubernetes deployment.
   4. Copy and paste the **DNS name** value into your browser's address
      bar.

   The 'Tutorial Complete!' webpage appears in your browser, indicating that you
   successfully deployed a new revision of your application.

10. (Optional) In AWS, switch to the Amazon ECR console and verify that the new Docker image
    was tagged with the commit ID from step 7 of this procedure.

## Clean up

You should clean up your environment so that you're not charged unnecessarily for the
storage and compute resources used by this tutorial.

###### To clean up

1.  Delete your cluster:
    1. In the Dev Environment terminal, enter:

    ```
    eksctl delete cluster --region=`us-west-2` --name=`codecatalyst-eks-cluster`
    ```

    Where:

        * `us-west-2` is replaced with your Region.
        * `codecatalyst-eks-cluster` is replaced with the
         name of the cluster you created.

    After 5-10 minutes, the cluster and associated resources are deleted, including
    but not limited to CloudFormation stacks, nodes groups (in Amazon EC2), and load balancers.###### Important

If the `eksctl delete cluster` command doesn't work, you may need to
refresh your AWS credentials or your `kubectl` credentials. If you're not
sure which credentials to refresh, refresh the AWS credentials first. To refresh your
AWS credentials, see [How do I fix "Unable to
locate credentials" and "ExpiredToken" errors?](troubleshooting-workflows.md#troubleshooting-workflows-auth-errors-eks "troubleshooting-workflows.md#troubleshooting-workflows-auth-errors-eks"). To refresh your
`kubectl` credentials, see [How do I fix "Unable to
connect to the server" errors?](troubleshooting-workflows.md#troubleshooting-workflows-unable-connect-eks "troubleshooting-workflows.md#troubleshooting-workflows-unable-connect-eks"). 2. In the AWS console, clean up as follows:

    1. In Amazon ECR, delete `codecatalyst-eks-image-repo`.
    2. In IAM Identity Center, delete:




    	1. `codecatalyst-eks-user`
    	2. `codecatalyst-eks-permission-set`
    3. In IAM, delete:




    	* `codecatalyst-eks-build-role`
    	* `codecatalyst-eks-deploy-role`
    	* `codecatalyst-eks-build-policy`
    	* `codecatalyst-eks-deploy-policy`

3. In the CodeCatalyst console, clean up as follows:
   1. Delete `codecatalyst-eks-workflow`.
   2. Delete `codecatalyst-eks-environment`.
   3. Delete `codecatalyst-eks-source-repository`.
   4. Delete your Dev Environment.
   5. Delete `codecatalyst-eks-project`.

In this tutorial, you learned how to deploy an application to an Amazon EKS service using a
CodeCatalyst workflow and a **Deploy to Kubernetes cluster** action.
