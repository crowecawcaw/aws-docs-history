# Step 3: Set up the inputs in the event

###### To set up an MPTS program

You must set up each program in the MPTS as an individual input.

You can use inputs from an MPTS with both asynchronous input switching
and SCTE-35-triggered input switching.

###### Note

The information in this section assumes that you are familiar with
the general steps for creating an event.

1. On the web interface, got to the **Inputs** section
   of the event.
2. Complete the **Input** section as follows:
   - **Input Type**: Choose Network Input.
   - **Input Name**: Enter the label for the input,
     obtained from the POIS operator.
   - **Network Location**: The URL of the MPTS. For
     example, udp://192.20.08.18:5001

3. Open the **Advanced** section of this input and
   complete the following fields (on the first line of fields)
   - **Virtual Input**: Choose this field to set up the
     input as a virtual input. Elemental Live notifies the POIS only about
     inputs that are configured as virtual inputs.
   - **Virtual Input SCTE 35 PID**: Enter the PID in
     the MPTS that holds the SCTE-35 data stream. You complete this field
     only if you are using this program with SCTE-35-triggered input
     switching. This is the PID that Elemental Live probes for SCTE-35
     messages to send to the POIS.

4. Go to the **Video Selector** section of this input
   and complete the following fields:
   - **Program**, in **Video
     Selector**: Enter the program number of the individual program
     in the mpts.

5. Set up the audio and captions for this MPTS in the usual way.
6. Set up more inputs, for other programs in the MPTS. For all the
   inputs, these rules apply:
   - The URLs must be identical, because the programs must all be in the
     same MPTS.
   - The Input names must each be different.
   - The Program (in the Video Selector) must each be different.

###### To set up a file input

You can use file inputs with asynchronous input switching. You can't
use them with SCTE-35-triggered input switching.

###### Note

The information in this section assumes that you are familiar with
the general steps for creating an event.

1. On the web interface, got to the **Inputs** section
   of the event.
2. Complete the **Input** section as follows:
   - **Input Type**: Choose File Input or HLS File
     Input.
   - **Input Name**: Enter the label for the input,
     obtained from the POIS operator.
   - **File Location**: The path and file name for the
     source. For example, ftp://vod_files/mlaw.wav

3. Open the **Advanced** section of this input and
   complete the fields as follows:
   - **Virtual Input**: Choose this field to set up the
     input as a virtual input. Elemental Live notifies the POIS only about
     inputs that are configured as virtual inputs.
   - **Virtual Input SCTE 35 PID**: Ignore this field.
     It is used only with SCTE-35-triggered input switching.
