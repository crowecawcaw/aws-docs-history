AWS Cloud9 is no longer available to new customers. Existing customers of 
 AWS Cloud9 can continue to use the service as normal. 
 [Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")

# Migrate from AWS Cloud9 to Amazon CodeCatalyst

AWS Cloud9 in CodeCatalyst provides a fully managed experience for interacting with AWS Cloud9. You
 can manually replicate your current AWS Cloud9 code resources in Amazon CodeCatalyst. The process is
 detailed in the following sections. To move your code resources and replicate them,
 create a Space within CodeCatalyst. A space represents your company,
 department, or group. You need to create spaces to add projects, members, and the
 associated cloud resources that you create in CodeCatalyst. When a user accepts an invitation
 to a project, CodeCatalyst automatically adds them to the space. Users with the
 **Space administrator** role can manage the space.

Within this space, you create a project and add your source repositories. A
 project is a collaboration space in CodeCatalyst that supports development teams and tasks.
 After you create a project, you can add, update, or remove resources. You can also
 customize your project dashboard, and monitor the progress of your team's work. You can
 have multiple projects within a space. The number of source repositories that you
 add depends on the number of repositories that you're already using in your AWS Cloud9
 environment. After you create this project and added the applicable source repositories,
 you might need to return to your AWS Cloud9 environment and replicate the environment data to
 these new repositories in CodeCatalyst. What you do depends on the type of source repositories
 you have in AWS Cloud9.

After you create a space, project, and source repositories, you can launch
 your environment in CodeCatalyst using AWS Cloud9 with a Dev Environment. A Dev Environment is a
 cloud-based development environment. You can use a Dev Environment in CodeCatalyst to work on the
 code that's stored in the source repositories of your project. You can also create
 Dev Environments in CodeCatalyst to work on code in a project-specific Dev Environment with a
 supported integrated development environment (IDE).

You can also replicate your current AWS Cloud9 code resources to CodeCatalyst using the
 replication tool. This is a tool that you download and run in your AWS Cloud9 environment. If
 you already signed up to CodeCatalyst, and created a space, the tool automatically
 creates a project within this space and replicates your code resources to new
 repositories in CodeCatalyst. Similar to the manual replication process. This depends on the
 type of source repositories that you have in AWS Cloud9. For example, if you have
 GitHub repositories, you still need to replicate these repositories
 using the **GitHub extension** in the CodeCatalyst
 console.


* [Step 1. Signing up to Amazon CodeCatalyst and
 creating a Space](#c9-replication-cc-space-creation "#c9-replication-cc-space-creation")
* [Step 2. Creating a project in your Space](#c9-replication-cc-project-creation "#c9-replication-cc-project-creation")
* [Step 3. Creating a source repository
 in your project](#c9-replication-cc-repo-creation "#c9-replication-cc-repo-creation")
* [Step 4. Replicating your
 AWS Cloud9 code resources to source repositories in CodeCatalyst](#c9-replication-cc-source-repo-creation "#c9-replication-cc-source-repo-creation")
* [Step 5. Creating a Dev Environment in CodeCatalyst using AWS Cloud9](#dev-environment-creation "#dev-environment-creation")

## Step 1. Signing up to Amazon CodeCatalyst and
 creating a Space


You can sign up for Amazon CodeCatalyst without an invitation to an existing space or
 project. When you sign up, you create a space and project. You can enter your
 existing AWS account ID that you used for AWS Cloud9. This same AWS account can be
 used for billing purposes. For information about how to find your AWS account ID,
 see [Your AWS account ID and
 its alias](https://docs.aws.amazon.com/IAM/latest/UserGuide/console_account-alias.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/console_account-alias.html"). Follow this procedure to sign up for your Amazon CodeCatalyst profile,
 create a space, and add an account for your space.


###### To sign up as a new user

1. Open the [CodeCatalyst
 console](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. On the welcome page, choose **Sign up**. 


The **Create your AWS Builder ID** page displays. Your
 AWS Builder ID is an identity that you create to sign in to. This ID isn't the
 same as an AWS account ID. To learn more about an AWS Builder ID, see [AWS Builder ID and other AWS credentials](https://docs.aws.amazon.com/signin/latest/userguide/differences-aws_builder_id.html "https://docs.aws.amazon.com/signin/latest/userguide/differences-aws_builder_id.html") in the *AWS
 Sign-In User Guide*.
3. For **Your email address**, enter the email address that
 you want to associate with CodeCatalyst. Then, choose
 **Next**.
4. For **Your name**, enter the first and last name that you
 want displayed in applications where you use your AWS Builder ID. 


This name is your AWS Builder ID profile name. If you want, you can change the
 name later.


Choose **Next**. The **Email
 verification** page appears. A verification code is sent to the
 email that you specified.
5. For **Verification code**, enter the code that you
 received, and then choose **Verify**. 


If you don't receive your code after 5 minutes and can't find it in your
 spam or junk folders, then choose **Resend code**.
6. After your code is verified, enter a password and choose **Confirm
 password**.


Select the check box confirming that you read and acknowledge the AWS
 Customer Agreement and the AWS Service Terms, and then choose
 **Create my profile**.
7. On the **Create your alias** page, enter an alias to use
 for CodeCatalyst. Other CodeCatalyst users will use this alias to @mention you in
 comments and pull requests. Your CodeCatalyst profile will contain both your full
 name from your AWS Builder ID and your CodeCatalyst alias. You can't change your
 CodeCatalyst alias.


Your full name and your alias will display in different areas in CodeCatalyst.
 For example, your profile name appears in your activity feed, but project
 members will use your alias to @mention you.


Choose **Create alias**. The page updates to show the
 **Create your space** section.
8. For **Space name**, enter the name of your
 space, and then choose **Next**. 


You can't change this name.
9. For **AWS account ID**, link the twelve-digit ID for
 the account that you want to connect to your space.


In **AWS account verification token**, copy the
 generated token ID. The token is automatically copied for you. But, you
 might want to store it while you approve the AWS connection
 request.
10. Choose **Verify in AWS**.
11. The **Verify Amazon CodeCatalyst space** page opens in the
 AWS Management Console. 


This is the **Amazon CodeCatalyst Spaces** page. You might need
 to log in to access the page.


To access the page, sign in to the Amazon CodeCatalyst Spaces in the [AWS Management Console](https://console.aws.amazon.com/codecatalyst/home/ "https://console.aws.amazon.com/codecatalyst/home/").


The verification token field in the AWS Management Console is automatically populated
 with the token generated in CodeCatalyst.
12. Choose **Verify space**.


An **Account verified** success message
 displays to show that the account was added to the space.


You will use CodeCatalyst free tier by default. If you want to change,
 choose **To enable the Standard tier or add IAM roles for this
 space, view space details**.


For more information about CodeCatalyst pricing tiers, see [Amazon CodeCatalyst -
 Pricing](https://codecatalyst.aws/explore/pricing "https://codecatalyst.aws/explore/pricing").


The **CodeCatalyst space details** page opens in the
 AWS Management Console. This is the **Amazon CodeCatalyst Spaces** page. You
 might need to log in to access the page.
13. Choose **Go to [Amazon CodeCatalyst](https://codecatalyst.aws/ "https://codecatalyst.aws/")**.
14. On the creation page in CodeCatalyst, choose **Create
 space**.


A status message displays while your space is being created. When the
 space is created, CodeCatalyst opens the page for your space. The view
 defaults to the **Projects** tab. 


###### Note

If a permissions error or banner is shown, then refresh the page and
 try to view the page again.

After you sign up to CodeCatalyst and create a space, the next step in the
 replication process is to create a project within this space.


## Step 2. Creating a project in your Space


The following steps outline how to create an empty project within the
 space that you created in the previous step. With this project, you can
 manually add the resources that you want at a later time. Before you create a
 project you must have the *Space administrator* role,
 and you must join the space where you want to create the project. When you
 create a space, CodeCatalyst automatically assigns you the *Space
 administrator* role. The *Space
 administrator* role is the most powerful role in CodeCatalyst. For more
 information about this role and its permissions, see [Space administrator role](https://docs.aws.amazon.com/codecatalyst/latest/userguide/welcome.html "https://docs.aws.amazon.com/codecatalyst/latest/userguide/welcome.html").


###### To create an empty project

1. Navigate to the space where you want to create a project.
2. On the space dashboard, choose **Create project**.
3. Choose **Start from scratch**.
4. Under **Give a name to your project**, enter the name that you want to assign to your project. The name must be unique within your space.
5. Choose **Create project**.

After you create a project, the next step in the replication process is to
 create one or more source repositories.


## Step 3. Creating a source repository
 in your project


Within the project that you just created, you need to create a source repository.
 This repository contains a single file, a **README.md** file, which
 you can edit or delete at any time. Depending on your choices that you made when you
 create a source repository, it might also contain a `.gitignore`
 file.


###### To create a source repository

1. Open the [CodeCatalyst
 console](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to your project.
3. In the navigation pane, choose **Code**, and then choose
 **Source repositories**.
4. Choose **Add repository**, and then choose
 **Create repository**.
5. In **Repository name**, provide a name for the
 repository. 


Repository names must be unique within a project. For more information
 about requirements for repository names, see [Quotas for source
 repositories in CodeCatalyst](https://docs.aws.amazon.com/codecatalyst/latest/userguide/source-quotas.html "https://docs.aws.amazon.com/codecatalyst/latest/userguide/source-quotas.html").
6. (Optional) In **Description**, add a description for the
 repository that helps other users in the project understand what the
 repository is used for.
7. (Optional) Add a `.gitignore` file for the type of code that
 you plan to push.
8. Choose **Create**.


###### Note

CodeCatalyst adds a `README.md` file to your repository when you
 create it. CodeCatalyst also creates an initial commit for the repository in a
 default branch named **main**. You can edit or delete
 the README.md file, but you can't change or delete the default
 branch.
9. To get the source repository clone URL and PAT, choose **Clone
 repository**.
10. To copy each of the HTTPS clone URL and PAT, choose
 **Copy**. Then, store the clone URL and PAT somewhere
 where you can retrieve it.


The clone URL and PAT will be used in the step 4, and referenced as
 `CODECATALYST_SOURCE_REPO_CLONE_URL` and
 `CODECATALYST_PAT`.

After you create a source repository within your project, replicate your AWS Cloud9
 data to this source repository.


## Step 4. Replicating
 your AWS Cloud9 code resources to source repositories in CodeCatalyst


The type of source repository that you have in your AWS Cloud9 environment
 determines the replication method that you follow to get your code resources into
 the CodeCatalyst source repository that you created. The options are as follows: 



* [Using GitHub
 repositories in AWS Cloud9](#c9-replication-cc-source-repo-creation-github "#c9-replication-cc-source-repo-creation-github")
* [Using
 non-GitHub, for example GitLab or Bitbucket,
 repositories in AWS Cloud9](#c9-replication-cc-source-repo-creation-nongithub "#c9-replication-cc-source-repo-creation-nongithub")
* [Using an empty repository in
 AWS Cloud9](#c9-replication-cc-source-norepo-creation "#c9-replication-cc-source-norepo-creation"). This option means you would not be using any source
 repository in AWS Cloud9.

### Using
 GitHub repositories in CodeCatalyst


With the **GitHub repositories**
 extension, you can use linked GitHub repositories from AWS Cloud9 in
 Amazon CodeCatalyst projects. The following steps outline how to install the
 GitHub extension from the CodeCatalyst catalog. The steps also show
 how to connect your existing GitHub account to your CodeCatalyst space
 and link your GitHub repository to your CodeCatalyst project.


The first step in this method is to install the
 **GitHub repositories** extension from
 the CodeCatalyst catalog. To install the extension, perform the following
 steps.


###### Important

As part of installing and configuring the
 **Github repositories** extension,
 you must install an extension into your GitHub account. To do
 this, you must be a GitHub account administrator and a CodeCatalyst
 space administrator.


###### Step 1. To install an extension from the CodeCatalyst catalog

1. Open the [CodeCatalyst
 console](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to your space.


###### Tip

If you belong to more than one space, you can choose which
 space to view in the top navigation bar.
3. Navigate to the CodeCatalyst catalog by choosing the
 **Catalog** icon in the top menu bar next to the
 search bar. You can search for **GitHub
 repositories** or filter extensions based on
 categories.
4. (Optional) To see more details about the extension, such as the
 permissions associated with it, choose the
 **GitHub repositories**
 extension name.
5. Choose **Install**. Review the permissions required
 by the extension, and if you want to continue, choose
 **Install** again.

After installing the **GitHub
 repositories** extension, you are taken to the
 **GitHub repositories** extension
 details page where you can view and manage connected GitHub
 accounts and linked GitHub repositories.


After you install the **GitHub
 repositories** extension, connect your GitHub
 account to your CodeCatalyst space. To connect your GitHub
 account, perform the following steps.


###### Step 2. To connect your GitHub account to
 CodeCatalyst

1. In the **Connected Github accounts** tab, choose
 **Connect GitHub account** to go to
 the external site for GitHub.
2. Sign into your GitHub account using your GitHub credentials, and
 then choose the account where you want to install Amazon CodeCatalyst.
3. Choose whether you want to allow CodeCatalyst to access all current and future repositories. Or,
 alternatively, choose the specific GitHub repository that
 you want to use in CodeCatalyst. The default option is all
 GitHub repositories in the GitHub
 space.
4. Review the permissions given to CodeCatalyst, and then choose **Install**.

After connecting your GitHub account to CodeCatalyst, you can
 view the connected account in the **GitHub
 accounts** tab of the **GitHub
 repositories** extension details page.


The final step to using your GitHub repositories in
 CodeCatalyst is to link the repository to the CodeCatalyst project where you want to use it.
 To link your GitHub repository to a CodeCatalyst project, perform the
 following steps outlined in Step 3 of the overall process:


###### Step 3. To link a GitHub repository to a CodeCatalyst
 project from the GitHub repositories extension details
 page

1. In the **Linked GitHub repositories** tab, choose
 **Link GitHub repository.**.
2. For **GitHub account**, select the GitHub
 account that contains the repository that you want to link.
3. For **GitHub repository**, select the repository that you want
 to link to a CodeCatalyst project.
4. For **CodeCatalyst project**, select the CodeCatalyst project that you want to link the
 GitHub repository to.
5. Choose **Link**.

Your CodeCatalyst repository should now have the updated files and commits you just pushed. You can now create Dev Environments from this branch and open them with AWS Cloud9.
 For detailed information on Dev Environments, see [Dev Environments in CodeCatalyst](https://docs.aws.amazon.com/codecatalyst/latest/userguide/devenvironment.html "https://docs.aws.amazon.com/codecatalyst/latest/userguide/devenvironment.html").


You can now create
 Dev Environments from this branch and open them with AWS Cloud9. The steps to do this
 are outlined in [Step 5: Creating a Dev Environment using AWS Cloud9 in CodeCatalyst](#dev-environment-creation "#dev-environment-creation")


### Using non-GitHub repositories in CodeCatalyst


You need to create a personal access token (PAT) in Amazon CodeCatalyst
 before replicating your environment from AWS Cloud9 using a non-GitHub
 repository. The following section outlines how to create this token. 


#### Creating a personal access
 token in Amazon CodeCatalyst


You can access the source repository that you created in your project on a
 local computer with a Git client or in an integrated
 development environment (IDE). To do this, you must enter an
 application-specific password. You can create a personal access token (PAT)
 to use for this purpose. The personal access tokens (PATs) that you create
 are associated with your user identity across all spaces and projects in
 CodeCatalyst. You can view the names and expiration dates of the PATs that you
 created, and you can delete thee PATs that you no longer need. You can only
 copy the PAT secret at the time you create it.


###### To create a personal access token (PAT)

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. In the top menu bar, choose your profile badge, and then choose
 **My settings**. 


###### Tip

You can also find your user profile. To do this, on the
 members page for a project or space, choose your name from
 the members list.
3. Under **Personal access tokens**, choose
 **Create**.
4. In **PAT name**, enter a descriptive name for
 your personal access token (PAT).
5. In **Expiration date**, keep the default date or
 choose the calendar icon to select a custom date. The expiration
 date defaults to 1 year from the current date.
6. Choose **Create**.


###### Tip

You can also create this token when you choose **Clone
 repository** for a source repository.
7. To copy the PAT secret choose **Copy**. Store the
 PAT secret somewhere where you can retrieve it.


###### Important

The PAT secret only displays once. You can't retrieve it after
 you close the window. If you didn't save the PAT secret in a
 secure location, you can create another one.

After you create the PAT for your source repository, replicate your data
 from your AWS Cloud9 environment to CodeCatalyst by adding a remote repository in your AWS Cloud9 environment and pushing your data to this repository, as outlined in the section below.


#### Adding a remote repository in your AWS Cloud9 environment


Say that you're running repositories that aren't GitHub
 repositories. You can add a remote repository in your AWS Cloud9 environment and
 push your data to your source repository in CodeCatalyst. To complete this
 process, run the following commands.


From within your AWS Cloud9 IDE, add a remote repository that points to the
 source repository that you created in step 3 of the replication process in
 CodeCatalyst. Replace `CODECATALYST_SOURCE_REPO_CLONE_URL` in the
 command with the Clone URL that you saved in the step 10 of [Step 3. Creating a source
 repository in your project](#c9-replication-cc-repo-creation "#c9-replication-cc-repo-creation").



```
 git remote add codecatalyst CODECATALYST_SOURCE_REPO_CLONE_URL
```

Push a new branch to the source repository by using the following command.
 When prompted to enter a password, use `CODECATALYST_PAT` that
 you stored in the step 10 of [Step 3. Creating a source repository in your project](#c9-replication-cc-repo-creation "#c9-replication-cc-repo-creation"):



```
git checkout -b replication && git push codecatalyst replication
```

The following is an example of expected command run output:



```
Switched to a new branch 'replication'
Password for 'https://[aws-account-id]@[aws-region].codecatalyst.aws/v1/MySpace222581768915/Replication/Repository':
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (4/4), 982 bytes | 122.00 KiB/s, done.
Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
remote: Validating objects: 100%
To https://[aws-account-id].codecatalyst.aws/v1/MySpace222581768915/Replication/Repository
* [new branch] replication → replication
```


This branch is available in the source repository that you created in
 CodeCatalyst. You can create Dev Environments from this branch and open them with
 AWS Cloud9. For more information about Dev Environments, see [Dev Environments in CodeCatalyst](https://docs.aws.amazon.com/codecatalyst/latest/userguide/devenvironment.html "https://docs.aws.amazon.com/codecatalyst/latest/userguide/devenvironment.html").


You can now create
 Dev Environments from this branch and open them with AWS Cloud9. The steps to do this
 are outlined in [Step 5: Creating a Dev Environment using AWS Cloud9 in CodeCatalyst](#dev-environment-creation "#dev-environment-creation")


#### Using an
 empty repository in AWS Cloud9


First create a personal access token (PAT) in Amazon CodeCatalyst before you
 can replicate your environment from AWS Cloud9 using an empty repository. The
 following section outlines how to create this token. 


##### Creating a personal access
 token in Amazon CodeCatalyst


You can access the source repository that you created in your project on a
 local computer with a Git client or in an integrated
 development environment (IDE). To do this, you must enter an
 application-specific password. You can create a personal access token (PAT)
 to use for this purpose. The personal access tokens (PATs) that you create
 are associated with your user identity across all spaces and projects in
 CodeCatalyst. You can view the names and expiration dates of the PATs that you
 created, and you can delete thee PATs that you no longer need. You can only
 copy the PAT secret at the time you create it.


###### To create a personal access token (PAT)

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. In the top menu bar, choose your profile badge, and then choose
 **My settings**. 


###### Tip

You can also find your user profile. To do this, on the
 members page for a project or space, choose your name from
 the members list.
3. Under **Personal access tokens**, choose
 **Create**.
4. In **PAT name**, enter a descriptive name for
 your personal access token (PAT).
5. In **Expiration date**, keep the default date or
 choose the calendar icon to select a custom date. The expiration
 date defaults to 1 year from the current date.
6. Choose **Create**.


###### Tip

You can also create this token when you choose **Clone
 repository** for a source repository.
7. To copy the PAT secret choose **Copy**. Store the
 PAT secret somewhere where you can retrieve it.


###### Important

The PAT secret only displays once. You can't retrieve it after
 you close the window. If you didn't save the PAT secret in a
 secure location, you can create another one.

After you create the PAT for your source repository, replicate your data
 from your AWS Cloud9 environment to CodeCatalyst by initiating an empty repository in your AWS Cloud9 environment and pointing to the source repository you created in CodeCatalyst, as outlined in the section below.


##### Initiating an
 empty repository in AWS Cloud9


If you don't have any source repository that's set up in AWS Cloud9, then
 initiate an empty repository in AWS Cloud9. Additionally, point to the source
 repository that you created in CodeCatalyst, and add and push the files you want
 to replicate through Git. Perform the following steps and run
 the following commands to replicate your AWS Cloud9 files to CodeCatalyst.



1. From your AWS Cloud9 environment, initiate an empty repository by
 running the following command:



```
git init -b main
```

Then, you see a similar output as shown below:



```

Initialized empty Git repository in /home/ec2-user/environment/.git/
```
2. Clone the source repository URL from CodeCatalyst. Navigate to the
 CodeCatalyst project that you created within the CodeCatalyst console, and, in
 the navigation pane, choose **Code**, and then
 choose **Source repositories**.
3. Choose the repository from the list of source repositories
 that you want, and choose **Clone repository** to
 copy the clone URL.
4. Add the CodeCatalyst repository using the URL you cloned, and push the content already in the empty repository in CodeCatalyst:



```
git remote add origin [...]
git push origin --force
```
5. Add the files that you want to replicate. If you want to
 replicate all the files in your environment directory, run `git
 add -A`:



```
git add -A .
git commit -m "replicate"
```
6. Merge the two unrelated histories. Address merge conflicts if
 they occur:



```
git merge origin/main --allow-unrelated-histories
```
7. Push the changes back to the source repository in CodeCatalyst by
 running the following command. When prompted to enter a password,
 enter the personal access token (`CODECATALYST_PAT`) that
 you generated the step 10 of [Step 3. Creating a
 source repository in your project](#c9-replication-cc-repo-creation "#c9-replication-cc-repo-creation"):



```
Admin:~/environment (main) $ git push origin main
Password for 'https://222581768915@git.us-west-2.codecatalyst.aws/v1/MySpace222581768915/Replication/Replication': 

```

After completing this procedure, your CodeCatalyst repository has
 the updated files and commits that you just pushed. You can now create
 Dev Environments from this branch and open them with AWS Cloud9. The steps to do this
 are outlined in the section below. 


## Step 5: Creating a Dev Environment using AWS Cloud9 in CodeCatalyst


The following procedure outlines how to create a Dev Environment in CodeCatalyst using AWS Cloud9 and the data you just replicated.


###### To create a Dev Environment using AWS Cloud9

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to the project where you want to create a Dev Environment.
3. In the navigation pane, Choose **Overview**, and then navigate to the
 **My Dev Environments** section.
4. Choose **Create Dev Environment**.
5. Choose AWS Cloud9 from the drop-down menu.
6. Choose **Clone a repository**.


###### Note

Currently, CodeCatalyst does not support cloning third-party repositories, but you can create a
 Dev Environment and clone a third-party repository into it from your
 chosen IDE.
7. Do one of the following:


	1. Choose the repository to clone, choose **Work in existing branch**, and then choose a branch from the
	 **Existing branch** drop-down menu.
	2. Choose the repository to clone, choose **Work in new branch**, enter a branch name into the **Branch
	 name** field, and choose a branch off of which to create the new
	 branch from the **Create branch from** drop-down menu.
8. Optionally, add an alias for the Dev Environment.
9. Optionally, choose the **Dev Environment configuration** edit button to edit the Dev Environment's compute, storage, or timeout configuration.
10. Choose **Create**. While your Dev Environment is being created, the Dev Environment status column will display **Starting**, and the status column will display **Running** once the Dev Environment has been created.
