# Step C: Add the router

Perform this procedure on the primary Conductor Live node.

1. On the web interface for the primary Conductor Live node, go to the
   **Settings** page and choose
   **Routers**.
2. On the **Routers** page, choose **Add Router** and
   select the type of router protocol. These are the available options:
   - Videohub Ethernet Protocol (previously BlackMagic VideoHub)
   - XY Terminal Protocol (previously Harris Panacea)
   - NV9000 Protocol (previously Miranda nVision)
   - SW-P-08 Protocol (previously Snell Aurora)
   - PassThrough Protocol
   - LRC Protocol

3. Complete the **Add New Router** fields as
   described in the table and choose **Add**.

| Field          | Description                                                                   |
| -------------- | ----------------------------------------------------------------------------- |
| **Name**       | The name that appears in the \*_Inputs_<br>• field on events and<br>profiles. |
| **IP Address** | The IP address of the router, excluding the protocol.                         |
| **Level**      | Applies to the XY Terminal, NV9000, SW-P-08, and<br>PassThrough.              |
| **User**       | Applies to the NV9000.                                                        |
| **Matrix ID**  | Applies to the SW-P-08.                                                       |
