vpls = input("Enter the name of VPLS: ")
aggregated_ethernet = input("Enter the aggregated ethernet name (e.g., ae6): ")
vlan = input("Enter the VLAN: ")

neighbour_cmd = ""

add_neighbour = input("Do you want to configure a neighbor? (yes/no): ").strip().lower()

if add_neighbour == "yes":
    while True:
        neighbour_ip = input("Enter neighbor IP: ")
        neighbour_cmd += f"set routing-instances {vpls} protocols vpls neighbor {neighbour_ip} pseudowire-status-tlv\n"
        more = input("Add another neighbour? (yes/no): ").strip().lower()
        if more != "yes":
            break

print(f"""
### The Command to configure VPLS in JUNIPER ROUTER ###

configure private



set interfaces ae{aggregated_ethernet} unit {vlan} description {vpls}
set interfaces ae{aggregated_ethernet} unit {vlan} encapsulation vlan-vpls
set interfaces ae{aggregated_ethernet} unit {vlan} vlan-id {vlan}
set interfaces ae{aggregated_ethernet} unit {vlan} family vpls
set routing-instances {vpls} interface ae{aggregated_ethernet}.{vlan}
set routing-instances {vpls} protocols vpls vpls-id {vlan}
set routing-instances {vpls} description {vpls}
set routing-instances {vpls} instance-type vpls
set routing-instances {vpls} protocols vpls no-tunnel-services
set routing-instances {vpls} protocols vpls vpls-id {vlan}

{neighbour_cmd}

commit check 

""")

input("Press Enter to exit...")