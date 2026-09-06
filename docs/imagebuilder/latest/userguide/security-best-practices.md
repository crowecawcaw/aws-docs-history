# Security best practices for Image Builder

EC2 Image Builder provides a number of security features to consider as you develop and
implement your own security policies. The following best practices are general
guidelines and don’t represent a complete security solution. Because these best
practices might not be appropriate or sufficient for your environment, treat them as
helpful considerations rather than prescriptions.

- Do not use overly-permissive security groups in Image Builder recipes.
- Do not share images with accounts that you do not trust.
- Do not make images public that have private or sensitive data.
- Apply all available Windows or Linux security patches during image
  builds.
- Periodically apply managed AMI updates to your macOS recipes and create
  new images to launch instances that have the latest security patches.
- When you import a Windows ISO disk image, obtain the ISO from Microsoft or
  an authorized reseller. Also, grant the instance profile role only the permissions
  that the import requires. For more information, see [Security considerations for ISO disk image import](import-iso-disk.md#iso-import-security "import-iso-disk.md#iso-import-security").
  We strongly recommend that you test your images to validate the security posture and
  applicable security compliance levels. Solutions such as [Amazon Inspector](https://aws.amazon.com/inspector/ "https://aws.amazon.com/inspector/") can help validate the
  security and compliance posture of images.

###### IMDSv2 for Image Builder pipelines

When your Image Builder pipeline runs, it sends HTTP requests to launch EC2 instances that Image Builder
uses to build and test your image. To configure the version of IMDS that your
pipeline uses for the launch requests, set the `httpTokens` parameter in
your Image Builder infrastructure configuration instance metadata settings.

###### Note

We recommend that you configure all EC2 instances that Image Builder launches from a pipeline
build to use IMDSv2 so that instance metadata retrieval requests require a signed token header.

For more information about Image Builder infrastructure configuration, see [Manage Image Builder infrastructure configuration](manage-infra-config.md "manage-infra-config.md"). For more
information about EC2 instance metadata options for Linux images, see [Configure the
instance metadata options](../../../AWSEC2/latest/UserGuide/configuring-instance-metadata-options.md "../../../AWSEC2/latest/UserGuide/configuring-instance-metadata-options.md") in the Amazon EC2 User Guide. For Windows images, see
[Configure
the instance metadata options](../../../AWSEC2/latest/UserGuide/configuring-instance-metadata-options.md "../../../AWSEC2/latest/UserGuide/configuring-instance-metadata-options.md") in the Amazon EC2 User Guide.

## Required post-build clean up

After Image Builder completes all of the build steps for your custom image, Image Builder prepares the build
instance for testing and image creation. Before shutting down the build instance to
create the snapshot, Image Builder performs the following clean up to ensure the security
of your image:

Linux
The Image Builder pipeline runs a clean up script to help ensure that the final image follows
security best practices, and to remove any build artifacts or settings
that should not carry over to your snapshot. However, you can skip
sections of the script, or override the user data entirely. Therefore,
the images produced by Image Builder pipelines are not necessarily compliant with
any specific regulatory criteria.

When the pipeline completes its build and test stages, Image Builder automatically runs the
following clean-up script just before it creates the output
image.

###### Important

If you override **User data** in your recipe, the script doesn't run.
In that case, make sure that you include a command in your user data
that creates an empty file named
`perform_cleanup`. Image Builder detects this file and
runs the clean-up script prior to creating the new image.

After the file clean up completes, Image Builder appends steps to the script that
uninstall the Systems Manager agent and remove the `cronie` package.
Image Builder tracks what it installed during the build in the
`/tmp/imagebuilder_service` service working directory.
Image Builder uses those markers to decide what to remove:

- **Systems Manager agent** – Whether Image Builder uninstalls the agent
  depends on the
  `systemsManagerAgent.uninstallAfterBuild` setting in
  your image recipe and whether Image Builder installed the agent. For more
  information, see the `uninstallAfterBuild` setting in
  [Create an image recipe with the AWS CLI](create-image-recipes.md#create-image-recipe-cli "create-image-recipes.md#create-image-recipe-cli").
- **`cronie` package** – This
  step applies to Amazon Linux 1, Amazon Linux 2, and Amazon Linux 2023.
  If Image Builder installed a crontab during the build, it records a
  `crontab_installed` marker in the service working
  directory. Image Builder then removes the `cronie` package as part of
  clean up. To keep `cronie` in your final image, delete
  the marker file before clean up runs by adding the following command
  to a component or to your user data:

```
rm -f /tmp/imagebuilder_service/crontab_installed
```

```
#!/bin/bash
if [[ ! -f {{workingDirectory}}/perform_cleanup ]]; then
    echo "Skipping cleanup"
    exit 0
else
    sudo rm -f {{workingDirectory}}/perform_cleanup
fi

function cleanup() {
    FILES=("$@")
    for FILE in "${FILES[@]}"; do
        if [[ -f "$FILE" ]]; then
            echo "Deleting $FILE";
            sudo shred -zuf $FILE;
        fi;
        if [[ -f $FILE ]]; then
            echo "Failed to delete '$FILE'. Failing."
            exit 1
        fi;
    done
};


# Clean up for cloud-init files
CLOUD_INIT_FILES=(
    "/etc/sudoers.d/90-cloud-init-users"
    "/etc/locale.conf"
    "/var/log/cloud-init.log"
    "/var/log/cloud-init-output.log"
)
if [[ -f {{workingDirectory}}/skip_cleanup_cloudinit_files ]]; then
    echo "Skipping cleanup of cloud init files"
else
    echo "Cleaning up cloud init files"
    cleanup "${CLOUD_INIT_FILES[@]}"
    if [[ -d "/var/lib/cloud" ]]; then
        if [[ $( sudo find /var/lib/cloud -type f | sudo wc -l ) -gt 0 ]]; then
            echo "Deleting files within /var/lib/cloud/*"
            sudo find /var/lib/cloud -type f -exec shred -zuf {} \;
        fi;

        if [[ $( sudo ls /var/lib/cloud | sudo wc -l ) -gt 0 ]]; then
            echo "Deleting /var/lib/cloud/*"
            sudo rm -rf /var/lib/cloud/* || true
        fi;
    fi;
fi;


# Clean up for temporary instance files
INSTANCE_FILES=(
    "/etc/.updated"
    "/etc/aliases.db"
    "/etc/hostname"
    "/var/lib/misc/postfix.aliasesdb-stamp"
    "/var/lib/postfix/master.lock"
    "/var/spool/postfix/pid/master.pid"
    "/var/.updated"
    "/var/cache/yum/x86_64/2/.gpgkeyschecked.yum"
)
if [[ -f {{workingDirectory}}/skip_cleanup_instance_files ]]; then
    echo "Skipping cleanup of instance files"
else
    echo "Cleaning up instance files"
    cleanup "${INSTANCE_FILES[@]}"
fi;


# Clean up for ssh files
SSH_FILES=(
    "/etc/ssh/ssh_host_rsa_key"
    "/etc/ssh/ssh_host_rsa_key.pub"
    "/etc/ssh/ssh_host_ecdsa_key"
    "/etc/ssh/ssh_host_ecdsa_key.pub"
    "/etc/ssh/ssh_host_ed25519_key"
    "/etc/ssh/ssh_host_ed25519_key.pub"
    "/root/.ssh/authorized_keys"
)
if [[ -f {{workingDirectory}}/skip_cleanup_ssh_files ]]; then
    echo "Skipping cleanup of ssh files"
else
    echo "Cleaning up ssh files"
    cleanup "${SSH_FILES[@]}"
    USERS=$(ls /home/)
    for user in $USERS; do
        echo Deleting /home/"$user"/.ssh/authorized_keys;
        sudo find /home/"$user"/.ssh/authorized_keys -type f -exec shred -zuf {} \;
    done
    for user in $USERS; do
        if [[ -f /home/"$user"/.ssh/authorized_keys ]]; then
            echo Failed to delete /home/"$user"/.ssh/authorized_keys;
            exit 1
        fi;
    done;
fi;


# Clean up for instance log files
INSTANCE_LOG_FILES=(
    "/var/log/audit/audit.log"
    "/var/log/boot.log"
    "/var/log/dmesg"
    "/var/log/cron"
)
if [[ -f {{workingDirectory}}/skip_cleanup_instance_log_files ]]; then
    echo "Skipping cleanup of instance log files"
else
    echo "Cleaning up instance log files"
    cleanup "${INSTANCE_LOG_FILES[@]}"
fi;

# Clean up for TOE files
if [[ -f {{workingDirectory}}/skip_cleanup_toe_files ]]; then
    echo "Skipping cleanup of TOE files"
else
    echo "Cleaning TOE files"
    shopt -s nullglob
    TOE_MATCHES=({{workingDirectory}}/TOE_*)
    shopt -u nullglob
    if [[ ${#TOE_MATCHES[@]} -gt 0 ]]; then
        if [[ $( sudo find "${TOE_MATCHES[@]}" -type f | sudo wc -l) -gt 0 ]]; then
            echo "Deleting files within {{workingDirectory}}/TOE_*"
            sudo find "${TOE_MATCHES[@]}" -type f -exec shred -zuf {} \;
        fi
        shopt -s nullglob
        TOE_REMAINING=({{workingDirectory}}/TOE_*)
        shopt -u nullglob
        if [[ ${#TOE_REMAINING[@]} -gt 0 ]]; then
            if [[ $( sudo find "${TOE_REMAINING[@]}" -type f | sudo wc -l) -gt 0 ]]; then
                echo "Failed to delete {{workingDirectory}}/TOE_*"
                exit 1
            fi
            echo "Deleting {{workingDirectory}}/TOE_*"
            sudo rm -rf "${TOE_REMAINING[@]}"
        fi
        shopt -s nullglob
        TOE_FINAL=({{workingDirectory}}/TOE_*)
        shopt -u nullglob
        if [[ ${#TOE_FINAL[@]} -gt 0 ]]; then
            echo "Failed to delete {{workingDirectory}}/TOE_*"
            exit 1
        fi
    fi
fi

# Clean up for ssm log files
if [[ -f {{workingDirectory}}/skip_cleanup_ssm_log_files ]]; then
    echo "Skipping cleanup of ssm log files"
else
    echo "Cleaning up ssm log files"
    if [[ -d "/var/log/amazon/ssm" ]]; then
        if [[ $( sudo find /var/log/amazon/ssm -type f | sudo wc -l) -gt 0 ]]; then
            echo "Deleting files within /var/log/amazon/ssm/*"
            sudo find /var/log/amazon/ssm -type f -exec shred -zuf {} \;
        fi
        if [[ $( sudo find /var/log/amazon/ssm -type f | sudo wc -l) -gt 0 ]]; then
            echo "Failed to delete /var/log/amazon/ssm"
            exit 1
        fi
        echo "Deleting /var/log/amazon/ssm/*"
        sudo rm -rf /var/log/amazon/ssm
        if [[ -d "/var/log/amazon/ssm" ]]; then
            echo "Failed to delete /var/log/amazon/ssm"
            exit 1
        fi
    fi
fi


shopt -s nullglob
SA_MATCHES=(/var/log/sa/sa*)
shopt -u nullglob
if [[ ${#SA_MATCHES[@]} -gt 0 ]]; then
    echo "Deleting /var/log/sa/sa*"
    sudo shred -zuf "${SA_MATCHES[@]}"
    shopt -s nullglob
    SA_REMAINING=(/var/log/sa/sa*)
    shopt -u nullglob
    if [[ ${#SA_REMAINING[@]} -gt 0 ]]; then
        echo "Failed to delete /var/log/sa/sa*"
        exit 1
    fi
fi

shopt -s nullglob
DHCLIENT_MATCHES=(/var/lib/dhclient/dhclient*.lease)
shopt -u nullglob
if [[ ${#DHCLIENT_MATCHES[@]} -gt 0 ]]; then
    echo "Deleting /var/lib/dhclient/dhclient*.lease"
    sudo shred -zuf "${DHCLIENT_MATCHES[@]}"
    shopt -s nullglob
    DHCLIENT_REMAINING=(/var/lib/dhclient/dhclient*.lease)
    shopt -u nullglob
    if [[ ${#DHCLIENT_REMAINING[@]} -gt 0 ]]; then
        echo "Failed to delete /var/lib/dhclient/dhclient*.lease"
        exit 1
    fi
fi

if [[ $( sudo find /var/tmp -type f | sudo wc -l) -gt 0 ]]; then
    echo "Deleting files within /var/tmp/*"
    sudo find /var/tmp -type f -exec shred -zuf {} \;
fi
if [[ $( sudo find /var/tmp -type f | sudo wc -l) -gt 0 ]]; then
    echo "Failed to delete /var/tmp"
    exit 1
fi
if [[ $( sudo ls /var/tmp | sudo wc -l ) -gt 0 ]]; then
    echo "Deleting /var/tmp/*"
    sudo rm -rf /var/tmp/*
fi

if [[ -f "/var/lib/systemd/random-seed" ]]; then
    echo "Deleting /var/lib/systemd/random-seed"
    sudo shred -zuf /var/lib/systemd/random-seed
    sudo rm -f /var/lib/systemd/random-seed
fi

# Shredding is not guaranteed to work well on rolling logs

if [[ -f "/var/lib/rsyslog/imjournal.state" ]]; then
    echo "Deleting /var/lib/rsyslog/imjournal.state"
    sudo shred -zuf /var/lib/rsyslog/imjournal.state
    sudo rm -f /var/lib/rsyslog/imjournal.state
fi

if [[ -d "/var/log/journal" ]] && [[ $( sudo ls /var/log/journal/ | sudo wc -l ) -gt 0 ]]; then
    echo "Deleting /var/log/journal/*"
    sudo find /var/log/journal/ -type f -exec shred -zuf {} \;
    sudo rm -rf /var/log/journal/*
fi

if [[ -f "/etc/machine-id" ]]; then
    echo "Truncating /etc/machine-id"
    sudo truncate -s 0 /etc/machine-id
fi

if [[ -f "/var/lib/dbus/machine-id" ]]; then
    echo "Truncating /var/lib/dbus/machine-id"
    sudo truncate -s 0 /var/lib/dbus/machine-id
fi

sudo touch /etc/machine-id

# Flush all pending writes to disk before instance shutdown and snapshot
sync

echo "Sanitize OK"


###############################################################################
# Image Builder appends the following steps to the clean up script to uninstall
# the Systems Manager (SSM) agent and, on Amazon Linux 1, Amazon Linux 2, and
# Amazon Linux 2023, to remove the cronie package when Image Builder installed a
# crontab during the build. Image Builder uses the /tmp/imagebuilder_service
# working directory to track what it installed.
###############################################################################

SERVICE_ROOT_WORKING_DIR="/tmp/imagebuilder_service"

# SSM_UNINSTALL_CONDITION reflects the systemsManagerAgent.uninstallAfterBuild
# recipe setting and how the SSM agent was installed:
#   SSM_INSTALLED_BY_CUSTOMER      - always uninstall the SSM agent
#   SSM_INSTALLED_BY_IMAGE_BUILDER - uninstall only if Image Builder installed it
#   (any other value)              - leave the SSM agent in the final image
SSM_UNINSTALL_CONDITION="<uninstallAfterBuild condition>"

function error_exit {
  echo "$1" 1>&2
  exit 1
}

function ssm_exists() {
  eval "$1"  > /dev/null 2>&1
  echo $?
}

function cleanup_image() {
  rm -rf "${SERVICE_ROOT_WORKING_DIR}"
}

function uninstall_ssm_agent() {

  uninstall_package="$1"
  uninstall_all=""
  uninstall_success="false"

  if [ "${uninstall_package}" == "" ]; then
    uninstall_all="true"
  fi

  yum="sudo yum search amazon-ssm-agent | grep amazon-ssm-agent"
  snap="sudo snap list amazon-ssm-agent"
  rpm="sudo rpm -qa amazon-ssm-agent | grep amazon-ssm-agent"
  dpkg="sudo dpkg --get-selections | grep amazon-ssm-agent"
  pkg="su -m root -c \"pkg info -l amazon-ssm-agent | grep amazon-ssm-agent\""


  if [[ ("${uninstall_all}" == "true" || "${uninstall_package}" == "snap") && $(ssm_exists "${snap}") -eq 0 ]]; then
    echo "Package found in Snap.... Uninstalling"
    (sleep 30 ; sudo snap remove amazon-ssm-agent) &>/dev/null &
    uninstall_success="true"
  fi

  if [[ ("${uninstall_all}" == "true" || "${uninstall_package}" == "yum") && $(ssm_exists "${yum}") -eq 0 ]]; then
    echo "Package found in Yum.... Uninstalling"
    (sleep 30 ; sudo yum remove -y amazon-ssm-agent) &>/dev/null &
    uninstall_success="true"
  fi

  if [[ ("${uninstall_all}" == "true" || "${uninstall_package}" == "rpm") && $(ssm_exists "${rpm}") -eq 0 ]]; then
    echo "Package found in Rpm.... Uninstalling"
    (sleep 30 ; sudo rpm -e amazon-ssm-agent) &>/dev/null &
    uninstall_success="true"
  fi

  if [[ ("${uninstall_all}" == "true" || "${uninstall_package}" == "dpkg") && $(ssm_exists "${dpkg}") -eq 0 ]]; then
    echo "Package found in Dpkg.... Uninstalling"
    (sleep 30 ; sudo dpkg -r --force-all amazon-ssm-agent) &>/dev/null &
    uninstall_success="true"
  fi

  if [[ ("${uninstall_all}" == "true" || "${uninstall_package}" == "pkg") && $(ssm_exists "${pkg}") -eq 0 ]]; then
    echo "Package found in FreeBSD.... Uninstalling"
    (sleep 30 ; su -m root -c "pkg remove -y amazon-ssm-agent") &> /dev/null &
    uninstall_success="true"
  fi

  if [ "${uninstall_success}" == "false" ] ; then
    error_exit "Unable to uninstall an SSM agent"
  fi
}

# Amazon Linux releases where Image Builder installs cronie to provide a crontab:
# Amazon Linux AMI (AL1), AL2, and AL2023.
function is_cronie_supported_amazon_linux() {
    if [ "$(get_os_type)" != "amzn" ]; then
        return 1
    fi
    case "$(get_os_version)" in
        2|2023) return 0 ;;
        # AL1 releases use date-based versions from 2010 through 2018.
        201[0-8].[0-9][0-9]) return 0 ;;
        *) return 1 ;;
    esac
}

function uninstall_crontab() {
    if is_cronie_supported_amazon_linux ; then
        echo "Uninstalling cronie package"
        sudo yum remove -y cronie
    fi
}

function get_os_type() {
    FILE=/etc/os-release
    if [ -e $FILE ]; then
        . $FILE
        echo $ID
    else
        echo ""
    fi
}

function get_os_version() {
    FILE=/etc/os-release
    if [ -e $FILE ]; then
        . $FILE
        echo $VERSION_ID
    else
        echo ""
    fi
}

if [ "${SSM_UNINSTALL_CONDITION}" == "SSM_INSTALLED_BY_CUSTOMER" ] ; then
  echo "Uninstall after build set to true. Uninstalling SSM agent."
  uninstall_ssm_agent

elif [ "${SSM_UNINSTALL_CONDITION}" == "SSM_INSTALLED_BY_IMAGE_BUILDER" ] ; then
  echo "Checking if the SSM agent was installed by Image Builder"
  if [[ -f ${SERVICE_ROOT_WORKING_DIR}/ssm_installed ]] ; then
    package_manager="$(cat ${SERVICE_ROOT_WORKING_DIR}/ssm_installed)"
    echo "Uninstalling the SSM agent installed by Image Builder using ${package_manager}"
    uninstall_ssm_agent "${package_manager}"
  fi
else
  echo "Uninstall after build set to false. Skipping SSM agent uninstall."
fi

# When Image Builder installs a crontab during the build (on Amazon Linux 1,
# Amazon Linux 2, or Amazon Linux 2023), it records a crontab_installed marker
# and removes the cronie package here. To keep cronie in your final image,
# delete the marker before clean up runs:
#   rm -f /tmp/imagebuilder_service/crontab_installed
if [[ -f ${SERVICE_ROOT_WORKING_DIR}/crontab_installed ]] ; then
  echo "Uninstalling crontab installed by Image Builder"
  uninstall_crontab
fi

cleanup_image

```

Windows
After the Image Builder pipeline customizes Windows images, it runs the Microsoft [Sysprep](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/sysprep--generalize--a-windows-installation?view=windows-11 "https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/sysprep--generalize--a-windows-installation?view=windows-11") utility. These actions follow [AWS best practices for
hardening and cleaning the image](https://aws.amazon.com/articles/public-ami-publishing-hardening-and-clean-up-requirements/ "https://aws.amazon.com/articles/public-ami-publishing-hardening-and-clean-up-requirements/").

macOS
The Image Builder pipeline runs a clean up script to help ensure that the final image follows
security best practices, and to remove any build artifacts or settings
that should not carry over to your snapshot. However, you can skip
sections of the script, or override the user data entirely. Therefore,
the images produced by Image Builder pipelines are not necessarily compliant with
any specific regulatory criteria.

When the pipeline completes its build and test stages, Image Builder automatically runs the
following clean-up script just before it creates the output image.

###### Important

If you override **User data** in your recipe, the script doesn't run.
In that case, make sure that you include a command in your user data
that creates an empty file named `perform_cleanup`. Image Builder detects
this file and runs the clean-up script prior to creating the new image.

```
#!/bin/bash
if [[ ! -f {{workingDirectory}}/perform_cleanup ]]; then
  echo "Skipping cleanup"
  exit 0
else
  sudo rm -f {{workingDirectory}}/perform_cleanup
fi

function cleanup() {
  FILES=("$@")
  for FILE in "${FILES[@]}"; do
      if [[ -f "$FILE" ]]; then
          echo "Deleting $FILE";
          sudo rm -f $FILE;
      fi;
      if [[ -f $FILE ]]; then
          echo "Failed to delete '$FILE'. Failing."
          exit 1
      fi;
  done
};

# Reset EC2 macOS Init instance history so the image behaves as a first boot
if [[ -f {{workingDirectory}}/skip_cleanup_ec2_macos_init_files ]]; then
  echo "Skipping cleanup of ec2-macos-init instance history"
else
  echo "Cleaning up ec2-macos-init instance history"
  if [[ -x /usr/local/bin/ec2-macos-init ]]; then
      sudo /usr/local/bin/ec2-macos-init clean -all
  fi
fi

# Clean up for temporary instance files
INSTANCE_FILES=(
  "/Library/Preferences/SystemConfiguration/NetworkInterfaces.plist"
)
if [[ -f {{workingDirectory}}/skip_cleanup_instance_files ]]; then
  echo "Skipping cleanup of instance files"
else
  echo "Cleaning up instance files"
  cleanup "${INSTANCE_FILES[@]}"
fi;


# Clean up for ssh files
SSH_FILES=(
  "/etc/ssh/ssh_host_rsa_key"
  "/etc/ssh/ssh_host_rsa_key.pub"
  "/etc/ssh/ssh_host_ecdsa_key"
  "/etc/ssh/ssh_host_ecdsa_key.pub"
  "/etc/ssh/ssh_host_ed25519_key"
  "/etc/ssh/ssh_host_ed25519_key.pub"
  "/var/root/.ssh/authorized_keys"
)
if [[ -f {{workingDirectory}}/skip_cleanup_ssh_files ]]; then
  echo "Skipping cleanup of ssh files"
else
  echo "Cleaning up ssh files"
  cleanup "${SSH_FILES[@]}"
  USERS=$(ls /Users/)
  for user in $USERS; do
      if [[ -f /Users/"$user"/.ssh/authorized_keys ]]; then
          echo Deleting /Users/"$user"/.ssh/authorized_keys;
          sudo rm -f /Users/"$user"/.ssh/authorized_keys;
      fi;
  done
  for user in $USERS; do
      if [[ -f /Users/"$user"/.ssh/authorized_keys ]]; then
          echo Failed to delete /Users/"$user"/.ssh/authorized_keys;
          exit 1
      fi;
  done;
fi;


# Clean up for instance log files
INSTANCE_LOG_FILES=(
  "/var/log/amazon/ec2/ec2-macos-init.log"
  "/var/log/amazon/ec2/ena-ethernet.log"
  "/var/log/amazon/ec2/system-monitoring.log"
)
if [[ -f {{workingDirectory}}/skip_cleanup_instance_log_files ]]; then
  echo "Skipping cleanup of instance log files"
else
  echo "Cleaning up instance log files"
  cleanup "${INSTANCE_LOG_FILES[@]}"
fi;

# Clean up for TOE files
if [[ -f {{workingDirectory}}/skip_cleanup_toe_files ]]; then
  echo "Skipping cleanup of TOE files"
else
  echo "Cleaning TOE files"
  shopt -s nullglob
  TOE_MATCHES=({{workingDirectory}}/TOE_*)
  shopt -u nullglob
  if [[ ${#TOE_MATCHES[@]} -gt 0 ]]; then
      if [[ $( sudo find "${TOE_MATCHES[@]}" -type f | sudo wc -l) -gt 0 ]]; then
          echo "Deleting files within {{workingDirectory}}/TOE_*"
          sudo find "${TOE_MATCHES[@]}" -type f -exec rm -f {} \;
      fi
      shopt -s nullglob
      TOE_REMAINING=({{workingDirectory}}/TOE_*)
      shopt -u nullglob
      if [[ ${#TOE_REMAINING[@]} -gt 0 ]]; then
          if [[ $( sudo find "${TOE_REMAINING[@]}" -type f | sudo wc -l) -gt 0 ]]; then
              echo "Failed to delete {{workingDirectory}}/TOE_*"
              exit 1
          fi
          echo "Deleting {{workingDirectory}}/TOE_*"
          sudo rm -rf "${TOE_REMAINING[@]}"
      fi
      shopt -s nullglob
      TOE_FINAL=({{workingDirectory}}/TOE_*)
      shopt -u nullglob
      if [[ ${#TOE_FINAL[@]} -gt 0 ]]; then
          echo "Failed to delete {{workingDirectory}}/TOE_*"
          exit 1
      fi
  fi
fi

# Clean up for ssm log files
if [[ -f {{workingDirectory}}/skip_cleanup_ssm_log_files ]]; then
  echo "Skipping cleanup of ssm log files"
else
  echo "Cleaning up ssm log files"
  if [[ -d "/var/log/amazon/ssm" ]]; then
      if [[ $( sudo find /var/log/amazon/ssm -type f | sudo wc -l) -gt 0 ]]; then
          echo "Deleting files within /var/log/amazon/ssm/*"
          sudo find /var/log/amazon/ssm -type f -exec rm -f {} \;
      fi
      if [[ $( sudo find /var/log/amazon/ssm -type f | sudo wc -l) -gt 0 ]]; then
          echo "Failed to delete /var/log/amazon/ssm"
          exit 1
      fi
      echo "Deleting /var/log/amazon/ssm/*"
      sudo rm -rf /var/log/amazon/ssm
      if [[ -d "/var/log/amazon/ssm" ]]; then
          echo "Failed to delete /var/log/amazon/ssm"
          exit 1
      fi
  fi
fi


# Clean up for DHCP lease files
shopt -s nullglob
DHCP_LEASE_MATCHES=(/var/db/dhcpclient/leases/*)
shopt -u nullglob
if [[ ${#DHCP_LEASE_MATCHES[@]} -gt 0 ]]; then
  echo "Deleting /var/db/dhcpclient/leases/*"
  sudo rm -f "${DHCP_LEASE_MATCHES[@]}"
  shopt -s nullglob
  DHCP_LEASE_REMAINING=(/var/db/dhcpclient/leases/*)
  shopt -u nullglob
  if [[ ${#DHCP_LEASE_REMAINING[@]} -gt 0 ]]; then
      echo "Failed to delete /var/db/dhcpclient/leases/*"
      exit 1
  fi
fi

if [[ $( sudo find /var/tmp -type f | sudo wc -l) -gt 0 ]]; then
      echo "Deleting files within /var/tmp/*"
      sudo find /var/tmp -type f -exec rm -f {} \;
fi
if [[ $( sudo find /var/tmp -type f | sudo wc -l) -gt 0 ]]; then
      echo "Failed to delete /var/tmp"
      exit 1
fi
if [[ $( sudo ls /var/tmp | sudo wc -l ) -gt 0 ]]; then
      echo "Deleting /var/tmp/*"
      sudo rm -rf /var/tmp/*
fi

# Flush all pending writes to disk before instance shutdown and snapshot
sync

```

## Override the Linux clean up script

Image Builder creates images that are secure by default and follow our security best
practices. However, some more advanced use-cases might require you to skip one
or more sections of the built-in clean up script. If you do need to skip
some of the clean up, we strongly recommend that you test your output AMI
to ensure the security of your image.

###### Important

Skipping sections in the clean up script can result in sensitive information,
such as owner account details or SSH keys being included in the final image, and
in any instance launched from that image. You might also experience problems
with launching in different Availability Zones, Regions, or accounts.

The following table outlines the sections of the clean up script, the files that
are deleted in that section, and the file names that you can use to flag a section that
Image Builder should skip. To skip a specific section of the clean up script, you can use
the [CreateFile](toe-action-modules.md#action-modules-createfile "toe-action-modules.md#action-modules-createfile")
component action module or a command in your user data (if overriding) to create
an empty file with the name specified in the **Skip section file name** column.

###### Note

The files that you create to skip a section of the clean up script should
not include a file extension. For example, if you want to skip the
`CLOUD_INIT_FILES` section of the script, but you create a file named
`skip_cleanup_cloudinit_files.txt`, Image Builder will not recognize
the skip file.

Input| Clean up section | Files removed | Skip section file name |
| --- | --- | --- |
| `CLOUD_INIT_FILES` | `/etc/sudoers.d/90-cloud-init-users`<br>`/etc/locale.conf`<br>`/var/log/cloud-init.log`<br>`/var/log/cloud-init-output.log`<br>All files under `/var/lib/cloud/` | `skip_cleanup_cloudinit_files` |
| `INSTANCE_FILES` | `/etc/.updated`<br>`/etc/aliases.db`<br>`/etc/hostname`<br>`/var/lib/misc/postfix.aliasesdb-stamp`<br>`/var/lib/postfix/master.lock`<br>`/var/spool/postfix/pid/master.pid`<br>`/var/.updated`<br>`/var/cache/yum/x86_64/2/.gpgkeyschecked.yum` | `skip_cleanup_instance_files` |
| `SSH_FILES` | `/etc/ssh/ssh_host_rsa_key`<br>`/etc/ssh/ssh_host_rsa_key.pub`<br>`/etc/ssh/ssh_host_ecdsa_key`<br>`/etc/ssh/ssh_host_ecdsa_key.pub`<br>`/etc/ssh/ssh_host_ed25519_key`<br>`/etc/ssh/ssh_host_ed25519_key.pub`<br>`/root/.ssh/authorized_keys`<br>`/home/<all users>/.ssh/authorized_keys` | `skip_cleanup_ssh_files` |
| `INSTANCE_LOG_FILES` | `/var/log/audit/audit.log`<br>`/var/log/boot.log`<br>`/var/log/dmesg`<br>`/var/log/cron` | `skip_cleanup_instance_log_files` |
| `TOE_FILES` | `{{workingDirectory}}/TOE_*` | `skip_cleanup_toe_files` |
| `SSM_LOG_FILES` | `/var/log/amazon/ssm/*` | `skip_cleanup_ssm_log_files` |

###### Clean up steps that always run

The sections in the preceding table are the only parts of the clean up script
that you can skip. After the script processes those sections, it also removes the
following items, and you can't skip these steps:

- `/var/log/sa/sa*`
- `/var/lib/dhclient/dhclient*.lease`
- All files under `/var/tmp/`
- `/var/lib/systemd/random-seed`
- `/var/lib/rsyslog/imjournal.state`
- All files under `/var/log/journal/`
  The script also truncates the machine ID files `/etc/machine-id`
  and `/var/lib/dbus/machine-id`. This ensures that each instance launched from
  the image generates a unique machine ID.

## Override the macOS clean up script

Image Builder creates images that are secure by default and follow our security best
practices. However, some more advanced use-cases might require you to skip one
or more sections of the built-in clean up script. If you do need to skip
some of the clean up, we strongly recommend that you test your output AMI
to ensure the security of your image.

###### Important

Skipping sections in the clean up script can result in sensitive information,
such as owner account details or SSH keys being included in the final image, and
in any instance launched from that image. You might also experience problems
with launching in different Availability Zones, Regions, or accounts.

The following table outlines the sections of the clean up script, the files that
are deleted in that section, and the file names that you can use to flag a section that
Image Builder should skip. To skip a specific section of the clean up script, you can use
the [CreateFile](toe-action-modules.md#action-modules-createfile "toe-action-modules.md#action-modules-createfile")
component action module or a command in your user data (if overriding) to create
an empty file with the name specified in the **Skip section file name** column.

###### Note

The files that you create to skip a section of the clean up script should
not include a file extension. For example, if you want to skip the
`INSTANCE_FILES` section of the script, but you create a file named
`skip_cleanup_instance_files.txt`, Image Builder will not recognize
the skip file.

Input| Clean up section | Files removed | Skip section file name |
| --- | --- | --- |
| `EC2_MACOS_INIT_FILES` | Runs `ec2-macos-init clean -all` to reset the EC2 macOS Init<br>instance history so the image behaves as a first boot. | `skip_cleanup_ec2_macos_init_files` |
| `INSTANCE_FILES` | `/Library/Preferences/SystemConfiguration/NetworkInterfaces.plist` | `skip_cleanup_instance_files` |
| `SSH_FILES` | `/etc/ssh/ssh_host_rsa_key`<br>`/etc/ssh/ssh_host_rsa_key.pub`<br>`/etc/ssh/ssh_host_ecdsa_key`<br>`/etc/ssh/ssh_host_ecdsa_key.pub`<br>`/etc/ssh/ssh_host_ed25519_key`<br>`/etc/ssh/ssh_host_ed25519_key.pub`<br>`/var/root/.ssh/authorized_keys`<br>`/Users/<all users>/.ssh/authorized_keys` | `skip_cleanup_ssh_files` |
| `INSTANCE_LOG_FILES` | `/var/log/amazon/ec2/ec2-macos-init.log`<br>`/var/log/amazon/ec2/ena-ethernet.log`<br>`/var/log/amazon/ec2/system-monitoring.log` | `skip_cleanup_instance_log_files` |
| `TOE_FILES` | `{{workingDirectory}}/TOE_*` | `skip_cleanup_toe_files` |
| `SSM_LOG_FILES` | `/var/log/amazon/ssm/*` | `skip_cleanup_ssm_log_files` |
