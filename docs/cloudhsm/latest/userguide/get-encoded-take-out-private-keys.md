# Allow the JCE provider to extract private key
 secrets out of AWS CloudHSM

Use the following steps to allow AWS CloudHSM JCE provider to extract your private key
 secrets.

###### Important

This configuration change allows extraction of all `EXTRACTABLE` key bytes in clear from your HSM cluster. For better security, 
 you should consider using [key wrapping methods](java-lib-supported_5.md "java-lib-supported_5.md") to extract the key out of the HSM securely. This prevents unintentional extraction of your key bytes from the HSM. 

1. Use the following commands to enable your **private** or **secret** keys to be extracted in JCE:



Linux

```

`$` `/opt/cloudhsm/bin/configure-jce --enable-clear-key-extraction-in-software`
```


Windows

```

`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\bin\configure-jce.exe" --enable-clear-key-extraction-in-software`
```
2. Once you enable your clear key extraction, the following methods are enabled for extracting private keys into memory.




| Class | Method | Format (getEncoded) |
| --- | --- | --- |
| Key | getEncoded() | RAW |
| ECPrivateKey | getEncoded() | PKCS#8 |
|  | getS() | N/A |
| RSAPrivateCrtKey | getEncoded() | X.509 |
|  | getPrivateExponent() | N/A |
|  | getPrimeP() | N/A |
|  | getPrimeQ() | N/A |
|  | getPrimeExponentP() | N/A |
|  | getPrimeExponentQ() | N/A |
|  | getCrtCoefficient() | N/A | If you want restore the default behavior and not allow JCE to export keys in clear, run the following command: Linux ``` `$` `/opt/cloudhsm/bin/configure-jce --disable-clear-key-extraction-in-software` ``` Windows ``` `PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\bin\configure-jce.exe" --disable-clear-key-extraction-in-software` ```
