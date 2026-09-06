

**AWS Mainframe Modernization self-managed experience** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization self-managed experience, explore capabilities from vendor-direct offerings and from AWS Transform. Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

**AWS Mainframe Modernization Service (Managed Runtime Environment experience)** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

# Supported source and target encodings in AWS Mainframe Modernization File Transfer
<a name="filetransfer-encodings"></a>

AWS Mainframe Modernization File Transfer supports various data set types and code page conversion options.

## Mainframe data set types
<a name="filetransfer-encodings-dataset-types"></a>

AWS Mainframe Modernization File Transfer supports the following mainframe data set types:
+ Non-VSAM: Sequential (PS), PDS, GDS, GDG
+ VSAM types: KSDS

## Supported code pages
<a name="filetransfer-encodings-codepages"></a>

AWS Mainframe Modernization File Transfer supports the following code pages for data set conversion (from/to):

"BIG5" , "BIG5\_HKSCS" , "CESU\_8" , "EUC\_JP" , "EUC\_KR" , "GB18030" , "GB2312" , "GBK" , "IBM00858" , "IBM01140" , "IBM01141" , "IBM01142", "IBM01143" , "IBM01144" , "IBM01145" , "IBM01146" , "IBM01147" , "IBM01148" , "IBM01149" , "IBM037" , "IBM1026" , "IBM1047" , "IBM273" , "IBM277" , "IBM278" , "IBM280" , "IBM284" , "IBM285" , "IBM290" , "IBM297" , "IBM420" , "IBM424" , "IBM437" , "IBM500" , "IBM775" , "IBM850" , "IBM852" , "IBM855" , "IBM857" , "IBM860" , "IBM861" , "IBM862" , "IBM863" , "IBM864" , "IBM865" , "IBM866" , "IBM868" , "IBM869" , "IBM870" , "IBM871" , "IBM918" , "IBM\_THAI" , "ISO\_2022\_CN" , "ISO\_2022\_JP" , "ISO\_2022\_JP\_2" , "ISO\_2022\_KR" , "ISO\_8859\_1" , "ISO\_8859\_13" , "ISO\_8859\_15" , "ISO\_8859\_16" , "ISO\_8859\_2" , "ISO\_8859\_3" , "ISO\_8859\_4" , "ISO\_8859\_5" , "ISO\_8859\_6" , "ISO\_8859\_7" , "ISO\_8859\_8" , "ISO\_8859\_9" ,"JIS\_X0201" , "JIS\_X0212\_1990" , "KOI8\_R" , "KOI8\_U" , "SHIFT\_JIS" , "TIS\_620" , "US\_ASCII" , "UTF\_16" , "UTF\_16BE" , "UTF\_16LE" , "UTF\_32" , "UTF\_32BE" , "UTF\_32LE" , "UTF\_8" , "WINDOWS\_1250" , "WINDOWS\_1251" , "WINDOWS\_1252" , "WINDOWS\_1253" ,"WINDOWS\_1254" , "WINDOWS\_1255" , "WINDOWS\_1256" , "WINDOWS\_1257" , "WINDOWS\_1258" , "WINDOWS\_31J" , "X\_BIG5\_HKSCS\_2001" , "X\_BIG5\_SOLARIS" , "X\_EUCJP\_OPEN" , "X\_EUC\_JP\_LINUX" , "X\_EUC\_TW" , "X\_IBM1006" , "X\_IBM1025" , "X\_IBM1046" , "X\_IBM1097" , "X\_IBM1098" , "X\_IBM1112" , "X\_IBM1122" , "X\_IBM1123" , "X\_IBM1124" , "X\_IBM1129" , "X\_IBM1166" , "X\_IBM1364" , "X\_IBM1381" , "X\_IBM1383" , "X\_IBM29626C" , "X\_IBM300" , "X\_IBM33722" , "X\_IBM737" , "X\_IBM833" , "X\_IBM834" , "X\_IBM856" , "X\_IBM874" , "X\_IBM875" , "X\_IBM921" , "X\_IBM922" , "X\_IBM930" , "X\_IBM933" , "X\_IBM935" , "X\_IBM937" , "X\_IBM939" , "X\_IBM942" , "X\_IBM942C" , "X\_IBM943" , "X\_IBM943C" , "X\_IBM948" , "X\_IBM949" , "X\_IBM949C" , "X\_IBM950" , "X\_IBM964" , "X\_IBM970" , "X\_ISCII91" , "X\_ISO\_2022\_CN\_CNS" , "X\_ISO\_2022\_CN\_GB" , "X\_ISO\_8859\_11" , "X\_JIS0208" , "X\_JISAUTODETECT" , "X\_JOHAB", "X\_MACARABIC" , "X\_MACCENTRALEUROPE" , "X\_MACCROATIAN" , "X\_MACCYRILLIC" , "X\_MACDINGBAT", "X\_MACGREEK" , "X\_MACHEBREW" , "X\_MACICELAND" , "X\_MACROMAN" , "X\_MACROMANIA" , "X\_MACSYMBOL" , "X\_MACTHAI" , "X\_MACTURKISH" , "X\_MACUKRAINE" , "X\_MS932\_0213" , "X\_MS950\_HKSCS" , "X\_MS950\_HKSCS\_XP" , "X\_MSWIN\_936" , "X\_PCK" , "X\_SJIS\_0213" , "X\_UTF\_16LE\_BOM" , "X\_UTF\_32BE\_BOM" , "X\_UTF\_32LE\_BOM" , "X\_WINDOWS\_50220" , "X\_WINDOWS\_50221" , "X\_WINDOWS\_874" , "X\_WINDOWS\_949" , "X\_WINDOWS\_950" , "X\_WINDOWS\_ISO2022j"