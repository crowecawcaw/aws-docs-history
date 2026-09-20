

# Step C: Install the Elemental Live software
<a name="install-lv-ig-install-sw"></a>

Perform these steps on each AWS Elemental Live hardware unit, either directly at the hardware unit or from your workstation via SSH. 

**Topics**
+ [About Installer Options](#install-live-sw-about-options)
+ [Setting up OCR Conversion in Versions 2.22.0 to 2.23.0](#install-live-sw-ocr-2220)
+ [Setting up OCR Conversion in Versions 2.23.1 and later](#install-live-sw-ocr-2231)
+ [Installing the Software](#install-live-sw-procedure)

## About Installer Options
<a name="install-live-sw-about-options"></a>

To install Elemental Live, you run the installer. The installer has options that control the way the installer works:
+ *Action options *instruct the installer to perform an action. For example, `--cleandb` instructs the installer to clean out the database.
+ *Skip options *instruct the installer to omit specific prompts. For example, `--skip-tz` instructs the installer to skip the timezone prompt.

To display built-in help about all the options, log in with the *elemental* user credentials, then enter this command at the Linux command line:

```
[elemental@hostname ~]$ sudo sh ./elemental_live_cpu_2.25.4.12345.run --help
```

### The skip-all Installer Option
<a name="install-live-sw-skip-all"></a>

The installer has a `--skip-all` option that skips all the prompts and performs the default choice for all options.

You should only use this option after you have followed the following procedure, and you have read the built-in help carefully.

The `--skip-all` option means that the installer won't present prompts. It will perform some actions using default information.

## Setting up OCR Conversion in Versions 2.22.0 to 2.23.0
<a name="install-live-sw-ocr-2220"></a>

The installer for Elemental Live versions 2.22.0 to 2.23.0 includes an option to set up the feature to convert captions using OCR conversion. (For information about the OCR feature, see [Support for OCR Conversion](https://docs.aws.amazon.com/elemental-live/latest/ug/support-for-ocr.html) in the *AWS Elemental Live User Guide*.)

**To set up this feature**

**Note**  
The Elemental Live node must have a connection to the internet. It needs this connection because the installer must download the OCR libraries from the internet. These libraries are language dictionaries used in the conversion.  
If the node doesn't have an internet connection, consider upgrading to a version after version 2.23.0. Newer versions of Elemental Live include more options for installing the OCR feature.

Run the installer with these options: 
+ With the `--install-ocr` option. You won't be presented with prompts to set up OCR. Instead, the installer will automatically set it up.
+ You can include or omit the `--skip-all` option, depending on whether you want to be presented with prompts for other features.

**To omit the feature**

If you don't want to set up this feature, run the installer with these options:
+ Without the `--install-ocr` option. The installer won't set up the OCR feature. 
+ You can include or omit the `--skip-all` option.

## Setting up OCR Conversion in Versions 2.23.1 and later
<a name="install-live-sw-ocr-2231"></a>

The installer for Elemental Live version 2.23.1 and later includes several options to set up the feature to convert captions using OCR conversion. (For information about the OCR feature, see [Support for OCR Conversion](https://docs.aws.amazon.com/elemental-live/latest/ug/support-for-ocr.html) in the *AWS Elemental Live User Guide*.)

Setting up this feature involves three steps:
+ Downloading the OCR libraries from the internet. These libraries are language dictionaries that are used in the captions conversion.
+ Installing the libraries on the node.
+ Enabling the OCR feature.

**To set up the feature on a node with access to the internet**

Run the installer with these options:
+ With the `--install-ocr` option. The installer will download the libraries from the internet, install them on the node, and enable the OCR feature. You won't be presented with prompts to set up OCR.
+ You can include or omit the `--skip-all` option, depending on whether you want to be presented with prompts for other features.

**To set up the feature on a node without internet access**

1. Download the OCR libraries file [live-ocr-tesseract-data.zip](http://d3v4cjmjhvrkiz.cloudfront.net/live-ocr-tesseract-data.zip).

   Keep the file zipped.

1. Use a method such as SCP to move the zipped file to a location on the Elemental Live node that you are setting up. For example, move to this location:

   `/home/live-ocr-tesseract-data.zip`

1. Run the installer with these options:
   + With the `--install-ocr-zip` option. This option includes a parameter for the folder where you copied the libraries file. For example: 

     `-- install-ocr-zip /home/live-ocr-tesseract-data.zip`

      You won't be presented with prompts to set up OCR.
   + You can include or omit the `--skip-all` option, depending on whether you want to be presented with prompts for other features.

**To omit the feature**

If you don't want to set up this feature, run the installer with these options:
+ Without the `--install-ocr` option. The installer won't install or enable the OCR feature.
+ With the `--skip-ocr` option. If you don't include this option, you will be presented with prompts to install OCR, even though you didn't include the `--install-ocr` option.
+ You can include or omit the `--skip-all` option, depending on whether you want to be presented with prompts for other features.

## Installing the Software
<a name="install-live-sw-procedure"></a>

**To install the software**

1. At the Linux command line, log in with the *elemental* user credentials. 

1. Decide which options you want to include with the installer. You can include options in the command to automate some of the installation. To display built-in help about all the options, enter this command:

   ```
   [elemental@hostname ~]$ sudo sh ./elemental_live_cpu_2.25.4.12345.run --help
   ```

1. Run the installer as follows. Use the actual file name of your `.run` file, rather than the example below.

   For GPU and CPU versions of the software.

   ```
   [elemental@hostname ~]$ sudo sh ./elemental_production_live_2.25.4.12345.run  {{options}}
   ```

   For CPU-only versions of the software.

   ```
   [elemental@hostname ~]$ sudo sh ./elemental_production_live_cpu_2.25.4.12345.run {{options}}
   ```

1.  Follow the prompts. This table specifies the prompts that appear when you don't include any options for the installer.


<table>
<thead>
  <tr><th>Prompt</th><th>Action</th></tr>
</thead>
<tbody>
  <tr><td><code>Do you agree to these terms</code></td><td>This prompt appears after you have paged through the EULA (End User License Agreement).<br />Enter <b>Yes</b> or <b>No</b>. (You must enter Yes to continue.)</td></tr>
  <tr><td><code>Enter this server's Hostname</code></td><td>Type the hostname of this hardware unit. For example, <b>live-01</b></td></tr>
  <tr><td><code>Would you like to configure eth1</code></td><td>If you type <b>No</b>, you can configure eth1 in the next phase of the configuration</td></tr>
  <tr><td><code>The firewall for this system is currently disabled. Would you like to enable it?</code></td><td>If you type <b>No</b> you can set up the firewall in the next phase of the configuration</td></tr>
  <tr><td><code>Is this machine a part of or intended to be a part of a Conductor Live 3 cluster?</code></td><td>Type <b>Yes</b> or <b>No</b></td></tr>
  <tr><td><code>Will this machine require use of SNMP alerts?</code></td><td>Type <b>Yes</b> or <b>No</b></td></tr>
  <tr><td><code>Will this machine be ingesting RTMP?</code></td><td>Type <b>Yes</b> or <b>No</b></td></tr>
  <tr><td><code>Will this machine ingest MPEG-TS over UDP (ports 5000-5100)</code></td><td>Type <b>Yes</b> or <b>No</b></td></tr>
  <tr><td><code>Will this machine serve files using Windows file-sharing (Samba/CIFS)?</code></td><td>Type <b>Yes</b> or <b>No</b></td></tr>
  <tr><td><code>Will this machine be an NTP server?</code></td><td>Type <b>Yes</b> or <b>No</b></td></tr>
  <tr><td><code>Enable conversion of eligible captions using OCR technology?</code></td><td>Type <b>Yes</b> or <b>No</b>. For information about requirements for this feature, see <a href="#install-live-sw-ocr-2231">Setting up OCR Conversion in Versions 2.23.1 and later</a>.</td></tr>
  <tr><td><code>Select time zone ('n' for more)</code></td><td>Enter the time zone you want to show on the web interface of the nodes. This setting does not affect activity via SSH or via the REST API.</td></tr>
  <tr><td><code>Do you wish to enable authentication?</code></td><td>Type <b>Yes</b> or <b>No</b> if you want to set up so that users must log in to use Elemental Live</td></tr>
  <tr><td><code>For security purposes, we require that you change the default password.</code></td><td>This prompt is shown if you are still using the default password.<br />We recommend that you create a strong password:<ul><li> Minimum 8 characters </li><li> At least one uppercase letter, at least one lowercase letter, at least one number, and at least one symbol. </li></ul></td></tr>
  <tr><td><code>Would you like to start the Elemental service now?</code></td><td>Type <b>Yes</b></td></tr>
</tbody>
</table>


   When the software install is complete, this message appears:

   ```
   Installation and configuration complete!
   ```

1. Start a web browser and start the Elemental Live web interface by typing the following:

   ```
   https://<hostname>
   ```

   Make sure the web interface displays.