# Get preview

configuration for the given contactId in Amazon Connect Agent Workspace

This gets configuration information related to the preview experience.

**Signature**

```

getPreviewConfiguration(contactId: string): Promise<GetPreviewConfigurationResponse>

```

**Usage**

```

const isPreview  = await contactClient.isPreviewMode(contactId);
if (isPreview) {
    const {autoDialTimeout, canDiscardPreview} = await contactClient.getPreviewConfiguration(contactId);
}

```

**Input**

| **Parameter**        | **Type** | **Description**                            |
| -------------------- | -------- | ------------------------------------------ |
| contactId _Required_ | string   | The id of the contact which is in preview. |

**Output - GetPreviewConfigurationResponse**

| **Parameter**     | **Type** | **Description**                                                                                                                                                                                             |
| ----------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| autoDialTimeout   | number   | The number of seconds the agent has to preview the contact<br>before the auto-dial triggers.                                                                                                                |
| canDiscardPreview | boolean  | Whether the agent has permission to discard the contact during<br>preview. Use this to control whether the agent should be presented<br>the option to discard the contact without dialing the end customer. |
