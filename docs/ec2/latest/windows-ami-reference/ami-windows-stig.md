

# STIG Hardened AWS Windows Server AMIs
<a name="ami-windows-stig"></a>

Security Technical Implementation Guides (STIGs) are the configuration standards created by the Defense Information Systems Agency (DISA) to secure information systems and software. DISA documents three levels of compliance risk, known as categories:
+ **Category I** — The highest level of risk. It covers the most severe risks, and includes any vulnerability that can result in a loss of confidentiality, availability, or integrity.
+ **Category II** — Medium risk.
+ **Category III** — Low risk.

Each compliance level includes all STIG settings from lower levels. This means that the highest level includes all applicable settings from all levels.

To ensure that your systems are compliant with STIG standards, you must install, configure, and test a variety of security settings. STIG Hardened EC2 Windows Server AMIs are pre-configured with over 160 required security settings. Amazon EC2 supports the following operating systems for STIG Hardened AMIs:
+ Windows Server 2025
+ Windows Server 2022
+ Windows Server 2019
+ Windows Server 2016

The STIG Hardened AMIs include updated Department of Defense (DoD) certificates to help you get started and achieve STIG compliance. STIG Hardened AMIs are available in all commercial AWS and GovCloud (US) Regions. You can launch instances from these AMIs directly from the Amazon EC2 console. They are billed using standard Windowspricing. There are no additional charges for using STIG Hardened AMIs.

The following sections list the STIG settings that Amazon applies to WindowsOperating Systems and components.

**Topics**
+ [Find a STIG Hardened AMI](#find-windows-stig-ami)
+ [Core and base operating systems](#base-os-stig)
+ [Microsoft .NET Framework 4.0 STIG Version 2 Release 7](#dotnet-os-stig)
+ [WindowsFirewall STIG Version 2 Release 2](#windows-firewall-stig)
+ [Internet Explorer (IE) 11 STIG Version 2 Release 6](#ie-os-stig)
+ [Microsoft Edge STIG Version 2 Release 4](#edge-stig)
+ [Microsoft Defender STIG Version 2 Release 7](#defender-stig)
+ [Version history](#stig-version-history)

## Find a STIG Hardened AMI
<a name="find-windows-stig-ami"></a>

You can search for a STIG Hardened EC2 Windows Server AMI when you launch an instance from the EC2 console, or you can search for an AMI in the CLI or in PowerShell, as follows.

**Name patterns for STIG Hardened Windows AMIs**
+ Windows\_Server-2025-English-STIG-Full-{{YYYY.MM.DD}}
+ Windows\_Server-2025-English-STIG-Core-{{YYYY.MM.DD}}
+ Windows\_Server-2022-English-STIG-Full-{{YYYY.MM.DD}}
+ Windows\_Server-2022-English-STIG-Core-{{YYYY.MM.DD}}
+ Windows\_Server-2019-English-STIG-Full-{{YYYY.MM.DD}}
+ Windows\_Server-2019-English-STIG-Core-{{YYYY.MM.DD}}
+ Windows\_Server-2016-English-STIG-Full-{{YYYY.MM.DD}}
+ Windows\_Server-2016-English-STIG-Core-{{YYYY.MM.DD}}

**Name patterns for NitroTPM STIG Hardened Windows AMIs**
+ TPM-Windows\_Server-2025-English-STIG-Full-{{YYYY.MM.DD}}
+ TPM-Windows\_Server-2025-English-STIG-Core-{{YYYY.MM.DD}}
+ TPM-Windows\_Server-2022-English-STIG-Full-{{YYYY.MM.DD}}
+ TPM-Windows\_Server-2022-English-STIG-Core-{{YYYY.MM.DD}}

------
#### [ Console ]

You can select an AMI from the **Community AMIs** tab when you launch an instance, as follows.

**Launch an EC2 instance with a STIG Hardened Windows Server AMI**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. Choose **Instances** from the navigation pane. This opens a list of your EC2 instances in the current AWS Region.

1. Choose **Launch instances** from the upper right corner above the list. This opens the **Launch an instance** page.

1. To find a STIG Hardened AMI, choose **Browse more AMIs** on the right side of the **Application and OS Images (Amazon Machine Image)** section. This displays an advanced AMI search.

1. Select the **Community AMIs** tab, and enter part or all of one of the following name patterns in the search bar. Our AMIs indicate that they are "provided by Amazon."
**Note**  
The date suffix for the AMI ({{YYYY.MM.DD}}) is the date when the latest version was created. You can search for the version without the date suffix.

------
#### [ AWS CLI ]

**Find the latest STIG AMIs**  
The following example retrieves a list of the latest STIG Hardened Windows Server AMIs.

```
aws ssm get-parameters-by-path \
    --path "/aws/service/ami-windows-latest" \
    --recursive \
    --query 'Parameters[*].{Name:Name,Value:Value}' \
    --output text | grep "Windows_Server-.*STIG" | sort
```

**Find a specific AMI**  
The following example retrieves STIG Hardened Windows Server AMIs by filtering on the AMI name, the owner, the platform, and the creation date (year and month). Output is formatted as a table with columns for the AMI name and image ID.

```
aws ec2 describe-images \
    --owners amazon \
    --filters \
        "Name=name,Values=*STIG*" \
        "Name=platform,Values=windows" \
        "Name=creation-date,Values={{2025-05}}*" \
    --query 'Images[].[Name,ImageId]' \
    --output text | sort
```

------
#### [ PowerShell ]

**Find the latest STIG AMIs**  
The following example retrieves a list of the latest STIG Hardened Windows Server AMIs.

```
Get-SSMLatestEC2Image `
    -Path ami-windows-latest `
    -ImageName *Windows_Server-*STIG* |
Sort-Object Name
```

**Note**  
If this command doesn't run in your environment, you might be missing a PowerShell module. For more information about this command, see [Get-SSMLatestEC2Image Cmdlet](https://docs.aws.amazon.com/powershell/v4/reference/items/Get-SSMLatestEC2Image.html).  
Alternatively, you can use the [CloudShell console](https://console.aws.amazon.com/cloudshell/home) and run `pwsh` to bring up a PowerShell prompt that already has all of the AWS tools installed. For more information, see the [AWS CloudShell User Guide](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html).

**Find a specific AMI**  


The following example retrieves STIG Hardened Windows Server AMIs by filtering on the AMI name, the owner, the platform, and the creation date (year and month). Output is formatted as a table with columns for the AMI name and image ID.

```
Get-EC2Image `
    -Owner amazon `
    -Filter @(
        @{Name = "name"; Values = @("*STIG*")}
        @{Name = "platform"; Values = @("amazon")}
        @{Name = "creation-date"; Values = @("{{2025}}*")}
    ) |
Sort-Object Name |
Format-Table Name, ImageID -AutoSize
```

------

## Core and base operating systems
<a name="base-os-stig"></a>

STIG Hardened EC2 AMIs are designed for use as standalone servers, and have the highest level of STIG settings applied.

The following list contains STIG settings that apply for STIG Hardened Windows AMIs. Not all settings apply in all cases. For example, some STIG settings might not apply to standalone servers. Organization-specific policies can also affect which settings apply, such as a requirement for administrators to review document settings.

For a complete list of Windows STIGs, see the [STIGs Document Library](https://public.cyber.mil/stigs/downloads/?_dl_facet_stigs=windows). For information about how to view the complete list, see [STIG Viewing Tools](https://public.cyber.mil/stigs/srg-stig-tools/).

### Windows Server 2025 STIG Version 1 Release 1
<a name="win-server-2025"></a>

This release includes the following STIG settings for Windows operating systems:

V-278082, V-278083, V-278084, V-278085, V-278098, V-278104, V-278110, V-278231, V-278015, V-278016, V-278019, V-278020, V-278021, V-278022, V-278023, V-278024, V-278025, V-278026, V-278033, V-278034, V-278035, V-278036, V-278037, V-278038, V-278039, V-278047, V-278048, V-278049, V-278050, V-278051, V-278052, V-278053, V-278054, V-278055, V-278056, V-278057, V-278058, V-278059, V-278060, V-278061, V-278062, V-278063, V-278064, V-278065, V-278066, V-278067, V-278068, V-278069, V-278070, V-278071, V-278072, V-278073, V-278074, V-278075, V-278076, V-278077, V-278078, V-278079, V-278080, V-278086, V-278088, V-278089, V-278091, V-278092, V-278093, V-278094, V-278095, V-278096, V-278097, V-278102, V-278103, V-278105, V-278106, V-278107, V-278108, V-278109, V-278111, V-278112, V-278113, V-278114, V-278115, V-278116, V-278117, V-278118, V-278119, V-278120, V-278122, V-278123, V-278124, V-278126, V-278127, V-278129, V-278130, V-278131, V-278165, V-278168, V-278169, V-278170, V-278171, V-278174, V-278180, V-278181, V-278182, V-278183, V-278184, V-278185, V-278187, V-278188, V-278189, V-278192, V-278193, V-278194, V-278195, V-278198, V-278199, V-278200, V-278201, V-278202, V-278203, V-278204, V-278205, V-278206, V-278209, V-278210, V-278211, V-278212, V-278213, V-278214, V-278218, V-278220, V-278221, V-278222, V-278223, V-278226, V-278227, V-278228, V-278229, V-278230, V-278232, V-278233, V-278234, V-278235, V-278236, V-278237, V-278238, V-278239, V-278240, V-278241, V-278243, V-278244, V-278245, V-278247, V-278248, V-278249, V-278251, V-278252, V-278253, V-278254, V-278255, V-278256, V-278257, V-278258, V-278259, V-278260, V-278261, V-278262, V-279916, V-279917, V-279918, V-279919, V-279920, V-279921, V-279922, V-279923, V-278040, V-278099, V-278100, V-278101, V-278121, V-278125, V-278128, V-278196, V-278215, V-278216, V-278217, V-278219, V-278225, V-278242, V-278246, and V-278250

### Windows Server 2022 STIG Version 2 Release 7
<a name="win-server-2022"></a>

This release includes the following STIG settings for Windows operating systems:

V-254335, V-254336, V-254337, V-254338, V-254351, V-254357, V-254363, V-254481, V-254247, V-254269, V-254270, V-254271, V-254272, V-254273, V-254274, V-254275, V-254276, V-254277, V-254278, V-254285, V-254286, V-254287, V-254288, V-254289, V-254290, V-254291, V-254292, V-254296, V-254297, V-254298, V-254299, V-254300, V-254301, V-254302, V-254303, V-254304, V-254305, V-254307, V-254309, V-254311, V-254312, V-254313, V-254314, V-254315, V-254316, V-254319, V-254320, V-254321, V-254322, V-254323, V-254324, V-254325, V-254326, V-254327, V-254328, V-254329, V-254330, V-254331, V-254332, V-254333, V-254334, V-254339, V-254341, V-254342, V-254344, V-254345, V-254346, V-254347, V-254348, V-254349, V-254350, V-254355, V-254356, V-254358, V-254359, V-254360, V-254361, V-254362, V-254364, V-254365, V-254366, V-254367, V-254368, V-254369, V-254370, V-254371, V-254372, V-254373, V-254375, V-254376, V-254377, V-254379, V-254380, V-254382, V-254383, V-254384, V-254431, V-254433, V-254434, V-254435, V-254436, V-254438, V-254439, V-254440, V-254442, V-254443, V-254444, V-254445, V-254447, V-254448, V-254449, V-254450, V-254451, V-254452, V-254453, V-254454, V-254455, V-254456, V-254459, V-254460, V-254461, V-254462, V-254463, V-254464, V-254468, V-254470, V-254471, V-254472, V-254473, V-254476, V-254477, V-254478, V-254479, V-254480, V-254482, V-254483, V-254484, V-254485, V-254486, V-254487, V-254488, V-254489, V-254491, V-254493, V-254494, V-254495, V-254497, V-254498, V-254499, V-254501, V-254502, V-254503, V-254504, V-254505, V-254506, V-254507, V-254508, V-254509, V-254510, V-254511, V-254512, V-278942, V-278943, V-278944, V-278945, V-278946, V-278947, V-278948, V-278949, V-254250, V-254293, V-254352, V-254353, V-254354, V-254374, V-254378, V-254381, V-254446, V-254466, V-254467, V-254469, V-254474, V-254475, V-254492, V-254496, and V-254500

### Windows Server 2019 STIG Version 3 Release 7
<a name="win-server-2019"></a>

This release includes the following STIG settings for Windows operating systems:

V-205691, V-205819, V-205858, V-205859, V-205860, V-205870, V-205871, V-205923, V-205625, V-205626, V-205627, V-205629, V-205630, V-205633, V-205634, V-205635, V-205636, V-205637, V-205638, V-205639, V-205640, V-205641, V-205642, V-205643, V-205644, V-205648, V-205649, V-205650, V-205651, V-205652, V-205655, V-205656, V-205659, V-205660, V-205662, V-205671, V-205672, V-205673, V-205675, V-205676, V-205678, V-205679, V-205680, V-205681, V-205682, V-205683, V-205684, V-205685, V-205686, V-205687, V-205688, V-205689, V-205690, V-205692, V-205693, V-205694, V-205697, V-205698, V-205708, V-205709, V-205712, V-205714, V-205716, V-205717, V-205718, V-205719, V-205720, V-205722, V-205730, V-205731, V-205733, V-205747, V-205748, V-205749, V-205751, V-205752, V-205754, V-205755, V-205756, V-205758, V-205759, V-205760, V-205761, V-205762, V-205763, V-205764, V-205765, V-205766, V-205767, V-205768, V-205769, V-205770, V-205771, V-205772, V-205773, V-205774, V-205775, V-205776, V-205777, V-205778, V-205779, V-205780, V-205781, V-205782, V-205783, V-205784, V-205795, V-205796, V-205797, V-205798, V-205801, V-205808, V-205809, V-205810, V-205811, V-205812, V-205813, V-205814, V-205815, V-205816, V-205817, V-205821, V-205822, V-205823, V-205824, V-205825, V-205826, V-205827, V-205828, V-205830, V-205832, V-205833, V-205835, V-205836, V-205837, V-205838, V-205842, V-205861, V-205863, V-205865, V-205866, V-205867, V-205868, V-205869, V-205872, V-205873, V-205874, V-205909, V-205910, V-205911, V-205912, V-205915, V-205916, V-205917, V-205918, V-205920, V-205921, V-205922, V-205925, V-257503, V-278934, V-278935, V-278936, V-278937, V-278938, V-278939, V-278940, V-278941, V-205653, V-205654, V-205663, V-205711, V-205713, V-205724, V-205725, V-205750, V-205753, V-205757, V-205802, V-205804, V-205805, V-205806, V-205849, V-205908, V-205914, and V-205919

### Windows Server 2016 STIG Version 2 Release 10
<a name="win-server-2016"></a>

This release includes the following STIG settings for Windows operating systems:

V-224916, V-224917, V-224918, V-224919, V-224931, V-224942, V-225060, V-224850, V-224852, V-224853, V-224854, V-224855, V-224856, V-224857, V-224858, V-224859, V-224866, V-224867, V-224868, V-224869, V-224870, V-224871, V-224872, V-224873, V-224881, V-224882, V-224883, V-224884, V-224885, V-224886, V-224887, V-224888, V-224889, V-224890, V-224891, V-224892, V-224893, V-224894, V-224895, V-224896, V-224897, V-224898, V-224899, V-224900, V-224901, V-224902, V-224903, V-224904, V-224905, V-224906, V-224907, V-224908, V-224909, V-224910, V-224911, V-224912, V-224913, V-224914, V-224915, V-224920, V-224922, V-224924, V-224925, V-224926, V-224927, V-224928, V-224929, V-224930, V-224935, V-224936, V-224937, V-224938, V-224939, V-224940, V-224941, V-224943, V-224944, V-224945, V-224946, V-224947, V-224948, V-224949, V-224951, V-224952, V-224953, V-224955, V-224956, V-224957, V-224959, V-224960, V-224962, V-224963, V-225010, V-225013, V-225014, V-225015, V-225016, V-225017, V-225018, V-225019, V-225021, V-225022, V-225023, V-225024, V-225028, V-225029, V-225030, V-225031, V-225032, V-225033, V-225034, V-225035, V-225038, V-225039, V-225040, V-225041, V-225042, V-225043, V-225047, V-225049, V-225050, V-225051, V-225052, V-225055, V-225056, V-225057, V-225058, V-225059, V-225061, V-225062, V-225063, V-225064, V-225065, V-225066, V-225067, V-225068, V-225069, V-225072, V-225073, V-225074, V-225076, V-225078, V-225080, V-225081, V-225082, V-225083, V-225084, V-225086, V-225087, V-225088, V-225089, V-225092, V-225093, V-236000, V-257502, V-224874, V-224932, V-224933, V-224934, V-224954, V-224958, V-224961, V-225025, V-225044, V-225045, V-225046, V-225048, V-225053, V-225054, and V-225079

## Microsoft .NET Framework 4.0 STIG Version 2 Release 7
<a name="dotnet-os-stig"></a>

The following list contains STIG settings that apply to Windows operating system components for STIG Hardened EC2 AMIs. The following list contains STIG settings that apply for STIG Hardened Windows AMIs. Not all settings apply in all cases. For example, some STIG settings might not apply to standalone servers. Organization-specific policies can also affect which settings apply, such as a requirement for administrators to review document settings.

For a complete list of Windows STIGs, see the [STIGs Document Library](https://public.cyber.mil/stigs/downloads/?_dl_facet_stigs=windows). For information about how to view the complete list, see [STIG Viewing Tools](https://public.cyber.mil/stigs/srg-stig-tools/).

**.NET Framework on Windows Server 2025, 2022, 2019, and 2016**  
V-225223, V-225230, V-225235, and V-225238

## WindowsFirewall STIG Version 2 Release 2
<a name="windows-firewall-stig"></a>

The following list contains STIG settings that apply to Windows operating system components for STIG Hardened EC2 AMIs. The following list contains STIG settings that apply for STIG Hardened Windows AMIs. Not all settings apply in all cases. For example, some STIG settings might not apply to standalone servers. Organization-specific policies can also affect which settings apply, such as a requirement for administrators to review document settings.

For a complete list of Windows STIGs, see the [STIGs Document Library](https://public.cyber.mil/stigs/downloads/?_dl_facet_stigs=windows). For information about how to view the complete list, see [STIG Viewing Tools](https://public.cyber.mil/stigs/srg-stig-tools/).

**WindowsFirewall on Windows Server 2025, 2022, 2019, and 2016**  
V-241994, V-241995, V-241996, V-241999, V-242000, V-242001, V-242006, V-242007, V-242008, V-241989, V-241990, V-241991, V-241993, V-241998, V-242003, V-241992, V-241997, and V-242002

## Internet Explorer (IE) 11 STIG Version 2 Release 6
<a name="ie-os-stig"></a>

The following list contains STIG settings that apply to Windows operating system components for STIG Hardened EC2 AMIs. The following list contains STIG settings that apply for STIG Hardened Windows AMIs. Not all settings apply in all cases. For example, some STIG settings might not apply to standalone servers. Organization-specific policies can also affect which settings apply, such as a requirement for administrators to review document settings.

For a complete list of Windows STIGs, see the [STIGs Document Library](https://public.cyber.mil/stigs/downloads/?_dl_facet_stigs=windows). For information about how to view the complete list, see [STIG Viewing Tools](https://public.cyber.mil/stigs/srg-stig-tools/).

**IE 11 on Windows Server 2022, 2019, and 2016**  
V-223016, V-223056, V-223078, V-223015, V-223017, V-223018, V-223019, V-223020, V-223021, V-223022, V-223023, V-223024, V-223025, V-223026, V-223027, V-223028, V-223029, V-223030, V-223031, V-223032, V-223033, V-223034, V-223035, V-223036, V-223037, V-223038, V-223039, V-223040, V-223041, V-223042, V-223043, V-223044, V-223045, V-223046, V-223048, V-223049, V-223050, V-223051, V-223052, V-223053, V-223054, V-223055, V-223057, V-223058, V-223059, V-223060, V-223061, V-223062, V-223063, V-223064, V-223065, V-223066, V-223067, V-223068, V-223069, V-223070, V-223071, V-223072, V-223073, V-223074, V-223075, V-223076, V-223077, V-223079, V-223080, V-223081, V-223082, V-223083, V-223084, V-223085, V-223086, V-223087, V-223088, V-223089, V-223090, V-223091, V-223092, V-223093, V-223094, V-223095, V-223096, V-223097, V-223098, V-223099, V-223100, V-223101, V-223102, V-223103, V-223104, V-223105, V-223106, V-223107, V-223108, V-223109, V-223110, V-223111, V-223112, V-223113, V-223114, V-223115, V-223116, V-223117, V-223118, V-223119, V-223120, V-223121, V-223122, V-223123, V-223124, V-223125, V-223126, V-223127, V-223128, V-223129, V-223130, V-223131, V-223132, V-223133, V-223134, V-223135, V-223136, V-223137, V-223138, V-223139, V-223140, V-223141, V-223142, V-223143, V-223144, V-223145, V-223146, V-223147, V-223148, V-223149, V-250540, V-250541, and V-252910

## Microsoft Edge STIG Version 2 Release 4
<a name="edge-stig"></a>

The following list contains STIG settings that apply to Windows operating system components for STIG Hardened EC2 AMIs. The following list contains STIG settings that apply for STIG Hardened Windows AMIs. Not all settings apply in all cases. For example, some STIG settings might not apply to standalone servers. Organization-specific policies can also affect which settings apply, such as a requirement for administrators to review document settings.

For a complete list of Windows STIGs, see the [STIGs Document Library](https://public.cyber.mil/stigs/downloads/?_dl_facet_stigs=windows). For information about how to view the complete list, see [STIG Viewing Tools](https://public.cyber.mil/stigs/srg-stig-tools/).

**Microsoft Edge on Windows Server 2022 and 2025**  
V-235727, V-235731, V-235751, V-235752, V-235765, V-235720, V-235721, V-235723, V-235724, V-235725, V-235726, V-235728, V-235729, V-235730, V-235732, V-235733, V-235734, V-235735, V-235736, V-235737, V-235738, V-235739, V-235740, V-235741, V-235742, V-235743, V-235744, V-235745, V-235746, V-235747, V-235748, V-235749, V-235750, V-235754, V-235756, V-235760, V-235761, V-235763, V-235764, V-235766, V-235767, V-235768, V-235769, V-235770, V-235771, V-235772, V-235773, V-235774, V-246736, V-235758, and V-235759

## Microsoft Defender STIG Version 2 Release 7
<a name="defender-stig"></a>

The following list contains STIG settings that apply to Windows operating system components for STIG Hardened EC2 AMIs. The following list contains STIG settings that apply for STIG Hardened Windows AMIs. Not all settings apply in all cases. For example, some STIG settings might not apply to standalone servers. Organization-specific policies can also affect which settings apply, such as a requirement for administrators to review document settings.

For a complete list of Windows STIGs, see the [STIGs Document Library](https://public.cyber.mil/stigs/downloads/?_dl_facet_stigs=windows). For information about how to view the complete list, see [STIG Viewing Tools](https://public.cyber.mil/stigs/srg-stig-tools/).

**Microsoft Defender on Windows Server 2022 and 2025**  
V-213427, V-213429, V-213430, V-213431, V-213432, V-213433, V-213434, V-213435, V-213436, V-213437, V-213438, V-213439, V-213440, V-213441, V-213442, V-213443, V-213444, V-213445, V-213446, V-213447, V-213448, V-213449, V-213450, V-213451, V-213454, V-213455, V-213456, V-213457, V-213458, V-213459, V-213460, V-213461, V-213462, V-213463, V-213464, V-213465, V-213466, V-278647, V-278648, V-278649, V-278650, V-278651, V-278652, V-278653, V-278654, V-278655, V-278656, V-278658, V-278659, V-278660, V-278661, V-278662, V-278668, V-278669, V-278672, V-278674, V-278675, V-278676, V-278677, V-278678, V-278679, V-278680, V-278863, V-213426, V-213428, V-213452, and V-213453

## Version history
<a name="stig-version-history"></a>

The following table provides version history updates for STIG settings that are applied to Windowsoperating systems and Windowscomponents.


| Date | AMIs | Details | 
| --- | --- | --- | 
| 05/14/2026 | Windows Server 2025 STIG Version 1 Release 1 | Added support for Windows Server 2025 with STIG Version 1 Release 1 applied. | 
| 03/12/2026 | Windows Server 2022 STIG Version 2 Release 7<br />Windows Server 2019 STIG Version 3 Release 7<br />Windows Server 2016 STIG Version 2 Release 10<br />Windows Server 2012 R2 MS STIG Version 3 Release 5<br />Microsoft .NET Framework 4.0 STIG Version 2 Release 7<br />WindowsFirewall STIG Version 2 Release 2<br />Internet Explorer 11 STIG Version 2 Release 6<br />Microsoft Edge STIG Version 2 Release 4<br />Microsoft Defender STIG Version 2 Release 7 | Updated all applicable STIGs to first quarter 2026 releases. | 
| 06/19/2025 | Windows Server 2022 STIG Version 2 Release 4<br />Windows Server 2019 STIG Version 3 Release 4<br />Windows Server 2016 STIG Version 2 Release 10<br />Windows Server 2012 R2 MS STIG Version 3 Release 5<br />Microsoft .NET Framework 4.0 STIG Version 2 Release 6<br />WindowsFirewall STIG Version 2 Release 2<br />Internet Explorer 11 STIG Version 2 Release 5<br />Microsoft Edge STIG Version 2 Release 2<br />Microsoft Defender STIG Version 2 Release 4 | AMIs released for 2025 Q1 and Q2 with updated versions where applicable, and applied STIGs. | 
| 03/06/2025 | Windows Server 2022 STIG Version 2 Release 2<br />Windows Server 2019 STIG Version 3 Release 2<br />Windows Server 2016 STIG Version 2 Release 9<br />Windows Server 2012 R2 MS STIG Version 3 Release 5<br />Microsoft .NET Framework 4.0 STIG Version 2 Release 2<br />WindowsFirewall STIG Version 2 Release 2<br />Internet Explorer 11 STIG Version 2 Release 5<br />Microsoft Edge STIG Version 2 Release 2<br />Microsoft Defender STIG Version 2 Release 4 | AMIs released for 2024 Q4 with updated versions where applicable, and applied STIGs. | 
| 04/24/2023 | Windows Server 2022 STIG Version 1 Release 1<br />Microsoft Edge STIG Version 1 Release 6<br />Microsoft Defender STIG Version 2 Release 4 | Added support for Windows Server 2022, Microsoft Edge, and Microsoft Defender. | 
| 03/01/2023 | Windows Server 2019 STIG Version 2 Release 5<br />Windows Server 2016 STIG Version 2 Release 5<br />Windows Server 2012 R2 MS STIG Version 3 Release 5<br />Microsoft .NET Framework 4.0 STIG Version 2 Release 2<br />WindowsFirewall STIG Version 2 Release 1<br />Internet Explorer 11 STIG Version 2 Release 3 | AMIs released for 2022 Q4 with updated versions where applicable, and applied STIGs. | 
| 07/21/2022 | Windows Server 2019 STIG Version 2 R4<br />Windows Server 2016 STIG Version 2 R4<br />Windows Server 2012 R2 MS STIG Version 3 R3<br />Microsoft .NET Framework 4.0 STIG Version 2 R1<br />WindowsFirewall STIG Version 2 R1<br />Internet Explorer 11 STIG V1 R19 | AMIs released with updated versions where applicable, and applied STIGs. | 
| 12/15/2021 | Windows Server 2019 STIG Version 2 R3<br />Windows Server 2016 STIG Version 2 R3<br />Windows Server 2012 R2 STIG Version 3 R3<br />Microsoft .NET Framework 4.0 STIG Version 2 R1<br />WindowsFirewall STIG Version 2 R1<br />Internet Explorer 11 STIG V1 R19 | AMIs released with updated versions where applicable, and applied STIGs. | 
| 6/9/2021 | Windows Server 2019 STIG Version 2 R2<br />Windows Server 2016 STIG Version 2 R2<br />Windows Server 2012 R2 STIG Version 3 R2<br />Microsoft .NET Framework 4.0 STIG Version 2 R1<br />WindowsFirewall STIG V1 R7<br />Internet Explorer 11 STIG V1 R19 | Updated versions where applicable, and applied STIGs. | 
| 4/5/2021 | Windows Server 2019 STIG Version 2 R 1<br />Windows Server 2016 STIG Version 2 R 1<br />Windows Server 2012 R2 STIG Version 3 R 1<br />Microsoft .NET Framework 4.0 STIG Version 2 R 1<br />WindowsFirewall STIG V1 R 7<br />Internet Explorer 11 STIG V1 R 19 | Updated versions where applicable, and applied STIGs. | 
| 9/18/2020 | Windows Server 2019 STIG V1 R 5<br />Windows Server 2016 STIG V1 R 12<br />Windows Server 2012 R2 STIG Version 2 R 19<br />Internet Explorer 11 STIG V1 R 19<br />Microsoft .NET Framework 4.0 STIG V1 R 9<br />WindowsFirewall STIG V1 R 7 | Updated versions and applied STIGs. | 
| 12/6/2019 | Server 2012 R2 Core and Base V2 R17<br />Server 2016 Core and Base V1 R11<br />Internet Explorer 11 V1 R18<br />Microsoft .NET Framework 4.0 V1 R9<br />WindowsFirewall STIG V1 R17 | Updated versions and applied STIGs. | 
| 9/17/2019 | Server 2012 R2 Core and Base V2 R16<br />Server 2016 Core and Base V1 R9<br />Server 2019 Core and Base V1 R2<br />Internet Explorer 11 V1 R17<br />Microsoft .NET Framework 4.0 V1 R8 | Initial release. | 