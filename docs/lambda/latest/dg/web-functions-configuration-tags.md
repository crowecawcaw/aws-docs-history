

# Tagging Web Functions
<a name="web-functions-configuration-tags"></a>

Tags are key-value labels that you attach to a Web Function to organize your resources and control access. Tags apply to the Web Function resource.

To add tags when you create a Web Function, use the `tags` parameter of `CreateWebFunction`. To add, remove, or list tags later, use the `TagResource`, `UntagResource`, and `ListTags` operations.

You can use tags in the following ways:
+ **Organization and search** – Group and find Web Functions by attributes such as project, environment, or team. You can find a Web Function by its tags only in its home Region. For more information, see [Replica visibility](web-functions-endpoint-replication.md#web-functions-endpoint-replication-visibility).
+ **Attribute-based access control (ABAC)** – Write AWS Identity and Access Management (IAM) policies that allow or deny actions based on tags. Use `aws:ResourceTag/${TagKey}` for actions on a Web Function and its revisions and endpoints, which inherit the tags of the Web Function. On `CreateWebFunction`, you can also use `aws:RequestTag/${TagKey}` and `aws:TagKeys`. You can't tag revisions or endpoints directly. For more information, see [Lambda Web Function permissions](web-functions-permissions.md) and [Lambda Web Function endpoint access control](web-functions-endpoint-access-control.md).

Tags have the following requirements:
+ Tag keys are 1–128 characters.
+ Tag values are 0–256 characters.
+ Keys and values can contain letters, numbers, spaces, and the characters `_ . : / = + - @`.