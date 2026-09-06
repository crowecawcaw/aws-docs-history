

# Create a project in AWS Settings
<a name="create-project"></a>

**Warning**  
We're currently releasing our new experience to a limited number of customers. You might not be able to access this experience yet.

A project contains a single AWS account where you create AWS resources. A project also includes settings for sharing with other collaborators. The AWS resources you create should represent an application or a set of related use cases. One project can span the development and production environments of your application. For example, you can create a project called Bookstore that holds resources for a bookstore application including a database, compute resources, and storage.

You can share this project with other team members, and they can build and manage resources for the bookstore application.

Each project has its own billing based on the resources in the account. If you're using the paid plan, you can configure a spend limit in AWS Settings for each project. For more information, see [Create a spend limit in AWS Settings](create-spend-limit.md). As the project owner, you are responsible for the monthly invoices for usage charges and recurring fees.

## Considerations for creating a project
<a name="create-project-considerations"></a>
+ You can access projects that you don't own as a team member.
+ Each project name must be unique to your projects. Projects owned by other team members can have the same name.
+ Project names can contain the following valid characters: a-z, A-Z, 0-9, and periods (.).
+ When you create your project, AWS assigns it to a Region—US East (Ohio) (`us-east-2`), Europe (Stockholm) (`eu-north-1`), or Asia Pacific (Sydney) (`ap-southeast-2`)—based on the country in your contact address—either the United States, Europe, or Asia Pacific. Any Regional resources that you create will be hosted in that Region. For more information, see [AWS Regions for your projects](project-regions.md).

## To create a project
<a name="create-project-procedure"></a>

**To create a project**

1. Open AWS Settings at [https://settings.aws.com](https://settings.aws.com).

1. In the main navigation pane, choose **Project**.

1. Choose **Create project**.

1. For **Project name**, enter a descriptive name for your project.

   This name is shared with team members when you invite them to collaborate.

1. Choose **Create**.

It takes a few seconds to create your project. When your project is available, you can choose the project and access the AWS Management Console to start building.

If you've already set up your AI coding tool to interface with your AWS account, you can prompt it to create resources in your new project.

Use the example prompts for your AI coding tool to get started:

```
What is the Region for my project {{test project}}?
```

```
Create a hello world Lambda function in my project {{test project}}.
```

```
Create an S3 bucket in my project {{test project}}.
```