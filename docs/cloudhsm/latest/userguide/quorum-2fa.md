# Quorum authentication and 2FA in AWS CloudHSM clusters using AWS CloudHSM

Management Utility

The cluster uses the same key for quorum authentication and for two-factor authentication
2FA). This means a user with 2FA enabled is effectively registered for M-of-N-access-control
(MofN). To successfully use 2FA and quorum authentication for the same HSM user, consider the
following points:

- If you are using quorum authentication for a user today, you should use the same key pair
  you created for the quorum user to enable 2FA for the user.
- If you add the 2FA requirement for a non-2FA user that is not a quorum authentication
  user, then you register that user as an MofN user with 2FA authentication.
- If you remove the 2FA requirement or change the password for a 2FA user that is also a
  quorum authentication user, you will also remove the registration of the quorum user as an
  MofN user.
- If you remove the 2FA requirement or change the password for a 2FA user that is also a
  quorum authentication user, but you _still want that user to
  participate in quorum authentication_, then you must register that user again as an
  MofN user.
  For more information about quorum authentication, see [Using CMU to manage quorum authentication](quorum-authentication.md "quorum-authentication.md").
