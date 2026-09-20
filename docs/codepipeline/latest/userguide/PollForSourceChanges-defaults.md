

# Valid settings for the `PollForSourceChanges` parameter
<a name="PollForSourceChanges-defaults"></a>

The `PollForSourceChanges` parameter default is determined by the method used to create the pipeline, as described in the following table. In many cases, the `PollForSourceChanges` parameter defaults to true and must be disabled. 

When the `PollForSourceChanges` parameter defaults to true, you should do the following:
+ Add the `PollForSourceChanges` parameter to the JSON file or CloudFormation template.
+ Create change detection resources (CloudWatch Events rule, as applicable).
+ Set the `PollForSourceChanges` parameter to false.
**Note**  
If you create a CloudWatch Events rule or webhook, you must set the parameter to false to avoid triggering the pipeline more than once.

  The `PollForSourceChanges` parameter is not used for Amazon ECR source actions.
+ 


**`PollForSourceChanges` parameter defaults**  

<table>
<thead>
  <tr><th>Source</th><th>Creation method</th><th>Example "configuration" JSON structure output</th></tr>
</thead>
<tbody>
  <tr><td rowspan="2">CodeCommit</td><td>Pipeline is created with the console (and change detection resources are created by the console). The parameter is displayed in the pipeline structure output and defaults to <code>false</code>.</td><td> <pre>BranchName": "main", <br />"PollForSourceChanges": "false",<br />"RepositoryName": "my-repo"</pre> </td></tr>
  <tr><td>Pipeline is created with the CLI or CloudFormation, and the <code>PollForSourceChanges</code> parameter is not displayed in JSON output, but it sets to <code>true</code>.²</td><td> <pre>BranchName": "main", <br />"RepositoryName": "my-repo"</pre> </td></tr>
  <tr><td rowspan="2">Amazon S3</td><td>Pipeline is created with the console (and change detection resources are created by the console). The parameter is displayed in the pipeline structure output and defaults to <code>false</code>.</td><td> <pre>"S3Bucket": "my-bucket",<br />"S3ObjectKey": "object.zip",<br />"PollForSourceChanges": "false"</pre> </td></tr>
  <tr><td>Pipeline is created with the CLI or CloudFormation, and the <code>PollForSourceChanges</code> parameter is not displayed in JSON output, but it sets to <code>true</code>.²</td><td> <pre>"S3Bucket": "my-bucket",<br />"S3ObjectKey": "object.zip"</pre> </td></tr>
  <tr><td rowspan="2">GitHub</td><td>Pipeline is created with the console (and change detection resources are created by the console). The parameter is displayed in the pipeline structure output and defaults to <code>false</code>.</td><td> <pre>"Owner": "{{MyGitHubAccountName}}",<br />"Repo": "{{MyGitHubRepositoryName}}"<br />"PollForSourceChanges": "false", <br />"Branch": "{{main}}"<br />"OAuthToken": "{{****}}"</pre> </td></tr>
  <tr><td>Pipeline is created with the CLI or CloudFormation, and the <code>PollForSourceChanges</code> parameter is not displayed in JSON output, but it sets to <code>true</code>.²</td><td> <pre>"Owner": "{{MyGitHubAccountName}}", <br />"Repo": "{{MyGitHubRepositoryName}}", <br />"Branch": "{{main}}", <br />"OAuthToken": "{{****}}"</pre> </td></tr>
  <tr><td></td><td colspan="2">² If <code>PollForSourceChanges</code> has been added at any point to the JSON structure or the CloudFormation template, it is displayed as shown: <pre><br />"PollForSourceChanges": "true",<br /></pre><br />³ For information about the change detection resources that apply to each source provider, see <a href="change-detection-methods.md">Change Detection Methods</a>.</td></tr>
</tbody>
</table>
