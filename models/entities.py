class DeliveryBoy:
    def __init__(self, id, shift, vehicle):
        self.id = id
        self.shift = shift
        self.vehicle = vehicle
        self.available_time = "07:00" if shift == "Morning" else "14:00"
        self.deliveries = []
        self.total_distance = 0
        self.total_time = 0

class DeliveryOrder:
    def __init__(self, id, lat, lon, order_type):
        self.id = id
        self.lat = lat
        self.lon = lon
        self.order_type = order_type
