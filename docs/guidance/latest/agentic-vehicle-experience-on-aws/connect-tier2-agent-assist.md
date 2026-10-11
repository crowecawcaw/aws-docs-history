

# Context the tier-2 agent receives
<a name="connect-tier2-agent-assist"></a>

When a session escalates, the tier-2 agent sees the context in the chat itself, so the driver does not repeat anything.


| Context element | Content | 
| --- | --- | 
| Initial message | The first line of the chat: severity, driver, VIN, the reason, the conversation summary, and whether roadside was requested | 
| Contact attributes |  `severity`, `escalationType` (`safety` or `service`), `tenantId`, `vin`, `vehicleId`, `driverId`, `driverName`, `reason`, `summary` (up to 2,000 characters), `triageSessionId` and `voiceSessionId`. Every value is length-capped, because Connect refuses a contact whose attributes exceed 32 KB | 
| P0 callback |  `p0CallbackPlaced` and `p0CallbackEscalationId`, which match the chat to the call placed before it | 

The contact flow uses `severity` and `escalationType` for routing only; neither grants roadside or callback authority. Agents work the chat in the Amazon Connect Contact Control Panel, which the CMS console embeds next to a panel that shows these attributes.