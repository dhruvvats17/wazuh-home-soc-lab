# MITRE ATT&CK Mapping

MITRE ATT&CK is a knowledge base of adversary tactics and techniques. Map only observed behavior and cite the relevant technique reference in the final report.

| Observed behavior | Possible mapping | Mapping rule |
|---|---|---|
| Repeated password guesses against SSH | Credential Access — Brute Force (T1110), potentially a relevant sub-technique | Use only if the test evidence supports password guessing; distinguish failed attempts from successful access. |
| Network service discovery/port scan | Discovery — Network Service Discovery (T1046) | Apply only if scan behavior was observed and the mapping fits the test. |
| Process creation event | No automatic mapping | A process event alone is not evidence of adversary behavior. More context is required. |

Reference: https://attack.mitre.org/

A mapping is an analytical classification, not proof that an attack succeeded. Re-check technique descriptions and IDs before final publication.
