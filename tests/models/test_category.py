from sqlalchemy import Integer, String, Boolean

"""
## Table and Column Validation
"""

"""
- [ ] Confirm the presence of all required tables within the database schema.
"""
def test_model_structure_table_exists(db_inspector):
    assert db_inspector.has_table("categories") is True
"""
- [ ] Validate the existence of expected columns in each table, ensuring correct data types.
"""
def test_model_structure_column_data_types(db_inspector):
    table = "categories"
    columns = {columns["name"]: columns for columns in db_inspector.get_columns(table)}
    assert isinstance(columns["id"]["type"], Integer)
    assert isinstance(columns["name"]["type"], String)
    assert isinstance(columns["slug"]["type"], String)
    assert isinstance(columns["is_active"]["type"], Boolean)
    assert isinstance(columns["level"]["type"], Integer)
    assert isinstance(columns["parent_id"]["type"], Integer)
    
"""
- [ ] Verify nullable or not nullable fields
"""
def test_model_structure_nullable_constraints(db_inspector):
    table = "categories"
    columns = {columns["name"]: columns for columns in db_inspector.get_columns(table)}
    assert columns["id"]["nullable"] is False
    assert columns["name"]["nullable"] is False
    assert columns["slug"]["nullable"] is False
    assert columns["is_active"]["nullable"] is False
    assert columns["level"]["nullable"] is False
    assert columns["parent_id"]["nullable"] is True
"""
- [ ] Test columns with specific constraints to ensure they are accurately defined.
"""
def test_model_structure_column_constraints(db_inspector):
    table = "categories"
    constraints = db_inspector.get_check_constraints(table)
    # assert any(constraint["name"] == "name_length_check" for constraint in constraints)
    # assert any(constraint["name"] == "slug_length_check" for constraint in constraints)
    constr = (constraint["name"] for constraint in constraints)
    for name in constr:
        print(name)

    
"""
- [ ] Verify the correctness of default values for relevant columns.
"""

"""
- [ ] Ensure that column lengths align with defined requirements.
"""

"""
- [ ]  Validate the enforcement of unique constraints for columns requiring unique values.
"""
