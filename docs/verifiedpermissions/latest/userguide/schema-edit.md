# Editing policy store schemas

When you select **Schema** in the Amazon Verified Permissions console, the **Entity
types** and **Actions** that make up your schema are
displayed. You can view edit your schema in either **Visual mode** or
**JSON mode**. Visual mode lets you update the schema by adding new
types and actions using various wizards. Using JSON mode, you can start updating the JSON code of the schema
directly in the JSON editor.

Visual ModeThe visual schema editor begins with a series of diagrams that illustrate the
relationships between the entities in your schema. Choose **Expand** to
maximize your view of the diagrams. There are two diagrams available:

- **Actions diagram** – The **Actions diagram** view lists the types of
  **Principals** you have configured in your policy store, the
  **Actions** they are eligible to perform, and the
  **Resources** that they are eligible to perform actions on. The
  lines between entities indicate your ability to create a policy that allows a principal
  to take an action on a resource. If your actions diagram doesn't indicate a relationship
  between two entities, you must create that relationship between them before you can
  allow or deny it in policies. Select an entity to see a properties overview and drill
  down to view full details. Choose **Filter by this [action | resource type |
  principal type]** to see an entity in a view with only its own
  connections.
- **Entity types diagram** – The **Entity types diagram** focuses on the relationships between
  principals and resources. When you want to understand the complex nested parent
  relationships in your schema, review this diagram. Hover over an entity to drill down
  into the parent relationships that it has.

Under the diagrams are list views of the **Entity types** and
**Actions** in your schema. The list view is useful when you want to
immediately view the details of a specific action or entity type. Select any entity to view
details.

###### To edit a Verified Permissions schema in Visual mode

1. Open the [Verified Permissions console](https://console.aws.amazon.com/verifiedpermissions/ "https://console.aws.amazon.com/verifiedpermissions/"). Choose your policy store.
2. In the navigation pane on the left, choose **Schema**.
3. Choose **Visual mode**. Review the entity-relationship diagrams
   and plan the changes that you want to make to your schema. You can optionally
   **Filter by** one entity to examine its individual connections
   to other entities.
4. Choose **Edit schema**.
5. In the **Details** section, type a **Namespace**
   for your schema.
6. In the **Entity types** section, choose **Add new entity
   type**.
7. Type the name of the entity.
8. (Optional) Choose **Add a parent** to add parent entities that
   the new entity is a member of. To remove a parent that has been added to the entity,
   choose **Remove** next to the name of the parent.
9. Choose **Add an attribute** to add attributes to the entity. Type
   the **Attribute name** and choose the **Attribute
   type** for each attribute of the entity. Verified Permissions uses the specified
   attribute values when verifying policies against the schema. Select whether each
   attribute is **Required**. To remove an attribute that has been
   added to the entity, choose **Remove** next to the
   attribute.
10. Choose **Add entity type** to add the entity to the
    schema.
11. In the **Actions** section, choose **Add new
    action**.
12. Type the name of the action.
13. (Optional) Choose **Add a resource** to add resource types for
    which the action applies to. To remove a resource type that has been added to the
    action, choose **Remove** next to the name of the resource
    type.
14. (Optional) Choose **Add a principal** to add a principal type
    that the action applies to. To remove a principal type that has been added to the
    action, choose **Remove** next to the name of the principal
    type.
15. Choose **Add an attribute** to add attributes that can be added
    to the context of an action in your authorization requests. Enter the
    **Attribute name** and choose the **Attribute
    type** for each attribute. Verified Permissions uses the specified attribute values
    when verifying policies against the schema. Select whether each attribute is
    **Required**. To remove an attribute that has been added to the
    action, choose **Remove** next to the attribute.
16. Choose **Add action**.
17. After all the entity types and actions have been added to the schema, choose
    **Save changes**.

JSON modeWhile making updates, you'll notice the JSON editor validates
your code against JSON syntax and will identify errors and warnings as you edit, making it
easier for you to find issues quickly. In addition, you don't need to worry about the
formatting of the JSON, simply choose **Format JSON** once you've made your
updates and the format will be updated to match expected JSON formatting.

###### To edit a Verified Permissions schema in JSON mode

1. Open the [Verified Permissions console](https://console.aws.amazon.com/verifiedpermissions/ "https://console.aws.amazon.com/verifiedpermissions/"). Choose your policy store.
2. In the navigation pane on the left, choose **Schema**.
3. Choose **JSON mode** and then choose **Edit
   schema**.
4. Enter the content of your JSON schema in the **Contents** field.
   You can't save updates to your schema until you resolve all syntax errors. You can
   choose **Format JSON** to format the JSON syntax of your schema
   with the recommended spacing and indentation.
5. Choose **Save changes**.
