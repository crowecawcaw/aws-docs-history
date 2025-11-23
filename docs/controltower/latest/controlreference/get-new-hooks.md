# Update your proactive control hooks

To update the way that AWS Control Tower handles the CloudFormation hooks for your enabled proactive
controls, follow the steps given in this section.

After you complete this process, you can utilize the full capacity of CloudFormation hooks, without
restriction by AWS Control Tower. It eliminates the need to apply the [**CT.CLOUDFORMATION.PR.1** preventive control](../../../ /controltower/latest/controlreference/elective-preventive-controls.md#disallow-cfn-extensions "../../../ /controltower/latest/controlreference/elective-preventive-controls.md#disallow-cfn-extensions") before you
can enable proactive controls.

The first time that you enable a proactive control, AWS Control Tower turns on the hook that it
requires, without restricting any other CloudFormation hooks that you may have deployed on AWS.
Only AWS Control Tower can change the AWS Control Tower hook, but principals with the correct permissions can
change other CloudFormation hooks in your environment.

If you enabled proactive controls before [the launch of the
service-linked hook integration](../userguide/2024-all.md#hook-management "../userguide/2024-all.md#hook-management"), follow these steps.

###### To update your proactive control hooks

- Reset any one enabled proactive control on the current OU by calling the
  **ResetEnabledControl** API or using the console’s
  **Reset control** button on the **Control**
  page.
- Navigate to the **CT.CLOUDFORMATION.PR.1** control in the
  AWS Control Tower controls library.
- Disable the **CT.CLOUDFORMATION.PR.1** control.
  Repeat this procedure for each OU that has proactive controls enabled, if those controls
  were enabled before [the launch of the
  service-linked hook integration](../userguide/2024-all.md#hook-management "../userguide/2024-all.md#hook-management").

###### Important

The **Reset** function resets control drift.
**Reset** operates differently for proactive controls than for any
other type of control in AWS Control Tower. When you reset any enabled proactive control on an
OU, all of the enabled proactive controls for that OU are reset. This behavior happens
because the artifacts for all enabled proactive controls are bundled together, and they
are deployed together, each time the `ResetEnabledControl` API is
called.
