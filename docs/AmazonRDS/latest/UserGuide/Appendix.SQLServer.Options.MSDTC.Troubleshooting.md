# Troubleshooting MSDTC for RDS for SQL Server

In some cases, you might have trouble establishing a connection between MSDTC running on a
client computer and the MSDTC service running on an RDS for SQL Server DB instance. If
so, make sure of the following:

- The inbound rules for the security group associated with the DB instance are configured correctly. For more information, see [Can't connect to Amazon RDS DB instance](CHAP_Troubleshooting.md#CHAP_Troubleshooting.Connecting "CHAP_Troubleshooting.md#CHAP_Troubleshooting.Connecting").
- Your client computer is configured correctly.
- The MSDTC firewall rules on your client computer are enabled.

###### To configure the client computer

1. Open **Component Services**.

Or, in **Server Manager**, choose
**Tools**, and then choose **Component
Services**. 2. Expand **Component Services**, expand
**Computers**, expand **My Computer**,
and then expand **Distributed Transaction
Coordinator**. 3. Open the context (right-click) menu for **Local DTC** and choose
**Properties**. 4. Choose the **Security** tab. 5. Choose all of the following:

    * **Network DTC Access**
    * **Allow Inbound**
    * **Allow Outbound**

6. Make sure that the correct authentication mode is chosen:
   - **Mutual Authentication Required** – The
     client machine is joined to the same domain as other nodes
     participating in distributed transaction, or there is a trust
     relationship configured between domains.
   - **No Authentication Required** – All other
     cases.

7. Choose **OK** to save your changes.
8. If prompted to restart the service, choose
   **Yes**.

###### To enable MSDTC firewall rules

1. Open Windows Firewall, then choose **Advanced settings**.

Or, in **Server Manager**, choose
**Tools**, and then choose **Windows Firewall
with Advanced Security**.

###### Note

Depending on your operating system, Windows Firewall might be called Windows Defender
Firewall. 2. Choose **Inbound Rules** in the left pane. 3. Enable the following firewall rules, if they are not already enabled:

    * **Distributed Transaction Coordinator (RPC)**
    * **Distributed Transaction Coordinator (RPC)-EPMAP**
    * **Distributed Transaction Coordinator (TCP-In)**

4. Close Windows Firewall.
