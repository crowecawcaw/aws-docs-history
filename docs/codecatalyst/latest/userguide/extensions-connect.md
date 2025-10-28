Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Connecting GitHub accounts, Bitbucket workspaces, GitLab users, and Jira sites CodeCatalyst

To use a GitHub repository, Bitbucket repository, or GitLab project repository or manage a Jira project in CodeCatalyst,
you must first connect your third-party source to your CodeCatalyst space. To learn more about the extensions and their
functionalities, see [Available third-party extensions](extensions.md#extensions-types "extensions.md#extensions-types").

###### Important

To connect your GitHub account, Bitbucket workspace, GitLab user, or Jira site to your CodeCatalyst space, you must be
both the third-party source's administrator and the CodeCatalyst **Space administrator**.

###### Note

If you're using a connection to a GitHub account, you must create a personal
connection to establish identity mapping between your CodeCatalyst identity and your GitHub identity.
For more information, see [Personal connections](concepts.md#personal-connection-concept "concepts.md#personal-connection-concept") and [Accessing GitHub resources with personal
connections](ipa-settings-connections.md "ipa-settings-connections.md").

###### To connect your GitHub account, Bitbucket workspace, GitLab user, or Jira site to CodeCatalyst

1.  Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2.  Navigate to your CodeCatalyst space.
3.  Do one of the following to view a list of the installed extensions for your space:
    1. Choose **Settings**, and then choose **Installed extensions**.
    2. Choose the **Catalog** icon

    ![The CodeCatalyst catalog icon in the top navigation bar in CodeCatalyst.](images/integrations/marketplace-icon.png)
    in the top menu.

4.  Choose **Configure** for one of the following extensions you want to configure: **GitHub repositories**,
    **Bitbucket repositories**, **GitLab repositories**, or **Jira Software**.
5.  Do one of the following depending on the third-party extension you chose to configure:

        * **GitHub repositories**: Connect to a GitHub account.



        	1. In the **Connected GitHub accounts** tab, choose **Connect GitHub account** to go to
        	 the external site for GitHub.
        	2. Sign in to your GitHub account using your GitHub credentials, and then choose the
        	 account where you want to install Amazon CodeCatalyst.


        	###### Tip

        	If you have previously connected a GitHub account to the space, you will not be
        	 prompted to reauthorize. You will instead see a dialog box asking you where you would
        	 like to install the extension if you are a member or collaborator in more than one
        	 GitHub space, or the configuration page for the Amazon CodeCatalyst application if you only
        	 belong to one GitHub space. Configure the application for the repository access
        	 that you want to allow, and then choose **Save**. If the
        	 **Save** button is not active, make a change to the configuration,
        	 and then try again.
        	3. Choose whether you want to allow CodeCatalyst to access all current and future repositories,
        	 or choose the specific GitHub repositories you want to use in CodeCatalyst.
        	 The
        	 default option is to include all GitHub repositories in the GitHub account, including
        	 future repositories that will be accessed by
        	 CodeCatalyst.
        	4. Review the permissions given to CodeCatalyst, and then choose
        	 **Install**.
        After connecting your GitHub account to CodeCatalyst, you're taken to the **GitHub repositories** extension details
         page, where you can view and manage connected GitHub accounts and linked GitHub repositories.
        * **Bitbucket repositories**: Connect to a Bitbucket workspace.



        	1. In the **Connected Bitbucket workspaces** tab, choose **Connect Bitbucket workspace** to go to
        	 the external site for Bitbucket.
        	2. Sign into your Bitbucket workspace using your Bitbucket credentials and review the permissions given to CodeCatalyst.
        	3. From the **Authorize for workspace** dropdown menu, choose the Bitbucket workspace you want to
        	 provide CodeCatalyst access to, and then choose **Grant access**.


        	###### Tip

        	If you have previously connected a Bitbucket workspace to the space, you will not be prompted
        	 to reauthorize. You will instead see a dialog asking you where you would like to
        	 install the extension if you're a member or collaborator in more than one Bitbucket
        	 workspace, or the configuration page for the Amazon CodeCatalyst application if you only
        	 belong to one Bitbucket workspace. Configure the application for the workspace access
        	 you want to allow, and then choose **Grant access**. If the
        	 **Grant access** button is not active, make a change to the configuration,
        	 and then try again.
        After connecting your Bitbucket workspace to CodeCatalyst, you're taken to the **Bitbucket repositories** extension details
         page, where you can view and manage connected Bitbucket workspaces and linked Bitbucket repositories.
        * **GitLab repositories**: Connect to a GitLab user.



        	1. Choose **Connect GitLab user** to go to
        	 the external site for GitLab.
        	2. Sign in to your GitLab user using your GitLab credentials and review the permissions given to CodeCatalyst.


        	###### Tip

        	If you have previously connected a GitLab user to the space, you will not be
        	 prompted to reauthorize. You will instead be navigated back to the CodeCatalyst console.
        	3. Choose **Authorize AWS Connector for GitLab**.
        After connecting your GitLab user to CodeCatalyst, you're taken to the **GitLab repositories** extension details
         page, where you can view and manage connected GitLab user and linked GitLab project repositories.
        * **Jira Software**: Connect a Jira site.



        	1. In the **Connected Jira sites** tab, choose **Connect Jira site** to go to the external
        	 site for Atlassian Marketplace.
        	2. Choose **Get it now** to get started with installing CodeCatalyst on your Jira site.


        	###### Note

        	If you previously installed CodeCatalyst to your Jira site, you will be notified. Choose **Get
        	 started** to be taken to the final step.
        	3. Depending on your role, do one of the following:




        		1. If you are a Jira site administrator, from the site dropdown menu, choose the Jira site to install the CodeCatalyst application, and
        		 then choose **Install app**.


        		###### Note

        		If you have one Jira site, this step won't appear, and you'll automatically be directed to the next step.
        		2. 1. If you aren't a Jira administrator, from the site dropdown menu, choose the Jira site to install the CodeCatalyst
        			 application, and then choose **Request app**. For more information on installing Jira apps, see
        			 [Who can install apps?](https://www.atlassian.com/licensing/marketplace#who-can-install-apps "https://www.atlassian.com/licensing/marketplace#who-can-install-apps").
        			2. Enter the reason you need to install CodeCatalyst into the input text field or keep the default text, and then choose
        			 **Submit request**.
        	4. Review the actions performed by CodeCatalyst when the application is installed, and then choose **Get it
        	 now**.
        	5. After the application is installed, choose **Return to CodeCatalyst** to return to CodeCatalyst.
        After connecting your Jira site to CodeCatalyst, you can view the connected site in the
         **Connected Jira sites** tab of the **Jira Software** extension
         details page.

    If you no longer want to use GitHub repositories, Bitbucket repositories, or GitLab project repositories, or manage Jira issues in CodeCatalyst, you can
    disconnect your third-party source. When a GitHub account, Bitbucket workspace, or GitLab user is disconnected, events in the third-party repositories
    will not start workflow runs, and you will not be able to use those repositories with CodeCatalyst Dev Environments. When a Jira
    site is disconnected, Jira issues from the site's projects will not be available in the CodeCatalyst projects, and CodeCatalyst
    **Issues** will be the issue provider again. For more information, see
    [Disconnecting GitHub accounts, Bitbucket workspaces, GitLab users, and Jira sites CodeCatalyst](extensions-disconnect.md "extensions-disconnect.md").
