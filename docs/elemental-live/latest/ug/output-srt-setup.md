# Creating the output

The setup for the output is identical for both roles (caller or
listener), except for the **SRT Connection
Mode**

1. In the Elemental Live event, go to **Output
   Groups**, then to **Reliable
   TS**.
2. Choose **Add Output** to create an output in
   this Reliable TS output group.
3. Set **Delivery Protocol** to
   **SRT**.
4. Set **SRT Connection Mode** to the mode for
   Elemental Live—**Caller** or
   **Listener**.
5. Complete the fields for the primary destination:
   - **Primary Destination/Amazon Resource
     Name**: The IP address and port on the
     downstream system. For example:

   `srt://192.168.1.2:5000`
   - **Interface**: Optional. See the
     tooltip.
   - **Latency**: Enter the value that you
     decided to use.
   - **Encryption**: Choose
     **None**, or choose an level.
   - **Key Value /Passphrase:** If you chose
     an encryption level, enter the passphrase that you decided
     to use.

6. Complete the fields for the secondary destination, if you
   decided to deliver redundant streams.
