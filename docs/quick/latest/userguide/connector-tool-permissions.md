

# Tool permissions
<a name="connector-tool-permissions"></a>

Connector owners and administrators can enable or disable individual tools within a connector to control which tools are available to users. Tool permission settings also let connector owners decide which tools require user consent before running, and which tools users can configure for themselves.

## Tool permission settings
<a name="connector-tool-permissions-review-behavior"></a>

Connector authors configure tool permissions at the individual action level. The permission setting determines whether you see a confirmation prompt before an action runs. These settings apply across all Amazon Quick clients, including Chat, Agents, Pages, and Flows.

**Always Ask**  
When a connector author sets an action to **Always Ask**, every invocation presents you with a confirmation prompt. You cannot override this behavior through your user-level preferences. The prompt always appears.

**Let Users Choose** (default)  
**Let Users Choose** is the default setting for all actions. When a connector author sets an action to **Let Users Choose**, your user-level preference determines the initial behavior.  
+ For write actions, the user-level default is **Always Ask**, so you see a confirmation prompt on every invocation until you change your preference.
+ For read actions, the user-level default is **Always Allow**, so you do not see a confirmation prompt unless you change your preference.
When you see a confirmation prompt, you can choose one of the following options.  
+ **Allow**. The action runs this time. The prompt reappears on the next invocation.
+ **Trust**. The action runs and the prompt does not appear for future invocations.
+ **Deny**. The action does not run.

## Connector-level settings
<a name="connector-tool-permissions-connector-level"></a>

Connector owners configure tool behavior for all users of a connector.


**Connector-level settings**  

| Setting | Behavior | 
| --- | --- | 
| Let Users Choose | You can individually configure how each action runs through your user-level preferences. | 
| Always Ask | You always see a confirmation prompt before the action runs. | 
| Disable | No user can run the action. | 

## User-level settings
<a name="connector-tool-permissions-user-level"></a>

You can configure tool behavior for your own connector. These settings apply only to your connection and do not affect other users.


**User-level settings**  

| Setting | Behavior | 
| --- | --- | 
| Always Ask | You see a confirmation prompt before the action runs. | 
| Always Allow | The action runs without a confirmation prompt. | 
| Disable | You cannot run the action from your connection. | 

## Default behavior
<a name="connector-tool-permissions-default-behavior"></a>

The following table shows the default settings that Amazon Quick applies to each action type.


**Default behavior by action type**  

| Action type | Connector-level default | User-level default | User-changeable | 
| --- | --- | --- | --- | 
| Write actions | Let Users Choose | Always Ask | Yes | 
| Read actions | Let Users Choose | Always Allow | Yes | 