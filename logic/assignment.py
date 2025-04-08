from utils.distance import calculate_distance
from utils.time_utils import str_to_time, time_to_str, add_minutes

def assign_deliveries(orders, boys, office_coords):
    schedule = []

    for order in orders:
        eligible_boys = [boy for boy in boys if is_eligible(order, boy)]
        if not eligible_boys:
            continue

        best_boy = min(eligible_boys, key=lambda b: calculate_distance(office_coords, (order.lat, order.lon)))
        dist = calculate_distance(office_coords, (order.lat, order.lon))
        speed = 35 if best_boy.vehicle == "Bike" else 15
        travel_time = (dist / speed) * 60

        start_time = str_to_time(best_boy.available_time)
        end_time = add_minutes(start_time, travel_time)
        delivery_end = add_minutes(end_time, 15)

        schedule.append({
            "Order ID": order.id,
            "Order Type": order.order_type,
            "Delivery Boy ID": best_boy.id,
            "Shift": best_boy.shift,
            "Start Time": time_to_str(start_time),
            "End Time": time_to_str(end_time),
            "Distance (km)": round(dist, 2),
            "Travel Time (min)": int(travel_time),
            "Delivery End Time": time_to_str(delivery_end),
        })

        best_boy.available_time = delivery_end.strftime("%H:%M")
        best_boy.deliveries.append(order.id)
        best_boy.total_distance += dist
        best_boy.total_time += travel_time + 15

    return schedule
