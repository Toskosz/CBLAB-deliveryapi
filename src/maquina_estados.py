possiveis_estados = {
    "RECEIVED": ["CONFIRMED", "CANCELED"],
    "CONFIRMED": ["DISPATCHED", "CANCELED"],
    "DISPATCHED": ["DELIVERED", "CANCELED"],
    "DELIVERED": [],
    "CANCELED": []
}