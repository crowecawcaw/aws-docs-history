# Running mode for WorkSpaces Pools

The running mode of a WorkSpaces Pool determines its immediate availability and how you pay
for it. You can choose between the following running modes when you create a
WorkSpaces Pool:

- **AutoStop** — Instances of a WorkSpaces Pool are billed an hourly
  usage fee based on the bundle chosen, only for the instances that are connected
  to users. Instances within a WorkSpaces Pool that are not connected to users are
  billed a low stopped-instance hourly fee. When users initiate their session,
  they start streaming after 1-2 minutes.
- **AlwaysOn** — Running instances of a WorkSpaces Pool are billed
  the applicable hourly usage fee, even when users aren't connected. This mode is
  best for users who don’t want to wait for their streaming to start.
  For more information, see [WorkSpaces Pricing](https://aws.amazon.com/workspaces/pricing/ "https://aws.amazon.com/workspaces/pricing/").

###### Contents

- [Modify the running mode](modify-running-mode-pool.md "modify-running-mode-pool.md")
