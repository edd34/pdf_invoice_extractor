import os
import shutil
from csv import DictWriter
from pprint import pprint
import os

import click
import pandas as pd
import pdfplumber
from tqdm import tqdm

from helpers import clean_data, extract_info
from pdf_spliter import split_pdf
import gc


@click.command()
@click.option("--input_file_name", help="Nom du fichier d'entrée", type=click.File())
@click.option("--output_file_name", help="Nom du dossier de sortie. Le nom du fichier de sortie est le même que celui du fichier d'entrée mais avec l'extension CSV")
def main(input_file_name, output_file_name):
    if os.path.isdir("./.tmp"):
        shutil.rmtree("./.tmp")
    if not os.path.isdir("./.tmp"):
        os.mkdir("./.tmp")

    headers_written = False
    fichier = str(input_file_name.name.split(".pdf")[0])
    split_pdf(input_file_name.name, "./.tmp")

    for file in tqdm(os.listdir("./.tmp")):
        numero_page = file.split(".")[0]
        if file.endswith(".pdf"):
            with pdfplumber.open("./.tmp/" + file) as pdf:
                # first_page_of_pdf = pdf.pages[0]
                res = [extract_info(numero_page, pdf)]
                # df = clean_data(res)
                df = pd.DataFrame(res)
                if headers_written:
                    df.to_csv(fichier + ".csv", index=False, mode="a", header=False)
                else:
                    df.to_csv(fichier + ".csv", index=False, mode="w", header=True)
                    headers_written = True

    if os.path.isdir("./.tmp"):
        shutil.rmtree("./.tmp")
    return 0


if __name__ == "__main__":
    main()
