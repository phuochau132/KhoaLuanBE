from sqlalchemy import Table, Column, Integer, String,MetaData
metadata = MetaData()
class_table = Table(
    "class",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(255)),
)