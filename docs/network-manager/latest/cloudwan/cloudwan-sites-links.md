# Sites and links in AWS Cloud WAN

After you've added any devices to your global network, you can create a Cloud WAN site and
associate any of your devices with that particular site using a link. For information on
adding devices, see [Devices in AWS Cloud WAN](cloudwan-devices.md "cloudwan-devices.md").

## Sites

A site represents the physical location of your network, using location information such
as latitude, longitude, and address. You can have multiple sites for each of your
network locations. Sites are useful when viewing the global network dashboard, which
provides you the geographical location of these sites based on location information you
provided. Once you create a site you can view the devices associated with the site and
create links between devices and sites. You can also view any VPNs associated with the
site as well as monitor CloudWatch metrics for this site.

## Links

A link represents the connection between a device and a site. Once you've added a
device and created a site, you can create an association between the device and a site.

###### Topics

- [Create a site](cloudwan-sites-add.md "cloudwan-sites-add.md")
- [View site details](cloudwan-sites-view.md "cloudwan-sites-view.md")
- [Update a site](cloudwan-sites-update.md "cloudwan-sites-update.md")
- [Delete a site](cloudwan-site-delete.md "cloudwan-site-delete.md")
- [Create a link](cloudwan-site-link-add.md "cloudwan-site-link-add.md")
- [Edit a device link](cloudwan-link-update.md "cloudwan-link-update.md")
- [Delete a link](cloudwan-link-delete.md "cloudwan-link-delete.md")
