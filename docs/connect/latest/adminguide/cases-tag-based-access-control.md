# Set up tag-based access controls on cases

You can use resource tags and access control tags to apply granular access to cases in Amazon Connect Cases. For example, you can control who has access to view, create, or edit cases containing sensitive customer information based on department, case type, or security classification.

Tag-based access controls enable you to configure granular access to specific cases based on assigned resource tags. Cases inherit tags from their associated case templates, ensuring consistent access control without requiring agents to manually tag individual cases. You can configure tag-based access controls by using the API or the Amazon Connect admin website. For more information, see [Add tags to resources in Amazon Connect](tagging.md "tagging.md") and [Apply tag-based access control in
Amazon Connect](tag-based-access-control.md "tag-based-access-control.md").

## How tag propagation works for cases

When you create a case using a case template, the case automatically inherits the tags configured on that template. This ensures consistent access control and reduces the risk of human error in tagging individual cases. It is important to note that tags specified during case creation will override any conflicting tags from the template.

For example, if you tag a "Fraud Investigation" template with `Department:Fraud`, all cases created using that template will automatically receive the `Department:Fraud` tag, restricting access to users with appropriate permissions. However, if a CreateCase public API request is made with the same "Fraud Investigation" template with `Department:Finance` in the request, the case will instead have the `Department:Finance` tag.

## How to enable tag-based access control for cases

To apply tags to control access to cases:

- **Tag your case templates**: Apply tags to case templates that will be inherited by all cases created from those templates. You can add tags when creating or editing templates in the Amazon Connect admin website or by using the Amazon Connect Cases CreateTemplate or UpdateTemplates APIs.
- **Configure security profiles**: Assign users to security profiles that grant access to specific case tags. On the Security profiles page, choose **Show advanced options** to configure tag-based permissions for the Cases resource. For more information about configuring access control tags, see [Apply tag-based access control in
  Amazon Connect](tag-based-access-control.md "tag-based-access-control.md").
- **Set appropriate permissions**: Users need one of the following permissions to work with cases:
  - **Cases - Create**: Allows creating new cases (requires permission for tags that will be applied)
  - **Cases - View**: Allows viewing existing cases with matching tags
  - **Cases - Edit**: Allows modifying existing cases with matching tags
