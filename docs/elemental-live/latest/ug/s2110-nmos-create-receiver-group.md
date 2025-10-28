# Create the receiver group

You must create the SMPTE 2110 receiver groups that you need. Each receiver group
identifies the set of individual streams of video, audio, and ancillary data (captions
and SCTE 104 messages) that you want to treat as one input.

1.  In the Elemental Live web interface, hover over **Settings** and choose
    **Input Devices**. Scroll down to the **SMPTE 2110
    Receiver Groups** section.
2.  Choose **Create SMPTE 2110 Receiver Groups**. Fields
    appear.
3.  In **NMOS SMPTE 2110 Input**, enter a name for the receiver
    group. This name will appear in the dropdown list of inputs when you create an
    Elemental Live event or Conductor Live profile.
4.  Adjust the remaining fields to match your requirements. The receiver group must
    include one video stream. But the audio and ancillary streams are optional.

        * Click **Add Audio SDP** to add one or more rows for
         audio streams. Or click **Remove** if you don't want any
         audio in the input.
        * Click **Add Ancillary SDP** to add one or more rows for
         ancillary streams (captions and SCTE-104 streams).

    Following example 1 above, you will three audio SDPs, and two ancillary
    SDPs.

Following example 2 above, you will one audio SDP, and two ancillary
SDPs. 5. Complete each stream row as follows:

    * **Label**: Enter a description. For example, in the
     video stream, enter `vid_rx`.


    Elemental Live will combine the receiver group name and the label to create a name
     for the stream that is unique to that system.
    * **Interface**: Enter the network interface for this
     stream to connect to the Elemental Live node. For example,
     `eth4`.
    * **Secondary Interface**: If you want to implement SMPTE
     2022-7 , enter the interface for the secondary source. For example,
     `eth5`.
    * **GUID**: This field is auto-populated with a
     system-generated value. You might want to change this value, for example, to
     make it match values you created outside of Elemental Live. To change the value,
     choose **Show Advanced** and enter the new value.

6.  Follow this step only if you are using Conductor Live. You must import the SMPTE 2110
    receiver group input into Conductor Live.

        * On the primary Conductor Live web interface, choose the
         **Cluster** page, then choose
         **Nodes**.
        * Choose the down arrow beside the node and select **Import
         Devices**.

    You will now be able to use this input when you create a channel in Conductor Live. The
    names of all the imported SMPTE 2110 inputs will appear in the list of
    devices.
