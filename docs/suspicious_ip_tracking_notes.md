# Suspicious IP Tracking — Understanding Notes

## Part 1 — Database Reading

```python
cursor.execute("SELECT message FROM incidents WHERE level='ALERT'")
```

## Part 2 — Regex IP Extraction

```python
re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', message)
```

## Part 3 — Counting Logic

```python
if ip in ip_count:
    ip_count[ip] += 1
else:
    ip_count[ip] = 1
```

## Part 4 — Threshold Logic

```python
if count >= 3:
```
