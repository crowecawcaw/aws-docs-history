

# Install custom fonts on Deadline Cloud Linux workers
<a name="examples-host-config-fonts"></a>

The [linux\_font\_installation](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/host_configuration_scripts/linux_font_installation) host configuration script on the GitHub website installs fonts from an Amazon S3 bucket on Deadline Cloud Linux service-managed fleet workers, which makes the fonts available to applications such as Nuke.

**Note**  
Fonts may render differently across operating systems.

To use this script:

1. Upload your font files to an Amazon S3 bucket. To save time at instance startup, store fonts in a dedicated folder so the script copies only font files.

   ```
   aws s3 cp {{/path/to/your/fonts/}} s3://{{your-bucket-name}}/Fonts/ --recursive
   ```

1. Edit `font_install_host_config.sh` to set `S3_FONTS_URI` and `JOB_USER`.

1. Add an IAM policy to your fleet IAM role that grants `s3:GetObject` and `s3:ListBucket` permissions for the bucket and prefix.