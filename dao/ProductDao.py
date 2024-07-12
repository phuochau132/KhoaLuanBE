from sqlalchemy import select, insert, update
from entity.ClassEntity import class_table
from entity.ProductEntity import product_table
from database import database
from model.ProductCreationModel import ProductCreationModel

async def getAllProduct():
    query = select(
        class_table.c.id.label('label_id'),
        class_table.c.name.label('class_name'),
        product_table.c.id.label('id'),
        product_table.c.label_id.label('label_id'),
        product_table.c.image.label('image'),
        product_table.c.product_name.label('product_name'),
        product_table.c.price.label('price')
    ).select_from(
        class_table.join(product_table, class_table.c.id == product_table.c.label_id)
    )
    results = await database.fetch_all(query=query)
    return [dict(result) for result in results]
async def delProductById(id)-> bool:
    query = product_table.delete().where(product_table.c.id == id)
    number_row = await database.execute(query=query)
    return number_row
async def createProduct(product: ProductCreationModel):
    print("product",product.label_id)
    query = insert(product_table).values(
        label_id=product.label_id,
        image=product.image,
        product_name=product.product_name,
        price=product.price
    )
    await database.execute(query=query)
async def updateProductById(id, new_data):
    query = (
        update(product_table)
        .where(product_table.c.id == id)
        .values(new_data)
    )
    await database.execute(query=query)