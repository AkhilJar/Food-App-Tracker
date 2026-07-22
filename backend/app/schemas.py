#API shape and input 
from datetime import date, datetime
from decimal import Decimal
from enum import Enum
from typing import Optional #used for nullable fields
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

#enum for unit
class Unit(str, Enum):
    g = "g"
    kg = "kg"
    lb = "lb"
    oz = "oz"
    ml = "ml"
    l = "l"
    fl_oz = "fl_oz"
    gal = "gal"
    count = "count"
    dozen = "dozen"
    bag = "bag"
    box = "box"
    can = "can"
    bottle = "bottle"
    pack = "pack"

#enum for location
class Location(str, Enum):
    fridge = "fridge"
    freezer = "freezer"
    cabinet = "cabinet"
    pantry = "pantry"
    counter = "counter"
    other = "other"

#validation for creating an item
class InventoryItemCreate(BaseModel):
    name: str = Field(min_length=1, max_length=200)
    quantity: Decimal = Field(gt=0, max_digits=10, decimal_places=2)
    unit: Unit
    location: Location = Location.fridge
    expiry_date: Optional[date] = None
    custom_name: Optional[str] = Field(default=None, max_length=200)

#build response into JSON from SQL Alchemy object
class IngredientRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    name: str


#Design choice: return soft delete in response
class InventoryItemRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    ingredient: IngredientRead #validate the Ingredient object 
    custom_name: Optional[str]
    quantity: Decimal
    unit: str
    location: str
    expiry_date: Optional[date]
    is_deleted: bool
    created_at: datetime
    updated_at: datetime

    # Validation for updating an item (all fields optional)
class InventoryItemUpdate(BaseModel):
    custom_name: Optional[str] = Field(default=None, max_length=200)
    quantity: Optional[Decimal] = Field(default=None, gt=0, max_digits=10, decimal_places=2)
    unit: Optional[Unit] = None
    location: Optional[Location] = None
    expiry_date: Optional[date] = None
    