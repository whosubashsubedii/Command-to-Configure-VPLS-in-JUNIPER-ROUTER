


# Juniper VPLS Configuration Generator

This Python script helps network engineers generate configuration commands for setting up **VPLS (Virtual Private LAN Service)** on Juniper routers.

## 🔧 What It Does

- Collects input for:
  - VPLS instance name
  - Aggregated Ethernet interface name (e.g., `ae6`)
  - VLAN ID
  - (Optional) One or more neighbor IPs for VPLS peering

- Generates Junos configuration commands automatically.

## ✅ Prerequisites

- Python 3.x installed on your system.
- Basic knowledge of Juniper networking and VPLS concepts.

## 🚀 How to Run

1. Open a terminal and run the script:

   ```bash
   python vpls_config_generator.py
````

2. Follow the prompts:

   ```
   Enter the name of VPLS: Customer1-VPLS
   Enter the aggregated ethernet name (e.g., ae6): ae6
   Enter the VLAN: 200
   Do you want to configure a neighbor? (yes/no): yes
   Enter neighbor IP: 192.0.2.1
   Add another neighbour? (yes/no): no
   ```

3. The script will output the configuration block:

   ```bash
   ### The Command to configure VPLS in JUNIPER ROUTER ###

   configure private

   set interfaces ae6 unit 200 description Customer1-VPLS
   set interfaces ae6 unit 200 encapsulation vlan-vpls
   set interfaces ae6 unit 200 vlan-id 200
   set interfaces ae6 unit 200 family vpls
   set routing-instances Customer1-VPLS interface ae6.200
   set routing-instances Customer1-VPLS protocols vpls vpls-id 200
   set routing-instances Customer1-VPLS description Customer1-VPLS
   set routing-instances Customer1-VPLS instance-type vpls
   set routing-instances Customer1-VPLS protocols vpls no-tunnel-services
   set routing-instances Customer1-VPLS protocols vpls vpls-id 200
   set routing-instances Customer1-VPLS protocols vpls neighbor 192.0.2.1 pseudowire-status-tlv

   commit check
   ```

## 📌 Notes

* The script ends with `commit check`, allowing you to verify the configuration before committing it.
* This script doesn't apply the configuration to a live device. It's meant for generating CLI-ready commands.

## 📁 File Structure

```
vpls_config_generator.py
README.md
```

---

Feel free to modify the script to support configuration file output or validation.

```
