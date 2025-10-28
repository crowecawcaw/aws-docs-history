# Font styles for Burn-in or DVB-Sub

This section applies if you are [setting up
Burn-in or DVB-Sub captions](output-embedded-and-more.md "output-embedded-and-more.md") in a MediaLive channel. You might decide to specify the
look of the captions. The following rule applies.

If you are using the same captions source in several outputs and all those outputs
use the same format, then you must set up the font style information identically in each
output. If you don't, you get an error when you save the channel. For example, you have
an Archive output that includes DVB-Sub captions converted from captions selector
"embedded". And you have a UDP output that also includes DVB-Sub captions converted from
the same captions selector.

Note that you must set up the font style information
separately
in each output. But you must enter the same information in
each
output.

For example, output A might use **Captions Selector 1** with the
**Destination Type** set to **Burn-in**. And output
B might also use **Captions Selector 1** with the **Destination
Type** set to **Burn-in**. You set the font information once
in output 1 and again in output 2. But you must set up all the font information
identically in both outputs.
