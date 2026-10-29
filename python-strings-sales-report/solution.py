def build_sales_report(raw: str) -> str:
    """
    `raw` is multi-line text. Each meaningful line has the form
        item , quantity , price
    with arbitrary whitespace around each field.

    Processing rules, applied to every line from splitlines():
      1. Strip the line. Skip it if it is empty or starts
         with "#".
      2. Split on "," . Skip the line if it does not have
         exactly 3 fields.
      3. Strip each field. Skip the line if the quantity field
         is not made only of digits. Convert quantity with
         int() and price with float().
      4. Format the item as title case, truncated to at most 12
         characters (slice AFTER applying title case).
      5. line_total = quantity * price.

    Build these output lines, in order, joined by "\\n" with
    no trailing newline:
      - Header: f"{'ITEM':<12}{'QTY':>4}{'PRICE':>10}{'TOTAL':>12}"
      - One row per valid record, in input order:
          item (width 12, left), quantity (width 4, right),
          price (width 10, right, 2 decimals),
          line_total (width 12, right, 2 decimals, with
          thousands separators)
      - A separator line of 38 "-" characters (use *).
      - Grand total line: "TOTAL" left-aligned in width 26,
        then the sum of all line totals right-aligned in width
        12 with 2 decimals and thousands separators.
      - Summary line:
          f"Rows: {rows} | UTF-8 bytes in items: {bytes_total}"
        where `bytes_total` is the sum of the UTF-8 byte lengths
        of the formatted (title-cased, truncated) item labels.

    If there are no valid records, the report still contains the
    header, separator, a grand total of 0.00, and the summary
    with Rows: 0 and 0 bytes.
    """
    lines = raw.splitlines()
    
    valid_records = []
    grand_total = 0.0
    rows = 0
    bytes_total = 0
    
    for line in lines:
        # 1. Strip the line. Skip if empty or starts with "#".
        line = line.strip()
        if not line or line.startswith("#"):
            continue
            
        # 2. Split on ",". Skip if not exactly 3 fields.
        parts = line.split(",")
        if len(parts) != 3:
            continue
            
        # 3. Strip each field. Validate quantity. Convert types.
        item_raw = parts[0].strip()
        qty_raw = parts[1].strip()
        price_raw = parts[2].strip()
        
        if not qty_raw.isdigit():
            continue
            
        qty = int(qty_raw)
        
        # If float conversion fails, skip the line
        try:
            price = float(price_raw)
        except ValueError:
            continue
        
        # 4. Format the item (title case, then truncate to 12 chars).
        item = item_raw.title()[:12]
        
        # 5. Calculate line total.
        line_total = qty * price
        
        # Update running totals
        grand_total += line_total
        rows += 1
        bytes_total += len(item.encode("utf-8"))
        
        # Format the record row
        row_str = f"{item:<12}{qty:>4}{price:>10.2f}{line_total:>12,.2f}"
        valid_records.append(row_str)
        
    # Build the final output lines
    output = []
    
    # Header
    output.append(f"{'ITEM':<12}{'QTY':>4}{'PRICE':>10}{'TOTAL':>12}")
    
    # Valid records
    output.extend(valid_records)
    
    # Separator
    output.append("-" * 38)
    
    # Grand total line
    output.append(f"{'TOTAL':<26}{grand_total:>12,.2f}")
    
    # Summary line
    output.append(f"Rows: {rows} | UTF-8 bytes in items: {bytes_total}")
    
    # Join with newlines (no trailing newline)
    return "\n".join(output)
