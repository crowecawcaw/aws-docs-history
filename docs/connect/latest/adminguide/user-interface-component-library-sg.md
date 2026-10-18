

# Component library in the Connect Customer UI builder
<a name="user-interface-component-library-sg"></a>

Connect Customer offers a library of UI components to build views. This [reference guide](https://d3irlmavjxd3d8.cloudfront.net/?path=/docs/overview--page) describes every component and how to configure it.

To find the components, open the **Library** tab of the **Create** panel in the UI builder. The following image shows an example of the **Library** tab and the **Container** components.

![The UI builder Create panel, the Library tab, the UI components.](https://docs.aws.amazon.com/connect/latest/adminguide/images/user-interface-component-library-example.png)


## Use containers to group components
<a name="user-interface-component-library-containers"></a>

Containers are the core building block of a view. You can move UI components (including other containers) into a container to group them together logically and visually on the page.

Use containers in every view, so the page stays consistent when you change view-level settings. Containers also have a column layout for arranging their contents.

## Create a form
<a name="user-interface-component-library-form-section"></a>

To create a form that users fill in and submit, use the [Form](https://d3irlmavjxd3d8.cloudfront.net/?path=/story/aws-managed-views-form--with-all) component. You can either:
+ Drag a **Form** component from the **Library** tab onto the canvas.
+ From the **Templates** tab, choose the **Form Example** template, which uses a Form component.

A [Form](https://d3irlmavjxd3d8.cloudfront.net/?path=/story/aws-managed-views-form--with-all) component is a special type of container into which you can insert input fields and add a **Submit** button. When a user chooses **Submit**, Connect Customer passes all of the values entered into the form fields to the flow. At that point in the flow, you can customize your own business logic and send data to and retrieve data from third-party systems by using the [AWS Lambda function](invoke-lambda-function-block.md) block.

The following image shows an example **Form** component with placeholder labels and a Submit button.

![A Form component with placeholder labels and a Submit button.](https://docs.aws.amazon.com/connect/latest/adminguide/images/user-interface-component-library-form-section-example.png)
