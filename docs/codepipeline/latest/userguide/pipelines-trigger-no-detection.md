# Add trigger to turn off change detection

Triggers allow you to configure your pipeline to start on a particular event type, such as
a code push or pull request. Triggers are configurable for source actions with connections
that use the `CodeStarSourceConnection` action in CodePipeline, such as GitHub,
Bitbucket, and GitLab.

###### Adding a trigger to turn off change detection (console)

1. Sign in to the AWS Management Console and open the CodePipeline console at [http://console.aws.amazon.com/codesuite/codepipeline/home](http://console.aws.amazon.com/codesuite/codepipeline/home "http://console.aws.amazon.com/codesuite/codepipeline/home").

The names and status of all pipelines associated with your AWS account are
displayed. 2. In **Name**, choose the name of the pipeline you want to edit.
Otherwise, use these steps on the pipeline creation wizard. 3. On the pipeline details page, choose **Edit**. 4. On the **Edit** page, choose the source action you want to edit.
Choose **Edit triggers**. Choose to add a trigger. 5. In **Trigger type**, choose **Do not detect
changes**.
