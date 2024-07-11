from sqlalchemy import Table, Column, Integer, String,MetaData, ForeignKey

metadata = MetaData()
product_table = Table(
    "product",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("label_id", Integer, ForeignKey("class.id")),
    Column("image", String(255)),
    Column("name", String(255)),
    Column("price", Integer),
)