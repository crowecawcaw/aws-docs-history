# Creating the output

1.  In the Elemental Live event, go to **Output
    Groups** > **Reliable TS**.
2.  Choose **Add Output** to create an output in
    this Reliable TS output group.
3.  Complete the fields in each output as follows:

        * **Delivery Protocol**: Zixi
        * **Destination/Amazon Resource Name**:
         Enter the IP address (that you obtained from the operator
         of the downstream system), a colon, and the port (default
         is 2088). For example:



        ```
        zixi://198.51.100.0:2088
        ```
        * **Interface**: Optional. See the
         tooltip.
        * If the downstream system requires that you authenticate,
         obtain the username and password from them. Then choose the
         **Lock** icon and complete the fields
         that appear.




        	+ **Username/Access Key ID**: The
        	 username.
        	+ **Password/Secret Access Key**:
        	 The password.
        * **Stream ID**: Enter the stream ID that
         you and the operator of the downstream system agreed on. It
         is required.
        * **Latency**: See the tooltip.
        * **Encryption**: Choose
         **None**, or choose an algorithm. The
         downstream system must support the algorithm you
         choose.
        * **Key Value:** Enter the encryption key
         that you and the operator of the downstream system agreed
         on. See the tooltip.

    Repeat the preceding steps to create a second output in this output
    group, if applicable. Use the same user name and password. You can also
    use the same encryption key, if you are encrypting.
