from fastapi import APIRouter, HTTPException
from models import Car
from config import supabase

router = APIRouter()

# Add a car
@router.post("/")
def create_car(car : Car):
    response  = supabase.table("cars").insert(car.model_dump()).execute()
    return response.data

# Get all the cars
@router.get("/")
def get_cars():
    response = supabase.table("cars").select("*").execute()
    return response.data

# Get car by id
@router.get("/{car_id}")
def get_car(car_id : int):
    response = supabase.table("cars").select("*").eq("id", car_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Car not found!")
    return response.data[0]

# Update car details by id
@router.put("/{car_id}")
def update_car(car_id: int, car: Car):
    response = supabase.table("cars").update(car.model_dump()).eq("id", car_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Car not found!")
    return response.data[0]

# Delete car by id
@router.delete("/{car_id")
def delete_car(car_id : int):
    response = supabase.table("cars").delete().eq("id", car_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Car not found!")
    return {"message" : "Car deleted!"}