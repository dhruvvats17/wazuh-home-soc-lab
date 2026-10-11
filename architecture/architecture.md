# Lab Architecture

## Components
- **Windows 11 endpoint:** Wazuh Agent, Sysmon, Windows Event Logs, and configured security/firewall telemetry.
- **Ubuntu Server:** Wazuh Manager, Indexer, and Dashboard.
- **Kali Linux:** separate testing machine used only for authorized lab simulations.
- **Analyst:** reviews events and alerts in Wazuh, validates evidence, and documents findings.

## Event flow
1. Windows records events through Windows logging and Sysmon.
2. The Wazuh Agent forwards configured event data to the Wazuh Manager.
3. The Manager evaluates received events against decoders and rules.
4. Relevant alert data is indexed and presented in the Dashboard.
5. The analyst validates the alert and reviews supporting events before reaching a conclusion.

The exact log sources and ports depend on the installed configuration. Confirm them on the live system before documenting them as enabled.

## Network notes

Private lab addresses are intentionally not included in this public repository. Use placeholders in any future examples, and publish only sanitized evidence.

## Trust boundaries
- Keep the testing machine and target systems within the authorized lab.
- Do not expose the Wazuh dashboard or management services directly to the public internet.
- Redact credentials, personal identifiers, and unnecessary internal addressing from evidence.
