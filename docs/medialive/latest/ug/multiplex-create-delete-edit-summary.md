# Summary of actions

The following table summarizes the create, edit, and delete capabilities for the MediaLive
multiplex, program, and channel.

| Item      | Action | Note                                                                                                                                                                                                                           |
| --------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Multiplex | Create |                                                                                                                                                                                                                                |
|           | Edit   | The multiplex can be idle or running. The channels can be all idle, or all<br>running, or a combination or idle and running.<br>Exception: To change the \*_Max Video Buffer Delay_<br>• field, the<br>multiplex must be idle. |
|           | Delete | The multiplex must be idle, and must not have any associated programs.                                                                                                                                                         |
| Program   | Create | The multiplex for the program can be idle or running.                                                                                                                                                                          |
|           | Edit   | The multiplex for this program can be idle or running. The channel for this<br>program can be idle or running.                                                                                                                 |
|           | Delete | The multiplex for this program can be idle or running. The program can't have any<br>associated channel.                                                                                                                       |
| Channel   | Create | The multiplex for this channel can be idle or running. The program for the<br>channel must be empty.                                                                                                                           |
|           | Edit   | The channel must be idle. The multiplex for this channel can be idle or running.                                                                                                                                               |
|           | Delete | The channel must be idle. The channel can still be attached to a program.                                                                                                                                                      |
