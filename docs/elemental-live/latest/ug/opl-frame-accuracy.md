# About output locking and frame

accuracy

You can implement output locking to produce video outputs that are _frame accurate_ with each other. The frames from several outputs are _locked_ together.

Frame accuracy means that two frames with the same timecode are
identical in the following ways:

- The same content—the same picture on the video
  frame.
- The same segment number, manifest data, and so on.
- The same presentation timestamp (PTS).
