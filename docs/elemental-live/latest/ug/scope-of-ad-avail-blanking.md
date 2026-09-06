

# Scope of ad avail blanking of SCTE-35 messages
<a name="scope-of-ad-avail-blanking"></a>

For Ad avail blanking (but not for Blackout), the ad avail mode you set controls which SCTE-35 events result in blanking of the content. 

**Using Splice Insert Mode**  
This table describes which message type/segmentation type combination is blanked by Ad avail blanking when the Ad Avail mode ([Getting ready: Setting the ad avail mode](getting-ready-setting-the-ad-avail-mode.md)) is **Splice Insert mode**. 



- **Splice insert **
  - **Segmentation type ID:** No segmentation descriptor present / **Blanked:** X / **Not blanked:**  
  - **Segmentation type ID:** Provider advertisement / **Blanked:** X / **Not blanked:**  
  - **Segmentation type ID:** Distributor advertisement / **Blanked:** X / **Not blanked:**  
  - **Segmentation type ID:** Placement opportunity / **Blanked:** X / **Not blanked:**  
  - **Segmentation type ID:** Other type (e.g. Chapter, Program) / **Blanked:**   / **Not blanked:** X

- **Time signal **
  - **Segmentation type ID:** Provider advertisement / **Blanked:** X / **Not blanked:**  
  - **Segmentation type ID:** Distributor advertisement / **Blanked:** X / **Not blanked:**  
  - **Segmentation type ID:** Placement opportunity / **Blanked:** X / **Not blanked:**  
  - **Segmentation type ID:** Other type (e.g. Chapter, Program) / **Blanked:**   / **Not blanked:** X



**Using Time Signal APOS Mode**  
This table describes which message type/segmentation type combination is blanked out by Ad avail blanking when the Ad Avail mode ([Getting ready: Setting the ad avail mode](getting-ready-setting-the-ad-avail-mode.md)) is **Timesignal with APOS mode**. 



- **Splice insert **
  - **Segmentation type ID:** Any
  - **Blanked:**  
  - **Not blanked:** X

- **Time signal **
  - **Segmentation type ID:** Provider advertisement / **Blanked:**   / **Not blanked:** X
  - **Segmentation type ID:** Distributor advertisement / **Blanked:**   / **Not blanked:** X
  - **Segmentation type ID:** Placement opportunity / **Blanked:** X / **Not blanked:**  
  - **Segmentation type ID:** Other type (e.g. Chapter, Program) / **Blanked:**   / **Not blanked:** X



**Ad avail blanking and restriction flags: restrictions in the input**  
SCTE-35 messages of type **time\_signal** always contain segmentation descriptors. 

SCTE-35 messages of type **splice\_insert **may or may not include segmentation descriptors.

If the input has SCTE-35 messages that *do* include segmentation descriptors, these segmentation descriptors always include two types of flags. These flags provide additional information as guidance for blanking in specific situations:
+ **web\_delivery\_allowed\_flag**. 
  + "True" means that there is no restriction on including the ad avail event’s content in a stream intended for web delivery: you do not need to blank out content in streams intended for web delivery. 
  + "False" means there is a restriction: you should blank out the content . 
+ **no\_regional\_blackout\_flag.** 
  + "True" means that there is no restriction on including the ad avail event’s video in a stream intended for regional markets: you do not need to blank out content in streams intended for regional markets. 
  + "False" means there is a restriction: you should blank out the content.

If neither flag is present (usually the case with **splice\_inserts**), then both are considered to be false: blanking should occur.

If both flags are present (which is usually the case; it is unusual to have only one flag present), then a “false” for one flag takes precedence over a “true” for the other flag: blanking should occur.

Typically, in any given message in the input only one of these flags would ever be set to "false", so only one restriction would ever be in place. There would typically never be *both* a regional delivery restriction and a web delivery restriction. This is because, if content is considered restricted for regional delivery, then it would not also be considered restricted for web delivery (where the concept of a region does not relate).

To summarize, this table shows the blanking logic that applies to each ad avail event that is encountered:


|  | Content of corresponding SCTE-35 MessageWeb delivery allowed? | Content of corresponding SCTE-35 MessageRegional delivery allowed? | Result | Comment | 
| --- | --- | --- | --- | --- | 
| S1 | Flag is not present. | Flag is not present. | Blanking will occur. | This combination can occur only in a message type splice\_insert (where the segmentation descriptor is optional). | 
| S2 | True | True | Blanking will not occur. |   | 
| S3 | True | False | Blanking will occur. |   | 
| S4 | False | True | Blanking will occur. |   | 

**Ad avail blanking and restriction flags: Elemental Live handling of restrictions**  
You can modify this default blanking behavior by instructing Elemental Live to ignore a restriction flag that is set to "false", so that blanking will not occur for this ad avail event. In other words, to use this logic: “Even if the message indicates to blank content because a regional blackout is in place, do not follow this instruction. Ignore the fact that a regional blackout is in place and do not blank content.”

You modify the behavior by setting one or the other of the **Ignore** flags to:
+ **Cleared**(default ). The logic as above applies: so continue to observe the restriction.
+ **Selected**. Ignore the restriction and do not blank video for the ad avail event.

**Warning**  
Never set both fields to **Ignore**\! 

To summarize, the Ignore flags make a difference only to the scenarios in this table:


|  | Content of corresponding SCTE-35 MessageWeb delivery allowed? | Content of corresponding SCTE-35 MessageRegional delivery allowed? | Restriction field in Elemental Live | Result | 
| --- | --- | --- | --- | --- | 
| S3 | True | False | Ignore “regional delivery” restriction | Blanking will not occur. | 
| S4 | False | True | Ignore “web delivery” restriction | Blanking will not occur. | 

**Ad avail blanking and restriction flags: restriction flags with “splice insert”**  
If you selected Splice Insert as the Ad Avail mode, then you can assume that the SCTE-35 ad avail message not include the two restriction flags described above. Every SCTE-35 ad avail message should result in an ad avail. 

Therefore, if you know that input contains splice inserts (not time signals), you should leave both Elemental Live fields cleared.