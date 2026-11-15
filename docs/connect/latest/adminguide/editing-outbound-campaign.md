

# Editing an outbound campaign
<a name="editing-outbound-campaign"></a>

**Note**  
You can edit any outbound campaign in the Initialized state. Running or paused campaigns can be updated only if they are journey-type.

While a journey is running or paused, you can update the following settings. Your changes take effect as the journey continues to run.

**Journey flow**  
This change takes effect only at the next scheduled repeat of the journey. Profiles that were already in the journey before the update continue to use the previous flow.

**Customer Profiles segment**  
When you change a journey's segment during execution, newly matched profiles are added to the journey starting at the next refresh. Profiles that no longer meet the segment definition are not included in the next refresh. Profiles that were already in the journey before the change continue in the journey and are not affected by the segment change.  
The replacement segment must have the same sorting type as the current segment. You can't replace a sorted segment with an unsorted segment, or an unsorted segment with a sorted segment.

**Communication limits**  
Updates to communication limits are applied within minutes. If you reduce limits, profiles whose communication counts now exceed the new limits are removed from the journey.

**Communication time**  
Updates to active communication time, or to exceptions to communication time, are applied within minutes, and sending is adjusted accordingly based on the new time windows.