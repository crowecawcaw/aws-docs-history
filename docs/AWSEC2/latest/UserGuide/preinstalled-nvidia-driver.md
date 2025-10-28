# Use AMIs that include NVIDIA drivers

AWS and NVIDIA offer different Amazon Machine Images (AMIs) that come with
the NVIDIA drivers installed.

- [Marketplace offerings with the Tesla public
  driver](https://aws.amazon.com/marketplace/search/results?page=1&filters=VendorId&VendorId=e6a5002c-6dd0-4d1e-8196-0a1d1857229b%2Cc568fe05-e33b-411c-b0ab-047218431da9&searchTerms=tesla+driver "https://aws.amazon.com/marketplace/search/results?page=1&filters=VendorId&VendorId=e6a5002c-6dd0-4d1e-8196-0a1d1857229b%2Cc568fe05-e33b-411c-b0ab-047218431da9&searchTerms=tesla+driver")
- [Marketplace offerings with the GRID
  driver](https://aws.amazon.com/marketplace/search/results?&searchTerms=NVIDIA+quadro "https://aws.amazon.com/marketplace/search/results?&searchTerms=NVIDIA+quadro")
- [Marketplace offerings with the Gaming
  driver](https://aws.amazon.com/marketplace/search/results?searchTerms=NVIDIA+gaming "https://aws.amazon.com/marketplace/search/results?searchTerms=NVIDIA+gaming")
  To review considerations that are dependent on your operating system (OS) platform,
  choose the tab that applies to your AMI.

Linux
To update the driver version installed using one of these AMIs, you
must uninstall the NVIDIA packages from your instance to avoid version
conflicts. Use this command to uninstall the NVIDIA packages:

```
`[ec2-user ~]$` sudo yum erase nvidia cuda
```

The CUDA toolkit package has dependencies on the NVIDIA drivers.
Uninstalling the NVIDIA packages erases the CUDA toolkit. You must reinstall the
CUDA toolkit after installing the NVIDIA driver.

Windows
If you create a custom Windows AMI using one of the AWS Marketplace
offerings, the AMI must be a standardized image created with
Windows Sysprep to ensure that the GRID driver works. For more
information, see [Create an Amazon EC2 AMI using Windows Sysprep](ami-create-win-sysprep.md "ami-create-win-sysprep.md").
