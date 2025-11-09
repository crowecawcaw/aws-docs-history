# Requirements for the appliance and network

A SMPTE 2110 input or output requires an Elemental Live appliance with a high-speed network
interface card (NIC). Therefore, to set up a SMPTE 2110 input or output, you must create
the event on one of the following appliances.

| Appliance                            | Network interface card (NIC)                                                                       | Scope of support for SMPTE 2110 | Support for NMOS |
| ------------------------------------ | -------------------------------------------------------------------------------------------------- | ------------------------------- | ---------------- |
| L800 series Elemental Live appliance | 25 GbE NIC                                                                                         | Inputs and outputs              | Supported        |
| A bare-metal appliance               | 25 GbE Mellanox NIC. You must make sure that the NIC is licensed for use<br>with the RiverMax SDK. | Inputs and outputs              | Supported        |
