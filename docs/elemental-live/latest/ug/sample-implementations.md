# Sample

implementations

## Implementing use

case 1

Use case 1 is described [here](typical-use-cases.md#use-case-1 "typical-use-cases.md#use-case-1").

1. Create an event that has the live feed as the
   input.
2. Once the event starts, create a dynamic playlist
   that consists of the following:
   - Second input – ad content – from
     file.
   - Third input – live input (identical to
     first input).
   - Fourth input - ad content – from
     file.
   - And so on.

3. Immediately set an activate time for the second
   input. The first input will be interrupted by the
   second input at this time.
4. After the second input becomes Active, prepare the
   third input.

When the second input ends, the third input will
immediately become Active. 5. After the third input becomes Active, set an
activate time for the fourth input. The third input
will be interrupted by the fourth input at this
time.

## Implementing use

case 2

Use case 2 is described [here](typical-use-cases.md#use-case-2 "typical-use-cases.md#use-case-2").

1. Create an event that has the live feed as the
   input.
   - Once the event starts, create a dynamic
     playlist that consists of the
     following:
     - Second input – ad content – from
       file.
     - Fourth input and others – file
       input, as required.
     - Finally, create an input to return
       to the live feed (same input source as
       the first input).

2. Immediately set an activate time for the second
   input in order to interrupt the live feed at the
   desired time.

The third input and others will play one after the
other, one starting when the previous has
completed. 3. When the last file input becomes Active:

    * Optionally set an activate time to return
     to the live feed. Or omit an activate time
     and let the live feed resume when the last
     file has completed.
    * Prepare the live input you are returning
     to.

## Implementing use

case 3

Use case 3 is described [here](typical-use-cases.md#use-case-3 "typical-use-cases.md#use-case-3").

1. Create an event that has the live feed as the
   input.
2. Once the event starts, create a dynamic playlist
   that consists of the following:
   - Second input – a file that displays the
     desired content. Include the loop_source tag
     for this input in order to play the content
     repeatedly until it is time to return to the
     live input.
   - Third input – live input (identical to the
     first input).

3. If an unanticipated event occurs, switch to the
   second input: either use the REST API (Activate
   Dynamic Playlist Input) or let the operator manually
   activate this input using the web interface
   control.
4. When you want to resume live input, prepare the
   third input and then switch to the third
   input.
5. If another unanticipated event occurs, you can
   switch again to the second input.

## Implementing use

case 4

Use case 4 is described [here](typical-use-cases.md#use-case-4 "typical-use-cases.md#use-case-4").

1. Create an event that has the live feed as the input.
2. Once the event starts, create a dynamic playlist that
   consists of the following:
   - Second input – a live input from a different
     live source.

3. Follow the desired action:
   - Optionally set an activate time to return to
     the live feed. Or omit an activate time and let
     the live feed resume when the last file has
     completed. Or omit the activate time and
     manually switch to the second input: either use
     the REST API (Activate Dynamic Playlist Input)
     or let the operator manually activate the second
     input using the web interface control.
   - Prepare the live input you are returning to.

## Implementing use

case 5

Use case 5 is described [here](typical-use-cases.md#use-case-5 "typical-use-cases.md#use-case-5").

1.  Create an event that has the first file as the
    input. In the event, set loop_all_inputs to
    true.
2.  Once the event starts, create a dynamic playlist
    that consists of the following:
    - Second input – a file input.

3.  Once the second input has become Active:

        * Modify the first input to point to a
         different file source. Change other tags as
         required (for example, the audio
         selectors).
        * Optionally set an activate time for the
         first input.

    When the second input has ended, the first input
    will become Active again.

4.  Once the first input has become Active
    again:
    - Modify the second input to point to a
      different file source. Change other tags as
      required (for example, the audio
      selectors).
    - Optionally set an activate time for the
      second input.

5.  Repeat as required.

## Implementing use

case 6

Use case 6 is described [here](typical-use-cases.md#use-case-6 "typical-use-cases.md#use-case-6").

1. Create an event that has the live feed as the
   input.
2. Once the event starts, create a dynamic playlist
   that consists of the following:
   - Second input – a file input such as a
     movie. Include the input_clipper tags to
     clip content. For example, clip it to run
     from the 0 mark to the 20 minute
     mark.
   - Third input – ad content – from file.
   - Fourth input – file input identical to the
     second input. Include the input_clipper tags
     to clip content, for example, to clip it to
     run from the 20 minute mark to the 35 minute
     mark.
   - Fifth input – ad content – from file.
   - Continue switching between the movie and
     ads.
   - Finally, create a dynamic playlist to
     return to the live feed.

3. Let each input complete. The next input in the XML
   will automatically start.
4. When the last file input becomes Active:
   - Optionally set an activate time to return
     to the live feed. Or omit an activate time
     and let the live feed resume when the last
     file has completed.
   - Prepare the live input you are returning
     to.
