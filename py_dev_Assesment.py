import csv

inventory = []
restock_items = []

# Read inventory file
try:
    with open("inventory.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                item = row["item_name"]
                quantity = int(row["current_quantity"])
                threshold = int(row["reorder_threshold"])

                inventory.append({
                    "item_name": item,
                    "quantity": quantity,
                    "threshold": threshold
                })

            except (ValueError, KeyError):
                print("Skipping invalid row:", row)

except FileNotFoundError:
    print("inventory.csv file not found.")
    exit()


print("\n========== RESTOCK REPORT ==========\n")

for item in inventory:

    quantity = item["quantity"]
    threshold = item["threshold"]

    if quantity < threshold:

        if quantity <= threshold * 0.25:
            priority = "Critical"
        else:
            priority = "Low"

        reorder_quantity = (threshold * 2) - quantity

        print("Item :", item["item_name"])
        print("Current Quantity :", quantity)
        print("Threshold :", threshold)
        print("Priority :", priority)
        print("Suggested Reorder :", reorder_quantity)
        print("-----------------------------")

        restock_items.append({
            "item_name": item["item_name"],
            "current_quantity": quantity,
            "reorder_threshold": threshold,
            "priority": priority,
            "suggested_reorder": reorder_quantity
        })


# Save report
with open("restock_report.csv", "w", newline="") as file:

    fields = [
        "item_name",
        "current_quantity",
        "reorder_threshold",
        "priority",
        "suggested_reorder"
    ]

    writer = csv.DictWriter(file, fieldnames=fields)

    writer.writeheader()

    for item in restock_items:
        writer.writerow(item)

print("\nCSV report created successfully.")

# Simulated email

print("\n========== EMAIL ALERT ==========\n")
print("Subject: Inventory Restock Alert\n")

if len(restock_items) == 0:
    print("All inventory items are sufficiently stocked.")
else:
    print("The following items require restocking:\n")

    for item in restock_items:
        print(
            f"- {item['item_name']} "
            f"({item['priority']}) "
            f"- Reorder {item['suggested_reorder']} units"
        )

print("\n=================================")