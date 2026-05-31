# Set the visual mode of a user in Connect Customer agent workspace

Sets the visual mode (light, dark, or auto) for the user that's currently
logged in to the Connect Customer agent workspace. The promise resolves once the
visual mode change has been persisted.

**Signature**

```

setVisualMode(visualMode: VisualMode): Promise<void>

```

**Usage**

```

await settingsClient.setVisualMode("dark");

```

**Input**

| **Parameter**         | **Type**   | **Description**                                                     |
| --------------------- | ---------- | ------------------------------------------------------------------- |
| visualMode _Required_ | VisualMode | The visual mode to set. One of `"light"`,<br>`"dark"`, or `"auto"`. |

**Permissions required:**

```

*

```
