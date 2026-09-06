

# Transformation Report
<a name="dotnet-report"></a>

After a transformation job finishes, transformation reports are available for both web console and IDE users.
+ **Web console users:** a transformation report is available for each transformed repository. You can download transformation reports from the dashboard or the **Artifacts** tab.
+ **IDE**: download the transformation report from the **AWS Transform Job Plan** window using the download icon.

The transformation report is an interactive HTML report. It contains in-depth information about the transformation, including the reasons for file changes and actionable error details. The information is arranged in the following hierarchy:
+ Job Information
+ For each solution:
  + Solution Transformation Summary
  + Transformation Overview
  + Projects
  + For each project:
    + Project Summary
    + Build Errors Summary
    + NuGet package changes
    + File Changes
    + Build Errors
  + Unit Test Results

For a walk-through of the transformation detail report sections with examples, refer to the blog post [Announcing AWS Transform for .NET detailed transformation reports](https://aws.amazon.com/blogs/dotnet/announcing-aws-transform-for-net-detailed-transformation-reports/).