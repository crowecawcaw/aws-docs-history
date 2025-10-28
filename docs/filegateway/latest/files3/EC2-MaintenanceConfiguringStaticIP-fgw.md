# Configuring your Amazon EC2 gateway

network settings

You can view and configure the network settings for your Amazon EC2 File Gateway by using the gateway local
console.

###### To configure your network settings

1. Log in to the local console on your Amazon EC2 File Gateway. For instructions, see [Logging in to your Amazon EC2 gateway
   local console](EC2_MaintenanceConsoleWindow-fgw.md "EC2_MaintenanceConsoleWindow-fgw.md").
2. From the **AWS Appliance Activation - Configuration** main
   menu, enter the corresponding numeral to select **Network
   Configuration**.
3. From the **AWS Appliance Activation - Network
   Configuration** menu, enter the corresponding numeral for the task
   that you want to perform:
   - **Edit DNS Configuration** - The gateway local console displays the available adapters
     for the primary and secondary DNS servers. The console then prompts
     you to provide the new IP address.
   - **View DNS Configuration** - The gateway local console displays the available adapters
     for the primary and secondary DNS servers.
   - **Configure Hostname** - The gateway local console prompts you to choose
     whether the gateway will use a static hostname that you specify, or
     if it will aquire a hostname automatically through DCHP or rDNS.

   ###### Note

   If you choose to configure a static hostname for your gateway, you must
   create an A record in your DNS system that points the IP address of the gateway
   to its static hostname.
   - **View Hostname Configuration** - The gateway local console displays
     hostname, aquisition mode, domain, and Active Directory realm for your Amazon EC2 File Gateway.
