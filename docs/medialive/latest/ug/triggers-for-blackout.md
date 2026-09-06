

# Triggers for blackout
<a name="triggers-for-blackout"></a>

The blackout feature is triggered only by time\_signal messages of segmentation type **Other**. It is not triggered by splice\_insert messages of any segmentation type, and is not triggered by time\_signal messages of any type except **Other**. 

SCTE 35 messages of type ID "splice insert" and messages of type ID "time signal" can both include "Other" time\_signal messages. Therefore, when enabling blackout, the [ad avail mode](getting-ready-set-the-ad-avail-mode.md) is not relevant. Blackout works the same with either mode.

The segmentation ID triggers blackout based on events, as shown in the following table.



- **splice insert**
  - **SCTE 35 segmentation type:** Any 
  - **Start blacking out:** Not a trigger
  - **End blacking out:** Not a trigger

- **time signal**
  - **SCTE 35 segmentation type:** Provider advertisement, Distributor advertisement, Break / **Start blacking out:** Not a trigger / **End blacking out:** Not a trigger
  - **SCTE 35 segmentation type:** Chapter Start / **Start blacking out:** Start blacking out / **End blacking out:** 
  - **SCTE 35 segmentation type:** Chapter End / **Start blacking out:**  / **End blacking out:** End blacking out
  - **SCTE 35 segmentation type:** Network End / **Start blacking out:** Start blacking out / **End blacking out:** 
  - **SCTE 35 segmentation type:** Network Start / **Start blacking out:**  / **End blacking out:** End blacking out
  - **SCTE 35 segmentation type:** Program Start / **Start blacking out:** Start blacking out / **End blacking out:** 
  - **SCTE 35 segmentation type:** Program End / **Start blacking out:**  / **End blacking out:** End blacking out
  - **SCTE 35 segmentation type:** Unscheduled Event Start / **Start blacking out:** Start blacking out / **End blacking out:** 
  - **SCTE 35 segmentation type:** Unscheduled Event End / **Start blacking out:**  / **End blacking out:** End blacking out



For example, if the blackout feature is enabled, then blanking always occurs when a Program Start message is encountered and always ends when a Program End message is encountered.

Note that the triggers for blackout on a Network event are different from the other events:
+ With Network, blanking starts when the Network *End* instruction is encountered.
+ With other events, blanking starts when the "Event *Start*" instruction is encountered.

**End event trigger hierarchy**

Events have the *strength hierarchy* shown in the following table. A blackout can be ended only by an event of equal or greater strength than the event that started it.

For example, if the blackout is started by a Program Start, it can be ended by a Network Start, an Unscheduled Event End or a Program End. It cannot be ended by a Chapter End. MediaLive ignores the "end blackout" instruction implied by the Chapter End.


| SCTE 35 segmentation type | Strength | 
| --- | --- | 
| Network | 1 (Strongest) | 
| Unscheduled Event | 2 | 
| Program | 3 | 
| Chapter | 4 (Weakest) | 