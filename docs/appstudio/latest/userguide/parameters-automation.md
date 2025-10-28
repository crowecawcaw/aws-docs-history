# Automation parameters

Automation parameters are a powerful feature in App Studio that can be used to create flexible and reusable
automations by passing dynamic values from various sources,
such as the UI, other automations, or data actions. They act as placeholders that are replaced with actual
values when the automation is run, allowing you to use the same automation with different inputs each time.

Within an automation, parameters have unique names, and you can reference a parameter's value using the params variable followed by the parameter's name, for example, `{{params.customerId}}`.

This article provides an in-depth understanding of automation parameters, including their fundamental concepts, usage, and best practices.

## Automation parameter benefits

Automation parameters provide several benefits, including the following list:

1. **Reusability**: By using parameters, you can create reusable automations that can be customized with different input
   values, allowing you to reuse the same automation logic with different inputs.
2. **Flexibility**: Instead of hard-coding values into an automation, you can define parameters and provide different
   values when needed, making your automations more dynamic and adaptable.
3. **Separation of concerns**: Parameters help separate the automation logic from the specific values used, promoting code organization and maintainability.
4. **Validation**: Each parameter has a data type, such as string, number, or boolean, which is validated at runtime. This ensures that
   requests with incorrect data types are rejected without the need for custom validation code.
5. **Optional and required parameters**: You can designate automation parameters as optional or required. Required parameters
   must be provided when running the automation, while optional parameters can have default values or be omitted. This flexibility allows you to create more versatile
   automations that can handle different scenarios based on the provided parameters.

## Scenarios and use cases

### Scenario: Retrieving product details

Imagine you have an automation that retrieves product details from a database based on a product ID. This automation could have a parameter called `productId`.

The `productId` parameter acts as a placeholder that you can fill in with the actual product ID value when running the automation.
Instead of hard-coding a specific product ID into the automation, you can define the `productId` parameter and pass in different product ID values each time you run the automation.

You could call this automation from a component's data source, passing the selected product's ID as the `productId` parameter using the
double curly bracket syntax: `{{ui.productsTable.selectedRow.id}}`. This way, when a user selects a product from a table (`ui.productsTable`),
the automation will retrieve the details for the selected product by passing the id of the selected row as the `productId` parameter.

Alternatively, you could invoke this automation from another automation that loops over a list of products and retrieves the details for each
product by passing the product's id as the `productId` parameter. In this scenario, the `productId` parameter value would be dynamically provided from the
`{{product.id}}` expression in each iteration of the loop.

By using the `productId` parameter and the double curly bracket syntax, you can make this automation more flexible and reusable. Instead of creating
separate automations for each product, you can have a single automation that can retrieve details for any product by simply providing the appropriate
product ID as the parameter value from different sources, such as UI components or other automations.

### Scenario: Handling optional parameters with fallback values

Let's consider a scenario where you have a "Task" entity with a required "Owner" column, but you want this field to be optional in the
automation and provide a fallback value if the owner is not selected.

1. Create an automation with a parameter named `Owner` that maps to the `Owner` field of the `Task` entity.
2. Since the `Owner` field is required in the entity, the `Owner` parameter will synchronize with the required setting.
3. To make the `Owner` parameter optional in the automation, toggle the `required` setting off for this parameter.
4. In your automation logic, you can use an expression like `{{params.Owner || currentUser.userId}}`. This expression checks if the `Owner` parameter is provided.
   If it's not provided, it will fallback to the current user's ID as the owner.
5. This way, if the user doesn't select an owner in a form or component, the automation will automatically assign the current user as the owner for the task.

By toggling the `required` setting for the `Owner` parameter and using a fallback expression, you can decouple it from the entity field requirement,
make it optional in the automation, and provide a default value when the parameter is not provided.

## Defining automation parameter types

By using parameter types to specify data types and set requirements, you can control the inputs for your automations.
This helps ensure your automations run reliably with the expected inputs.

### Synchronizing types from an entity

Dynamically synchronizing parameter types and requirements from entity field definitions
streamlines building automations that interact with entity data, ensuring that the parameter always
reflects the latest entity field type and requirements.

The following procedure details general steps for synchronizing parameter types from an entity:

1. Create an entity with typed fields (e.g. Boolean, Number, etc.) and mark fields as needed.
2. Create a new automation.
3. Add parameters to the automation, and when choosing the **Type**, choose the entity field you want to
   sync with. The data type and required setting will automatically synchronize from the mapped entity field
4. If needed, you can override the "required" setting by toggling it on/off for each parameter. This means the required status will not be kept in sync with the entity field, but otherwise, it will remain synchronized.

### Manually defining types

You can also define parameter types manually without synchronizing from an entity

By defining custom parameter types, you can create
automations that accept specific input types and handle optional or required parameters as needed,
without relying on entity field mappings.

1. Create an entity with typed fields (e.g. Boolean, Number, etc.) and mark fields as needed.
2. Create a new automation.
3. Add parameters to the automation, and when choosing the **Type**, choose desired type.

## Configuring dynamic values to be passed to automation parameters

Once you've defined parameters for an automation, you can pass values to them when invoking
the automation. You can pass parameter values in two ways:

1. **Component triggers**: If you're invoking the automation from a
   component trigger, such as a button click, you can use JavaScript expressions to pass values from the component context.
   For example, if you have a text input field named `emailInput`, you can pass its value to the email parameter with the
   following expression: `ui.emailInput.value`.
2. **Other automations**: If you're invoking the automation from
   another automation, you can use JavaScript expressions to pass values from the automation context.
   For example, you can pass the value of another parameter or the result of a previous action step.

## Type safety

By defining parameters with specific data types, such as String, Number, or Boolean, you
can ensure that the values passed into your automation are of the expected type.

###### Note

In App Studio, date(s) are ISO string dates, and those will be validated too.

This type safety helps prevent type mismatches, which can lead to errors or unexpected behavior in your automation logic.
For example, if you define a parameter as a `Number`, you can be confident that any value passed to that
parameter will be a number, and you won't have to perform additional type checks or conversions within your automation.

## Validation

You can add validation rules to your parameters,
ensuring that the values passed into your automation meet certain criteria.

While App Studio does not provide built-in validation settings for parameters,
you can implement custom validations by adding a JavaScript action to your automation that
throws an error if specific constraints are violated.

For entity fields, a subset of validation rules, such as minimum/maximum values, are supported.
However, those are not validated at the automation level, only at the data layer, when running Create/Update/Delete Record actions.

## Best practices for automation parameters

To ensure that your automation parameters are well-designed, maintainable, and easy to use, follow these best practices:

1. **Use descriptive parameter names**: Choose parameter names that clearly describe the purpose or context of the parameter.
2. **Provide parameter descriptions**: Take advantage of the **Description** field when defining parameters to explain their purpose, constraints,
   and expectations. These descriptions will be surfaced in the JSDoc comments when referencing the parameter, as well as in any user interfaces where users need to provide values for the
   parameters when invoking the automation.
3. **Use appropriate data types**: Carefully consider the data type of each parameter based on the expected input values,
   for example: String, Number, Boolean, Object.
4. **Validate parameter values**: Implement appropriate validation checks within your automation to ensure
   that parameter values meet specific requirements before proceeding with further actions.
5. **Use fallback or default values**: While App Studio does not currently support setting default values for parameters, you can
   implement fallback or default values when consuming the parameters in your automation logic. For example, you can use an expression like `{{ params.param1 || "default value" }}`
   to provide a default value if the `param1` parameter is not provided or has a false value.
6. **Maintain parameter consistency**: If you have multiple automations that require similar parameters, try to maintain consistency in parameter
   names and data types across those automations.
7. **Document parameter usage**: Maintain clear documentation for your automations, including descriptions of each parameter, its purpose, expected values,
   and any relevant examples or edge cases.
8. **Review and refactor frequently**: Periodically review your automations and their parameters, refactoring or consolidating
   parameters as needed to improve clarity, maintainability, and reusability.
9. **Limit the number of parameters**: While parameters provide flexibility, too many parameters can make an
   automation complex and difficult to use. Aim to strike a balance between flexibility and simplicity by limiting the number of parameters to only what is necessary.
10. **Consider parameter grouping**: If you find yourself defining multiple related parameters, consider grouping
    them into a single `Object` parameter.
11. **Separate concerns**: Avoid using a single parameter for multiple purposes or combining unrelated
    values into a single parameter. Each parameter should represent a distinct concern or piece of data.
12. **Use parameter aliases**: If you have parameters with long or complex names, consider using aliases or shorthand
    versions within the automation logic for better readability and maintainability.

By following these best practices, you can ensure that your automation parameters are well-designed, maintainable, and easy to use, ultimately
improving the overall quality and efficiency of your automations.
