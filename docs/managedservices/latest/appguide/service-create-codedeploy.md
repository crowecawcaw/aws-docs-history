End of support notice: On June 30, 2027, AWS
will end support for AMS Advanced. After June 30, 2027, you will
no longer be able to access the AMS Advanced console or AMS Advanced resources.
For more information, see [AMS Advanced end of support](../userguide/SunsetPlan.md "../userguide/SunsetPlan.md").

# CodeDeploy requests

You can use AWS CodeDeploy to create application containers that you can then deploy
through a CodeDeploy application group. For more information about CodeDeploy, see [AWS CodeDeploy Documentation](../../../codedeploy/index.md "../../../codedeploy/index.md").

Working with AWS CodeDeploy involves the following process:

1. Create a CodeDeploy application. The CodeDeploy application is a name or container used by
   CodeDeploy to ensure that the correct revision, deployment configuration, and
   deployment group are referenced during a deployment.
2. Create a CodeDeploy deployment group. A CodeDeploy deployment group defines a set of individual instances targeted for a deployment. AMS has a separate change type for CodeDeploy deployment groups for EC2.
3. Deploy the CodeDeploy application through the CodeDeploy deployment group.
