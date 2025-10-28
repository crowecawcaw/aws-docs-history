# Recommended testing

procedure

We strongly recommend that you perform this performance testing before you deploy a new
appliance into production.

1. Design the lab tests as follows:
   - Set up all of the workflows that you expect to run on the appliance.
   - Obtain input that is a good example of the most complex source that you expect to
     handle. A complex source is one that has video that includes the following:
     - A lot of movement and change of scene.
     - Possibly a ticker tape or other strip of text.
     - Broad areas of the same color, like a grassy area, because high video quality of these
       areas is difficult to obtain.

   - Set up the events with the most complex outputs that you expect to
     run on the appliance. Include any high-demand features that you plan to
     implement. See [Features that affect
     performance](performance-features.md "performance-features.md").
   - Run the events for several days.

2. Monitor the events as described in this section:
   - Frequently measure the CPU usage, RAM usage, I/O bandwidth, and
     system bandwidth. See [Assessing performance by
     measuring](performance-measures.md "performance-measures.md").
   - Continually monitor the logs that Elemental Live produces. See [Assessing performance with logging messages](performance-via-logs.md "performance-via-logs.md").

3. Revise the workflows in terms of density and video quality, and
   continue testing. You should revise the workflows incrementally.
