# Modernizing .NET code with the AWS Transform web application

You can modernize your .NET code using the AWS Transform web application (described here) or the [Visual Studio IDE](dotnet-ide.md "dotnet-ide.md"). The web application is best suited for IT professionals interested in large-scale transformation. It works at repository level, and can transform as many as 5,000 repositories in a single job.

To access the web application, navigate to the web link you received with your AWS Transform email invitation or contact your AWS Transform administrator.

## Web transformation workflow

To modernize your .NET repositories using the AWS Transform web application, navigate to the web application and follow these steps:

1. **Start transformation**

   - [Create a .NET modernization job](dotnet-web-create-job.md "dotnet-web-create-job.md")
   - [Connect to source code](dotnet-web-connect-source-code.md "dotnet-web-connect-source-code.md")

2. **Discovery and assessment**

   - [Discover and confirm repositories](dotnet-web-confirm-repos.md "dotnet-web-confirm-repos.md")
   - [Set transformation mode](dotnet-web-settings.md "dotnet-web-settings.md")
   - [Assessment](dotnet-web-assessment.md "dotnet-web-assessment.md")

3. **Prepare for transformation**

   - [Resolve missing package dependencies](dotnet-web-resolve-dependencies.md "dotnet-web-resolve-dependencies.md")
   - [Review and customize transformation plan](dotnet-web-review-and-customize-plan.md "dotnet-web-review-and-customize-plan.md")

4. **Transformation and checkpoint reviews**

   - [Transform your .NET code](dotnet-web-transform-code.md "dotnet-web-transform-code.md")

5. **End of transformation**

   - [Review transformation artifacts](dotnet-web-final-summary.md "dotnet-web-final-summary.md")
   - [Validate and finalize with AI code companion](dotnet-next-steps.md "dotnet-next-steps.md")

### Developer hand-off

Hand-off of repositories to developers is common, and can happen in two ways:

1. **Early hand-off:** For complex repositories, have developers perform the transformation in IDE instead of using the web application. Complex repositories are best transformed by developers working on one solution at a time in Visual Studio, interactively and iteratively, where they can directly review the transformed code and guide the agent at project level. AWS Transform will recommend handing off complex repositories to developers after assessment.
2. **Post-transformation hand-off:** After repositories are transformed in the web application, hand them off to developers to review, validate, and debug the transformed application - typically assisted by an AI code companion. See [Beam a transformed repository to a developer](dotnet-web-final-summary.md#beam-transformed-repository "dotnet-web-final-summary.md#beam-transformed-repository").
