# PIDs for ARIB

This section applies if you are [setting up
ARIB captions](output-embedded-and-more.md "output-embedded-and-more.md") in an

output group
that supports a
transport stream. For example, UDP or
SRT.
You must specify the output PID.

- In the relevant
  output
  group, choose the output that has the ARIB captions.
- For **PID settings**, complete **ARIB captions PID
  control** and **ARIB captions PID** as shown in the
  following table.

| ARIB Captions PID Control | ARIB Captions PID              | Result                                                                              |
| ------------------------- | ------------------------------ | ----------------------------------------------------------------------------------- |
| Auto                      | Ignore                         | A PID is automatically assigned during encoding. This value could be any<br>number. |
| Use Configured            | Enter a decimal or hexadecimal | This PID is used for the captions.                                                  |
