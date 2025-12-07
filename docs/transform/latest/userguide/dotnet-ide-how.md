# How AWS Transform modernizes .NET applications

Review the following sections for details about how .NET transformation with AWS Transform works.

## Analyzing your application and generating a transformation plan

Before a transformation begins, AWS Transform builds your code locally to verify
that it is buildable and configured correctly for transformation. If the code does not build,
AWS Transform will prompt whether to continue with transformation. AWS Transform then
uploads your code to a secure and encrypted build environment on AWS, analyzes your codebase, and
determines the necessary updates to port your application

During this analysis, AWS Transform divides your .NET solution or project into code
groups. A code group is a project and all its dependencies that together generate a
buildable unit of code such as a dynamic link library (DLL) or an executable. Even
if you didn't select all project dependencies to be transformed, AWS Transform determines
the dependencies needed to build your selected projects and transforms them too, so
that your transformed application will be buildable and ready for use.

After analyzing your code, AWS Transform generates a transformation plan that outlines the
proposed changes that it will make, including a list of code groups and their
dependencies that will be transformed.

## Transforming your application

To start the transformation, AWS Transform builds your code again in the secure build
environment to verify if it is buildable remotely. AWS Transform then begins porting your
application. It works from the bottom up, starting with the lowest level dependency. If
AWS Transform runs into an issue with porting a dependency, it stops the transformation and
provides information about what caused the error.

The transformation includes the following updates to your application:

- Replacing outdated C# versions of code with Linux-compatible C# versions
- Upgrading .NET Framework to cross-platform .NET, including:
  - Identifying and iteratively replacing packages, libraries, and APIs
  - Upgrading and replacing NuGet packages and APIs
  - Transitioning to cross-platform runtime
  - Setting up middleware and updating runtime configurations
  - Replacing private or third-party packages
  - Handling IIS and WCF components
  - Debugging build errors

- Rewriting code for Linux compatibility, including refactoring and rewriting
  deprecated and inefficient code to port existing code

## Reviewing transformation

report and accepting changes

After the transformation is complete, AWS Transform provides a transformation report with
information about the proposed updates it made to your application, including the number
of files changed, packages updated, and APIs changed. It flags any unsuccessful
transformations, including affected files or portions of files and the errors
encountered during an attempted build. You can also view a build summary with build logs
to learn more about what changes were made.

The transformation report also provides a Linux porting status, which indicates
whether or not additional user input is needed to make the application Linux
compatible. If any of the items in a code group require input from you, you download
a Linux readiness report that contains Windows-specific considerations that AWS Transform
could not address at build time. If input is needed for any code groups or files,
review the report for details about what type of change still needs to be made and,
if applicable, for recommendations for how to update your code. These changes must
be made manually before your application can be run on Linux.

You can review the proposed changes AWS Transform made in a diff view before accepting them
as in-place updates to your files. After updating your files and addressing any items in
the Linux readiness report, your application is ready to run on cross-platform
.NET.

You can download a _Next Steps_ markdown file
with prompts for continued transformation with AWS Transform or an AI code companion. To
download the file, choose the **Download Next Steps** button at the top
right of the report.
