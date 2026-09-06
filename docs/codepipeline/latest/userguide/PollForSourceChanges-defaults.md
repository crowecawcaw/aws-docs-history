

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
[See the AWS documentation website for more details](http://docs.aws.amazon.com/codepipeline/latest/userguide/PollForSourceChanges-defaults.html)