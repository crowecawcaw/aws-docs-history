# Verify the authenticity of downloaded software

Verify your software's authenticity after downloading the installer to protect against
file tampering. This procedure works for both Windows and Linux systems.

Windows
To verify the authenticity of your downloaded files, complete the following
steps.

1. In the following command, replace
   `file` with the file that you want
   to verify. For example, ``C:\PATH\TO\MY\`DeadlineCloudSubmitter-windows-x64-installer.exe` . Also, replace
 ``signtool-sdk-version`` with the
   version of the SignTool SDK installed. For example,
   `10.0.22000.0`.

`"C:\Program Files (x86)\Windows
 Kits\10\bin\`signtool-sdk-version`\x86\signtool.exe"
 verify /v `file`` 2. For example, you can verify the Deadline Cloud submitter installer file by running
the following command:

`"C:\Program Files (x86)\Windows
 Kits\10\bin\10.0.22000.0\x86\signtool.exe" verify /v
 DeadlineCloudSubmitter-windows-x64-installer.exe` 3. Confirm that the output contains `Successfully verified:
 DeadlineCloudSubmitter-windows-x64-installer.exe`. The successful
verification means that you can run the installer.

Linux
To verify the authenticity of your downloaded files, use the `gpg`
command line tool.

1. Import the `OpenPGP` key by running the following
   command:

```
 gpg --import --armor <<EOF
-----BEGIN PGP PUBLIC KEY BLOCK-----

mQINBGlANDUBEACg6zffjN43gqe5ryPhk+wQM10rEdvmItw4WPWaVsN+/at/OIJw
MGCagSYXcgR+jKbsHQOQoEQdo5SrxxHjpKTEs3KQhGvf+ehrU1Ac7koXKIBWtes+
BI9F0slRECz0nXTOy/cd/90RXjpF07mreTLIKNIbybULfad82nYykpITjFr5XRGj
/shYkucxRQZdwkgkIYyV25pPICPd2RsX+Zua85jV8mCqVffDfRXvgcPe3+ofClj/
2CE8UfUIqO8Csua4YEkSqr3aeoTOEFT4kuQR5nFXVzorOEkQtO3gB35KNWKMlIOU
2vA+wyoL7nWSii4yfYtW3EZ+3gq6HxvnT9Zs8MC53uTOiOdamASXecYREwGmY/io
6n5XTEA/35LNbl4A756vSTZ7h4VFJAN5BpuqxstI1D7ou94skoSmcPoC/iniTvY9
kZylU5OCH/nifMAHM2a5jrQel80cW4oko9eyc8ENQpSy15JElFOKFf7D/4tcZJLF
F0VBTXbhfvq3dPfoq94IWt7p54Ovwj0S//CEu3jZYbNl2QC/3YiHE2H2XyGCQbq6
2MjcuxLnEapoRIqfbi8GPtCWVPzm28WGyKIDofWICczzeJFFJnvzrY3wRG64ibKJ
bR/uedwua1UuiC482V1FD5ffmzSSs8ktTp9hgj7RGDXlc9NTcF1jHxG9hwARAQAB
tCxBV1MgRGVhZGxpbmUgQ2xvdWQgPGF3cy1kZWFkbGluZUBhbWF6b24uY29tPokC
VwQTAQgAQRYhBJmXd7So2csyehiIYsg71N18bhtjBQJpQDQ1AhsvBQkDwmcABQsJ
CAcCAiICBhUKCQgLAgQWAgMBAh4HAheAAAoJEMg71N18bhtjk2UP/3h4KlEzZO/7
BxRmkbixuo1QuqOGvA6tXbSWaM8QH5jglcvL12PZLALklLT4v82uCsLR1lF8/Tch
cCl0SZEOFIS+XxAaw1Xfai6jlyLhabOwKF2ylq5eJlLcw1lh2nAArDRb4fLD0m1g
Dfqetq/XEpyXpOSkWxGRV4RlUdjQfytxrmcUnsT5/fk5f9VDdblu6K/lEmwfyYjB
lXv0uUCkqPot0SmbvOh3PY3Hi3n54ncy8NfTeV+TUvSe3C1s1zNl8aqHoTxJB/eU
kp+LFZ9m+igpSYnKeglKnytylH3KGCjTHglT/QXnI1wNTqmj1kFBVwtt/y1mtnA+
CPIUHP1CtbKsHaLtpp4llBm5TVtPN/Wqqicn5QLl4khg7R4K+V2aaA4ubY6p1tG9
0fFhN5tTnHDSKWMfmb83wfh5Zkcg85c3egjoit+wgGQRAQVqbznx7NqAHs9VoDIu
SPcAr+C329AOBzod4gyNGH7Ah5DkMITo4O4+axnAU9yhFOHcMJmTIask/fNg1Aum
OqYPMUwcgv1GZjLaTJyfGGC1xALsYR0KHnwIehD06MHR/Z98bGkcV8+Y0q8UPsd1
VN1fc1rjCJh/AT3w6owvG4DaEwspseSjzHv16mW4e2N6Uu23SPzgQsJ5qYN2g8D+
P7N9LGDfP8DaYc5JM9mlyFmYI2Q94ufL
=rY5l
-----END PGP PUBLIC KEY BLOCK-----
EOF
```

2. Determine whether to trust the `OpenPGP` key. When deciding,
   consider that AWS has taken measures to secure the hosting of the
   `OpenPGP` public key on this page, and that you obtained the
   key from the official Deadline Cloud documentation.
3. If you decide to trust the OpenPGP key, edit the key to
   trust with `gpg` similar to the following example:

```
$ gpg --edit-key 0xC83BD4DD7C6E1B63

    gpg (GnuPG) 2.3.7; Copyright (C) 2021 Free Software Foundation, Inc.
    This is free software: you are free to change and redistribute it.
    There is NO WARRANTY, to the extent permitted by law.


    pub  rsa4096/C83BD4DD7C6E1B63  created: 2025-12-15  expires: 2027-12-15  usage: SCEA
                         trust: unknown       validity: unknown
    [ unknown] (1). AWS Deadline Cloud <aws-deadline@amazon.com>

    gpg> trust
    pub  rsa4096/C83BD4DD7C6E1B63  created: 2025-12-15  expires: 2027-12-15  usage: SCEA
                         trust: unknown       validity: unknown
    [ unknown] (1). AWS Deadline Cloud <aws-deadline@amazon.com>

    Please decide how far you trust this user to correctly verify other users' keys
    (by looking at passports, checking fingerprints from different sources, etc.)

      1 = I don't know or won't say
      2 = I do NOT trust
      3 = I trust marginally
      4 = I trust fully
      5 = I trust ultimately
      m = back to the main menu

    Your decision? 5
    Do you really want to set this key to ultimate trust? (y/N) y

    pub  rsa4096/C83BD4DD7C6E1B63  created: 2025-12-15  expires: 2027-12-15  usage: SCEA
                         trust: ultimate      validity: unknown
    [ unknown] (1). AWS Deadline Cloud <aws-deadline@amazon.com>
    Please note that the shown key validity is not necessarily correct
    unless you restart the program.

    gpg> quit
```

4. ###### Verify the Deadline Cloud submitter installer

To verify the Deadline Cloud submitter installer, complete the following
steps:

    1. Download the signature file for the Deadline Cloud submitter installer.


    [Download signature file (.sig)](https://downloads.deadlinecloud.amazonaws.com/submitters/latest/linux/DeadlineCloudSubmitter-linux-x64-installer.run.sig "https://downloads.deadlinecloud.amazonaws.com/submitters/latest/linux/DeadlineCloudSubmitter-linux-x64-installer.run.sig")
    2. Verify the signature of the Deadline Cloud submitter installer by
     running:



    ```
    gpg --verify ./DeadlineCloudSubmitter-linux-x64-installer.run.sig ./DeadlineCloudSubmitter-linux-x64-installer.run
    ```

5. ###### Verify the Deadline Cloud monitor

###### Note

You can verify the Deadline Cloud monitor download using signature files or platform
specific methods. For platform specific methods, see the Linux
(Debian) tab, the Linux (RPM) tab, or the Linux
(AppImage) tab based on your downloaded file type.

To verify the Deadline Cloud monitor desktop application with signature files, complete
the following steps:

    1. Download the corresponding signature file for your Deadline Cloud monitor installer:




    	* [Download .deb signature file](https://downloads.deadlinecloud.amazonaws.com/dcm/latest/deadline-cloud-monitor_amd64.deb.sig "https://downloads.deadlinecloud.amazonaws.com/dcm/latest/deadline-cloud-monitor_amd64.deb.sig")
    	* [Download .rpm signature file](https://downloads.deadlinecloud.amazonaws.com/dcm/latest/deadline-cloud-monitor.x86_64.rpm.sig "https://downloads.deadlinecloud.amazonaws.com/dcm/latest/deadline-cloud-monitor.x86_64.rpm.sig")
    	* [Download .AppImage signature file](https://downloads.deadlinecloud.amazonaws.com/dcm/latest/deadline-cloud-monitor_amd64.AppImage.sig "https://downloads.deadlinecloud.amazonaws.com/dcm/latest/deadline-cloud-monitor_amd64.AppImage.sig")
    2. Verify the signature:


    **For .deb:**



    ```
    gpg --verify ./deadline-cloud-monitor_amd64.deb.sig ./deadline-cloud-monitor_amd64.deb
    ```

    **For .rpm:**



    ```
    gpg --verify ./deadline-cloud-monitor.x86_64.rpm.sig ./deadline-cloud-monitor.x86_64.rpm
    ```

    **For .AppImage:**



    ```
    gpg --verify ./deadline-cloud-monitor_amd64.AppImage.sig ./deadline-cloud-monitor_amd64.AppImage
    ```
    3. Confirm that the output looks similar to the following:


    `gpg: Signature made Mon Jan 5 21:10:14 2026 UTC`


    `gpg: using RSA key
     C83BD4DD7C6E1B63`


    If the output contains the phrase `Good signature from "AWS
     Deadline Cloud"`, it means that the signature has
     successfully been verified and you can run the Deadline Cloud monitor installation
     script.

**Historical keys**

If you downloaded an installer that was signed before the current key was
issued, import the following historical key and repeat the verification
steps.

```

-----BEGIN PGP PUBLIC KEY BLOCK-----

mQINBGX6GQsBEADduUtJgqSXI+q76O6fsFwEYKmbnlyL0xKvlq32EZuyv0otZo5L
le4m5Gg52AzrvPvDiUTLooAlvYeozaYyirIGsK08Ydz0Ftdjroiuh/mw9JSJDJRI
rnRn5yKet1JFezkjopA3pjsTBP6lW/mb1bDBDEwwwtH0x9lV7A03FJ9T7Uzu/qSh
qO/UYdkafro3cPASvkqgDt2tCvURfBcUCAjZVFcLZcVD5iwXacxvKsxxS/e7kuVV
I1+VGT8Hj8XzWYhjCZxOLZk/fvpYPMyEEujN0fYUp6RtMIXve0C9awwMCy5nBG2J
eE2Ol5DsCpTaBd4Fdr3LWcSs8JFA/YfP9auL3NczOozPoVJt+fw8CBlVIXO0J7l5
hvHDjcC+5v0wxqAlMG6+f/SX7CT8FXK+L3iOJ5gBYUNXqHSxUdv8kt76/KVmQa1B
Akl+MPKpMq+lhw++S3G/lXqwWaDNQbRRw7dSZHymQVXvPp1nsqc3hV7KlOM+6s6g
1g4mvFY4lf6DhptwZLWyQXU8rBQpojvQfiSmDFrFPWFi5BexesuVnkGIolQoklKx
AVUSdJPVEJCteyy7td4FPhBaSqT5vW3+ANbr9b/uoRYWJvn17dN0cc9HuRh/Ai+I
nkfECo2WUDLZ0fEKGjGyFX+todWvJXjvc5kmE9Ty5vJp+M9Vvb8jd6t+mwARAQAB
tCxBV1MgRGVhZGxpbmUgQ2xvdWQgPGF3cy1kZWFkbGluZUBhbWF6b24uY29tPokC
VwQTAQgAQRYhBLhAwIwpqQeWoHH6pfbNPOa3bzzvBQJl+hkLAxsvBAUJA8JnAAUL
CQgHAgIiAgYVCgkICwIDFgIBAh4HAheAAAoJEPbNPOa3bzzvKswQAJXzKSAY8sY8
F6Eas2oYwIDDdDurs8FiEnFghjUEO6MTt9AykF/jw+CQg2UzFtEyObHBymhgmhXE
3buVeom96tgM3ZDfZu+sxi5pGX6oAQnZ6riztN+VpkpQmLgwtMGpSMLl3KLwnv2k
WK8mrR/fPMkfdaewB7A6RIUYiW33GAL4KfMIs8/vIwIJw99NxHpZQVoU6dFpuDtE
1OuxGcCqGJ7mAmo6H/YawSNp2Ns80gyqIKYo7o3LJ+WRroIRlQyctq8gnR9JvYXX
42ASqLq5+OXKo4qh81blXKYqtc176BbbSNFjWnzIQgKDgNiHFZCdcOVgqDhwO15r
NICbqqwwNLj/Fr2kecYx180Ktpl0jOOw5IOyh3bf3MVGWnYRdjvA1v+/CO+55N4g
z0kf50Lcdu5RtqV10XBCifn28pecqPaSdYcssYSRl5DLiFktGbNzTGcZZwITTKQc
af8PPdTGtnnb6P+cdbW3bt9MVtN5/dgSHLThnS8MPEuNCtkTnpXshuVuBGgwBMdb
qUC+HjqvhZzbwns8dr5WI+6HWNBFgGANn6ageYl58vVp0UkuNP8wcWjRARciHXZx
ku6W2jPTHDWGNrBQO2Fx7fd2QYJheIPPAShHcfJO+xgWCof45D0vAxAJ8gGg9Eq+
gFWhsx4NSHn2gh1gDZ41Ou/4exJ1lwPM
=uVaX
-----END PGP PUBLIC KEY BLOCK-----

```

Linux (AppImage)
To verify packages that use a Linux .AppImage binary, first complete steps
1-3 in the Linux tab, then complete the following steps.

1. From the AppImageUpdate [page](https://github.com/AppImageCommunity/AppImageUpdate/releases/tag/continuous "https://github.com/AppImageCommunity/AppImageUpdate/releases/tag/continuous") in GitHub, download the
   **validate-x86\_64.AppImage** file.
2. After downloading the file, to add execute permissions, run the following
   command.

```
chmod a+x ./validate-x86_64.AppImage
```

3. To add execute permissions, run the following command.

```
chmod a+x ./deadline-cloud-monitor_`<APP_VERSION>`_amd64.AppImage
```

4. To verify the Deadline Cloud monitor signature, run the following command.

```
./validate-x86_64.AppImage ./deadline-cloud-monitor_`<APP_VERSION>`_amd64.AppImage
```

If the output contains the phrase `Validation successful`, it
means that the signature has successfully been verified and you can safely
run the Deadline Cloud monitor installation script.

Linux (Debian)
To verify packages that use a Linux .deb binary, first complete steps 1-3 in
the Linux tab.

**dpkg** is the core package management tool in most
debian based Linux distributions. You can verify
the .deb file with the tool.

1. Download the Deadline Cloud monitor .deb file:

[Download Deadline Cloud monitor (.deb)](https://downloads.deadlinecloud.amazonaws.com/dcm/latest/deadline-cloud-monitor_amd64.deb "https://downloads.deadlinecloud.amazonaws.com/dcm/latest/deadline-cloud-monitor_amd64.deb") 2. Verify the .deb file:

```
dpkg-sig --verify deadline-cloud-monitor_amd64.deb
```

3. The output will be similar to:

```
Processing deadline-cloud-monitor_amd64.deb...
GOODSIG _gpgbuilder C83BD4DD7C6E1B63 1765815349
```

4. To verify the .deb file, confirm that `GOODSIG` is present in
   the output.

Linux (RPM)
To verify packages that use a Linux .rpm binary, first complete steps 1-3 in
the Linux tab.

1. Download the Deadline Cloud monitor .rpm file:

[Download Deadline Cloud monitor (.rpm)](https://downloads.deadlinecloud.amazonaws.com/dcm/latest/deadline-cloud-monitor.x86_64.rpm "https://downloads.deadlinecloud.amazonaws.com/dcm/latest/deadline-cloud-monitor.x86_64.rpm") 2. Verify the .rpm file:

```
gpg --export --armor "Deadline Cloud" > key.pub
sudo rpm --import key.pub
rpm -K deadline-cloud-monitor.x86_64.rpm
```

3. The output will be similar to:

```
deadline-cloud-monitor.x86_64.rpm: digests signatures OK
```

4. To verify the .rpm file, confirm that `digests signatures OK`
   is in the output.
