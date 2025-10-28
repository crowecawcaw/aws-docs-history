# Control Objective 6: Keys are administered in a secure manner.

_Requirement 21:_ Key storage and use with AWS Payment Cryptography was assessed as part of the
service’s PCI PIN assessment. For key component related storage requirements, you are responsible to store them as delineated
under 21-2 and 21-3. You will need to describe key protection mechanisms in your policy documentation prior to import
to and after export from the service.

_Requirement 22:_ Key compromise procedures for AWS Payment Cryptography were assessed as part of
the service’s PCI PIN assessment. You will need to describe key compromise detection and response procedures, including
[monitoring and response to notification from AWS](https://aws.amazon.com/security-incident-response/ "https://aws.amazon.com/security-incident-response/").

_Requirement 23:_ AWS Payment Cryptography does not support variants or other reversible key calculation methods. APC main
keys or keys enciphered by them are never available to customers. Use of reversible key calculation was assessed as part of
the service's PCI PIN assessment.

_Requirement 24:_ Destruction practices for internal secret and private keys AWS Payment Cryptography
was assessed as part of the service’s PCI PIN assessment. You will need to describe key destruction procedure for keys prior
to import to and after export from APC. Key component related destruction requirements (24-2.2 and 24-2.3) remain your responsibility.

_Requirement 25:_ Access to secret and private keys within AWS Payment Cryptography was assessed as part of
the service's PCI PIN assessment. You will need to have a process and documentation for access controls for keys prior to import to
and after export from AWS Payment Cryptography.

_Requirement 26:_ You will need to describe logging for any access to keys, key components, or related
materials used outside of the service. Logs for all key management activities that your application does with the service are
available via AWS CloudTrail.

_Requirement 27:_ You will need to describe backup procedures for keys, key components, or related
materials used outside of the service.

_Requirement 28:_ Procedures for all key administration using the API should include use of roles with
key administration permissions and approvals for running scripts or other code that manages keys. AWS CloudTrail logs contain all key
administration events
