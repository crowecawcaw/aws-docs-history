# Creating actions in the schedule

(console)

You can create different actions in the schedule. For a list of supported actions,
see [Types of actions in the
schedule](x-actions-in-schedule.md "x-actions-in-schedule.md").

The general procedure is the same to create any type of action.

###### To create an action

1. Read the information about [planning
   the actions](sched-how-actions-work.md "sched-how-actions-work.md") you want to add.
2. Open the MediaLive console at [https://console.aws.amazon.com/medialive/](https://console.aws.amazon.com/medialive/ "https://console.aws.amazon.com/medialive/").
3. In the navigation pane, choose **Channel**, and then
   choose the channel that you want to work with.
4. On the **Details** pane, choose the
   **Schedule** tab.
5. Choose the **Switch** button to display the view that you
   want: **List** view or **Timeline** view.
   For information about the layout and color coding of the timeline view, see
   [Viewing the
   schedule (console)](schedule-using-console-view.md "schedule-using-console-view.md").
6. For **List** view, choose the appropriate action:
   - To create a fixed, follow, or immediate action from scratch,
     choose **Create**.
   - To create a follow action after an existing action, choose that
     action, choose **Schedule actions**, and then
     choose **Create follow actions from**.

   This method displays the **Create schedule
   action** page with some fields already completed, so
   you can quickly create a follow switch for that existing
   action.

7. For **Timeline** view, choose the appropriate
   action:
   - To create a fixed, follow, or immediate action from scratch,
     choose **Create**.
   - To create a follow action, find the input switch that you want to
     follow, and then choose **Create follow action** in
     that card.

   This method displays the **Create schedule
   action** page with some fields already completed, so
   you can quickly create a follow switch for that existing
   action.

8. On the **Create schedule action** page, complete the
   fields. For information about completing the fields, see the following
   topics.
9. When you have finished, choose **Create**.

MediaLive adds the action to the list or the timeline at its appropriate time
slot.
When you create a follow input switch, you effectively create an _input follow chain_. The input follow chain starts with
the input above the first follow and ends with the last follow input. For more
information about input follow chains, see [Fixed, immediate, and follow switches](ips-switch-types.md "ips-switch-types.md").

###### Topics

- [Fields for an input switch](schedule-fields-for-ips.md "schedule-fields-for-ips.md")
- [Fields for an input
  prepare](schedule-fields-for-input-prep.md "schedule-fields-for-input-prep.md")
- [Fields for activating a
  global image overlay](schedule-fields-for-activate-image.md "schedule-fields-for-activate-image.md")
- [Fields for deactivating a
  global image overlay](schedule-fields-for-deactivate-image.md "schedule-fields-for-deactivate-image.md")
- [Fields for
  activating a per-outputs image overlay](schedule-fields-activate-image-per-output.md "schedule-fields-activate-image-per-output.md")
- [Fields for
  deactivating a per-outputs image overlay](schedule-fields-deactivate-image-per-output.md "schedule-fields-deactivate-image-per-output.md")
- [Fields for activating a motion graphics
  overlay](schedule-fields-for-mg.md "schedule-fields-for-mg.md")
- [Fields for deactivating a
  motion graphics overlay](schedule-fields-for-mg-deactivate.md "schedule-fields-for-mg-deactivate.md")
- [Fields for a splice_insert
  message](schedule-fields-for-splice_insert.md "schedule-fields-for-splice_insert.md")
- [Fields for a time_signal
  message](schedule-fields-for-time-signal.md "schedule-fields-for-time-signal.md")
- [Fields for a
  return-to-network message](schedule-fields-for-return-to-network.md "schedule-fields-for-return-to-network.md")
- [Fields for ID3
  metadata](schedule-fields-for-id3-userdata.md "schedule-fields-for-id3-userdata.md")
- [Fields for ID3 segment
  tags](schedule-fields-for-id3-segment-tags.md "schedule-fields-for-id3-segment-tags.md")
- [Fields for pause](schedule-fields-for-pause.md "schedule-fields-for-pause.md")
- [Fields for unpause](schedule-fields-for-unpause.md "schedule-fields-for-unpause.md")
