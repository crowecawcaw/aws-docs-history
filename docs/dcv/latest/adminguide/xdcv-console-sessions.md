# Using Xdcv with console sessions

Amazon DCV offers two types of sessions: console and virtual.

With **virtual sessions**, Amazon DCV starts a dedicated X server instance, Xdcv, and runs a desktop environment
inside it. Amazon DCV starts a new Xdcv instance for each virtual session, and each virtual session uses the display provided by its own X server
instance. The Xdcv binary is provided by the `nice-xdcv` package.

With **console sessions**, Amazon DCV directly captures the content of the desktop screen, which on Linux is normally
rendered by the system's X server (Xorg). It is also possible to configure a console session to be served by Xdcv in place of Xorg. This provides
dynamic resizing and multi-monitor without configuring specifics in your `xorg.conf`.

This topic describes how to make that switch on Ubuntu, RHEL/Rocky Linux/CentOS Stream, and Amazon Linux 2023.

###### Important

This configuration applies only to non-GPU hosts. Applying these steps on instances with a GPU will break the GPU-accelerated display pipeline.

###### Note

These instructions assume that your system uses GDM (GNOME Display Manager). If you use a different display manager, such as LightDM or SDDM, adjust the `systemctl restart` command accordingly.

###### Topics

- [Prerequisites](#xdcv-console-prereqs "#xdcv-console-prereqs")
- [Ubuntu](#xdcv-console-ubuntu "#xdcv-console-ubuntu")
- [RHEL / Rocky Linux / CentOS Stream](#xdcv-console-rhel "#xdcv-console-rhel")
- [Amazon Linux 2023](#xdcv-console-al2023 "#xdcv-console-al2023")
- [Verifying the configuration](#xdcv-console-verify "#xdcv-console-verify")
- [Reverting](#xdcv-console-revert "#xdcv-console-revert")

## Prerequisites

Before running the commands for your distribution, confirm the following:

- The `nice-xdcv` package is installed, and the `Xdcv-console` binary is present at
  `/usr/bin/Xdcv-console`.
- You have root privileges (use `sudo` where appropriate).

###### Note

After configuration, the next console login will start an Xdcv-backed session rather than a standard Xorg session.

## Ubuntu

On Ubuntu, the switch is performed by diverting the original Xorg binary out of the way and pointing `/usr/bin/Xorg` at
`Xdcv-console` via a symlink.

```
`$` dpkg-divert --package nice-xdcv --divert /usr/bin/Xorg.orig --rename /usr/bin/Xorg
`$` ln -sf /usr/bin/Xdcv-console /usr/bin/Xorg
`$` sudo systemctl restart gdm
```

###### What each command does

`dpkg-divert`

Tells dpkg that the `nice-xdcv` package owns the path `/usr/bin/Xorg` and renames the existing Xorg binary to
`/usr/bin/Xorg.orig`. This preserves the original binary and prevents future Xorg package upgrades from overwriting your
customization.

`ln -sf`

Creates or replaces a symbolic link so that any process invoking `/usr/bin/Xorg` actually runs
`/usr/bin/Xdcv-console`.

`systemctl restart gdm`

Restarts the GNOME Display Manager so the change takes effect. This terminates any active graphical session on the host, so run it when
no one is logged in to the console.

## RHEL / Rocky Linux / CentOS Stream

On RHEL-family distributions, the `nice-xdcv` package provides two systemd units that handle the switch declaratively.

```
`$` systemctl enable --now xdcv-console-update.service
`$` systemctl enable xdcv-console.path
`$` sudo systemctl restart gdm
```

###### What each command does

`xdcv-console-update.service`

The unit that reconciles the system to use `Xdcv-console` for console sessions. Enabling it with `--now` activates
it immediately and makes it start on subsequent boots.

`xdcv-console.path`

A path-based unit that watches the relevant files on disk and re-triggers the update service if the X server configuration changes, for
example, after a package upgrade. Enabling it ensures the Xdcv configuration is re-applied automatically rather than silently reverting.

`systemctl restart gdm`

Restarts the GNOME Display Manager so the change takes effect. This terminates any active graphical session on the host, so run it when
no one is logged in to the console.

## Amazon Linux 2023

Amazon Linux 2023 uses the `update-alternatives` system to manage which binary provides `/usr/bin/X`.

```
`$` update-alternatives --install /usr/bin/X X /usr/bin/Xdcv-console 11
`$` sudo update-alternatives --set X /usr/bin/Xdcv-console
`$` sudo systemctl restart gdm
```

###### What each command does

`update-alternatives --install`

Registers `Xdcv-console` as a candidate for the `X` alternative, with priority 11. Priority only matters when the
alternative is in automatic mode; the next command overrides that.

`update-alternatives --set X`

Pins `X` to `Xdcv-console` explicitly, so it will not be displaced by a higher-priority candidate later.

`systemctl restart gdm`

Restarts the GNOME Display Manager so the change takes effect. This terminates any active graphical session on the host, so run it when
no one is logged in to the console.

## Verifying the configuration

After applying the steps for your distribution, confirm that the X server path now resolves to `Xdcv-console`:

```
`$` ls -l /usr/bin/Xorg       # Ubuntu
`$` ls -lh /usr/bin/X         # RHEL/Rocky Linux/CentOS Stream
`$` ls -l /etc/alternatives/X # Amazon Linux 2023
```

Then start a console session and check that it comes up as expected. If the display manager fails to start, log in via SSH to troubleshoot
before attempting another graphical login.

## Reverting

If you need to revert to the stock X server:

- **Ubuntu:** Remove the symlink and then run
  `dpkg-divert --package nice-xdcv --rename --remove /usr/bin/Xorg` to restore the original binary.
- **RHEL/Rocky:**
  `systemctl disable --now xdcv-console.path xdcv-console-update.service`.
- **Amazon Linux 2023:**
  `update-alternatives --remove X /usr/bin/Xdcv-console`, then restart gdm.
