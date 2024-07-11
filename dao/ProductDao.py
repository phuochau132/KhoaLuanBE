from sqlalchemy import select
from entity.ClassEntity import class_table
from entity.ProductEntity import product_table
from database import database

async def getAllProduct():
    query = select(
        class_table.c.id.label('label_id'),
        class_table.c.name.label('class_name'),
        product_table.c.id.label('id'),
        product_table.c.label_id.label('label_id'),
        product_table.c.image.label('image'),
        product_table.c.name.label('product_name'),
        product_table.c.price.label('price')
    ).select_from(
        class_table.join(product_table, class_table.c.id == product_table.c.label_id)
    )
    results = await database.fetch_all(query=query)
    return [dict(result) for result in results]
