# Known issues for AWS CloudHSM integration Java
 Keytool and Jarsigner using Client SDK 3

The following list provides the current list of known issues for integrations with AWS CloudHSM and
 Java Keytool and Jarsigner using Client SDK 3. 


* When generating keys using keytool, the first provider in provider
 configuration cannot be CaviumProvider.
* When generating keys using keytool, the first (supported) provider in the
 security configuration file is used to generate the key. This is generally a
 software provider. The generated key is then given an alias and imported into
 the AWS CloudHSM HSM as a persistent (token) key during the key addition process.
* When using keytool with AWS CloudHSM key store, do not specify
 `-providerName`, `-providerclass`, or
 `-providerpath` options on the command line. Specify these
 options in the security provider file as described in the [Key store prerequisites](keystore-prerequisites.md "keystore-prerequisites.md").
* When using non-extractable EC keys through keytool and Jarsigner, the SunEC
 provider needs to be removed/disabled from the list of providers in the
 java.security file. If you use extractable EC keys through keytool and
 Jarsigner, the providers export key bits from the AWS CloudHSM HSM and use the key
 locally for signing operations. We do not recommend you use exportable keys with
 keytool or Jarsigner.
