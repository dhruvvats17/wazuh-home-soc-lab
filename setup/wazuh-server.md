# Wazuh Server Setup Notes

## Purpose
Document the Ubuntu Server that hosts Wazuh Manager, Indexer, and Dashboard.

## Known lab notes
- Ubuntu Server was used as the SIEM host.
- Wazuh components were installed and the Dashboard was accessible.
- The lab notes recorded Wazuh version 4.14.7. Confirm the current version before publishing a screenshot.

## Record the current environment
Run these commands on the server and record sanitized output:

```bash
lsb_release -a
sudo systemctl status wazuh-manager --no-pager
sudo systemctl status wazuh-indexer --no-pager
sudo systemctl status wazuh-dashboard --no-pager
sudo /var/ossec/bin/wazuh-control info
```

Some service names or commands may vary by installation. If a command is unavailable, check the installed package/service names rather than claiming it succeeded.

## Validation checklist
- [ ] Dashboard loads from an authorized local network.
- [ ] Manager, Indexer, and Dashboard services are healthy.
- [ ] Windows endpoint appears in the agent list.
- [ ] Recent events arrive from the expected log sources.
- [ ] Screenshots are redacted before publication.

## Security
Do not publish passwords, certificates, private keys, API credentials, or full private configuration files.
