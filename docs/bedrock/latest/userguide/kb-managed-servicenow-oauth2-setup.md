

# Set up OAuth 2.0 Client Credentials authentication for ServiceNow
<a name="kb-managed-servicenow-oauth2-setup"></a>

Use the ServiceNow Table API with OAuth 2.0 Client Credentials (2LO) for authentication. Complete all the following steps in your ServiceNow instance before you configure the data source in Amazon Bedrock.

## Step 1: Enable client credentials grant type
<a name="kb-managed-servicenow-oauth2-step1"></a>

1. In ServiceNow, navigate to `sys_properties.list` using the filter navigator.

1. Create a new system property with the following values:
   + **Name** – `glide.oauth.inbound.client.credential.grant_type.enabled`
   + **Type** – `true | false`
   + **Value** – `true`

## Step 2: Create a dedicated service account
<a name="kb-managed-servicenow-oauth2-step2"></a>

1. Navigate to **User Administration** > **Users**.

1. Choose **New** and complete the form:
   + **User ID** – A descriptive name (for example, `svc.amazon.quick.kb`).
   + **Web service access only** – Checked. This prevents interactive login.
   + **Password** – Set a strong password. The connector uses OAuth, but a password is required for account creation.

1. Choose **Submit**.

## Step 3: Assign service account roles
<a name="kb-managed-servicenow-oauth2-step3"></a>

1. Open the service account (**User Administration** > **Users** > your service account).

1. Under the **Roles** tab, choose **Edit** and add the following roles:
   + `knowledge_admin` – Full read access to all knowledge base articles. Bypasses per-KB user criteria restrictions.
   + `catalog_admin` – Full read access to all service catalog items. Bypasses per-catalog restrictions.

1. Choose **Save**.

**Note**  
After saving, you see approximately 14 total roles. ServiceNow auto-inherits contained roles from the `_admin` parent roles. You only manually assign the two roles listed in step 2 (`knowledge_admin` and `catalog_admin`). Do not assign the `admin`, `itil`, or `snc_read_only` roles.

## Step 4: Register the OAuth application
<a name="kb-managed-servicenow-oauth2-step4"></a>

1. Navigate to **System OAuth** > **Application Registry**.

1. Choose **New** > **Create an OAuth API endpoint for external clients**.

1. Complete the form:
   + **Name** – A descriptive name (for example, `Amazon-Quick-KB-Client`).
   + **Redirect URL** – Leave blank. Not required for client credentials flow.

1. Choose **Submit**.

1. Immediately copy the **Client ID** and **Client Secret**. The Client Secret is only shown once.

**Important**  
You must use the interceptor page to create the application. Do not create the record by directly inserting into the `oauth_entity` table.

## Step 5: Configure the OAuth application
<a name="kb-managed-servicenow-oauth2-step5"></a>

1. Re-open the application record from the Application Registry list.

1. If the **OAuth Application User** field is not visible, add it using **Configure** > **Form Builder**.

1. Set the following fields:
   + **OAuth Application User** – Your service account (for example, `svc.amazon.quick.kb`).
   + **Scope Restriction** – `Broadly scoped`.
   + **Client Type** – `integration_as_a_service`.

1. Choose **Update**.

## Step 6: Configure API access policies
<a name="kb-managed-servicenow-oauth2-step6"></a>

Without API access policies, tokens authenticate but the Table API returns HTTP 401. Complete both sub-steps below.

**Create the Inbound Authentication Profile**

1. Navigate to **System Web Services** > **API Access Policies** > **Inbound Authentication Profile**.

1. Choose **New** and set:
   + **Name** – For example, `Amazon-Quick-KB-Client-Profile`.
   + **Type** – `OAuth`.
   + **OAuth Entity** – Select your OAuth application.

1. Choose **Submit**.

1. Re-open the profile. In the **Authentication Policies** related list, choose **Edit** and add **Allow Access Policy**. Choose **Save**.

**Create the REST API Access Policy**

1. Navigate to **System Web Services** > **API Access Policies** > **REST API Access Policies**.

1. Choose **New** and set:
   + **Name** – For example, `Table API Oauth access policy`.
   + **REST API** – `Table API`.
   + **REST API Path** – `now/table`.
   + **Apply to all methods** – Checked.
   + **Apply to all resources** – Checked.
   + **Apply to all tables** – Checked.
   + **Apply to all versions** – Checked.

1. Choose **Submit**.

1. Re-open the policy. In the **Inbound authentication profiles** related list, choose **Edit** and add your Inbound Authentication Profile. Choose **Save**.

## Step 7: Verify the OAuth flow
<a name="kb-managed-servicenow-oauth2-step7"></a>

Before you configure the data source, verify that the OAuth flow works end-to-end.

**Request a token:**

```
curl -s -X POST "https://{{INSTANCE}}.service-now.com/oauth_token.do" \
  -d "grant_type=client_credentials" \
  -d "client_id={{CLIENT_ID}}" \
  -d "client_secret={{CLIENT_SECRET}}"
```

**Verify Table API access:**

```
curl -s "https://{{INSTANCE}}.service-now.com/api/now/table/kb_knowledge?sysparm_limit=1" \
  -H "Authorization: Bearer {{ACCESS_TOKEN}}"
```

The following table describes each verification result and the action to take.


**Verification results**  

| Result | Meaning | Action | 
| --- | --- | --- | 
| HTTP 200 with data | Working correctly | Proceed to create the Secrets Manager secret. | 
| HTTP 200 with empty array | Missing knowledge\_admin role | Assign the knowledge\_admin role to the service account. | 
| HTTP 401 | API access policy not configured | Verify both the Inbound Authentication Profile and the REST API Access Policy configuration. | 

## Step 8: Create the Secrets Manager secret
<a name="kb-managed-servicenow-oauth2-step8"></a>

Store the credentials in an AWS Secrets Manager secret in the same AWS Region as your knowledge base with the following key-value pairs:

```
{
    "clientId": "{{your-client-id}}",
    "clientSecret": "{{your-client-secret}}",
    "instanceUrl": "https://{{YOUR_INSTANCE}}.service-now.com",
    "aclCheckPath": "/api/{{NAMESPACE}}/{{RESOURCE}}"
}
```


**Secret fields**  

| Field | Description | 
| --- | --- | 
| clientId | The App Client ID from step 4. | 
| clientSecret | The App Client Secret revealed at creation time in step 4. | 
| instanceUrl | Full ServiceNow instance URL (include https://, no trailing slash). | 
| aclCheckPath | (Optional) The path to the real-time ACL verifier Scripted REST API endpoint (for example, /api/{{namespace}}/{{resource}}). Add this field only when you enable document-level access control and set up the endpoint to resolve advanced (scripted) user criteria. See [Set up the real-time ACL verifier endpoint for advanced criteria](#kb-managed-servicenow-oauth2-acl-verifier). | 

**Important**  
The `instanceUrl` must not have a trailing slash.

Create the secret with the AWS Command Line Interface:

```
aws secretsmanager create-secret \
  --name {{bedrock-servicenow-creds}} \
  --secret-string file://secret.json
```

Record the secret ARN from the response. You use it as the data source `secretArn`.

## Additional setup for document-level access control (ACLs)
<a name="kb-managed-servicenow-oauth2-acl"></a>

Complete the following steps only if you plan to enable document-level access control (ACLs) on the data source. They build on the setup above — the same service account, OAuth application, and secret are still required and unchanged. ACL crawling adds ServiceNow-side table-access permissions and knowledge base configuration; no AWS or IAM policy changes are required. For how ACL enforcement works and how to enable it on the data source, see [Document-level access controls](kb-managed-ds-servicenow-acl.md).

### Add ACL-read roles to the service account
<a name="kb-managed-servicenow-oauth2-acl-roles"></a>

To resolve user criteria into concrete users, the ACL crawl reads membership and ACL-definition tables. The `knowledge_admin` and `catalog_admin` roles don't grant access to these tables. Without these reads, the crawl fails with HTTP 403. Worse, it can resolve criteria to zero members and silently hide documents from everyone (fail-closed). Grant the service account read access to the following tables.


**Tables the ACL crawl must read**  

| Table | Purpose | Covered by base setup roles? | 
| --- | --- | --- | 
| sys\_user\_grmember | Resolve group criteria to member users. | No | 
| sys\_user\_has\_role | Resolve role criteria to users holding the role. | No | 
| sys\_security\_acl | Inspect ACL rule definitions. | No | 
| user\_criteria, kb\_uc\_\*\_mtom | The user criteria themselves. | Yes (via user\_criteria\_read, inherited) | 
| sc\_cat\_item\_user\_\* (four tables) | Catalog direct and criteria allow and deny lists. | Yes (via catalog\_admin) | 

There are two ways to grant the missing reads:
+ **Option A (recommended for production) — one scoped custom read-only role.** Create a custom role (for example, `x_amazonbedrockmkb.acl_crawler`) with read access control on exactly the tables above, and assign it to the service account. This avoids broad admin roles and is the least-privilege posture.
+ **Option B (fast for proof of concept or non-production) — three out-of-box read roles.** Assign `group_viewer` (reads `sys_user_grmember` and `sys_group_has_role`), `role_delegator` (reads `sys_user_has_role`), and `access_control_read_admin` (reads `sys_security_acl` and `sys_user_role`).

**Important**  
No single narrow out-of-box role covers all of these tables. The broad out-of-box roles that would (`user_admin`, `itil`) also grant write access on user records and aren't appropriate for a crawl account. Use Option A, or the three read-only roles in Option B.

To assign roles, go to **User Administration** > **Users**, open the service account, and on the **Roles** tab choose **Edit**.

**Grant the `impersonator` role to the OAuth run-as user (required for advanced criteria).** ServiceNow's advanced (scripted) user criteria are evaluated under impersonation. Without the `impersonator` role, every advanced-criteria document is denied because the guard fails closed.

1. In ServiceNow, go to **User Administration** > **Users**, and open the OAuth 2.0 run-as user.

1. In the **Roles** related list, choose **Edit**, add `impersonator`, and save.

1. Confirm the assignment appears in `sys_user_has_role` for that user.

### Configure restricted knowledge bases
<a name="kb-managed-servicenow-oauth2-acl-kb-config"></a>

Two ServiceNow settings can make an ACL crawl fail with no obvious error. Check both before you crawl.

**Grant the crawl account read access to restricted knowledge bases.** Many hardened instances set `glide.knowman.block_access_with_no_user_criteria` to `true`. With this setting on, a knowledge base blocks any user who has no matching `can_read` criterion. This includes the connector's service account. A knowledge base restricted by user criteria that don't include the service account crawls zero documents. The ingestion job then fails with a generic internal error, and no permission error is surfaced. To fix this without making the knowledge base public, grant the service account read access through a dedicated `can_read` user criterion:

1. Go to **Knowledge** > **User Criteria** > **New**. Name it (for example, `Amazon Bedrock Connector Read`), add the service account to its **User** list, and leave everything else empty.

1. On each restricted knowledge base, add that criterion to **Can Read**.

Because the criterion contains only the service account, it doesn't change any end user's access — it only lets the connector read the articles it must index.

**Remove the out-of-box "Any User" criterion from restricted knowledge bases.** New knowledge bases receive an out-of-box "Any User" `can_read` criterion that makes the knowledge base readable by everyone. On an access-controlled knowledge base, this default silently defeats your other criteria — every article that relies on knowledge-base-level fallback becomes public. On each access-controlled knowledge base, remove the "Any User" entry from **Can Read**, keeping only the criteria that reflect real access plus the connector-read criterion from the previous step.

### Verify the service account can read the ACL tables
<a name="kb-managed-servicenow-oauth2-acl-verify"></a>

Before you enable ACLs on the data source, confirm that the service account (using its OAuth token, exactly as the connector authenticates) can read the membership and ACL tables.

```
for T in sys_user_grmember sys_user_has_role sys_security_acl; do
  code=$(curl -s -o /dev/null -w "%{http_code}" \
    "https://{{INSTANCE}}.service-now.com/api/now/table/$T?sysparm_limit=1" \
    -H "Authorization: Bearer {{ACCESS_TOKEN}}" -H "Accept: application/json")
  echo "$T: HTTP $code"
done
```

If every table returns HTTP 200, the ACL tables are readable and you can proceed. If any table returns HTTP 403, the service account is missing an ACL-read role — complete the role assignment described earlier on this page.

### Set up the real-time ACL verifier endpoint for advanced criteria
<a name="kb-managed-servicenow-oauth2-acl-verifier"></a>

ServiceNow's advanced user criteria (`advanced = true`) hold a server-side script. Because of this, the connector crawl can't resolve their membership automatically. Without a way to evaluate them, the affected articles would be invisible to everyone. To resolve advanced criteria on demand, install a Scripted REST API on your ServiceNow instance. At retrieve time, the connector sends the requesting user and a batch of document sys IDs to this endpoint and receives an allow or deny verdict for each document. This setup is required only if your content uses advanced (scripted) user criteria.

The connector reaches the endpoint using the same OAuth 2.0 credentials stored in the connector's AWS Secrets Manager secret, and finds the endpoint path from an `aclCheckPath` field on that secret.

**Prerequisites.** In addition to the base setup on this page, make sure that:
+ OAuth 2.0 Client Credentials are configured for the connector.
+ The OAuth 2.0 client user can POST to the new resource (the default Scripted REST resource access control denies `snc_external`) and has read access to `sys_user`, `sys_user_grmember`, `sys_user_has_role`, `sys_user_role_contains`, `sys_security_acl`, `kb_knowledge`, `user_criteria`, `kb_uc_can_read_mtom`, and `kb_uc_cannot_read_mtom`.
+ **Impersonator role.** The OAuth 2.0 run-as user must hold the `impersonator` role. Advanced (scripted) criteria are evaluated under impersonation. If the run-as user can't impersonate, `GlideImpersonate.impersonate()` silently no-ops. The script guards against this by re-checking `gs.getUserID()` and failing closed. As a result, a missing impersonator role causes every advanced-criteria document to be denied. Grant the role before you rely on the endpoint. See [Add ACL-read roles to the service account](#kb-managed-servicenow-oauth2-acl-roles).
+ **Scope: knowledge base articles only (as written).** The script queries `kb_knowledge` and the knowledge base user-criteria tables only. If the verifier must also cover service catalog items, extend it to query the catalog tables (`sc_cat_item` and the `sc_cat_item_user_*` many-to-many tables) and grant read on them. Otherwise, the endpoint is knowledge-base-only, and catalog documents are out of scope.

**Placeholders.** This section uses the following placeholders.


**Placeholders**  

| Placeholder | Meaning | 
| --- | --- | 
| {{INSTANCE}} | ServiceNow instance subdomain, as in https://{{INSTANCE}}.service-now.com. | 
| {{NAMESPACE}} | The API namespace segment the Scripted REST API resolves to. | 
| {{RESOURCE}} | The resource name (for example, check\_access). | 
| {{ACL\_CHECK\_PATH}} | The final path: /api/{{NAMESPACE}}/{{RESOURCE}}. | 
| {{SECRET\_ARN}} | The AWS Secrets Manager secret ARN holding the OAuth 2.0 client credentials. | 
| {{REGION}} | The AWS Region of the secret. | 

To set up the endpoint, complete the following steps.

1. **Create the Scripted REST API.**

   1. Navigate to **System Web Services** > **Scripted REST APIs** > **New**.

   1. Set a **Name** and **API ID**. The API ID plus the instance's application namespace determine the base path `/api/{{NAMESPACE}}/...`. Record the resolved base path — it must match the `aclCheckPath` you store later.

   1. In the **Resources** related list, choose **New**, and set the **HTTP method** to `POST`, the **Relative path** to `/{{RESOURCE}}`, and paste the script from the next step.

   1. On the resource **Security** tab, keep **Requires authentication** enabled, and make sure the OAuth 2.0 client user has an access control or role that permits POST (the default resource access control denies `snc_external`), holds the `impersonator` role, and has read on all tables listed in the prerequisites.

1. **Add the resource script.** Paste the following script into the resource.

   ```
   (function process(request, response) {
       // Contract:
       //   IN : { "user_email": "<email>", "document_ids": ["<sys_id>", ...] }   (<= 50 ids)
       //   OUT: 200 { "result": { "<sys_id>": true|false, ... } }   strict booleans
       //        404 { "error": "User not found or inactive" }        -> connector denies (USER_NOT_FOUND)
       //   A sys_id omitted from the map is treated as NOT granted (fail-closed).
   
       var body = request.body && request.body.data ? request.body.data : {};
       var userEmail = body.user_email;
       var documentIds = body.document_ids || [];
   
       if (!userEmail || !documentIds.length) {
           response.setStatus(200);
           response.setBody({ result: {} });
           return;
       }
   
       // Contract enforces up to 50 ids per call; reject oversized batches so the
       // connector's batching contract is validated at the boundary.
       if (documentIds.length > 50) {
           response.setStatus(400);
           response.setBody({ error: 'document_ids exceeds batch limit of 50' });
           return;
       }
   
       // Validate sys_id shape (32 hex chars) up front; a malformed id can never
       // match a record, and validating here keeps a bad input from silently
       // producing an omitted (deny) verdict that looks like a real decision.
       var SYS_ID = /^[0-9a-f]{32}$/;
       for (var v = 0; v < documentIds.length; v++) {
           if (!SYS_ID.test(String(documentIds[v]))) {
               response.setStatus(400);
               response.setBody({ error: 'Invalid sys_id in document_ids: ' + documentIds[v] });
               return;
           }
       }
   
       // Resolve the caller to a sys_user.
       var userGr = new GlideRecord('sys_user');
       userGr.addQuery('email', userEmail);
       userGr.addQuery('active', true);
       userGr.setLimit(1);
       userGr.query();
       if (!userGr.next()) {
           response.setStatus(404);
           response.setBody({ error: 'User not found or inactive' });
           return;
       }
       var userSysId = userGr.getUniqueValue();
   
       // Direct group membership only (sys_user_grmember). ServiceNow user_criteria
       // does NOT walk nested groups, so this is intentionally not recursive.
       var userGroups = {};
       var grm = new GlideRecord('sys_user_grmember');
       grm.addQuery('user', userSysId);
       grm.query();
       while (grm.next()) userGroups[grm.getValue('group')] = true;
   
       // Direct roles from sys_user_has_role, then transitively expanded through
       // sys_user_role_contains so a parent role implies the roles it contains.
       // ServiceNow resolves role containment when evaluating criteria, so a user
       // holding a parent role must be treated as holding the contained roles too.
       var userRoles = {};
       var directRoles = [];
       var uhr = new GlideRecord('sys_user_has_role');
       uhr.addQuery('user', userSysId);
       uhr.query();
       while (uhr.next()) {
           var r = uhr.getValue('role');
           userRoles[r] = true;
           directRoles.push(r);
       }
       expandContainedRoles(directRoles, userRoles);
   
       var result = {};
       for (var i = 0; i < documentIds.length; i++) {
           var docId = documentIds[i];
           result[docId] = evaluateDocument(docId, userSysId, userGroups, userRoles);
       }
   
       response.setStatus(200);
       response.setBody({ result: result });   // Scripted REST serializer wraps under "result"
   
       // ------------------------------------------------------------
       function evaluateDocument(articleSysId, uSysId, uGroups, uRoles) {
           var art = new GlideRecord('kb_knowledge');
           if (!art.get(articleSysId)) return false;               // unknown doc -> deny
           if (art.getValue('workflow_state') !== 'published') return false;
   
           var canRead = art.getValue('can_read_user_criteria');
           var cannotRead = art.getValue('cannot_read_user_criteria');
   
           var allowCriteria = [];
           var denyCriteria = [];
   
           if (canRead || cannotRead) {
               // ARTICLE-LEVEL: criteria live directly on the article.
               allowCriteria = splitIds(canRead);
               denyCriteria  = splitIds(cannotRead);
           } else {
               // KB-LEVEL FALLBACK: read parent KB's M2M criteria tables.
               var kbId = art.getValue('kb_knowledge_base');
               allowCriteria = mtomCriteria('kb_uc_can_read_mtom', kbId);
               denyCriteria  = mtomCriteria('kb_uc_cannot_read_mtom', kbId);
           }
   
           // DENY takes precedence: any satisfied deny criteria -> blocked.
           for (var d = 0; d < denyCriteria.length; d++) {
               if (satisfiesCriteria(denyCriteria[d], uSysId, uGroups, uRoles)) return false;
           }
   
           // No ALLOW criteria at all: nothing grants read -> deny (fail-closed).
           if (!allowCriteria.length) return false;
   
           // ALLOW: user must satisfy at least one allow criteria.
           for (var a = 0; a < allowCriteria.length; a++) {
               if (satisfiesCriteria(allowCriteria[a], uSysId, uGroups, uRoles)) return true;
           }
           return false;
       }
   
       function mtomCriteria(table, kbId) {
           var out = [];
           var gr = new GlideRecord(table);
           gr.addQuery('kb_knowledge_base', kbId);
           gr.query();
           while (gr.next()) out.push(gr.getValue('user_criteria'));
           return out;
       }
   
       // Transitively expand role containment: for every role the user holds,
       // add every role it contains (sys_user_role_contains), following the graph
       // to its full closure. Without this, a user granted a parent role would be
       // denied a criterion keyed on a contained role.
       function expandContainedRoles(seedRoles, roleSet) {
           var frontier = seedRoles.slice();
           while (frontier.length) {
               var current = frontier;
               frontier = [];
               var gr = new GlideRecord('sys_user_role_contains');
               gr.addQuery('role', 'IN', current.join(','));
               gr.query();
               while (gr.next()) {
                   var contained = gr.getValue('contains');
                   if (contained && !roleSet[contained]) {
                       roleSet[contained] = true;
                       frontier.push(contained);   // walk deeper for nested containment
                   }
               }
           }
       }
   
       // Split a comma- or newline-delimited criteria id list, trimming blanks.
       function splitIds(csv) {
           if (!csv) return [];
           var parts = csv.toString().split(/[,\n]/);
           var out = [];
           for (var i = 0; i < parts.length; i++) {
               var t = parts[i].trim();
               if (t) out.push(t);
           }
           return out;
       }
   
       // Evaluate one user_criteria record against the user.
       // Handles: allow-all (all fields empty), group, role, direct user, match_all AND/OR,
       //          and advanced (scripted) criteria via the criteria's own script.
       function satisfiesCriteria(criteriaId, uSysId, uGroups, uRoles) {
           var uc = new GlideRecord('user_criteria');
           if (!uc.get(criteriaId)) return false;
   
           if (uc.getValue('advanced') === 'true') {
               try {
                   return evaluateAdvancedCriteria(uc, uSysId);
               } catch (e) {
                   gs.error('[acl_verifier] advanced criteria eval failed for ' +
                       criteriaId + ': ' + e.message);
                   return false; // fail-closed
               }
           }
   
           var group = uc.getValue('group');
           var role  = uc.getValue('role');
           var user  = uc.getValue('user');
           var matchAll = uc.getValue('match_all') === 'true';
   
           // Allow-all: no group, role, or user, and not advanced -> public.
           if (!group && !role && !user) return true;
   
           var conditions = [];
           if (group) conditions.push(!!uGroups[group]);
           if (role)  conditions.push(!!uRoles[role]);
           if (user)  conditions.push(user === uSysId);
   
           if (!conditions.length) return false;
   
           if (matchAll) {                       // AND
               for (var c = 0; c < conditions.length; c++) if (!conditions[c]) return false;
               return true;
           }
           for (var o = 0; o < conditions.length; o++) if (conditions[o]) return true; // OR
           return false;
       }
   
       // Advanced/scripted user_criteria: evaluate the criteria's script for this user.
       function evaluateAdvancedCriteria(uc, uSysId) {
           var script = uc.getValue('script');
           if (!script) return false;
           var target = new GlideRecord('sys_user');
           if (!target.get(uSysId)) return false;
           // Advanced UC scripts set `answer` for the CURRENT user (gs.getUserID()).
           // Impersonate the target so the script sees the right user, then restore.
           var impersonator = new GlideImpersonate();
           var original = gs.getUserID();
           try {
               impersonator.impersonate(uSysId);
               // CRITICAL: verify impersonation actually took effect. If the run-as
               // integration user lacks the impersonator role, impersonate() silently
               // no-ops and the script would evaluate as the PRIVILEGED user, which can
               // return answer=true for everyone (false-ALLOW). Fail closed instead.
               if (gs.getUserID() !== uSysId) {
                   gs.error('[acl_verifier] impersonation did not take effect for ' +
                       uSysId + ' (missing impersonator role?) -- failing closed');
                   return false;
               }
               var answer = false;
               eval(script);   // criteria script body assigns to `answer`
               return answer === true;
           } finally {
               impersonator.impersonate(original);
           }
       }
   })(request, response);
   ```

   The endpoint applies the following access-decision logic:
   + Article-level criteria (`can_read_user_criteria` or `cannot_read_user_criteria` set on the article) are used directly.
   + Knowledge-base-level fallback: when both article fields are empty, the parent knowledge base's `kb_uc_can_read_mtom` (allow) and `kb_uc_cannot_read_mtom` (deny) criteria are used.
   + Deny precedence: if the user satisfies any deny criteria, access is denied.
   + Allow-all: a criterion with no group, role, or user and `advanced = false` is public.
   + `match_all`: `true` is AND across the populated conditions; `false` is OR. This must match the connector's crawl-time intersection semantics, because the verifier is the oracle for the retrieve-versus-crawl cross-check.
   + Groups are direct-membership only (`sys_user_grmember`), by design: ServiceNow user criteria don't walk nested groups, so a user in a child group is correctly denied a criterion keyed on the parent group.
   + Roles are expanded transitively through `sys_user_role_contains`, because ServiceNow resolves role containment: a user holding a parent role is treated as holding the roles it contains.
   + Advanced (scripted) criteria are evaluated by the criteria's own script under impersonation; the script re-verifies `gs.getUserID()` and fails closed if impersonation didn't take effect. Any failure fails closed (deny).

1. **Verify the endpoint over HTTP.** Obtain an OAuth 2.0 access token using the connector's `clientId` and `clientSecret` against `https://{{INSTANCE}}.service-now.com/oauth_token.do`, then call the endpoint with a real user email and one known published article sys ID.

   ```
   POST https://{{INSTANCE}}.service-now.com{{ACL_CHECK_PATH}}
   Authorization: Bearer {{access_token}}
   Content-Type: application/json
   
   { "user_email": "{{email}}", "document_ids": ["{{sys_id}}"] }
   ```

   Confirm a `200` response with `{ "result": { "{{sys_id}}": true|false } }`.

1. **Set `aclCheckPath` on the connector secret.** The connector reads the endpoint path from an `aclCheckPath` field on the OAuth 2.0 secret, alongside `clientId`, `clientSecret`, and `instanceUrl`. Add or update only that one key; leave the existing credential fields untouched.

   **Option A (AWS Management Console).** In the [AWS Secrets Manager console](https://console.aws.amazon.com/secretsmanager/home), open the connector's secret, choose **Retrieve secret value**, choose **Edit**, and add a key `aclCheckPath` with the value `{{ACL_CHECK_PATH}}` (for example, `/api/{{NAMESPACE}}/{{RESOURCE}}`). The existing `clientId`, `clientSecret`, and `instanceUrl` values stay as they are. The console performs an in-place update that preserves the other fields.

   **Option B (AWS Command Line Interface).** `put-secret-value` replaces the entire secret value, so include all fields in the new JSON.

   ```
   aws secretsmanager get-secret-value \
     --secret-id {{SECRET_ARN}} --region {{REGION}} \
     --query SecretString --output text
   
   aws secretsmanager put-secret-value \
     --secret-id {{SECRET_ARN}} --region {{REGION}} \
     --secret-string '{"clientId":"...","clientSecret":"...","instanceUrl":"https://{{INSTANCE}}.service-now.com","aclCheckPath":"{{ACL_CHECK_PATH}}"}'
   ```

1. **Validate end to end.** Sync the ServiceNow data source so ACL-enabled articles are ingested. Then run Retrieve as an authorized user (the restricted article is returned) and as an unauthorized user (the restricted article is not returned).

   **Expected result:** the restricted article is returned only for the authorized user's Retrieve call, and is omitted for the unauthorized user.

**Notes.**
+ **Release dependency.** The advanced-criteria evaluation path (`GlideImpersonate` plus `eval` of the criteria script, or the platform `GlideUserCriteria` evaluator) behaves differently across ServiceNow releases. Validate it in a **Scripts - Background** window on the target instance before production use.
+ **Namespace resolution.** The {{NAMESPACE}} segment of the path is derived from the instance's application scope and may not equal the API ID verbatim. Record the actual resolved base path and store exactly that in `aclCheckPath`.

**Troubleshooting.** Before you expose the endpoint, validate impersonation and release compatibility in a **Scripts - Background** window on the target instance. Replace the two IDs with a real advanced `user_criteria` sys ID and a real user sys ID.

```
var criteriaId = '<advanced_user_criteria_sys_id>';
var userId     = '<user_sys_id>';

var imp = new GlideImpersonate();
var original = gs.getUserID();
try {
    imp.impersonate(userId);
    gs.info('impersonation took effect: ' + (gs.getUserID() === userId));  // must be true
    var uc = new GlideRecord('user_criteria');
    uc.get(criteriaId);
    var script = uc.getValue('script');
    var answer = false;
    eval(script);
    gs.info('advanced criteria answer for user: ' + answer);
} finally {
    imp.impersonate(original);
}
```
+ If "impersonation took effect" logs `false`, the `impersonator` role is missing. Assign it (see [Add ACL-read roles to the service account](#kb-managed-servicenow-oauth2-acl-roles)).
+ If `eval(script)` throws on this release, switch the advanced branch to the platform `GlideUserCriteria` evaluator and re-test.

Also confirm `match_all` agreement with the crawl. Pick one article with `match_all = true` (AND) and one with `match_all = false` (OR). Confirm that the verifier denies a user who satisfies only part of an AND criterion, and that Retrieve on the crawled index agrees. Any divergence means the verifier is not a valid oracle for the retrieve-versus-crawl cross-check.

## Next steps
<a name="kb-managed-servicenow-oauth2-next"></a>

After you store the secret, create the data source. See [Connect a ServiceNow data source](kb-managed-ds-servicenow-connect.md).