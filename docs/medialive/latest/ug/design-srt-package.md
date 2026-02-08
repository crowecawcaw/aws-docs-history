# Organize encodes in an SRT output

group

An SRT output group can contain the following:

- One or more outputs.

Each output contains the following:

- One video encode.
- One or more audio encodes.
- Zero or more captions encodes. The captions are either embedded or
  object-style captions.
  Each output represents one SPTS. Each output (SPTS) has its own destination.

This diagram illustrates an SRT output group with one output. The captions are
embedded in the video encode.

![](images/output3-nonABR-Ve-2A.png)
This diagram illustrates an SRT output group with one output. The captions are
object-style captions.

![](images/output4-nonABR-V-2A-2C.png)
