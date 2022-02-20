import pandas as pd
import gc


def get_feature(pdf_page, feature_name, x, y, width, height, crop=True):
    x = x
    y = y
    width = width
    height = height

    left = x
    right = x + width
    top = y
    bottom = y + height

    image_bbox = (float(left), float(top), float(right), float(bottom))
    if crop:
        data = pdf_page.crop(image_bbox)
    else:
        data = pdf_page.within_bbox(image_bbox)
    return {feature_name: data.extract_text(x_density=0, y_density=0)}


def extract_info(numero_page, pdf):
    ####################################################################################
    ############################ identification ########################################
    ####################################################################################
    num_facture = get_feature(pdf.pages[0], "numero_facture", 351.4, 30.2, 211.7, 20.2)
    date = get_feature(pdf.pages[0], "date", 354.2, 13.7, 211.7, 20.2)
    adr_branchement = get_feature(pdf.pages[0], "adresse_branchement", 291.6, 70.6, 280.8, 51.8)
    ref_client = get_feature(pdf.pages[0], "reference_client", 365.8, 126.7, 209.5, 7.9)
    adr_client = get_feature(pdf.pages[0], "nom_adresse_client", 293.0, 169.9, 286.6, 35.3)
    email = get_feature(pdf.pages[0], "email", 113.8, 90.0, 145.4, 3.6)
    num_bimestre = get_feature(pdf.pages[0], "numero_bimestre", 61.2, 186.5, 110.9, 15.1)
    num_compteur = get_feature(pdf.pages[0], "numero_compteur", 18.1, 232.6, 110.9, 15.1)
    periode_consommation = get_feature(pdf.pages[0], "periode_consommation", 119.5, 207.4, 109.4, 10.1)
    num_sem_releve = get_feature(pdf.pages[0], "semaine_du_releve", 172.8, 233.3, 52.6, 13.0)

    ancien_index_1 = get_feature(pdf.pages[0], "ancien_index_1", 275.8, 234.7, 44.6, 10.1, False)
    ancien_index_2 = get_feature(pdf.pages[0], "ancien_index_2", 275.8, 244.1, 44.6, 10.1, False)
    nouvel_index_1 = get_feature(pdf.pages[0], "nouvel_index_1", 388.8, 234.7, 46.8, 10.1, False)
    nouvel_index_2 = get_feature(pdf.pages[0], "nouvel_index_2", 389.5, 243.5, 44.6, 10.1, False)
    sem_releve_index_1 = get_feature(pdf.pages[0], "sem_releve_index_1", 168.5, 233.5, 61.9, 9.4, False)
    sem_releve_index_2 = get_feature(pdf.pages[0], "sem_releve_index_2", 169.9, 244.1, 61.2, 9.4, False)
    conso_index_1 = get_feature(pdf.pages[0], "conso_index_1", 500.4, 235.4, 49.0, 9.4, False)
    conso_index_2 = get_feature(pdf.pages[0], "conso_index_2", 499.7, 244.1, 49.0, 9.4, False)

    ####################################################################################
    #################### historique consommation #######################################
    ####################################################################################
    hist_cons_1_date = get_feature(pdf.pages[0], "historique_consommation_1_date", 85.7, 136.1, 93.6, 10.1, False)
    hist_cons_1_valeur = get_feature(pdf.pages[0], "historique_consommation_1_valeur", 198.7, 136.1, 21.6, 9.4, False)
    hist_cons_2_date = get_feature(pdf.pages[0], "historique_consommation_2_date", 87.1, 145.4, 59.0, 10.1, False)
    hist_cons_2_valeur = get_feature(pdf.pages[0], "historique_consommation_2_valeur", 195.1, 144.7, 23.8, 10.1, False)
    hist_cons_3_date = get_feature(pdf.pages[0], "historique_consommation_3_date", 93.6, 154.1, 36.7, 9.4, False)
    hist_cons_3_valeur = get_feature(pdf.pages[0], "historique_consommation_3_valeur", 198.0, 154.1, 18.0, 10.1, False)

    # prix litre
    prix_litre_eau_potable = get_feature(pdf.pages[0], "prix_litre_eau_potable", 222.5, 259.9, 38.9, 12.2, False)
    prix_litre_global = get_feature(pdf.pages[0], "prix_litre_global", 221.0, 269.3, 38.9, 12.2, False)

    # conso par tranche et conso total en m3
    conso_tranche_1 = get_feature(pdf.pages[0], "conso_tranche_1", 262.8, 331.9, 38.9, 12.2, False)
    conso_tranche_2 = get_feature(pdf.pages[0], "conso_tranche_2", 262.1, 342.0, 38.9, 12.2, False)
    conso_tranche_3 = get_feature(pdf.pages[0], "conso_tranche_3", 256.3, 351.4, 47.5, 12.2, False)
    sous_part = get_feature(pdf.pages[0], "sous_part", 253.4, 367.2, 48.2, 12.2, False)
    ####################################################################################
    ##########################    Distribution de l'eau     ############################
    ####################################################################################

    ##### Distribution de l'eau part distributeur (SMAE) ######
    # abonnement
    abonnement_ht = get_feature(pdf.pages[0], "abonnement_ht", 406.8, 313.9, 38.9, 12.2, False)
    abonnement_ttc = get_feature(pdf.pages[0], "abonnement_ttc", 522.7, 316.1, 55.4, 10.1, False)
    # prix unitaire part SMAE
    pu_tranche_1_SMAE = get_feature(pdf.pages[0], "pu_tranche_1_SMAE", 324.7, 331.9, 48.2, 12.2, False)
    pu_tranche_2_SMAE = get_feature(pdf.pages[0], "pu_tranche_2_SMAE", 324.0, 342.7, 48.2, 10.8, False)
    pu_tranche_3_SMAE = get_feature(pdf.pages[0], "pu_tranche_3_SMAE", 324.0, 352.1, 48.2, 9.4, False)
    # montant total ht SMAE
    mt_ht_tranche_1_SMAE = get_feature(pdf.pages[0], "mt_ht_tranche_1_SMAE", 391.0, 333.4, 55.4, 10.8, False)
    mt_ht_tranche_2_SMAE = get_feature(pdf.pages[0], "mt_ht_tranche_2_SMAE", 390.2, 342.7, 55.4, 10.8, False)
    mt_ht_tranche_3_SMAE = get_feature(pdf.pages[0], "mt_ht_tranche_3_SMAE", 391.7, 352.1, 55.4, 10.1, False)
    mt_ht_sous_total_SMAE = get_feature(pdf.pages[0], "mt_ht_sous_total_SMAE", 390.2, 370.1, 55.4, 10.1, False)
    # montant total ttc SMAE
    mt_ttc_tranche_1_SMAE = get_feature(pdf.pages[0], "mt_ttc_tranche_1_SMAE", 524.2, 332.6, 55.4, 10.1, False)
    mt_ttc_tranche_2_SMAE = get_feature(pdf.pages[0], "mt_ttc_tranche_2_SMAE", 522.7, 342.7, 55.4, 10.1, False)
    mt_ttc_tranche_3_SMAE = get_feature(pdf.pages[0], "mt_ttc_tranche_3_SMAE", 522.7, 352.8, 55.4, 10.1, False)
    mt_ttc_sous_total_SMAE = get_feature(pdf.pages[0], "mt_ttc_sous_total_SMAE", 522.1, 369.4, 55.4, 10.1, False)

    ##### Distribution de l'eau part intercommunale (SMEAM) ########################
    # prix unitaire part SMEAM
    pu_tranche_1_SMEAM = get_feature(pdf.pages[0], "pu_tranche_1_SMEAM", 324.0, 405.4, 47.5, 10.1, False)
    pu_tranche_2_SMEAM = get_feature(pdf.pages[0], "pu_tranche_2_SMEAM", 324.0, 414.7, 47.5, 10.1, False)
    pu_tranche_3_SMEAM = get_feature(pdf.pages[0], "pu_tranche_3_SMEAM", 324.0, 423.4, 47.5, 10.1, False)
    # montant total ht SMEAM
    mt_ht_tranche_1_SMEAM = get_feature(pdf.pages[0], "mt_ht_tranche_1_SMEAM", 397.4, 406.1, 47.5, 10.1, False)
    mt_ht_tranche_2_SMEAM = get_feature(pdf.pages[0], "mt_ht_tranche_2_SMEAM", 397.4, 414.7, 47.5, 10.1, False)
    mt_ht_tranche_3_SMEAM = get_feature(pdf.pages[0], "mt_ht_tranche_3_SMEAM", 395.3, 424.1, 47.5, 10.1, False)
    mt_ht_sous_total_SMEAM = get_feature(pdf.pages[0], "mt_ht_sous_total_SMEAM", 395.3, 442.1, 47.5, 10.1, False)
    part_fixe_ht_SMEAM = get_feature(pdf.pages[0], "part_fixe_ht_SMEAM", 395.3, 432.7, 47.5, 10.1, False)

    # montant total ttc SMEAM
    mt_ttc_tranche_1_SMEAM = get_feature(pdf.pages[0], "mt_ttc_tranche_1_SMEAM", 530.6, 405.4, 47.5, 10.1, False)
    mt_ttc_tranche_2_SMEAM = get_feature(pdf.pages[0], "mt_ttc_tranche_2_SMEAM", 530.6, 414.7, 47.5, 10.1, False)
    mt_ttc_tranche_3_SMEAM = get_feature(pdf.pages[0], "mt_ttc_tranche_3_SMEAM", 530.6, 424.8, 47.5, 9.4, False)
    mt_ttc_sous_total_SMEAM = get_feature(pdf.pages[0], "mt_ttc_sous_total_SMEAM", 529.2, 442.8, 48.2, 8.6, False)
    part_fixe_ttc_SMEAM = get_feature(pdf.pages[0], "part_fixe_ttc_SMEAM", 530.6, 434.2, 48.2, 8.6, False)

    ##### octroi de mer regional ######
    octroi_de_mer_taux = get_feature(pdf.pages[0], "octroi_de_mer_taux", 464.4, 459.4, 51.1, 10.8, False)
    octroi_de_mer_ttc = get_feature(pdf.pages[0], "octroi_de_mer_ttc", 517.0, 459.4, 63.4, 10.8, False)

    ##### sous total distribution eau potable ######
    sous_total_distrib_eau_potable_ht = get_feature(pdf.pages[0], "sous_total_distrib_eau_potable_ht", 380.2, 475.9, 62.6, 10.8)
    sous_total_distrib_eau_potable_ttc = get_feature(pdf.pages[0], "sous_total_distrib_eau_potable_ttc", 516.2, 476.6, 62.6, 11.5, False)

    ####################################################################################
    ###################    Collecte et traitement eaux usées     #######################
    ####################################################################################
    abonnement_assai_SMEAM_ht = get_feature(pdf.pages[0], "abonnement_assai_SMEAM_ht", 408.2, 505.4, 38.9, 11.5, False)
    abonnement_assai_SMAA_ht = get_feature(pdf.pages[0], "abonnement_assai_SMAA_ht", 408.2, 541.4, 36.7, 10.1, False)
    abonnement_assai_SMEAM_ttc = get_feature(pdf.pages[0], "abonnement_assai_SMEAM_ttc", 454.0, 506.2, 34.6, 9.4, False)
    abonnement_assai_SMAA_ttc = get_feature(pdf.pages[0], "abonnement_assai_SMAA_ttc", 547.2, 541.4, 31.7, 10.1, False)
    conso_assai_smeam_pu = get_feature(pdf.pages[0], "conso_assai_smeam_pu", 338.4, 522.0, 33.1, 12.2, False)
    conso_assai_smaa_pu = get_feature(pdf.pages[0], "conso_assai_smaa_pu", 338.4, 557.3, 33.8, 12.2, False)
    conso_assai_smeam_total_ht = get_feature(pdf.pages[0], "conso_assai_smeam_total_ht", 405.4, 522.0, 39.6, 12.2, False)
    conso_assai_smaa_total_ht = get_feature(pdf.pages[0], "conso_assai_smaa_total_ht", 403.9, 552.0, 39.6, 12.2, False)
    conso_assai_smeam_total_ttc = get_feature(pdf.pages[0], "conso_assai_smeam_total_ttc", 539.3, 522.7, 39.6, 12.2, False)
    conso_assai_smaa_total_ttc = get_feature(pdf.pages[0], "conso_assai_smaa_total_ttc", 538.6, 558.0, 39.6, 12.2, False)

    sous_total_assai_ht = get_feature(pdf.pages[0], "sous_total_assai_ht", 404.6, 575.3, 39.6, 12.2)
    sous_total_assai_ttc = get_feature(pdf.pages[0], "sous_total_assai_ht", 543.6, 575.3, 34.6, 12.2)

    ####################################################################################
    #############################    Total général     #################################
    ####################################################################################
    total_general_ht = get_feature(pdf.pages[0], "total_general_ht", 377.3, 594.0, 68.4, 11.5, False)
    total_general_ttc = get_feature(pdf.pages[0], "total_general_ttc", 517.7, 594.0, 59.8, 10.8, False)

    return {
        "numero_page": int(numero_page) + 1,
        **num_facture,
        **date,
        **adr_branchement,
        **ref_client,
        **adr_client,
        **email,
        **num_bimestre,
        **num_compteur,
        **periode_consommation,
        **num_sem_releve,
        **ancien_index_1,
        **ancien_index_2,
        **nouvel_index_1,
        **nouvel_index_2,
        **sem_releve_index_1,
        **sem_releve_index_2,
        **conso_index_1,
        **conso_index_2,
        **hist_cons_1_date,
        **hist_cons_1_valeur,
        **hist_cons_2_date,
        **hist_cons_2_valeur,
        **hist_cons_3_date,
        **hist_cons_3_valeur,
        **prix_litre_eau_potable,
        **prix_litre_global,
        **conso_tranche_1,
        **conso_tranche_2,
        **conso_tranche_3,
        **sous_part,
        **abonnement_ht,
        **abonnement_ttc,
        **pu_tranche_1_SMAE,
        **pu_tranche_2_SMAE,
        **pu_tranche_3_SMAE,
        **mt_ht_tranche_1_SMAE,
        **mt_ht_tranche_2_SMAE,
        **mt_ht_tranche_3_SMAE,
        **mt_ht_sous_total_SMAE,
        **mt_ttc_tranche_1_SMAE,
        **mt_ttc_tranche_2_SMAE,
        **mt_ttc_tranche_3_SMAE,
        **mt_ttc_sous_total_SMAE,
        **pu_tranche_1_SMEAM,
        **pu_tranche_2_SMEAM,
        **pu_tranche_3_SMEAM,
        **mt_ht_tranche_1_SMEAM,
        **mt_ht_tranche_2_SMEAM,
        **mt_ht_tranche_3_SMEAM,
        **mt_ht_sous_total_SMEAM,
        **part_fixe_ht_SMEAM,
        **mt_ttc_tranche_1_SMEAM,
        **mt_ttc_tranche_2_SMEAM,
        **mt_ttc_tranche_3_SMEAM,
        **mt_ttc_sous_total_SMEAM,
        **part_fixe_ttc_SMEAM,
        **octroi_de_mer_taux,
        **octroi_de_mer_ttc,
        **sous_total_distrib_eau_potable_ht,
        **sous_total_distrib_eau_potable_ttc,
        **abonnement_assai_SMEAM_ht,
        **abonnement_assai_SMAA_ht,
        **abonnement_assai_SMEAM_ttc,
        **abonnement_assai_SMAA_ttc,
        **conso_assai_smeam_pu,
        **conso_assai_smaa_pu,
        **conso_assai_smeam_total_ht,
        **conso_assai_smaa_total_ht,
        **conso_assai_smeam_total_ttc,
        **conso_assai_smaa_total_ttc,
        **sous_total_assai_ht,
        **sous_total_assai_ttc,
        **total_general_ht,
        **total_general_ttc,
    }


def clean_data(res):
    df = pd.DataFrame(res)
    df["CR"] = df["montant_total_du"].str.contains("CR")
    df["montant_total_du"] = df["montant_total_du"].str.replace("CR", "")

    # clean data historique consommation
    s = df["historique_consommation"].str.split("\n").apply(pd.Series, 1)
    print(s)
    s.rename(columns={0: "historique_consommation_1", 1: "historique_consommation_2", 2: "historique_consommation_3"}, inplace=True)
    df = df.join(s)

    df[["historique_consommation_1_date", "historique_consommation_1_valeur"]] = df.historique_consommation_1.str.split(expand=True)
    df[["historique_consommation_2_date", "historique_consommation_2_valeur"]] = df.historique_consommation_2.str.split(expand=True)
    df[["historique_consommation_3_date", "historique_consommation_3_valeur"]] = df.historique_consommation_3.str.split(expand=True)

    del df["historique_consommation_1"]
    del df["historique_consommation_2"]
    del df["historique_consommation_3"]

    # clean consommation tranche
    s = df["consommation_tranche"].str.split("\n").apply(pd.Series, 1)
    s.rename(columns={0: "consommation_tranche_1", 1: "consommation_tranche_2", 2: "consommation_tranche_3"}, inplace=True)

    df = df.join(s)
    del df["consommation_tranche"]
    df = df.fillna(0)
    return df
