import json
from models.entities import DeliveryBoy, DeliveryOrder
from logic.assignment import assign_deliveries

OFFICE_COORDS = (16.86114504153856, 74.57615831791716)

# Load Data
with open("data/DeliveryBoyData.json") as f:
    boys_raw = json.load(f)

with open("data/DeliveryData.json") as f:
    orders_raw = json.load(f)

# Convert to objects
boys = [DeliveryBoy(d["DELIVERY_BOY_ID"], d["SHIFT"], d["VEHICLE_TYPE"]) for d in boys_raw]
orders = [DeliveryOrder(o["ORDER_ID"], o["LATITUDE"], o["LONGITUDE"], o["DELIVERY_TYPE"]) for o in orders_raw]

# Assign Deliveries
schedule = assign_deliveries(orders, boys, OFFICE_COORDS)

# Output Results
import csv

with open("output/delivery_schedule.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=schedule[0].keys())
    writer.writeheader()
    writer.writerows(schedule)

with open("output/summary_report.txt", "w") as f:
    for boy in boys:
        f.write(f"{boy.id} | {boy.shift} | Orders: {len(boy.deliveries)} | Distance: {round(boy.total_distance, 2)} km | Time: {round(boy.total_time, 2)} mins\n")

print("✅ Schedule & summary generated in /output")
