End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Your Python simulation fails to start

You might see an `Unable to start app` error in your simulation's management log. This
can happen if your custom container creation failed. For more information, see
[Failure during custom container creation](working-with_python_troubleshooting_create-container-failure.md "working-with_python_troubleshooting_create-container-failure.md"). For more information
about logs, see [SimSpace Weaver logs in Amazon CloudWatch Logs](cloudwatch-logs.md "cloudwatch-logs.md").

If you're sure that there's nothing wrong with your container, check your app's Python source code.
You can use SimSpace Weaver Local to test your app. For more information, see
[Local development in SimSpace Weaver](working-with_local-development.md "working-with_local-development.md").
