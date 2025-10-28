# Using the workflow wizard

## Creating a workflow

1. Determine which type of output or outputs you need.

If you're not sending to Facebook, Twitch, or YouTube, your major decision
is whether to use MediaPackage or MediaStore. If you plan to repackage the output,
choose [MediaPackage](https://aws.amazon.com/mediapackage/ "https://aws.amazon.com/mediapackage/"). If
you don't know about repackaging and suspect that you don't need it, you
could choose [MediaStore](https://aws.amazon.com/mediastore/ "https://aws.amazon.com/mediastore/").
You can always modify the workflow later, if you find you made the wrong
decision. 2. Determine which type of source you have. If necessary, speak to the person
who is providing the source. 3. If the source is using the RTMP protocol, you must set up an input
security group using the regular MediaLive console. See [Working with input security groups](working-with-input-security-groups.md "working-with-input-security-groups.md"). 4. Make sure that you have set up the IAM permissions
that your users must have so that they can create and
run the workflow. See [Setting up IAM permissions for
users](setting-up-for-production.md "setting-up-for-production.md"), and
specifically [Reference: summary of
non-administrator user access requirements](setup-users-step-1-summary.md "setup-users-step-1-summary.md") 5. Sign in to the AWS Management Console and open the MediaLive console at [https://console.aws.amazon.com/medialive/](https://console.aws.amazon.com/medialive/ "https://console.aws.amazon.com/medialive/"). 6. Choose **Workflow wizard** from the navigation panel.
Follow the steps in the workflow wizard. 7. After you choose **Create** on the
page, details about the workflow appear. A card appears
for each resource that the workflow wizard involves.

The workflow wizard creates a AWS CloudFormation stack. AWS CloudFormation runs
that stack to create all the other resources:

    * One MediaLive input.
    * One MediaLive channel.
    * All the resources in all AWS services that
     are involved in the workflow you have created.
     You workflow might involve MediaPackage, MediaStore, and
     CloudFront.

8. When the resources have all been created, you can choose **Start
   workflow** on the details page for the workflow. The wizard
   starts the channel. The wizard also starts the MediaConnect flow, if you have
   one.

## Modifying a workflow

You can't use the workflow wizard to modify an existing workflow. For suggestions
about making changes, see [Next steps—novice users](wizard-next-step-novice.md "wizard-next-step-novice.md") and [Next steps—experienced video
users](wizard-next-step-experienced.md "wizard-next-step-experienced.md").

## Deleting a workflow

You can delete the workflow. MediaLive handles the resources that belong to the
workflow as follows:

- It always deletes the channel.
- It always deletes the AWS CloudFormation stack.
- It deletes the input, if the workflow wizard created
  it. It doesn't delete the input if the input already
  existed.

- It deletes the flow associated with a MediaConnect input (if there is one), if
  the workflow wizard created the flow.
- It deletes the MediaPackage channel (if there is one) and its endpoints.
- It attempts to delete the MediaStore container, if there is one and if the
  workflow wizard created it. Deletion will fail if the container has any
  objects in it, including objects that aren't associated with this
  workflow.
- It deletes the CloudFront distribution, if the workflow wizard created
  it.
