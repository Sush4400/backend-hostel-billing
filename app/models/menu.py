# id, day_of_week, meal_type, name, price, service_start, service_end, is_active



'''
Use NUMERIC(10, 2) for prices and amounts; map these to Python Decimal.
Use timezone-aware timestamps and store them in UTC. Configure the UI and reports for Asia/Kolkata.
Save a snapshot of the item name and price on every order line. Changing tomorrow's menu must not change yesterday's bill.
Give order_number a database-level unique constraint.
Allow multiple payment records if partial payments are required later. For the initial implementation, require one full payment before collection.
Keep collection records and payment records separate.
Never hard-delete completed orders or payments.
Use an audit trail for cancellation, refund, manual payment entry, and reprinting.
'''