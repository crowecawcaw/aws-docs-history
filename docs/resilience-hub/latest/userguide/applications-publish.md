# Publishing a new AWS Resilience Hub application

version

After you make changes to your AWS Resilience Hub application resources as described in [Editing AWS Resilience Hub application resources](application-resources.md "application-resources.md"), you must
publish a new version of your application to run an accurate resiliency assessment.
Also, you might need to publish a new version of your application if you added new
recommended alarms, SOPs, and tests to your application.

###### To publish a new version of your application

1. In the navigation pane, choose **Applications**.
2. On the **Applications** page, choose the name of the
   application.
3. Choose the **Application structure** tab.
4. Choose **Publish new version**.
5. In **Publish version** dialog, in the
   **Name** box, enter a name for the application version or
   you can use the default name suggested by AWS Resilience Hub.
6. Choose **Publish**.

When you publish a new version of your application, this becomes the version
that is assessed when you run resiliency assessments. Also, the draft version
will be identical to the released version until you make any changes.
After you publish a new version of your application, we recommend you to run a new
resiliency assessment report to confirm your application still meets your resiliency
policy. For information about running an assessment, see [Running and managing resiliency assessments in
AWS Resilience Hub](resil-assessments.md "resil-assessments.md").
