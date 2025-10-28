# Types of starts for input prepares

There are three start types for input prepare actions in MediaLive. These start types are the
same as the start types for input switches.

- Fixed – the input prepare starts at a specific time.
- Immediate – the input prepare starts as soon as you add the action to the
  schedule.
- Follow – the input prepare follows a specific input switch—the _reference input switch_. It can have a start or an end _follow point_—it can follow the start of the reference input
  or the end of the reference input.
  With the follow start type, the following rules apply:

- You can't use the console to create a follow input prepare with a follow point set to
  _start_. The start option is not shown on the console. Only
  the end option is shown.
- MediaLive starts preparing the input _after_ the
  reference input is active. Therefore:
  - For a follow-start prepare (which you can create only using the CLI), you must add the
    prepare action before the reference input has started in the channel.

  If the reference switch is an immediate switch, you must include the switch action and
  the prepare action in the same [batch update
  command](about-batch-update-schedule.md "about-batch-update-schedule.md").

  If the reference switch is a fixed or follow switch, you can add the switch action in
  one batch update command, and the prepare action in a later batch update command.
  - For a follow-end prepare, you must add the prepare action before the reference input
    has ended (before ingest has ended).

- You can't create two follow prepare actions that both follow the same reference switch
  and the same follow point. Therefore:
  - You _cannot_ create action 2 and action 4 to both
    follow the start of action 1.
  - But you can create action 2 to follow the _start_ of
    action 1, and action 4 to follow the _end_ of action
  1.
