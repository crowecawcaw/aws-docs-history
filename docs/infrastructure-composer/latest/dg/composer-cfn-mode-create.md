# Create a new template in Infrastructure Composer in CloudFormation console mode

Follow the instructions in this topic to create a new template.

1. Go to the [CloudFormation console](https://console.aws.amazon.com/cloudformation "https://console.aws.amazon.com/cloudformation") and log in.
2. Select **Infrastructure Composer** from the left-side navigation menu. This will open Infrastructure Composer in CloudFormation console mode.
3. Drag, drop, configure, and connect the resources ([cards](using-composer-cards-intro.md "using-composer-cards-intro.md")) you need from the **Resources** pallete.

###### Note

See [How to compose](using-composer-basics.md "using-composer-basics.md") for details on using Infrastructure Composer, and
note that Lambda-related cards (**Lambda Function** and **Lambda Layer**) require code builds and packaging solutions that are not available in
Infrastructure Composer in CloudFormation console mode. These cards can be used in the [Infrastructure Composer console](https://aws.amazon.com/application-composer/ "https://aws.amazon.com/application-composer/")
or the AWS Toolkit for Visual Studio Code. For information on using these tools, refer to [Where you can use Infrastructure Composer](using-composer.md "using-composer.md"). 4. Double click cards to use the **Resource properties** panel to specify how cards are configured. 5. [Connect your cards](using-composer-connecting.md "using-composer-connecting.md") to specify your application’s event-driven workflow. 6. Select **Template** to view and edit your infrastructure code. Changes are automatically synced with your canvas view. 7. Once your template is ready to be exported into a stack, select **Create template**. 8. Select the **Confirm and export to CloudFormation** button. This will take you back to the create stack workflow with a message confirming your template was successfully imported.

###### Note

Only templates with resources in them can be exported. 9. In the **Create stack** workflow, select **Next**. 10. Provide a stack name, review any listed parameters, and select **Next**.

###### Note

The stack name must start with a letter and contain only letters, numbers, dashes. 11. Select **Next** after providing the following information:

    * Tags associated with the stack
    * Stack permissions
    * The stack's failure options

###### Note

For guidance on managing stacks, see
[CloudFormation best practices](../../../AWSCloudFormation/latest/UserGuide/best-practices.md "../../../AWSCloudFormation/latest/UserGuide/best-practices.md") in the _CloudFormation User Guide_. 12. Confirm your stack details are correct, check acknowledgements at the bottom of the page, and select the **Submit** button.
CloudFormation will begin creating the stack based on the data in your template.
