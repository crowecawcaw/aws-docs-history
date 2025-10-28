# Custom project profile

Complete the following procedure to create a custom project profile for your Amazon
SageMaker unified domain. With the Custom creation option, you can create a project profile
from scratch with your own profile settings and a selection of blueprints.

1.  Navigate to the Amazon SageMaker management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and use the region selector in the top
    navigation bar to choose the appropriate AWS Region.
2.  Either create a new domain or choose an existing domain where you want to create a
    custom project profile.
3.  On the domain's details page, choose the **Project profiles** tab and
    then choose **Create**.
4.  On the **Create project profile** page, in the **Project
    profile name and description** section, specify the name of the project profile
    and the description.
5.  On the **Create project profile** page, in the **Project
    profile creation options** section, choose **Custom
    create**.
6.  On the **Create project profile** page, in
    **Blueprints**, specify the Amazon SageMaker Unified Studio blueprints to use in your
    project. You can customize each blueprint configuration after this custom project profile
    is created. This is where you can choose built-in blueprints or your own [custom blueprints](custom-blueprint.md "custom-blueprint.md").
7.  To configure the project account and Region information you want the profile to use,
    you can either provide account and Region information that projects will use each time, or
    you can configure your project profile to allow specifying accounts during project
    creation. Under **Account and region**, choose one of the
    following.
    - To create a project profile that will use the same account and region for each
      project created, select **Choose account and region**. Projects
      created with this profile will use the specified account and region and cannot specify
      otherwise at project creation.
    - To create a project profile that will choose from accounts available at project
      creation, select **Choose account and region during project
      creation**.
      - Under **Accounts available during project creation**, you can
        choose to create a project profile that will provide a list of all AWS accounts
        associated to the domain for selection at project creation. To choose this option,
        choose **All associated accounts**. For more information about
        associated accounts in Amazon SageMaker Unified Studio, see [Associated accounts in Amazon SageMaker Unified Studio](associated-accounts.md "associated-accounts.md").
      - Under **Accounts available during project creation**, you can
        choose to create a project profile that will provide account pools to be selected
        at project creation. An account pool is a list of authorized associated accounts
        and regions. To choose this option, select **Choose account
        pool(s)**. Next, under **Account pools**, choose the
        account pool or pools that you want to be available for the project profile to use
        at project creation. For information about creating and updating account pools,
        see [Account pools in Amazon SageMaker Unified Studio](account-pools.md "account-pools.md").

8.  On the **Create project profile** page, in the **Default
    tooling blueprint deployment settings** section, review the selections for the
    default deployment settings for the Tooling blueprint.
9.  On the **Create project profile** page, in the **Project
    files storage** section, specify the storage configuration for project code
    artifacts. You can choose one of the following:

        * Amazon S3
        * Git repository

    For more information, see [Unified storage in Amazon SageMaker Unified Studio](smus-admin-storage-guide.md "smus-admin-storage-guide.md").

10. On the **Create project profile** page, in the
    **Authorization - optional** section, specify who can use this project
    profile to create projects in all domain units. This can also be done per domain unit in
    Amazon SageMaker Unified Studio. You can specify **Selected users and groups** or
    **Allow all users and groups** options.

###### Note

Projects do not provide strong security isolation. To limit cross-domain and
cross-project resource discovery you can consider creating projects in separate
accounts. 11. On the **Create project profile** page, in the **Project
profile readiness** section, specify whether you want to enable this project
profile on creation. Unless you check the **Enable project profile on
creation** checkbox, your project profile is disabled and not available to use
for Amazon SageMaker Unified Studio projects after its creation. Leaving a project profile in a disabled state
upon creation gives you the opportunity to customize your blueprints before making the
project profile available. 12. Choose **Create project profile**.
