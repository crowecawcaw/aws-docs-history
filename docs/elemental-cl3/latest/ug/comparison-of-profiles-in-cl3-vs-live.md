# Comparison of

profiles

The way that channels (which you create using Conductor Live) and events (which
you create using Elemental Live) use their profiles is different. The way that
channels use profiles has some distinct advantages in terms of visibility and
maintenance.

If you have been using AWS Elemental Live in standalone mode or if you think you
might occasionally run work in Elemental Live in standalone mode, you should read the
information in the table to understand the differences.

| Conductor Live                                                                                                                                                                              | Elemental Live                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Conductor Live profile can be used only with a channel created in Conductor Live.<br>It cannot be used by an Elemental Live event.                                                          | An Elemental Live profile can be used only with an event created in Elemental Live.<br>It cannot be used by an Conductor Live channel.                                                                                                                                                                                                   |
| After a channel is created, it is linked to its profile.<br>A link exists between a channel and the profile used.<br>You can view the channels-profile association on the Channels<br>page. | After an event is created, it is not linked to the profile.<br>After the event is created, the data from the source profile exists<br>in the event, but no link exists for that profile.<br>You cannot query the event to find out which profile was originally<br>used.                                                                 |
| You cannot change a profile.<br>Instead, you can create a new profile with a new name. You can also<br>duplicate an existing profile and then change it.                                    | You can change a profile.                                                                                                                                                                                                                                                                                                                |
| Two channels can share a profile.<br>If channel_A was created using profile_X and channel_B was created<br>using profile_X, then they all have the same “profile values.”                   | There is no idea exists of two events “sharing” the same profile.<br>If event_A was created using profile_X and event_B was created<br>using profile_X, they do not automatically therefore have all the same<br>“profile values.” (For example, if event_B was created after profile_X<br>was modified, A and B have different values.) |
