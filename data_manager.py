import numpy as np

def generate_sales_dataset(seed: int = 42) -> np.ndarray:
    rng = np.random.default_rng(seed)
    units_sold = rng.integers(0, 101, size=(4, 30, 5))

    print("Sales dataset generated successfully.")
    print(f"Shape: {units_sold.shape}")
    print(f"Dimensions: {units_sold.ndim}")
    print(f"Total readings: {units_sold.size}")
    print(f"Data type: {units_sold.dtype}")

    return units_sold