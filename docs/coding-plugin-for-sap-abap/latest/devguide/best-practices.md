

# Best practices
<a name="best-practices"></a>

These practices help you get the most from Coding Plugin. Agentic development for SAP ABAP changes frequently. For the latest guidance and innovations, see the [AWS for SAP blog](https://aws.amazon.com/blogs/awsforsap/).

 **Keep each initiative in its own tab.** Open a new tab for each effort you undertake, and do not mix separate efforts in one tab. A tab holds one conversation, so a focused tab keeps Kiro’s context window on that one effort. For spec-driven development, author the spec in one tab and implement it in another, so each tab’s context can focus on a single phase.

 **Keep agentic work in its own transport.** Do not mix your own changes and the changes Coding Plugin makes in the same transport. Release any open transport before you start, so those changes land in a fresh one. A dedicated transport makes it clear what changed, and lets you compare versions and revert changes with SAP’s version management tools.

 **Keep scratch objects out of transports.** Tell Kiro to create temporary objects and test harnesses in `$TMP`, or another local (`$`) package, so they are never transported to production. Put this instruction in a steering file so Kiro applies it in every session.

 **Review changes before you release.** When you finish, ask Kiro to walk you through its changes. The Coding Plugin can open code editors to show you code, and can read past versions to help you understand what changed.