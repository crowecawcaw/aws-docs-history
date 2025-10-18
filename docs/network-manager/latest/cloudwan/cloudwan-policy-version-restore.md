# Restore an out-of-date AWS Cloud WAN core network policy
 version

An out-of-date policy can be restored as a new version of a policy. 

###### To restore an out-of-date policy version

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global Networks**.
3. On the **Global networks** page, choose the global network ID.
4. In the navigation pane, choose **Core network**, and then
 choose **Policy versions**.
5. Under **Policy version ID**, choose the out-of-date policy
 version that you want to restore, and then choose
 **Restore**.


The **Policy version ID** is incremented by one from the last
 version listed on the **Policy versions** page, and the
 **Change set state** displays as **Pending
 generation.**


When generated, the **Change set state** changes to
 **Ready to execute**, and the **Alias**
 changes to **LATEST**. If any previous policies were in the
 **Ready to execute** change set state, those change to
 **Out of date**. This indicates that those policies are now
 considered older than the **LATEST**.
