# Create a monitor in Internet Monitor using the console

You create a monitor in Internet Monitor to visualize and explore performance and availability data about your application's client traffic. 
 You create a monitor by adding AWS resources that your application uses, and then 
 setting several configuration options. The resources that you add to the monitor provide the information — for example, through
 resource flow logs — for Internet Monitor to learn which internet traffic is specific to your AWS application.

After you create your monitor, wait 15 to 30 minutes before reviewing the monitor dashboard. Internet Monitor needs a
 few minutes to generate a traffic profile for where your application is used by your end users, and 
 then to begin publishing data for your traffic.

Typically, it's simplest to create one monitor in Internet Monitor for one application. Within the same monitor, you can search through and 
 sort measurements and metrics by different locations and ASNs, or other information. You don't need to create separate 
 monitors for applications in different areas. 

The steps provided here walk you through setting up your monitor by using the console. To work with Internet Monitor API actions 
 using the AWS Command Line Interface, see 
 [Examples of using the CLI with Internet Monitor](CloudWatch-IM-get-started-CLI.md "CloudWatch-IM-get-started-CLI.md").

###### To create a monitor using the console

1. Open the CloudWatch console at
 [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the left navigation pane, under **Network Monitoring**, choose **Internet monitors**.
3. Choose **Create monitor**.
4. For **Monitor name**, enter the name that you want to use for this monitor.
5. Choose **Add resources**, and then select the resources that will determine the internet traffic profile
 for this monitor.


###### Note

Be aware of the following:



	* To generate meaningful output with Internet Monitor, VPCs that you add must be connected to the internet by having
	 an Internet Gateway configured.
	* You can specify only one type of resource for each monitor.
6. Choose a percentage of your application's internet traffic to monitor.
7. Optionally, under **Advanced settings**, specify one or more of the following additional options.




	* **City-networks maximum** — The default city-networks maximum value is `500000`. 
	 If you like, you can lower this limit, to restrict the number of city-networks (locations and ASNs) that Internet Monitor will monitor 
	 traffic for. You can change the city-networks maximum at any time by editing your monitor. For more information, 
	 see [Choose a city-networks maximum limit](IMCityNetworksMaximum.md "IMCityNetworksMaximum.md").
	* **Amazon S3 bucket storage** — You can specify an Amazon S3 bucket name and custom prefix to 
	 publish internet measurements for your application's internet traffic to Amazon S3, for all monitored city-networks. 
	
	
	Internet Monitor stores internet measurements for pairs of your client locations and ASNs, or *city-networks*. 
	 Internet Monitor also creates aggregated CloudWatch metrics for traffic to your application, and to each AWS Region and edge location.
	 In addition, Internet Monitor publishes internet measurements for your application traffic to CloudWatch Logs every five
	 minutes, to support using CloudWatch tools and other methods with your data. If you choose to publish measurements to S3, 
	 measurements are still published to CloudWatch Logs. For more information, 
	 see [Publish internet measurements to Amazon S3 in Internet Monitor](CloudWatch-IM-get-started.md "CloudWatch-IM-get-started.md").
	* **Tags** — Add one or more tags for your monitor.
8. Choose **Create monitor**.
After you create a monitor, wait about 15-30 minutes for Internet Monitor to create a traffic profile and begin publishing your data. Then,
 you can view information about your application's internet traffic performance by navigating to the monitor dashboard in the console.

###### To view the Internet Monitor dashboard

1. Open the CloudWatch console at
 [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Network Monitoring**, then **Internet monitors**.
3. To see more information about a specific monitor, on the **Monitors** tab, choose a monitor.
