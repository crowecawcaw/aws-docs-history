# Setting up the Amazon SageMaker Unified Studio integration in VS Code

Follow these steps to integrate Amazon SageMaker Unified Studio in VS code:

1. Open the AWS Toolkit panel in VS Code and navigate to the Amazon SageMaker Unified Studio section.
2. Choose **Sign in to get started** and enter your domain URL (format: `https://`<domain-id>`.sagemaker.`<region>`.on.aws`).
3. You will see a prompt asking you to open a link in the browser for IdC authentication, choose **Open** on the **Do you want Code to open the external website?** prompt. You will be directed to the browser for AWS IdC authentication. Complete the authentication flow in your browser, choose **Allow access** on the next prompt, and return to VS Code.
4. You should now be prompted to select a project. If not, under the domain, choose **Select a project** to choose from the list of available projects in your domain.
   Once connected, you'll see a hierarchical view of your resources. Under the selected Project, you have Data and Compute resources
   associated with the project.

The resources under Data show all your project's data sources: S3 buckets, Redshift, and Lakehouse
in one place, with easy browsing through databases, tables, and schema. You can access the data schema directly without switching
between different tools or screens, making it easy for code authoring in VS Code.

The Compute resource has Data warehouse,
Data processing, and Spaces within each project. Data Warehouse and Data Processing list the compute connections in the project
and hovering over them displays the connection metadata. Spaces are remote IDE environments you have access to in the project
that you can connect to remotely to author code from your local VS Code IDE.
