

# PCoIP-based WorkSpaces Personal end of support
<a name="workspaces-pcoip-end-of-support"></a>

After careful consideration, we decided to end support for PCoIP-based WorkSpaces Personal, effective October 31, 2027. PCoIP-based WorkSpaces Personal will no longer accept new customers beginning July 31, 2026. As an existing customer with an account signed up for the service before July 30, 2026, you can continue to use PCoIP-based WorkSpaces Personal features. After October 31, 2027, you will no longer be able to use PCoIP-based WorkSpaces Personal.

## What AWS will continue to do before October 31, 2027
<a name="pcoip-eos-continued-support"></a>

Through October 31, 2027, your existing PCoIP WorkSpaces remain fully supported. During this period, AWS will:
+ Keep PCoIP-based WorkSpaces available and accessible for end users.
+ Apply security patches and critical bug fixes to the PCoIP service components in coordination with HP.
+ Provide AWS Support for operational issues on PCoIP WorkSpaces.
+ Send recurring reminders through AWS Health notifications with the count of PCoIP WorkSpaces remaining in your account, so you can track migration progress.
+ Continue to invest in migration tooling to make the transition to DCV as seamless as possible.

All new feature development across Amazon WorkSpaces is focused on DCV. AWS will not add new features or new operating system support to the PCoIP protocol.

## Migrate to Amazon DCV
<a name="pcoip-eos-migrate-to-dcv"></a>

Amazon DCV is the high-performance streaming protocol built by AWS and is now the single protocol for WorkSpaces Personal. By migrating to DCV, you gain:
+ Broader operating system support, including Windows 11 and Windows Server 2025.
+ Enhanced security features, such as certificate-based authentication and WebAuthN.
+ Improved streaming performance.
+ A unified streaming experience across all WorkSpaces services, which simplifies client management, troubleshooting, and administrator training.

DCV is included at no additional charge — WorkSpaces pricing is unchanged.

## How to migrate your PCoIP WorkSpaces to DCV
<a name="pcoip-eos-how-to-migrate"></a>

Two pathways cover most environments. Pathway 1 is for WorkSpaces on a current operating system (OS); Pathway 2 is for WorkSpaces on an OS at or near end-of-life. If your users also connect through PCoIP Zero Clients, plan a hardware refresh in parallel — see [Replace PCoIP Zero Client hardware](#pcoip-eos-zero-clients).

### Before you start
<a name="pcoip-eos-before-you-start"></a>

1. **Configure the required network paths for DCV:** DCV uses different ports and IP ranges than PCoIP. Update security groups, firewalls, and any on-premises routes so end-user clients and WorkSpaces can reach the DCV gateways for authentication and streaming. For the current list of ports and IP ranges, see [IP address and port requirements for WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html).

1. **Install a supported DCV client:** Make sure end users are on a currently supported client version — Windows and macOS 5.22.1 or later, Linux 2025.1\+ for Ubuntu 24.04 or 2025.0\+ for Ubuntu 22.04 or 20.04, latest Chrome, Firefox, or Edge for Web Access, and the WorkSpaces Progressive Web App (PWA) for iOS, Android, and Chromebook users. Download the latest client from the [WorkSpaces client download page](https://clients.amazonworkspaces.com/).

1. **Run a pilot:** Select 5 to 10 WorkSpaces that represent your different user personas and migrate those first. Validate application compatibility, peripherals, printing, and network performance before scaling up.

### Pathway 1: WorkSpaces on a supported OS
<a name="pcoip-eos-pathway-1"></a>

Use this pathway when your WorkSpaces are running a supported OS — for example, Windows Server 2019, 2022, or 2025, or a supported Linux distribution — and you only need to switch the streaming protocol. The WorkSpace keeps its OS, applications, data, and user profile; only the streaming protocol changes. You can do this using the Modify protocol feature.

**Modify protocol of an individual WorkSpace using the AWS Management Console**

1. Open the Amazon WorkSpaces console.

1. In the navigation pane, choose **WorkSpaces**.

1. Select the PCoIP WorkSpace to migrate and choose **Actions**, **Modify Protocol**.

1. Confirm to proceed.

1. It can take up to 40 minutes for the modification to complete. During the modification, the WorkSpace Status will show as *Modifying Protocol*.

1. To confirm completion, verify the WorkSpace's Protocol property has changed to DCV (WSP).

You can also modify the protocol using the AWS CLI or API. For more information, see [Modify protocols](https://docs.aws.amazon.com/workspaces/latest/adminguide/modify-workspaces.html#modify_protocols) in the Amazon WorkSpaces Personal Administration Guide.

**Error recovery**  
Every migration takes a pre-migration snapshot. In a rare scenario, if migration fails, the system automatically retries. If the retry also fails, the WorkSpace is automatically restored to the pre-migration snapshot with the PCoIP protocol to ensure no data is lost. A WorkSpace that has already been migrated to DCV can revert to PCoIP using the AWS CLI or API if needed.

### Pathway 2: WorkSpaces on an OS at or near end-of-life
<a name="pcoip-eos-pathway-2"></a>

Use this pathway if your WorkSpaces are running an OS that is at or near end-of-life, such as Windows 10 BYOL, Windows Server 2016, or Amazon Linux 2. You can migrate to a newer OS and DCV bundle in a single step using the Migrate WorkSpace feature. Combining the OS upgrade with the protocol change avoids duplicate testing and migration work.

The Migrate WorkSpace feature recreates the WorkSpace using a new root volume from the target WorkSpaces bundle image and the user volume from the most recent snapshot of the original WorkSpace. Before you migrate, confirm that the target bundle includes a current OS image with the applications your users need.

**To migrate a WorkSpace**

1. If you use Windows BYOL, first create a BYOL DCV bundle on the target operating system. See [Bring Your Own Windows desktop license](https://docs.aws.amazon.com/workspaces/latest/adminguide/byol-windows-images.html). For public AWS bundles, no bundle creation is needed.

1. In the Amazon WorkSpaces console, select the WorkSpace and choose **Actions**, **Migrate WorkSpace**.

1. Choose the target DCV bundle and confirm.

   1. For Windows: The user profile on the D: drive is preserved from the most recent snapshot. Applications and files on the C: drive are not transferred. Notify end users before you migrate so they can back up anything stored on C: drive.

   1. For Linux: Data on the /home directory is preserved from the most recent snapshot. Applications and files on other paths are not transferred. Notify end users before you migrate so they can back up anything not stored in their /home directory.

You can also migrate using the AWS CLI or API. For details, see [Migrate a WorkSpace](https://docs.aws.amazon.com/workspaces/latest/adminguide/migrate-workspaces.html) in the Amazon WorkSpaces Personal Administration Guide.

## Replace PCoIP Zero Client hardware
<a name="pcoip-eos-zero-clients"></a>

PCoIP Zero Clients cannot support DCV given their proprietary hardware level integration with the PCoIP protocol. Users connecting with Zero Clients will need to replace the endpoint devices before October 31, 2027.

For the current list of qualified thin client endpoint devices, see [supported devices for WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/userguide/amazon-workspaces-clients.html). Conduct a proof-of-concept before deploying any new endpoint device at scale to validate performance, peripheral support, and compliance requirements in your environment.

## Need help or have questions?
<a name="pcoip-eos-help"></a>

If you have additional questions about the PCoIP WorkSpaces end of support or your migration to DCV, contact AWS Support or reach out to your AWS account manager for assistance.

## FAQs
<a name="pcoip-eos-faq"></a>

**Why is AWS ending support for PCoIP-based WorkSpaces?**  
HP, the owner of PCoIP technology, has announced the end-of-life of HP Anyware, which includes the PCoIP protocol. Because the underlying technology will no longer be supported by its vendor, AWS is ending support for PCoIP-based WorkSpaces Personal and consolidating on Amazon DCV, the AWS-built streaming protocol that already powers all other Amazon WorkSpaces services.

**Does this change affect DCV-based WorkSpaces Personal?**  
No. This change only applies to PCoIP-based WorkSpaces Personal.

**What happens to my PCoIP WorkSpaces on October 31, 2027 if I haven't migrated?**  
After October 31, 2027, you will not be able to create or connect to PCoIP WorkSpaces. We strongly recommend completing migration well before this date to avoid any disruptions or data loss.

**As an existing PCoIP WorkSpaces customer, can I continue to create new PCoIP WorkSpaces?**  
Yes. Existing PCoIP WorkSpaces customers can continue to create new PCoIP WorkSpaces until October 31, 2027. We recommend planning your migration to Amazon DCV well in advance of this date to avoid disruption.

**Does this apply to AWS GovCloud (US) and other regions?**  
Yes, the PCoIP WorkSpaces end of support applies to all AWS Regions, including AWS GovCloud (US).

**Is there an additional cost to migrate to DCV?**  
No. There is no additional charge for using DCV, and WorkSpaces pricing is unchanged. The migration itself does not incur any additional cost.