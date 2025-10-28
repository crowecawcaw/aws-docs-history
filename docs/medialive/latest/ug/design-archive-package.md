# Organize encodes in an Archive output

group

An Archive output group
can
contain
the following:

- One or
  more
  outputs.
  The output contains the following:

- One video encode.
- Zero or more audio encodes.
- Zero or more captions encodes. The captions are either embedded or
  object-style captions.
  Typically,
  the Archive output group mirrors the output structure of another output group. For
  example, it might mirror the ABR stack in an HLS output group.

This diagram illustrates an Archive output group that contains one output that holds
one video encode with embedded captions, and two audio encodes.

![Output group diagram showing one output with a video encode and two audio encodes.](images/output3-nonABR-Ve-2A.png)
This diagram illustrates an Archive output group that contains one output that holds
one video encode, two audio encodes, and two object-style captions encode.

![Output group containing V, A, A, C, C elements representing video, audio, and caption encodes.](images/output4-nonABR-V-2A-2C.png)
