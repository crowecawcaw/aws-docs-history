# Working with Amazon SWF APIs

In addition to using the AWS SDKs that are described in [Develop with AWS SDKs](intro.md#aws-sdks "intro.md#aws-sdks"), you can use the HTTP API directly.

To use the API, you send HTTP requests to the [SWF endpoint](../../../general/latest/gr/rande.md#swf_region "../../../general/latest/gr/rande.md#swf_region") that matches the region that
you want to use for your domains, workflows and activities. For more information about making HTTP requests for
Amazon SWF, see [Making HTTP Requests to Amazon SWF](UsingJSON-swf.md "UsingJSON-swf.md").

This section provides basic information about using the HTTP API to develop your workflows with Amazon SWF. More
advanced features, such as using timers, logging with CloudTrail and tagging your workflows are provided in the section,
[Basic workflow concepts in Amazon SWF](swf-dg-basic.md "swf-dg-basic.md").

###### Topics

- [Making HTTP Requests](UsingJSON-swf.md "UsingJSON-swf.md")
- [List of Amazon SWF Actions](swf-api-by-category.md "swf-api-by-category.md")
- [Registering a Domain](swf-dg-register-domain-api.md "swf-dg-register-domain-api.md")
- [Setting timeout values](setting-timeouts.md "setting-timeouts.md")
- [Registering a Workflow Type](swf-dg-register-workflow.md "swf-dg-register-workflow.md")
- [Registering an Activity Type](swf-dg-register-activity.md "swf-dg-register-activity.md")
- [Lambda tasks](lambda-task.md "lambda-task.md")
- [Developing an Activity Worker](swf-dg-develop-activity.md "swf-dg-develop-activity.md")
- [Developing deciders](swf-dg-dev-deciders.md "swf-dg-dev-deciders.md")
- [Starting workflows](swf-dg-start-workflow-exec.md "swf-dg-start-workflow-exec.md")
- [Setting task priority](programming-priority.md "programming-priority.md")
- [Handling errors](swf-dg-error-handling.md "swf-dg-error-handling.md")
