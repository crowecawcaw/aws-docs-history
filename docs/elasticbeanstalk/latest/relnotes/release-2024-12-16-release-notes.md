# Release: Automatic Elastic Beanstalk environment state update after recovered CloudFormation stack on December 16, 2024

AWS Elastic Beanstalk provides automatic state update for environments with recovered CloudFormation stacks.

**Release date:** December 16, 2024

## Changes

Today we released the capability for Elastic Beanstalk to automatically detect and change your environment’s state after you complete
corrective actions to restore its CloudFormation stack. This type of corrective action is normally required to address permission issues.

Prior to this release, after you completed the recommended actions to restore the environment's CloudFormation stack, you would have to contact AWS
Support to reset the environment state. With this release, after you successfully complete the corrective actions, Elastic Beanstalk automatically updates the
environment's state from invalid to available. You can then resume the standard operations on your environment without further delay.

For more information, see
[Recovering your Elastic Beanstalk environment from an invalid stack state](../dg/environment-management-invalid-stack.md "../dg/environment-management-invalid-stack.md") in
the _AWS Elastic Beanstalk Developer Guide_.
