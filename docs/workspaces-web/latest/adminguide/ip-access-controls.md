# Managing IP access controls in Amazon WorkSpaces Secure Browser

###### Important

IP access controls only support IPv4. Users connecting from IPv6-only networks will be blocked.

WorkSpaces Secure Browser allows you to control which IP addresses your web portal can be accessed from. By
using IP access settings, you can define and manage groups of trusted IP addresses, and only
allow users to access their portal when they're connected to a trusted network.

By default, WorkSpaces Secure Browser allows users to access their web portal from anywhere. An IP access
control group acts as a virtual firewall that filters which IP address a user can use to connect
to the web portal. When associated with your web portal, IP access settings will detect the user
IP before authentication to determine whether they are eligible to connect. Once connected, WorkSpaces Secure Browser
continuously monitors a user's IP address to ensure they remain connected from a trusted network.
If a user's IP changes, WorkSpaces Secure Browser will detect and terminate the session.

To specify the CIDR address ranges, add rules to your IP access control group, and then
associate the group with your web portal. You can associate each IP access setting with one or
more web portals. To specify the public IP addresses and ranges of IP addresses for your trusted
networks, add rules to your IP access control groups. If your users access their web portal
through a NAT gateway or VPN, you must create rules that allow traffic from the public IP
addresses for the NAT gateway or VPN.

###### Note

Customers are responsible for understanding the potential legal issues that arise with
their use of WorkSpaces Secure Browser, and must ensure that their use of WorkSpaces Secure Browser complies with all
applicable laws and regulations. This includes laws that regulate an employer's ability to
monitor an employee's use of WorkSpaces Secure Browser, including activities performed within the
application.

###### Topics

- [Creating an IP access control group in Amazon WorkSpaces Secure Browser](create-ip-access-controls.md "create-ip-access-controls.md")
- [Associating an IP access setting with a web portal in Amazon WorkSpaces Secure Browser](associate-ip-access-controls.md "associate-ip-access-controls.md")
- [Editing an IP access control group in Amazon WorkSpaces Secure Browser](edit-ip-access-controls.md "edit-ip-access-controls.md")
- [Deleting an IP access control group in Amazon WorkSpaces Secure Browser](delete-ip-access-controls.md "delete-ip-access-controls.md")
