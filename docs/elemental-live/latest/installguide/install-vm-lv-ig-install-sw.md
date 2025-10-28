# Step C: Install the

Elemental Live software

###### Topics

- [About Installer
  Options](#install-live-vm-about-options "#install-live-vm-about-options")
- [Setting up OCR
  Conversion in Versions 2.22.0 to 2.23.0](#install-live-vm-ocr2200-option "#install-live-vm-ocr2200-option")
- [Setting up OCR
  Conversion in Versions 2.23.1 and later](#install-live-vm-ocr2231-option "#install-live-vm-ocr2231-option")
- [The Install
  Procedure](#install-live-vm-procedure "#install-live-vm-procedure")

## About Installer

Options

To install Elemental Live, you run the installer. The installer
has options that control the way the installer works:

- _Action options_ instruct the installer to perform an action.
  For example, `--cleandb` instructs the
  installer to clean out the database.
- _Skip options_ instruct the installer to omit specific
  prompts. For example, `--skip-tz` instructs
  the installer to skip the timezone prompt.

To display built-in help about all the options, log in with
the _elemental_ user credentials, then enter
this command at the Linux command line:

```
[elemental@hostname ~]$ sudo sh ./elemental_live_cpu_2.25.4.12345.run --help
```

### The skip-all

Installer Option

The installer has a `--skip-all` option that
skips all the prompts and performs the default choice for
all options.

You should only use this option after you have followed
the following procedure, and you have read the built-in help
carefully.

The `--skip-all` option means that the
installer won't present prompts. It will perform some
actions using default information.

## Setting up OCR

Conversion in Versions 2.22.0 to 2.23.0

The installer for Elemental Live versions 2.22.0 to 2.23.0
includes an option to set up the feature to convert captions
using OCR conversion. (For information about the OCR feature,
see [Support
for OCR Conversion](../ug/support-for-ocr.md "../ug/support-for-ocr.md") in the _AWS Elemental Live User
Guide_.)

**To set up this feature**

###### Note

The Elemental Live node must have a connection to the
internet. It needs this connection because the installer
must download the OCR libraries from the internet. These
libraries are language dictionaries used in the
conversion.

If the node doesn't have an internet connection,
consider upgrading to a version after version 2.23.0. Newer
versions of Elemental Live include more options for
installing the OCR feature.

Run the installer with these options:

- With the `--install-ocr` option. You
  won't be presented with prompts to set up OCR.
  Instead, the installer will automatically set it
  up.
- You can include or omit the `--skip-all`
  option, depending on whether you want to be presented
  with prompts for other features.

**To omit the feature**

If you don't want to set up this feature, run the
installer with these options:

- Without the `--install-ocr` option. The
  installer won't set up the OCR feature.
- You can include or omit the `--skip-all`
  option.

## Setting up OCR

Conversion in Versions 2.23.1 and later

The installer for Elemental Live version 2.23.1 and later
includes several options to set up the feature to convert
captions using OCR conversion. (For information about the OCR
feature, see [Support
for OCR Conversion](../ug/support-for-ocr.md "../ug/support-for-ocr.md") in the _AWS Elemental Live User
Guide_.)

Setting up this feature involves three steps:

- Downloading the OCR libraries from the internet. These
  libraries are language dictionaries used in the
  conversion
- Installing the libraries on the node
- Enabling the OCR feature

**To set up the feature on a node with
access to the internet**

Run the installer with these options:

- With the `--install-ocr` option. The
  installer will download the libraries from the internet,
  install them on the node, and enable the OCR feature.
  You won't be presented with prompts to set up
  OCR.
- You can include or omit the `--skip-all`
  option, depending on whether you want to be presented
  with prompts for other features.

**To set up the feature on a node without
internet access**

1. Download the OCR libraries file [live-ocr-tesseract-data.zip](http://d3v4cjmjhvrkiz.cloudfront.net/live-ocr-tesseract-data.zip "http://d3v4cjmjhvrkiz.cloudfront.net/live-ocr-tesseract-data.zip")

Don't unzip the file after you download
it. 2. Use SCP to move the zipped file to a location on the
Elemental Live node that you are setting up. For example,
move to this location:

`/home/live-ocr-tesseract-data.zip` 3. Run the installer with these options:

    * With the `--install-ocr-zip`
     option. This option includes a parameter for the
     folder where you copied the libraries file. For
     example:


    `-- install-ocr-zip
     /home/live-ocr-tesseract-data.zip`


     You won't be presented with prompts to
     set up OCR.
    * You can include or omit the
     `--skip-all` option, depending on
     whether you want to be presented with prompts
     for other features.

**To omit the feature**

If you don't want to set up this feature, run the
installer with these options:

- Without the `--install-ocr` option. The
  installer won't install or enable the OCR
  feature.
- With the `--skip-ocr` option. If you
  don't include this option, you will be presented
  with prompts to install OCR, even though you didn't
  include the `--install-ocr` option.
- You can include or omit the `--skip-all`
  option, depending on whether you want to be presented
  with prompts for other features.

## The Install

Procedure

1. Use SCP to move each Elemental Live software installer
   (`.run` file) to the
   /home/elemental directory on the appropriate virtual
   machine. Use the _elemental_ user
   credentials.
2. From the VMware vSPhere client, choose **Open
   Console** and access the VM with the
   _elemental_ user
   credentials.

You are logged in at the home directory
(/home/elemental). 3. Decide which options you want to include with the
installer. You can include options in the command to
automate some of the installation. To display built-in
help about all the options, enter this command:

```
[elemental@hostname ~]$ sudo sh ./elemental_live_cpu_2.25.4.12345.run --help
```

4. Run the installer as follows. Use the actual file name
   of your `.run` file, rather than the
   example below.

```
[elemental@hostname ~]$ sudo sh ./elemental_production_live_2.25.4.12345.run  `options`
```

5. Follow the prompts. This table specifies the prompts
   that appear when you don't include any options for the
   installer.

| Prompt                                                                              | Action                                                                                                                                                                                                                                                         |
| ----------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Do you agree to these terms`                                                       | This prompt appears after you have paged through the EULA (End User License Agreement). Enter `Yes` or `No`. (You must enter Yes to continue.)                                                                                                                 |
| `Enter this server's Hostname`                                                      | Type the hostname of this hardware unit. For example, `live-01`                                                                                                                                                                                                |
| `Would you like to configure eth1`                                                  | If you type `No`, you can configure eth1 in the next phase of the configuration                                                                                                                                                                                |
| `The firewall for this system is currently disabled. Would you like to enable it?`  | If you type `No` you can set up the firewall in the next phase of the configuration                                                                                                                                                                            |
| `Is this machine a part of or intended to be a part of a Conductor Live 3 cluster?` | Type `Yes` or `No`                                                                                                                                                                                                                                             |
| `Will this machine require use of SNMP alerts?`                                     | Type `Yes` or `No`                                                                                                                                                                                                                                             |
| `Will this machine be ingesting RTMP?`                                              | Type `Yes` or `No`                                                                                                                                                                                                                                             |
| `Will this machine ingest MPEG-TS over UDP (ports 5000-5100)`                       | Type `Yes` or `No`                                                                                                                                                                                                                                             |
| `Will this machine serve files using Windows file-sharing (Samba/CIFS)?`            | Type `Yes` or `No`                                                                                                                                                                                                                                             |
| `Will this machine be an NTP server?`                                               | Type `Yes` or `No`                                                                                                                                                                                                                                             |
| `Enable conversion of eligible captions using OCR technology?`                      | Type `Yes` or `No`. For information about requirements for this feature, see [Setting up OCR Conversion in Versions 2.23.1 and later](install-lv-ig-install-sw.md#install-live-sw-ocr-2231 "install-lv-ig-install-sw.md#install-live-sw-ocr-2231").            |
| `Select time zone ('n' for more)`                                                   | Enter the time zone you want to show on the web interface of the nodes. This setting does not affect activity via SSH or via the REST API.                                                                                                                     |
| `Do you wish to enable authentication?`                                             | Type `Yes` or `No` if you want to set up so that users must log in to use Elemental Live                                                                                                                                                                       |
| `For security purposes, we require that you change the default password.`           | This prompt is shown if you are still using the default password. We recommend that you create a strong password: <br>• Minimum 8 characters <br>• At least one uppercase letter, at least one lowercase letter, at least one number, and at least one symbol. |
| `Would you like to start the Elemental service now?`                                | Type `Yes`                                                                                                                                                                                                                                                     | The software is installed. Finally, this message appears: `Installation and configuration complete!` 6. Take a snapshot of the VM, as described in the CentOS 7 Virtual Manager online help. 7. Start a web browser and start the Elemental Live web interface by typing the following: `https://<hostname>` Make sure the web interface displays. |
