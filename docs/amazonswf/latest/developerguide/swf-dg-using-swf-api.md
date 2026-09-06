

# Working with Amazon SWF APIs
<a name="swf-dg-using-swf-api"></a>

In addition to using the AWS SDKs that are described in [Develop with AWS SDKs](intro.md#aws-sdks), you can use the HTTP API directly.

To use the API, you send HTTP requests to the [SWF endpoint](https://docs.aws.amazon.com/general/latest/gr/rande.html#swf_region) that matches the region that you want to use for your domains, workflows and activities. For more information about making HTTP requests for Amazon SWF, see [Making HTTP Requests to Amazon SWF](UsingJSON-swf.md).

This section provides basic information about using the HTTP API to develop your workflows with Amazon SWF. More advanced features, such as using timers, logging with CloudTrail and tagging your workflows are provided in the section, [Basic workflow concepts in Amazon SWF](swf-dg-basic.md).

**Topics**
+ [Making HTTP Requests](UsingJSON-swf.md)
+ [List of Amazon SWF Actions](swf-api-by-category.md)
+ [Registering a Domain](swf-dg-register-domain-api.md)
+ [Setting timeout values](setting-timeouts.md)
+ [Registering a Workflow Type](swf-dg-register-workflow.md)
+ [Registering an Activity Type](swf-dg-register-activity.md)
+ [Lambda tasks](lambda-task.md)
+ [Developing an Activity Worker](swf-dg-develop-activity.md)
+ [Developing deciders](swf-dg-dev-deciders.md)
+ [Starting workflows](swf-dg-start-workflow-exec.md)
+ [Setting task priority](programming-priority.md)
+ [Handling errors](swf-dg-error-handling.md)