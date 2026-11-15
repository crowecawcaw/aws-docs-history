

# Tips and troubleshooting
<a name="genai-tips"></a>

## Get better answers
<a name="get-better-answers"></a>
+ Give a time range, for example "last 30 days" or "this quarter".
+ Name the accounts, Regions or services you care about.
+ Ask for amounts and savings estimates, and for a prioritized list.
+ To verify a number, ask the agent where to find it in the dashboards.
+ Deploy more dashboards: every dashboard in an agent’s list adds knowledge.

## Troubleshooting
<a name="troubleshooting"></a>

 ** `cid-cmd` reports access denied, but I can create agents in the Quick console.** 

The console uses your Quick user, while `cid-cmd` calls the API with your IAM identity. Add the IAM actions listed in [Deploy agents](genai-deploy-agents.md) to your role.

 ** `cid-cmd` says the user needs the Author Pro role.** 

The owner of the agent must be an Author Pro or Admin Pro user in Quick. Ask your Quick administrator to change the user’s role, or pass a group with `--quicksight-group`.

 **The agent shows no "Created by" in the console.** 

This is expected for agents created through the API. You own the agent through its permissions and can edit, share and delete it.

 **The agent says data is missing.** 

Check which dashboards the agent found with `cid-cmd list-agents`. Deploy the missing dashboards, then run `cid-cmd update-agent` to add them to the Space.