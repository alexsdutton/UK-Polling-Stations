import os
import glob
from django.db import connection
from django.core.management.base import BaseCommand


"""
To import ONSUD, grab the latest release:
http://ons.maps.arcgis.com/home/search.html?q=ONS%20Address%20Directory&t=content
and run
python manage.py import_onsud /path/to/data
"""
class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'path',
            help='Path to the directory containing the ONSUD CSVs'
        )
        parser.add_argument(
            '-t',
            '--table',
            help='If you have extended the AbstractOnsud model, use this flag to specify the table name for your child table',
            default='uk_geo_utils_onsud',
            required=False,
        )

    def handle(self, *args, **kwargs):
        self.table_name = kwargs['table']

        cursor = connection.cursor()
        print("clearing existing data..")
        cursor.execute("TRUNCATE TABLE %s;" % (self.table_name))
        glob_str = os.path.join(kwargs['path'], "*.csv")
        print("importing from files..")
        for f in glob.glob(glob_str):
            print(f)
            cursor.execute("""
                COPY {0} (
                uprn, ctry_flag, cty, lad, ward, hlthau, ctry,
                rgn, pcon, eer, ttwa, nuts, park, oa11, lsoa11, msoa11, parish,
                wz11, ccg, bua11, buasd11, ruc11, oac11, lep1, lep2, pfa, imd)
                FROM '{1}' (FORMAT CSV, DELIMITER ',', QUOTE '"', HEADER);
            """.format(self.table_name, f))
        print("...done")
