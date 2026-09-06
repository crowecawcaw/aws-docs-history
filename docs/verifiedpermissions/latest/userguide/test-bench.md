

# Using the Amazon Verified Permissions test bench
<a name="test-bench"></a>

Use the Verified Permissions test bench to test and troubleshoot Verified Permissions policies by running [authorization requests](terminology.md#term-authorization-request) against them. The test bench uses the parameters that you specify to determine whether the Cedar policies in your policy store would authorize the request. You can toggle between **Visual mode** and **JSON mode** while testing authorization requests. For more information about how Cedar policies are structured and evaluated, see [Basic policy construction in Cedar](https://docs.cedarpolicy.com/policies/syntax-policy.html) in the Cedar policy language Reference Guide.

**Note**  
When you make an authorization request using Verified Permissions, you can provide the list of principals and resources as part of the request in the **Additional entities** section. However, you can't include the details about the actions. They must be specified in the schema or inferred from the request. You can't put an action in the **Additional entities** section.

For a visual overview and demonstration of the test bench, see [Amazon Verified Permissions - Policy Creation and Testing (Primer Series \#3)](https://www.youtube.com/watch?v=Gi3joEySMPQ) on the AWS YouTube channel.

------
#### [ Visual mode ]

**Note**  
You must have a schema defined in your policy store to use the **Visual mode** of the test bench.

**To test policies in Visual mode**

1. Open the [Verified Permissions console](https://console.aws.amazon.com/verifiedpermissions/). Choose your policy store.

1. In the navigation pane on the left, choose **Test bench**.

1. Choose **Visual mode**.

1. In the **Principal** section, choose the **Principal taking action** from the principal types in your schema. Type an identifier for the principal in the text box.

1. (Optional) Choose **Add a parent** to add parent entities for the specified principal. To remove a parent that has been added to the principal, choose **Remove** next to the name of the parent.

1. Specify the **Attribute value** for each attribute of the specified principal. The test bench uses the specified attribute values in the simulated authorization request.

1. In the **Resource** section, choose the **Resource that principal is acting on**. Type an identifier for the resource in the text box.

1. (Optional) Choose **Add a parent** to add parent entities for the specified resource. To remove a parent that has been added to the resource, choose **Remove** next to the name of the parent.

1. Specify the **Attribute value** for each attribute of the specified resource. The test bench uses the specified attribute values in the simulated authorization request.

1. In the **Action** section, choose the **Action that principal is taking** from the list of valid actions for the specified principal and resource.

1. Specify the **Attribute value** for each attribute of the specified action. The test bench uses the specified attribute values in the simulated authorization request.

1. (Optional) In the **Additional entities** section, choose **Add entity** to add entities to be evaluated for the authorization decision.

1. Choose the **Entity Identifier** from the dropdown list and type the entity identifier.

1. (Optional) Choose **Add a parent** to add parent entities for the specified entity. To remove a parent that has been added to the entity, choose **Remove** next to the name of the parent.

1. Specify the **Attribute value** for each attribute of the specified entity. The test bench uses the specified attribute values in the simulated authorization request.

1. Choose **Confirm** to add the entity to the test bench.

1. Choose **Run authorization request** to simulate the authorization request for the Cedar policies in your policy store. The test bench displays the decision to allow or deny the request along with information about the policies satisfied or the errors encountered during evaluation.

------
#### [ JSON mode ]

**To test policies in JSON mode**

1. Open the [Verified Permissions console](https://console.aws.amazon.com/verifiedpermissions/). Choose your policy store.

1. In the navigation pane on the left, choose **Test bench**.

1. Choose **JSON mode**.

1. In the **Request details** section, if you have a schema defined, choose the **Principal taking action** from the principal types in your schema. Type an identifier for the principal in the text box.

   If you do not have a schema defined, type the principal in the **Principal taking action** text box.

1. If you have a schema defined, choose the **Resource** from the resource types in your schema. Type an identifier for the resource in the text box.

   If you do not have a schema defined, type the resource in the **Resource** text box.

1. If you have a schema defined, choose the **Action** from the list of valid actions for the specified principal and resource.

   If you do not have a schema defined, type the action in the **Action** text box.

1. Enter the context of the request to simulate in the **Context** field. The request context is additional information that can be used for authorization decisions.

1. In the **Entities** field, enter the hierarchy of the entities and their attributes to be evaluated for the authorization decision.

1. Choose **Run authorization request** to simulate the authorization request for the Cedar policies in your policy store. The test bench displays the decision to allow or deny the request along with information about the policies satisfied or the errors encountered during evaluation.

------