# Organize encodes in a UDP output group

A UDP output group
can
contain
the following:

- One or
  more
  outputs.
  Each output can contain the following:

- One video encode.
- One or more audio encodes.
- One or more captions encodes. The captions are either embedded or object-style
  captions.
  Each output represents one SPTS. Each output (SPTS) has its own destination..

This diagram illustrates a UDP output group
with one output.
The
captions are embedded in the video encode.

![Output group diagram showing video encode with embedded captions and two audio outputs.](images/output3-nonABR-Ve-2A.png)
This diagram illustrates a UDP output
group with one
output. The captions are
object-style
captions.

![Output group diagram showing V, A, A, C, C as individual elements in sequence.](images/output4-nonABR-V-2A-2C.png)
