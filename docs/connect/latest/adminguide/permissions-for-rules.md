

# Security profile permissions for conversational analytics rules

To view, edit, or add rules for automatic categorization, you must be assigned to a security profile that has **Analytics and Optimization: Rules** permissions.

To create, edit, or delete rules that use generative AI (using the **Natural language - semantic match** condition), your security profile must also have the **Analytics and Optimization: Rules - Generative AI** permission. To view these rules, the **Rules - View** permission is enough.

For more information, see [Assign permissions to use conversational analytics in Connect Customer](permissions-for-contact-lens.md).

## Permissions for resources in rules
<a name="permissions-for-rules-resources"></a>

To add a resource to a rule condition or action, you need permission to view that resource. The following table lists the resources that you can use in rules, and the permission that you need for each.


| Resource | Permission | Where you use it in rules | 
| --- | --- | --- | 
| Queues | **Routing: Queues - View** | Queue conditions, and queue filters in metric conditions | 
| Agents | **Users and permissions: Users - View** | Agent conditions, agent filters in metric conditions, and notification recipients and exclusions | 
| Agent hierarchies | **Users and permissions: Agent hierarchy - View** | Agent hierarchy conditions, and agent hierarchy filters in metric conditions | 
| Routing profiles | **Routing: Routing profiles - View** | Routing profile conditions, and routing profile filters in metric conditions | 
| Flows | **Channels and flows: Flows - View** | Flow filters in conditions, and the flow in a **Create Task** action | 
| Flow modules | **Channels and flows: Flow modules - View** | Flow module filters in metric conditions | 
| AI agents | **AI agents - View** | AI agent conditions, and AI agent filters in metric conditions | 
| Evaluation forms | **Analytics and Optimization: Evaluation forms - manage form definitions - View** | Evaluation form conditions, and the form in a **Submit automated evaluation** action | 
| Information extraction definitions | **Analytics and Optimization: Information extraction - definitions - View** | The definitions in an information extraction action | 

Your security profile might use tag-based or hierarchy-based access control on a resource. If so, you can add only the resources that you have access to. For more information, see [Granular access controls on rules](rules-tag-based-access-control.md).