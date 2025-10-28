# Create a CloudFormation

stack from scanned resources

After you create your template, you can preview the generated template with Infrastructure Composer
before creating the stack and importing the scanned resources. This helps you visualize
the full application architecture with the resources and their relationships. For more
information about Infrastructure Composer, see [Create templates visually with Infrastructure Composer](infrastructure-composer-for-cloudformation.md "infrastructure-composer-for-cloudformation.md").

###### To create the stack and import the scanned resources

1. Open the [IaC generator page](https://console.aws.amazon.com/cloudformation/home?#iac-generator "https://console.aws.amazon.com/cloudformation/home?#iac-generator") of the CloudFormation console.
2. On the navigation bar at the top of the screen, choose the AWS Region for
   your template.
3. Choose the **Templates** tab, and then choose the name of
   your template to view more information.
4. On the **Template definition** tab, at the top of the
   **Template** section, you can switch the template from YAML
   to JSON syntax based on your preference.
5. Review the details of your template to make sure everything is set up
   correctly. To make it easier to review and understand the template, you can
   switch from the default code view to a graphical view of the infrastructure
   described in the template using Infrastructure Composer. To do so, under
   **Template**, choose **Canvas** instead of
   **Template**.

**Canvas actions**

    * To focus on the details of a specific resource within your template,
     double-click a card to bring up the **Resource
     properties** panel.
    * To visually arrange and organize cards on the canvas, choose
     **Arrange** from the upper left of the canvas.
    * To zoom in and out of your canvas, use the zoom controls in the lower
     right of the canvas.

6. To view a specific resource in the console, choose the **Template
   resources** tab and then choose the physical ID of the resource you
   want to look at. This takes you to the console for that specific resource. You
   can also add, remove, and resync resources in the template definition from the
   **Template resources** tab.
7. On the **Template definition** tab, IaC generator might issue
   warnings about resources that contain write-only properties. After reviewing the
   warnings, you can download the generated template and make any necessary
   changes. For more information, see [Resolve write-only properties](generate-IaC-write-only-properties.md "generate-IaC-write-only-properties.md").
8. When you are satisfied with your template definition, on the
   **Template definition** tab, choose **Import to
   stack** and then choose **Next**.
9. On the **Specify stack** panel of the **Specify stack
   details** page, enter the name of your stack, and then choose
   **Next**.
10. Review and enter the parameters for the stack. Choose
    **Next**.
11. Review your options on the **Review changes** page and choose
    **Next**.
12. Review your details on the **Review and import** page and
    choose **Import resources**.
