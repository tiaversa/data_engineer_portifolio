#!/bin/bash
sleep 15
echo "Adding the table structure from the YAMLs"
python3 /warehouse_set_up/tables_structure/table_structure_script.py
echo "Addign data from the SQL tests"
python3 warehouse_set_up/SQLTasks/add_test_data.py
echo "Finalized set up."