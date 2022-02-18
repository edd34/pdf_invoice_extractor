import pandas as pd
import gc


def get_feature(pdf_page, feature_name, x, y, width, height):
    x = x
    y = y
    width = width
    height = height

    left = x
    right = x + width
    top = y
    bottom = y + height

    image_bbox = (float(left), float(top), float(right), float(bottom))
    data = pdf_page.crop(image_bbox)
    return {
        feature_name: data.extract_text(
            x_density=0,
            y_density=0,
        )
    }


def extract_info(numero_page, pdf):
    num_facture = get_feature(
        pdf.pages[numero_page], "numero_facture", 351.4, 30.2, 211.7, 20.2
    )
    date = get_feature(pdf.pages[numero_page], "date", 354.2, 13.7, 211.7, 20.2)
    adr_branchement = get_feature(
        pdf.pages[numero_page], "adresse_branchement", 291.6, 70.6, 280.8, 51.8
    )
    ref_client = get_feature(
        pdf.pages[numero_page], "reference_client", 365.8, 126.7, 209.5, 7.9
    )
    adr_client = get_feature(
        pdf.pages[numero_page], "nom_adresse_client", 293.0, 169.9, 286.6, 35.3
    )
    hist_cons = get_feature(
        pdf.pages[numero_page], "historique_consommation", 85.0, 134.6, 145.4, 31.7
    )
    email = get_feature(pdf.pages[numero_page], "email", 113.8, 90.0, 145.4, 3.6)
    num_bimestre = get_feature(
        pdf.pages[numero_page], "numero_bimestre", 61.2, 186.5, 110.9, 15.1
    )
    num_compteur = get_feature(
        pdf.pages[numero_page], "numero_compteur", 18.1, 232.6, 110.9, 15.1
    )
    periode_consommation = get_feature(
        pdf.pages[numero_page], "periode_consommation", 119.5, 207.4, 109.4, 10.1
    )
    num_sem_releve = get_feature(
        pdf.pages[numero_page], "semaine_du_releve", 172.8, 233.3, 52.6, 13.0
    )
    montant_total_du = get_feature(
        pdf.pages[numero_page], "montant_total_du", 514.8, 625.7, 54.0, 18.7
    )
    conso_tranches = get_feature(
        pdf.pages[numero_page], "consommation_tranche", 16.6, 329.0, 283.0, 36.7
    )
    sous_total = get_feature(
        pdf.pages[numero_page], "sous_total", 251.3, 472.3, 59.0, 15.1
    )

    return {
        "numero_page": numero_page + 1,
        **num_facture,
        **date,
        **adr_branchement,
        **ref_client,
        **adr_client,
        **hist_cons,
        **email,
        **num_bimestre,
        **num_compteur,
        **periode_consommation,
        **num_sem_releve,
        **montant_total_du,
        **conso_tranches,
        **sous_total,
    }


def clean_data(res):
    df = pd.DataFrame(res)
    df["CR"] = df["montant_total_du"].str.contains("CR")
    df["montant_total_du"] = df["montant_total_du"].str.replace("CR", "")

    # clean data historique consommation
    s = df["historique_consommation"].str.split("\n").apply(pd.Series, 1)
    s.rename(
        columns={
            0: "historique_consommation_1",
            1: "historique_consommation_2",
            2: "historique_consommation_3",
        },
        inplace=True,
    )
    df = df.join(s)

    df[
        ["historique_consommation_1_date", "historique_consommation_1_valeur"]
    ] = df.historique_consommation_1.str.split(expand=True)
    df[
        ["historique_consommation_2_date", "historique_consommation_2_valeur"]
    ] = df.historique_consommation_2.str.split(expand=True)
    df[
        ["historique_consommation_3_date", "historique_consommation_3_valeur"]
    ] = df.historique_consommation_3.str.split(expand=True)

    del df["historique_consommation_1"]
    del df["historique_consommation_2"]
    del df["historique_consommation_3"]

    # clean consommation tranche
    s = df["consommation_tranche"].str.split("\n").apply(pd.Series, 1)
    s.rename(
        columns={
            0: "consommation_tranche_1",
            1: "consommation_tranche_2",
            2: "consommation_tranche_3",
        },
        inplace=True,
    )

    df = df.join(s)
    del df["consommation_tranche"]
    df = df.fillna(0)
    return df
