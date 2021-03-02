import csv

def save_file(jobs):
    for i, job in enumerate(jobs):
        with open(f"./result/{job['file_title']}.csv", 'w') as file:
            writer = csv.writer(file)
            writer.writerow(['place', 'title', 'time', 'pay', 'date'])
            for alba in job['brand_alba_list']:
                writer.writerow(list(alba.values()))
        print(f"job saved: {job['file_title']} ({i+1}/{len(jobs)})")
    return