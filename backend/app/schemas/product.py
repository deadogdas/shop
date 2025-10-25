from pydantic import BaseModel,Field
from datetime import datetime
from typing import Optional
from.category import CategoryResponse


class ProductBase(BaseModel):
    name: str = Field(...,min_length=5,max_length=200,
                      description="Category name")
    description: Optional[str] = Field(None,description="Product description")
    price: int = Field(...,gt=0,description="Product price")
    category_id: int = Field(...,description="Category ID")
    image_url: Optional[str] = Field(None, description="Product image URL")

class ProductCreate(ProductBase):
    pass

class ProductResponse(BaseModel):
    id: int = Field(...,description="Unique product ID")
    name: str
    description: Optional[str]
    price: float
    category_id: int
    image_url: Optional[str]
    created_at: datetime
    category: CategoryResponse = Field(..., description="Product category details")

    class Config:
        from_attributes = True

class ProductListResponse(BaseModel):
    products: list[ProductResponse]
    total: int = Field(...,description="Total number of products")