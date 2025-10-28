# Triggers for blackout

The blackout feature is triggered only by time_signal messages of segmentation
type **Other**. It is not triggered by splice_insert messages of
any segmentation type, and is not triggered by time_signal messages of any type
except **Other**.

SCTE 35 messages of type ID "splice insert" and messages of type ID "time signal"
can both include "Other" time_signal messages. Therefore, when enabling blackout,
the [ad avail mode](getting-ready-set-the-ad-avail-mode.md "getting-ready-set-the-ad-avail-mode.md") is not
relevant. Blackout works the same with either mode.

The segmentation ID triggers blackout based on events, as shown in the following
table.

| Message type Id           | SCTE 35 segmentation type                                | Start blacking out | End blacking out  |
| ------------------------- | -------------------------------------------------------- | ------------------ | ----------------- | --------------------- | --- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| splice insert             | Any                                                      | Not a trigger      | Not a trigger     |
| time signal               | Provider advertisement, Distributor advertisement, Break | Not a trigger      | Not a trigger     |
| Chapter Start             | Start blacking out                                       |                    |                   | Chapter End           |     | End blacking out |
| Network _End_             | Start blacking out                                       |                    |                   | Network _Start_       |     | End blacking out |
| Program Start             | Start blacking out                                       |                    |                   | Program End           |     | End blacking out |
| Unscheduled Event Start   | Start blacking out                                       |                    |                   | Unscheduled Event End |     | End blacking out | For example, if the blackout feature is enabled, then blanking always occurs when a Program Start message is encountered and always ends when a Program End message is encountered. Note that the triggers for blackout on a Network event are different from the other events: <br>• With Network, blanking starts when the Network _End_ instruction is encountered. <br>• With other events, blanking starts when the "Event _Start_" instruction is encountered. **End event trigger hierarchy** Events have the _strength hierarchy_ shown in the following table. A blackout can be ended only by an event of equal or greater strength than the event that started it. For example, if the blackout is started by a Program Start, it can be ended by a Network Start, an Unscheduled Event End or a Program End. It cannot be ended by a Chapter End. MediaLive ignores the "end blackout" instruction implied by the Chapter End. |
| SCTE 35 segmentation type | Strength                                                 |                    | ---               | ---                   |
| Network                   | 1 (Strongest)                                            |                    | Unscheduled Event | 2                     |
| Program                   | 3                                                        |                    | Chapter           | 4 (Weakest)           |
