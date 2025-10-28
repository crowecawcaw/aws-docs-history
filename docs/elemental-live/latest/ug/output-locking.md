# Output locking

You can implement output locking to produce video outputs that are _frame accurate_ with each other. Implement output locking to enhance output
redundancy, or to implement distributed encoding.

When outputs are locked together, they are frame accurate with each
other. Frame accuracy means that two frames with the same timecode are
identical in the following ways:

- The same content—the same picture on the video frame.
- The same segment number, manifest data, and so on.
- The same presentation timestamp (PTS).
  There are two ways to implement:

- [Standard output
  locking](opl-standard-how-it-works.md "opl-standard-how-it-works.md").

- [Epoch locking](opl-epoch-how-it-works.md "opl-epoch-how-it-works.md").

###### Note

The information in this section assumes that you are familiar with the
general steps for creating an event.

###### Topics

- [About output locking and frame
  accuracy](opl-frame-accuracy.md "opl-frame-accuracy.md")
- [Output locking use cases](output-locking-general.md "output-locking-general.md")
- [How output locking
  works](opl-standard-how-it-works.md "opl-standard-how-it-works.md")
- [How epoch locking works](opl-epoch-how-it-works.md "opl-epoch-how-it-works.md")
- [Output locking pools](opl-pools.md "opl-pools.md")
- [Output locking pairs](opl-redundant-pairs.md "opl-redundant-pairs.md")
- [Requirements for inputs
  and outputs](output-locking-requirements.md "output-locking-requirements.md")
- [Step 1: Design the workflow](opl-step-get-ready.md "opl-step-get-ready.md")
- [Step 2: Set up inputs in the
  events](output-locking-setup-inputs.md "output-locking-setup-inputs.md")
- [Step 3: Set up the global
  controls](output-locking-setup-global.md "output-locking-setup-global.md")
- [Step 4: Set up the output
  groups and outputs](opl-setup-output-groups.md "opl-setup-output-groups.md")
- [Step 5:
  Set up the video encodes](output-locking-event-setup-stream-video-fields.md "output-locking-event-setup-stream-video-fields.md")
