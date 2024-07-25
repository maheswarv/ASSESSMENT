import tkinter as tk
from tkinter import ttk

# Domain dictionary
domains = {
    'ams': {
        'domain': 'https://ams.hirepro.in',
        'pearson_domain': 'https://vet.hirepro.in',
        'eu_domain': 'https://euapp.hirepro.ai'
    },
    'live': {
        'domain': 'https://ams.hirepro.in',
        'pearson_domain': 'https://vet.hirepro.in',
        'eu_domain': 'https://euapp.hirepro.ai'
    },
    'betaams': {
        'domain': 'https://betaams.hirepro.in',
        'pearson_domain': 'https://betavet.hirepro.in',
        'eu_domain': 'https://betavet.hirepro.in'
    },
    'beta': {
        'domain': 'https://betaams.hirepro.in',
        'pearson_domain': 'https://betavet.hirepro.in',
        'eu_domain': 'https://betavet.hirepro.in'
    },
    'amsin': {
        'domain': 'https://amsin.hirepro.in',
        'pearson_domain': 'https://pearsonstg.hirepro.in',
        'eu_domain': 'https://euamsin.hirepro.in'
    },
    'mumbai': {
        'domain': 'https://amsin.hirepro.in',
        'pearson_domain': 'https://pearsonstg.hirepro.in',
        'eu_domain': 'https://euamsin.hirepro.in'
    }
}

# Function to update text boxes
def update_values():
    env = env_combo.get().strip().lower()
    if env in domains:
        domain_info = domains[env]
        domain = domain_info['domain']
        pearson_domain = domain_info['pearson_domain']
        eu_domain = domain_info['eu_domain']

    else:
        domain = "Invalid"
        pearson_domain = "Invalid"
        eu_domain = "Invalid"

# Initialize main window
root = tk.Tk()
root.title("Environment Domain Checker")

# Environment dropdown
ttk.Label(root, text="Select Environment:").grid(column=0, row=0, padx=10, pady=10)
env_combo = ttk.Combobox(root, values=list(domains.keys()), state="readonly")
env_combo.grid(column=1, row=0, padx=10, pady=10)
ttk.Button(root, text="Submit", command=update_values).grid(column=2, row=0, padx=10, pady=10)

# Run the application
root.mainloop()
print(root.domain)
print(root.pearson_domain)
print(root.eu_domain)