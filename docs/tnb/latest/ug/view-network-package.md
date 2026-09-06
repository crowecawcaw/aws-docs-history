

# View a network package in AWS TNB
<a name="view-network-package"></a>

Learn how to view the content of a network package.

------
#### [ Console ]

**To view a network package using the console**

1. Open the AWS TNB console at [https://console.aws.amazon.com/tnb/](https://console.aws.amazon.com/tnb/).

1. In the navigation pane, choose **Network packages**.

1. Use the search box to find the network package.

------
#### [ AWS CLI ]

**To view a network package using the AWS CLI**

1. Use the [list-sol-network-packages](https://docs.aws.amazon.com/cli/latest/reference/tnb/list-sol-network-packages.html) command to list your network packages.

   ```
   aws tnb list-sol-network-packages
   ```

1. Use the [get-sol-network-package](https://docs.aws.amazon.com/cli/latest/reference/tnb/get-sol-network-package.html) command to view details about a network package.

   ```
   aws tnb get-sol-network-package \
   --nsd-info-id {{^np-[a-f0-9]{17}$}} \
   --endpoint-url "{{https://tnb.us-west-2.amazonaws.com}}" \
   --region {{us-west-2}}
   ```

------