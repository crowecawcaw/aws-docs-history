# Transforming your .NET code

After the AWS account administrator finishes [Reviewing your plan to prepare for transformation](dotnet-reviewing-plan.md "dotnet-reviewing-plan.md"), you can view the transformation progress
on the _Dashboard_ tab of your transformation job.

###### Note

In addition to transforming repositories and dependencies, AWS Transform
can execute fully transformed (zero build errors) unit test projects. AWS Transform doesn't have access to unit test results
prior to the transformation and can only share post-transformation results.
You can then compare your baseline data, prior to transformation, with the post-transformation results to understand any potential gaps.

In the top right corner, you can see the job status, which has one of the following values:

- Awaiting user input
- Time elapsed
- Running
  You can also see the following icons:

- A stop transformation icon
- A refresh icon
- A settings icon
  The _Dashboard_ provides a high level summary of the transformation. It
  shows metrics for the number of jobs transformed and transformation applied, and the estimated
  time to complete the transformation.

The _Dashboard_ includes:

1.  The transformation _Job details_ section, which lists the default
    settings and details of the transformation job, including:
    1. _Target branch destination_
       To transform your code, AWS Transform creates a new branch for the transformed code in your code repo.
    2. _Target .NET version_, .NET 8.0 or .NET 10
    3. The AWS Transform _job ID._
    4. The job settings:
       1. Exclude .NET standard projects

2.  The _Transformation summary_ section contains:

        1. The number of repositories selected for transformation
        2. The number of projects to be transformed
        3. The total lines of codes in these repositories and projects

    After the transformation starts, pie charts appear in the _Repository
    status_, _Package status_, and _Unit test
    status_ sections displaying progress in real time. The _Unit test
    status_ shows the status of unit tests located in your repositories that
    AWS Transforms runs after transformation to test the transformed code. AWS Transform shares the
    executed test results, along with individual test name for customers to review the list of
    unit tests passed and failed.

###### Note

The _Repositories_ section lists the repositories that AWS Transform recommends or that you selected for transformation.
Select **Download JSON** to download a list of repositories, dependencies, and packages in your transformation plan.

## Review the transformation reports

After a transformation job completes, you can download [Transformation Reports](tdotnet-reports.md "tdotnet-reports.md"):

- [Transformation summary report](tdotnet-reports.md#transformation-summary-report "tdotnet-reports.md#transformation-summary-report"): This report provides an overview of the transformation in HTML or JSON format.
  Download the transformation summary report from the **Dashboard tab**. Select **Download**, and choose **Download as HTML** or **Download as JSON**.
- [Transformation detail report](tdotnet-reports.md#transformation-detail-report "tdotnet-reports.md#transformation-detail-report"):
  This report provides in-depth information about a transformation in HTML format. Download transformation detail reports from the **Dashboard tab**.
  Select a **Download detailed report** link in the repository list to download a detail report.

### Chat with AWS Transform about the transformation report

You can chat with AWS Transform about the transformation report after a repository has been
completely processed or after the transformation job is completed. The
**Worklog** tab displays this message for each repository that is
available for chat: _Repository `repository_name` transformation
details are now available in chat for queries_. It displays this message when the transformation job is completed: _AWS Transform transformation job is completed_.

To open the chat click the purple hexagonal icon in the lower
right corner of the web console.

Here are some example prompts:

- Which projects were successfully transformed?
- Which projects were partially ported?
- What changes were made to the `repo_name` repository?
- What packages were upgraded in the `project_name` project?
