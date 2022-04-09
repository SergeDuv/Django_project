
import csv  # https://docs.python.org/3/library/csv.html
from unesco.models import Site, Category, Region, State, Iso
def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header
    Site.objects.all().delete()
    Category.objects.all().delete()
    Region.objects.all().delete()
    State.objects.all().delete()
    Iso.objects.all().delete()

    for row in reader:
        print(row)
        try:
            y = int(row[3])
        except:
            y = None
        try:
            a = float(row[6])
        except:
            a = 0.0

        # for category
        c, created = Category.objects.get_or_create(name=row[7])

        # for region
        r, created = Region.objects.get_or_create(name=row[9])

        # for state/country
        st, created = State.objects.get_or_create(name=row[8])

        #    j = None
        i, created = Iso.objects.get_or_create(name=row[10])

        s, created = Site.objects.get_or_create(name=row[0], description=row[1], justification=row[2], year=y,longitude=row[4],latitude=row[5],area_hectares=a,category=c,state=st,region=r,iso=i)
