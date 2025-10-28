# STIG Hardened AWS Windows Server AMIs

Security Technical Implementation Guides (STIGs) are the configuration standards created
by the Defense Information Systems Agency (DISA) to secure information systems and software.
DISA documents three levels of compliance risk, known as categories:

- **Category I** — The highest level of risk. It
  covers the most severe risks, and includes any vulnerability that can result in a
  loss of confidentiality, availability, or integrity.
- **Category II** — Medium risk.
- **Category III** — Low risk.
  Each compliance level includes all STIG settings from lower levels. This means that the
  highest level includes all applicable settings from all levels.

To ensure that your systems are compliant with STIG standards, you must install,
configure, and test a variety of security settings. STIG Hardened EC2 Windows Server AMIs
are pre-configured with over 160 required security settings. Amazon EC2 supports the following
operating systems for STIG Hardened AMIs:

- Windows Server 2022
- Windows Server 2019
- Windows Server 2016
- Windows Server 2012 R2
  The STIG Hardened AMIs include updated Department of Defense (DoD) certificates to help you
  get started and achieve STIG compliance. STIG Hardened AMIs are available in all commercial
  AWS and GovCloud (US) Regions. You can launch instances from these AMIs
  directly from the Amazon EC2 console. They are billed using standard Windowspricing. There are
  no additional charges for using STIG Hardened AMIs.

The following sections list the STIG settings that Amazon applies to WindowsOperating Systems
and components.

###### Topics

- [Find a STIG Hardened AMI](#find-windows-stig-ami "#find-windows-stig-ami")
- [Core and base operating systems](#base-os-stig "#base-os-stig")
- [Microsoft .NET Framework 4.0 STIG Version 2 Release 6](#dotnet-os-stig "#dotnet-os-stig")
- [WindowsFirewall STIG Version 2 Release 2](#windows-firewall-stig "#windows-firewall-stig")
- [Internet Explorer (IE) 11 STIG Version 2 Release 5](#ie-os-stig "#ie-os-stig")
- [Microsoft Edge STIG Version 2 Release 2](#edge-stig "#edge-stig")
- [Microsoft Defender STIG Version 2 Release 4](#defender-stig "#defender-stig")
- [Version history](#stig-version-history "#stig-version-history")

## Find a STIG Hardened AMI

You can search for a STIG Hardened EC2 Windows Server AMI when you launch an instance from
the EC2 console, or you can search for an AMI in the CLI or in PowerShell, as follows.

###### Name patterns for STIG Hardened Windows AMIs

- Windows_Server-2022-English-STIG-Full-`YYYY.MM.DD`
- Windows_Server-2022-English-STIG-Core-`YYYY.MM.DD`
- Windows_Server-2019-English-STIG-Full-`YYYY.MM.DD`
- Windows_Server-2019-English-STIG-Core-`YYYY.MM.DD`
- Windows_Server-2016-English-STIG-Full-`YYYY.MM.DD`
- Windows_Server-2016-English-STIG-Core-`YYYY.MM.DD`
- Windows_Server-2012-R2-English-STIG-Full-`YYYY.MM.DD`
- Windows_Server-2012-R2-English-STIG-Core-`YYYY.MM.DD`

Console
You can select an AMI from the **Community AMIs** tab when you
launch an instance, as follows.

###### Launch an EC2 instance with a STIG Hardened Windows Server AMI

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. Choose **Instances** from the navigation pane. This opens
   a list of your EC2 instances in the current AWS Region.
3. Choose **Launch instances** from the upper right corner above
   the list. This opens the **Launch an instance** page.
4. To find a STIG Hardened AMI, choose **Browse more AMIs** on the
   right side of the **Application and OS Images (Amazon Machine Image)**
   section. This displays an advanced AMI search.
5. Select the **Community AMIs** tab, and enter part or all of one of the
   following name patterns in the search bar. Our AMIs indicate that they are "provided
   by Amazon."

###### Note

The date suffix for the AMI (`YYYY.MM.DD`) is the date when
the latest version was created. You can search for the version without the date
suffix.

AWS CLI

###### Find the latest STIG AMIs

The following example retrieves a list of the latest STIG Hardened Windows Server AMIs.

```
`aws ssm get-parameters-by-path \
 --path "/aws/service/ami-windows-latest" \
 --recursive \
 --query 'Parameters[*].{Name:Name,Value:Value}' \
 --output text | grep "Windows_Server-.*STIG" | sort`
```

###### Find a specific AMI

The following example retrieves STIG Hardened Windows Server AMIs by
filtering on the AMI name, the owner, the platform, and the creation date
(year and month). Output is formatted as a table with columns for the AMI name
and
image ID.

```
`aws ec2 describe-images \
 --owners amazon \
 --filters \
 "Name=name,Values=*STIG*" \
 "Name=platform,Values=windows" \
 "Name=creation-date,Values=`2025-05`*" \
 --query 'Images[].[Name,ImageId]' \
 --output text | sort`
```

PowerShell

###### Find the latest STIG AMIs

The following example retrieves a list of the latest STIG Hardened Windows Server AMIs.

```
`Get-SSMLatestEC2Image `
 -Path ami-windows-latest `
 -ImageName *Windows_Server-*STIG* | `
Sort-Object Name`
```

###### Note

If this command doesn't run in your environment, you might be missing a PowerShell module. For
more information about this command, see [Get-SSMLatestEC2Image Cmdlet](../../../powershell/v4/reference/items/Get-SSMLatestEC2Image.md "../../../powershell/v4/reference/items/Get-SSMLatestEC2Image.md").

Alternatively, you can use the [CloudShell console](https://console.aws.amazon.com/cloudshell/home "https://console.aws.amazon.com/cloudshell/home")
and run `pwsh` to bring up a PowerShell prompt that already has all of the AWS tools installed.
For more information, see the [AWS CloudShell User Guide](../../../cloudshell/latest/userguide/welcome.md "../../../cloudshell/latest/userguide/welcome.md").

###### Find a specific AMI

The following example retrieves STIG Hardened Windows Server AMIs by filtering
on the AMI name, the owner, the platform, and the creation date (year and month).
Output is formatted as a table with columns for the AMI name and
image ID.

```
`Get-EC2Image `
 -Owner amazon `
 -Filter @(
 @{Name = "name"; Values = @("*STIG*")},
 @{Name = "owner-alias"; Values = @("amazon")},
 @{Name = "platform"; Values = "windows"},
 @{Name = "creation-date"; Values = @("`2025-05`*")}
 ) | `
Sort-Object Name |`
Format-Table Name, ImageID -AutoSize`
```

## Core and base operating systems

STIG Hardened EC2 AMIs are designed for use as standalone servers, and have the
highest level of STIG settings applied.

The following list contains STIG settings that apply for STIG Hardened
Windows AMIs. Not all settings apply in all cases. For example, some STIG settings might
not apply to standalone servers. Organization-specific policies can also affect which
settings apply, such as a requirement for administrators to review document settings.

For a complete list of Windows STIGs, see the [STIGs
Document Library](https://public.cyber.mil/stigs/downloads/?_dl_facet_stigs=windows "https://public.cyber.mil/stigs/downloads/?_dl_facet_stigs=windows"). For information about how to view the complete list, see [STIG Viewing Tools](https://public.cyber.mil/stigs/srg-stig-tools/ "https://public.cyber.mil/stigs/srg-stig-tools/").

This release includes the following STIG settings for Windows operating systems:

V-254335, V-254336, V-254337, V-254338, V-254351, V-254357, V-254363, V-254481,
V-254247, V-254265, V-254269, V-254270, V-254271, V-254272, V-254273, V-254274,
V-254276, V-254277, V-254278, V-254285, V-254286, V-254287, V-254288, V-254289,
V-254290, V-254291, V-254292, V-254300, V-254301, V-254302, V-254303, V-254304,
V-254305, V-254306, V-254307, V-254308, V-254309, V-254310, V-254311, V-254312,
V-254313, V-254314, V-254315, V-254316, V-254317, V-254318, V-254319, V-254320,
V-254321, V-254322, V-254323, V-254324, V-254325, V-254326, V-254327, V-254328,
V-254329, V-254330, V-254331, V-254332, V-254333, V-254334, V-254339, V-254341,
V-254342, V-254344, V-254345, V-254346, V-254347, V-254348, V-254349, V-254350,
V-254355, V-254356, V-254356, V-254358, V-254359, V-254360, V-254361, V-254362,
V-254364, V-254365, V-254366, V-254367, V-254368, V-254369, V-254370, V-254371,
V-254372, V-254373, V-254375, V-254376, V-254377, V-254379, V-254380, V-254382,
V-254383, V-254384, V-254431, V-254432, V-254433, V-254434, V-254435, V-254436,
V-254438, V-254439, V-254442, V-254443, V-254444, V-254445, V-254449, V-254450,
V-254451, V-254452, V-254453, V-254454, V-254455, V-254456, V-254459, V-254460,
V-254461, V-254462, V-254463, V-254464, V-254468, V-254470, V-254471, V-254472,
V-254473, V-254476, V-254477, V-254478, V-254479, V-254480, V-254482, V-254483,
V-254484, V-254485, V-254486, V-254487, V-254488, V-254489, V-254490, V-254493,
V-254494, V-254495, V-254497, V-254499, V-254501, V-254502, V-254503, V-254504,
V-254505, V-254507, V-254508, V-254509, V-254510, V-254511, V-254512, V-254293,
V-254352, V-254353, V-254354, V-254374, V-254378, V-254381, V-254446, V-254465,
V-254466, V-254467, V-254469, V-254474, V-254475, and V-254500

This release includes the following STIG settings for Windows operating systems:

V-205691, V-205819, V-205858, V-205859, V-205860, V-205870, V-205871, V-205923,
V-205625, V-205626, V-205627, V-205629, V-205630, V-205633, V-205634, V-205635,
V-205636, V-205637, V-205638, V-205639, V-205643, V-205644, V-205648, V-205649,
V-205650, V-205651, V-205652, V-205655, V-205656, V-205659, V-205660, V-205662,
V-205671, V-205672, V-205673, V-205675, V-205676, V-205678, V-205679, V-205680,
V-205681, V-205682, V-205683, V-205684, V-205685, V-205686, V-205687, V-205688,
V-205689, V-205690, V-205692, V-205693, V-205694, V-205697, V-205698, V-205708,
V-205709, V-205712, V-205714, V-205716, V-205717, V-205718, V-205719, V-205720,
V-205722, V-205729, V-205730, V-205733, V-205747, V-205751, V-205752, V-205754,
V-205756, V-205758, V-205759, V-205760, V-205761, V-205762, V-205764, V-205765,
V-205766, V-205767, V-205768, V-205769, V-205770, V-205771, V-205772, V-205773,
V-205774, V-205775, V-205776, V-205777, V-205778, V-205779, V-205780, V-205781,
V-205782, V-205783, V-205784, V-205795, V-205796, V-205797, V-205798, V-205801,
V-205808, V-205809, V-205810, V-205811, V-205812, V-205813, V-205814, V-205815,
V-205816, V-205817, V-205821, V-205822, V-205823, V-205824, V-205825, V-205826,
V-205827, V-205828, V-205830, V-205832, V-205833, V-205834, V-205835, V-205836,
V-205837, V-205838, V-205839, V-205840, V-205841, V-205842, V-205861, V-205863,
V-205865, V-205866, V-205867, V-205868, V-205869, V-205872, V-205873, V-205874,
V-205911, V-205912, V-205915, V-205916, V-205917, V-205918, V-205920, V-205921,
V-205922, V-205924, V-205925, V-236001, V-257503, V-205653, V-205654, V-205711,
V-205713, V-205724, V-205725, V-205757, V-205802, V-205804, V-205805, V-205806,
V-205849, V-205908, V-205913, V-205914, and V-205919

This release includes the following STIG settings for Windows operating systems:

V-224916, V-224917, V-224918, V-224919, V-224931, V-224942, V-225060, V-224850,
V-224852, V-224853, V-224854, V-224855, V-224856, V-224857, V-224858, V-224859,
V-224866, V-224867, V-224868, V-224869, V-224870, V-224871, V-224872, V-224873,
V-224881, V-224882, V-224883, V-224884, V-224885, V-224886, V-224887, V-224888,
V-224889, V-224890, V-224891, V-224892, V-224893, V-224894, V-224895, V-224896,
V-224897, V-224898, V-224899, V-224900, V-224901, V-224902, V-224903, V-224904,
V-224905, V-224906, V-224907, V-224908, V-224909, V-224910, V-224911, V-224912,
V-224913, V-224914, V-224915, V-224920, V-224922, V-224924, V-224925, V-224926,
V-224927, V-224928, V-224929, V-224930, V-224935, V-224936, V-224937, V-224938,
V-224939, V-224940, V-224941, V-224943, V-224944, V-224945, V-224946, V-224947,
V-224948, V-224949, V-224951, V-224952, V-224953, V-224955, V-224956, V-224957,
V-224959, V-224960, V-224962, V-224963, V-225010, V-225013, V-225014, V-225015,
V-225016, V-225017, V-225018, V-225019, V-225021, V-225022, V-225023, V-225024,
V-225028, V-225029, V-225030, V-225031, V-225032, V-225033, V-225034, V-225035,
V-225038, V-225039, V-225040, V-225041, V-225042, V-225043, V-225047, V-225049,
V-225050, V-225051, V-225052, V-225055, V-225056, V-225057, V-225058, V-225059,
V-225061, V-225062, V-225063, V-225064, V-225065, V-225066, V-225067, V-225068,
V-225069, V-225072, V-225073, V-225074, V-225076, V-225078, V-225080, V-225081,
V-225082, V-225083, V-225084, V-225086, V-225087, V-225088, V-225089, V-225092,
V-225093, V-236000, V-257502, V-224874, V-224932, V-224933, V-224934, V-224954,
V-224958, V-224961, V-225025, V-225044, V-225045, V-225046, V-225048, V-225053,
V-225054, and V-225079

This release includes the following STIG settings for Windows operating systems:

V-225250, V-225318, V-225319, V-225324, V-225327, V-225328, V-225330, V-225331,
V-225332, V-225333, V-225334, V-225335, V-225336, V-225342, V-225343, V-225355,
V-225357, V-225358, V-225359, V-225360, V-225362, V-225363, V-225376, V-225392,
V-225394, V-225412, V-225459, V-225460, V-225462, V-225468, V-225473, V-225476,
V-225479, V-225480, V-225481, V-225482, V-225483, V-225484, V-225485, V-225487,
V-225488, V-225489, V-225490, V-225511, V-225514, V-225525, V-225526, V-225536,
V-225537, V-225239, V-225259, V-225260, V-225261, V-225263, V-225264, V-225265,
V-225266, V-225267, V-225268, V-225269, V-225270, V-225271, V-225272, V-225273,
V-225275, V-225276, V-225277, V-225278, V-225279, V-225280, V-225281, V-225282,
V-225283, V-225284, V-225285, V-225286, V-225287, V-225288, V-225289, V-225290,
V-225291, V-225292, V-225293, V-225294, V-225295, V-225296, V-225297, V-225298,
V-225299, V-225300, V-225301, V-225302, V-225303, V-225304, V-225305, V-225314,
V-225315, V-225316, V-225317, V-225325, V-225326, V-225329, V-225337, V-225338,
V-225339, V-225340, V-225341, V-225344, V-225345, V-225346, V-225347, V-225348,
V-225349, V-225350, V-225351, V-225352, V-225353, V-225356, V-225367, V-225368,
V-225369, V-225370, V-225371, V-225372, V-225373, V-225374, V-225375, V-225377,
V-225378, V-225379, V-225380, V-225381, V-225382, V-225383, V-225384, V-225385,
V-225386, V-225389, V-225391, V-225393, V-225395, V-225397, V-225398, V-225400,
V-225401, V-225402, V-225404, V-225405, V-225406, V-225407, V-225408, V-225409,
V-225410, V-225411, V-225413, V-225414, V-225415, V-225441, V-225442, V-225443,
V-225448, V-225452, V-225453, V-225454, V-225455, V-225456, V-225457, V-225458,
V-225461, V-225463, V-225464, V-225469, V-225470, V-225471, V-225472, V-225474,
V-225475, V-225477, V-225478, V-225486, V-225494, V-225500, V-225501, V-225502,
V-225503, V-225504, V-225506, V-225508, V-225509, V-225510, V-225513, V-225515,
V-225516, V-225517, V-225518, V-225519, V-225520, V-225521, V-225522, V-225523,
V-225524, V-225527, V-225528, V-225529, V-225530, V-225531, V-225532, V-225533,
V-225534, V-225535, V-225538, V-225539, V-225540, V-225541, V-225542, V-225543,
V-225544, V-225545, V-225546, V-225548, V-225549, V-225550, V-225551, V-225553,
V-225554, V-225555, V-225557, V-225558, V-225559, V-225560, V-225561, V-225562,
V-225563, V-225564, V-225565, V-225566, V-225567, V-225568, V-225569, V-225570,
V-225571, V-225572, V-225573, V-225574, V-225274, V-225354, V-225364, V-225365,
V-225366, V-225390, V-225396, V-225399, V-225444, V-225449, V-225491, V-225492,
V-225493, V-225496, V-225497, V-225498, V-225505, V-225507, V-225547, V-225552,
and V-225556

## Microsoft .NET Framework 4.0 STIG Version 2 Release 6

The following list contains STIG settings that apply to
Windows operating system components for STIG Hardened EC2 AMIs. The following list contains STIG settings that apply for STIG Hardened
Windows AMIs. Not all settings apply in all cases. For example, some STIG settings might
not apply to standalone servers. Organization-specific policies can also affect which
settings apply, such as a requirement for administrators to review document settings.

For a complete list of Windows STIGs, see the [STIGs
Document Library](https://public.cyber.mil/stigs/downloads/?_dl_facet_stigs=windows "https://public.cyber.mil/stigs/downloads/?_dl_facet_stigs=windows"). For information about how to view the complete list, see [STIG Viewing Tools](https://public.cyber.mil/stigs/srg-stig-tools/ "https://public.cyber.mil/stigs/srg-stig-tools/").

###### .NET Framework on Windows Server 2019, 2016, and 2012 R2 MS

V-225238

## WindowsFirewall STIG Version 2 Release 2

The following list contains STIG settings that apply to
Windows operating system components for STIG Hardened EC2 AMIs. The following list contains STIG settings that apply for STIG Hardened
Windows AMIs. Not all settings apply in all cases. For example, some STIG settings might
not apply to standalone servers. Organization-specific policies can also affect which
settings apply, such as a requirement for administrators to review document settings.

For a complete list of Windows STIGs, see the [STIGs
Document Library](https://public.cyber.mil/stigs/downloads/?_dl_facet_stigs=windows "https://public.cyber.mil/stigs/downloads/?_dl_facet_stigs=windows"). For information about how to view the complete list, see [STIG Viewing Tools](https://public.cyber.mil/stigs/srg-stig-tools/ "https://public.cyber.mil/stigs/srg-stig-tools/").

###### WindowsFirewall on Windows Server 2022, 2019, 2016, and 2012 R2 MS

V-241994, V-241995, V-241996, V-241999, V-242000, V-242001, V-242006, V-242007,
V-242008, V-241989, V-241990, V-241991, V-241993, V-241998, V-242003, V-241992,
V-241997, and V-242002

## Internet Explorer (IE) 11 STIG Version 2 Release 5

The following list contains STIG settings that apply to
Windows operating system components for STIG Hardened EC2 AMIs. The following list contains STIG settings that apply for STIG Hardened
Windows AMIs. Not all settings apply in all cases. For example, some STIG settings might
not apply to standalone servers. Organization-specific policies can also affect which
settings apply, such as a requirement for administrators to review document settings.

For a complete list of Windows STIGs, see the [STIGs
Document Library](https://public.cyber.mil/stigs/downloads/?_dl_facet_stigs=windows "https://public.cyber.mil/stigs/downloads/?_dl_facet_stigs=windows"). For information about how to view the complete list, see [STIG Viewing Tools](https://public.cyber.mil/stigs/srg-stig-tools/ "https://public.cyber.mil/stigs/srg-stig-tools/").

###### IE 11 on Windows Server 2022, 2019, 2016, and 2012 R2 MS

V-223016, V-223056, V-223078, V-223015, V-223017, V-223018, V-223019, V-223020,
V-223021, V-223022, V-223023, V-223024, V-223025, V-223026, V-223027, V-223028,
V-223029, V-223030, V-223031, V-223032, V-223033, V-223034, V-223035, V-223036,
V-223037, V-223038, V-223039, V-223040, V-223041, V-223042, V-223043, V-223044,
V-223045, V-223046, V-223048, V-223049, V-223050, V-223051, V-223052, V-223053,
V-223054, V-223055, V-223057, V-223058, V-223059, V-223060, V-223061, V-223062,
V-223063, V-223064, V-223065, V-223066, V-223067, V-223068, V-223069, V-223070,
V-223071, V-223072, V-223073, V-223074, V-223075, V-223076, V-223077, V-223079,
V-223080, V-223081, V-223082, V-223083, V-223084, V-223085, V-223086, V-223087,
V-223088, V-223089, V-223090, V-223091, V-223092, V-223093, V-223094, V-223095,
V-223096, V-223097, V-223098, V-223099, V-223100, V-223101, V-223102, V-223103,
V-223104, V-223105, V-223106, V-223107, V-223108, V-223109, V-223110, V-223111,
V-223112, V-223113, V-223114, V-223115, V-223116, V-223117, V-223118, V-223119,
V-223120, V-223121, V-223122, V-223123, V-223124, V-223125, V-223126, V-223127,
V-223128, V-223129, V-223130, V-223131, V-223132, V-223133, V-223134, V-223135,
V-223136, V-223137, V-223138, V-223139, V-223140, V-223141, V-223142, V-223143,
V-223144, V-223145, V-223146, V-223147, V-223148, V-223149, V-250540, V-250541,
and V-252910

## Microsoft Edge STIG Version 2 Release 2

The following list contains STIG settings that apply to
Windows operating system components for STIG Hardened EC2 AMIs. The following list contains STIG settings that apply for STIG Hardened
Windows AMIs. Not all settings apply in all cases. For example, some STIG settings might
not apply to standalone servers. Organization-specific policies can also affect which
settings apply, such as a requirement for administrators to review document settings.

For a complete list of Windows STIGs, see the [STIGs
Document Library](https://public.cyber.mil/stigs/downloads/?_dl_facet_stigs=windows "https://public.cyber.mil/stigs/downloads/?_dl_facet_stigs=windows"). For information about how to view the complete list, see [STIG Viewing Tools](https://public.cyber.mil/stigs/srg-stig-tools/ "https://public.cyber.mil/stigs/srg-stig-tools/").

###### Microsoft Edge on Windows Server 2022

V-235727, V-235731, V-235751, V-235752, V-235765, V-235720, V-235721, V-235723,
V-235724, V-235725, V-235726, V-235728, V-235729, V-235730, V-235732, V-235733,
V-235734, V-235735, V-235736, V-235737, V-235738, V-235739, V-235740, V-235741,
V-235742, V-235743, V-235744, V-235745, V-235746, V-235747, V-235748, V-235749,
V-235750, V-235754, V-235756, V-235760, V-235761, V-235763, V-235764, V-235766,
V-235767, V-235768, V-235769, V-235770, V-235771, V-235772, V-235773, V-235774,
V-246736, V-235758, and V-235759

## Microsoft Defender STIG Version 2 Release 4

The following list contains STIG settings that apply to
Windows operating system components for STIG Hardened EC2 AMIs. The following list contains STIG settings that apply for STIG Hardened
Windows AMIs. Not all settings apply in all cases. For example, some STIG settings might
not apply to standalone servers. Organization-specific policies can also affect which
settings apply, such as a requirement for administrators to review document settings.

For a complete list of Windows STIGs, see the [STIGs
Document Library](https://public.cyber.mil/stigs/downloads/?_dl_facet_stigs=windows "https://public.cyber.mil/stigs/downloads/?_dl_facet_stigs=windows"). For information about how to view the complete list, see [STIG Viewing Tools](https://public.cyber.mil/stigs/srg-stig-tools/ "https://public.cyber.mil/stigs/srg-stig-tools/").

###### Microsoft Defender on Windows Server 2022

V-213427, V-213429, V-213430, V-213431, V-213432, V-213433, V-213434, V-213435,
V-213436, V-213437, V-213438, V-213439, V-213440, V-213441, V-213442, V-213443,
V-213444, V-213445, V-213446, V-213447, V-213448, V-213449, V-213450, V-213451,
V-213455, V-213464, V-213465, V-213466, V-213426, V-213452, and V-213453

## Version history

The following table provides version history updates for STIG settings that are applied
to Windowsoperating systems and Windowscomponents.

| Date       | AMIs                                                                                                                                                                                                                                                                                                                                                                                                                        | Details                                                                                     |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| 06/19/2025 | Windows Server 2022 STIG Version 2 Release 4 Windows Server 2019 STIG Version 3 Release 4 Windows Server 2016 STIG Version 2 Release 10 Windows Server 2012 R2 MS STIG Version 3 Release 5 Microsoft .NET Framework 4.0 STIG Version 2 Release 6 WindowsFirewall STIG Version 2 Release 2 Internet Explorer 11 STIG Version 2 Release 5 Microsoft Edge STIG Version 2 Release 2 Microsoft Defender STIG Version 2 Release 4 | AMIs released for 2025 Q1 and Q2 with updated versions where applicable, and applied STIGs. |
| 03/06/2025 | Windows Server 2022 STIG Version 2 Release 2 Windows Server 2019 STIG Version 3 Release 2 Windows Server 2016 STIG Version 2 Release 9 Windows Server 2012 R2 MS STIG Version 3 Release 5 Microsoft .NET Framework 4.0 STIG Version 2 Release 2 WindowsFirewall STIG Version 2 Release 2 Internet Explorer 11 STIG Version 2 Release 5 Microsoft Edge STIG Version 2 Release 2 Microsoft Defender STIG Version 2 Release 4  | AMIs released for 2024 Q4 with updated versions where applicable, and applied STIGs.        |
| 04/24/2023 | Windows Server 2022 STIG Version 1 Release 1 Microsoft Edge STIG Version 1 Release 6 Microsoft Defender STIG Version 2 Release 4                                                                                                                                                                                                                                                                                            | Added support for Windows Server 2022, Microsoft Edge, and Microsoft Defender.              |
| 03/01/2023 | Windows Server 2019 STIG Version 2 Release 5 Windows Server 2016 STIG Version 2 Release 5 Windows Server 2012 R2 MS STIG Version 3 Release 5 Microsoft .NET Framework 4.0 STIG Version 2 Release 2 WindowsFirewall STIG Version 2 Release 1 Internet Explorer 11 STIG Version 2 Release 3                                                                                                                                   | AMIs released for 2022 Q4 with updated versions where applicable, and applied STIGs.        |
| 07/21/2022 | Windows Server 2019 STIG Version 2 R4 Windows Server 2016 STIG Version 2 R4 Windows Server 2012 R2 MS STIG Version 3 R3 Microsoft .NET Framework 4.0 STIG Version 2 R1 WindowsFirewall STIG Version 2 R1 Internet Explorer 11 STIG V1 R19                                                                                                                                                                                   | AMIs released with updated versions where applicable, and applied STIGs.                    |
| 12/15/2021 | Windows Server 2019 STIG Version 2 R3 Windows Server 2016 STIG Version 2 R3 Windows Server 2012 R2 STIG Version 3 R3 Microsoft .NET Framework 4.0 STIG Version 2 R1 WindowsFirewall STIG Version 2 R1 Internet Explorer 11 STIG V1 R19                                                                                                                                                                                      | AMIs released with updated versions where applicable, and applied STIGs.                    |
| 6/9/2021   | Windows Server 2019 STIG Version 2 R2 Windows Server 2016 STIG Version 2 R2 Windows Server 2012 R2 STIG Version 3 R2 Microsoft .NET Framework 4.0 STIG Version 2 R1 WindowsFirewall STIG V1 R7 Internet Explorer 11 STIG V1 R19                                                                                                                                                                                             | Updated versions where applicable, and applied STIGs.                                       |
| 4/5/2021   | Windows Server 2019 STIG Version 2 R 1 Windows Server 2016 STIG Version 2 R 1 Windows Server 2012 R2 STIG Version 3 R 1 Microsoft .NET Framework 4.0 STIG Version 2 R 1 WindowsFirewall STIG V1 R 7 Internet Explorer 11 STIG V1 R 19                                                                                                                                                                                       | Updated versions where applicable, and applied STIGs.                                       |
| 9/18/2020  | Windows Server 2019 STIG V1 R 5 Windows Server 2016 STIG V1 R 12 Windows Server 2012 R2 STIG Version 2 R 19 Internet Explorer 11 STIG V1 R 19 Microsoft .NET Framework 4.0 STIG V1 R 9 WindowsFirewall STIG V1 R 7                                                                                                                                                                                                          | Updated versions and applied STIGs.                                                         |
| 12/6/2019  | Server 2012 R2 Core and Base V2 R17 Server 2016 Core and Base V1 R11 Internet Explorer 11 V1 R18 Microsoft .NET Framework 4.0 V1 R9 WindowsFirewall STIG V1 R17                                                                                                                                                                                                                                                             | Updated versions and applied STIGs.                                                         |
| 9/17/2019  | Server 2012 R2 Core and Base V2 R16 Server 2016 Core and Base V1 R9 Server 2019 Core and Base V1 R2 Internet Explorer 11 V1 R17 Microsoft .NET Framework 4.0 V1 R8                                                                                                                                                                                                                                                          | Initial release.                                                                            |
