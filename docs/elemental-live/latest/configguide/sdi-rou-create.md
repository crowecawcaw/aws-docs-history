# Step B: Create the router

Create the router on the Elemental Live node.

###### To create the router

1. On the Elemental Live web interface, hover over
   **Settings**, and choose **Routers**.
2. On the **Routers** screen, choose **New Router** and
   select the type of router protocol. These are the available options:
   - Videohub Ethernet Protocol (previously BlackMagic VideoHub)
   - XY Terminal Protocol (previously Harris Panacea)
   - NV9000 Protocol (previously Miranda nVision)
   - SW-P-08 Protocol (previously Snell Aurora)
   - Pass-Through Protocol
   - LRC Protocol

3. Complete the **Add New Router** fields as described in the table and
   choose **Create**.

| Field           | Description                                                                   |
| --------------- | ----------------------------------------------------------------------------- |
| **Name**        | The name that appears in the \*_Inputs_<br>• field on events and<br>profiles. |
| **IP Address**  | The IP address of the router, excluding the protocol.                         |
| **Max Inputs**  | Typically, the number of physical inputs on the router.                       |
| **Max Outputs** | Typically, the number physical outputs on the router.                         |
| **Level**       | Available for XY Terminal, NV9000, SW-P-08, and Pass-Through.                 |
| **User**        | Available for NV9000.                                                         |
| **Matrix ID**   | Available for SW-P-08                                                         |
