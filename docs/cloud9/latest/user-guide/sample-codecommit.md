AWS Cloud9 is no longer available to new customers. Existing customers of
AWS Cloud9 can continue to use the service as normal.
[Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")

# AWS CodeCommit tutorial for AWS Cloud9

You can use the AWS CodeCommit tutorial to set up an AWS Cloud9 development environment to interact with a remote code
repository in CodeCommit. CodeCommit is a source code control service that you can use to privately
store and manage Git repositories in the AWS Cloud. For more information
about CodeCommit, see the [AWS CodeCommit User Guide](../../../codecommit/latest/userguide.md "../../../codecommit/latest/userguide.md").

Following this tutorial and creating this sample might result in charges to your AWS account. These include possible
charges for services such as Amazon EC2 and CodeCommit. For more information, see [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/ "https://aws.amazon.com/ec2/pricing/") and [AWS CodeCommit Pricing](https://aws.amazon.com/codecommit/pricing/ "https://aws.amazon.com/codecommit/pricing/").

- [Prerequisites](#sample-codecommit-prereqs "#sample-codecommit-prereqs")
- [Step 1: Set up your IAM group with
  required access permissions](#sample-codecommit-permissions "#sample-codecommit-permissions")
- [Step 2: Create a repository in AWS CodeCommit](#sample-codecommit-create-repo "#sample-codecommit-create-repo")
- [Step 3: Connect your environment to the
  remote repository](#sample-codecommit-connect-repo "#sample-codecommit-connect-repo")
- [Step 4: Clone the remote repository into
  your environment](#sample-codecommit-clone-repo "#sample-codecommit-clone-repo")
- [Step 5: Add files to the repository](#sample-codecommit-add-files "#sample-codecommit-add-files")
- [Step 6: Clean up](#sample-codecommit-clean-up "#sample-codecommit-clean-up")

## Prerequisites

Before you use this sample, make sure that your setup meets the following
requirements:

- **You must have an existing AWS Cloud9 EC2 development environment.** This sample
  assumes that you already have an EC2 environment that's connected to an Amazon EC2 instance that
  runs Amazon Linux or Ubuntu Server. If you have a different type of environment or
  operating system, you might need to adapt this sample's instructions to set up related
  tools. For more information, see [Creating an environment in AWS Cloud9](create-environment.md "create-environment.md").
- **You have the AWS Cloud9 IDE for the existing environment already
  open.** When you open an environment, AWS Cloud9 opens the IDE for that environment in your
  web browser. For more information, see [Opening an environment in AWS Cloud9](open-environment.md "open-environment.md").

## Step 1: Set up your IAM group with

required access permissions

Suppose that your AWS credentials are associated with an administrator user in your
AWS account, and you want to use that user to work with CodeCommit Then, skip ahead to [Step 2: Create a Repository in
AWS CodeCommit](#sample-codecommit-create-repo "#sample-codecommit-create-repo").

You can complete this step using the [AWS Management Console](#sample-codecommit-permissions-console "#sample-codecommit-permissions-console") or the
[AWS Command Line Interface (AWS CLI)](#sample-codecommit-permissions-cli "#sample-codecommit-permissions-cli").

### Set up your IAM group with

required access permissions using the console

1. Sign in to the AWS Management Console, if you aren't already signed in.

For this step, we recommend you sign in using credentials for an administrator
user in your AWS account. If you cannot do this, check with your AWS account
administrator. 2. Open the IAM console. To do this, in the console's navigation bar, choose
**Services**. Then, choose **IAM**. 3. Choose **Groups**. 4. Choose the group's name. 5. On the **Permissions** tab, for **Managed
Policies**, choose **Attach Policy**. 6. In the list of policy names, select one of the following boxes:

    * Select **AWSCodeCommitPowerUser** for access to all of
     the functionality of CodeCommit and repository-related resources. However, this
     doesn't allow you to delete CodeCommit repositories or create or delete
     repository-related resources in other AWS services, such as
     Amazon CloudWatch Events.
    * Select **AWSCodeCommitFullAccess** for full control over
     CodeCommit repositories and related resources in the AWS account. This includes
     the ability to delete repositories.

If you don't see either of these policy names in the list, enter the policy
names in the **Filter** box to display them. 7. Choose **Attach Policy**.

To see the list of access permissions that these AWS managed policies give to a
group, see [AWS Managed (Predefined) Policies for AWS CodeCommit](../../../codecommit/latest/userguide/auth-and-access-control-iam-identity-based-access-control.md#managed-policies "../../../codecommit/latest/userguide/auth-and-access-control-iam-identity-based-access-control.md#managed-policies") in the
_AWS CodeCommit User Guide_.

Skip ahead to [Step 2: Create a
Repository in AWS CodeCommit](#sample-codecommit-create-repo "#sample-codecommit-create-repo").

### Set up your IAM group with

required access permissions using the AWS CLI

Run the IAM `attach-group-policy` command, specifying the group's name and
the Amazon Resource Name (ARN) of the AWS managed policy that describes the required
access permissions. The syntax is as follows.

```
aws iam attach-group-policy --group-name MyGroup --policy-arn POLICY_ARN
```

In the preceding command, replace `MyGroup` with the name of the group.
Replace `POLICY_ARN` with the ARN of the AWS managed policy:

- `arn:aws:iam::aws:policy/AWSCodeCommitPowerUser` for access to all of
  the functionality of CodeCommit and repository-related resources. However, it doesn't
  allow you to delete CodeCommit repositories or create or delete repository-related
  resources in other AWS services, such as Amazon CloudWatch Events.
- `arn:aws:iam::aws:policy/AWSCodeCommitFullAccess` for full control over
  CodeCommit repositories and related resources in the AWS account. This includes the
  ability to delete repositories.

To see the list of access permissions that these AWS managed policies give to a
group, see [AWS Managed (Predefined) Policies for AWS CodeCommit](../../../codecommit/latest/userguide/auth-and-access-control-iam-identity-based-access-control.md#managed-policies "../../../codecommit/latest/userguide/auth-and-access-control-iam-identity-based-access-control.md#managed-policies") in the
_AWS CodeCommit User Guide_.

## Step 2: Create a repository in

CodeCommit

In this step, you create a remote code repository in CodeCommit by using the CodeCommit
console.

If you already have a CodeCommit repository, skip ahead to [Step 3: Connect Your Environment to the Remote
Repository](#sample-codecommit-connect-repo "#sample-codecommit-connect-repo").

You can complete this step using the [AWS Management Console](#sample-codecommit-create-repo-console "#sample-codecommit-create-repo-console") or the
[AWS Command Line Interface (AWS CLI)](#sample-codecommit-create-repo-cli "#sample-codecommit-create-repo-cli").

### Create a repository in CodeCommit

using the console

1. Suppose that you're signed in to the AWS Management Console as an administrator user from
   the previous step, and you don't want to use the administrator user to create the
   repository. Then, sign out of the AWS Management Console.
2. Open the CodeCommit console, at [https://console.aws.amazon.com/codecommit](https://console.aws.amazon.com/codecommit "https://console.aws.amazon.com/codecommit").
3. In the console's navigation bar, use the Region selector to choose the
   AWS Region that you want to create the repository in (for example, **US
   East (Ohio)**).
4. If a welcome page is displayed, choose **Get started**.
   Otherwise, choose **Create repository**.
5. On the **Create repository** page, for **Repository
   name**, enter a name for your new repository (for example,
   `MyDemoCloud9Repo`). If you choose a different name, substitute it
   throughout this sample.
6. (Optional) For **Description**, enter something about the
   repository. For example, you can enter: `This is a demonstration repository
for the AWS Cloud9 sample.`
7. Choose **Create repository**. A **Connect to your
   repository** pane is displayed. Choose **Close**, as
   you will connect to your repository in a different way later in this topic.

Skip ahead to [Step 3: Connect Your
Environment to the Remote Repository](#sample-codecommit-connect-repo "#sample-codecommit-connect-repo").

### Create a repository in CodeCommit using

the AWS CLI

Run the AWS CodeCommit `create-repository` command. Specify the repository's
name, an optional description, and the AWS Region to create the repository in.

```
aws codecommit create-repository --repository-name MyDemoCloud9Repo --repository-description "This is a demonstration repository for the AWS Cloud9 sample." --region us-east-2
```

In the preceding command, replace `us-east-2` with the ID of the
AWS Region to create the repository in. For a list of supported Regions, see [AWS CodeCommit](../../../general/latest/gr/rande.md#codecommit_region "../../../general/latest/gr/rande.md#codecommit_region") in the _Amazon Web Services General Reference_.

If you choose to use a different repository name, substitute it throughout this
sample.

## Step 3: Connect your environment to the remote

repository

In this step, you use the AWS Cloud9 IDE to connect to the CodeCommit repository that you created
or identified in the previous step.

###### Note

If you prefer working with Git through a visual interface, you can
clone the remote repository. Then, you can add files using the [Git panel](source-control-gitpanel.md "source-control-gitpanel.md") feature that's available in the
IDE.

Complete one of the following sets of procedures based on your type of
AWS Cloud9 development environment.

| **Environment type** | **Follow these procedures**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| EC2 environment      | 1. From a terminal session in the IDE, run the following two<br>commands:<br>`<br>git config --global credential.helper '!aws codecommit credential-helper $@'<br>git config --global credential.UseHttpPath true<br>`<br>For more information, see [Step 2: Configure the AWS CLI Credential Helper On Your AWS Cloud9<br>EC2 Development Environment](../../../codecommit/latest/userguide/setting-up-ide-c9.md#setting-up-ide-c9-credentials "../../../codecommit/latest/userguide/setting-up-ide-c9.md#setting-up-ide-c9-credentials") in *Integrate AWS Cloud9 with AWS CodeCommit<br>• in the<br>*AWS CodeCommit User Guide\*.<br>2. Skip ahead to [Step 4:<br>Clone the Remote Repository into Your Environment](#sample-codecommit-clone-repo "#sample-codecommit-clone-repo") later in<br>this topic.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| SSH environment      | 1. If Git isn't already installed in the environment, use a<br>terminal session in the IDE to install it. For more information, see<br>[Step 2: Install Git](../../../codecommit/latest/userguide/setting-up-ssh-unixes.md#setting-up-ssh-unixes-install-git "../../../codecommit/latest/userguide/setting-up-ssh-unixes.md#setting-up-ssh-unixes-install-git") in *Setup<br>Steps for SSH Connections to AWS CodeCommit Repositories on Linux,<br>macOS, or Unix<br>• in the<br>*AWS CodeCommit User Guide*.<br>2. Complete [Step 3: Configure Credentials on Linux, macOS, or Unix](../../../codecommit/latest/userguide/setting-up-ssh-unixes.md#setting-up-ssh-unixes-install-git "../../../codecommit/latest/userguide/setting-up-ssh-unixes.md#setting-up-ssh-unixes-install-git") in<br>*Setup Steps for SSH Connections to AWS CodeCommit Repositories on Linux, macOS, or Unix<br>• in the<br>_AWS CodeCommit User Guide_.<br>When you're instructed to sign in to the AWS Management Console and open the<br>IAM console, we recommend you sign in using credentials for an<br>administrator user in your AWS account. If you cannot do this, check<br>with your AWS account administrator.<br>3. Skip ahead to [Step 4:<br>Clone the Remote Repository into Your Environment](#sample-codecommit-clone-repo "#sample-codecommit-clone-repo") later in<br>this topic. |

## Step 4: Clone the remote repository into

your environment

In this step, you use the AWS Cloud9 IDE to clone the remote repository in CodeCommit into your
environment.

To clone the repository, run the **`git clone`**
command. Replace `*CLONE\_URL*` with the repository's clone
URL.

```
git clone CLONE_URL
```

For an EC2 environment, you supply an HTTPS clone URL that starts with `https://`.
For an SSH environment, you supply an SSH clone URL that starts with `ssh://`.

To get the repository's full clone URL, see [Use the AWS CodeCommit Console to View Repository Details](../../../codecommit/latest/userguide/how-to-view-repository-details.md#how-to-view-repository-details-console "../../../codecommit/latest/userguide/how-to-view-repository-details.md#how-to-view-repository-details-console") in the
_AWS CodeCommit User Guide_.

If your repository doesn't have any files in it, a warning message is displayed, such as
`You appear to have cloned an empty repository.` This is expected. You will
address later.

## Step 5: Add files to the repository

In this step, you create three simple files in the cloned repository in your AWS Cloud9
environment. Next, you add the files to the Git staging area in your cloned
repository. Last, you commit the staged files and push the commit to your remote repository
in CodeCommit.

If the cloned repository already has files in it, you're done and can skip the rest of
this sample.

###### To add files to the repository

1. Create a new file. On the menu bar, choose **File**,
   **New File**.
2. Enter the following content into the file, and then choose
   **File**, **Save** to save the file as
   `bird.txt` in the `MyDemoCloud9Repo`
   directory in your AWS Cloud9 environment.

```
bird.txt
--------
Birds are a group of endothermic vertebrates, characterized by feathers,
toothless beaked jaws, the laying of hard-shelled eggs, a high metabolic
rate, a four-chambered heart, and a lightweight but strong skeleton.
```

###### Note

To confirm that you're saving this file in the correct directory, in the
**Save As** dialog box, choose the
`MyDemoCloud9Repo` folder. Then, make sure
**Folder** displays
`/MyDemoCloud9Repo`. 3. Create two more files, named `insect.txt` and
`reptile.txt`, with the following content. Save the files in
the same `MyDemoCloud9Repo` directory.

```
insect.txt
----------
Insects are a class of invertebrates within the arthropod phylum that
have a chitinous exoskeleton, a three-part body (head, thorax, and abdomen),
three pairs of jointed legs, compound eyes, and one pair of antennae.
```

```
reptile.txt
-----------
Reptiles are tetrapod (four-limbed vertebrate) animals in the class
Reptilia, comprising today's turtles, crocodilians, snakes,
amphisbaenians, lizards, tuatara, and their extinct relatives.
```

4. In the terminal, run the **`cd`** command
   to switch to the `MyDemoCloud9Repo` directory.

```
cd MyDemoCloud9Repo
```

5. Confirm that the files were successfully saved in the
   `MyDemoCloud9Repo` directory by running the **`git status`** command. All three files will be listed as
   untracked files.

```
Untracked files:
  (use "git add <file>..." to include in what will be committed)

        bird.txt
        insect.txt
        reptile.txt
```

6. Add the files to the Git staging area by running the **`git add`** command.

```
git add --all
```

7. Confirm that the files were successfully added to the Git staging area by running
   the **`git status`** command again. All three
   files are now listed as changes to commit.

```
Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

        new file:   bird.txt
        new file:   insect.txt
        new file:   reptile.txt
```

8. Commit the staged files by running the **`git
commit`** command.

```
git commit -m "Added information about birds, insects, and reptiles."
```

9. Push the commit to your remote repository in CodeCommit by running the **`git push`** command.

```
git push -u origin master
```

10. Confirm whether the files were successfully pushed. Open the CodeCommit console, if it
    isn't already open, at [https://console.aws.amazon.com/codecommit](https://console.aws.amazon.com/codecommit "https://console.aws.amazon.com/codecommit").
11. In the top navigation bar, near the right edge, choose the AWS Region where you
    created the repository (for example, **US East (Ohio)**).
12. On the **Dashboard** page, choose
    **MyDemoCloud9Repo**. The three files are displayed.

To continue experimenting with your CodeCommit repository, see [Browse the Contents of Your Repository](../../../codecommit/latest/userguide/getting-started-cc.md#getting-started-cc-browse "../../../codecommit/latest/userguide/getting-started-cc.md#getting-started-cc-browse") in the
_AWS CodeCommit User Guide_.

If you're new to Git and you don't want to mess up your CodeCommit repository,
experiment with a sample Git repository on the [Try Git](https://try.github.io/ "https://try.github.io/") website.

## Step 6: Clean up

To prevent ongoing charges to your AWS account after you're done using this sample,
delete the CodeCommit repository. For instructions, see [Delete
an AWS CodeCommit Repository](../../../codecommit/latest/userguide/how-to-delete-repository.md "../../../codecommit/latest/userguide/how-to-delete-repository.md") in the _AWS CodeCommit User Guide_.

Make sure also to delete the environment. For instructions, see [Deleting an Environment](delete-environment.md "delete-environment.md").
