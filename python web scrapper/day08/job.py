from alba import get_alba_list


def print_jobs(jobs):
    for job in jobs:
        print()
        print(f"{job['file_title']}")
        for alba in job['brand_alba_list']:
            print(f"{alba['place']} {alba['title']} {alba['time']} {alba['pay']} {alba['date']}")
        print()


def get_job(brand):
    alba_list = get_alba_list(brand)
    job = {'file_title': brand['company'], 'brand_alba_list': alba_list}
    return job


def get_jobs(brand_list):
    jobs = []
    for i, brand in enumerate(brand_list):
        job = get_job(brand)
        jobs.append(job)
        print(f"job appended: {brand['company']} ({i+1}/{len(brand_list)})")
    return jobs