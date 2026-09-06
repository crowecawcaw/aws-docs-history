

# Limitations of apps in Quick
<a name="apps-limitations"></a>

The following limitations apply to apps in Amazon Quick in its current release.

## Limits
<a name="apps-limits-platform"></a>


**Limits**  

| Resource | Limit | 
| --- | --- | 
| Dashboard visuals per app | 8 | 
| Visual minimum size | 100 × 100 pixels | 
| Storage value size | 350 KB per item | 
| Storage key length | 255 characters | 
| Table name length | 255 characters | 

## Building experience
<a name="apps-limits-building"></a>
+ **Content policy violations** — Prompts occasionally trigger security guardrails as false positives. When this happens, the agent cannot process further prompts in the current session. Close the editor and wait 15 to 20 minutes for the session to time out, then reopen the app.
+ **Agent memory in long conversations** — The agent's accuracy decreases as the conversation grows longer. For complex applications, consider building in phases.
+ **No image upload from agent chat** — You cannot upload screenshots or reference images to the agent.
+ **No investigation-only mode** — The agent executes code changes with every instruction. To have the agent investigate without making changes, explicitly say "Investigate but do not write code yet."
+ **Network sensitivity** — The editor uses a WebSocket for real-time streaming. Unstable connections can cause prompts to fail silently.

## Sharing and access
<a name="apps-limits-sharing"></a>
+ **Subscription requirement** — Only users with Author, Professional, Author Pro, Enterprise, or Admin Pro subscriptions can view apps.
+ **External access** — Users must have a Amazon Quick account to view an app, unless the app is published publicly. Public access is available on Free and Plus accounts only. Public apps cannot use connectors, embedded visuals, embedded chat, or spaces.

## Portability
<a name="apps-limits-portability"></a>
+ **No code export** — You cannot download the source code of an app.
+ **Duplication** — You can duplicate an app to create a copy.

## Integration limitations
<a name="apps-limits-integrations"></a>
+ **No direct Quick Flows integration** — Use a space as an intermediary.
+ **No standalone agent embedding** — You can create a new agent instance backed by a space.
+ **No integration removal** — You cannot remove a registered integration from an app through the settings UI.

## Sandbox restrictions
<a name="apps-limits-sandbox"></a>

For detailed information about sandbox restrictions, see [Sandbox restrictions](security-sandbox-apps.md#apps-sandbox-restrictions). Key restrictions include:
+ **No direct link navigation** — Users must use Cmd\+Click or Ctrl\+Click.
+ **No external images** — CSP blocks loading images from external URLs.
+ **No built-in app analytics** — As a workaround, you can ask the agent to implement a view counter using shared app storage.