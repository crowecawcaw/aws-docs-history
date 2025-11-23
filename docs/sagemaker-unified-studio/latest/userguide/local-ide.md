# Authenticating directly in Local IDE

###### In Identity Center based domains

1. Open the AWS Toolkit panel in VS Code and navigate to the Amazon SageMaker Unified Studio
   section.
2. Choose Sign in to get started. You will see 2 options to sign in with IAM
   Credentials and IAM Identity Center. Choose IAM Identity Center and enter
   your domain URL (format:
   `https://domain-id.sagemaker.region.on.aws`).
3. You will see a prompt asking you to open a link in the browser for IAM
   Identity Center authentication, choose Open on the Do you want Code to open
   the external website? prompt. You will be directed to the browser AWS IAM
   Identity Center authentication. Complete the authentication flow in your
   browser, choose Allow access on the next prompt, and return to VS
   Code.
4. You should now be prompted to select a project. If not, under the domain,
   choose Select a project to choose from the list of available projects in
   your domain.
5. Once connected, you'll see a hierarchical view of your resources. Under
   the selected Project, you have Data and Compute resources associated with
   the project.

###### In IAM-based domains

1. Open the AWS Toolkit panel in VS Code and navigate to the Amazon SageMaker Unified Studio
   section.
2. Choose Sign in to get started. You will see 2 options to sign in with IAM
   Credentials and IAM Identity Center. Choose IAM Credentials.
3. You can either choose an existing credential profile and edit it or create
   a new one.
   - To edit an existing credential profile, follow the process in
     [AWS IAM credentials](../../../toolkit-for-vscode/latest/userguide/setup-credentials.md "../../../toolkit-for-vscode/latest/userguide/setup-credentials.md").
   - To create a new credential profile, follow the prompts and provide
     the credential of the Login Role you use to access your project in
     Amazon SageMaker Unified Studio IAM-based domain.
     - Select the region where your IAM-based domain is in. After
       the profile is created, sign in by selecting the created
       profile.

4. You will then see your Amazon SageMaker Unified Studio resources including Data and Compute
   resources listed in a sub-panel within AWS Toolkit.
   The resources under Data show all your project's data sources: S3 buckets,
   Redshift, and Lakehouse in one place, with easy browsing through databases, tables,
   and schema. You can access the data schema directly without switching between
   different tools or screens, making it easy for code authoring in VS Code.

The Compute resource has Data warehouse, Data processing, and Spaces within each
project. Data Warehouse and Data Processing list the compute connections in the
project and hovering over them displays the connection metadata. Spaces are remote
IDE environments you have access to in the project that you can connect to remotely
to author code from your local VS Code IDE.
