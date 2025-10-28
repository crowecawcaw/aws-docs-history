# Create, modify, or delete a traffic mirror session

A traffic mirror session establishes a relationship between a traffic mirror source and a
traffic mirror target. For more information, see [Understand traffic mirror session concepts](traffic-mirroring-sessions.md "traffic-mirroring-sessions.md").

You can create a traffic mirror session only if you are the owner of the network interface
or the subnet for the traffic mirror source.

###### To create, modify, or delete a traffic mirror session using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the **Region** selector, choose the AWS Region that you used
   when you created the VPCs.
3. In the navigation pane, choose **Traffic Mirroring**, **Mirror
   sessions**.
4. Select the traffic mirror session, and then choose **Actions**,
   **Delete**.
5. When prompted for confirmation, enter `delete`, and then choose
   **Delete**.
6. To modify a session, select the radio button for the traffic mirror session.
7. Choose **Actions**, **Modify session**.
8. To create a session, choose **Create traffic mirror session**.
9. (Optional) For **Name tag**, enter a name for the traffic mirror
   session.
10. (Optional) For **Description**, enter a description for the traffic mirror
    session.
11. For **Mirror source**, choose the network interface of the mirror
    source.
12. For **Mirror target**, choose an existing traffic mirror target or
    choose **Create target** to create one. For more information, see
    [Create or delete a traffic mirror target](create-traffic-mirroring-target.md "create-traffic-mirroring-target.md").

If the mirror target is owned by another account and shared with you, you must
first [accept the resource share](tm-share-accept.md "tm-share-accept.md"). 13. For **Additional settings**, do the following:

    1. For **Session number**, enter the session number. The valid
     values are 1 to 32,766, where 1 is the highest priority. Sessions are evaluated
     based on the priority indicated by this session number.
    2. (Optional) For **VNI**, enter the VXLAN ID to use for the traffic mirror
     session. For more information about the VXLAN protocol, see [RFC 7348](https://tools.ietf.org/html/rfc7348 "https://tools.ietf.org/html/rfc7348").


    If you do not enter a value, we assign a random number.
    3. (Optional) For **Packet Length**, enter the number of bytes in
     each packet to mirror.


    To mirror the entire packet, do not enter a value. To mirror only a portion of
     each packet, set this value to the number of bytes to mirror. For example, if you
     set this value to 100, the first 100 bytes after the VXLAN header that meet the
     filter criteria are copied to the target.
    4. For **Filter**, choose an existing traffic mirror filter.
     Alternatively, choose **Create filter**. For more information,
     see [Step 2: Create the traffic mirror
     filter](traffic-mirroring-getting-started.md#step-create-traffic-mirroring-filters "traffic-mirroring-getting-started.md#step-create-traffic-mirroring-filters").

14. (Optional) For each tag to add, choose **Add new tag** and enter the tag key
    and tag value.
15. If you're modifying a session, choose **Modify**. If you're creating a session, choose **Create**.

###### To create a traffic mirror session using the AWS CLI

Use the [create-traffic-mirror-session](../../../cli/latest/reference/ec2/create-traffic-mirror-session.md "../../../cli/latest/reference/ec2/create-traffic-mirror-session.md") command.
