# Details on

activating inputs

## Dynamic

playlist order rules

When an input starts to be processed (it is “playing”),
that input becomes “active”.

A file input typically moves through these stages:

- Idle and not prepared.
- Next-in-line and not prepared.
- Due-to-be-processed and not prepared.
- Active (prepared and processing).
- Idle (completed)

A live input typically moves through these stages:

- Idle and not prepared.
- Next-in-line and prepared.
- Due-to-be-processed and prepared.
- Active (processing).
- Idle (completed)

### Idle

Any number of inputs can be idle.

The list of idle inputs includes inputs that have
completed and those that have not been processed.

### Next-in-Line

Only one input can be Next-in-line. This is the input
that is either:

- The input that is after the currently active
  input, based on the order in which the inputs
  appear in the event XML and on the web
  interface.
- The input that has an activate time that
  exactly aligns with the end time of the current
  input.

Ideally, you should order the inputs in the XML so
that an input that has an activate time also appears in
its natural order. For example, it does not appear at
the end of the list; this placement will cause confusion
to your operators.

A next-in-line input may be prepared or unprepared.

### Due-to-be-processed input

The input that is currently Next-in-line becomes
Due-to-be-processed at the moment that the currently
Active input completes.

This input then instantaneously transitions to
Active.

### Active input

This is the input that is being processed. An input
becomes active as follows:

- If the input is a live input has been
  prepared, it will be activated and processing
  will start seamlessly.
- If the input is a live input has not yet been
  prepared, it will still be activated; it will
  not be skipped. Instead, it will first be
  prepared, then activated. There will be a
  noticeable delay while the input is prepared.
- If the input is a file input, it will be
  prepared and activated.

## Rules for

activating

The rules apply to activating an input.

- When you call Activate Immediately on an input,
  the currently Activated input will immediately
  transition to Idle and processing of that input will
  stop.
- When you call Activate Immediately on an input
  that has previously been set up to activate at a
  time that is still in the future, the input will
  activate immediately and the future activation will
  be cleared. It will not be activated both
  immediately and in the future.
- When you call Activate with Specified Time and
  then call Prepare, the activate time is not cleared:
  the input will be prepared (either immediately or
  later, depending on what you set up), then the input
  will be activated at the specified time.
- If you call Activate with Specified Time on an
  input that has not been prepared, the input will
  first be prepared (at the specified time), then it
  will be activated. There will be a noticeable delay
  in activation. In other words, activating with a
  specified time does not automatically set up any
  prepare schedule.
- If you both manually prepare an input with a
  prepare time and manually activate it with an
  activate time, make sure the prepare time is before
  the activate time; Elemental Live does not
  check.
