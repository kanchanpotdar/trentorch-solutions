def cache_hit_rate(keys: list[int]) -> tuple[int, int, float]:
    seen = set()
    hits = 0
    misses = 0
    
    for key in keys:
        if key in seen:
            hits += 1
        else:
            seen.add(key)
            misses += 1
            
    rate = hits / len(keys) if keys else 0.0
    
    return (hits, misses, rate)
