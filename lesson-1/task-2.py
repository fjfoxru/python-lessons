seconds = int(input("секунды"))
total = seconds
hours = int(((seconds / 60) / 60))
total = total - (hours * 60 * 60)
minutes = int(total / 60)
total = int(total - (minutes * 60))
print(f"{hours}:{minutes}:{total}")