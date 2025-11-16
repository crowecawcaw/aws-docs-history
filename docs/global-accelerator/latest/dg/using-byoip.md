# Advertise the address range through AWS

After the address range is provisioned, it's ready to be advertised. You must advertise the
exact address range that you provisioned. You can't advertise only a portion of the
provisioned address range. In addition, you must stop advertising your IP address range from other
locations before you advertise it through AWS.

You must advertise (or stop advertising) your address range using the CLI or Global Accelerator API operations.
This functionality is not available in the AWS console.

###### Important

Make sure that your IP address range is advertised by AWS before you use an IP address from
your pool with Global Accelerator.

To advertise the address range, use the following [AdvertiseByoipCidr](../api/API_AdvertiseByoipCidr.md "../api/API_AdvertiseByoipCidr.md")
command.

```
`aws globalaccelerator --region us-west-2 advertise-byoip-cidr --cidr `address-range``
```

The following is an example of requesting Global Accelerator to advertise an address range.

```
`aws globalaccelerator --region us-west-2 advertise-byoip-cidr --cidr 203.0.113.0/24`
```

To monitor the state of the address ranges that you've advertised, use the following
[ListByoipCidrs](../api/API_ListByoipCidrs.md "../api/API_ListByoipCidrs.md")
command.

```
`aws globalaccelerator --region us-west-2 list-byoip-cidrs`
```

When your IP address range is advertised, the `State` returned by `list-byoip-cidrs`
is `ADVERTISING`. For example:

```
{
    "ByoipCidrs": [
        {
            "Cidr": "203.0.113.0/24",
            "State": "ADVERTISING"
        }
    ]
}
```

To stop advertising the address range, use the following `withdraw-byoip-cidr`
command.

###### Important

To stop advertising your address range, you first must remove any accelerators that have static
IP addresses that are allocated from the address pool. To delete an
accelerator using the console or using API operations, see [Delete accelerator](about-accelerators.md "about-accelerators.md").

```
`aws globalaccelerator --region us-west-2 withdraw-byoip-cidr --cidr `address-range``
```

The following is an example of requesting Global Accelerator to withdraw an address range.

```
aws globalaccelerator --region us-west-2 withdraw-byoip-cidr
    --cidr 203.0.113.0/24

```
