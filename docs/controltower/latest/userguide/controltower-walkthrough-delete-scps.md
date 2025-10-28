# Delete SCPs

AWS Control Tower uses service control policies (SCPs) for its controls. This procedure walks through
how to delete the SCPs specifically related to AWS Control Tower.

###### To delete AWS Organizations SCPs

1. Open the Organizations console at [https://console.aws.amazon.com/organizations/](https://console.aws.amazon.com/organizations/ "https://console.aws.amazon.com/organizations/").
2. Open the **Policies** tab, and find the Service Control Policies (SCPs)
   that have the prefix **aws-guardrails-** and do the following for each
   SCP:
   1. Detach the SCP from the associated OU.
   2. Delete the SCP.
