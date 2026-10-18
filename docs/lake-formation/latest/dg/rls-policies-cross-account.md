

# Cross-account RLS policies
<a name="rls-policies-cross-account"></a>

When a table is shared across AWS accounts, row-level security (RLS) policies can be attached by the producer account, the recipient (consumer) account, or both. This section describes how RLS filtering behaves in each cross-account scenario. For general cross-account sharing setup, see [Cross-account data sharing in Lake Formation](cross-account-permissions.md).

**Overview**  
Cross-account RLS builds on Lake Formation cross-account data sharing. The producer account owns the table and its RLS policies; the consumer account receives access to the shared table and can manage permissions and its own RLS attachments for its principals. An RLS attachment always scopes down a principal's `SELECT` permission and never grants access on its own.

**Producer account attaches RLS for the consumer account**  
The producer account can attach an RLS policy that applies to principals in the consumer account. A consumer-account administrator can then grant those principals broad `SELECT` access on the shared table without being aware that the producer account has already attached an RLS policy to them.

In this scenario, the RLS policy attached by the producer account remains in effect. Consumer principals see only the rows the RLS filter allows, even though the consumer-account administrator granted full `SELECT` on the table. The consumer-side grant provides the `SELECT` permission that RLS then scopes down; it does not override the producer account's attachment.

**Important**  
A consumer-account administrator who grants full `SELECT` may not realize that rows are still being filtered by an RLS policy attached by the producer account. If a consumer principal appears to be missing rows, check for RLS attachments made by the producer account, not only for attachments in the consumer account.

**RLS attached in both accounts**  
Both the producer account and the consumer account can attach RLS policies that apply to the same consumer principal on the shared table. When both attachments are in effect, the principal sees the intersection of the two filters – only the rows that satisfy both the producer account's RLS filter and the consumer account's RLS filter.

**Note**  
Within a single account, multiple RLS policies attached to a principal combine additively (union), so the principal sees the union of all matching rows. Across accounts, the producer account's filter and the consumer account's filter combine with intersection (AND), so the principal sees only the rows that satisfy both. For details on how additive (union) behavior works within a single account, see [How RLS policies work in detail](rls-policies-about.md).

**Direct cross-account grant with a direct cross-account RLS attachment**  
The producer account can make a direct cross-account `SELECT` grant to a specific consumer-account principal and, in the same account, make a direct cross-account RLS attachment for that principal on the shared table.

In this scenario, the direct grant provides the consumer principal's `SELECT` permission and the direct RLS attachment scopes it down. The consumer principal sees only the rows matching the producer account's RLS filter, without the consumer account making any attachment of its own.

**How producer and consumer filters combine**  
When RLS policies are attached in both the producer account and the consumer account for the same consumer principal, Lake Formation combines them as follows:
+ **Between accounts (producer and consumer): AND.** The principal sees only rows that satisfy both the producer account's filter and the consumer account's filter (the intersection).
+ **Within a single account: OR.** When one account attaches multiple RLS policies to the same principal on the table, that account's filters combine additively (the union of their matching rows).
+ **A direct producer-to-principal attachment is authoritative.** When the producer account attaches an RLS policy directly to a specific consumer principal (rather than for the consumer account as a whole), the producer's filter alone determines the rows that principal can see. In this case, Lake Formation does not also apply a consumer-account attachment for that principal on the shared table.

**Example: how cross-account filters change query results**  
The following examples use a shared `employees` table owned by the producer account. The producer account grants `SELECT` on the table to the consumer *account* (not directly to a principal), and the consumer-account administrator then grants `SELECT` on the full table to the `DataAnalyst` role. The following table shows the sample data in the `employees` table.


| Row | region | dept | 
| --- | --- | --- | 
| 1 | us | sales | 
| 2 | us | hr | 
| 3 | eu | sales | 
| 4 | eu | hr | 
| 5 | us | finance | 
| 6 | eu | finance | 
| 7 | asia | sales | 
| 8 | asia | hr | 

The following table shows how different combinations of producer-account and consumer-account attachments change the effective filter and the rows that the `DataAnalyst` role's query returns.


| Producer account attaches | Consumer account attaches (for the DataAnalyst role) | Effective filter | Rows the DataAnalyst role sees | 
| --- | --- | --- | --- | 
| For the consumer account, two policies: region = 'us', region = 'eu' (combined with OR) | Two policies: dept = 'sales', dept = 'hr' (combined with OR) | (region = 'us' OR region = 'eu') AND (dept = 'sales' OR dept = 'hr') | 1, 2, 3, 4 | 
| For the consumer account, one policy: region = 'us' | One policy: dept = 'sales' | region = 'us' AND dept = 'sales' | 1 | 
| Nothing (the cross-account SELECT grant is on the consumer account, not on the principal directly) | One policy: dept = 'finance' | dept = 'finance' | 5, 6 | 

Within each account, multiple policies attached to the principal combine with OR (the union of their rows). Across the producer and consumer accounts, the two filters combine with AND (the intersection). For how additive (union) behavior works within a single account, see [How RLS policies work in detail](rls-policies-about.md).