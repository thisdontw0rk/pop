from ansible.parsing.dataloader import DataLoader
from ansible.inventory.manager import InventoryManager

def load_inventory_and_print_hosts():
    
    loader = DataLoader()

    # Define the path to the inventory file
    inventory_path = './hosts.yml'

    # Load the inventory
    inventory = InventoryManager(loader=loader, sources=inventory_path)

    # Get all hosts in the inventory
    all_hosts = inventory.get_hosts()

    # Print names, IP addresses, and group names of all hosts
    for host in all_hosts:
        print("Name:", host.name)
        print("IP Address(es):", ', '.join(host.vars['ansible_host']))
        print("Group(s):", ', '.join(host.groups))
        print()

if __name__ == "__main__":
    load_inventory_and_print_hosts()
