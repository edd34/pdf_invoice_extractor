import os
from csv import DictWriter
from pprint import pprint

import click
import pandas as pd
import pdfplumber
from tqdm import tqdm

from helpers import clean_data, extract_info
import gc


@click.command()
@click.option("--input_file_name", help="Nom du fichier d'entrée", type=click.File())
@click.option(
    "--output_file_name",
    help="Nom du dossier de sortie. Le nom du fichier de sortie est le même que celui du fichier d'entrée mais avec l'extension CSV",
)
def main(input_file_name, output_file_name):
   headers_written = False
   fichier = str(input_file_name.name.split(".pdf")[0])

   with pdfplumber.open(fichier + ".pdf") as pdf:
        # first_page_of_pdf = pdf.pages[0]
      nb_page = len(pdf.pages)

   for i in tqdm(range(nb_page)):
      with pdfplumber.open(fichier + ".pdf") as pdf:
        # first_page_of_pdf = pdf.pages[0]
         res = [extract_info(i, pdf)]
         df = pd.DataFrame(res)
         if headers_written:
            df.to_csv(fichier +".csv", index=False, mode="a")
         else:
            df.to_csv(fichier + ".csv", index=False, mode="w", header=True)
            headers_written = True

   return 0


if __name__ == "__main__":
    main()
