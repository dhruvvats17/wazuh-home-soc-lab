# Case 001 — SSH Brute-Force Test

**Case status:** Author-reported test; dedicated screenshot/raw alert export pending  
**Environment:** Owned home lab only  
**Expected data source:** SSH authentication logs and the relevant Wazuh alert

## Summary
The project owner reports that an SSH brute-force test and alert were verified in the lab. The evidence set included with this repository did not contain a dedicated SSH alert screenshot or raw alert export, so this case is not presented as independently evidenced here.

## Investigation checklist
1. Record the exact test time and the source/target roles in the lab.
2. Find the corresponding SSH authentication failures on the target.
3. Inspect the Wazuh alert fields: timestamp, agent, rule ID, level, source address, username, and decoder/rule description.
4. Check whether failures are repeated within a short time window and whether a successful login follows.
5. Correlate the Wazuh alert with the original authentication log.
6. Export the alert JSON and redact usernames, IP addresses, and other private details before committing evidence.
7. Repeat only against a system owned by the project owner or where explicit permission exists.

## Assessment
**Status: author-reported, evidence pending.** Do not describe this case as independently verified in the public portfolio until a dedicated screenshot or sanitized event export is added.

## Evidence to add
- Wazuh alert detail showing the relevant SSH rule.
- Target authentication log excerpt for the same time range.
- Test notes with timestamp, lab source/target role, expected result, and observed result.
