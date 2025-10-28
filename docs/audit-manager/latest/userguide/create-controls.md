# Creating a custom control in AWS Audit Manager

You can use custom controls to collect evidence for your specific compliance needs.

Just like standard controls, custom controls collect evidence continually when they’re
active in your assessments. You can also add manual evidence to any custom control that you
create. Each piece of evidence becomes a record that helps you to demonstrate compliance with
your custom control’s requirements.

To get started, here are some examples of how you can use custom controls:

**Map your enterprise controls to predefined groupings of AWS
data sources**

You can onboard your enterprise controls to Audit Manager by using common controls as an
evidence source. Choose the common controls that represent your goals, and use them as
building blocks to create a control that collects evidence across your portfolio of
compliance needs. Each automated common control maps to a predefined grouping of data
sources. This means that you don’t have to be an AWS expert to know which data
sources collect the relevant evidence for your goals. And when you use common controls
as an evidence source, you no longer have to maintain data source mappings, because
Audit Manager handles this for you.

**Create a vendor risk assessment question**

You can use custom controls to support how you manage vendor risk assessments.
Each control that you create can represent an individual risk assessment question. For
example, the control name can be a question, and you can provide an answer by
uploading a file or entering a text response as manual evidence.

## Key points

When it comes to creating custom controls in Audit Manager, you have two methods to choose
from:

1. **Creating a control from scratch** - This method
   provides maximum flexibility and enables you to tailor the control to your exact needs.
   This is a good option when you have a specific compliance requirement that isn't
   adequately covered by an existing control. This method is particularly useful when you
   need to map your organization's enterprise controls to predefined groupings of AWS
   data sources or when you want to create vendor risk assessment questions as individual
   controls.
2. **Making an editable copy of an existing control** - If
   an existing standard control or custom control partially meets your needs, you can make
   an editable copy of that control. This approach is more efficient if you only need to
   make minor changes to an existing control. This is a good option if you want to adjust a
   few attributes to better align the control with your specific requirements. For example,
   you might change how often a control uses an API call to collect evidence, and then
   change the control’s name to reflect this.

## Additional resources

For instructions on how to create a custom control, see the following resources.

- [Creating a custom control from scratch in
  AWS Audit Manager](customize-control-from-scratch.md "customize-control-from-scratch.md")
- [Making an editable copy of a control in
  AWS Audit Manager](customize-control-from-existing.md "customize-control-from-existing.md")
