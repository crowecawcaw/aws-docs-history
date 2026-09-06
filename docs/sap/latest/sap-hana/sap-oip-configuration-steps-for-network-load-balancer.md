

# Configuration Steps for Network Load Balancer
<a name="sap-oip-configuration-steps-for-network-load-balancer"></a>

Use the following instructions to set up the Network Load Balancer to access the overlay IP address. The following values are used for the example configuration.

 **Table 1: System Settings** 


| System Setting | Value | 
| --- | --- | 
| Instance number for ASCS and SAP HANA | 00 | 
| OIP for ASCS | 192.168.0.20 | 
| OIP for HANA | 192.168.1.99 | 

 **Table 2: Listener Port Values** 


| Listener Ports | Value | 
| --- | --- | 
| ASCS Message server port | 36<instance number> (3600) | 
| SAP HANA | SAP HANA Studio service connection (login required) [SAP Note 1592925](https://me.sap.com/notes/1592925)  | 
| SAPStartSrv/HTTP Port | 5<instance number>13 (50013) | 
| JDBC/SQL Port | 3<instance number>15 (30015) | 

## Step 1. Create the target group
<a name="sap-oip-step-1.-create-the-target-group."></a>

1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/

1. On the navigation pane, under **LOAD BALANCING**, choose **Target Groups**.

1. Choose Create target group.

1. For **Name**, type an easily identified target group name for the sap-ascs instance. (For example, type sap-ascs for your ASCS overlay IP address).

1. For **Target type**, select **IP**.

1. For **Protocol**, choose **TCP**.

1. For **Port**, type 36<ASCS instance number>. For example: 3600, where 00 is the instance number.

1. For **Health checks**, keep the default health check settings, or change settings based on your requirements.

1. Choose **Create**.

1. Repeat steps 1 to 9 to create target group for JDBC/SQL port 3<instance number>15 and SAP HANA HTTP port 5<instance number>13 to access your SAP HANA instance with the respective overlay IP address.

1. Choose the **Targets** tab, then choose **Edit**.

1. Choose **Add** to register your targets.

1. Choose the **Network** drop-down and select **Other private IP address**. Then, enter the ASCS overlay IP address and choose **Add to list**.

1. Repeat steps 11 to 13 to register JDBC/SQL and HTTP ports with the respective overlay IP address.

## Step 2. Create the Network Load Balancer for ASCS
<a name="sap-oip-step-2.-create-the-network-load-balancer-for-ascs."></a>

1. On the EC2 navigation pane, under **LOAD BALANCING**, choose **Load Balancers**.

1. Choose Create Load Balancer.

1. For Network Load Balancer, choose Create.

1. For **Name**, type a name for your load balancer. For example, sap-ha-nlb.

1. For **Scheme**, choose **internal**. An internal load balancer routes requests to targets using private IP addresses.

1. For **Listeners**, under Protocol, choose **TCP**. For **Port**, specify the ASCS port (36< SAP Instance number>. For example, use 3600 if your SAP instance number is 00.

1. For **Availability Zones**, select the VPC and subnets where the SAP instances with HA setup are deployed.

1. For **Tags**, choose **Add Tags** and for Key, type Name. For Value, type the name of the network load balancer, such as sap-ha-nlb.

1. Choose Next: Configure Security Settings.

1. Ignore the warning that appears and choose **Next: Configure Routing**. (In this scenario, the network load balancer is used as pass through without any SSL termination. For end-to-end encryption, use SNC from SAP GUI to SAP Instance.)

1. For **Target group**, choose **Existing target group** and select the **sap-ascs** target group created earlier.

1. Choose **Next: Register Targets**.

1. Choose **Next: Review**.

1. Choose **Create**.

1. Repeat the steps 1 to 14 to create another Network Load Balancer for SAP HANA setup with Network Load Balancer TCP protocol listener to JDBC/SQL port 3<instance number>15. Choose VPC and the subnets where the primary and secondary SAP HANA database is deployed and register the target JDBC/SQL target group.

1. Add an additional listener to the Network Load Balancer created in step 14 with SAP StartSrv/HTTP port 5<instance number>13 listener port and register the target StartSrv/HTTP port target group.

## Step 3. Set up VPC routing table
<a name="sap-oip-step-3.-set-up-vpc-routing-table."></a>

This step enables the connection to your SAP instance.

1. Open the Amazon VPC console at https://console.aws.amazon.com/vpc/

1. In the navigation pane, choose **Route Tables**, and select the Amazon VPC routing table where your SAP instance is deployed.

1. Choose **Actions**, **Edit routes**.

1. For **Destination**, specify your overlay IP address. For **Target**, specify the SAP instance Elastic Network Interface.

1. Choose Save routes.

This setup allows the static Network Load Balancer DNS to forward the traffic to your SAP instance network interface through the static overlay IP address. During failover scenarios, you can point to the elastic network interface of the active SAP instance using manual steps or automatically using cluster management software.

## Step 4. Connect using SAP GUI
<a name="sap-oip-step-4.-connect-using-sap-gui."></a>

1. In the **Load Balancers** section of the EC2 console, make a note of the Network Load Balancer DNS name for the sap-ha-nlb.

    **Figure 7: sap-ha-nlb DNS name**   
![sap-ha-nlb DNS name](http://docs.aws.amazon.com/sap/latest/sap-hana/images/ha-overlay-ip-image7.png)

1. Start SAP Logon.

1. Choose **New**, then **Next**.

1. In the System Entry Properties box, for Connection Type, choose Group/Server Selection.

1. For **Message Server**, type the Network Load Balancer DNS name, and choose **OK**.

    **Figure 8: Configuring System Connection Parameters for SAP GUI**   
![Configuring System Connection Parameters for SAP GUI](http://docs.aws.amazon.com/sap/latest/sap-hana/images/ha-overlay-ip-image8.png)

## Step 5. Connect using SAP HANA Studio
<a name="sap-oip-step-5.-connect-using-sap-hana-studio."></a>

1. In the **Load Balancers** section of the EC2 console, make a note of the Network Load Balancer DNS name for the JBDC/SQL and SAPStartSrv/HTTP ports.

    **Figure 9: DNS name of ports**   
![DNS name of ports](http://docs.aws.amazon.com/sap/latest/sap-hana/images/ha-overlay-ip-image9.png)

1. In the Host Name parameter of SAP HANA Studio, use the Network Load Balancer DNS name and provide additional credentials to connect to the SAP HANA system.

    **Figure 10: Updated Host Name in SAP HANA Studio**   
![Updated Host Name in SAP HANA Studio](http://docs.aws.amazon.com/sap/latest/sap-hana/images/ha-overlay-ip-image10.png)