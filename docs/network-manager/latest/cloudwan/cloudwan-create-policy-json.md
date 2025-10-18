# Create an AWS Cloud WAN core network policy version using JSON

You can create a core network policy by creating a JSON file. In the JSON editor, you add
 the parameters of your core network and policies. For a description of the required and
 optional parameters in the JSON file, see  [Core network policy version parameters in
 AWS Cloud WAN](cloudwan-policies-json.md "cloudwan-policies-json.md").


###### Note

Familiarity with creating JSON files is required.


###### To create a policy version using a JSON editor

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity** choose **Cloud WAN**.
3. On the **Global networks** page, choose the global network ID that for the core network you want to create a policy version for, and then choose **Core network**.
4. In the navigation pane, choose **Policy versions**.
5. Choose **Create policy version**.
6. In **Choose policy view mode**, choose
 **JSON**.
7. In the JSON editor, create your new policy. You can create a new policy
 version using a blank form, or copy and modify the contents of a policy version
 that you've downloaded.




	* For the required and optional parameters in your JSON policy, see
	  [Core network policy version parameters in
	 AWS Cloud WAN](cloudwan-policies-json.md "cloudwan-policies-json.md").
	* For the steps to download a previous policy version, see
8. Choose **Create policy**.


A new policy version is generated. 


The **Change set state** on the **Policy
 version** page displays **Pending generation**
 while the new policy generates. The state changes when the policy either
 generates successfully or fails to generate.

###### Topics

* [Core network policy version
 parameters](cloudwan-policies-json.md "cloudwan-policies-json.md")
* [Core network policy examples](cloudwan-policy-examples.md "cloudwan-policy-examples.md")
