# Update an existing stack in Infrastructure Composer in CloudFormation console mode

Follow the instructions in this topic to update an existing AWS CloudFormation stack.

###### Note

If your file is saved locally, we recommend using [AWS Toolkit for Visual Studio Code](using-composer-ide.md "using-composer-ide.md").

1. Go to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation "https://console.aws.amazon.com/cloudformation") and log in.
2. Select the stack you want to edit.
3. Select the **Update** button. Doing this will take you to the update stack wizard.
4. On the right, select **Edit in Infrastructure Composer**.
5. Select the button below that's labeled **Edit in Infrastructure Composer**. This will take you to Infrastructure Composer in CloudFormation console mode.
6. Here, you can drag, drop, configure, and connect resources ([cards](using-composer-cards-intro.md "using-composer-cards-intro.md")) from the **Resources** pallete.

###### Note

See [How to compose](using-composer-basics.md "using-composer-basics.md") for details on using Infrastructure Composer, and
note that Lambda-related cards (**Lambda Function** and **Lambda Layer**) require code builds and packaging solutions that are not available in
Infrastructure Composer in CloudFormation console mode. These cards can be used in the [Infrastructure Composer console](https://aws.amazon.com/application-composer/ "https://aws.amazon.com/application-composer/")
or the AWS Toolkit for Visual Studio Code. For information on using these tools, refer to [Where you can use Infrastructure Composer](using-composer.md "using-composer.md"). 7. When you are ready to export changes to AWS CloudFormation, select **Update template**. 8. Select **Confirm and continue to CloudFormation**. This will take you back to the **Update stack** workflow with a message confirming
your template was successfully imported.

###### Note

Only templates with resources in them can be exported. 9. In the **Update stack** workflow, select **Next**. 10. Review any listed parameters and select **Next**. 11. Select **Next** after providing the following information:

    * Tags associated with the stack
    * Stack permissions
    * The stack's failure options

###### Note

For guidance on managing stacks, see
[AWS CloudFormation best practices](../../../AWSCloudFormation/latest/UserGuide/best-practices.md "../../../AWSCloudFormation/latest/UserGuide/best-practices.md")
in the _AWS CloudFormation User Guide_. 12. Confirm your stack details are correct, check acknowledgements at the bottom of the page, and select the **Submit** button.
AWS CloudFormation will begin updating the stack based on the updates you made in your template.
