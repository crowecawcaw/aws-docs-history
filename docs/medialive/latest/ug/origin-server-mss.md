# Coordinate with the downstream system

You and the operator of the downstream system must agree about the destination for the
output of the Microsoft Smooth output group.

1. Decide if you need two destinations for the output:
   - You need two destinations in a [standard channel](plan-redundancy.md "plan-redundancy.md").
   - You need one destination in a single-pipeline channel.

2. Talk to the operator at the Microsoft IIS server to agree on a full path for
   the output. Make a note of the URLs that you agree on. For example:

`https://203.0.113.55/sports/curling`

`https://203.0.113.82/sports/curling` 3. Arrange with the operator to set up user credentials, if the protocol is
HTTPS. 4. Find out if the downstream system has special connection requirements. These
connection fields are in the **General configuration** section
for the Microsoft Smooth output group. To display this page on the MediaLive
console, in the **Create channel** page, in
**Output groups** section, choose
**Add**, then choose **Microsoft Smooth**.
Choose the group, then in **Microsoft Smooth
settings**, open **General configuration**.
