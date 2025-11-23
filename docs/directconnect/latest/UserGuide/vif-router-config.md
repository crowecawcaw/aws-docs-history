# Download the Direct Connect router configuration file

After you create the virtual interface and the interface state is up, you can download the
router configuration file for your router.

If you use any of the following routers for virtual interfaces that have MACsec
turned on, we automatically create the configuration file for your router:

- Cisco Nexus 9K+ Series switches running NX-OS 9.3 or later software
- Juniper Networks M/MX Series Routers running JunOS 9.5 or later
  software

###### To download the router configuration file

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home "https://console.aws.amazon.com/directconnect/v2/home").
2. In the navigation pane, choose **Virtual
   Interfaces**.
3. Select the virtual interface and then choose **View
   details**.
4. Choose **Download router configuration**.
5. For **Download router configuration**, do the
   following:
   1. For **Vendor**, select the manufacturer of your
      router.
   2. For **Platform**, select the model of your
      router.
   3. For **Software**, select the software version for
      your router.

6. Choose **Download**, and then use the appropriate
   configuration for your router to ensure that you can connect to
   Direct Connect.
7. If you need to manually configure your router for MACsec, use the following table as a
   guideline.

| Parameter               | Description                                                                                                            |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| CKN length              | This is a 64 hexadecimal character (0–9, A–E) string. Use the full<br>length to maximize cross-platform compatibility. |
| CAK length              | This is a 64 hexadecimal character (0–9, A–E) string. Use the full<br>length to maximize cross-platform compatibility. |
| Cryptographic algorithm | AES_256_CMAC                                                                                                           |
| SAK Cipher Suite        | • For 100 Gbps connections: GCM_AES_XPN_256<br>• For 10 Gbps connections: GCM_AES_XPN_256 or<br>GCM_AES \_256          |
| Key Cipher Suite        | 16                                                                                                                     |
| Confidentiality Offset  | 0                                                                                                                      |
| ICV Indicator           | No                                                                                                                     |
| SAK Rekey Time          | PN Rollover>                                                                                                           |
