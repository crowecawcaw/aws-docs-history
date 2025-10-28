# Reviewing your plan to prepare for transformation

After [Confirming your repositories to prepare for transformation](dotnet-confirming-repos.md "dotnet-confirming-repos.md"), and [Resolving package dependencies to prepare for
transformation](dotnet-resolving-dependencies.md "dotnet-resolving-dependencies.md"), the AWS account administrator must review the transformation plan and approve it in AWS Transform.

AWS Transform displays the job's list of repositories, dependent repositories, and dependent packages that were selected for transformation.

## Reviewing the transformation plan

AWS Transform displays the job's list of repositories, dependent repositories, and dependent packages that were selected for transformation.

###### Note

AWS Transform can transform a maximum of 100 dependencies and repositories per transformation plan.

1. If you are not the AWS account administrator, review the job plan, and if you accept it, select **Send for approval**.
2. If you are the AWS account administrator, you must review the plan, and when ready, approve the plan to start the transformation. After you review the job plan, select either:
   1. _Reject_
      If the job was created by a user who is not the AWS account administrator, we suggest you notify the job creator to restart the job.
   2. _Approve and start transformation_.

The job review includes the following details:

1. _Job summary_
   This includes:
   1. The target branch where AWS Transform will place the transformed code.
   2. The target .NET version, currently .NET 8.0.
   3. The job settings:
      1. Exclude .NET standard projects
      2. Transform MVC Razor Views to ASP.NET Core Razor Views

   4. Number of repositories selected for transformation
   5. Number of dependent repositories
   6. Number of private NuGet packages
   7. Total lines of code for the job

2. _Repositories selected_
   These are the repositories selected for transformation. They must be either MVC, Web, Windows Communication Foundation (WCF), Console, class library, UI framework - Razor pages, or unit test packages. This table includes the following information:
   1. Name
   2. Source branch
   3. Supported projects
   4. Lines of code
   5. Projects detected
   6. Projects skipped
   7. Dependencies detected

3. _Dependent repositories added_
   These are the dependent repositories added for transformation. They must be either MVC, Web, Windows Communication Foundation (WCF), Console, class library, UI framework - Razor pages, or unit test packages. This table includes the following information:
   1. Name
   2. Needed by
   3. Source branch
   4. Supported projects
   5. Lines of code
   6. Projects detected
   7. Projects skipped

4. _Dependent packages_
   These are the dependent packages added for transformation. They must be either MVC, Web, Windows Communication Foundation (WCF), Console, class library, UI framework - Razor pages, or unit test packages. This table includes the following information:
   1. Name
   2. Associated repositories
   3. Framework version status
   4. Core version status
