import os
from brand import get_brand_list
from job import get_jobs
from save import save_file

os.system("clear")

brand_list = get_brand_list()

jobs = get_jobs(brand_list)

#print_jobs(jobs)

save_file(jobs)
